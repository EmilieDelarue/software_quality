# Création du dictionnaire d'entrée
# CALC_GR = {"<DIGIT>": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#            "<OPERATOR>": ["+", "*", "/", "-", "%"],
#            "<SEPARATOR>": ["(", ")", ".", "-"]}


EXPR_GRAMMAR = {
    "<start>":
        ["<expr>"],

    "<expr>":
        ["<term> + <expr>", "<term> - <expr>", "<term>"],

    "<term>":
        ["<factor> * <term>", "<factor> / <term>", "<factor>"],

    "<factor>":
        ["+<factor>",
         "-<factor>",
         "(<expr>)",
         "<integer>.<integer>",
         "<integer>"],

    "<OPERATOR>": ["+", "*", "/", "-", "%"],

    "<integer>":
        ["<digit><integer>", "<digit>"],

    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

