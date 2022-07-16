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