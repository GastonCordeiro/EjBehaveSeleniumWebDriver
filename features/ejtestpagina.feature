Feature: "Check the page works"
    @TEST
    Scenario: find the dress size M
        Given a browser
        When I enter the url http://automationpractice.com/index.php
        When I click on a Woman
        When I click on Dresses
        #When I click on Size M
        When I find class product dresses
        When I find SIZE click in M

        Then I will find the dress size M

    @TEST
    Scenario: Buy a Dress
        Given I am on url http://automationpractice.com/index.php?id_product=3&controller=product#/color-orange/size-m
        When I click on Submit
        When Proceed to checkout
        Then Check url

