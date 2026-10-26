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

The pages are generated: edit the text in `build.py`, then run `python build.py` and commit the output.
Amounts (show-up fee, bonus per round, wheel bonus) are set in `AMOUNTS` in `build.py` and must match the survey.
