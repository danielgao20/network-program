# NAME: <Daniel Gao>
# DATE: 2023-04-25
# DESCRIPTION: Assignment 14, for practice OOP programming

from Graph import *
from typing import IO, Tuple, List, Dict

PROGRAMMER = "Daniel Gao"
MEMBER_INFO = "1"
NUM_OF_FRIENDS = "2"
LIST_OF_FRIENDS = "3"
RECOMMEND = "4"
SEARCH = "5"
ADD_FRIEND = "6"
REMOVE_FRIEND = "7"
SHOW_GRAPH = "8"
SAVE = "9"

LINE = "\n-------------------------------------------------------------\n"


class Member:
    # The following function initializes a Member object
    def __init__(self, member_id: int, first_name: str, last_name: str, email: str, country: str):
        """
        The following code initializes a Member object
        """
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
        self.friends_id_list = []

    # Check if the friend is not already in the list
    def add_friend(self, friend_id) -> None:
        """
        Add if the friend is not already in the list
        """
        if friend_id not in self.friends_id_list:
            self.friends_id_list.append(friend_id)
            self.friends_id_list.sort()

    # Check if the friend is in the list
    def remove_friend(self, friend_id) -> None:
        """
        Remove if the friend is in the list
        """
        if friend_id in self.friends_id_list:
            self.friends_id_list.remove(friend_id)

    # Complete according to the output sample in the handout
    def __str__(self) -> str:
        """
        Display according to the output sample in the handout
        """
        member_info = f"{self.member_id}\n" \
                      f"{self.first_name} " \
                      f"{self.last_name}\n" \
                      f"{self.email}\nFrom " \
                      f"{self.country}\nHas " \
                      f"{len(self.friends_id_list)} friends."
        return member_info

    # Must return the complete name
    def display_name(self) -> str:
        """
        Return the complete name
        """
        return f"{self.first_name} {self.last_name}"


def open_file(file_type: str) -> IO:
    """
    Opens the file
    """
    if file_type == "profile":
        file_name = "profile_10.csv"
    else:
        file_name = "connection_10.txt"
    file_pointer = None
    while file_pointer is None:
        file_name = input("Enter the " + file_type + " filename:\n")
        try:
            file_pointer = open(file_name, 'r')
        except IOError:
            print(f"An error occurred while opening the file {file_name}.\n"
                  f"Make sure the file path and name are correct \nand that "
                  f"the file exist and is readable.")

    return file_pointer


def create_network(fp: IO) -> Dict[int, List[int]]:
    """
    Function creates and returns a dictionary representing a network where keys are
    member IDs and values are lists of their friends' IDs.
    """
    size = int(fp.readline())
    network = {}

    for i in range(size):
        network[i] = []

    for line in fp:
        split_line = line.strip().split(" ")
        member_id1 = int(split_line[0])
        member_id2 = int(split_line[1])
        network[member_id1].append(member_id2)
        network[member_id2].append(member_id1)

    return network


def num_in_common_between_lists111(list1: List, list2: List) -> int:
    """
    Returns the number of elements that two lists have in common.
    """
    degree = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            degree += 1

    return degree


def common_degree(list1: List, list2: List) -> int:
    """
    Calculate the common degree of two lists, which is the number of elements they share.
    """
    degree = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            degree += 1

    return degree


def init_matrix(size: int) -> List[List[int]]:
    """
    Initialize a square matrix of zeroes with the given size.
    """
    matrix = []
    for row in range(size):
        matrix.append([])
        for column in range(size):
            matrix[row].append(0)

    return matrix


# This function calculates the similarity scores between each pair of members in the social network
def calc_similarity_scores(network: Dict[int, List[int]]) -> List[List[int]]:
    similarity_matrix = init_matrix(len(network))
    """
    Calculates the similarity scores between each pair of members in the social network and 
    returns a matrix of these scores.
    """
    # Iterate through the network and calculate the similarity scores between each pair of members
    for i in range(len(network)):
        for j in range(i, len(network)):
            degree = common_degree(network[i], network[j])
            similarity_matrix[i][j] = degree
            similarity_matrix[j][i] = degree

    return similarity_matrix


def recommend(member_id: int, friend_list: List[int], similarity_list: List[int]) -> int:
    """
    Recommends a friend to a given member based on a list of friends and a similarity list.
    """
    max_similarity_val = -1
    max_similarity_pos = -1

    for i in range(len(similarity_list)):
        if i not in friend_list and i != member_id:
            if max_similarity_val < similarity_list[i]:
                max_similarity_pos = i
                max_similarity_val = similarity_list[i]

    return max_similarity_pos


# This function creates a list of Member objects from the given profile file
def create_members_list(profile_fp: IO) -> List[Member]:
    """
    Creates a list of Member objects from the given profile file.
    """
    profiles = []
    profile_fp.readline()  # skip the first line
    line = profile_fp.readline().strip()

    # Iterate through the file and create a Member object for each line
    while line:
        profile_list = line.split(',')
        if len(profile_list) == 5:
            member = Member(int(profile_list[0]), profile_list[1], profile_list[2], profile_list[3], profile_list[4])
            profiles.append(member)
        line = profile_fp.readline().strip()

    return profiles


# This function displays all the options for the user to select from
def display_menu():
    """
    A function to display a menu of options for the user to select from.
    """
    print("\nPlease select one of the following options.\n")
    print(MEMBER_INFO + ". Show a member's information \n" +
          NUM_OF_FRIENDS + ". Show a member's number of friends\n" +
          LIST_OF_FRIENDS + ". Show a member's list of friends\n" +
          RECOMMEND + ". Recommend a friend for a member\n" +
          SEARCH + ". Search members by country\n" +
          ADD_FRIEND + ". Add friend\n" +
          REMOVE_FRIEND + ". Remove friend\n" +
          SHOW_GRAPH + ". Show graph\n" +
          SAVE + ". Save changes\n")

    return input("Press any other key to exit.\n")


# This function receives and validates the user's menu selection
def receive_verify_member_id(size: int):
    """
    Receive and validate a member id input from the user.
    """
    valid = False
    while not valid:
        member_id = input(f"Please enter a member id between 0 and {size - 1}:\n")
        if not member_id.isdigit():
            print("This is not a valid entry.")
        elif not 0 <= int(member_id) < size:
            print("This member id does not exist.")
        else:
            valid = True

    return int(member_id)


# This function adds a new friendship connection between two members in the given profile list
def add_friend(profile_list: List[Member],
               similarity_matrix: List[List[int]]) -> None:
    """
    Adds a new friendship connection between two members in the given profile list
    and updates the similarity matrix accordingly.
    """
    size = len(profile_list)
    print("For the first friend: ")
    member1 = receive_verify_member_id(size)
    print("For the second friend: ")
    member2 = receive_verify_member_id(size)

    # Check if the two members are already friends
    if member1 == member2:
        print("You need to enter two different ids. Please try again.")
    elif member1 in profile_list[member2].friends_id_list:
        print("These two members are already friends. Please try again.")
    else:
        for f_id in profile_list[member2].friends_id_list:
            similarity_matrix[member1][f_id] += 1
            similarity_matrix[f_id][member1] += 1

        for f_id in profile_list[member1].friends_id_list:
            similarity_matrix[member2][f_id] += 1
            similarity_matrix[f_id][member2] += 1

        profile_list[member1].add_friend(member2)
        profile_list[member2].add_friend(member1)

        similarity_matrix[member1][member1] += 1
        similarity_matrix[member2][member2] += 1

        print("The connection is added. Please check the graph.")


# This function removes a friend connection between two members, updating their friend lists
def remove_friend(profile_list: List[Member],
                  similarity_matrix: List[List[int]]) -> None:
    """
    Remove a friend connection between two members, updating their friend lists
    and similarity matrix accordingly.
    """
    size = len(profile_list)
    print("For the first friend: ")
    member1 = receive_verify_member_id(size)
    print("For the second friend: ")
    member2 = receive_verify_member_id(size)

    # Check if the two members are already friends
    if member1 == member2:
        print("You need to enter two different ids. Please try again.")
    elif member1 not in profile_list[member2].friends_id_list:
        print("These two members are not friends. Please try again.")
    else:
        for f_id in profile_list[member2].friends_id_list:
            similarity_matrix[member1][f_id] -= 1
            similarity_matrix[f_id][member1] -= 1

        for f_id in profile_list[member1].friends_id_list:
            similarity_matrix[member2][f_id] -= 1
            similarity_matrix[f_id][member2] -= 1

        profile_list[member1].remove_friend(member2)
        profile_list[member2].remove_friend(member1)

        similarity_matrix[member1][member1] -= 1
        similarity_matrix[member2][member2] -= 1

        print("The connection is removed. Please check the graph.")


# This function searches for members of a social network based on their country of origin
def search(profile_list: List[Member]) -> None:
    """
    Searches for members of a social network based on their country of origin.
    """
    country = input("Please enter the country you want to search:\n")
    count = 0
    for member in profile_list:
        if member.country.lower() == country.lower():
            print(member.display_name())
            count += 1
    if count == 0:
        print(f"No member is found from {country}.")


def add_friends_to_profiles(profile_list: List[Member],
                            network: List[List[int]]) -> None:
    """
    Adds friends to profiles in a list of Member objects based on their corresponding IDs in a network.
    """
    for i in range(len(profile_list)):
        profile_list[i].friends_id_list = network[i]


# This function performs an action on the social network based on user's selection
def select_action(profile_list: List[Member],
                  network: List[List[int]],
                  similarity_matrix: List[List[int]]) -> str:
    """
    Performs an action on the social network based on user's selection.
    """
    response = display_menu()

    print(LINE)
    size = len(profile_list)

    # Receives and validates the member id if the action requires it
    if response in [MEMBER_INFO, NUM_OF_FRIENDS, LIST_OF_FRIENDS, RECOMMEND]:
        member_id = receive_verify_member_id(size)

    # Carries out the action based on user's selection
    if response == MEMBER_INFO:
        print(profile_list[member_id])
    elif response == NUM_OF_FRIENDS:
        print(f"{profile_list[member_id].first_name} has {len(profile_list[member_id].friends_id_list)} Friends.")
    elif response == LIST_OF_FRIENDS:
        for i, friend_id in enumerate(profile_list[member_id].friends_id_list):
            print(f"{friend_id} {profile_list[friend_id].display_name()}")
    elif response == RECOMMEND:
        recommended_friend = recommend(int(member_id), network[int(member_id)], similarity_matrix[int(member_id)])
        print(
            f"The suggested friend for {profile_list[member_id].display_name()} is {profile_list[recommended_friend].display_name()} with id {recommended_friend}")
    elif response == SEARCH:
        search(profile_list)
    elif response == ADD_FRIEND:
        add_friend(profile_list, similarity_matrix)
    elif response == REMOVE_FRIEND:
        remove_friend(profile_list, similarity_matrix)
    elif response == SHOW_GRAPH:
        tooltip_list = []
        for profile in profile_list:
            tooltip_list.append(profile)
        print("network fr graph", network)
        graph = Graph(PROGRAMMER,
                      [*range(len(profile_list))],
                      tooltip_list, network)
        graph.draw_graph()
        print("Graph is ready. Please check your browser.")
    elif response == SAVE:
        save_changes(profile_list)
    else:
        return "Exit"

    print(LINE)

    return "Continue"


# This function saves all changes made to network in a file selected by user
def save_changes(profile_list: List[Member]) -> None:
    """
    Saves all changes made to network in a file selected by user.
    """
    filename = input("Please enter the filename to save changes: ")
    with open(filename, "w") as file:
        # Write the header row
        file.write("MemberID,First Name,Last Name,Email,Country,Friends\n")

        # Write each member's information
        for member in profile_list:
            friend_ids = ",".join(str(friend_id) for friend_id in member.friends_id_list)
            file.write(
                f"{member.member_id},{member.first_name},{member.last_name},{member.email},{member.country},{friend_ids}\n")

    print(f"All changes are saved in {filename}")


def initialization() -> Tuple[List[Member], List[List[int]], List[List[int]]]:
    """
    Initialize the social network by reading data from the "profile" and "connection" files,
    creating a list of Member objects, a network adjacency matrix, and a similarity score matrix.
    """
    profile_fp = open_file("profile")
    profile_list = create_members_list(profile_fp)

    connection_fp = open_file("connection")
    network = create_network(connection_fp)
    if len(network) != len(profile_list):
        input("Both files must have the same number of members.\n"
              "Please try again.")
        exit()

    add_friends_to_profiles(profile_list, network)
    similarity_matrix = calc_similarity_scores(network)

    profile_fp.close()
    connection_fp.close()

    return profile_list, network, similarity_matrix


def main():
    print("Welcome to the network program.")
    print("We need two data files.")
    profile_list, network, similarity_matrix = initialization()

    action = "Continue"
    while action != "Exit":
        action = select_action(profile_list, network, similarity_matrix)

    input("Thanks for using this program.")


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()
