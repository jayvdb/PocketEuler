import codecs

from collections import OrderedDict

from bs4 import BeautifulSoup

import sarge


def load_raw():
    f = codecs.open('README.md', 'r', 'utf8')
    return f


def extract_equations(raw):
    soup = BeautifulSoup(raw, 'lxml')
    equation_tags = soup.find_all('img', class_="equation")
    equations = list(
        (item['src'], item['data-expr'])
        for item in equation_tags
    )

    if len(dict(equations)) != len(equation_tags):
        # A filename was repeated
        filenames = set(item[0] for item in equations)
        for filename in filenames:
            equation = None
            for item in equations:
                if item[0] == filename:
                    if equation:
                        assert equation == item[1], "filename reused with different equation"
                    else:
                        equation = item[1]

    return OrderedDict(equations)


def create_svg(filename, maths):
    sarge.run("mimetex '{0}' -o -e '{1}'".format(maths, filename))


def main():
    f = load_raw()
    equations = extract_equations(f)
    for filename, maths in equations.items():
        create_svg(filename, maths)
        print('created {0}'.format(filename))


if __name__ == '__main__':
    main()
