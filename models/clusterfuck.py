import markovify

def generate(state):

        with open("data/patchnotes.txt") as f:
                text1 = f.read()


        with open("data/worsepatchnotes.txt") as f:
                text2 = f.read()

        text_model1 = markovify.NewlineText(text1, state_size=state)
        text_model2 = markovify.NewlineText(text2, state_size=state)

        combined = markovify.combine([text_model1, text_model2])


        return combined.make_sentence(max_overlap_ratio=1, max_overlap_total=15, tries=1000)

if __name__ == "__main__":
        from sys import argv
        print(generate(int(argv[1])))

