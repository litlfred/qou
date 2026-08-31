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


## TRAP — a ripgrep FILE CAP is not a result (measured on myself, 2026-08-30)

A scoped SEMF sweep returned `Found 60 files limit: 60`. That line is
**truncation**, not a count, and it was read as a count. The uncapped re-run
returned **98**. Worse, the background job launched as the uncapped check was
*itself* silently short — 62 hits, `content/` only, no `computations/` or
`docs/` at all, exit 0 — while `computations/.../delta2phi_semf_pairing_probe.py`
is literally named `semf`. So two independent measurements of one surface were
both incomplete, in different ways, and both exited clean.

**Read the cap line before the hit list, and when a second pass is meant to
confirm a first, verify its SCOPE covers the trees the first one did.** An
exit-0 grep over the wrong subtree is indistinguishable from an exhaustive one.

In that instance the verdict survived — the seven recovered files were all
pre-refutation and none bore on the question — but that was luck, not method.

## RESOLVED TOPIC — `A^{1/3}` / nuclear radius: refuted four ways, do NOT re-open

Asked again 2026-08-30 and it costs a full sweep each time. The answer:

- **bean `qou-nf9l` (COMPLETED)** +
  `docs/audits/2026-07-13-packing-exponent-combinatorics-derive-or-refute.md` —
  all three corpus combinatorial classes refuted symbolically. *"The framework
  has no combinatorial object producing a cube root of A; `A^{-1/3}` remains an
  empirical import."* Its census: every `1/3` in the corpus is a **fixed index
  3**, never an `A`-th root.
- **The exponent the data wants is `1/4`, not `1/3`.** 8-pair mirror fit
  `p* = 0.252 ± 0.020` — `1/4` at 0.1σ, `1/3` at **4.1σ**. Independently
  reproduced on 5 pairs 2026-08-30 (`coulomb_from_crossing_counts_probe.py`).
- **The hyperbolic route gives `ln A`, not `A^{1/3}`** —
  `2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md:326-341`: in
  `H³`, `V ∝ A` ⇒ `R ~ ½ln(2V/π)`. This is the strongest structural fact.
- **There is no volume→length transport in the corpus, and it says so about
  itself** — `pion_radius_and_cusp_volume_gap_probe.py:56-63`. Every corpus
  length is a Compton inversion `ℏc/mass`.
- **The radius formulation is IDENTICALLY the energy formulation** (40-digit
  verified, `2026-07-13-pion-radius-and-vol-to-radius-gaps.md` GAP 2), so there
  is no length object owed at all. Attack `E_pack ∝ m_π·A^{-1/3}` in pure MeV.

**Not refuted, and often confused with the above:** the `Z(Z-1)` multiplicity.
`CrossingCountAffine` excludes only the LINEAR class; the counts reach it
quadratically (`16·Z(Z-1) = (n₊-n₋)(n₊-n₋-4)`, `CoulombFromCrossingCounts`).
Keep the two halves of `Z(Z-1)/A^{1/3}` apart — one is open, one is closed.
