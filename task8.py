#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: white;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("x")


if plate_no == "HH02EP15Z3":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#3399ff;" >HH02EP15Z3 number details</h1>')
    print('''<pre>
    Registration Name : ankush shukla 
    License No : 12345678910
    Make / Model : Renault / kwid
    Registration Date : 1/1/2017
    Registering Authority : UTTAR PRADESH , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "HR26DK8337":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#00e6ac;" >HR26DD4890 Number Details</h1>')
    print('''<pre>
    Registration Name : kshitij Rastogi
    License No : 10987654321
    Make / Model : maruti suzuki / dezire
    Registration Date : 1/1/2019
    Registering Authority : UTTAR PRADESH, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")


else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
