# Online VIN decoder - another python client

This is another example of python client for VinLink online decoder (HTTP service instead of SOAP service).

You need to create an account at www.vinlink.com

It's necessary to add some money for production use of service however you may apply for free funds for tests.

Please provide real credentials in main.py
```
auth=HTTPDigestAuth('login', 'password')
```
You may decode a sample VIN
```
python main.py 1FMCU04112KA71263
```
```
Model Year = 2002
Make = Ford
Model = Escape
Trim Level = XLT
Body Type = 4 Door Wagon
Manufacturer = Ford Motor Company
Production Seq. Number = A71263
Engine Type = V6, 3.0L; DOHC 24V; SEFI
Engine Manufacturer = Ford
Fuel Type = Gasoline
Horsepower = 201HP
Engine Code = 1
Drive Line Type = 4WD
Vehicle Type = Multipurpose Vehicle (MPV)
Vehicle Class = Small MPV
Brake System = Hydraulic
Restraint System = Side Air Bag; Air Bag-2nd Generation
Country = UNITED STATES
Assy. Plant = Kansas City: Claycomo, MO
GVWR Class = Class C: 4,001-5,000 lb
Tonnage = 1/2
Check Digit = 1
MPG = A4:16-22-18
AAIA = 11771/69955
AAIA_ENGINE = 8026
AAIA_LEGACY = 1385276
AAIA_TRANSMISSION = 742/2452
AAIA_VehicleID = 11771/11771/11771/11771
AAIA_EngineConfigID = 8026/8026/8026/8026
AAIA_TransmissionID = 742/2452/742/2452
AAIA_BodyStyleConfigID = 9/9/9/9
AAIA_BrakeConfigID = 9/9/9/9
AAIA_DriveTypeID = 8/8/5/5
AAIA_SpringTypeConfigID = 1/1/1/1
Curb weight = 3364
Gross vehicle weight rating = 4520
Wheelbase = 103.1
Overall length = 173
Overall height = 69.1
Overall width = 70.1
Warranty whole vehicle Months = 36
Warranty whole vehicle Miles = 36000
Warranty powertrain Months = 36
Warranty powertrain Miles = 36000
Warranty anti-corrosion Months = 60
Warranty anti-corrosion Miles = 999999
Warranty roadside assistance Months = 36
Warranty roadside assistance Miles = 36000
MSRP = 24000-26000
```
