from random import randint


def D6():
    return randint(1, 6)


def D66():
    return str(D6()) + str(D6())


class NameGenerator:
    data = {
        "ork": {
            "en": {
                "11": {"front_bit": "Urzog", "uvver_bit": "Drakka"},
                "12": {"front_bit": "Snikrat", "uvver_bit": "Grug"},
                "13": {"front_bit": "Krogskull", "uvver_bit": "Gitstompa"},
                "14": {"front_bit": "Gorgrok", "uvver_bit": "Skullcrusha"},
                "15": {"front_bit": "", "uvver_bit": ""},
                "16": {"front_bit": "", "uvver_bit": ""},
                "21": {"front_bit": "", "uvver_bit": ""},
                "22": {"front_bit": "", "uvver_bit": ""},
                "23": {"front_bit": "", "uvver_bit": ""},
                "24": {"front_bit": "", "uvver_bit": ""},
                "25": {"front_bit": "", "uvver_bit": ""},
                "26": {"front_bit": "", "uvver_bit": ""},
                "31": {"front_bit": "", "uvver_bit": ""},
                "32": {"front_bit": "", "uvver_bit": ""},
                "33": {"front_bit": "", "uvver_bit": ""},
                "34": {"front_bit": "", "uvver_bit": ""},
                "35": {"front_bit": "", "uvver_bit": ""},
                "36": {"front_bit": "", "uvver_bit": ""},
                "41": {"front_bit": "", "uvver_bit": ""},
                "42": {"front_bit": "", "uvver_bit": ""},
                "43": {"front_bit": "", "uvver_bit": ""},
                "44": {"front_bit": "", "uvver_bit": ""},
                "45": {"front_bit": "", "uvver_bit": ""},
                "46": {"front_bit": "", "uvver_bit": ""},
                "51": {"front_bit": "", "uvver_bit": ""},
                "52": {"front_bit": "", "uvver_bit": ""},
                "53": {"front_bit": "", "uvver_bit": ""},
                "54": {"front_bit": "", "uvver_bit": ""},
                "55": {"front_bit": "", "uvver_bit": ""},
                "56": {"front_bit": "", "uvver_bit": ""},
                "61": {"front_bit": "", "uvver_bit": ""},
                "62": {"front_bit": "", "uvver_bit": ""},
                "63": {"front_bit": "", "uvver_bit": ""},
                "64": {"front_bit": "", "uvver_bit": ""},
                "65": {"front_bit": "", "uvver_bit": ""},
                "66": {"front_bit": "", "uvver_bit": ""},
            },
            "fr": {
                "11": {"front_bit": "", "uvver_bit": ""},
                "12": {"front_bit": "", "uvver_bit": ""},
                "13": {"front_bit": "", "uvver_bit": ""},
                "14": {"front_bit": "", "uvver_bit": ""},
                "15": {"front_bit": "", "uvver_bit": ""},
                "16": {"front_bit": "", "uvver_bit": ""},
                "21": {"front_bit": "", "uvver_bit": ""},
                "22": {"front_bit": "", "uvver_bit": ""},
                "23": {"front_bit": "", "uvver_bit": ""},
                "24": {"front_bit": "", "uvver_bit": ""},
                "25": {"front_bit": "", "uvver_bit": ""},
                "26": {"front_bit": "", "uvver_bit": ""},
                "31": {"front_bit": "", "uvver_bit": ""},
                "32": {"front_bit": "", "uvver_bit": ""},
                "33": {"front_bit": "", "uvver_bit": ""},
                "34": {"front_bit": "", "uvver_bit": ""},
                "35": {"front_bit": "", "uvver_bit": ""},
                "36": {"front_bit": "", "uvver_bit": ""},
                "41": {"front_bit": "", "uvver_bit": ""},
                "42": {"front_bit": "", "uvver_bit": ""},
                "43": {"front_bit": "", "uvver_bit": ""},
                "44": {"front_bit": "", "uvver_bit": ""},
                "45": {"front_bit": "", "uvver_bit": ""},
                "46": {"front_bit": "", "uvver_bit": ""},
                "51": {"front_bit": "", "uvver_bit": ""},
                "52": {"front_bit": "", "uvver_bit": ""},
                "53": {"front_bit": "", "uvver_bit": ""},
                "54": {"front_bit": "", "uvver_bit": ""},
                "55": {"front_bit": "", "uvver_bit": ""},
                "56": {"front_bit": "", "uvver_bit": ""},
                "61": {"front_bit": "", "uvver_bit": ""},
                "62": {"front_bit": "", "uvver_bit": ""},
                "63": {"front_bit": "", "uvver_bit": ""},
                "64": {"front_bit": "", "uvver_bit": ""},
                "65": {"front_bit": "", "uvver_bit": ""},
                "66": {"front_bit": "", "uvver_bit": ""},
            }
        }
    }
