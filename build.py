"""Build the participant instruction pages (German + English) for the belief-updating study.

Writes:
  index.html            language choice
  de/index.html         standard treatment (Deutsch)
  de/bonusrad.html      bonus-wheel (motivated) treatment (Deutsch)
  en/index.html         standard treatment (English)
  en/bonus-wheel.html   bonus-wheel (motivated) treatment (English)

Edit the text in DE / EN below and run:  python build.py
Amounts are fixed here (they are not piped from Qualtrics), so keep them in sync with the survey.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
AMOUNTS = {  # same numbers in both surveys; € in the German survey, $ in the English (US) survey
    'de': {'show_up': '€6.00', 'questionnaire': '€3.00', 'per_round': '€2.00', 'max_belief': '€12.00', 'wheel_bonus': '€6.00'},
    'en': {'show_up': '$6.00', 'questionnaire': '$3.00', 'per_round': '$2.00', 'max_belief': '$12.00', 'wheel_bonus': '$6.00'},
}

# Ticket examples: estimate for wheel A (%) -> winning tickets out of 10,000 if A / if B is the selected wheel
EXAMPLES = [(p, 10000 - (p - 100) ** 2, 10000 - p ** 2) for p in (0, 20, 50, 80, 100)]


def fmt(n, sep):
    return f'{n:,}'.replace(',', sep)


A = AMOUNTS['de']
DE = {
    'lang': 'de',
    'title': 'Anleitung zum Experiment',
    'title_bonus': 'Anleitung zum Experiment (mit Bonus-Glücksrad)',
    'intro_h': 'Die beiden Glücksräder',
    'intro': [
        'Im Experiment verwenden wir zwei verschiedene „Glücksräder“. Jedes Rad ist gleichmäßig in vier Felder unterteilt. '
        'Rad A (das „grüne Rad“) besteht zu drei Vierteln aus Grün und zu einem Viertel aus Gelb. '
        'Rad B (das „gelbe Rad“) besteht zu drei Vierteln aus Gelb und zu einem Viertel aus Grün. '
        'Dieser Aufbau ist für Ihre Entscheidungen während des Experiments sehr wichtig.',
    ],
    'img_wheels': 'Rad A links mit drei grünen und einem gelben Feld, Rad B rechts mit drei gelben und einem grünen Feld',
    'covered': 'Während des Experiments sind die farbigen Felder der Räder verdeckt, wie im Bild unten.',
    'img_covered': 'Die beiden Räder mit verdeckten Feldern',
    'flow_h': 'Ablauf',
    'flow': [
        'Das Experiment besteht aus 6 Runden. In jeder Runde gibt es ein „ausgewähltes Glücksrad“: entweder Rad A oder Rad B. '
        'Da die Felder verdeckt sind, können Sie nicht sehen, welches Rad das ausgewählte Rad ist.',
        'In jeder Runde sehen Sie 8 Drehungen. Nach jeder Drehung wird das Feld aufgedeckt, auf das der rote Zeiger am oberen Rand des Rades zeigt. '
        'Die Abfolge der Drehungen wurde vorab festgelegt.',
        'Welches Rad das ausgewählte Rad einer Runde ist, wird vom Computer per Zufall bestimmt, und zwar passend zu den aufgedeckten Feldern: '
        'Je mehr grüne Felder aufgedeckt werden, desto wahrscheinlicher ist Rad A das ausgewählte Rad; je mehr gelbe Felder, desto wahrscheinlicher Rad B. '
        'Die Wahrscheinlichkeiten sind genau dieselben, als ob zu Beginn der Runde eines der beiden Räder zufällig (50% – 50%) ausgewählt und dann gedreht worden wäre. '
        'Die aufgedeckten Felder helfen Ihnen also einzuschätzen, welches Rad das ausgewählte Rad ist.',
        'Da immer nur ein Feld aufgedeckt wird, können Sie bei einem grünen oder gelben Feld nie ganz sicher sein, welches Rad das ausgewählte ist. '
        'Der Zeiger kann auch mehrmals auf dasselbe Feld zeigen; ob das der Fall ist, wissen Sie nicht.',
    ],
    'slider_h': 'Der Schieberegler',
    'slider': [
        'Vor der ersten Drehung und nach jeder Drehung geben Sie mit einem Schieberegler an, wie wahrscheinlich Sie es finden, '
        'dass das ausgewählte Rad Rad A (grünes Rad) oder Rad B (gelbes Rad) ist. Links neben dem Regler sehen Sie Rad A, rechts Rad B.',
    ],
    'img_slider': 'Schieberegler zwischen Rad A (links) und Rad B (rechts) mit der Anzeige „A: 50% - B: 50%“',
    'slider_list': [
        '<b>Mitte:</b> Beide Räder sind gleich wahrscheinlich (je 50%). Sie sind sich völlig unsicher.',
        '<b>Nach links:</b> Sie halten Rad A für wahrscheinlicher. Je weiter links, desto sicherer sind Sie. Ganz links bedeutet „A: 100% - B: 0%“.',
        '<b>Nach rechts:</b> Sie halten Rad B für wahrscheinlicher. Je weiter rechts, desto sicherer sind Sie. Ganz rechts bedeutet „A: 0% - B: 100%“.',
        '<b>Anzeige:</b> Über dem Regler sehen Sie die Wahrscheinlichkeiten für Rad A und B. Sie ergeben immer zusammen 100%.',
    ],
    'pay_h': 'Auszahlung',
    'pay_fixed': f'Sie erhalten eine Basiszahlung von <b>{A["show_up"]}</b> für die Teilnahme und zusätzliche <b>{A["questionnaire"]}</b> für das Ausfüllen des Fragebogens am Ende.',
    'belief_h': 'Bonus für Ihre Wahrscheinlichkeitsschätzungen',
    'belief': [
        'In jeder Runde wird eine Ihrer neun Schätzungen zufällig ausgewählt (vor der ersten Drehung oder nach Drehung 1 bis 8). '
        f'Mit dieser Schätzung nehmen Sie an einer Verlosung von <b>{A["per_round"]}</b> teil. Insgesamt können Sie so bis zu <b>{A["max_belief"]}</b> gewinnen.',
        'Je näher Ihre Schätzung an dem Rad liegt, das in dieser Runde das ausgewählte Rad ist, desto mehr Gewinnlose erhalten Sie.',
        '<b>Ihre Gewinnchance ist am größten, wenn Sie den Schieberegler immer auf die Wahrscheinlichkeit stellen, die Sie selbst für zutreffend halten.</b>',
    ],
    'rule_h': 'Die genaue Regel',
    'rule': [
        'Für die ausgewählte Schätzung gibt es 10.000 Lose. Davon sind 10.000 − (Abstand)² Gewinnlose. '
        'Der Abstand ist der Unterschied in Prozentpunkten zwischen Ihrer Schätzung für Rad A und 100, wenn Rad A das ausgewählte Rad ist, '
        'bzw. 0, wenn Rad B das ausgewählte Rad ist. Dann wird ein Los gezogen. '
        f'Ist das gezogene Los ein Gewinnlos, erhalten Sie <b>{A["per_round"]}</b>; andernfalls nichts.',
        'Beispiel: Sie haben 80% für Rad A angegeben. Ist Rad A das ausgewählte Rad, beträgt der Abstand 20, also 10.000 − 400 = 9.600 Gewinnlose (96%). '
        'Ist Rad B das ausgewählte Rad, beträgt der Abstand 80, also 10.000 − 6.400 = 3.600 Gewinnlose (36%).',
    ],
    'table_head': ('Ihre Schätzung für Rad A', 'Gewinnlose, wenn Rad A ausgewählt ist', 'Gewinnlose, wenn Rad B ausgewählt ist'),
    'sep': '.',
    'bet_h': 'Bonus-Glücksrad',
    'bet': [
        'Zu Beginn jeder Runde wetten Sie, ob Rad A oder Rad B das ausgewählte Glücksrad dieser Runde ist. Sie schließen diese Wette in jeder Runde ab, also 6 Mal.',
        f'Am Ende des Experiments wird eine Runde zufällig ausgewählt. Wenn Sie in dieser Runde auf das ausgewählte Rad gewettet haben, beträgt Ihr Bonus für das Glücksrad <b>{A["wheel_bonus"]}</b>.',
    ],
    'own_h': 'Ihr Rad',
    'own': [
        'Zu Beginn des Experiments haben Sie 9 Musteraufgaben gelöst. Eines der beiden Glücksräder ist das <b>Rad der besseren Hälfte</b>. '
        'Welches Rad das ist, wurde für Sie zufällig festgelegt und wird Ihnen im Experiment angezeigt.',
        'Dieses Rad ist <b>Ihr Rad</b>, wenn Ihr Ergebnis in den Musteraufgaben mindestens so gut war wie das der Hälfte der bisherigen Teilnehmenden; '
        'andernfalls ist das andere Rad Ihr Rad. Welches Rad Ihr Rad ist, erfahren Sie am Ende des Experiments.',
        f'Am Ende des Experiments wird eine Runde zufällig ausgewählt. Wenn in dieser Runde Ihr Rad das ausgewählte Rad ist, beträgt Ihr Bonus für Ihr Rad <b>{A["wheel_bonus"]}</b>.',
    ],
    'coin_ego': [
        'Am Ende des Experiments entscheidet ein Münzwurf, ob Ihnen <b>entweder</b> die Boni für Ihre Wahrscheinlichkeitsschätzungen <b>oder</b> der Bonus für Ihr Rad ausgezahlt wird. Sie erhalten nie beide.',
        'Deshalb lohnt es sich, bei den Schätzungen immer Ihre tatsächliche Einschätzung anzugeben, unabhängig davon, welches Rad Ihr Rad ist.',
    ],
    'rand_h': 'Zufallsbonus',
    'rand': [f'Am Ende des Experiments wird außerdem ein Zufallsbonus von <b>{A["wheel_bonus"]}</b> verlost, den Sie mit einer Wahrscheinlichkeit von 50% gewinnen.'],
    'coin_ctrl': [
        'Am Ende des Experiments entscheidet ein Münzwurf, ob Ihnen <b>entweder</b> die Boni für Ihre Wahrscheinlichkeitsschätzungen <b>oder</b> der Zufallsbonus ausgezahlt wird. Sie erhalten nie beide.',
    ],
    'coin_h': 'Münzwurf: welcher Bonus ausgezahlt wird',
    'coin': [
        'Am Ende des Experiments entscheidet ein Münzwurf, ob Ihnen <b>entweder</b> die Boni für Ihre Wahrscheinlichkeitsschätzungen <b>oder</b> der Bonus für das Glücksrad ausgezahlt wird. Sie erhalten nie beide.',
        'Deshalb lohnt es sich, bei den Schätzungen immer Ihre tatsächliche Einschätzung anzugeben, unabhängig davon, auf welches Rad Sie gewettet haben.',
    ],
    'end': 'Am Ende des Experiments teilen wir Ihnen mit, welches Rad in jeder Runde das ausgewählte Glücksrad war, und geben Ihnen eine Aufschlüsselung Ihrer gesamten Auszahlung.',
}

A = AMOUNTS['en']
EN = {
    'lang': 'en',
    'title': 'Instructions for the experiment',
    'title_bonus': 'Instructions for the experiment (with bonus wheel)',
    'intro_h': 'The two wheels of fortune',
    'intro': [
        'In this experiment we use two different "wheels of fortune". Each wheel is divided evenly into four fields. '
        'Wheel A (the "green wheel") is three quarters green and one quarter yellow. '
        'Wheel B (the "yellow wheel") is three quarters yellow and one quarter green. '
        'This setup is very important for your decisions during the experiment.',
    ],
    'img_wheels': 'Wheel A on the left with three green fields and one yellow field, Wheel B on the right with three yellow fields and one green field',
    'covered': 'During the experiment the colored fields of the wheels are covered, as in the picture below.',
    'img_covered': 'The two wheels with their fields covered',
    'flow_h': 'How it works',
    'flow': [
        'The experiment has 6 rounds. In each round there is a "selected wheel": either Wheel A or Wheel B. '
        'Because the fields are covered, you cannot see which wheel is the selected wheel.',
        'In each round you see 8 spins. After each spin, the field that the red pointer at the top of the wheel points to is revealed. '
        'The sequence of spins was fixed in advance.',
        'Which wheel is the selected wheel of a round is determined at random by the computer, in line with the revealed fields: '
        'the more green fields are revealed, the more likely Wheel A is the selected wheel; the more yellow fields, the more likely Wheel B. '
        'The probabilities are exactly the same as if one of the two wheels had been selected at random (50% – 50%) at the start of the round and then spun. '
        'So the revealed fields help you judge which wheel is the selected wheel.',
        'Because only one field is revealed at a time, a green or yellow field never tells you for certain which wheel is the selected one. '
        'The pointer may also point to the same field several times; you do not know whether that is the case.',
    ],
    'slider_h': 'The slider',
    'slider': [
        'Before the first spin and after every spin, you use a slider to tell us how likely you think it is that the selected wheel is '
        'Wheel A (green wheel) or Wheel B (yellow wheel). Wheel A is shown to the left of the slider, Wheel B to the right.',
    ],
    'img_slider': 'Slider between Wheel A (left) and Wheel B (right) showing “A: 50% - B: 50%”',
    'slider_list': [
        '<b>Middle:</b> both wheels are equally likely (50% each). You are completely unsure.',
        '<b>To the left:</b> you think Wheel A is more likely. The further left, the more certain you are. All the way left means "A: 100% - B: 0%".',
        '<b>To the right:</b> you think Wheel B is more likely. The further right, the more certain you are. All the way right means "A: 0% - B: 100%".',
        '<b>Display:</b> above the slider you see the probabilities for Wheel A and B. They always add up to 100%.',
    ],
    'pay_h': 'Payment',
    'pay_fixed': f'You receive a base payment of <b>{A["show_up"]}</b> for taking part and an additional <b>{A["questionnaire"]}</b> for completing the questionnaire at the end.',
    'belief_h': 'Bonus for your probability estimates',
    'belief': [
        'In each round, one of your nine estimates is chosen at random (before the first spin or after any one of the 8 spins). '
        f'With this estimate you take part in a lottery for <b>{A["per_round"]}</b>. In total you can win up to <b>{A["max_belief"]}</b> this way.',
        'The closer your estimate is to the wheel that is the selected wheel of that round, the more winning tickets you receive.',
        '<b>Your chance of winning is highest if you always set the slider to the probability that you yourself believe is correct.</b>',
    ],
    'rule_h': 'The exact rule',
    'rule': [
        'There are 10,000 tickets for the chosen estimate, of which 10,000 − (distance)² are winning tickets. '
        'The distance is the difference in percentage points between your estimate for Wheel A and 100 if Wheel A is the selected wheel, '
        'or 0 if Wheel B is the selected wheel. Then one ticket is drawn. '
        f'If the ticket drawn is a winning ticket, you receive <b>{A["per_round"]}</b>; otherwise nothing.',
        'Example: you reported 80% for Wheel A. If Wheel A is the selected wheel, the distance is 20, so 10,000 − 400 = 9,600 winning tickets (96%). '
        'If Wheel B is the selected wheel, the distance is 80, so 10,000 − 6,400 = 3,600 winning tickets (36%).',
    ],
    'table_head': ('Your estimate for Wheel A', 'Winning tickets if Wheel A is selected', 'Winning tickets if Wheel B is selected'),
    'sep': ',',
    'bet_h': 'Bonus wheel',
    'bet': [
        'At the start of each round you bet on whether Wheel A or Wheel B is the selected wheel of that round. You place this bet in every round, so 6 times.',
        f'At the end of the experiment one round is chosen at random. If you bet on the selected wheel in that round, your bonus for the wheel is <b>{A["wheel_bonus"]}</b>.',
    ],
    'own_h': 'Your wheel',
    'own': [
        'At the start of the experiment you solved 9 pattern tasks. One of the two wheels is the <b>wheel of the better half</b>. '
        'Which wheel this is was decided at random for you and is shown to you during the experiment.',
        'This wheel is <b>your wheel</b> if your result in the pattern tasks was at least as good as that of half of the earlier participants; '
        'otherwise the other wheel is your wheel. You find out which wheel is your wheel at the end of the experiment.',
        f'At the end of the experiment one round is chosen at random. If your wheel is the selected wheel in that round, your bonus for your wheel is <b>{A["wheel_bonus"]}</b>.',
    ],
    'coin_ego': [
        'At the end of the experiment a coin flip decides whether you are paid <b>either</b> the bonuses for your probability estimates <b>or</b> the bonus for your wheel. You never receive both.',
        'This is why it always pays to report your true estimate, regardless of which wheel is your wheel.',
    ],
    'rand_h': 'Random bonus',
    'rand': [f'At the end of the experiment there is also a random bonus of <b>{A["wheel_bonus"]}</b>, which you win with a probability of 50%.'],
    'coin_ctrl': [
        'At the end of the experiment a coin flip decides whether you are paid <b>either</b> the bonuses for your probability estimates <b>or</b> the random bonus. You never receive both.',
    ],
    'coin_h': 'Coin flip: which bonus is paid',
    'coin': [
        'At the end of the experiment a coin flip decides whether you are paid <b>either</b> the bonuses for your probability estimates <b>or</b> the bonus for the wheel. You never receive both.',
        'This is why it always pays to report your true estimate, regardless of which wheel you bet on.',
    ],
    'end': 'At the end of the experiment we tell you which wheel was the selected wheel in each round and give you a breakdown of your total payment.',
}

# One stand-alone page per language and treatment; the survey links to the page of its
# language and treatment (no language switch on the pages).
PAGES = {'de': {'std': 'index.html', 'bonus': 'bonusrad.html', 'ego': 'ego.html'},
         'en': {'std': 'index.html', 'bonus': 'bonus-wheel.html', 'ego': 'ego.html'}}


def paras(items):
    return '\n'.join(f'<p>{t}</p>' for t in items)


def page(T, kind):
    rows = '\n'.join(f'<tr><td>{p}%</td><td>{fmt(a, T["sep"])} ({a // 100}%)</td><td>{fmt(b, T["sep"])} ({b // 100}%)</td></tr>' for p, a, b in EXAMPLES)
    th = ''.join(f'<th scope="col">{h}</th>' for h in T['table_head'])
    title = T['title_bonus'] if kind == 'bonus' else T['title']
    stake = {'bonus': f'<h2>{T["bet_h"]}</h2>\n{paras(T["bet"])}\n',
             'ego': f'<h2>{T["own_h"]}</h2>\n{paras(T["own"])}\n'}.get(kind, '')
    coin = {'bonus': f'<h3>{T["coin_h"]}</h3>\n{paras(T["coin"])}\n',
            'ego': f'<h3>{T["coin_h"]}</h3>\n{paras(T["coin_ego"])}\n'}.get(
        kind, f'<h3>{T["rand_h"]}</h3>\n{paras(T["rand"])}\n<h3>{T["coin_h"]}</h3>\n{paras(T["coin_ctrl"])}\n')
    bonus = stake  # placed before the payment section, as on the bonus-wheel page
    return f'''<!doctype html>
<html lang="{T['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>
<main>
<h1>{title}</h1>

<h2>{T['intro_h']}</h2>
{paras(T['intro'])}
<img src="../img/wheels.png" width="1259" height="894" alt="{T['img_wheels']}">
<p>{T['covered']}</p>
<img src="../img/wheels-covered.png" width="746" height="524" alt="{T['img_covered']}">

<h2>{T['flow_h']}</h2>
{paras(T['flow'])}

<h2>{T['slider_h']}</h2>
{paras(T['slider'])}
<img src="../img/slider.png" width="688" height="218" alt="{T['img_slider']}">
<ul>
{''.join(f'<li>{t}</li>' for t in T['slider_list'])}
</ul>

{bonus}<h2>{T['pay_h']}</h2>
<p>{T['pay_fixed']}</p>
<h3>{T['belief_h']}</h3>
{paras(T['belief'])}
<h3>{T['rule_h']}</h3>
{paras(T['rule'])}
<div class="table-wrap"><table>
<thead><tr>{th}</tr></thead>
<tbody>
{rows}
</tbody>
</table></div>
{coin}<p>{T['end']}</p>
</main>
</body>
</html>
'''


def index():
    # The site root only forwards to the German standard page; the survey links to pages directly.
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=de/">
<title>{DE['title']}</title>
<link rel="canonical" href="de/">
</head>
<body>
<p><a href="de/">{DE['title']}</a></p>
</body>
</html>
'''


def main():
    out = {'index.html': index()}
    for T in (DE, EN):
        for kind, name in PAGES[T['lang']].items():
            out[f'{T["lang"]}/{name}'] = page(T, kind)
    for rel, html in out.items():
        path = os.path.join(HERE, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
        print('wrote', rel)


if __name__ == '__main__':
    main()
