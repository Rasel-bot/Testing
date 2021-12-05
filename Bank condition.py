{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ee6e884f",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Bank: \n",
    "    def __init__(self):\n",
    "        self.minimum = 100\n",
    "        self.balance = 1000\n",
    "        \n",
    "    def get_balance(self):\n",
    "        return self.balance\n",
    "    \n",
    "    def withdraw(self,amount):\n",
    "        if amount < self.minimum:\n",
    "            print(\" No money for you\")\n",
    "            \n",
    "        elif amount > self.balance:\n",
    "            print(\"Insufficient balance\")\n",
    "            \n",
    "        else:\n",
    "            self.balance = self.balance - amount\n",
    "            return amount"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c4b48296",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_account = Bank()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5e4595d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_account.get_balance()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c4ca241b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "500"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_account.withdraw(500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "95e87d3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Insufficient balance\n"
     ]
    }
   ],
   "source": [
    "my_account.withdraw(600)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a635ffce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " No money for you\n"
     ]
    }
   ],
   "source": [
    "my_account.withdraw(50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f8980fcb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "500"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_account.get_balance()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ad96930",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
