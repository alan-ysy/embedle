import json


def main():
    # Store as cluster : [word list]
    cluster_dict = {}

    # Read word list and parse clusters
    with open("word_lists/main_list.txt", "r") as word_list_file:
        for word in word_list_file:
            word = word.strip()  # Remove trailing '\n'

            word_clusters = set(find_clusters(word))  # Use set to avoid duplication
            for cluster in word_clusters:
                if cluster in cluster_dict:
                    cluster_dict[cluster].append(word)
                    # print(f'UPDATE: {cluster} : {word}')
                else:
                    cluster_dict[cluster] = [word]
                    # print(f'CREATE: {cluster} : {word}')

    # Save to JSON file
    with open("word_lists/clusters.json", "w") as cluster_file:
        json.dump(cluster_dict, cluster_file, indent=2)


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
