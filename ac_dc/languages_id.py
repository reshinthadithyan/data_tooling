import pandas as pd

langs_id = [
    {
        "lang": "Afrikaans",
        "oscar_id": "af",
        "nltk_id": None,
        "kenlm_id": "af",
        "fasttext_id": "af",
        "badwords_id": None,
    },
    {
        "lang": "Tosk Albanian",
        "oscar_id": "als",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "als",
        "badwords_id": None,
    },
    {
        "lang": "Amharic",
        "oscar_id": "am",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "am",
        "badwords_id": None,
    },
    {
        "lang": "Aragonese",
        "oscar_id": "an",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "an",
        "badwords_id": None,
    },
    {
        "lang": "Arabic",
        "oscar_id": "ar",
        "nltk_id": "arabic",
        "kenlm_id": "ar",
        "fasttext_id": "ar",
        "badwords_id": None,
    },
    {
        "lang": "Egyptian Arabic",
        "oscar_id": "arz",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "arz",
        "badwords_id": None,
    },
    {
        "lang": "Asturian",
        "oscar_id": "ast",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ast",
        "badwords_id": None,
    },
    {
        "lang": "Assamese",
        "oscar_id": "as",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "as",
        "badwords_id": None,
    },
    {
        "lang": "Avaric",
        "oscar_id": "av",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "av",
        "badwords_id": None,
    },
    {
        "lang": "South Azerbaijani",
        "oscar_id": "azb",
        "nltk_id": "azerbaijani",
        "kenlm_id": None,
        "fasttext_id": "azb",
        "badwords_id": None,
    },
    {
        "lang": "Azerbaijani",
        "oscar_id": "az",
        "nltk_id": "azerbaijani",
        "kenlm_id": "az",
        "fasttext_id": "az",
        "badwords_id": None,
    },
    {
        "lang": "Bavarian",
        "oscar_id": "bar",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "bar",
        "badwords_id": None,
    },
    {
        "lang": "Bashkir",
        "oscar_id": "ba",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ba",
        "badwords_id": None,
    },
    {
        "lang": "Central Bikol",
        "oscar_id": "bcl",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "bcl",
        "badwords_id": None,
    },
    {
        "lang": "Belarusian",
        "oscar_id": "be",
        "nltk_id": None,
        "kenlm_id": "be",
        "fasttext_id": "be",
        "badwords_id": "be",
    },
    {
        "lang": "Bulgarian",
        "oscar_id": "bg",
        "nltk_id": None,
        "kenlm_id": "bg",
        "fasttext_id": "bg",
        "badwords_id": "bg",
    },
    {
        "lang": "Bihari",
        "oscar_id": "bh",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "bh",
        "badwords_id": None,
    },
    {
        "lang": "Bengali",
        "oscar_id": "bn",
        "nltk_id": "bengali",
        "kenlm_id": "bn",
        "fasttext_id": "bn",
        "badwords_id": None,
    },
    {
        "lang": "Tibetan",
        "oscar_id": "bo",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "bo",
        "badwords_id": None,
    },
    {
        "lang": "Bishnupriya",
        "oscar_id": "bpy",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "bpy",
        "badwords_id": None,
    },
    {
        "lang": "Breton",
        "oscar_id": "br",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "br",
        "badwords_id": None,
    },
    {
        "lang": "Bosnian",
        "oscar_id": "bs",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "bs",
        "badwords_id": None,
    },
    {
        "lang": "Russia Buriat",
        "oscar_id": "bxr",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "bxr",
        "badwords_id": None,
    },
    {
        "lang": "Catalan",
        "oscar_id": "ca",
        "nltk_id": None,
        "kenlm_id": "ca",
        "fasttext_id": "ca",
        "badwords_id": "ca",
    },
    {
        "lang": "Chavacano",
        "oscar_id": "cbk",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "cbk",
        "badwords_id": None,
    },
    {
        "lang": "Cebuano",
        "oscar_id": "ceb",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ceb",
        "badwords_id": None,
    },
    {
        "lang": "Chechen",
        "oscar_id": "ce",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ce",
        "badwords_id": None,
    },
    {
        "lang": "Central Kurdish",
        "oscar_id": "ckb",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ckb",
        "badwords_id": None,
    },
    {
        "lang": "Czech",
        "oscar_id": "cs",
        "nltk_id": None,
        "kenlm_id": "cs",
        "fasttext_id": "cs",
        "badwords_id": "cs",
    },
    {
        "lang": "Chuvash",
        "oscar_id": "cv",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "cv",
        "badwords_id": None,
    },
    {
        "lang": "Welsh",
        "oscar_id": "cy",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "cy",
        "badwords_id": "cy",
    },
    {
        "lang": "Danish",
        "oscar_id": "da",
        "nltk_id": "danish",
        "kenlm_id": "da",
        "fasttext_id": "da",
        "badwords_id": "da",
    },
    {
        "lang": "German",
        "oscar_id": "de",
        "nltk_id": "german",
        "kenlm_id": "de",
        "fasttext_id": "de",
        "badwords_id": "de",
    },
    {
        "lang": "Dimli",
        "oscar_id": "diq",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "diq",
        "badwords_id": None,
    },
    {
        "lang": "Lower Sorbian",
        "oscar_id": "dsb",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "dsb",
        "badwords_id": None,
    },
    {
        "lang": "Dhivehi",
        "oscar_id": "dv",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "dv",
        "badwords_id": None,
    },
    {
        "lang": "Modern Greek",
        "oscar_id": "el",
        "nltk_id": "greek",
        "kenlm_id": "el",
        "fasttext_id": "el",
        "badwords_id": "el",
    },
    {
        "lang": "Emilian-Romagnol",
        "oscar_id": "eml",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "eml",
        "badwords_id": None,
    },
    {
        "lang": "English",
        "oscar_id": "en",
        "nltk_id": "english",
        "kenlm_id": "en",
        "fasttext_id": "en",
        "badwords_id": "en",
    },
    {
        "lang": "Esperanto",
        "oscar_id": "eo",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "eo",
        "badwords_id": None,
    },
    {
        "lang": "Spanish",
        "oscar_id": "es",
        "nltk_id": "spanish",
        "kenlm_id": "es",
        "fasttext_id": "es",
        "badwords_id": "es",
    },
    {
        "lang": "Estonian",
        "oscar_id": "et",
        "nltk_id": None,
        "kenlm_id": "et",
        "fasttext_id": "et",
        "badwords_id": "et",
    },
    {
        "lang": "Basque",
        "oscar_id": "eu",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "eu",
        "badwords_id": "eu",
    },
    {
        "lang": "Persian",
        "oscar_id": "fa",
        "nltk_id": None,
        "kenlm_id": "fa",
        "fasttext_id": "fa",
        "badwords_id": "fa",
    },
    {
        "lang": "Finnish",
        "oscar_id": "fi",
        "nltk_id": "finnish",
        "kenlm_id": "fi",
        "fasttext_id": "fi",
        "badwords_id": "fi",
    },
    {
        "lang": "Northern Frisian",
        "oscar_id": "frr",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "frr",
        "badwords_id": None,
    },
    {
        "lang": "French",
        "oscar_id": "fr",
        "nltk_id": "french",
        "kenlm_id": "fr",
        "fasttext_id": "fr",
        "badwords_id": "fr",
    },
    {
        "lang": "Western Frisian",
        "oscar_id": "fy",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "fy",
        "badwords_id": None,
    },
    {
        "lang": "Irish",
        "oscar_id": "ga",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ga",
        "badwords_id": None,
    },
    {
        "lang": "Scottish Gaelic",
        "oscar_id": "gd",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "gd",
        "badwords_id": "gd",
    },
    {
        "lang": "Galician",
        "oscar_id": "gl",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "gl",
        "badwords_id": "gl",
    },
    {
        "lang": "Guarani",
        "oscar_id": "gn",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "gn",
        "badwords_id": None,
    },
    {
        "lang": "Goan Konkani",
        "oscar_id": "gom",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "gom",
        "badwords_id": None,
    },
    {
        "lang": "Gujarati",
        "oscar_id": "gu",
        "nltk_id": None,
        "kenlm_id": "gu",
        "fasttext_id": "gu",
        "badwords_id": None,
    },
    {
        "lang": "Hebrew",
        "oscar_id": "he",
        "nltk_id": None,
        "kenlm_id": "he",
        "fasttext_id": "he",
        "badwords_id": None,
    },
    {
        "lang": "Hindi",
        "oscar_id": "hi",
        "nltk_id": None,
        "kenlm_id": "hi",
        "fasttext_id": "hi",
        "badwords_id": "hi",
    },
    {
        "lang": "Croatian",
        "oscar_id": "hr",
        "nltk_id": None,
        "kenlm_id": "hr",
        "fasttext_id": "hr",
        "badwords_id": "hr",
    },
    {
        "lang": "Upper Sorbian",
        "oscar_id": "hsb",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "hsb",
        "badwords_id": None,
    },
    {
        "lang": "Haitian",
        "oscar_id": "ht",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ht",
        "badwords_id": None,
    },
    {
        "lang": "Hungarian",
        "oscar_id": "hu",
        "nltk_id": "hungarian",
        "kenlm_id": "hu",
        "fasttext_id": "hu",
        "badwords_id": "hu",
    },
    {
        "lang": "Armenian",
        "oscar_id": "hy",
        "nltk_id": None,
        "kenlm_id": "hy",
        "fasttext_id": "hy",
        "badwords_id": "hy",
    },
    {
        "lang": "Interlingua",
        "oscar_id": "ia",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ia",
        "badwords_id": None,
    },
    {
        "lang": "Indonesian",
        "oscar_id": "id",
        "nltk_id": "indonesian",
        "kenlm_id": "id",
        "fasttext_id": "id",
        "badwords_id": "id",
    },
    {
        "lang": "Interlingue",
        "oscar_id": "ie",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ie",
        "badwords_id": None,
    },
    {
        "lang": "Iloko",
        "oscar_id": "ilo",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ilo",
        "badwords_id": None,
    },
    {
        "lang": "Ido",
        "oscar_id": "io",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "io",
        "badwords_id": None,
    },
    {
        "lang": "Icelandic",
        "oscar_id": "is",
        "nltk_id": None,
        "kenlm_id": "is",
        "fasttext_id": "is",
        "badwords_id": "is",
    },
    {
        "lang": "Italian",
        "oscar_id": "it",
        "nltk_id": "italian",
        "kenlm_id": "it",
        "fasttext_id": "it",
        "badwords_id": "it",
    },
    {
        "lang": "Japanese",
        "oscar_id": "ja",
        "nltk_id": None,
        "kenlm_id": "ja",
        "fasttext_id": "ja",
        "badwords_id": "ja",
    },
    {
        "lang": "Lojban",
        "oscar_id": "jbo",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "jbo",
        "badwords_id": None,
    },
    {
        "lang": "Javanese",
        "oscar_id": "jv",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "jv",
        "badwords_id": None,
    },
    {
        "lang": "Georgian",
        "oscar_id": "ka",
        "nltk_id": None,
        "kenlm_id": "ka",
        "fasttext_id": "ka",
        "badwords_id": None,
    },
    {
        "lang": "Kazakh",
        "oscar_id": "kk",
        "nltk_id": "kazakh",
        "kenlm_id": "kk",
        "fasttext_id": "kk",
        "badwords_id": None,
    },
    {
        "lang": "Central Khmer",
        "oscar_id": "km",
        "nltk_id": None,
        "kenlm_id": "km",
        "fasttext_id": "km",
        "badwords_id": None,
    },
    {
        "lang": "Kannada",
        "oscar_id": "kn",
        "nltk_id": None,
        "kenlm_id": "kn",
        "fasttext_id": "kn",
        "badwords_id": "kn",
    },
    {
        "lang": "Korean",
        "oscar_id": "ko",
        "nltk_id": None,
        "kenlm_id": "ko",
        "fasttext_id": "ko",
        "badwords_id": "ko",
    },
    {
        "lang": "Karachay-Balkar",
        "oscar_id": "krc",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "krc",
        "badwords_id": None,
    },
    {
        "lang": "Kurdish",
        "oscar_id": "ku",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ku",
        "badwords_id": None,
    },
    {
        "lang": "Komi",
        "oscar_id": "kv",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "kv",
        "badwords_id": None,
    },
    {
        "lang": "Cornish",
        "oscar_id": "kw",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "kw",
        "badwords_id": None,
    },
    {
        "lang": "Kirghiz",
        "oscar_id": "ky",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ky",
        "badwords_id": None,
    },
    {
        "lang": "Latin",
        "oscar_id": "la",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "la",
        "badwords_id": "la",
    },
    {
        "lang": "Luxembourgish",
        "oscar_id": "lb",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "lb",
        "badwords_id": None,
    },
    {
        "lang": "Lezghian",
        "oscar_id": "lez",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "lez",
        "badwords_id": None,
    },
    {
        "lang": "Limburgan",
        "oscar_id": "li",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "li",
        "badwords_id": None,
    },
    {
        "lang": "Lombard",
        "oscar_id": "lmo",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "lmo",
        "badwords_id": None,
    },
    {
        "lang": "Lao",
        "oscar_id": "lo",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "lo",
        "badwords_id": None,
    },
    {
        "lang": "Northern Luri",
        "oscar_id": "lrc",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "lrc",
        "badwords_id": None,
    },
    {
        "lang": "Lithuanian",
        "oscar_id": "lt",
        "nltk_id": None,
        "kenlm_id": "lt",
        "fasttext_id": "lt",
        "badwords_id": "lt",
    },
    {
        "lang": "Latvian",
        "oscar_id": "lv",
        "nltk_id": None,
        "kenlm_id": "lv",
        "fasttext_id": "lv",
        "badwords_id": "lv",
    },
    {
        "lang": "Maithili",
        "oscar_id": "mai",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "mai",
        "badwords_id": None,
    },
    {
        "lang": "Malagasy",
        "oscar_id": "mg",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "mg",
        "badwords_id": None,
    },
    {
        "lang": "Eastern Mari",
        "oscar_id": "mhr",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "mhr",
        "badwords_id": None,
    },
    {
        "lang": "Minangkabau",
        "oscar_id": "min",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "min",
        "badwords_id": None,
    },
    {
        "lang": "Macedonian",
        "oscar_id": "mk",
        "nltk_id": None,
        "kenlm_id": "mk",
        "fasttext_id": "mk",
        "badwords_id": "mk",
    },
    {
        "lang": "Malayalam",
        "oscar_id": "ml",
        "nltk_id": None,
        "kenlm_id": "ml",
        "fasttext_id": "ml",
        "badwords_id": "ml",
    },
    {
        "lang": "Mongolian",
        "oscar_id": "mn",
        "nltk_id": None,
        "kenlm_id": "mn",
        "fasttext_id": "mn",
        "badwords_id": "mn",
    },
    {
        "lang": "Western Mari",
        "oscar_id": "mrj",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "mrj",
        "badwords_id": None,
    },
    {
        "lang": "Marathi",
        "oscar_id": "mr",
        "nltk_id": None,
        "kenlm_id": "mr",
        "fasttext_id": "mr",
        "badwords_id": "mr",
    },
    {
        "lang": "Malay",
        "oscar_id": "ms",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ms",
        "badwords_id": "ms",
    },
    {
        "lang": "Maltese",
        "oscar_id": "mt",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "mt",
        "badwords_id": "mt",
    },
    {
        "lang": "Mirandese",
        "oscar_id": "mwl",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "mwl",
        "badwords_id": None,
    },
    {
        "lang": "Burmese",
        "oscar_id": "my",
        "nltk_id": None,
        "kenlm_id": "my",
        "fasttext_id": "my",
        "badwords_id": "my",
    },
    {
        "lang": "Erzya",
        "oscar_id": "myv",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "myv",
        "badwords_id": None,
    },
    {
        "lang": "Mazanderani",
        "oscar_id": "mzn",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "mzn",
        "badwords_id": None,
    },
    {
        "lang": "Nahuatl",
        "oscar_id": "nah",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "nah",
        "badwords_id": None,
    },
    {
        "lang": "Neapolitan",
        "oscar_id": "nap",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "nap",
        "badwords_id": None,
    },
    {
        "lang": "Low German",
        "oscar_id": "nds",
        "nltk_id": "german",
        "kenlm_id": None,
        "fasttext_id": "nds",
        "badwords_id": None,
    },
    {
        "lang": "Nepali",
        "oscar_id": "ne",
        "nltk_id": "nepali",
        "kenlm_id": "ne",
        "fasttext_id": "ne",
        "badwords_id": None,
    },
    {
        "lang": "Newari",
        "oscar_id": "new",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "new",
        "badwords_id": None,
    },
    {
        "lang": "Dutch",
        "oscar_id": "nl",
        "nltk_id": "dutch",
        "kenlm_id": "nl",
        "fasttext_id": "nl",
        "badwords_id": "nl",
    },
    {
        "lang": "Norwegian Nynorsk",
        "oscar_id": "nn",
        "nltk_id": "norwegian",
        "kenlm_id": None,
        "fasttext_id": "nn",
        "badwords_id": None,
    },
    {
        "lang": "Norwegian",
        "oscar_id": "no",
        "nltk_id": "norwegian",
        "kenlm_id": "no",
        "fasttext_id": "no",
        "badwords_id": None,
    },
    {
        "lang": "Occitan",
        "oscar_id": "oc",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "oc",
        "badwords_id": None,
    },
    {
        "lang": "Oriya",
        "oscar_id": "or",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "or",
        "badwords_id": None,
    },
    {
        "lang": "Ossetian",
        "oscar_id": "os",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "os",
        "badwords_id": None,
    },
    {
        "lang": "Pampanga",
        "oscar_id": "pam",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "pam",
        "badwords_id": None,
    },
    {
        "lang": "Panjabi",
        "oscar_id": "pa",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "pa",
        "badwords_id": None,
    },
    {
        "lang": "Polish",
        "oscar_id": "pl",
        "nltk_id": None,
        "kenlm_id": "pl",
        "fasttext_id": "pl",
        "badwords_id": "pl",
    },
    {
        "lang": "Piemontese",
        "oscar_id": "pms",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "pms",
        "badwords_id": None,
    },
    {
        "lang": "Western Panjabi",
        "oscar_id": "pnb",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "pnb",
        "badwords_id": None,
    },
    {
        "lang": "Pushto",
        "oscar_id": "ps",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ps",
        "badwords_id": None,
    },
    {
        "lang": "Portuguese",
        "oscar_id": "pt",
        "nltk_id": "portuguese",
        "kenlm_id": "pt",
        "fasttext_id": "pt",
        "badwords_id": "pt",
    },
    {
        "lang": "Quechua",
        "oscar_id": "qu",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "qu",
        "badwords_id": None,
    },
    {
        "lang": "Romansh",
        "oscar_id": "rm",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "rm",
        "badwords_id": None,
    },
    {
        "lang": "Romanian",
        "oscar_id": "ro",
        "nltk_id": "romanian",
        "kenlm_id": "ro",
        "fasttext_id": "ro",
        "badwords_id": "ro",
    },
    {
        "lang": "Russian",
        "oscar_id": "ru",
        "nltk_id": "russian",
        "kenlm_id": "ru",
        "fasttext_id": "ru",
        "badwords_id": "ru",
    },
    {
        "lang": "Yakut",
        "oscar_id": "sah",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "sah",
        "badwords_id": None,
    },
    {
        "lang": "Sanskrit",
        "oscar_id": "sa",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "sa",
        "badwords_id": None,
    },
    {
        "lang": "Sicilian",
        "oscar_id": "scn",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "scn",
        "badwords_id": None,
    },
    {
        "lang": "Sindhi",
        "oscar_id": "sd",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "sd",
        "badwords_id": None,
    },
    {
        "lang": "Serbo-Croatian",
        "oscar_id": "sh",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "sh",
        "badwords_id": None,
    },
    {
        "lang": "Sinhala",
        "oscar_id": "si",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "si",
        "badwords_id": None,
    },
    {
        "lang": "Slovak",
        "oscar_id": "sk",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "sk",
        "badwords_id": "sk",
    },
    {
        "lang": "Slovenian",
        "oscar_id": "sl",
        "nltk_id": "slovene",
        "kenlm_id": None,
        "fasttext_id": "sl",
        "badwords_id": "sl",
    },
    {
        "lang": "Somali",
        "oscar_id": "so",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "so",
        "badwords_id": None,
    },
    {
        "lang": "Albanian",
        "oscar_id": "sq",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "sq",
        "badwords_id": "sq",
    },
    {
        "lang": "Serbian",
        "oscar_id": "sr",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "sr",
        "badwords_id": "sr",
    },
    {
        "lang": "Sundanese",
        "oscar_id": "su",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "su",
        "badwords_id": None,
    },
    {
        "lang": "Swedish",
        "oscar_id": "sv",
        "nltk_id": "swedish",
        "kenlm_id": None,
        "fasttext_id": "sv",
        "badwords_id": "sv",
    },
    {
        "lang": "Swahili",
        "oscar_id": "sw",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "sw",
        "badwords_id": None,
    },
    {
        "lang": "Tamil",
        "oscar_id": "ta",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ta",
        "badwords_id": None,
    },
    {
        "lang": "Telugu",
        "oscar_id": "te",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "te",
        "badwords_id": "te",
    },
    {
        "lang": "Tajik",
        "oscar_id": "tg",
        "nltk_id": "tajik",
        "kenlm_id": None,
        "fasttext_id": "tg",
        "badwords_id": None,
    },
    {
        "lang": "Thai",
        "oscar_id": "th",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "th",
        "badwords_id": "th",
    },
    {
        "lang": "Turkmen",
        "oscar_id": "tk",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "tk",
        "badwords_id": None,
    },
    {
        "lang": "Tagalog",
        "oscar_id": "tl",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "tl",
        "badwords_id": None,
    },
    {
        "lang": "Turkish",
        "oscar_id": "tr",
        "nltk_id": "turkish",
        "kenlm_id": "tr",
        "fasttext_id": "tr",
        "badwords_id": "tr",
    },
    {
        "lang": "Tatar",
        "oscar_id": "tt",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "tt",
        "badwords_id": None,
    },
    {
        "lang": "Tuvinian",
        "oscar_id": "tyv",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "tyv",
        "badwords_id": None,
    },
    {
        "lang": "Uighur",
        "oscar_id": "ug",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ug",
        "badwords_id": None,
    },
    {
        "lang": "Ukrainian",
        "oscar_id": "uk",
        "nltk_id": None,
        "kenlm_id": "uk",
        "fasttext_id": "uk",
        "badwords_id": "uk",
    },
    {
        "lang": "Urdu",
        "oscar_id": "ur",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "ur",
        "badwords_id": None,
    },
    {
        "lang": "Uzbek",
        "oscar_id": "uz",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "uz",
        "badwords_id": "uz",
    },
    {
        "lang": "Venetian",
        "oscar_id": "vec",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "vec",
        "badwords_id": None,
    },
    {
        "lang": "Vietnamese",
        "oscar_id": "vi",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "vi",
        "badwords_id": "vi",
    },
    {
        "lang": "Volap\u00fck",
        "oscar_id": "vo",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "vo",
        "badwords_id": None,
    },
    {
        "lang": "Waray",
        "oscar_id": "war",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "war",
        "badwords_id": None,
    },
    {
        "lang": "Walloon",
        "oscar_id": "wa",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "wa",
        "badwords_id": None,
    },
    {
        "lang": "Wu Chinese",
        "oscar_id": "wuu",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "wuu",
        "badwords_id": None,
    },
    {
        "lang": "Kalmyk",
        "oscar_id": "xal",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "xal",
        "badwords_id": None,
    },
    {
        "lang": "Mingrelian",
        "oscar_id": "xmf",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "xmf",
        "badwords_id": None,
    },
    {
        "lang": "Yiddish",
        "oscar_id": "yi",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "yi",
        "badwords_id": None,
    },
    {
        "lang": "Yoruba",
        "oscar_id": "yo",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "yo",
        "badwords_id": None,
    },
    {
        "lang": "Yue Chinese",
        "oscar_id": "yue",
        "nltk_id": None,
        "kenlm_id": None,
        "fasttext_id": "yue",
        "badwords_id": None,
    },
    {
        "lang": "Chinese",
        "oscar_id": "zh",
        "nltk_id": None,
        "kenlm_id": "zh",
        "fasttext_id": "zh",
        "badwords_id": None,
    },
]
langs_id = pd.DataFrame(langs_id)