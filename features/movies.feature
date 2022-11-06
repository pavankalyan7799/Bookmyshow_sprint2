Feature:Book_my_show
  Background:   click on location icon
    Given  launch chrome browser
    When open bookmyshow home page and click on location
    Then User must be able to click on location
    Then User must be able to click on movietheater
    Then user must be able to click on seats
    Then user must be able to click on seat positions

  Scenario Outline:
    When User is able to enter email "<email>"
    And  User is able to enter mobilenumber "<mobilenumber>"
    And User is able to click on submit button
    And User is able to enter the usercardnumber "<cardnumber>"
    Then User is able to enter cardname "<cardname>"
    And User is able to enter cardexpirymonth "<expmonth>"
    And User is able to enter cardexpiryyear "<expyear>"
    Then User is able to enter cardcvv "<cvv>"
    And User is able to click on make the payment
    Then close the browser


    Examples:
    | email                 |  |mobilenumber |  |cardnumber          | |cardname | |expmonth | |expyear | |cvv |
    | pavankalyan@gmail.com |   |8639461234  |  |0123 4567 8912 4567 |  |pavankalyan | |07 |    |20|   |123|
    | suvarna@gmail.com     |   |9353781139  |  |1234 4567 suva 2345 |  |suvarna    |  |08 |    |21|   |456|
    |suvarna                |   |9876543210  |  |1234 2345 3456 5678 |   |pk        |  | 09 |    |22|   |789|
    |pk123@gmail.com        |   |abcdefghij  |  |1234 4567 7892 3456 |   |pavan     |  | 11 |    |98|   |025|
    |sohel@gmail.com        |   |9876543210  |  |abcd efgh ijkl mnop |   |mestri    |  | 01 |    |20|   |024|