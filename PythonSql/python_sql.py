import psycopg2


hostname= "localhost"
database= "Demo"
username= "postgres"
pwd = 'system'
port_id = 5432

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user=username,
        password= pwd,
        port=port_id
    )   #step 1  crete connection to database
    
    cur = conn.cursor() #step 2 create a cursor to do the crud operations 

    cur.execute('drop table if exists employee') # step 5 drop table otherwise duplicate values will be inserted



    create_script = '''create table if not exists employee( 
    id int primary key,
    name varchar(40),
    salary int,
    dept_id varchar(30)
    )'''   
    cur.execute(create_script)  #step 3 creat the table if not exists

    insert_script = '''insert into employee (id,name,salary,dept_id) values (%s,%s,%s,%s)'''
    insert_values = [(1,"varsha",800000,"data analytics1"),(2,"meghu",1000000,"data engineer1"),(3,"runia",1500000,"data scientist")]
    for v in insert_values:
        cur.execute(insert_script,v) # step 4 insert multiple recods into the table

    update_script = 'update employee set salary = salary + (0.5*salary)'
    cur.execute(update_script)

    delete_script = 'delete from employee where name = %s '
    delete_value = ('runia',)
    cur.execute(delete_script,delete_value)

    cur.execute('select * from employee')
    print(cur.fetchall())

    #show me all nthe names
    for records in cur.fetchall():
        print(records[1])

    conn.commit()




    cur.close()





    conn.close()
except Exception as error:
    print(error)