import sqlite3
import config
from datetime import datetime

class Database():
    def __init__(self):
        #self.conn = sqlite3.connect('voting.db')
        self.conn = sqlite3.connect(f'{config.voting_db}/voting.db')
        self.ads = sqlite3.connect(f'ads.db') 
        self.token = sqlite3.connect(f'{config.pay_url}/paymant.db')
        # self.conn2 = sqlite3.connect(f'voting.db')
        # self.token = sqlite3.connect(f'paymant.db')

        self.c = self.conn.cursor()        
        self.ctok = self.token.cursor()
           
        #table
        self.ELEMENT = "ELEMENT"
        self.OPTION = "OPTION"
        self.PROMPT = "PROMPT"
        self.ELEMENTS = "ELEMENTS"
        self.table_vote = 'TABLE_VOTE'
        self.user_info = 'USER_INFO'
        self.users_token = 'USER_TOKEN'
        self.PAYER = "PAYER"      
        self.user_image = "USER_IMAGE"
        self.COMPETITION = "COMPETITION"
        self.QUEUE = "QUEUE"
        self.MEMBER = "MEMBER"
        self.MEMBER_VIP = "MEMBER_VIP"
        self.MODE = "MODE"
        self.PAYED_USER = "PAYED_USER"
        self.LANGUAGE = "LANGUAGE"
        self.MODEL = "MODEL"
        self.USER_MODEL = "USER_MODEL"
        self.SIZE_IMAGE = "SIZE_IMAGE"
        self.LEONARDO_MODE = "LEONARDO_MODE"

        #self.total_token = 'total_token'
        self.post_id = "post_id"
        self.user_id = "user_id"
        self.username = "username"      
        self.vote = "user_vote"       
        self.datetime = "datetime"
        self.table_queue = "queue"
        self.joined = "joined"
        self.elements = "elements"
        self.alchemy = "alchemy_v2"
        self.photoreal = "photoreal_v2"
        self.gradation = "gradazione"
        self.prompt = "prompt"
        self.element_name = "element_name"
        self.element_id = "element_id"
        self.leonardo_mode = "leonardo_mode"
        self.language_code = "language_code"
        self.total_token = "token" 
        self.model_id = "model_id"
        self.model_name = "model_name"
        self.image_size = "image_size"
        self.enable = "enable"

    pass
        
    def create_table(self):
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.user_info} ({self.user_id} INTEGER PRIMARY KEY, {self.username} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_vote} ({self.user_id} INTEGER, {self.post_id} INTEGER, {self.vote} TEXT, PRIMARY KEY ({self.user_id}, {self.post_id}))''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.users_token} ({self.user_id} INTEGER PRIMARY KEY, {self.total_token} INTEGER)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.user_image} ({self.post_id} INTEGER PRIMARY KEY, {self.user_id} INTEGER)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.COMPETITION} ({self.user_id} INTEGER PRIMARY KEY, {self.post_id} INTEGER, {self.datetime} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.QUEUE} ({self.user_id} INTEGER PRIMARY KEY, {self.datetime} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.MEMBER} ({self.user_id} INTEGER PRIMARY KEY, {self.joined} BOOL)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.MEMBER_VIP} ({self.user_id} INTEGER PRIMARY KEY, {self.joined} BOOL)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.ELEMENT} ({self.element_id} TEXT PRIMARY KEY, {self.user_id} INT, {self.gradation} FLOAT CHECK({self.gradation} >= -1 AND {self.gradation} <= 1))''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.OPTION} ({self.user_id} INT PRIMARY KEY, {self.alchemy} BOOL, {self.photoreal} BOOL)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.PROMPT} ({self.user_id} INT PRIMARY KEY, {self.post_id} INT,  {self.prompt} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.ELEMENTS} ({self.element_id} TEXT PRIMARY KEY, {self.element_name} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.MODE} ({self.user_id} TEXT PRIMARY KEY, {self.leonardo_mode} BOOL)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.LANGUAGE} ({self.user_id} INT PRIMARY KEY, {self.language_code} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.MODEL} ({self.model_id} TEXT PRIMARY KEY, {self.model_name} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.USER_MODEL} ({self.user_id} INT PRIMARY KEY, {self.model_id} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.SIZE_IMAGE} ({self.user_id} INT PRIMARY KEY, {self.image_size} TEXT)''')
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {self.LEONARDO_MODE} ({self.user_id} INT PRIMARY KEY, {self.enable} BOOL)''')
        # self.ctok.execute(f'''CREATE TABLE IF NOT EXISTS {self.PAYER} ({self.user_id} INTEGER PRIMARY KEY, {self.total_token} INT)''')
        self.conn.commit()
        # self.token.commit()

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

    def delate_user(self, user_ids):
        for user_id in user_ids:
            self.c.execute(f"DELETE FROM {self.user_info} WHERE {self.user_id} = ?", (user_id,)) 
        self.conn.commit()          
    
    def get_user_data(self, user_id):
        self.c.execute(f'''SELECT {self.user_id} FROM {self.user_info} WHERE {self.user_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else (None)
    
    def insert_member(self, user_id, joined):
        self.c.execute(f"INSERT INTO {self.MEMBER} ({self.user_id}, {self.joined}) VALUES (?, ?)", (user_id, joined))
        self.conn.commit()

    def get_member(self, user_id):
        self.c.execute(f'''SELECT {self.user_id} FROM {self.MEMBER} WHERE {self.user_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else (None)
    
    def insert_vip_member(self, user_id, joined):
        self.c.execute(f"INSERT OR REPLACE INTO {self.MEMBER_VIP} ({self.user_id}, {self.joined}) VALUES (?, ?)", (user_id, joined))
        self.conn.commit()

    def get_vip_member(self, user_id):
        self.c.execute(f'''SELECT {self.user_id} FROM {self.MEMBER_VIP} WHERE {self.user_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else (None)
    
    def save_vote(self, user_id, post_id, vote):
        self.c.execute(f'''INSERT OR REPLACE INTO {self.table_vote} ({self.user_id}, {self.post_id}, {self.vote}) VALUES (?, ?, ?) ''', (user_id, post_id, vote))
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
        self.c.execute(f"CREATE TEMPORARY TABLE temp_user_info AS SELECT * FROM {self.user_info}")

        self.c.execute(f"SELECT {self.user_id} FROM temp_user_info")
        while True:
            user_id = self.c.fetchone()
            if user_id is None:
                break
            yield user_id

        self.c.execute("DROP TABLE temp_user_info")

    def delate_ids(self, user_ids):
        for user_id in user_ids:
            self.c.execute("DELETE FROM users WHERE user_id = ?", (user_id,)) 
        self.conn.commit()
        return f"Deleted"
    
    # def get_vote_count(self):
    #     self.c.execute(f"SELECT COUNT({self.user_id}) FROM {self.table_vote}")
    #     results = self.c.fetchall()
    #     return results[0] if results else 0
    
    def get_vote_count(self, user_id):
        self.c.execute(f"SELECT COUNT({self.post_id}) FROM {self.table_vote} WHERE {self.user_id} = ?", (user_id,))
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
                    SUM({self.table_vote}.{self.vote}) as total_votes, 
                    COUNT({self.table_vote}.{self.vote}) as num_votes
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
            averages.append((post_id, average_vote, num_votes))

        # Ordina per punteggio medio e numero di voti
        averages.sort(key=lambda x: (x[1], x[2]), reverse=True)

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
        self.c.execute(f"SELECT {self.datetime} FROM {self.COMPETITION} ORDER BY {self.datetime} ASC LIMIT 1")
        result = self.c.fetchone()
        return result[0] if result else None

    def reset_competition(self):
        #current_month_start = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        self.c.execute(f"DELETE FROM {self.COMPETITION}")
        self.conn.commit()

    def insert_element(self, user_id, element_id):
        self.c.execute(f'''INSERT OR REPLACE INTO {self.ELEMENT} ({self.element_id}, {self.user_id}) VALUES (?, ?)''', (element_id, user_id))
        self.conn.commit()

    def update_gradation(self, gradation, element_id):
        self.c.execute(f'''UPDATE {self.ELEMENT} SET {self.gradation} = ? WHERE {self.element_id} = ?''', (gradation, element_id))
        self.conn.commit()

    def get_gradations(self, user_id):
        self.c.execute(f'''SELECT {self.element_id} FROM {self.ELEMENT} WHERE {self.user_id} = ?''', (user_id,))
        rows = self.c.fetchall()
        self.conn.commit()
        return [row[0] for row in rows] if rows else []
    
    def get_gradation(self, user_id, element_id):
        self.c.execute(f'''SELECT {self.gradation} FROM {self.ELEMENT} WHERE {self.user_id} = ? AND {self.element_id} = ?''', (user_id, element_id,))
        rows = self.c.fetchall()
        self.conn.commit()
        return rows[0]

    def get_elements(self, user_id):
        self.c.execute(f'''SELECT {self.element_id} FROM {self.ELEMENT} WHERE {self.user_id} = ?''', (user_id,))
        rows = self.c.fetchall()
        self.conn.commit()
        return [row[0] for row in rows] if rows else []
    
    def delate_elements(self, user_id):
        self.c.execute(f"DELETE FROM {self.ELEMENT} WHERE {self.user_id} = ?", (user_id,)) 
        self.conn.commit()

    def delate_selected_element(self, user_id, element_id):
        self.c.execute(f"DELETE FROM {self.ELEMENT} WHERE {self.user_id} = ? AND {self.element_id} = ?", (user_id, element_id,)) 
        self.conn.commit()
    
    def insert_option(self, user_id, alchemy, photoreal):
        self.c.execute(f'''INSERT OR REPLACE INTO {self.OPTION} ({self.user_id}, {self.alchemy}, {self.photoreal}) VALUES (?, ?, ?)''', (user_id, alchemy, photoreal))
        self.conn.commit()

    def delate_option(self, user_id):
        self.c.execute(f"DELETE FROM {self.OPTION} WHERE {self.user_id} = ?", (user_id,)) 
        self.conn.commit()

    def get_option(self, user_id):
        self.c.execute(f'''SELECT {self.alchemy}, {self.photoreal} FROM {self.OPTION} WHERE {self.user_id} = ?''', (user_id,))
        rows = self.c.fetchall()
        self.conn.commit()
        if rows:
            return rows[0] # Restituisce il secondo campo della prima riga
        else:
            return None  # Restituisce None se non ci sono risultati
        
    def insert_model(self, model_id, model_name):
        self.c.execute(f"INSERT OR REPLACE INTO {self.MODEL} ({self.model_id}, {self.model_name}) VALUES (?, ?)", (model_id, model_name))
        self.conn.commit()
    
    def get_model_id(self, model_name):
        self.c.execute(f'''SELECT {self.model_id} FROM {self.MODEL} WHERE {self.model_name} = ?''', (model_name,))
        result = self.c.fetchone()
        self.conn.commit()
        return result[0] if result else (None)
    
    def get_models(self, user_id):
        self.c.execute(f'''SELECT {self.element_id} FROM {self.ELEMENT} WHERE {self.user_id} = ?''', (user_id,))
        rows = self.c.fetchall()
        self.conn.commit()
        return [row[0] for row in rows] if rows else []
    
    def insert_user_model(self, user_id, model_id):
        self.c.execute(f"INSERT OR REPLACE INTO {self.USER_MODEL} ({self.user_id}, {self.model_id}) VALUES (?, ?)", (user_id, model_id))
        self.conn.commit()

    def get_user_model(self, user_id):
        self.c.execute(f'''SELECT {self.model_id} FROM {self.USER_MODEL} WHERE {self.model_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        return result[0] if result else (None)
    
    def get_model_name_by_user_id(self, user_id):
        self.c.execute(f'''
            SELECT {self.MODEL}.{self.model_name}
            FROM {self.USER_MODEL}
            JOIN {self.MODEL} ON {self.USER_MODEL}.{self.model_id} = {self.MODEL}.{self.model_id}
            WHERE {self.USER_MODEL}.{self.user_id} = ?
        ''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        return result[0] if result else "Leonardo Diffusion XL"
    
    def delate_user_model(self, user_id):
        self.c.execute(f"DELETE FROM {self.USER_MODEL} WHERE {self.user_id} = ?", (user_id,)) 
        self.conn.commit() 

    # def image_id(self, user_id, generationid):
    #     self.c.execute('''INSERT INTO IMAGE (generationid, user_id) VALUES (?, ?)''', 
    #                     (generationid, user_id))
    #     self.conn.commit()
    
    # def get_image_ids(self, user_id):
    #     self.c.execute('''SELECT generationid FROM IMAGE WHERE user_id = ?''', (user_id,))
    #     rows = self.c.fetchall()
    #     self.conn.commit()
    #     return [row[0] for row in rows] if rows else []

    # def delate_image_id(self, user_id):
    #     self.c.execute("DELETE FROM IMAGE WHERE user_id = ?", (user_id,)) 
    #     self.conn.commit()

    def insert_prompt(self, user_id, post_id, prompt):
        self.c.execute(f'''INSERT OR REPLACE INTO {self.PROMPT} ({self.user_id}, {self.post_id}, {self.prompt}) VALUES (?, ?, ?)''', (user_id, post_id, prompt))
        self.conn.commit()

    def get_prompt(self, user_id):
        self.c.execute(f'''SELECT {self.prompt}, {self.post_id} FROM {self.PROMPT} WHERE {self.user_id} = ?''', (user_id,))
        rows = self.c.fetchall()
        self.conn.commit()
        if rows:
            return rows[0] # Restituisce il secondo campo della prima riga
        else:
            return None  # Restituisce None se non ci sono risultati
        
    def delate_prompt(self, user_id):
        self.c.execute(f"DELETE FROM {self.PROMPT} WHERE {self.user_id} = ?", (user_id,)) 
        self.conn.commit()

    def insert_elements_id(self, element_id, element_name):
        self.c.execute(f'''INSERT OR REPLACE INTO {self.ELEMENTS} ({self.element_id}, {self.element_name}) VALUES (?, ?)''', (element_id, element_name))
        self.conn.commit()
        return
    
    def get_element_id(self, element_name):
        self.c.execute(f'''SELECT {self.element_id} FROM {self.ELEMENTS} WHERE {self.element_name} = ?''', (element_name,))
        rows = self.c.fetchall()
        self.conn.commit()
        if rows:
            return rows[0] # Restituisce il secondo campo della prima riga
        else:
            return None  # Restituisce None se non ci sono risultati
        
    def get_element_name(self, user_id):
        self.c.execute(f'''
            SELECT {self.ELEMENTS}.{self.element_name}, COALESCE({self.ELEMENT}.{self.gradation}, 1) AS gradation
            FROM {self.ELEMENT}
            JOIN {self.ELEMENTS} ON {self.ELEMENT}.{self.element_id} = {self.ELEMENTS}.{self.element_id}
            WHERE {self.ELEMENT}.{self.user_id} = ?
        ''', (user_id,))
        rows = self.c.fetchall()
        return [f"{row[0]}:{row[1]}" for row in rows] if rows else []

    def insert_mode(self, user_id, leonardo_mode):
        self.c.execute(f"INSERT OR REPLACE INTO {self.MODE} ({self.user_id}, {self.leonardo_mode}) VALUES (?, ?)", (user_id, leonardo_mode))
        self.conn.commit()

    def get_mode(self, user_id):
        self.c.execute(f'''SELECT {self.leonardo_mode} FROM {self.MODE} WHERE {self.user_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else (None)
    
    def insert_language(self, user_id, language_code):
        self.c.execute(f"INSERT OR REPLACE INTO {self.LANGUAGE} ({self.user_id}, {self.language_code}) VALUES (?, ?)", (user_id, language_code))
        self.conn.commit()

    def get_language_code(self, user_id):
        self.c.execute(f"SELECT {self.language_code} FROM {self.LANGUAGE} WHERE {self.user_id} = ?", (user_id,))
        result = self.c.fetchone()
        self.conn.commit()     
        return result[0] if result else (None)
    
    def insert_image_size(self, user_id, size):
        self.c.execute(f"INSERT OR REPLACE INTO {self.SIZE_IMAGE} ({self.user_id}, {self.image_size}) VALUES (?, ?)", (user_id, size))
        self.conn.commit()
    
    def get_image_size(self, user_id):
        self.c.execute(f'''SELECT {self.image_size} FROM {self.SIZE_IMAGE} WHERE {self.user_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        
        return result[0] if result else "1024x768"
    
    def insert_enable_mode(self, user_id, enable):
        self.c.execute(f"INSERT OR REPLACE INTO {self.LEONARDO_MODE} ({self.user_id}, {self.enable}) VALUES (?, ?)", (user_id, enable))
        self.conn.commit()
    
    def get_enabled_mode(self, user_id):
        self.c.execute(f'''SELECT {self.enable} FROM {self.LEONARDO_MODE} WHERE {self.user_id} = ?''', (user_id,))
        result = self.c.fetchone()
        self.conn.commit()
        return result[0] if result else False
    
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
        
    def insert_payed_user(self, user_id, datetime):
        self.ctok.execute(f"INSERT OR REPLACE INTO {self.PAYED_USER} ({self.datetime}, {self.user_id}) VALUES (?, ?)", (datetime, user_id))
        self.token.commit()
        
    def get_payed_user(self, user_id):
        self.ctok.execute(f'''SELECT {self.user_id} FROM {self.PAYED_USER} WHERE {self.user_id} = ?''', (user_id,))
        result = self.ctok.fetchone()
        self.token.commit()
        return result[0] if result else (None)    
        
    def update_user_token(self, total_token, user_id):
        self.ctok.execute(f"INSERT OR REPLACE INTO {self.PAYER} ({self.user_id}, {self.total_token}) VALUES (?, ?)", (user_id, total_token))
        #self.ctok.execute(f'''UPDATE {self.PAYER} SET {self.total_token} = ? WHERE {self.user_id} = ?''', (total_token, user_id))
        self.token.commit()

class Result():
    def __init__(self, user_id):
        self.db = Database()
        result_prompt = self.db.get_prompt(user_id)
        result_option = self.db.get_option(user_id)
        if result_option:
            self.photoreal_current = result_option[1]
            self.alchemy_current = result_option[0]
        else:
            self.photoreal_current = None
            self.alchemy_current = None
        if result_prompt:
            self.prompt = result_prompt[0]
            self.post_id = result_prompt[1]
        else: 
            self.prompt = None
            self.post_id = None