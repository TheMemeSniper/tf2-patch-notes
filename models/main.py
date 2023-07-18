import markovify

def generate():

        with open("data/patchnotes.txt") as f:
                text = f.read()

        text_model = markovify.NewlineText(text, state_size=2)

        return text_model.make_sentence(max_overlap_ratio=1, max_overlap_total=10, tries=1000)

if __name__ == "__main__":
        print(generate())