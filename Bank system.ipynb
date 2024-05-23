{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "13b3030b",
   "metadata": {},
   "source": [
    "# 1)FIRSTLY --> BANK NAME \n",
    "\n",
    "# 2) CLASS --> BANK  OOPS \n",
    "   > CREATE NEW ACCOUNT --> NAME , AADHAR CARD , .... --> file handling > msg -> your account has been created\n",
    "   > LOGIN -> ACCOUNTHOLDER'SNAME , ID , PASSWORD(conditions , alphabumeric, special characters) , (No space , len should be less than 10 & greater than 6)\n",
    "    --> exception raise , handle it\n",
    "# 3) Login\n",
    "  > credit\n",
    "  > debit \n",
    "  > add the amount , then again check the balance\n",
    "  > balance check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a9ae66ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "class BankofBaroda:\n",
    "    currentBal =0\n",
    "    startingBal =5000\n",
    "    dLogin = dict()\n",
    "    dBal = {}\n",
    "    def __init__(self,name, aadhar, address, user_id,pwd,amt):\n",
    "        self.name = name\n",
    "        self.aadhar =aadhar\n",
    "        self.address =address\n",
    "        self.user_id =user_id\n",
    "        self.pwd=pwd\n",
    "        self.amt =amt\n",
    "       \n",
    "       # accfile = open('new1.txt' , mode='x')\n",
    "       \n",
    "       \n",
    "        \n",
    "    \n",
    "    def newAcc(self, name, aadhar, address, user_id):\n",
    "        print(\"startingBal =5000\", self.startingBal)\n",
    "        accfile = open('new1.txt' , mode='a')\n",
    "        x=False\n",
    "        # Aadhar is digits only\n",
    "        if not aadhar.isdigit():\n",
    "            print('Aadhar card number should be numeric value')\n",
    "            raise Exception (\"Account not created!Try again\")\n",
    "        accfile = open('new1.txt' , mode='r')\n",
    "        content = accfile.read()\n",
    "        print ('Content', content)\n",
    "        print('user ID',user_id )\n",
    "        checkString= \",\"+ user_id\n",
    "        if checkString in content:\n",
    "            x= True\n",
    "            print(\"YESSSSSSSSSSSSSSSS\")\n",
    "        else:\n",
    "            x= False\n",
    "        \n",
    "        if (x):\n",
    "            print(\"User ID already exist! Try different user id\")\n",
    "        else:\n",
    "            accfile = open('new1.txt' , mode='a')\n",
    "            line =name +\",\" + aadhar + \",\" + address + \",\" + user_id + \"\\n\"\n",
    "            accfile.write(line)\n",
    "            print (\"Account successfully created! \")\n",
    "        \n",
    "        accfile.close()\n",
    "\n",
    "    \n",
    "    def signup(self,user_id,pwd):\n",
    "        accfile = open('new1.txt' , mode='r')\n",
    "        \n",
    "        content = accfile.read()\n",
    "        print(\"conteent\",content)\n",
    "        print('user ID',user_id )\n",
    "        greenflag = False\n",
    "        hasdigit =False\n",
    "        hasAlphabet =False\n",
    "        hasSpecial =False\n",
    "        \n",
    "        special_characters = \"!@#$%^&*()-+?_=,<>\"\n",
    "        checkString= \",\"+ user_id\n",
    "        if checkString in content :\n",
    "            print (\"content\",content,\"user_id,\",user_id, \"pwd\" , pwd)\n",
    "            for i in pwd:\n",
    "                if i.isdigit() and hasdigit== False:\n",
    "                    hasdigit = True\n",
    "                    print('It has number')\n",
    "                        \n",
    "                if (i in special_characters and hasSpecial==False):\n",
    "                    hasSpecial=True\n",
    "                    print('It has special char')\n",
    "                    \n",
    "                if(i.isalpha() and hasAlphabet == False):\n",
    "                    hasAlphabet=True\n",
    "                    print('It has alphabet')\n",
    "                        \n",
    "        \n",
    "            if not (hasSpecial and hasAlphabet and hasdigit):\n",
    "                 raise Exception(\"The password must be alphanumeric with at least one special charactor!\")\n",
    "            else:\n",
    "                greenflag=True\n",
    "            \n",
    "            if(greenflag):\n",
    "                if(len(pwd) < 6): \n",
    "                     raise Exception(\"Length of the password should be at least 6 characters\") \n",
    "                elif (len(pwd)>10):\n",
    "                     raise Exception(\"Length of the password should be between 6 and 10 characters\") \n",
    "                else:\n",
    "                    self.dLogin.update({user_id:pwd})\n",
    "                    \n",
    "                    print (\"Login successfully created! \",self.dLogin)\n",
    "                    self.dBal.update({user_id:5000})\n",
    "                    print(\"balance file updated\",self.dBal)\n",
    "        \n",
    "        \n",
    "        else:\n",
    "             raise Exception(\"User ID does not exist! Create an account first\")\n",
    "\n",
    "         \n",
    "    def checkbalance(self,user_id):\n",
    "        user_id_missing =True\n",
    "        print('user_id',user_id)\n",
    "        \n",
    "        if user_id in self.dLogin.keys():\n",
    "            user_id_missing =False\n",
    "            self.currentBal = self.dLogin.get(user_id)\n",
    "            \n",
    "        if(user_id_missing):\n",
    "            raise Exception (\"log in not created for this user_id :\",user_id)\n",
    "        \n",
    "        return self.currentBal\n",
    "        \n",
    "        \n",
    "    def Debit(self, user_id, amt):\n",
    "        user_id_missing =True\n",
    "        print(\"dLogin\",self.dLogin)\n",
    "        if user_id in self.dLogin.keys():\n",
    "            user_id_missing =False\n",
    "            self.startingBal = self.dBal.get(user_id)\n",
    "            \n",
    "        if(user_id_missing):\n",
    "            raise Exception (\"log in not created for this user_id :\",user_id)\n",
    "        \n",
    "        print (\"TYPE:\",type( self.startingBal))\n",
    "        print(\"self.startingBal\",self.startingBal)\n",
    "        self.currentBal=self.startingBal -int(amt)\n",
    "        self.dBal.update({user_id:self.currentBal})\n",
    "        return  print(user_id,\" balance is \", self.currentBal)\n",
    "        \n",
    "    def credit(self, user_id, amt):\n",
    "        user_id_missing =True\n",
    "        print(\"dLogin\",self.dLogin)\n",
    "        if user_id in self.dLogin.keys():\n",
    "            user_id_missing =False\n",
    "            \n",
    "            self.startingBal = self.dBal.get(user_id)\n",
    "        print(\"self.startingBal\",self.startingBal)\n",
    "        self.currentBal=self.startingBal +int(amt)\n",
    "        self.dBal.update({user_id:self.currentBal})\n",
    "        return  print(user_id,\" balance is \", self.currentBal)\n",
    "        \n",
    "        \n",
    "        \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "458140a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Object creation\n",
    "b1= BankofBaroda('Ajay', \"12121212a\", \"AMD\", \"ajay123\",\"ajay123#\",'7000')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bf139fca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "startingBal =5000 5000\n",
      "Content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ajay123\n",
      "YESSSSSSSSSSSSSSSS\n",
      "User ID already exist! Try different user id\n"
     ]
    }
   ],
   "source": [
    "#Account created and Amar\n",
    "b1.newAcc('amar', \"12121212\", \"AMD\", \"ajay123\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cd34b331",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "startingBal =5000 5000\n",
      "Content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID EKta456\n",
      "YESSSSSSSSSSSSSSSS\n",
      "User ID already exist! Try different user id\n"
     ]
    }
   ],
   "source": [
    "b1.newAcc('Ekta', \"12121212\", \"AMD\", \"EKta456\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2b97de99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conteent amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID EKta456\n",
      "content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      " user_id, EKta456 pwd Water456#\n",
      "It has alphabet\n",
      "It has number\n",
      "It has special char\n",
      "Login successfully created!  {'EKta456': 'Water456#'}\n",
      "balance file updated {'EKta456': 5000}\n"
     ]
    }
   ],
   "source": [
    "#Correct pwd  \n",
    "b1.signup('EKta456','Water456#')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d573ba1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conteent amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ajay123\n",
      "content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      " user_id, ajay123 pwd ajay123#\n",
      "It has alphabet\n",
      "It has number\n",
      "It has special char\n",
      "Login successfully created!  {'EKta456': 'Water456#', 'ajay123': 'ajay123#'}\n",
      "balance file updated {'EKta456': 5000, 'ajay123': 5000}\n"
     ]
    }
   ],
   "source": [
    "#Correct pwd \n",
    "b1.signup('ajay123','ajay123#')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c576468d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dLogin {'EKta456': 'Water456#', 'ajay123': 'ajay123#'}\n",
      "self.startingBal 7000\n",
      "ajay123  balance is  8000\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print (b1.credit('ajay123',1000))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2d1a4b9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dLogin {'EKta456': 'Water456#', 'ajay123': 'ajay123#'}\n",
      "TYPE: <class 'int'>\n",
      "self.startingBal 5000\n",
      "EKta456  balance is  3000\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print (b1.Debit('EKta456',2000))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a66bf796",
   "metadata": {},
   "source": [
    "# ERRORS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5fab50c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "startingBal =5000 7000\n",
      "Content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ajay123\n",
      "YESSSSSSSSSSSSSSSS\n",
      "User ID already exist! Try different user id\n"
     ]
    }
   ],
   "source": [
    "# ERROR: user id already exist\n",
    "b1.newAcc('astha', \"13434342\", \"AMD\", \"ajay123\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0819f7b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "startingBal =5000 5000\n",
      "Aadhar card number should be numeric value\n"
     ]
    },
    {
     "ename": "Exception",
     "evalue": "Account not created!Try again",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mException\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[13], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m b1\u001b[38;5;241m.\u001b[39mnewAcc(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAjay\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m12121212a\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAMD\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124majay123\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "Cell \u001b[1;32mIn[10], line 25\u001b[0m, in \u001b[0;36mBankofBaroda.newAcc\u001b[1;34m(self, name, aadhar, address, user_id)\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m aadhar\u001b[38;5;241m.\u001b[39misdigit():\n\u001b[0;32m     24\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAadhar card number should be numeric value\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m---> 25\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m (\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAccount not created!Try again\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     26\u001b[0m accfile \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mnew1.txt\u001b[39m\u001b[38;5;124m'\u001b[39m , mode\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mr\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m     27\u001b[0m content \u001b[38;5;241m=\u001b[39m accfile\u001b[38;5;241m.\u001b[39mread()\n",
      "\u001b[1;31mException\u001b[0m: Account not created!Try again"
     ]
    }
   ],
   "source": [
    "b1.newAcc('Ajay', \"12121212a\", \"AMD\", \"ajay123\") #Aadhar card error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a7e82651",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conteent amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ajay123\n",
      "content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      " user_id, ajay123 pwd abcd\n",
      "It has alphabet\n"
     ]
    },
    {
     "ename": "Exception",
     "evalue": "The password must be alphanumeric with at least one special charactor!",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mException\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[10], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Only Alphabets ->exception\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m b1\u001b[38;5;241m.\u001b[39msignup(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124majay123\u001b[39m\u001b[38;5;124m'\u001b[39m,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mabcd\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "Cell \u001b[1;32mIn[1], line 79\u001b[0m, in \u001b[0;36mBankofBaroda.signup\u001b[1;34m(self, user_id, pwd)\u001b[0m\n\u001b[0;32m     75\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mIt has alphabet\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m     78\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m (hasSpecial \u001b[38;5;129;01mand\u001b[39;00m hasAlphabet \u001b[38;5;129;01mand\u001b[39;00m hasdigit):\n\u001b[1;32m---> 79\u001b[0m      \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThe password must be alphanumeric with at least one special charactor!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     80\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m     81\u001b[0m     greenflag\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m\n",
      "\u001b[1;31mException\u001b[0m: The password must be alphanumeric with at least one special charactor!"
     ]
    }
   ],
   "source": [
    "#Only Alphabets ->exception\n",
    "b1.signup('ajay123','abcd')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "53066ddf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conteent amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ajay123\n",
      "content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      " user_id, ajay123 pwd abcd12\n",
      "It has alphabet\n",
      "It has number\n"
     ]
    },
    {
     "ename": "Exception",
     "evalue": "The password must be alphanumeric with at least one special charactor!",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mException\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[11], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Only Alphabets and numbers ->exception\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m b1\u001b[38;5;241m.\u001b[39msignup(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124majay123\u001b[39m\u001b[38;5;124m'\u001b[39m,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mabcd12\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "Cell \u001b[1;32mIn[1], line 79\u001b[0m, in \u001b[0;36mBankofBaroda.signup\u001b[1;34m(self, user_id, pwd)\u001b[0m\n\u001b[0;32m     75\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mIt has alphabet\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m     78\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m (hasSpecial \u001b[38;5;129;01mand\u001b[39;00m hasAlphabet \u001b[38;5;129;01mand\u001b[39;00m hasdigit):\n\u001b[1;32m---> 79\u001b[0m      \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThe password must be alphanumeric with at least one special charactor!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     80\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m     81\u001b[0m     greenflag\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m\n",
      "\u001b[1;31mException\u001b[0m: The password must be alphanumeric with at least one special charactor!"
     ]
    }
   ],
   "source": [
    "#Only Alphabets and numbers ->exception\n",
    "b1.signup('ajay123','abcd12')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "861248a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conteent amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ajay123\n",
      "content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      " user_id, ajay123 pwd abcd!\n",
      "It has alphabet\n",
      "It has special char\n"
     ]
    },
    {
     "ename": "Exception",
     "evalue": "The password must be alphanumeric with at least one special charactor!",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mException\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[12], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Only Alphabets and special char ->exception\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m b1\u001b[38;5;241m.\u001b[39msignup(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124majay123\u001b[39m\u001b[38;5;124m'\u001b[39m,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mabcd!\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "Cell \u001b[1;32mIn[1], line 79\u001b[0m, in \u001b[0;36mBankofBaroda.signup\u001b[1;34m(self, user_id, pwd)\u001b[0m\n\u001b[0;32m     75\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mIt has alphabet\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m     78\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m (hasSpecial \u001b[38;5;129;01mand\u001b[39;00m hasAlphabet \u001b[38;5;129;01mand\u001b[39;00m hasdigit):\n\u001b[1;32m---> 79\u001b[0m      \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThe password must be alphanumeric with at least one special charactor!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     80\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m     81\u001b[0m     greenflag\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m\n",
      "\u001b[1;31mException\u001b[0m: The password must be alphanumeric with at least one special charactor!"
     ]
    }
   ],
   "source": [
    "#Only Alphabets and special char ->exception\n",
    "b1.signup('ajay123','abcd!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e5e7cd9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conteent amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ajay123\n",
      "content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      " user_id, ajay123 pwd abc3#\n",
      "It has alphabet\n",
      "It has number\n",
      "It has special char\n"
     ]
    },
    {
     "ename": "Exception",
     "evalue": "Length of the password should be at least 6 characters",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mException\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[13], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Only Less than 6 char ->exception\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m b1\u001b[38;5;241m.\u001b[39msignup(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124majay123\u001b[39m\u001b[38;5;124m'\u001b[39m,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mabc3#\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "Cell \u001b[1;32mIn[1], line 85\u001b[0m, in \u001b[0;36mBankofBaroda.signup\u001b[1;34m(self, user_id, pwd)\u001b[0m\n\u001b[0;32m     83\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m(greenflag):\n\u001b[0;32m     84\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m(\u001b[38;5;28mlen\u001b[39m(pwd) \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m6\u001b[39m): \n\u001b[1;32m---> 85\u001b[0m          \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLength of the password should be at least 6 characters\u001b[39m\u001b[38;5;124m\"\u001b[39m) \n\u001b[0;32m     86\u001b[0m     \u001b[38;5;28;01melif\u001b[39;00m (\u001b[38;5;28mlen\u001b[39m(pwd)\u001b[38;5;241m>\u001b[39m\u001b[38;5;241m10\u001b[39m):\n\u001b[0;32m     87\u001b[0m          \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLength of the password should be between 6 and 10 characters\u001b[39m\u001b[38;5;124m\"\u001b[39m) \n",
      "\u001b[1;31mException\u001b[0m: Length of the password should be at least 6 characters"
     ]
    }
   ],
   "source": [
    "#Only Less than 6 char ->exception\n",
    "b1.signup('ajay123','abc3#')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "32842f5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conteent amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ajay123\n",
      "content amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      " user_id, ajay123 pwd abc3#asadaff\n",
      "It has alphabet\n",
      "It has number\n",
      "It has special char\n"
     ]
    },
    {
     "ename": "Exception",
     "evalue": "Length of the password should be between 6 and 10 characters",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mException\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[14], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Only pwd greater than 10 char ->exception\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m b1\u001b[38;5;241m.\u001b[39msignup(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124majay123\u001b[39m\u001b[38;5;124m'\u001b[39m,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mabc3#asadaff\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "Cell \u001b[1;32mIn[1], line 87\u001b[0m, in \u001b[0;36mBankofBaroda.signup\u001b[1;34m(self, user_id, pwd)\u001b[0m\n\u001b[0;32m     85\u001b[0m      \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLength of the password should be at least 6 characters\u001b[39m\u001b[38;5;124m\"\u001b[39m) \n\u001b[0;32m     86\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m (\u001b[38;5;28mlen\u001b[39m(pwd)\u001b[38;5;241m>\u001b[39m\u001b[38;5;241m10\u001b[39m):\n\u001b[1;32m---> 87\u001b[0m      \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLength of the password should be between 6 and 10 characters\u001b[39m\u001b[38;5;124m\"\u001b[39m) \n\u001b[0;32m     88\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m     89\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdLogin\u001b[38;5;241m.\u001b[39mupdate({user_id:pwd})\n",
      "\u001b[1;31mException\u001b[0m: Length of the password should be between 6 and 10 characters"
     ]
    }
   ],
   "source": [
    "#Only pwd greater than 10 char ->exception\n",
    "b1.signup('ajay123','abc3#asadaff')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "774b2e96",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "conteent amar,12121212,AMD,ajay123\n",
      "Ekta,12121212,AMD,EKta456\n",
      "\n",
      "user ID ay123\n"
     ]
    },
    {
     "ename": "Exception",
     "evalue": "User ID does not exist! Create an account first",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mException\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[15], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# used id does not exist in the login file\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m b1\u001b[38;5;241m.\u001b[39msignup(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124may123\u001b[39m\u001b[38;5;124m'\u001b[39m,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mabc3#daff\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "Cell \u001b[1;32mIn[1], line 97\u001b[0m, in \u001b[0;36mBankofBaroda.signup\u001b[1;34m(self, user_id, pwd)\u001b[0m\n\u001b[0;32m     93\u001b[0m             \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbalance file updated\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdBal)\n\u001b[0;32m     96\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m---> 97\u001b[0m      \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mUser ID does not exist! Create an account first\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mException\u001b[0m: User ID does not exist! Create an account first"
     ]
    }
   ],
   "source": [
    "# used id does not exist in the login file\n",
    "b1.signup('ay123','abc3#daff')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
