*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go And Check Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ptuomola
    Set Password  test1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pt
    Set Password  test1234
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  ptuomola
    Set Password  test213
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  ptuomola
    Set PasswordOnly  test1234
    Set PasswordConfirmation  test3214
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  testuser
    Set Password  test1234
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  testuser
    Set PasswordOnly  test1234
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  test1234
    Set Password  test1234
    Submit Credentials
    Register Should Fail With Message  Username must contain lowercase letters only
    Go To Login Page
    Set Username  test1234
    Set PasswordOnly  test1234
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Go And Check Register Page
    Go To Register Page
    Register Page Should Be Open

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Set PasswordOnly
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Login Should Succeed
    Main Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}