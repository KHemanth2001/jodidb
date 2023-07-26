# JODI Data Downloader

This Python script utilizes the Selenium library to download a dataset from the website [http://www.jodidb.org/TableViewer/tableView.aspx?ReportId=93906](http://www.jodidb.org/TableViewer/tableView.aspx?ReportId=93906). The website provides access to the Joint Organizations Data Initiative (JODI) World Oil Database, containing information about global oil production and consumption.

## Prerequisites

1. Python 3.x installed on your system.
2. Install required packages by running `pip install selenium` and `pip install pandas`.

## Webdriver Setup

1. Download the appropriate WebDriver for your browser:
   - Chrome: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

2. Place the WebDriver executable in the same directory as the Python script.

## PostgreSQL Setup

1. Install PostgreSQL on your system and set up a database.
2. Modify the database connection parameters in the script `jodi_data_downloader.py`:

```python
DATABASE_CONFIG = {
    'database': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}
```

Replace the placeholders with your actual PostgreSQL database configuration.

## Running the Script

Run the Python script `jodi_data_downloader.py`:

```bash
python jodi_data_downloader.py
```

The script will use Selenium to navigate to the [http://www.jodidb.org/TableViewer/tableView.aspx?ReportId=93906](http://www.jodidb.org/TableViewer/tableView.aspx?ReportId=93906) website, download the dataset in CSV format, and store the CSV file in the same directory as the script. Then, it will load the data from the CSV file and insert it into the specified PostgreSQL database table.

## Important Notes

- Ensure that you have the necessary permissions to access and download data from the website.
- Always comply with the terms of service and usage policies of the website.
- Use this script responsibly and avoid causing any load or strain on the website's server and database.

Feel free to explore and modify the script according to your specific requirements for downloading, handling, and storing JODI oil data. Happy coding!
