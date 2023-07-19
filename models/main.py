import markovify

def generate(state):

        with open("data/patchnotes.txt") as f:
                text = f.read()

        text_model = markovify.NewlineText(text, state_size=state)

        return text_model.make_sentence(max_overlap_ratio=1, max_overlap_total=15, tries=1000)

if __name__ == "__main__":
        from sys import argv
        print(generate(int(argv[1])))