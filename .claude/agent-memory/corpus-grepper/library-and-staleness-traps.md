# corpus-grepper — detail file: library reach + number staleness

Read on demand. Summarised in `MEMORY.md`; this file carries the measurements.

## TRAP — for some docs `sections/` is BOILERPLATE; the text is in `ocr/`

Path 5 as written (`grep library/*/sections/`) reads a file that, for scanned
/ JSTOR-style docs, contains only the download banner. The real text is under
`library/<doc-id>/ocr/page-NNN.txt`, which **no documented path searches**.

Measured 2026-08-30 on `origin/main`: 536 library dirs, **25 carry an `ocr/`
dir**, 11 of those have exactly one `sections/` file, and **10 of the 11 hold
under 15 % of their OCR bytes in `sections/` — six under 3 %**:

| doc | sections B | ocr B | ratio |
|---|---:|---:|---:|
| `centsim` | 275 | 45574 | 0.006 |
| `bm-markov-j` | 268 | 31396 | 0.009 |
| `mcmullen-braids-hodge-2013` | 390 | 34760 | 0.011 |
| `1992evansberger` | 437 | 20305 | 0.022 |
| `procrsoclondona92` | 1916 | 46511 | 0.041 |

Worked case, and it is why this was found: **`procrsoclondona92` = Moffatt &
Ricca 1992, *Helicity and the Calugareanu invariant*** — the canonical source
for `Lk = Wr + Tw` and `H = nΦ²` (helicity of one knotted flux tube = its
SELF-linking × flux²). Its `sections/sec-000-document.md` is 1916 B of JSTOR
banner; the decomposition is in `ocr/page-002.txt` and is invisible to path 5.

**Add a fourth tier when the topic could be in an older / scanned paper:**

```sh
grep -rln <topic> library/*/ocr/
```

Cheap discriminator that a doc is affected: `structure.json` reports 1 section
titled "Document" while `ocr/` has many pages.


## TRAP — a number can be stale by CONVENTION and by IMPORT-CONE at once

Before citing any measured binding/Gram figure predating **2026-08-09**, check
both. Worked case, all four witnesses from one 2026-07-11 session:

- **Convention.** `binding_ghost_gram_quadratic.py`'s `⟨g⟩²_G = −0.4275` and
  the `b*` bridge's `0.8550672621` are convention **C**. `pyhecke/gram.py`'s
  own historical banner lists C eigenvalues `−0.855067 … +3.476950` against D
  `−0.752702 … +4.230339` — the "bit-identical" check value *is* the C
  eigenvalue. Convention D is canonical (owner ruling 2026-08-15) and under it
  `G` is **singular**, so the Gram inverse the route wants does not exist
  (bean `qou-cds2`).
- **float64.** All four are on `computations/raw-float64-baseline.json`
  (`binding-ghost-gram-quadratic` 1, `binding-bstar-bridge` 4,
  `binding-bond-extensive-derivation` 1, `binding-edge-set-selection` 4). The
  probe does `np.array(G.G, dtype=float)` — the banned pattern.
- **Import cone.** Bean `qou-wlaf` measured a sibling binding witness wrong by
  5–49 % because `atom_braid_word_3A` was mpf-ified *downstream*; the
  producer file never changed, so `scriptHash` triage cannot see it.

Distinguish the **algebra** from the **numbers**: split-link factorisation,
tracelessness, and `C(w) = tr(w²) − tr(w)² = ⟨δw⟩²_G` are convention-free and
survive; every decimal in that audit does not.



## TRAP — `beans create` is not idempotent

It mints a fresh ID every call and dedupes on nothing. Run the exact-title
existence check in `.claude/skills/local/todo-manager.md` §"Check before you
create" first; on a match, claim the existing bean with
`beans update <id> --status in-progress`.

An unguarded re-run on 2026-08-04 produced **14,688** duplicate beans — 92%
of every open bean — which starved the idle-backlog policy of signal and
corrupted a later agent's corpus-grep badly enough to nearly land a false
correction in a PR body (bean `qou-2ryn`). Your searches read `.beans/`;
that is why this matters to you.

## TRAP — a number can be stale by CONVENTION and by IMPORT-CONE at once

Before citing any measured binding/Gram figure predating **2026-08-09**, check
convention (C vs the canonical D), the float64 baseline, and import-cone drift
— the 2026-07-11 ghost-Gram witnesses fail all three. **Separate the algebra
from the numbers:** factorisation and trace identities survive a convention
change; every decimal does not. Evidence:
`library-and-staleness-traps.md`.

