from selenium import webdriver
from time import sleep

class YouTubeVideoDownloader:
    
    def __init__(self, ytube_video_link):
        self.ytube_video_link = ytube_video_link
        self.driver = webdriver.Chrome('C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.driver.get('https://www.y2mate.com/en19')
        self.ytube_video_link_input = self.driver.find_element_by_xpath('//*[@id="txt-url"]')
        self.ytube_video_link_input.send_keys(self.ytube_video_link)
        self.start_btn = self.driver.find_element_by_xpath('//*[@id="btn-submit"]')
        self.start_btn.click()
        sleep(4)        
        self.quality_selector_table_body = self.driver.find_element_by_xpath('//*[@id="mp4"]/table/tbody')
        self.available_video_qualities = self.quality_selector_table_body.find_elements_by_tag_name('a')
        self.available_video_qualities = [quality.text for quality in self.available_video_qualities if quality.text != '' and quality.text != '  Download']
        self.available_video_qualities.pop()
    
    def download_video(self, quality):
        download_btn = self.driver.find_element_by_xpath(f'//*[@id="mp4"]/table/tbody/tr[{quality}]/td[3]/a')
        download_btn.click()
        # sleep(4)
        # real_download

if __name__ == '__main__':
    downloader = YouTubeVideoDownloader('https://www.youtube.com/watch?v=rUWxSEwctFU')
    print('Choose the Video Quality From the available video qualities...')
    for i, quality in enumerate(downloader.available_video_qualities, 1):
        print(i, quality)
    quality = int(input(f'Ex. Select 1 for {downloader.available_video_qualities[0]}\n'))
    downloader.download_video(quality)    