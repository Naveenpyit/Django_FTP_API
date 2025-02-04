

class encrypt:
    @staticmethod
    def encrypt_data(data):
        keys="abcdefghjklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ0987654321~!@#$%^&*()_-+=[]|';:,.></? "

        en_data=[]

        for char in data:
            if char in keys:
                index=keys.index(char)
                new_index=(index + 5 ) % len(keys)
                en_data.append(keys[new_index])
            else:
                en_data.append(char)
        return en_data
        