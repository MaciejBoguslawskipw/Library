import re
import logging

class TextAnalyzer:
    def __init__(self, text, log_filename='log.txt'):
        self.text = text
        self.log_filename = log_filename
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Ustawia logger do zapisywania wyników w pliku logów."""
        logger = logging.getLogger('TextAnalysisLogger')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(self.log_filename)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def word_count(self):
        """Zlicza liczbę słów w tekście."""
        words = re.findall(r'\b\w+\b', self.text)
        return len(words)

    def unique_words(self):
        """Zwraca listę unikalnych słów w tekście."""
        words = re.findall(r'\b\w+\b', self.text)
        return list(set(words))

    def log_results(self):
        """Loguje wyniki analizy do pliku."""
        try:
            total_words = self.word_count()
            self.logger.info(f"Liczba słów: {total_words}")

            unique_words_list = self.unique_words()
            self.logger.info(f"Unikalne słowa: {', '.join(unique_words_list)}")
        except Exception as e:
            self.logger.error(f"Błąd analizy tekstu: {e}")

    def __str__(self):
        """Zwraca wyniki analizy w formie tekstowej."""
        total_words = self.word_count()
        unique_words_list = self.unique_words()
        return (f"Liczba słów: {total_words}\n"
                f"Unikalne słowa: {', '.join(unique_words_list)}")

def main():
    # Wczytanie tekstu
    text = input("Wprowadź tekst do analizy: ")

    # Tworzenie obiektu analizy
    analyzer = TextAnalyzer(text)

    # Logowanie wyników do pliku
    analyzer.log_results()

    # Wyświetlanie wyników na ekranie
    print(analyzer)

if __name__ == "__main__":
    main()
