from database.DB_connect import DBConnect
from model.aeroporti import Aeroporti


class DAO():
    @staticmethod
    def allNodes():
        conn = DBConnect.get_connection()
        cursor=conn.cursor(dictionary=True)
        res=[]
        query="""SELECT *
                FROM airports a  """
        cursor.execute(query)
        for row in cursor:
            res.append(Aeroporti(**row))
        cursor.close()
        conn.close()
        return res

    @staticmethod
    def edges(a1,a2):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res =0
        query = """SELECT AVG(f.DISTANCE) as disMedia
                    FROM flights f 
                    where (f.ORIGIN_AIRPORT_ID =%s
                    and f.DESTINATION_AIRPORT_ID  =%s)
                    or (f.ORIGIN_AIRPORT_ID =%s
                    and f.DESTINATION_AIRPORT_ID  =%s)  """
        cursor.execute(query,(a1.ID,a2.ID, a2.ID, a1.ID,))
        for row in cursor:
            if row["disMedia"] is not None:
                res = row["disMedia"]
            else :
                return 0
        cursor.close()
        conn.close()
        return res

    @staticmethod
    def allEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """SELECT ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, DISTANCE
                    FROM flights
                    GROUP BY  ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID , DISTANCE"""
        cursor.execute(query)
        for row in cursor:
            res.append((row["ORIGIN_AIRPORT_ID"],
                       row["DESTINATION_AIRPORT_ID"],
                       row["DISTANCE"]))
        cursor.close()
        conn.close()
        return res