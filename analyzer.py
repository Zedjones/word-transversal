import requests, sys

def main(iterations):
    seen_words = ['hack']
    base_format_url = "https://api.datamuse.com/words?rel_trg={}&topics=computer,hack,mechanics"
    start_url = base_format_url.format("hack")
    response = requests.get(start_url)
    resp_json = response.json()
    curr_ind = 0
    potential = resp_json[curr_ind]['word']
    while potential in seen_words:
        curr_ind += 1
        potential = resp_json[curr_ind]['word']
    else:
        seen_words.append(potential)
    print(potential)
    for _ in range(0, iterations):
        curr_url = base_format_url.format(potential)
        response = requests.get(curr_url)
        resp_json = response.json()
        curr_ind = 0
        potential = resp_json[curr_ind]['word']
        while potential in seen_words:
            curr_ind += 1
            potential = resp_json[curr_ind]['word']
        else:
            seen_words.append(potential)
        print(potential)

if __name__ == '__main__':
    iterations = int(sys.argv[1])
    main(iterations)