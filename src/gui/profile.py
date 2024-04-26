from tkinter import ttk, constants
import tkinter as tk
from financeservice import FinanceService
from compound_interest_calc import calculate_investments


class Profile:
    def __init__(self, root, handle_login, profile):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._app = FinanceService()
        self._profile_tree = None
        self._profile = profile
        self._transaction_amount_entry = None
        self._transaction_name_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def add_transaction(self):
        name = self._transaction_name_entry.get()
        amount = self._transaction_amount_entry.get()
        print(name, amount)

    def open_transaction_window(self):
        transaction_window = tk.Toplevel(self._frame)
        transaction_window.wm_transient(self._frame)
        transaction_window.grab_set()
        transaction_name_label = ttk.Label(
            master=transaction_window, text="Transaction name")
        self._transaction_name_entry = ttk.Entry(master=transaction_window)
        transaction_amount_label = ttk.Label(
            master=transaction_window, text="Amount")
        self._transaction_amount_entry = ttk.Entry(master=transaction_window)
        add_transaction_button = ttk.Button(master=transaction_window, text="Add transaction",
                                            command=self.add_transaction)
        transaction_name_label.grid(row=0, column=0)
        self._transaction_name_entry.grid(row=0, column=1)
        transaction_amount_label.grid(row=1, column=0)
        self._transaction_amount_entry.grid(row=1, column=1)
        add_transaction_button.grid(row=2, columnspan=2)

    def open_compound_interest_calculator(self):
        cic_window = tk.Toplevel(self._frame)
        cic_window.wm_transient(self._frame)
        cic_window.grab_set()

        cic_window.geometry(
            f"+{self._root.winfo_x() + 50}+{self._root.winfo_y() + 50}"
        )

        ttk.Label(master=cic_window, text="Compound Interest Calculator",
                  font=("TkDefaultFont", 20)).grid(row=0, column=0, columnspan=2)

        cic_curr_value_ent = ttk.Entry(master=cic_window)
        cic_curr_value_ent.grid(row=1, column=1)
        ttk.Label(master=cic_window, text="Current value of investments (€)").grid(
            row=1, column=0)

        cic_monthly_ctrb_ent = ttk.Entry(master=cic_window)
        cic_monthly_ctrb_ent.grid(row=2, column=1)
        ttk.Label(master=cic_window, text="Monthly contribution (€)").grid(
            row=2, column=0)

        cic_est_return_ent = ttk.Entry(master=cic_window)
        cic_est_return_ent.grid(row=3, column=1)
        ttk.Label(master=cic_window, text="Anticipated return for investment (%)").grid(
            row=3, column=0)

        cic_time_hrz_ent = ttk.Entry(master=cic_window)
        cic_time_hrz_ent.grid(row=4, column=1)
        ttk.Label(
            master=cic_window, text="Investment time horizon (years)").grid(row=4, column=0)

        ttk.Button(master=cic_window,
                   text="Calculate",
                   command=lambda:
                       calculate_investments(
                           cic_curr_value_ent.get(),
                           cic_monthly_ctrb_ent.get(),
                           cic_est_return_ent.get(),
                           cic_time_hrz_ent.get())).grid(row=5, column=0, columnspan=2)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=self._profile.name,
                          font=("TkDefaultFont", 20))

        button = ttk.Button(
            master=self._frame,
            text="Log out",
            command=self._handle_login
        )

        add_transaction_button = ttk.Button(
            master=self._frame,
            text="Add transaction",
            command=self.open_transaction_window
        )

        investment_calculator_btn = ttk.Button(
            master=self._frame,
            text="Compound Interest Calculator",
            command=self.open_compound_interest_calculator
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        add_transaction_button.grid(row=2, column=0)
        investment_calculator_btn.grid(row=3, column=0)
