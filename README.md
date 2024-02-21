# GazpromTest
### ENG
#### General info
**Attention!**
Project has been setup and tested on localhost. Make shure to adjust parameters in the compose.yaml if you want to deploy the app on the actual server. Also make sure to use actual username and password.

App uses FastAPI and PostgreSQL stack.
Database can be accessed from HOST:/8080 through Adminer interface.
db-name: device_data_db
username: postgres
password: device_data_db_passwd

Or by url:
postgresql://postgres:device_data_db_passwd@db:5432/device_data_db

Database operations in the code performed with use of SQLAlchemy ORM.
#### Functionality
The app is used to store and analyze data recieved from some kind of device. Device have to be registered in the database, that can be achieved by sending POST method to the HOST:/device/. ID will be assigned to the device and should be used by it in the future to send the data.
Recieved Data contains 3 values: x: float, y: float, z: float.
Statistic can be accessed on HOST:/statistic/ with parameters:
- device_id:int - observed device's statistic
- max_value:bool - whether max values will be calculated
- min_value:bool - whether min values will be calculated
- median:bool - whether medians will be calculated
- sum:bool - whether values sums will be calculated
- count:bool - whether data will be counted

More info about the methods can be found here: HOST:/docs/