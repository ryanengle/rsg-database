#
# This file is part of the Air Force Institute of Technology (AFIT) 
# Resilient Sensor Grid (RSG) Extract, Transform, Load (ETL) Tool.
#
# Written by:
#               Ryan D. L. Engle
#               ryan.engle@afit.edu, rdengle@gmail.com
#               Air Force Institute of Technology
#               Department of Systems Engineering & Management (ENV)
#               2950 Hobson Way
#               Wright Patterson AFB, Ohio  45433-7765  USA
#
# This source code is property of the United States Government.
#
# NO PART OF THIS PROGRAM MAY BE COPIED, REPRODUCED, OR DUPLICATED WITHOUT
# THE EXPRESSED WRITTEN PERMISSION FROM AFIT/ENV.
#
# # This software is provided "AS IS" and the author disclaims all warranties with 
# regard to this software. In no event shall the author be liable for any indirect 
# or consequential damages arising out of, or in connection with, the use of this 
# software. USE AT YOUR OWN RISK.
#
# __version__ = '2020 0213 2053'
###############################################################################
import MySQLdb

import dbConfig
# dbconfig is not tracked by git
import closeDbConnection # For testing

def getDbConnection(typeCursor='simple', useLocalDb=True, userToken=0, dbName='umiami', verbose=False):
    '''
    Tries to connect to a database
        typeCursor: simple or dict type of cursor
        useLocalDb: True if using local, false if not 
        userToken: userId/token to identify the user name 
        dbName: name of the database 

    Returns
        status: True on success
        dbConnection: connection to the database
        cursor: cursor object
    '''
    # Database Server
    host = dbConfig.getHost(useLocal=useLocalDb)
    # Database Username/Password
    user = dbConfig.getUser(userToken=userToken)
    pwd  = dbConfig.getSecurityCheck(user)
    # Database Name
    databaseName = dbConfig.getDatabaseName(dbName)

    if verbose is True:
        print host, user, pwd, databaseName

    # Create the database connection object and connect
    try:
        dbConnection = MySQLdb.connect(host, user, pwd, databaseName)
        if typeCursor == 'dict':
            cursor = dbConnection.cursor(MySQLdb.cursors.DictCursor)
        elif typeCursor == 'simple':
            cursor = dbConnection.cursor()
    except Exception as e:
        print "ERROR: getDbConnection(): " + str(e)
        # TODO Write log on failure
        return False, None, None
    
    try:
        cursor.execute("SELECT VERSION()")
        results = cursor.fetchone()
        # Check if anything at all is returned
        if results:
            status = True
        else:
            status = False
    except MySQLdb.Error, e:
        print "ERROR: getDbConnection() %d IN CONNECTION: %s" % (e.args[0], e.args[1])
        return False, None, None

    return status, dbConnection, cursor

if __name__ == "__main__":
    status, dbConnection, cursor = getDbConnection(verbose=True)
    print status, type(dbConnection), type(cursor)
    if status is True:
        closeDbConnection.closeDbConnection(cursor, dbConnection)
        #closeDbConnection.closeDbConnection(None, None)
    