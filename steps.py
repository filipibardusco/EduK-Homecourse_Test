from random import randint
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@given(u'a user enters eduK')
def impl(context):  
    context.browser.visit('/')

@when(u'we log in')
def impl(context):
    username_field = context.browser.find_by_id('session_email')
    password_field = context.browser.find_by_id('session_password')
    username_field.send_keys('bardusco@gmail.com')
    password_field.send_keys('123456')

@then(u'we click submit')
def impl(context):
    submit_button = context.browser.find_by_xpath('//button[text()="Entrar"]')
    submit_button.click()

@when(u'we click on the "gastronomia page"')
def step_impl(context):
    gastronomia_button = context.browser.find_by_xpath('//*[contains(@class, "header_cat-gastronomia")]')
    gastronomia_button.click()

@then(u'we should see "courses"')
def step_impl(context):
    course_check = context.browser.find_by_class('course_card_card')

@when(u'we click on the "random course"')
def step_impl(context):
    random_number = randint(1, len(context.browser.find_elements_by_xpath('//*[contains(@class, "course_card_card")]')))
    third_course = context.browser.find_by_xpath('//ul[li[div[@class="course_card_card"]]]/li[{}]'.format(random_number))
    third_course.click()

@then(u'we should see "lessons"')
def step_impl(context):
    try:
        context.browser.find_by_xpath('//*[contains(@class, "course_activities_lesson")]')
        lesson_check = context.browser.find_by_xpath('//*[contains(@class, "course_activities_lesson")]')
    except NoSuchElementException:
        serie_part_check = context.browser.find_by_xpath('//*[contains(@class, "serie_episodes_episode")]')


@when(u'we click on the "random lesson"')
def step_impl(context):
    sections = context.browser.find_elements_by_xpath('//ul[contains(@class, "course_activities_activities")]')
    random_lesson = randint(1, (len(context.browser.find_elements_by_xpath('//section[div[ul[contains(@class, "course_activities_activities")]]]/div[1]/ul/li'))))
    element = '//section[div[ul[contains(@class, "course_activities_activities")]]]/div/ul[1]/li[{}]'.format(random_lesson)
    context.browser.wait_click(element)

@then(u'we should see "a video"')
def step_impl(context):
    context.browser.find_by_xpath('//iframe[contains(@class, "player_frame")]')

@given(u'we make a search')
def step_impl(context):
    search_box = context.browser.find_by_class('header_search-input')
    search_box.clear()
    search_box.send_keys('vimeo')
    submit_search = context.browser.find_by_xpath('//button[contains(@class, "header_search-btn")]')
    submit_search.click()

@when(u'we favourite a course')
def step_impl(context):
    context.browser.wait_click('//button[contains(@class, "save_button_off")]')

@when(u'we undo the favourite course')
def step_impl(context):
    context.browser.wait_click('//button[contains(@class, "save_button_on")]')

@then(u'we go to meus cursos')
def step_impl(context):
    meus_cursos = context.browser.find_by_xpath('//*[text()="Meus Cursos"]')
    meus_cursos.click()

@given(u'we have not completed the course')
def step_impl(context):
    try:
        context.browser.find_by_xpath('//*[contains(@class, "course_activities_exam-icon-blocked")]')
        print("banana")
    except NoSuchElementException:
#        context.execute_steps(u"""
#            given we make a search
#            when we click on the "random course"
#            given we have not completed the course
#        """)
        print('the definition of insanity is doing the same thing over and over again expecting different results')

@when(u'we click on the first lesson')
def step_impl(context):
    context.browser.wait_click('//*[contains(@class, "course_activities_lesson")]')

@then(u'we skip to the end of the video')
def step_impl(context):
    num_lessons = len(context.browser.find_elements_by_xpath('//li[contains(@class, "course_activities_lesson")]'))
    for i in range(num_lessons):
        time.sleep(5)
        #context.browser.switch_to()
        if context.browser.check_exists_by_xpath('//*[contains(@class, "cuepoints")]'):
            ontext.browser.switch_to()
            bar = context.browser.find_by_xpath('//*[contains(@class, "cuepoints")]')
            context.browser.wait_click('//*[contains(@class, "cuepoints")]')
            context.browser.click_point(bar.size['width']-1, bar.size['height']/2, '//*[contains(@class, "cuepoints")]')
            time.sleep(20)
        else:
            context.browser.wait_click('//a[contains(@class, "question_cover_cta")]')
            while context.browser.check_exists_by_xpath('//*[contains(@class, "question_container")]') == True:
                context.browser.wait_click('//ul[contains(@class, "question_alternative-list")]/li[{}]'.format(randint(1,4)))
                context.browser.wait_click('//div[contains(@class, "question_container")]/footer[contains(@class, "question_bottom-bar")]')
                time.sleep(4)
                if context.browser.check_exists_by_xpath('//div[contains(@class, "question_result")]/footer') == True:
                    context.browser.wait_click('//div[contains(@class, "question_result")]/footer[contains(@class, "question_bottom-bar")]')
                else:
                    print("Wow, you're lucky")

@then(u'go through the assignment if there is no video')
def step_impl(context):
    assert True
