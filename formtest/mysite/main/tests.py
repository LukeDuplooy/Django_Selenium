from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class CarFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/')
    #find the elements you need to submit form
    car_name = selenium.find_element_by_id('id_name')
    car_year = selenium.find_element_by_id('id_year')
    car_hp = selenium.find_element_by_id('id_hp')
    car_topSpeed = selenium.find_element_by_id('id_top_speed_mph')
    car_weight = selenium.find_element_by_id('id_weight_kg')

    submit = selenium.find_element_by_id('submit_button')

    #populate the form with data

    car_name.send_keys('Ferrari 488')
    car_year.send_keys('2015')
    car_hp.send_keys('530')
    car_topSpeed.send_keys('224')
    car_weight.send_keys('1500')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Ferrari 488' in selenium.page_source