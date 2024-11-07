class StudentAccount:
    def __init__(self, builders):
        self._builder = builders

    def create_account(self):
        self._builder.create_new_account()
        self._builder.add_id()
        self._builder.add_type()
        self._builder.add_clearance()

    def show_account(self):
        return self._builder.account


class Builder():
    def __init__(self):
        self.account = None

    def create_new_account(self):
        self.account = Account()


class MoniepointStudentBuilder(Builder):
    def add_id(self):
        self.account.id = 'Two'

    def add_type(self):
        self.account.type = 'Savings'

    def add_clearance(self):
        self.account.clearance = 'Domiciliary'


class Account():
    def __init__(self):
        self.id = None
        self.type = None
        self.clearance = None

    def __str__(self):
        return '{} | {} | {} '.format(self.id, self.type, self.clearance)


builder = MoniepointStudentBuilder()
director = StudentAccount(builder)
director.create_account()
account = director.show_account()


print(account)

