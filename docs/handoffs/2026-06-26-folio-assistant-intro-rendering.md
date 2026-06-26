# Handoff: folio-assistant rendering changes (Introduction PDF review)

**Audience:** an agent working in the **`litlfred/folio-assistant`** repo
(the platform repo — content→LaTeX→PDF rendering lives there, *not* in
`qou`). These six items came out of an owner walk-through of the rendered
**Introduction** PDF. None of them are fixable from the `qou` content repo;
they are all renderer / preamble / status-label concerns.

**Why this is a handoff and not a PR here:** `qou` is content-only. The
LaTeX preamble, page geometry, margin-note emission, formalization-status
display strings, and the markdown→LaTeX converter all live in
folio-assistant (imported into a `qou` checkout via
`scripts/setup-folio-assistant.sh` → `folio-assistant/` symlink). In the
review environment that repo was network-blocked (403), so the exact
file:line coordinates below are *where to look*, to be confirmed in the
folio-assistant tree.

**The qou status enum** (source of truth for items 1 & 6) is
`qou/schemas/qou-types.ts`:
```ts
export type FormalizationStatus =
  | "not_started" | "stated" | "has_sorry" | "proved" | "mathlib_ok";
```
The **display strings** for these are mapped somewhere in folio-assistant
(likely `adapters/paper/` or `schemas/`) — that mapping is what items 1 & 6
edit. Grep folio-assistant for the literal current strings:
`"Merged into Mathlib"`, `"genuine statement in Lean"`, `"Drafted"`.

---

## 1. "Merged into Mathlib" is a false claim — fix the `mathlib_ok` label

**Problem.** The margin status note for `mathlib_ok` renders as **"Merged
into Mathlib"**. The project has **never contributed anything to Mathlib**.
`mathlib_ok` only means *"the declaration type-checks, sorry-free, using
only Mathlib as a dependency."* "Merged into Mathlib" is an outright
overclaim and must go.

**Fix.** In the status→display-string map, change `mathlib_ok`'s string.
Suggested honest wording (pick one, owner preference):
- `"Proved (Mathlib only)"`
- `"Mathlib-verified"`
- `"Proved, Mathlib deps"`

**While you're there, review the whole mapping for honesty + length**
(length matters for item 5). Current → suggested:

| status | likely current string | suggested (short, honest) |
|---|---|---|
| `not_started` | (none / "Not started") | *(no margin note)* |
| `stated` | "Drafted: genuine statement in Lean" | `"Stated in Lean"` |
| `has_sorry` | "Drafted …" / "Has sorry" | `"Lean: proof pending"` |
| `proved` | "Proved" | `"Proved in Lean"` |
| `mathlib_ok` | **"Merged into Mathlib"** | `"Proved (Mathlib only)"` |

**Acceptance:** no rendered margin note claims Mathlib contribution; the
`stated`/`has_sorry` labels fit the margin (see item 5).

---

## 2. Add a GitHub source link `<>` in the right margin per block

**Ask.** In the right margin of each content block, render a small
clickable **`<>`** that links to that block's **`.md`** source on GitHub
(the canonical human-readable face — never `.ts`/`.lean` as the primary
link, per `qou/AGENTS.md`).

**URL shape:**
```
https://github.com/litlfred/qou/blob/<branch>/<path-to-block>.md
```
The renderer already knows each block's source path (it reads the `.md`).
It needs the **branch/ref** — thread the current git ref (or a configured
`PUBLIC_BRANCH`, default `main`) into the render context. The qou type
`qou/schemas/qou-types.ts` also has a `github_source_url` field that may
already carry this for some blocks; prefer it when present, else construct
from `<repo>/blob/<branch>/<block .md path>`.

**LaTeX.** Emit a `\marginnote{\href{<url>}{\small\texttt{<>}}}` (or the
existing margin command — see item 3/5) right-aligned in the margin.

**Acceptance:** every block shows a `<>` in the right margin linking to its
`.md` on GitHub at the built ref.

---

## 3. Make the right margin width equal the left

**Problem.** The right margin is currently wider than the left
(asymmetric — widened to hold the status margin-notes), which looks
unbalanced.

**Fix.** In the LaTeX preamble (find the `\usepackage[...]{geometry}` /
`\geometry{...}` / `marginparwidth` settings — likely a `.tex` template or
a TS template string in folio-assistant), set the right margin equal to the
left (symmetric `left=` / `right=`, and a `marginparwidth` that fits within
a symmetric right margin). The margin notes (items 1, 2, 5) must still fit —
so this couples with item 5 (shorter labels + wrapping).

**Acceptance:** left and right text margins are visually equal; margin
notes still render without overflow.

---

## 4. Introduction chapter heading should read "0. Introduction"

**Problem.** The Introduction chapter heading renders as just
**"Introduction"** (unnumbered), but its sections are numbered **0.1, 0.2,
0.3** — i.e. the chapter *is* logically chapter 0. The heading should show
the number: **"0. Introduction"**.

**Fix.** Find where chapter titles become `\chapter{…}` / `\chapter*{…}`
(or a custom heading macro). The intro is currently emitted unnumbered
(`\chapter*`) while its section counter is set to chapter 0. Either emit it
numbered with the chapter counter at 0, or prefix the starred heading with
the number explicitly. The chapter manifest is
`qou/content/quantum-observable-universe/introduction/introduction.ts`
(`title: "Introduction"`, `tabLabel: "I"`). The **Notation** front-matter
chapter (`tabLabel: "N"`) stays unnumbered; only Introduction = 0.

**Acceptance:** heading reads "0. Introduction"; sections stay 0.1/0.2/0.3;
chapter 1 onward unchanged.

---

## 5. Margin-note overflow (overfull \hbox off the right page edge)

**Problem.** Long status labels ("Drafted: genuine statement in Lean") and
long inline math in margin notes ("n→…") overflow the right page edge
(overfull `\hbox`). (Note: main is already landing related render fixes —
e.g. `78503979 fix(render): wrap raw 𝔔_β`, `04fc76a7 balance inline $` —
coordinate with whoever is doing those.)

**Fix.** Two levers, do both:
- **Shorter labels** (item 1) — "Stated in Lean" not "Drafted: genuine
  statement in Lean".
- **Make margin notes wrap + not protrude** — ensure the margin command
  uses `\raggedright`, a `\footnotesize`/`\scriptsize` font, and a width
  bound to `\marginparwidth` so long content wraps instead of overflowing.
  For unbreakable inline math in a margin note, wrap in an `\mbox`-free
  `\sloppy` / allow `\linebreak`, or shrink.

**Acceptance:** a clean PDF build with **no overfull-\hbox warnings**
originating from margin notes in the Introduction.

---

## 6. Numeric chapter cross-references (`\cref`-style) — optional but wanted

**Context.** Raw `\ref{chap:foo}` written in block `.md` prose renders as
**literal "\ref{…}" text** — the markdown→LaTeX converter escapes it. The
only working cross-ref today is markdown `[text](#label)` →
`\hyperref[label]{text}`, which carries **hard-coded link text** (no auto
number). On the qou side this was worked around in the Introduction by
linking **chapter titles** (`[*Quantum Universes*](#chap:qu)`) — stale-proof
but numberless.

**Ask.** Add support so a label reference can render the **chapter/section
number** automatically (like LaTeX `\cref`/`\autoref`). Options:
- Teach the converter to pass a chosen markdown form (e.g. `[](#chap:qu)`
  with empty text, or a `:cref[chap:qu]` directive) through to
  `\cref{chap:qu}` / `\autoref{chap:qu}`, and ensure `cleveref`/`hyperref`
  is loaded in the preamble.
- This fixes the **whole corpus at once** — there are ~20+ stale hard-coded
  `[Chapter N](#chap:X)` references across `qou/content/**` whose numbers
  are already wrong (e.g. `chap:brings-surface` is cited as both "Chapter 6"
  and "Chapter 9" in different files). With `\cref` support, a codemod can
  replace the hard-coded numbers with auto-numbered refs.

**Acceptance:** a label-based reference renders the live chapter number;
`cleveref` (or `hyperref` autoref) is loaded; document a codemod path for
the existing hard-coded numbers.

---

## Verification

After items 1–5, rebuild the Introduction PDF and confirm: "0. Introduction"
heading; symmetric margins; a `<>` GitHub link + an honest, non-overflowing
status note per block; no "Merged into Mathlib"; no margin overfull-\hbox.
Item 6 is verified corpus-wide (a numeric ref renders the live number).
