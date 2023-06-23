
from datetime import datetime
from dependencies.scraping.scraper import Scrapper
from dependencies.cleaning.cleaning import clean_data
from dependencies.geocoding.geocoder import geocode_csv
from dependencies.standardization.standardizer import *

def step_1():
    filename = input("Enter csv file name : ")
    writer, file = open_file(filename)
    Scrapper(writer)
    closefile(file)


def step_2():
    clean_data()


def step_3():
    geocode_csv()

class Main:
    filename = input("Enter csv file name : ")
    writer,file=open_file(filename)
    Scrapper(writer)
    closefile(file)
    t=True
    while(t):
        print("1-->Scrapping Meta Data\n2-->Cleaned Main Data\n3-->Geocoded Cleaned Data")
        stepnum = int(input("Enter step to go :"))
        eval(f"step_{stepnum}()")


