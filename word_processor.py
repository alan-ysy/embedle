import json


def main():
    # Store as cluster : [word list]
    cluster_dict = {}

    while True:
        read_file = input("Enter a file to read from: ")

        try:
            # Read word list and parse clusters
            with open(read_file, "r") as word_list_file:
                for word in word_list_file:
                    word = word.strip()  # Remove trailing '\n'

                    # Use set to avoid duplication
                    word_clusters = set(
                        find_clusters(word)
                    )  
                    for cluster in word_clusters:
                        if cluster in cluster_dict:
                            cluster_dict[cluster].append(word)
                            print(f"UPDATE: {cluster} : {word}")
                        else:
                            cluster_dict[cluster] = [word]
                            print(f"CREATE: {cluster} : {word}")
            break
        except FileNotFoundError:
            print("Error: Could not find file.")

    print("\nSuccessfully parsed word clusters.")

    while True:
        write_file = input("Enter a file to write to: ")

        try:
            # Save to JSON file
            with open(write_file, "w") as cluster_file:
                json.dump(cluster_dict, cluster_file, indent=2)
            break
        except FileNotFoundError:
            print("Error: Could not find file.")


# Takes in a string and a cluster length, returns a list of all clusters that word contains
def find_clusters(word, cluster_length=3):
    if len(word) < cluster_length:
        return []

    num_clusters = len(word) - (cluster_length - 1)

    cluster_list = []

    for i in range(num_clusters):
        cluster_list.append(word[i : i + cluster_length])

    return cluster_list


if __name__ == "__main__":
    main()
