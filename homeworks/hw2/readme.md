# Домашнее задание 2. OWASP Juice Shop.
В рамках данного домашнего задания вам необходимо выполнить несколько заданий в рамках тренажера по веб-уязвимостям [OWASP Juice Shop](https://github.com/juice-shop/juice-shop).

**Цель**: Выполнить минимум 3 задания (уязвимости) в [Juice Shop](https://github.com/juice-shop/juice-shop).

**Шкала оценивания:**
- 3 любых уязвимости — 50 баллов
- 4 любых уязвимости — 75 баллов
- 5 и более уязвимостей — 100 баллов

Шаблон отчета для заполнения представлен по [ссылке](https://docs.google.com/document/d/1QUaD_fyfFBDOnHOzVislsspFrE9BTxUnLaXwaPTz4qo/edit?usp=sharing).

[Ссылка для сдачи](https://forms.gle/MZcYqrcmSPs4Feps8)

## Рекомендации
1. Устанавливаем [Kali Linux](https://www.kali.org/) на виртуальную машину.

   [Инструкция для MacOS на ARM](https://www.youtube.com/watch?v=9zdjQ9w_v_4). Еще можно использовать VMWare Fusion, хорошо работает.

   [В остальных случаях рекомендуется ставить на Virtual Box](https://www.youtube.com/watch?v=sAMnXte56yY)

2. _(опционально, можно воспользоваться для работы с запросами, но в автоматическом режиме не так интересно сканить будет)_ Устанавливаем OWASP ZAP через командную строку Kali
   ```
   sudo apt install zaproxy
   ```
3. Ставим Docker на Kali
   ```
   sudo apt update
   sudo apt install -y docker.io
   ```
4. Разворачиваем Juice Shop
   ```
   sudo docker pull bkimminich/juice-shop
   sudo docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
   ```
5. На `localhost:3000` можем открыть Juice Shop
6. Рекомендую сначала залогиниться, найти панель с заданиями (Score Board), просто ссылку надо угадать или по js коду сайта поискать прямо в браузере, это считается за отдельный челлендж, за него дается поинт
7. Выбираем любые задания на странице, их делаем
