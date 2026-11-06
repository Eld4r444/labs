# Лабораторная работа №1. Все команды по порядку (Git Bash / PowerShell).
# Задание 1
mkdir git_lab
cd git_lab
git init -b main
git status
# Задание 2
echo "Первая версия файла" > notes.txt
git status
git add notes.txt
git status
git commit -m "Добавлен файл notes.txt"
git log
git log --oneline
# Задание 3
echo "Цель: изучить основы Git" >> notes.txt
echo "Рабочий каталог, индекс и коммит" >> notes.txt
git status
git diff
git add notes.txt
git diff --staged
git commit -m "Добавлены цель и основные понятия"
# Задание 4
echo "git add добавляет изменения в индекс" >> notes.txt
git commit -am "Добавлено описание git add"
echo "git commit сохраняет изменения в истории" >> notes.txt
git commit -am "Добавлено описание git commit"
echo "git log показывает историю коммитов" >> notes.txt
git commit -am "Добавлено описание git log"
git log --oneline
# Задание 5
git switch -c experiment
echo "Эксперимент в отдельной ветке" > experiment.txt
git add experiment.txt
git commit -m "Добавлен файл experiment.txt"
git log --oneline
git switch main
ls
# Задание 6
git merge experiment
ls
git log --oneline --graph
# Задание 7
echo "Временная строка" >> notes.txt
git diff
git restore notes.txt
git status
# Задание 8
echo "Изменение для индекса" >> notes.txt
git add notes.txt
git status
git restore --staged notes.txt
git status
git restore notes.txt
# Задание 9
echo "Экспериментальная строка" >> notes.txt
git commit -am "Экспериментальное изменение"
git log --oneline
git revert --no-edit HEAD
git log --oneline
# Задание 10
git switch -c todo-list
echo "1. Повторить команды Git" > todo.txt
git add todo.txt
git commit -m "Добавлен список дел"
echo "2. Ответить на контрольные вопросы" >> todo.txt
git commit -am "Добавлен второй пункт в список дел"
git diff HEAD~1 HEAD
git switch main
git merge todo-list
git log --oneline --graph --all
