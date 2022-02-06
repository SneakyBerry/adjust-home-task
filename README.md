# adjust-home-task
### Usage:
```bash
python manage.py migrate
python manage.py import_data dataset.csv
python manage.py runserver
```

### Examples

[Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.](http://127.0.0.1:8000/adjust?date_before=2017-06-01&group=channel&group=country&order=-clicks)

[Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.](http://127.0.0.1:8000/adjust?os=ios&date_after=2017-05-01&date_before=2017-05-31&group=date&order=date)

[Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.](http://127.0.0.1:8000/adjust?country=US&date_after=2017-06-01&date_before=2017-06-01&group=os&order=-revenue)

[Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.](http://127.0.0.1:8000/adjust?country=CA&group=channel&order=-cpi)


### Farther improvements:
* Run in docker for easier deployment
* Use gunicorn for more stability under load
* Add linters like mypy, black, isort, flake8
