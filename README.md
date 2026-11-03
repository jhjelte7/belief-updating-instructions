# Belief-updating study: participant instructions

Detailed instructions that participants can open from the Qualtrics survey: one stand-alone page per language and treatment, with no language switch.
The survey links to its own language's page (German now; switch the links to `en/` when the survey is translated). The site root forwards to `de/`.

| Page | Treatment | Language |
|---|---|---|
| `de/index.html` | standard | Deutsch |
| `de/bonusrad.html` | bonus wheel (motivated) | Deutsch |
| `en/index.html` | standard | English |
| `de/ego.html` | own wheel (Raven's matrices) | Deutsch |
| `en/bonus-wheel.html` | bonus wheel (motivated) | English |
| `en/ego.html` | own wheel (Raven's matrices) | English |
| `en/bdm.html` | standard, BDM alternative | English |

The pages are generated: edit the text in `build.py`, then run `python build.py` and commit the output.
Amounts (show-up fee, bonus per round, wheel bonus) are set in `AMOUNTS` in `build.py` and must match the survey.

The English standard RQSR page (`en/index.html`) uses a 100-ticket illustration and a worked 70% example, configured in `EN_STANDARD_RQSR`. Winning tickets are `100 - distance^2 / 100`, retaining decimal values; this rescales the original 10,000-ticket explanation without changing the winning probabilities or survey payment code. Example ticket totals and winning percentages display two decimal places. The other RQSR pages retain their existing explanation.

The separate English BDM page is generated with `python build_bdm.py`. Edit its payment text in `build_bdm.py`; the wheels, slider images, shared experiment description, and amounts come from `build.py`.

This page describes the standard control treatment with matching-probability payment: a uniform comparison percentage in [0, 100], the wheel option when the report is greater than or equal to that percentage, and otherwise an independent lottery at the drawn percentage. Numerical precision must be specified in the survey implementation. Expandable multiple price lists compare the two options and illustrate the 70% example, with selected whole-percentage rows and ellipses for omitted rows; they do not restrict the comparison draw to integers. The page contains no comprehension questions or response collection.

Adding this alternative page does not change the existing RQSR pages, the Qualtrics payment code, or the survey's instruction links. Only link it from a survey after that survey implements the same BDM rule.
