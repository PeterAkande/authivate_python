## Authivate (Python SDK)

This is the official python package for the [Authivate](https://authivate.com) service.

Authivate is an easy-to-use User Authentication and Management service.

### Install
To Install, using pip
```sh
pip install authivate
```

Using poetry
```shell
poetry add authivate
```

### Example Usage

```python
from authivate import  Authivate, AuthivateConfig
from pprint import pprint


def signup_user(authivate: Authivate):
    # Sign up a user
    sign_up_response = authivate.sign_up_user(
        email_address="user@example.com",
        last_name="Doe",
        first_name="John",
        password="password"
    )
    if sign_up_response.was_successful:
        print("User signed up successfully.")
        print(sign_up_response.json_data)
    else:
        print(f"Error: {sign_up_response.status_code} - {sign_up_response.json_data}")


def signin_user(authivate: Authivate):
    # Signs In a User
    sign_in_response = authivate.sign_in_user(
        email_address="user@example.com",
        password="password"
    )
    if sign_in_response.was_successful:
        print("User signed in successfully.")
        pprint(sign_in_response.json_data)
    else:
        print(f"Error: {sign_in_response.status_code} - {sign_in_response.json_data}")


def request_confirm_account_email(authivate: Authivate):
    # Request OTP for a user
    request_otp_response = authivate.request_otp_for_user(
        email_address="user@example.com"
    )
    if request_otp_response.was_successful:
        print("OTP request successful.")
        pprint(request_otp_response.json_data)
    else:
        print(f"Error: {request_otp_response.status_code} - {request_otp_response.json_data}")


def request_forgot_password_email(authivate: Authivate):
    # Example: Request a forgot password email for a user
    forgot_password_response = authivate.request_forgot_password_for_user(
        email_address="user@example.com"
    )
    if forgot_password_response.was_successful:
        print("Forgot password email request successful.")
        pprint(forgot_password_response.json_data)
    else:
        print(f"Error: {forgot_password_response.status_code} - {forgot_password_response.json_data}")


# Initialize AuthivateConfig
authivate_config = AuthivateConfig(api_key="your-api-key", project_id="project-id")


# Create an instance of Authivate
authivate_instance = Authivate(config=authivate_config)

# Sign up the user to the project
'''Response
{'message': 'Email Sent!',
 'user_record': {'email_address': 'user@example.com',
                 'is_verified': False,
                'date_created': '2023-11-11T22:59:46.636726Z',
                 'first_name': 'John',
                'last_name': 'Doe',
                 'user_unique_id': 'lrucu.pxpmleelxcxeme'
                 }
 }
 '''
signup_user(authivate_instance)

# Signs In a user to the project
'''
Response is:
{'user_record': {'date_created': '2023-11-11T22:59:46.636726Z',
             'email_address': 'user@example.com',
             'first_name': 'John',
             'is_verified': False,
             'last_name': 'Doe',
             'user_unique_id': 'lrucu.pxpmleelxcxeme'}}
'''
signin_user(authivate_instance)

# Send a confirm email mail if the original one has expired
'''
Response
{'message': 'Email Sent Successfully'}
'''
request_confirm_account_email(authivate_instance)

# Send a forgot password email if the original one has expired
'''
Response
{'message': 'Forgot Password Email Sent!'}
'''
request_forgot_password_email(authivate_instance)
```