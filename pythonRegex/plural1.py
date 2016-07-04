import re;
def bulid_match_and_apply_fucntions(pattern,search,replace):
    def matchs_rule(word):
        return re.search(pattern,word)
    def apply_rule(word):
        return re.sub(search,replace,word)
    return (matchs_rule,apply_rule)

patterns=(
    ("[sxz$]","$","es"),
    ("[^aeioudgkprt]h$","$","es"),
    ("(qu|[^aeiou])y$", "y$", "ies"),
    ("$", "$", "s")
)
rules=[bulid_match_and_apply_fucntions(pattern,search,replace) for (pattern,search,replace) in patterns]
for match,apply in rules:
   if match("sexs"):
       print(apply("sexs"))