import os

def prepare_space(file):
    if os.path.isfile(file):
        os.remove(file)
        print(f"File {file} from previous analysis has been removed")
    else:
        pass


def import_database(path):

    dictionary = dict()

    for root, dirs, files in os.walk(path):
        for file in files:
            names = file.split('.')
            if file.endswith('.xml'):
                with open(os.path.join(root, file), 'r') as f:
                    text = f.read()
                    dictionary[names[0]] = text

    return dictionary
