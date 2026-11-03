"""Build the separate English BDM instructions: python build_bdm.py.

Uses the standard treatment's shared content and amounts from build.py.
This adds an instruction page; it does not change survey payment code or links.
"""
from pathlib import Path

from build import AMOUNTS, EN, paras


def page():
    amount = AMOUNTS['en']
    prize = amount['per_round']
    assert prize == amount['wheel_bonus'], 'This page assumes equal prizes for both bonuses.'
    slider_items = list(EN['slider_list'])
    slider_items[0] = '<b>Middle:</b> you think both wheels are equally likely (50% each).'
    choice_rows = '\n'.join(
        f'<tr><th scope="row">{chance}%</th>'
        f'<td>{prize} if Wheel A is selected</td>'
        f'<td>{chance}% chance of {prize}</td>'
        f'<td><b>{"Wheel option" if chance <= 70 else "Lottery option"}</b></td></tr>'
        for chance in range(101)
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
.choice-list {{ border: 1px solid var(--line); border-radius: 6px; padding: 14px 16px; margin: 20px 0; }}
summary {{ cursor: pointer; font-weight: 600; }}
summary:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 4px; }}
.mpl-scroll {{ max-height: 400px; overflow: auto; margin-top: 14px; }}
.mpl-scroll:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
.mpl-scroll table {{ min-width: 520px; }}
.mpl-scroll thead th {{ position: sticky; top: 0; z-index: 1; }}
.mpl-scroll caption {{ text-align: left; font-weight: 600; padding-bottom: 10px; }}
@media (max-width: 520px) {{ .options {{ grid-template-columns: 1fr; }} }}
@media print {{ .options, tr {{ break-inside: avoid; }} .mpl-scroll {{ max-height: none; overflow: visible; }} }}
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
<h3 id="estimate-bonus">Bonus for your probability estimate</h3>
<p>At the end of the experiment, <b>one of the six rounds</b> is chosen at random. In that round, <b>one of your nine estimates</b> is chosen at random: before the first spin or after any of the eight spins. Each round and each estimate within it has the same chance of being chosen. The chosen estimate is used for a chance to win <b>{prize}</b>.</p>
<p><b>Your chance of winning is highest if you always set the slider to the probability that you yourself believe is correct.</b></p>

<h3>The payment rule</h3>
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
<p>Your own best estimate makes the computer use the option that, according to your estimate, gives you the greater chance of winning. If the chances are equal, either option is equally good. Reporting a higher or lower number can make it use the option you think is worse.</p>

<details class="choice-list">
<summary>See the full choice list for the 70% example</summary>
<p>This list illustrates the payment rule at whole percentages. For an estimate of 70%, the wheel option is used through 70%; above 70%, the lottery option is used. Your estimate fills in these choices automatically.</p>
<p>The computer's random percentage can also fall between the whole percentages shown. Both options pay $0 when you do not win.</p>
<div class="mpl-scroll" tabindex="0" role="region" aria-label="Choice list for a 70 percent estimate; scroll to see all lottery chances">
<table>
<caption>Your estimate: A 70% — B 30%</caption>
<thead><tr><th scope="col">Lottery chance</th><th scope="col">Wheel option</th><th scope="col">Lottery option</th><th scope="col">Option used</th></tr></thead>
<tbody>
{choice_rows}
</tbody>
</table>
</div>
</details>

<h3>{EN['rand_h']}</h3>
{paras(EN['rand'])}
<h3>{EN['coin_h']}</h3>
<p>At the end of the experiment, a fair coin flip decides whether you are paid <b>either</b> the bonus for your probability estimate <b>or</b> the random bonus. Each has a 50% chance of being chosen. You never receive both.</p>
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
