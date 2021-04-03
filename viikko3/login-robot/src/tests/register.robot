*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
  Input Register Command
  Input Credentials  ptuomola  test1234
  Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
  Create User  ptuomola  test1234
  Input Register Command
  Input Credentials  ptuomola  test1234
  Output Should Contain  User with username ptuomola already exists

Register With Too Short Username And Valid Password
  Input Register Command
  Input Credentials  pt  test1234
  Output Should Contain  Username pt is too short

Register With Valid Username And Too Short Password
  Input Register Command
  Input Credentials  ptuomola  test123
  Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
  Input Register Command
  Input Credentials  ptuomola  testabcd
  Output Should Contain  Password may not contain only letters

Register With Invalid Username And Valid Password
  Input Register Command
  Input Credentials  ptuo123mola  testabcd
  Output Should Contain  Username should only contain letters
