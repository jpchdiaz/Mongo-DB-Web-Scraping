import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime


# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


# Function to scrape for weather in Cost Rica
def scrape_weather():

    # Initialize browser
    browser = init_browser()

    # Visit the Costa Rica climate site
    url = "https://weather-and-climate.com/average-monthly-Rainfall-Temperature-Sunshine-fahrenheit,san-jose,Costa-Rica"
    browser.visit(url)
    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find today's forecast
    forecast_today = soup.find("div", class_="weather-forecasts todays-weather forecast")
    forecast_today

    # Get the max temp
    max_temp = forecast_today.find("span", class_="temp-max").text
    # Print the min temp
    min_temp = forecast_today.find("span", class_="temp-min").text
    # Get current time stamp
    time_stamp = str(datetime.now())

    # Store in dictionary
    weather = {"Max Temp": max_temp, "Min Temp": min_temp, "Time Stamp": time_stamp}

    # Return results
    return weather


# Function to scrape surf info
def scrape_surf():

    # Initialize browser
    browser = init_browser()

    # Visit Costa Rica surf site
    url = "https://www.surfline.com/surf-reports-forecasts-cams/costa-rica/3624060"

    # Scrape page into soup

    # Find today's surf conditions

    # Store in dictionary

    # Return results
    return surf
