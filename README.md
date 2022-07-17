# Simple Calculator

## Project Details
This project develops a python program which can perform the following arithmetic operations on two given numbers.
- Addition
- Subtraction
- Multiplication
- Division
- Floor Division
- Modulus

## Project Tasks
### Task1 : Create a project git repository 
- Log into github account and create a new repository named 'simple_calculator'
- Clone the empty repo into local machine using the below git command.
  > git clone https://github.com/<github_username>/simple_calculator.git
- Move into 'simple_calculator' folder using `cd` command as shown below.
  > cd simple_calculator
- Create a new markdown file named 'README.md' and specify the steps carried out till now.
- Save the changes done to `README.md` file and add it to staging area using below command
  > git add README.md
- Before committing the changes, set your name and email using `git config` commands as shwon below
  > git config --global user.name <user_name>
  > git config --global user.email <user_email> 
- Commit the changes with the message "Added Readme file", using below command
  > git commit -m "Created a Readme file"
- Before pushing changes to remote github repo, check if the remote repo details are added to the local repo using the below command.
  > git remote -v
- If remote repo details are not visible in the output, add the remote repo details as shown below
  > git remote add origin https://github.com/<github_username>/simple_calculator.git
- The default branch is named as `main`. You can change it to master using below command
  > git branch -M master
- Now push the changes using the below command
  > git push -u origin master 


### Task2 : Develop a python method capable of performing addition and subtraction
- Let us create a new branch `feature/arithmetic_operations` and start working in it.
  > git checkout -b feature/arithmetic_operations
- The above command creates and takes us to the new branch `feature/arithmetic_operations`. This can be verified using below command. It displays the branch we are currently in and marked with asterix (\*)
  > git branch
- Create a new file `calculator.py` with the below code
  ```py
  def display_operations(operations):
      
      print()
      for op_num, op_name in operations.items():
          print(f'* {op_name} - {op_num}')


  def perform_arithmetic_operations():

      operations = {'1': 'Addition',
                    '2': 'Subtraction',
                    '99': 'Quit'}

      welcome_msg = """
  -------------------------------
  Welcome to Simple Calculator!!!
  -------------------------------

  Simple Calculator can perform the below operations. 
  Each arithmetic operation is mapped to a number.
  """

      print(welcome_msg)
      
      while True:

          display_operations(operations)

          op_input_msg = "Select the number of arithmetic operation to be performed : "

          op = input(op_input_msg).strip()
          
          if op not in operations:
              print(f'Selected invalid operation: {op}\nExiting ...')
              break
          elif op == '99':
              print(f'Quiting ...')
              break

          line = input('Enter two input numbers (x, y): ')
          n1, n2 = [int(n.strip()) for n in line.split(',')]

          if op == '1':
              result = n1 + n2
          elif op == '2':
              result = n1 - n2

          print(f'The result of {operations[op]} operation on two numbers, {n1} and {n2}, is: {result}')

          flag = input("Do you like to perform an other operation? (y/n): ")

          flag = flag.strip()
          if flag == 'n':
              print('Thank you for using Simple Calculator\nExiting ...')
              break
          elif flag == 'y':
              continue
          else:
              print(f'Provided invaild Input {flag}\nExiting ...')
              
  if __name__ == '__main__':
      perform_arithmetic_operations()
  ```
- Save the contents of the file and add it to staging area.
  > git add calculator.py
- The python file defines the method `perform_arithmetic_operations` which is capable for performing addition and subtraction.
- Update `README.md` and also add it to staging area.
  > git add README.md
- Commit the changes as shown below
  > git commit -m "Added addition and subtraction operations"
- Push the changes to remote repo using below command
  > git push origin feature/arithmetic_operations
  