# This file populated the database Hospital with following relations;
# TODO: Enter which relations and attributes that's included in the db
# All data can ba found in db_data

from db_data import *
import psycopg2
# http://initd.org/psycopg/docs/usage.html

# Drop table given by name parameter
def dropTable(cur, name):
    cur.execute('DROP TABLE %s;' % name)
    return

# Make the relation Queue and populate it with patients that are
#   assigned to a teamID and has a name, age, gender, issue and priority.
def mkQueue(cur):
    cur.execute ("CREATE TABLE Queue(   \
        personid varchar PRIMARY KEY,   \
        teamID serial,                  \
        name varchar,                   \
        age integer,                    \
        gender char,                    \
        issue varchar,                  \
        priority integer,               \
        timestmp varchar);"
    )
    for pdata in queue_data:
        cur.execute("INSERT INTO Queue \
            (personid, teamID, name, age, gender, issue, priority, timestmp) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (pdata[0], pdata[1], pdata[2], pdata[3], pdata[4], pdata[5], pdata[6], pdata[7])
        )
    return

# Make the Team relation that contains the TeamID, head of team and the
#   three issues a team can deal with.
def mkTeam(cur):
    cur.execute("CREATE TABLE Team( \
        teamId serial PRIMARY KEY,  \
        head varchar,               \
        issue1 varchar,             \
        issue2 varchar,             \
        issue3 varchar);"
    )
    for tdata in team_data:
        cur.execute("INSERT INTO Team \
            (teamId, head, issue1, issue2, issue3) \
            VALUES (%s, %s, %s, %s, %s)",
            (tdata[0], tdata[1], tdata[2], tdata[3], tdata[4])
        )
    return

# Make relation Treatments that lists all issues and corresponding treatments.
def mkTreatments(cur):
    cur.execute("CREATE TABLE Treatments(   \
        issue varchar,                      \
        treatment varchar,                  \
        cost int);"
    )
    for data in issues_and_treatments:
        cur.execute("INSERT INTO Treatments \
            (issue, treatment, cost) VALUES (%s, %s, %s)",
            (data[0], data[1], data[2])
        )
    return

# Make relation Drugs that lists all drugs and their associated cost
def mkDrugs(cur):
    cur.execute("CREATE TABLE Drugs(   \
        drug varchar,                      \
        cost int);"
    )
    for data in drugs_data:
        cur.execute("INSERT INTO Drugs \
            (drug, cost) VALUES (%s, %s)",
            (data[0], data[1])
        )
    return

def mkLog(cur):
    cur.execute ("CREATE TABLE patientLOG( \
        personID varchar UNIQUE,        \
        name varchar,                   \
        age integer,                    \
        issue varchar,                  \
        treat varchar,                  \
        drugs varchar,                  \
        waitTime int,                   \
        home char,                      \
        timee varchar UNIQUE,           \
        totCost int);"
        )

def main():
    # Connect to an existing database
    conn = psycopg2.connect("dbname=hospital user=postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Drop then create following relations
    # dropTable(cur, 'patientLOG')
    mkLog(cur)
    dropTable(cur, 'Queue')
    mkQueue(cur)
    dropTable(cur, 'Team')
    mkTeam(cur)
    dropTable(cur, 'Treatments')
    mkTreatments(cur)
    dropTable(cur, 'Drugs')
    mkDrugs(cur)
    # Make the changes to the database persistent
    conn.commit()
    # # Close communication with the database
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
