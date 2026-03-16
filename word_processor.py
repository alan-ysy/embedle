import json

with open('word_lists/main_list.txt', 'r') as word_list_file:
    word_list = word_list_file.readlines()

    for word in word_list:
        pass

# Takes in a string and a cluster length, returns a list of all clusters that word contains
def find_clusters(word, cluster_length=3):
    num_clusters = len(word) - (cluster_length - 1)

    cluster_list = []

    for i in range(num_clusters):
        cluster_list.append(word[i:i+cluster_length])
    
    return cluster_list