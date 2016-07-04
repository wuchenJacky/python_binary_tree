import re;


def bulid_match_and_apply_functions(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return match_rule, apply_rule


def rules(rules_fileName):
    with open(rules_fileName, encoding="utf-8") as patterns:
        for line in patterns:
            pattern, search, replace = line.split(None, 3)
            yield bulid_match_and_apply_functions(pattern, search, replace)


def plural(noun, rules_fileName="plural4-rules.txt"):
    for match_rule, apply_rule in rules(rules_fileName):
        if match_rule(noun):
            return apply_rule(noun)
    raise ValueError(" no match rule for {0}".format(noun))


nouns = ("python", "appdata", "admin", "sex", "programs")
msps = map(plural, nouns)
for m in msps:
    print(m)
