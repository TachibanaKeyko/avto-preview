# общий блок заявки: заголовок и подводка свои у каждой страницы, остальное как на сайте
def form(title, lead, ph):
    return f'''<div class="cta" id="form">
  <div class="wrap cta-grid">
    <div class="cta-form">
      <div class="cta-head"><span class="cta-ava" aria-hidden="true"></span><h2 class="h2">{title}</h2></div>
      <p class="lead">{lead}</p>
      <form onsubmit="return false">
        <input name="name" placeholder="Ваше имя">
        <div class="row"><input name="phone" type="tel" placeholder="Телефон"><input name="email" type="email" placeholder="Эл. почта"></div>
        <textarea name="comment" maxlength="500" placeholder="{ph}"></textarea>
        <label class="attach"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5l-8.6 8.6a5.5 5.5 0 01-7.8-7.8l8.6-8.6a3.7 3.7 0 015.2 5.2l-8.6 8.6a1.8 1.8 0 01-2.6-2.6l7.9-7.9"/></svg>Прикрепить ТЗ / Схему (PDF, DOC, Excel)<input type="file" accept=".pdf,.doc,.docx,.xls,.xlsx" hidden></label>
        <label class="consent"><input type="checkbox" name="agree"><span>Нажимая на кнопку, вы даете согласие на обработку персональных данных и соглашаетесь с политикой конфиденциальности</span></label>
        <button class="btn btn-main" type="submit">Отправить инженеру</button>
        <p class="note">Ваша заявка поступит напрямую в инженерный отдел, минуя колл-центр</p>
      </form>
    </div>
    <div class="eng"><img src="https://avtomatika.ru/engineer.png" alt="Инженер"></div>
  </div>
</div>
<div class="perks">
  <div class="wrap">
    <div class="perk">Ответ по существу в течение 24 часов</div>
    <div class="perk">Закрепление ведущего инженера за вашим проектом</div>
    <div class="perk">Прямая линия с инженерным отделом, минуя колл-центр</div>
    <div class="perk">Сопровождение объекта от разработки ТЗ до пусконаладки</div>
  </div>
</div>'''
