from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Lolik_13721@127.0.0.1:3306/houses", echo=True)

def get_connection():
    user = 'root'
    password = "Lolik_13721"
    host = '127.0.0.1'
    port = 3306
    database = "houses"
    try:
        eng = create_engine(
            url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
                user, password, host, port, database
            ),
            pool_pre_ping=True,
            echo=True
        )
        return engine
    except Exception as why:
        raise Exception('Error while connecting to DataBase')

engine = get_connection()
print("Engine okay: ", engine)

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

meta = MetaData()
print("MetaDtaa okay: ", meta)
homes = Table(
    'homes', meta,
    Column('id', Integer, primary_key = True),
    Column('Country', String(16)),
    Column('Region', String(16)),
    Column('City', String(16)),
    Column('Street', String(16)),
    Column('Building', String(16)),
    Column('Apartment', Integer),
    Column('Floor', Integer),
    Column('Type', Integer),
    Column('ImgPath', String(32))
)

#print("homes okay: ", homes)
meta.create_all(engine)
import requests
houses_web = "https://www.realtor.com/"
resp = requests.get(houses_web, verify=False)
print(resp.status_code)

from sqlalchemy import table
from sqlalchemy import insert

def addNewLineToHomesTable(engine, table, country, region, city, street, building, apartment, floor):
    print(type(table))
    statement1 = homes.insert().values(Country=country,Region=region,City=city,Street=street,Building=building,Apartment=apartment,Floor=floor)
    result = engine.execute(statement1)

def getLines(engine, homes, SearchBy, Value):
    import sqlalchemy as db

    engine = db.create_engine("mysql+pymysql://root:Lolik_13721@127.0.0.1:3306/houses")
    connection = engine.connect()
    metadata = db.MetaData()
    hs = db.Table('homes', metadata, autoload=True, autoload_with=engine)
    result_proxy = connection.execute("Select * from homes where " + SearchBy + "= '" + Value + "'")
    result_set = result_proxy.fetchall()
    for line in result_set:
        print(line)


from tkinter import *
from tkinter.ttk import *

def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("House")
    newWindow.geometry("200x200")
    Label(newWindow, text="New").pack()

def insertgui():
    newWindow = Toplevel(master)
    newWindow.title("Insert")
    newWindow.geometry("500x500")

    countryText = Text(newWindow, width=2, height=3, background="gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
    countryText.insert(INSERT, "country")
    countryText.pack(expand=1, fill=BOTH)

    regionText = Text(newWindow, width=2, height=3, background="gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
    regionText.insert(INSERT, "region")
    regionText.pack(expand=1, fill=BOTH)

    cityText = Text(newWindow, width=2, height=3, background="gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
    cityText.insert(INSERT, "city")
    cityText.pack(expand=1, fill=BOTH)

    streetText = Text(newWindow, width=2, height=3, background="gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
    streetText.insert(INSERT, "street")
    streetText.pack(expand=1, fill=BOTH)

    buildingText = Text(newWindow, width=2, height=3, background="gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
    buildingText.insert(INSERT, "building")
    buildingText.pack(expand=1, fill=BOTH)

    apartmentText = Text(newWindow, width=2, height=3, background="gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
    apartmentText.insert(INSERT, "apartment")
    apartmentText.pack(expand=1, fill=BOTH)

    floorText = Text(newWindow, width=2, height=3, background="gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
    floorText.insert(INSERT, "floor")
    floorText.pack(expand=1, fill=BOTH)

    def getValues():
        cntry = countryText.get("1.0", "end-1c").upper()
        reg = regionText.get("1.0", "end-1c").upper()
        cit = cityText.get("1.0", "end-1c")
        st = streetText.get("1.0", "end-1c")
        bld = buildingText.get("1.0", "end-1c")
        ap = apartmentText.get("1.0", "end-1c")
        fl = floorText.get("1.0", "end-1c")
        # TODO: 3rd party for checking address
        # TODO: here can be checks for validation values
        print(cntry)

        addNewLineToHomesTable(engine, homes, cntry, reg, cit, st, bld, ap, fl)

    btn = Button(newWindow, text="Save", command=getValues)
    btn.pack(pady=10)

def searchgui():
    newWindow = Toplevel(master)
    newWindow.title("Search")
    newWindow.geometry("500x500")

    OPTIONS = [
        "SearchBy",
        "Country",
        "Region",
        "City",
        "Street"
    ]
    variable = StringVar(newWindow)
    variable.set(OPTIONS[0])
    w = OptionMenu(newWindow, variable, *OPTIONS)
    w.pack()

    valueText = Text(newWindow, width=50, height=5, background="gray71", foreground="#fff", font=('Sans Serif', 13, 'italic bold'))
    valueText.insert(INSERT, "value")
    valueText.pack(expand=True)

    def getSearchResult():
        v = valueText.get("1.0", "end-1c")
        getLines(engine, homes, str(variable.get()), v)

    btn = Button(newWindow, text="Search", command=getSearchResult)
    btn.pack(pady=10)

def mainWin():
    master.title("House")
    master.geometry("500x500")
    label = Label(master)
    label.pack(pady=10)
    btn = Button(master, text="Insert", command=insertgui)
    btn.pack(pady=10)
    btn = Button(master, text="Search", command=searchgui)
    btn.pack(pady=10)
    mainloop()

master = Tk()
mainWin()