# Order Tracker

Creating this project for these reasons

- Knowledge
- Practice
- Anxiety with my order from a website without any e-mail alerts or automated tracking
- Fun

## Description

Using [Selenium with Python](https://selenium-python.readthedocs.io/), I want to build an automated tracker for an website who I order my new notebook and doesn't have any kind of alert about order updates. _And I have anxiety with this_. I'm gonna also update tech skills by sending e-mails with the updated, dockerize the project and deploying the whole project (in a free resource). Also, I'm gonna try achieve schedule the times when I should access the website and make updates.

## Techs for this project

- [Python](https://www.python.org/)
- [Pip-tools](https://pip-tools.readthedocs.io/en/latest/)
- [Selenium with Python](https://selenium-python.readthedocs.io/)
- [Docker](https://www.docker.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Schedule](https://schedule.readthedocs.io/en/stable/)
- [Mailgun](https://www.mailgun.com/solutions/use-cases/services/email-service-provider/free-email-sending-service/)

## Features

- [x] Crawl the status from the order page
  - [x] Login in the website
  - [x] Access the order
  - [x] Get the latest update
  - [x] Save the latest update
    - [x] Add sqlite
    - [x] Add model
    - [x] Integrate
- [x] Send an email if there is any changes on the update
- [x] Schedule the running for at least two times in the day (e.g 10 AM and 6 PM)
- [x] Deploy the dockerized application
