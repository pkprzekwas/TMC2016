# Projekt TMC 2016

### Instrukcja uruchomienia.

Zależności wstępne:
* [Anaconda (Python 3.6)](https://www.continuum.io/downloads)

Zalecany system: 
* Ubuntu 16.04

Uruchomienie:
1. Stworzenie wirtualnego środowiska: 
    * `conda create --name <nazwa_środowiska>` 
    * `Proceed ([y]/n)? <yes>`
2. Uruchomienie środowiska:
    * `source activate <nazwa_środowiska>`
3. Instalacja potrzebnych zależności:
    * `pip install -r req.txt`
4. Uruchomienie Jupyter notebooka:
    * `./start_notebook.sh`
5. Stworzenie katalogu `out`:
    * `mkdir out`
6. Rozpakowanie paczki z plikami csv do katalogu `out`:
    * `unzip data.zip -d ./out`
7. Gdy Jupiter uruchomi się w przeglądarce należy odpalić plik `TMC_project_results.ipynb`.
8. Pozostałe instrukcje znajdują się w notebooku.

Note: Powyższe czynności powinny zostać wykonane w głównym katalogu projektu.

