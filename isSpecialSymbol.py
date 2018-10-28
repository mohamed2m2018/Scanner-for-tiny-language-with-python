specialSymbols=[  {"sign": "+",
                  "label":"add"
                 },{"sign": "-",
                  "label":"minus"
                 },
                 {"sign": "μ",
                  "label":"multiply"
                 },
                 {"sign": "divide",
                  "label":"/"
                 },
                 {"sign": "=",
                  "label":"equal"
                 },
                 {"sign": "<",
                  "label":"smaller than"
                 },
                 {"sign": "(",
                  "label":"left bracket"
                 },
                 {"sign": ")",
                  "label":"right bracket"
                 },
                 {"sign": ";",
                  "label":"semicolon"
                 },
                 {"sign": "α",
                  "label":"assign"
                 }]
def isSpecialSymbol(word):
    for special in specialSymbols:
        if(word==special['sign']):
            return True
def checkSymbol (word):
    for special in specialSymbols:
        if(word==special['sign']):
            return special['label'];
