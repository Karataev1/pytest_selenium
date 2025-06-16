from selenium.webdriver.common.by import By


class TextInputSelectors:

    input_text_line =           (By.ID, 'id_text_string')
    result =                    (By.ID, 'result-text')
    error_message =             (By.ID, 'error_1_id_text_string')
    email_input_line =          (By.ID, 'id_email')
    email_error_message =       (By.ID, 'error_1_id_email')
    password_input_line =       (By.ID, 'id_password')
    password_error_message =    (By.ID, 'error_1_id_password')
