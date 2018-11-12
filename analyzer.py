import requests, sys, random, argparse

def main(initial, topics, iterations):
    seen_words = [initial]
    base_format_url = "https://api.datamuse.com/words?rel_trg={}&topics={}"
    start_url = base_format_url.format(initial, topics)
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
        curr_url = base_format_url.format(potential, topics)
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

if __name__ == '__main__':
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('--initial', '-s', default="hack", help="Initial word to start with")
    main_parser.add_argument('--topics', '-t', nargs=1, default="technology",
                             help="Comma separated topic list to make " \
                                  "sure the words are roughly related to")
    main_parser.add_argument('--iterations', '-i', required=True, type=int,
                             help="Number of iterations to go down")
    args = main_parser.parse_args()
    main(args.initial, args.topics, args.iterations)