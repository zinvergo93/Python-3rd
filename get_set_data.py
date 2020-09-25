# class Invoice:
#     def __init__(self, client, total):
#         self.client = client
#         self.total = total
    
#     def formatter(self):
#         return f'{self.client} owes: ${self.total}'

# google = Invoice('Google', 100000)

# print(google.client)
# print(google.total)

# google.client = 'Yahoo'

# print(google.client)


# *********************************************
# **********Python decorator*******************

class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client


    # @client.setter
    # def client(self, client):
    #     self._client = client

    # ^^^^ gives ability to override, but when deactivated, doesn't have ability
    #  '@' is a decorator that wraps a function into something with further functionality.

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

google = Invoice('Google', 100)

print(google.client)

# google.client = 'Yahoo'

# print(google.client)

google.total = 12000
print(google.total)

