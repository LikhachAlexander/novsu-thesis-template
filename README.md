# LaTeX Шаблон дипломной работы НовГУ

Этот репозиторий содержит LaTeX-шаблон для написания дипломных работ. Шаблон предназначен для студентов, которые хотят оформить свои работы в соответствии с требованиями учебного заведения.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Структура проекта](#структура-проекта)
- [Контрибьюции](#контрибьюции)

## Установка

Для работы с этим шаблоном необходимо установить LaTeX. Автор использует [TeX Live](https://www.tug.org/texlive/).

А также расширение для LaTeX Workshop для VS code (https://github.com/James-Yu/LaTeX-Workshop).


## Использование

1. Склонируйте репозиторий на ваш компьютер:

   `git clone https://github.com/LikhachAlexander/novsu-thesis-template.git`

2. Перейдите в папку с проектом:

   `cd novsu-thesis-template`

3. Отредактируйте файл main.tex в соответствии с вашей работой.

4. Скомпилируйте LaTeX-файл с помощью следующей команды:

   `pdflatex main.tex`

5. Повторите команду компиляции, чтобы обновить ссылки и содержание.

Примечание: при большом документе с большим количеством изображений компиляций занимает достаточно большое количество времени. Для ускорения работы в файле `diplom_style.sty` можно заменить строчку 

```
90        % draft - пустая картинка. Ускоряет время компиляции
91        % \includegraphics[draft]{#1}
92        \includegraphics{#1}
```

на

```
90        % draft - пустая картинка. Ускоряет время компиляции
91        \includegraphics[draft]{#1}
92        % \includegraphics{#1}
```
это значительно ускорит время сборки документа.

## Структура проекта

Структура проекта выглядит следующим образом:

```
/novsu-thesis-template
 ├── content/
 │   ├── images/             % Папка для изображений
 │   │   └── doggy.jpg       % Пример изображения
 │   ├── source/             % Папка для исходного кода
 │   │   ├── ex1.ino         % Пример программы на Arduino
 │   │   ├── ex2.py          % Пример на Python
 │   │   └── fib.py          % Фибоначчи
 │   ├── annotation.tex      % Аннотация дипломной работы
 │   ├── appendix.tex        % Приложение
 │   ├── bibliography.tex    % Список литературы
 │   ├── conclusion.tex      % Заключение
 │   ├── example.tex         % Пример текста документа
 │   ├── introduction.tex    % Введение
 │   └── titlepage.tex       % Титульный лист
 ├── diplom_style.sty         % Описание стилей
 ├── main.tex                 % Главный файл
 ├── main.pdf                 % Выходной файл
 ├── .vscode/                 % Настройки проекта VS Code
 └── README.md                % Этот файл
```

## Контрибьюции

Если у вас есть предложения или исправления для улучшения шаблона, не стесняйтесь открывать pull request или создавать issues.

