# Belief-updating study: participant instructions

Detailed instructions that participants can open from the Qualtrics survey: one stand-alone page per language and treatment, with no language switch.
The survey links to its own language's page (German now; switch the links to `en/` when the survey is translated). The site root forwards to `de/`.

| Page | Treatment | Language |
|---|---|---|
| `de/index.html` | standard | Deutsch |
| `de/bonusrad.html` | bonus wheel (motivated) | Deutsch |
| `de/ego.html` | own wheel (Raven's matrices) | Deutsch |
| `en/index.html` | standard (RQSR) | English |
| `en/bdm.html` | standard, BDM alternative | English |
| `en/bonus-wheel.html` | bonus wheel (motivated) | English |
| `en/ego.html` | own wheel (Raven's matrices) | English |

## Editing

The HTML files are the source: edit the text directly in the file (on GitHub, open the file and click the pencil icon) and commit. GitHub Pages republishes the site automatically within a minute or two.

- Each page is self-contained, so a change to text that appears on several pages has to be made on each of them.
- `style.css` holds the shared layout; `img/` holds the wheel and slider images.
- Bold (`<b>…</b>`) is used only for headings and amounts on the English standard pages (`en/index.html`, `en/bdm.html`).

## Amounts

Amounts are written into each page, not piped from Qualtrics, so they must match the survey: €6.00 show-up, €3.00 questionnaire, €10.00 per-round and wheel bonus in German; the same numbers in $ in English. The two English standard pages (`en/index.html`, `en/bdm.html`) instead state a single $9.00 base payment plus an extra $10.00 that can be won through bonus payments. When an amount changes, search all pages for it and update every occurrence.

## Payment rules

The English standard RQSR page (`en/index.html`) uses a 100-ticket illustration and a worked 70% example. Winning tickets are `100 - distance^2 / 100`, retaining decimal values; this rescales the original 10,000-ticket explanation without changing the winning probabilities or survey payment code. Example ticket totals and winning percentages display two decimal places. The other RQSR pages retain the 10,000-ticket explanation.

The two English standard pages (`en/index.html`, RQSR, and `en/bdm.html`, BDM) are kept as similar as possible: the slider list, the estimate-bonus paragraphs and the coin-flip text are word for word the same, and only the payment rule differs. Keep them in sync when editing either page.

The BDM page describes the standard control treatment with matching-probability payment: a uniform comparison percentage in [0, 100], the wheel option when the report is greater than or equal to that percentage, and otherwise an independent lottery at the drawn percentage. Numerical precision must be specified in the survey implementation. Expandable multiple price lists compare the two options and illustrate the 70% example, with selected whole-percentage rows and ellipses for omitted rows; they do not restrict the comparison draw to integers. The page contains no comprehension questions or response collection.

The BDM page does not change the RQSR pages, the Qualtrics payment code, or the survey's instruction links. Only link it from a survey after that survey implements the same BDM rule.
