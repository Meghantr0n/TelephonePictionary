import json
import uuid


def make_unique_id():
    return str(uuid.uuid4())[:8]

def save_game(state):
    """
    :param state: a completed turn of a game that I want to save  
    :return: None
    """
    filename = state['game']+'.json'
    with open(filename, 'w') as f:
        json.dump(state, f, indent=4)

def open_game(game):
    filename = game + '.json'
    with open(filename, 'r') as f:
        return json.load(f)

def example():
    return {'game': make_unique_id(),
             'turn': [
                 {'player': 1,
                  'phrase': 'pusheen',
                  'picture': 'https://media.giphy.com/media/TN0kjxBsz3iXm/giphy.gif'},
                 {'player': 2,
                  'phrase': 'pair of boots',
                  'picture': 'www.google.com'},
                 {'player': 3,
                  'phrase': 'flock of seagulls',
                  'picture': 'www.google.com'},
             ]}

if __name__ == '__main__':

    # example of saving a game
    state = example()
    save_game(state)

    # example of opening a saved game
    # game = 'eb806ec5'
    # state = open_game(game)

    print state

