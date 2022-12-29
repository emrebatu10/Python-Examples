import pandas as pd
import itertools, time, string

fname = "enable1.txt"

def read_in_word_list(fname):
    data = []
    with open(fname, "r") as word_list:
        for w in word_list:
            w = w.rstrip('\n')
            l_used = "".join(sorted(list(set(w))))
            if len(w) >= 4 and len(l_used) <= 7 and "s" not in w:
                points = len(w) + 7 * (len(l_used) == 7)
                data.append([w,l_used,points])

    df = pd.DataFrame(data=data, columns = ["word","letters","points"])
    return df

def create_sub_lists(df):
    for l in string.ascii_lowercase:
        filtered_df = df[df['letters'].str.contains(l)]
        filtered_df['letters'].replace(l,"", regex=True, inplace=True)
        sub_fname = 'C:/Users/Tyler/PycharmProjects/spelling_bee/venv/sub_dicts/'
        filtered_df.to_csv(sub_fname+l+".csv")

def evaluate_hive(hub,letters):
    points = 0
    sub_df = pd.read_csv("./sub_dicts/"+hub+".csv")
    for i in range(len(sub_df)):
        line = sub_df.iloc[i]

        successful = True
        for l in line.letters:
            if not (successful and ((l in letters) or l == hub)):
                successful = False
        if successful: points += int(line.points)

    return points

def evaluate_hive_faster(hub,letters):
    sub_df = pd.read_csv("./sub_dicts/"+hub+".csv")
    not_letters = "etaoinhrdlcumwfgypbvkjxqz"
    for i in letters:
        not_letters = not_letters.replace(i, "")
    not_letters = not_letters.replace(hub, "")

    for n_l in not_letters:
        sub_df = sub_df[~sub_df['letters'].str.contains(n_l)]
    points = sub_df.points.sum()
    return points

def evaluate_hive_fasterer(hub,letters):
    temp_df = sub_df
    not_letters = "etaoinhrdlcumwfgypbvkjxqz"
    for i in letters:
        not_letters = not_letters.replace(i, "")
    not_letters = not_letters.replace(hub, "")

    for n_l in not_letters:
        temp_df = temp_df[~temp_df['letters'].str.contains(n_l)]
    points = temp_df.points.sum()

    return points

def evaluate_hive_fastererer(hub,letters):
    not_letters = "etaoinhrdlcumwfgypbvkjxqz"
    for i in letters:
        not_letters = not_letters.replace(i, "")
    not_letters = not_letters.replace(hub, "")
    not_letters = not_letters.replace("", "|")[1: -1]

    temp_df = sub_df[~sub_df['letters'].str.contains(not_letters)]

    temp_df.to_csv("best_one.csv")
    points = temp_df.points.sum()

    return points

def run_permutations():
    t = time.time()

    for hub in string.ascii_lowercase:
        sub_df = pd.read_csv("./sub_dicts/" + hub + ".csv")
        valid_letters = string.ascii_lowercase
        valid_letters = valid_letters.replace(hub, "")
        valid_letters = valid_letters.replace("s", "")

        letter_combos = itertools.combinations(valid_letters, 6)

        data = []
        for l_c in letter_combos:
            pt = evaluate_hive_fastererer(hub, l_c)
            data.append([hub, l_c, pt])
            # print(hub,"_","".join(l_c),"  ",pt)

            if len(data) % 1000 == 0:
                print(len(data), " , ", str(time.time() - t))

        temp_df = pd.DataFrame(data=data, columns=['hub', 'letters', 'points'])
        temp_df.to_csv(hub + ".csv")

def report_results():
    best = 0
    for hub in string.ascii_lowercase:
        sub_df = pd.read_csv(hub + ".csv")
        sub_df = sub_df.sort_values(by=['points'], ascending=False)
        if sub_df.iloc[0].points > best:
            best = sub_df.iloc[0].points
            print(sub_df.iloc[0])


### use this to generate the sub dictionaries
df = read_in_word_list(fname)
create_sub_lists(df)

### run all the permutations
run_permutations()

###report results
report_results()


###use this to find all the words associated with the end
sub_df = pd.read_csv("./sub_dicts/" + "r" + ".csv")
evaluate_hive_fastererer("r",'aegint')