from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from xlsxwriter import Workbook
import os
import requests
import shutil


class InstaScrap:
    def __init__(self,
                 username = 'tuusuario',
                 password = 'tucontraseña',
                 target_username ='perfildestino'
                 ):

        self.username = username
        self.password = password
        self.target_username = target_username
        self.path = path = target_username
        self.driver = webdriver.Firefox()
        self.main_url = 'https://www.instagram.com/'
        self.driver.get(self.main_url)
        sleep(3)
        self.log_in()
        self.open_target_profile()
        if not os.path.exists(path):
            print('Creando Carpeta ' + path)
            os.mkdir(path)
        self.scroll_down()
        self.downloading_images()




    def log_in(self, ):
        try:
            log_in_button = self.driver.find_element_by_link_text('Inicia sesión')
            log_in_button.click()
        except Exception:
            print('No Pude Encontrar El Boton De Inicio')
        else:
            try:
                user_name_input = self.driver.find_element_by_xpath(
                    '//input[@aria-label="Teléfono, usuario o correo electrónico"]')
                user_name_input.send_keys(self.username)
                password_input = self.driver.find_element_by_xpath('//input[@aria-label="Contraseña"]')
                password_input.send_keys(self.password)
                user_name_input.submit()
                sleep(3)
            except Exception:
                print('Algo Ocurrio Al Intentar Encontrar El Campo De Usuario Y Contraseña')

    def scroll_down(self):
        try:
            no_of_posts = self.driver.find_element_by_xpath('//span[text()=" publicaciones"]').text
            no_of_posts = no_of_posts.replace(' publicaciones', '')
            no_of_posts = str(no_of_posts).replace(',', '')
            self.no_of_posts = int(no_of_posts)
            print(no_of_posts)
            if self.no_of_posts > 12:
                no_of_scrolls = int(self.no_of_posts/12) + 3
                try:
                    for value in range(no_of_scrolls):
                        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                        sleep(2)
                except Exception as e:
                    print(e)
                    print('Un Error Ocurrio Mientras Recorria El Perfil')
            sleep(10)
        except Exception:
            print('No Pude Encontras Publicaciones En El Perfil')
            self.error = True


    def open_target_profile(self):
        try:
            target_profile_url = self.main_url + self.target_username + '/'
            self.driver.get(target_profile_url)
            sleep(3)
        except Exception:
            print('No Pude Navegar Al Perfil')

    def write_captions_to_excel_file(self, images, caption_path):
        print('Guardando en Excel')
        workbook = Workbook(os.path.join(caption_path, 'Pie De Foto.xlsx'))
        worksheet = workbook.add_worksheet()
        row = 0
        worksheet.write(row, 0, 'Nombre De Imagen')       # 3 --> row number, column number, value
        worksheet.write(row, 1, 'Pie De Foto')
        row += 1
        for index, image in enumerate(images):
            filename = 'image_' + str(index) + '.jpg'
            try:
                caption = image['alt']
            except KeyError:
                caption = 'No Existe Pie De Foto'
            worksheet.write(row, 0, filename)
            worksheet.write(row, 1, caption)
            row += 1
        workbook.close()

    def download_captions(self, images):
        captions_folder_path = os.path.join(self.path, 'Pie De Foto')
        if not os.path.exists(captions_folder_path):
            os.mkdir(captions_folder_path)
        self.write_captions_to_excel_file(images, captions_folder_path)

    def downloading_images(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        all_images = soup.find_all('img')
        self.download_captions(all_images)
        print('Total De Imagenes ', len(all_images))
        for index, image in enumerate(all_images):
            filename = 'image_' + str(index) + '.jpg'
            image_path = os.path.join(self.path, filename)
            link = image['src']
            print('Descargando Imagen ', index)
            response = requests.get(link, stream=True)
            try:
                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)  # source -  destination
            except Exception as e:
                print(e)
                print('No Pude Bajar La Imagen ', index)
                print('Imagen link -->', link)

    def random_scroll(self):
        import random
        for i in range(10):
            if random.randint(1, 100) % 3 == 0:
                text = 'window.scrollTo(document.body.scrollHeight, 0);'
            elif random.randint(1, 100) % 2 == 0:
                text = 'window.scrollTo(0, document.body.scrollHeight/2);'
            else:
                text = 'window.scrollTo(0, document.body.scrollHeight);'
            self.driver.execute_script(text)
            sleep(2)

if __name__ == '__main__':
    insta = InstaScrap()