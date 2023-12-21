import re


class Analyze:
    def __init__(self, Path):
        self.Path = Path
        self.data = None
        self.read_file()

    def read_file(self):
        try:
            with open(self.Path, 'r', encoding='utf-8') as file:
                self.data = file.readlines()
        except FileNotFoundError:
            print("Файл не найден.")
        except Exception as e:
            print(e)

    def search_text(self, pattern):
        if self.data is None:
            print("Error")
            return []

        matches = []
        for line_number, line in enumerate(self.data, start=1):
            found = re.findall(pattern, line)
            if found:
                matches.append({
                    'line_number': line_number,
                    'matches': found
                })

        return matches

file_analyzer = Analyze("")
file_analyzer.read_file()

if file_analyzer.data is not None:
    Search = r'\b\w+ing\b'
    Result = file_analyzer.search_text(Search)

    print(f"Результаты поиска '{Search}':")
    for found in Result:
        print(f"В строке {found['line_number']}: {found['matches']}")
