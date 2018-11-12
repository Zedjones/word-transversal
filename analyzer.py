import requests, sys, random, argparse
from anytree import Node, RenderTree

BASE_FORMAT_URL = "https://api.datamuse.com/words?rel_trg={}&topics={}"

def random_iteration(initial, topics, iterations):
    seen_words = [initial]
    BASE_FORMAT_URL = "https://api.datamuse.com/words?rel_trg={}&topics={}"
    start_url = BASE_FORMAT_URL.format(initial, topics)
    response = requests.get(start_url)
    resp_json = response.json()
    curr_ind = random.randint(0, 3)
    potential = resp_json[curr_ind]['word']
    while potential in seen_words:
        curr_ind += 1
        potential = resp_json[curr_ind]['word']
    else:
        seen_words.append(potential)
    for _ in range(0, iterations):
        curr_url = BASE_FORMAT_URL.format(potential, topics)
        response = requests.get(curr_url)
        resp_json = response.json()
        curr_ind = random.randint(0, 3)
        potential = resp_json[curr_ind]['word']
        while potential in seen_words:
            curr_ind += 1
            potential = resp_json[curr_ind]['word']
        else:
            seen_words.append(potential)
    print(seen_words)

def layered_iteration(initial, topics, iterations):
    word_dict = {}
    root = Node(initial)
    word_dict[initial] = root
    start_url = BASE_FORMAT_URL.format(initial, topics)
    response = requests.get(start_url)
    synonyms = response.json()
    


if __name__ == '__main__':
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('--initial', '-s', default="hack", help="Initial word to start with")
    main_parser.add_argument('--topics', '-t', nargs=1, default="technology",
                             help="Comma separated topic list to make " \
                                  "sure the words are roughly related to")
    main_parser.add_argument('--iterations', '-i', required=True, type=int,
                             help="Number of iterations to go down")
    args = main_parser.parse_args()
    random_iteration(args.initial, args.topics, args.iterations)