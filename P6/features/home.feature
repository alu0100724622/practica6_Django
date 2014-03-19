Feature: Rocking with lettuce and django

    Scenario: Simple Hello World
        Given I access the url "/home.html"
        Then I see the header "This is the home!"

    Scenario: Simple Hello World
        Given I access the url "/help.html"
        Then I see the header "This is the help!"


    Scenario: Simple Hello World
        Given I access the url "/about.html"
        Then I see the header "This is the about!"


