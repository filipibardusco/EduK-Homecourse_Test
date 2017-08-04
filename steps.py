from random import randint

@given(u'a user enters eduK')
def impl(context):  
    context.browser.visit('/')

@when(u'we log in')
def impl(context):
    username_field = context.browser.find_by_id('session_email')
    password_field = context.browser.find_by_id('session_password')
    username_field.send_keys('eduk001@bardusco.com')
    password_field.send_keys('123456')

@then(u'we click submit')
def impl(context):
    submit_button = context.browser.find_by_xpath('//*[@id="new_session"]/div[5]/button')
    submit_button.click()

@when(u'we click on the "gastronomia page"')
def step_impl(context):
    gastronomia_button = context.browser.find_by_xpath('//*[@id="appRoot"]/div/div/div[1]/header/div[2]/ul/li[3]/a')
    gastronomia_button.click()

@then(u'we should see "courses"')
def step_impl(context):
    course_check = context.browser.find_by_class('course_card_card')

@when(u'we click on the "random course"')
def step_impl(context):
    random_number = randint(1, len(context.browser.find_elements_by_xpath('//*[@id="appRoot"]/div/div/section/ul/li')))
    third_course = context.browser.find_by_xpath('//*[@id="appRoot"]/div/div/section/ul/li[{}]/div'.format(random_number))
    third_course.click()

@then(u'we should see "lessons"')
def step_impl(context):
    lesson_check = context.browser.find_by_xpath('//*[@id="appRoot"]/div/div/div[2]/div[2]/div[2]/section[1]/div[1]/ul/li[2]/a/span')

@when(u'we click on the "random lesson"')
def step_impl(context):
    random_number = randint(1, len(context.browser.find_elements_by_xpath('//*[@id="appRoot"]/div/div/div[2]/div[2]/div[2]/section[1]/div[1]/ul/li')))
    second_lesson = context.browser.find_by_xpath('//*[@id="appRoot"]/div/div/div[2]/div[2]/div[2]/section[1]/div[1]/ul/li[{}]/a/span'.format(random_number))
    second_lesson.click()

@then(u'we should see "a video"')
def step_impl(context):
    video = context.browser.find_by_xpath('//*[@id="appRoot"]/div/div/div[2]/div[1]/section/iframe')

@given(u'we make a search')
def step_impl(context):
    search_box = context.browser.find_by_class('header_search-input')
    search_box.send_keys('batatas')
    submit_search = context.browser.find_by_xpath('//*[@id="appRoot"]/div/div/div/header/div[1]/div[1]/form/button')
    submit_search.click()
