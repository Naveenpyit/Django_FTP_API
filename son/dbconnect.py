from .mainconnection import connection

class Api_methods:
    @staticmethod
    def get_commmon(query):
        try:
            conn=connection.db_connection()
            cur=conn.cursor()
            cur.execute(query)
            cols=[des[0]for des in cur.description]
            row=cur.fetchall()
            if cur.rowcount==0:
                return "Row doesn't Exist!,Need to Insert!"
            res=[dict(zip(cols,r))for r in row ]
            return res
        except Exception as err:
            return {"Error":str(err)}
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()

    @staticmethod
    def post_common(query):
        try:
            conn=connection.db_connection()
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            return {"Message":"Data Submitted Successfully!"}
        except Exception as err:
            return {"Error":str(err)}
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()

    @staticmethod
    def put_common(query):
        try:
            conn=connection.db_connection()
            cur=conn.cursor()
            cur.execute(query)
            conn.commit()
            if cur.rowcount==0:
                return {"Message":"Row doesn't Exist, Need to Insert!"}
            return {"Message":"Data Updated Successfully!"}
        except Exception as err:
            return {"Error":str(err)}
        finally:
            if conn:
                conn.close()
            if cur:
                cur.close()

    