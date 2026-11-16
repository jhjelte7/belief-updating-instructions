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

Amounts are written into each page, not piped from Qualtrics, so they must match the survey: €6.00 show-up, €3.00 questionnaire, €10.00 per-round and wheel bonus in German; the same numbers in $ in English. All English pages instead state a single $9.00 base payment plus an extra $10.00 that can be won through bonus payments. When an amount changes, search all pages for it and update every occurrence.

## Section links

The survey links jump to sections: `#slider`, `#overview`, `#payment`, `#bonus-wheel` (bonus-wheel pages), `#your-wheel` (ego pages). Keep these ids when editing.

## Payment rules

The English standard RQSR page (`en/index.html`) uses a 100-ticket illustration and a worked 70% example. Winning tickets are `100 - distance^2 / 100`; this rescales the original 10,000-ticket explanation without changing the winning probabilities or survey payment code. No amount or percentage is shown with decimals ($9, $10, 91%), on any page. The three examples (Example #1: A: 70% - B: 30%, #2: A: 0% - B: 100%, #3: A: 100% - B: 0%) are expandable (`<details>`). The English pages repeat the survey word for word: introduction, procedure and slider (survey pages Wheel Introduction and Game Explanation) and the Overview and Payment sections (survey overview page before Round 1, per arm). Only the details (payment rule, the three examples, the exact rule) are on GitHub alone; the survey no longer contains them. The treatment pages (`en/bonus-wheel.html`, `en/ego.html`) differ from `en/index.html` only in the title, the Bonus wheel / Your wheel paragraph in the Overview and the Payment list and coin-flip text of their arm. When the survey overview changes, change these pages too. The German pages retain the 10,000-ticket explanation.

The two English standard pages (`en/index.html`, RQSR, and `en/bdm.html`, BDM) are kept as similar as possible: the slider list, the estimate-bonus paragraphs and the coin-flip text are word for word the same, and only the payment rule differs. Keep them in sync when editing either page.

The BDM page describes the standard control treatment with matching-probability payment: a uniform comparison percentage in [0, 100], the wheel option when the report is greater than or equal to that percentage, and otherwise an independent lottery at the drawn percentage. Numerical precision must be specified in the survey implementation. Expandable multiple price lists compare the two options and illustrate the 70% example, with selected whole-percentage rows and ellipses for omitted rows; they do not restrict the comparison draw to integers. The page contains no comprehension questions or response collection.

The BDM page does not change the RQSR pages, the Qualtrics payment code, or the survey's instruction links. Only link it from a survey after that survey implements the same BDM rule.
