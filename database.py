from services.monogdb import db
import os
import sys
from telegraph import upload_file

from datetime import datetime


class database(object):
    
    def __init__(self, *args):
        super(database, self).__init__(*args)
        self.db = db

    
    async def register(self,database_name, dict) -> bool:
        if await db[database_name].insert_one(dict):
            return True
        else:
            return False

    async def find_one(self,database_name,dict):
        find = await self.db[database_name].find_one(dict)
        if find is None: return None
        else: return find
        
    async def find_register(self, Client, message):
        """[summary]
    Find and return data. register if data not found and return registred data.
    Args:
        Client ([object]): [Client Object]
        Message ([object]): [Messsage Object]

    Returns:
        [Dict]: [return Database user Info]
    """
        find = await self.db.users.find_one({'_id': message.from_user.id})
        if find is not None: return find
        else:
            if message.from_user.photo is None:
                userimage = "https://te.legra.ph/file/8692b409921efe361831f.png"
            else:
                user_image_path = (f"./user-image/{message.from_user.id}.jpg")
                await Client.download_media(message=message.from_user.photo.big_file_id, file_name=user_image_path)
                tlink = upload_file(user_image_path)
                userimage = f"https://telegra.ph{tlink[0]}"
                os.remove(user_image_path)
            my_dict = {
                '_id' : message.from_user.id,
                'username': message.from_user.username,
                'plan': 'F',
                'credit': 0,
                'role': 'Free',
                'image': userimage,
                'date': datetime.now().strftime("%b-%d-%Y %I:%M %p"),
                'ccs' : []
            }
            reg = await self.register('users', my_dict)
            if reg == False: return False
            else:
                return await self.find_one('users',{'_id': message.from_user.id})
    
    async def find_bin(self,bin) -> dict:
        """return bin info

        Args:
            bin ([int]): [6 didgit bin.]

        Returns:
            object: [return None if bin not found else find]
        """
        find = await self.db.bins.find_one({'number': int(bin)})
        if find is None:
            return None
        else:
            return find
        
    async def update_one(self,database_name,filter, update):
        update = await self.db[database_name].update_one(filter, update)
        if update.modified_count > 0: return True
        else: return False
    
    async def delete_bin(self,data_to_delete):
        x = await self.db.bins.delete_one(data_to_delete)
        return x
    
    async def delete(self,database_name, data_to_delete):
        x = await self.db[database_name].delete_one(data_to_delete)
        return x
