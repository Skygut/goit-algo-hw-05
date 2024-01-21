from timeit import timeit
from kmp_search import kmp_search
from boyer_moore_search import boyer_moore_search
from rabin_karp_search import rabin_karp_search


def main():
    with open("./article_1.txt", "r") as fh:
        article_1 = "".join(fh.readlines())
        existent_pattern = "порівнюється із середнім"
        non_existent_pattern = "юєсятьпорівн ім ізсередн"

        kmp_search_article_1_existent = timeit(
            lambda: kmp_search(article_1, existent_pattern), number=10
        )
        boyer_moore_search_article_1_existent = timeit(
            lambda: boyer_moore_search(article_1, existent_pattern), number=10
        )
        rabin_karp_search_article_1_existent = timeit(
            lambda: rabin_karp_search(article_1, existent_pattern), number=10
        )

        kmp_search_article_1_non_existent = timeit(
            lambda: kmp_search(article_1, non_existent_pattern), number=10
        )
        boyer_moore_search_article_1_non_existent = timeit(
            lambda: boyer_moore_search(article_1, non_existent_pattern), number=10
        )
        rabin_karp_search_article_1_non_existent = timeit(
            lambda: rabin_karp_search(article_1, non_existent_pattern), number=10
        )

    with open("./article_2.txt", "r") as fh:
        article_2 = "".join(fh.readlines())
        existent_pattern = "традиційних представленнях структур"
        non_existent_pattern = "традпредставлкту реннях сиційнихтру"

        kmp_search_article_2_existent = timeit(
            lambda: kmp_search(article_2, existent_pattern), number=10
        )
        boyer_moore_search_article_2_existent = timeit(
            lambda: boyer_moore_search(article_2, existent_pattern),
            number=10,
        )
        rabin_karp_search_article_2_existent = timeit(
            lambda: rabin_karp_search(article_2, existent_pattern), number=10
        )

        kmp_search_article_2_non_existent = timeit(
            lambda: kmp_search(article_2, non_existent_pattern), number=10
        )
        boyer_moore_search_article_2_non_existent = timeit(
            lambda: boyer_moore_search(article_2, non_existent_pattern), number=10
        )
        rabin_karp_search_article_2_non_existent = timeit(
            lambda: rabin_karp_search(article_2, non_existent_pattern), number=10
        )

    print(f"{'Article 1': ^60}")
    print(
        f"{'| Algorithm': <20} | {'Time(Existent)': <20} | {'Time(Non existent)': <20}"
    )
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")
    print(
        f"{'| Kmp search': <20} | {kmp_search_article_1_existent: <20.5f} | {kmp_search_article_1_non_existent: <20.5f}"
    )
    print(
        f"{'| Boyer moore search': <20} | {boyer_moore_search_article_1_existent: <20.5f} | {boyer_moore_search_article_1_non_existent: <20.5f}"
    )
    print(
        f"{'| Rabin karp search': <20} | {rabin_karp_search_article_1_existent: <20.5f} | {rabin_karp_search_article_1_non_existent: <20.5f}"
    )
    print("")
    print(f"{'Article 2': ^60}")
    print(
        f"{'| Algorithm': <20} | {'Time(Existent)': <20} | {'Time(Non existent)': <20}"
    )
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")
    print(
        f"{'| Kmp search': <20} | {kmp_search_article_2_existent: <20.5f} | {kmp_search_article_2_non_existent: <20.5f}"
    )
    print(
        f"{'| Boyer moore search': <20} | {boyer_moore_search_article_2_existent: <20.5f} | {boyer_moore_search_article_2_non_existent: <20.5f}"
    )
    print(
        f"{'| Rabin karp search': <20} | {rabin_karp_search_article_2_existent: <20.5f} | {rabin_karp_search_article_2_non_existent: <20.5f}"
    )


if __name__ == "__main__":
    main()
