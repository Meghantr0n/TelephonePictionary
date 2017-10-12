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

def example_game():
    return {'game': make_unique_id(),
            'player': {
                1:'http://TelephonePictionary.info/meghatr0n',
                2:'http://spectacle.press/lemons',
                3:'http://spectacle.press/pandora'},
             'turn':

             [ # 1 First Turn
                [{'player': 1,
                  'phrase': 'pusheen',
                  'picture': 'https://media.giphy.com/media/TN0kjxBsz3iXm/giphy.gif'},
                 {'player': 2,
                  'phrase': 'pair of boots',
                  'picture': 'www.google.com'},
                 {'player': 3,
                  'phrase': 'flock of seagulls',
                  'picture': 'www.google.com'}],

            [ # 2 Second Turn
                {'player': 1,
                  'phrase': 'socrates',
                  'picture': 'http://news.gtp.gr/wp-content/uploads/2017/07/Socrates-NOW.jpg'},
                 {'player': 2,
                  'phrase': 'chrysanthemum',
                  'picture': 'https://fthmb.tqn.com/FMIdhFc5CLsznxCy37_VqMTI91I=/768x0/filters:no_upscale()/chrysanthemum-drawing-56a26d0d5f9b58b7d0ca2430.png'},
                 {'player': 3,
                  'phrase': 'dog sled',
                  'picture': 'http://newsdesk.si.edu/sites/default/files/imagecache/snapshot_image/dog-sled.jpg'}]]}

if __name__ == '__main__':

    # example of saving a game
    state = example_game()
    save_game(state)

    # example of opening a saved game
    # game = 'eb806ec5'
    # state = open_game(game)

    print(state)

