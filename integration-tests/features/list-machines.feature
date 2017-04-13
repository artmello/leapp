Feature: Listing details of local virtual machines

Scenario: Machine listing responsiveness
   Given the local virtual machines:
         | name       | definition          | ensure_fresh |
         | vm1        | centos6-guest-httpd | no           |
         | vm2        | centos7-target      | no           |
   Then a shallow machine listing should take less than 15 seconds
    and a full machine listing should take less than 30 seconds
