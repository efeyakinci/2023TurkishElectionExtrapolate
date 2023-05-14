import json
from collections import defaultdict

votes = defaultdict(int)

'''
obp: Opened Ballots
tpc: Total voters
cdts->vp: voting percentage
'''

def process_votes(city):
    for district in city["districts"]:
        total_voters = district["tpc"]
        for candidate in district["cdts"]:
            cur_percentage = float(candidate["vp"])
            votes[candidate['cn']] += cur_percentage * int(total_voters) / 100



def main():
    for i in range(1, 81):
        with open("data/{}.json".format(i)) as file:
            data = file.read()
        city = json.loads(data)
        process_votes(city['data'])

    total_votes = sum(votes.values())
    for candidate, vote in votes.items():
        print("{}: {}%".format(candidate, vote / total_votes * 100))

if __name__ == "__main__":
    main()
