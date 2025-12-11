import discord
from discord.ext import commands
import asyncio
import random
from asyncio import sleep 


intent = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents = intent)
token = ('MTM3NTQ5MDQxODAzMjI1MDk1MA.Gk6k_g.0XuMsKvDYPbmgFFQ-3QoQyQ7ZTnVMs8HfyUagQ')

role_id=854005819610759199

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('Секретутка'))

@bot.command()
async def ball(ctx, *, vopro):
	otvet1 = discord.Embed(title='', description='Да', color=discord.Color.blue())
	otvet2 = discord.Embed(title='', description='Нет', color=discord.Color.blue())
	otvet3 = discord.Embed(title='', description='Возможно', color=discord.Color.blue())
	otvet4 = discord.Embed(title='', description='Перспективы не очень хорошие', color=discord.Color.blue())
	otvet5 = discord.Embed(title='', description='Даже не думай об этом', color=discord.Color.blue())
	otvet6 = discord.Embed(title='', description='Спроси ещё раз', color=discord.Color.blue())
	otvet7 = discord.Embed(title='', description='Я не могу ответить на ваш вопрос', color=discord.Color.blue())
	otvet8 = discord.Embed(title='', description='Не рассчитывай на это', color=discord.Color.blue())
	otvet9 = discord.Embed(title='', description='Очень сомнительно', color=discord.Color.blue())
	otvet10 = discord.Embed(title='', description='Перспективы очень хорошие', color=discord.Color.blue())
	otvet11 = discord.Embed(title='', description='Вероятно', color=discord.Color.blue())
	otvet12 = discord.Embed(title='', description='Вы можете рассчитывать на это', color=discord.Color.blue())
	otvet13 = discord.Embed(title='', description='мой ответ - нет', color=discord.Color.blue())
	otvet14 = discord.Embed(title='', description='Сконцентрируйся и спроси ещё раз', color=discord.Color.blue())
	otvet15 = discord.Embed(title='', description='Твоя мама тебе запрещает таким заниматься', color=discord.Color.blue())
	otvet16 = discord.Embed(title='', description='Сегодня не твой день', color=discord.Color.blue())
	otvet17 = discord.Embed(title='', description='тебе нужно более делекатнее спрашивать такое у девушки', color=discord.Color.blue())
	embed=random.choice([otvet1, otvet2, otvet3, otvet4, otvet15, otvet6, otvet7, otvet8, otvet9, otvet10, otvet11, otvet12, otvet13, otvet14, otvet15, otvet16, otvet17])
	await ctx.reply(embed=embed)

class MyView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Озвучка', style=discord.ButtonStyle.primary, custom_id="persistent:button_callback")
	async def button_callback(self, interaction, button):
		await interaction.response.send_message("Имя/творческий псевдоним: \n\n Возраст: \n\n Опыт в озвучке: \n\n Немного о себе: \n\n Модель микрофона: \n\n Пробник: (аудио- видео- файл или ссылка на вашу озвучку продолжительностью не менее 1 минуты и не более 5 минут раскрывающий ваши возможности) \n\n\n Как записать пробник? \n  - Выбираете, что хотите озвучить. Либо самостоятельно, либо используйте заранее заготовленные нами тексты*. \n - Открываете любое приложение для записи голоса (Reaper, Audacity и т.д.). \n - Записываетесь. \n\n Заполненную форму отправлять @Morack или #пробники \n Ожидайте обратной связи. Вам обязательно напишут. \n\n\n Тексты для парней: \n 1) Монолог. Судо Кен https://docs.google.com/document/d/1nJNI7KgsjaAUUg3PaMmNr6RDB6yNipn3WwDbKCYXNhU/edit?usp=drivesdk \n 2) Монолог. Хирата Йосуке https://docs.google.com/document/d/1pqZm0Us3k_fTzzqbEiUiq68nkqR8CWaFo2q0G74byqw/edit?usp=drivesdk \n\n Тексты для девушек: \n\n 1) Монолог. Каруизава Кей https://docs.google.com/document/d/17T7R4S1IjFoXAU3291Ph-pOqlr-OFx1CB8lPyXr_sK4/edit?usp=drivesdk \n 2) Монолог. Кушида Кикё https://docs.google.com/document/d/1VuP4TNVJlT66M5Ff3MvhJcC6dWZy-Go32gH2vtAZRR0/edit?usp=drivesdk", ephemeral=True)
		
	@discord.ui.button(label='Технарь', style=discord.ButtonStyle.primary, custom_id="persistent:button_dont_call")
	async def button_dont_call(self, interaction, button):
		await interaction.response.send_message("Имя/творческий псевдоним: \n\n Возраст: \n\n Опыт: \n\n Немного о себе: \n\n Программа для работы: \n\n Устройство (характеристики): \n\n Пробник: (аудио- видео- файл или ссылка на файл с демонстрацией ваших способностей монтажа или работы со звуком) \n\n Заполненную форму отправлять @Morack \n Ожидайте обратной связи. Вам обязательно напишут.", ephemeral=True)
		

	@discord.ui.button(label='Основные роли', style=discord.ButtonStyle.gray, custom_id="persistent:button_relax_callGay")
	async def button_relax_callGay(self, interaction, button):
		await interaction.response.send_message("Класс А - администраторы, руководители проекта. \n\n Класс В - состав команды по озвучке. Участвуют в озвучке большинства произведений и владеют достаточным уровнем навыком, чтобы числится в основном составе RMTeam. \n\n Технарь - состав команды по технической части (монтаж и работа со звуком). Имеют достаточно опыта и владеют навыками для самостоятельного выполнения своих задач. \n\n Академия - состав команды по озвучке. Получают соответствующие знания и опыт в озвучке от руководителей, старших товарищей или от участвуя в некоторых проектах команды. \n\n Стажер - состав команды по технической части (монтаж и работа со звуком). Обучаются некоторым азам монтажа и работы со звуком под руководством своих старших товарищей. \n\n Класс С - люди поддерживающие наш проект. Получают доступ к каналу с нашими неудачными и смешными дублями и моментами при озвучке. \n\n Класс D - люди следящие за нашим творчеством и проектом в целом.", ephemeral=True)
		

	@discord.ui.button(label='Правила', style=discord.ButtonStyle.danger, custom_id="persistent:button_Lax_callRed")
	async def button_Lax_callRed(self, interaction, button):
		await interaction.response.send_message("1. Общие положения:```\n**1.1.** Участники сервера Дискорд равны перед правилами вне зависимости от опыта и роли; \n**1.2.** Мат разрешается, но без злоупотребления; \n**1.3.** Запрещено оскорбление других пользователей. \nИсключение - если оба готовы сказать, что оскорбление было шуткой и никто не в обиде; \n**1.4.** Нельзя использовать NSFW: шок-контент, порнографию в обычных каналах. Для этого есть #балдежная \n**1.5.** Запрещено злоупотребление Caps Lock;\n**1.6.** Запрещается жестки троллинг. \n Исключение - это никого не задело взаправду. \n\n 2. Размещение ссылок:```\n**2.1.** До согласования с администрацией запрещена любая в её проявлении реклама;\n**2.2.** Не допускается спам-рассылка в личных СМС с другими пользователями;\n**2.3.** Нельзя кидать ссылки с доменами на Ютуб, ВК, Роблокс и Вики. Размещение ссылки по согласованию с администратором. \n\n 3. Ники и аватарки:```\n**3.1.** Администратор вправе требовать изменение ника и картинки, если считает, что они оскорбляют кого-либо или являются распространением NSFW-контента;\n**3.2.** Запрещены ники наподобие User, Discord User, NickName и прочие, в том числе Admin, Moderator и т.д.;\n**3.3.** Запрещено использование имен с матом, оскорблением, религиозными названиями, рекламой, пропагандой алкоголя / наркотиков;\n**3.4.** Не допускается применение символики террористов и запрещенных организации, (кроме Инстаграмма), призыв к насилию и экстремизму;\n**3.5.** Нельзя использовать бессмысленный набор символов с многократным повторением одной или нескольких букв;\n**3.6.** Не допускаются картинки с ненормативной лексикой, оскорблением и прочими запрещенными вещами, о которых упоминалось выше.", ephemeral=True)
		

@bot.event
async def on_ready():
	bot.add_view(MyView())












@bot.command()
async def button(ctx):
	view = MyView()
	await ctx.send('Добро пожаловать на Discord сервер RMTeam. \n\n Мы являемся русскоязычным объединением по озвучке аниме, манги, ранобэ и др. \n\n В каждую нашу работу мы вкладываем душу, много сил и опыта. Поэтому, если вам нравится такой скрупулёзный подход к произведениям, то оставайтесь с нами, а мы постараемся погрузить вас в произведение и растворить в нём своими голосами. \n\n Перед началом общения, как всегда, рекомендуем ознакомится с правилами.', view = MyView())

@bot.event
async def on_member_join(member):
	guild = member.guild
	role = guild.get_role(role_id)
	if role:
			await member.add_roles(role)

bot.run(token)