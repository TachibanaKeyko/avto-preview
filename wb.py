# собирает wiren-board.html: шапка и подвал берутся из intesis.html, форма из form.py
from form import form

s = open('intesis.html', encoding='utf-8').read()
head = s[:s.index('<div class="wrap crumbs">')].replace(
    '<title>Intesis — набросок редизайна</title>', '<title>Wiren Board — набросок редизайна</title>')
foot = s[s.index('<footer>'):]


def img(f):
    return 'https://cms.avtomatika.ru/uploads/' + f


body = f'''<div class="wrap crumbs"><a href="#">Главная</a> / <a href="#">Услуги</a> / Программирование Wiren Board</div>

<div class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="tag">Услуга</span>
      <h1 class="h1">Услуги программирования контроллеров Wiren Board</h1>
      <p class="lead">Предлагаем индивидуальную разработку системы автоматизации «под ключ»</p>
      <div class="btns">
        <a class="btn btn-main" href="#form">Рассчитать стоимость</a>
      </div>
    </div>
    <div class="hero-pic"><img src="img/wb.png" alt="Контроллер Wiren Board"></div>
  </div>
</div>

<div class="wrap">
  <div class="facts three">
    <div class="fact"><b>10+</b><span>Лет опыта в автоматизации</span></div>
    <div class="fact"><b>100+</b><span>Реализованных проектов</span></div>
    <div class="fact"><b>24 ч</b><span>Ответ после заявки</span></div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="sec-head">
      <div class="num">01</div>
      <div>
        <h2 class="h2">Платформа Wiren Board</h2>
        <p class="lead">Wiren Board (WB) — мощная платформа и экосистема на базе Debian Linux, которая даёт безграничную свободу для автоматизации зданий, промышленных и IoT-проектов. Её главная фишка — гибкость и открытый софт</p>
      </div>
    </div>
    <div class="ps">
      <div class="card">
        <h3 class="h3">Что нужно для работы с WB</h3>
        <p class="muted">Для прошивки адресов Modbus RTU по шине RS-485, создания веб-интерфейсов и интеграции по MQTT нужны основы системного администрирования и программирования</p>
        <div class="proto lt"><span class="chip">Modbus RTU</span><span class="chip">RS-485</span><span class="chip">MQTT</span><span class="chip">Debian Linux</span></div>
      </div>
      <div class="card dark">
        <h3 class="h3">Что делают наши инженеры</h3>
        <p>Индивидуальная разработка промышленной автоматизации под ключ: написание сложной логики, включая визуальное программирование в Node-RED, интеграция стороннего оборудования по Modbus TCP и создание кастомных графических дашбордов</p>
        <div class="proto"><span class="chip y">Node-RED</span><span class="chip y">Modbus TCP</span><span class="chip y">Дашборды</span></div>
      </div>
    </div>
  </div>
</section>

<section class="soft" id="price">
  <div class="wrap">
    <div class="sec-head">
      <div class="num">02</div>
      <div>
        <h2 class="h2">Стоимость услуг</h2>
        <p class="lead">Цена на программирование напрямую зависит от выбранного формата работы и масштаба объекта</p>
      </div>
    </div>
    <div class="tiers">
      <div class="tier"><div class="pic"><img src="img/lid1.png" alt=""></div><div class="body"><h3 class="h3">Базовая конфигурация</h3><span class="price">15 000 – 35 000 ₽</span><p>Первичная настройка контроллера: регистрация модулей через встроенный веб-интерфейс Wiren Board, тестирование обмена данными по Modbus и простое включение и выключение света без многошаговых сцен</p></div></div>
      <div class="tier"><div class="pic"><img src="img/lid2.png" alt=""></div><div class="body"><h3 class="h3">Проект среднего уровня</h3><span class="price">40 000 – 90 000 ₽</span><p>Управляющая логика для вентиляции, отопления и освещения: контроль температуры и влажности, диммирование светодиодных лент. Наглядные экраны управления во встроенном веб-интерфейсе контроллера для ежедневной работы</p></div></div>
      <div class="tier"><div class="pic"><img src="img/lid3.png" alt=""></div><div class="body"><h3 class="h3">Полная автоматизация</h3><span class="price">от 100 000 – 250 000 ₽</span><p>Продвинутые скрипты автоматизации, сопряжение контроллера с внешними экосистемами и сервисами, защищённый удалённый доступ через VPN. При необходимости подключаются сетевые серверы и счётчики, данные обрабатываются в реальном времени</p></div></div>
    </div>
  </div>
</section>

{form("Заказать расчёт стоимости программирования", "Закажите быстрый расчёт стоимости без обязательств. Если требуется индивидуальная разработка под ключ, оставьте заявку — специалисты свяжутся с вами в течение 24 часов", "Ваш комментарий")}

<section class="soft">
  <div class="wrap">
    <div class="sec-head">
      <div class="num">03</div>
      <div><h2 class="h2">Этапы работы: от ТЗ до сдачи объекта</h2></div>
    </div>
    <div class="steps">
      <div class="step"><div class="n">1</div><h3 class="h3">Сбор исходных данных и аудит</h3><p>Обследование объекта, определение параметров и алгоритмов управления в местах установки оборудования. Фиксация требований заказчика</p></div>
      <div class="step"><div class="n">2</div><h3 class="h3">ТЗ и расчёт сметы</h3><p>Формирование требований, подбор товаров из каталога магазина для комплектации объекта. Договор и аванс за оборудование</p></div>
      <div class="step"><div class="n">3</div><h3 class="h3">Документация и код</h3><p>Схемы подключений, чертежи щита и алгоритмы работы; при необходимости расчёт длины кабеля и количества материалов</p></div>
      <div class="step"><div class="n">4</div><h3 class="h3">Конфигурация и программирование</h3><p>Прошивка адресов Modbus, настройка каналов ввода и вывода, проверка каждого входа и выхода, настройка правил и загрузка системы в контроллер</p></div>
      <div class="step"><div class="n">5</div><h3 class="h3">Пусконаладочные работы</h3><p>Тестирование сценариев на объекте, обучение персонала и подготовка к эксплуатации. Акт выполненных работ и финальный расчёт</p></div>
      <div class="step"><div class="n">6</div><h3 class="h3">Мониторинг и поддержка</h3><p>Инструменты доступа и техническая поддержка системы. Консультации пользователей, обновление ПО контроллеров по запросу</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <div class="num">04</div>
      <div><h2 class="h2">Частые вопросы</h2></div>
    </div>
    <div class="faq">
      <details open><summary>Предоставляете ли вы исходный код и права на логику после оплаты?</summary><div class="ans">Да. Главная фишка Wiren Board — открытость и отсутствие вендор-лока. Вы полностью владеете системой, исходными кодами и настройками</div></details>
      <details><summary>Что произойдёт при отказе контроллера — система встанет?</summary><div class="ans">Архитектура Wiren Board предусматривает отказоустойчивость. Многие модули расширения хранят конфигурацию в энергонезависимой памяти и продолжают работать автономно при потере связи с контроллером, а на модулях реле есть физические кнопки для ручного управления. Надёжность также обеспечивается корректной настройкой питания и защитой линий</div></details>
      <details><summary>Какие протоколы и устройства поддерживает Wiren Board?</summary><div class="ans">Modbus RTU и TCP, RS-485, 1-wire, MQTT и другие интерфейсы. Можно добавить счётчики, датчики и другие устройства, если они соответствуют требованиям проекта</div></details>
      <details><summary>Можно ли добавить каналы ввода и вывода?</summary><div class="ans">Да. Можно добавить аналоговый вход и увеличить количество выходов с помощью карт расширения и дополнительных модулей</div></details>
      <details><summary>Можно ли использовать готовые программы и написать дополнительные функции?</summary><div class="ans">Да. Можно использовать готовые программы и библиотеки, а также написать дополнительные функции и сценарии под задачи объекта</div></details>
      <details><summary>Как интегрировать Wiren Board с мобильными приложениями?</summary><div class="ans">Для этого настраивается публикация данных в MQTT-брокеры и интеграция с Home Assistant</div></details>
    </div>
  </div>
</section>

'''
open('wiren-board.html', 'w', encoding='utf-8').write(head + body + foot)
