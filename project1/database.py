################################################# TO DO #######################################################
# write import statements for psycopg2 and Error from psycopg2 package #

import psycopg2
from psycopg2 import Error


try:
    # connection to database
    print("Connecting...") # DO NOT ALTER OR DELETE
    
    ########################################### TO DO #########################################################

    # CREATE FUNCTION CALLED "GET_CONNECTED" WHICH CREATES CONNECTION WITH PSYCOPG2.CONNECT #
    def get_connected():
    # DEFINE DBNAME, USER, PASSWORD, HOST, AND PORT FROM HEROKU POSTGRES CREDENTIALS # 
        connection = psycopg2.connect(

            dbname = "d8s7bv7re9at91",
            user = "oibwblyvydurxa",
            password = "b46346bca6cf70b6cdd85c6e0ce415a360c7442209701c05e52dd792effa6965",
            host = "ec2-3-219-19-205.compute-1.amazonaws.com",
            port = "5432"
        )
        return connection




    # CREATE CONNECTION VARIABLE EQUAL TO GET_CONNECTED FUNCTION INVOKED

    connection = get_connected()



    ########################################### TO DO #########################################################

    # CREATE CURSOR USING CONNECTION.CURSOR() FUNCTION
    cursor = connection.cursor()

    ###########################################################################################################

    # prints postgresql details - DO NOT ALTER OR DELETE
    print("PostgreSQL server information:")
    print(connection.get_dsn_parameters(), "\n") # DO NOT ALTER OR DELETE PRINT STATEMENT

    # executes query for database version - DO NOT ALTER OR DELETE
    cursor.execute("SELECT version();")

    # fetches result and prints database information - DO NOT ALTER OR DELETE
    record = cursor.fetchone() 
    print("Connection successful. You are connected to - ", record, "\n") # DO NOT ALTER OR DELETE PRINT STATEMENT

# handles errors and prints them to the console - DO NOT ALTER OR DELETE

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)


finally:
    ##################################### TO DO ###########################################################
    ### USING IF(CONNECTION) FUNCTION, CLOSE THE CURSOR AND THE CONNECTION ###
    if(connection):
        cursor.close
        connection.close
        print("DB connection is closed.") # DO NOT ALTER OR DELETE PRINT STATEMENT

###########################################################################################################