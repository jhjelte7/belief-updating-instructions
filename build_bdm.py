"""Build the separate English BDM instructions: python build_bdm.py.

Uses the standard treatment's shared content and amounts from build.py.
This adds an instruction page; it does not change survey payment code or links.
"""
from decimal import Decimal
from pathlib import Path

from build import AMOUNTS, EN, paras


def page():
    amount = AMOUNTS['en']
    prize = amount['per_round']
    assert prize == amount['wheel_bonus'], 'This page assumes equal prizes for both bonuses.'
    fixed = sum(Decimal(amount[key].removeprefix('$')) for key in ('show_up', 'questionnaire'))
    total_low = f'${fixed:.2f}'
    total_high = f'${fixed + Decimal(prize.removeprefix("$")):.2f}'
    slider_items = list(EN['slider_list'])
    slider_items[0] = '<b>Middle:</b> you think both wheels are equally likely (50% each).'
    practice = [
        (
            'The computer draws 30%. Which option is used?',
            f'The wheel option. Your estimate of 60% is higher than 30%. You receive {prize} '
            'if the selected wheel is A, and $0 if it is B.',
        ),
        (
            f'The computer draws 80%. What is your chance of winning {prize}?',
            '80%. The lottery option is used because 80% is higher than your estimate of 60%. '
            'The lottery uses the percentage drawn by the computer, not your estimate.',
        ),
        (
            'With the 80% lottery, can you win if Wheel B is selected?',
            'Yes. The lottery result does not depend on which wheel is selected.',
        ),
        (
            'Can changing your answer change the percentage the computer draws?',
            'No. Your answer can change which option is used, but it does not change the random percentage.',
        ),
        (
            'Can both the estimate bonus and the random bonus be paid?',
            'No. The fair coin flip selects only one of these two bonuses.',
        ),
    ]
    answers = '\n'.join(
        f'<details><summary>{question}</summary><p>{answer}</p></details>'
        for question, answer in practice
    )
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Instructions for the experiment — BDM</title>
<meta name="description" content="Instructions for the wheel experiment, with a two-option probability-estimate bonus.">
<link rel="stylesheet" href="../style.css">
<style>
.options {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 16px 0; }}
.option {{ padding: 16px; border: 1px solid var(--line); border-radius: 6px; }}
.option h4 {{ font-size: 1rem; margin: 0 0 8px; }}
.option p {{ margin: 0; }}
.reminder {{ border-left: 3px solid var(--accent); padding: 10px 16px; background: var(--head); }}
details {{ border-bottom: 1px solid var(--line); padding: 12px 0; }}
summary {{ cursor: pointer; font-weight: 600; }}
summary:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 4px; }}
details p {{ margin: 10px 0 0; }}
.practice-intro {{ color: var(--muted); }}
@media (max-width: 520px) {{ .options {{ grid-template-columns: 1fr; }} }}
@media print {{ .options, tr {{ break-inside: avoid; }} details::details-content {{ content-visibility: visible; }} }}
</style>
</head>
<body>
<main>
<h1>{EN['title']}</h1>

<h2>{EN['intro_h']}</h2>
{paras(EN['intro'])}
<img src="../img/wheels.png" width="1259" height="894" alt="{EN['img_wheels']}">
<p>{EN['covered']}</p>
<img src="../img/wheels-covered.png" width="746" height="524" alt="{EN['img_covered']}">

<h2>{EN['flow_h']}</h2>
{paras(EN['flow'])}

<h2>{EN['slider_h']}</h2>
{paras(EN['slider'])}
<img src="../img/slider.png" width="688" height="218" alt="{EN['img_slider']}">
<ul>
{''.join(f'<li>{item}</li>' for item in slider_items)}
</ul>

<h2 id="payment">Payment</h2>
<p>{EN['pay_fixed']}</p>
<p>At the end, the computer randomly selects <b>one of the six rounds</b>. Each round has the same chance of being selected. Only this round counts for your bonus.</p>
<p>A <b>fair coin flip</b> decides which of the following two bonuses is paid. Each has a 50% chance of being chosen. You never receive both.</p>
<ul>
<li><b>Bonus for your probability estimate:</b> one of your estimates in the selected round is used as explained below.</li>
<li><b>Random bonus:</b> a separate lottery gives you a 50% chance of receiving {amount['wheel_bonus']}, and otherwise pays $0.</li>
</ul>
<p>Either bonus can pay {prize} or $0. Your total payment, including participation and the completed questionnaire, is therefore {total_high} or {total_low}.</p>

<h3 id="estimate-bonus">Bonus for your probability estimate</h3>
<p>If the coin selects this bonus, <b>one of your nine estimates</b> in the selected round is chosen at random. Each estimate has the same chance of being chosen, including your estimate before the first spin.</p>
<p>There are two ways to win {prize}:</p>
<div class="options">
<div class="option">
<h4>Wheel option</h4>
<p>You receive <b>{prize} if Wheel A is the selected wheel</b> in that round. If it is Wheel B, you receive $0.</p>
</div>
<div class="option">
<h4>Lottery option</h4>
<p>You receive <b>{prize} with a given chance</b>, and $0 otherwise. This lottery does not depend on which wheel is selected.</p>
</div>
</div>
<p><b>Your estimate tells the computer which option to use.</b></p>
<p>The computer draws a random percentage between 0% and 100%, with all values equally likely. This is the lottery's chance of winning. Your answer does not change this draw, and the draw does not depend on which wheel is selected.</p>
<ul>
<li>If <b>your estimate for Wheel A is higher</b> than the lottery chance, the computer uses the <b>wheel option</b>.</li>
<li>If <b>the lottery chance is higher</b> than your estimate, the computer uses the <b>lottery option</b>, with the chance it drew. A separate random draw then decides whether you win.</li>
<li>If they are equal, the computer uses the wheel option.</li>
</ul>

<h3>An example</h3>
<p>Suppose you report <b>A: 70% — B: 30%</b>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">The computer draws</th><th scope="col">Option used</th><th scope="col">How you win {prize}</th></tr></thead>
<tbody>
<tr><th scope="row">40%</th><td>Wheel option</td><td>You win if Wheel A is the selected wheel. If it is Wheel B, you receive $0.</td></tr>
<tr><th scope="row">90%</th><td>Lottery option</td><td>You have a 90% chance of winning, whichever wheel is selected.</td></tr>
</tbody>
</table></div>
<p>The 70% in this example is just an example, not a suggested answer.</p>

<h3>Why give your own best estimate?</h3>
<p>Your own best estimate makes the computer use the option that, according to your estimate, gives you the greater chance of winning. If the chances are equal, either option is equally good. Reporting a higher or lower number can make it use the option you think is worse.</p>
<p class="reminder"><b>Report your own best estimate to give yourself the best overall chance of winning the {prize} bonus.</b></p>

<h2>Check your understanding</h2>
<p class="practice-intro">Optional practice: try each question, then open it to see the answer. These practice questions do not count for payment.</p>
<p>Suppose an example answer is <b>A: 60% — B: 40%</b>. The first four questions concern the bonus for this estimate.</p>
{answers}

<h2>At the end</h2>
<p>{EN['end']}</p>
</main>
</body>
</html>
'''


def main():
    destination = Path(__file__).resolve().parent / 'en' / 'bdm.html'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(page(), encoding='utf-8', newline='\n')
    print('wrote en/bdm.html')


if __name__ == '__main__':
    main()
