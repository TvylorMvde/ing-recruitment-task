Feature: Cookies Test

    Background:
        Given the "cookiePolicyGDPR" cookie is removed
        And I open the "https://ing.pl" page

    Scenario: Set analytical cookies
        When I click on the "Dostosuj" button on the cookie policy modal
        And I click on the "Cookies analityczne" checkbox on the cookie policy modal
        And I click on the "Zaakceptuj wybrane" button on the cookie policy modal
        Then the "cookiePolicyGDPR" cookie value is set to "3"
