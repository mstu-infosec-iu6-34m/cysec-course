# Домашнее задание 1. Поиск уязвимости.
В данном домашнем задании вам предстоит просканировать при помощи [OWASP ZAP](https://www.zaproxy.org/) просканировать мини-сайт, найти в нем уязвимость, придумать к ней исправление и "зарепортить".
Шаблон отчета для заполнения представлен по [ссылке](https://docs.google.com/document/d/1oeEQ9tgPgiTpxwa8yUeGoSRXMkMTDoklGTJ-HpysbbM/edit?usp=sharing).

**Оценка (суммарно 100 баллов)**:
- 50 баллов - выполнено сканирование, предоставлен отчет со скринами (запущенное веб-приложение, работа с OWASP ZAP)
- 25 баллов - уязвимость найдена и предоставлен эксплойт, демонстрация
- 25 баллов - предоставлено исправление уязвимости в коде веб-приложения

**Определение номера варианта (у меня пока нет списка группы, поэтому так):** 

`Номер варианта = (ДР % 4) + 1`
  где ДР - ваш день рождения (номер в месяце)

[Ссылка для сдачи](https://forms.gle/RWNzV8aCkeRDUR8b7)

## Инструкция по выполнению ДЗ
1. Устанавливаем [Kali Linux](https://www.kali.org/) на виртуальную машину.

   [Инструкция для MacOS на ARM](https://www.youtube.com/watch?v=9zdjQ9w_v_4)

   [В остальных случаях рекомендуется ставить на Virtual Box](https://www.youtube.com/watch?v=sAMnXte56yY)

2. Устанавливаем OWASP ZAP через командную строку Kali
   ```
   sudo apt install zaproxy
   ```
3. Открываем командную строку на Kali и чекаутим себе репозиторий с домашкой
   ```
   git clone <URL репозитория>
   ```
4. По инструкции в папке со своим вариантом (variant<номер варианта>) запускаем свой сайт, проверяем в браузере, что он запустился
5. Запускаем ZAP
6. Выполняем Active Scan для развернутого на localhost сайта, дожидаемся завершения
7. Открываем вкладку Alerts, делаем скриншот окна ZAP, вставляем в отчет
8. Читаем описания найденных уязвимостей с красными флажками
9. Перезапускаем сервер веб-сайта, чтобы его вернуть к исходному состоянию
10. Вручную через браузер пытаемся провернуть ту же самую уязвимость с красным флажком
11. Смотрим в код сайта, придумываем исправление (подсказка: экранирование входных данных), проверяем
12. Заполняем всё в отчет
