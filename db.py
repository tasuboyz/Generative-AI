import sqlite3
import config
from datetime import datetime

class Database():
    def __init__(self):
        self.conn = sqlite3.connect('voting.db')
        self.conn2 = sqlite3.connect(f'{config.pay_url}/voting.db')
        self.token = sqlite3.connect(f'{config.pay_url}/paymant.db')

        self.c = self.conn.cursor()        
        self.ctok = self.token.cursor()
           
        self.table_vote = 'TABLE_VOTE'
        self.user_info = 'USER_INFO'
        self.users_token = 'USER_TOKEN'
        self.PAYER = "PAYER"      
        self.user_image = "USER_IMAGE"
        self.COMPETITION = "COMPETITION"
        self.QUEUE = "QUEUE"

        self.total_token = 'total_token'
        self.post_id = "post_id"
        self.user_id = "user_id"
        self.username = "username"      
        self.vote = "user_vote"       
        self.datetime = "datetime"
        self.table_queue = "queue"

        self.total_token = "token" 
    pass
        
    def create_table(self):
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.user_info} ({self.user_id} INTEGER PRIMARY KEY, {self.username} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_vote} ({self.user_id} INTEGER, {self.post_id} INTEGER, {self.vote} TEXT, PRIMARY KEY ({self.user_id}, {self.post_id}))''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.users_token} ({self.user_id} INTEGER PRIMARY KEY, {self.total_token} INTEGER)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.user_image} ({self.post_id} INTEGER PRIMARY KEY, {self.user_id} INTEGER)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.COMPETITION} ({self.user_id} INTEGER PRIMARY KEY, {self.post_id} INTEGER, {self.datetime} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.QUEUE} ({self.user_id} INTEGER PRIMARY KEY, {self.datetime} TEXT)''')
        self.conn.commit()

    def insert_queue(self, user_id, datetime):
        self.c.execute(f"INSERT OR REPLACE INTO {self.QUEUE} ({self.user_id}, {self.datetime}) VALUES (?, ?)", (user_id, datetime))
        self.conn.commit()

    def get_count_queue(self):
        self.c.execute(f"SELECT COUNT({self.user_id}) FROM {self.QUEUE}")
        row_count = self.c.fetchone()[0]
        return row_count
    
    def get_oldest_datetime(self):
        self.c.execute(f"SELECT MIN({self.datetime}) FROM {self.QUEUE}")
        oldest_datetime = self.c.fetchone()[0]
        return oldest_datetime
    
    def clear_queue(self, user_id):
        self.c.execute(f"DELETE FROM {self.QUEUE} WHERE {self.user_id} = ?", (user_id,)) 
        self.conn.commit()   
        
    def insert_user_data(self, user_id, username):
        self.c.execute(f"INSERT OR REPLACE INTO {self.user_info} ({self.user_id}, {self.username}) VALUES (?, ?)", (user_id, username))
        self.conn.commit()

    def get_user_data(self, user_id):
        self.c.execute(f'''SELECT {self.user_id} FROM {self.user_info} WHERE {self.user_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else (None)
    
    def save_vote(self, user_id, post_id, vote):
        self.c.execute(f'''INSERT INTO {self.table_vote} ({self.user_id}, {self.post_id}, {self.vote}) VALUES (?, ?, ?) ''', (user_id, post_id, vote))
        self.conn.commit()

    def update_vote(self, user_id, post_id, vote):
        self.c.execute(f'''UPDATE {self.table_vote} SET {self.vote} = ? WHERE {self.user_id} = ? AND {self.post_id} = ?''', (vote, user_id, post_id))
        self.conn.commit()
        
    def get_vote(self, user_id, post_id):
        self.c.execute(f'''SELECT {self.vote} FROM {self.table_vote} WHERE {self.user_id} = ? AND {self.post_id} = ?''', (user_id, post_id))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else (None)
    
    def get_post_vote(self, post_id):
        self.c.execute(f'''SELECT {self.vote} FROM {self.table_vote} WHERE {self.post_id} = ?''', (post_id,))
        result = self.c.fetchone()
        self.conn.commit()
        return result
    
    def save_user_image(self, user_id, post_id):
        self.c.execute(f'''INSERT INTO {self.user_image} ({self.post_id}, {self.user_id}) VALUES (?, ?) ''', (post_id, user_id))
        self.conn.commit()
        return
    
    def get_user_by_image(self, post_id):
        self.c.execute(f'''SELECT {self.user_id} FROM {self.user_image} WHERE {self.post_id} = ?''', (post_id,))
        result = self.c.fetchone()
        self.conn.commit()
        return result[0] if result else (None)
    
    def delate_image(self, user_id):
        self.c.execute(f"DELETE FROM {self.user_image} WHERE {self.user_id} = ?", (user_id,)) 
        self.conn.commit()                        
            
    def count_users(self):
        self.c.execute(f"SELECT COUNT({self.user_id}) FROM {self.user_info}")
        row_count = self.c.fetchone()[0]
        return row_count
    
    async def get_users(self):
        self.c.execute(f"SELECT {self.user_id} FROM {self.user_info}")
        while True:
            user_id = self.c.fetchone()
            if user_id is None:
                break
            yield user_id     
    
    def get_vote_count(self):
        self.c.execute(f"SELECT COUNT({self.user_id}) FROM {self.table_vote}")
        results = self.c.fetchall()
        return results[0] if results else 0
    
    def write_ids(self):
        self.c.execute(f"SELECT {self.user_id} FROM {self.user_info}")
        results = self.c.fetchall()
        with open('ids.txt', 'w') as file:
            for result in results:
                file.write(str(result[0]) + '\n')
        self.conn.commit()

    def calculate_average_votes(self):
        query = f"""
                SELECT {self.table_vote}.{self.post_id}, 
                    SUM({self.table_vote}.{self.vote}), 
                    COUNT({self.table_vote}.{self.vote}) 
                FROM {self.table_vote}
                JOIN {self.COMPETITION} ON {self.table_vote}.{self.post_id} = {self.COMPETITION}.{self.post_id}
                GROUP BY {self.table_vote}.{self.post_id}
            """

        self.c.execute(query)
        results = self.c.fetchall()

        averages = []
        for result in results:
            post_id = result[0]
            total_votes = result[1]
            num_votes = result[2]
            average_vote = total_votes / num_votes
            averages.append((post_id, average_vote))

        return averages
    
    def insert_concurrent(self, user_id, post_id, datetime):
        self.c.execute(f"INSERT OR REPLACE INTO {self.COMPETITION} ({self.user_id}, {self.post_id}, {self.datetime}) VALUES (?, ?, ?)", (user_id, post_id, datetime))
        self.conn.commit()

    def get_concurrent(self, user_id):
        self.c.execute(f'''SELECT {self.user_id} FROM {self.COMPETITION} WHERE {self.user_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else (None)
    
    def get_user_id_by_post(self, post_id):
        self.c.execute(f'''SELECT {self.user_id} FROM {self.COMPETITION} WHERE {self.post_id} = ?''', (post_id,))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else (None)
    
    def get_first_submission_of_month(self):
        current_month_start = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        self.c.execute(f"SELECT {self.datetime} FROM {self.COMPETITION} WHERE {self.datetime} >= ?", (current_month_start,))
        result = self.c.fetchone()
        return result[0] if result else None

    def reset_competition(self):
        current_month_start = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        self.c.execute(f"DELETE FROM {self.COMPETITION} WHERE {self.datetime} >= ?", (current_month_start,))
        self.conn.commit()

    #connect to payment database
    def user_token(self, user_id):
        self.ctok.execute(f'''SELECT {self.total_token} FROM {self.PAYER} WHERE {self.user_id} = ?''', (user_id,))
        results = self.ctok.fetchall()        
        self.token.commit()    
        if results:    
            token = results[0]
            token = token[0]
            return token
        else:
            return 0
        
    def update_user_token(self, total_token, user_id):
        self.ctok.execute(f"INSERT OR REPLACE INTO {self.PAYER} ({self.user_id}, {self.total_token}) VALUES (?, ?)", (user_id, total_token))
        #self.ctok.execute(f'''UPDATE {self.PAYER} SET {self.total_token} = ? WHERE {self.user_id} = ?''', (total_token, user_id))
        self.token.commit()


