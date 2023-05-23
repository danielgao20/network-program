# Python Social Network Program
This Python program allows you to manage a social network and perform various operations on it. You can interact with the network using options to view member information, manipulate friend connections, search members by country, and more.

## Prerequisites

Before running the program, make sure you have the following:

- Python 3.x installed on your machine.
- Two data files containing profile and connection information. The profile file should be in CSV format, and the connection file should be a text file.

## Usage

To use the program, follow these steps:

1. Clone this repository or download the source code files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the program using the following command:

```
python social_network.py
```

4. When prompted, enter the names of the profile and connection files. For example:

```
Welcome to the network program.
We need two data files.
Enter the profile filename:
profile_10.csv
Enter the connection filename:
connection_10.txt
```

5. After providing the file names, a menu with options will be displayed. Choose an option by entering the corresponding number and pressing Enter.

```
Please select one of the following options:

1. Show a member's information 
2. Show a member's number of friends
3. Show a member's list of friends
4. Recommend a friend for a member
5. Search members by country
6. Add friend
7. Remove friend
8. Show graph
9. Save changes

Press any other key to exit.
```

6. Follow the instructions for each option to perform the desired operation.

7. To exit the program, press any key other than the available options.

## Options

1. **Show a member's information**: Using this option, the program asks for a user id. After the entry is validated, the user's information will be displayed

2. **Show a member's number of friends**: This option receives a user id and displays the number of friends for that member.

3. **Show a member's list of friends**: This option will list the id, first name, and last name of a given member's friends. 

4. **Recommend a friend for a member**: This option provides one recommended friend for a given user id based on shared connections.

5. **Search members by country**: Once this option is selected, the program will ask for a country name and lists all the members from that country.

6. **Add friend**: This option receives two members’ id and connects them. If the connection already exists, it displays an error message and asks the user to try again.

7. **Remove friend**: By selecting this option, the user will be asked to enter two members' ids. It also provides a list of the friends’ ids of the first member. If the two members are connected, their connection will be removed. If the two ids are not friends, an error message is displayed, and the user is asked to try again.

8. **Show graph**: This option allows you to visualize the social network as a graph.

![Graph Image](https://github.com/danielgao20/network-program/blob/main/project/graphview.png)

9. **Save changes**: The user will be asked to provide a file name by selecting this option. All the connections will be saved to the file in the format of the connection file. The new file must have the same format and structure as the original connection file. Pressing any other key will terminate the program.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.
