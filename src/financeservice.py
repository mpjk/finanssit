from repositories.userrepository import user_repository as userrepository
from repositories.userrepository import User
from repositories.profilerepository import profile_repository as profilerepository
from repositories.profilerepository import Profile
from repositories.transactionrepository import transaction_repository as transactionrepository
from repositories.transactionrepository import Transaction


class FinanceService:
    """handles the ui events to pass for the database through the repository components
    """

    def __init__(self, users=userrepository, profiles=profilerepository,
                 transactions=transactionrepository):
        """_summary_

        Args:
            users (_type_, optional): _description_. Defaults to userrepository.
            profiles (_type_, optional): _description_. Defaults to profilerepository.
            transactions (_type_, optional): _description_. Defaults to transactionrepository.
        """
        self._users = users
        self._user = None
        self._profiles = profiles
        self._transactions = transactions

    def login(self, username, password):
        """handles the logging in event

        Args:
            username (str): name of the user to log in
            password (str): password of the user

        Returns:
            User: the user object of the logged in user
        """
        user = self._users.find_username(username)

        if not user or user.password != password:
            return None

        self._user = user
        return user

    def register(self, username, password):
        """handles the registering of a user

        Args:
            username (str): new user name
            password (str): new user password

        Returns:
            User, str: user object if succesful, a string error message if not.
        """
        if username == "":
            return "Error: username must not be empty"

        if len(password) < 8:
            return """Error: password must contain at least\n 8 characters, 1 number
                        and\n1 special character"""

        if not any(c.isnumeric() for c in password):
            return "Error: password must contain at least\n1 number and 1 special character"

        if password.isalnum():
            return "Error: password must contain at least\n1 special character"

        username_exists = self._users.find_username(username)
        if username_exists:
            return "Error: username already exists"

        new_user = self._users.create_new_user(User(username, password))

        self._user = new_user
        return new_user

    def create_profile(self, profile_name, username):
        """handles the profile creation

        Args:
            profile_name (str): new profile name
            username (str): the username of the profile owner

        Returns:
            Profile: created profile object
        """
        new_profile = self._profiles.create_new_profile(
            Profile(profile_name, username))

        return new_profile

    def find_profile(self, profile_name):
        """finds a profile based on the searched name

        Args:
            profile_name (str): profile name to be searched

        Returns:
            Profile | None: found profile object if found, else None
        """
        profile = self._profiles.find_profile(profile_name)

        return profile

    def return_profiles(self, username):
        """returns all the profiles belonging to a user

        Args:
            username (str): username to be searched with

        Returns:
            list[Profile] | list: list of profiles if found, else an empty list.
        """
        return self._profiles.find_all_with_user(username)

    def create_transaction(self, name, amount_entry, profile, radio_value, date):
        """handles the creation of a new transaction

        Args:
            name (str): name of the transaction
            amount_entry (str): amount of the transaction
            profile (Profile): corresponding profile for the transaction
            radio_value (str): ttk.Radiobutton value
            date (str): DateEntry component value

        Returns:
            _type_: _description_
        """
        if amount_entry == "" or name == "":
            return "Error: transaction name or amount missing"

        try:
            float(amount_entry)
        except ValueError:
            return "Error: amount must be a numeric value"

        if radio_value == "":
            return "Error: transaction type missing"

        if radio_value == "Expense":
            amount = -abs(float(amount_entry))
        else:
            amount = float(amount_entry)

        new_transaction = self._transactions.create_transaction(
            Transaction(name, amount, profile, date))

        return new_transaction

    def edit_transaction(self, name, amount_entry, profile, radio_value, transaction_id, date):
        """handles the editing of an existing transaction

        Args:
            name (str): name of the transaction
            amount_entry (str): amount of the transaction
            profile (Profile): corresponding profile for the transaction
            radio_value (str): ttk.Radiobutton value
            transaction_id (int): existing transaction identifier
            date (str): DateEntry component value

        Returns:
            Transaction | str: 
                transaction object if succesful, else a string with an error message
        """
        if amount_entry == "" or name == "":
            return "Error: transaction name or amount missing"
        try:
            float(amount_entry)
        except ValueError:
            return "Error: amount must be a numeric value"

        if radio_value == "":
            return "Error: transaction type missing"

        if radio_value == "Expense":
            amount = -abs(float(amount_entry))
        else:
            amount = float(amount_entry)

        edit_transaction = self._transactions.edit_transaction(
            Transaction(name, amount, profile, date, transaction_id))

        return edit_transaction

    def remove_transaction(self, transaction_id):
        """handles the removal of a transaction

        Args:
            transaction_id (int): the transaction identifier

        Returns:
            bool | None: true value if successful, else None.
        """
        return self._transactions.remove_transaction(transaction_id)

    def get_transaction(self, transaction_id):
        """handles the retrieval of a transaction based on an identifier

        Args:
            transaction_id (int): the transaction identifier

        Returns:
            Transaction: transaction returned if found, else None.
        """
        return self._transactions.get_transaction(transaction_id)

    def return_transactions(self, profile):
        """returns all the transactions belonging to a profile

        Args:
            profile (Profile): the corresponding profile for the transactions

        Returns:
            list[Transaction] | list: list of transactions if found, else an empty list
        """
        return self._transactions.find_all_transactions_with_profile(profile)

    def return_profile_balance(self, profile):
        """returns the total balance of the profile based on the added transactions

        Args:
            profile (Profile): the corresponding profile for the transactions

        Returns:
            int | None: integer value of the sum, if transactions were found, else None.
        """
        return self._transactions.sum_of_profile_transactions(profile)
