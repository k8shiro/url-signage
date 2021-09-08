import sys
import os
import argparse
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--display', help='Display number', default=':0.0')
    parser.add_argument('-i', '--interval', help='Interval of page transfer (seconds) ', type=int, default='60')
    parser.add_argument('-u', '--urls_file', help='URL list file path', default='./urls.txt')
    parser.add_argument('-s', '--scroll_speed', help='Page scroll speed (min 1)', type=int, default='1')
    args = parser.parse_args()

    print("Display number: {}".format(args.display))
    print("Interval of page transfer (seconds): {}".format(args.interval))
    print("URL list file path: {}".format(args.urls_file))
    if args.scroll_speed < 1:
        args.scroll_speed = 1
    print("Page scroll speed (min 1): {}".format(args.scroll_speed))

    return args.display, args.interval, args.urls_file, args.scroll_speed

def load_urls_file(urls_file):
    urls = []
    with open(urls_file, 'r') as f:
        urls = f.readlines()
    return urls

def flush_progress_bar(barname, rate):
    bar_num = int(rate/0.05)+1
    bar = ('#' * bar_num).ljust(20, '-')
    sys.stdout.write(f"\r{barname} : [{bar}] {rate*100:.2f}%")

def run_signage(display, interval, scroll_speed, urls):
    os.environ['DISPLAY'] = display
    driver = webdriver.Chrome()
    for url in urls:
        print('Open URL: {}'.format(url))
        driver.get(url)
        time.sleep(interval)
        height = driver.execute_script('return document.body.scrollHeight')
        for h in tqdm(range(1, height, scroll_speed)):
            driver.execute_script("window.scrollTo(0, {});".format(h))
    driver.close()


if __name__ == "__main__":
    display, interval, urls_file, scroll_speed = get_args()
    urls = load_urls_file(urls_file)
    while True:
        run_signage(display, interval, scroll_speed, urls)





