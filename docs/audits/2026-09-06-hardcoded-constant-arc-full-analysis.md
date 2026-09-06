# The hardcoded-constant arc: what was fixed, what was wrong, and the two decisions left

**Date:** 2026-09-06 · **Beans:** `qou-psjm` `qou-rbdi` `qou-9ies` `qou-4kc0`
`qou-742w` `qou-9q4h` `qou-43v0` · **PRs:** #6904 (merged), #6926

The arc started from one observation: *scripts hardcode a truncated constant
instead of loading it, and sometimes copy a value another producer computed.*
Both turned out to be real and larger than the CODATA cases that prompted them.
The more useful result is a pattern: **in five separate instances the obvious
fix was backwards, and only measuring first caught it.**

---

## 1. What is fixed and merged

| gate | before | after | what it now catches |
|---|---|---|---|
| reference-literal (`codata_truncation_audit`) | 970 raw, ~20× over-flagged | **243 baselined, 0 NEW** | truncation / rounding / divergence against 20 canonical constants incl. three α determinations |
| witness-copy (`witness_value_copy_audit`) | did not exist | **277 baselined, 0 NEW** | a value one producer wrote into a witness, typed into another script |

Both are wired into `scripts/precision-gates.sh` as blocking rows. Both carry
`--self-test`. The witness-copy self-test now covers four properties: the
11-digit floor, AST-bounded marker extent, the trailing-comment column, and the
self-reference exclusion.

Landed on `main` via #6904 (6 commits): scope extension past `computations/`,
the deliberate-vs-accidental hand pass, the `# witness-copy-intentional:`
marker, the self-reference fix, and the chi-deuteron witness restore.

---

## 2. The five times the obvious fix was backwards

This is the reusable part.

**(a) The audit was a carrier for all 232 of its own findings.** It wrote every
literal it reported into its own witness, then indexed that witness next run.
Two findings had *no* carrier but the audit itself — self-sustaining phantoms.
Worse, every count was inflated by 1 against a `<= 3` NARROW/SHARED cut, so
literals carried by 3 real witnesses were filed SHARED. The omission made the
gate **looser**: 47 real copies were hidden. Fixing it took NARROW 232 → 277.

**(b) Importing the canonical `Vol(4_1)` would have been a 7.4e15× DOWNGRADE.**
Four findings carry it at 31 digits (correct to 2e-32). The canonical was a
Python float at 1.49e-16. The drain queue said "import the canonical"; the
canonical was the worse value.

**(c) Excluding other detectors' report witnesses promotes α_em and m_e into
"one producer's output, copied".** Measured: removes 76 findings (right) but
promotes 49 (wrong). The `<= 3` threshold stops meaning what it means once
reports leave the carrier set.

**(d) The α "edition drift" is a DETERMINATION tension, not an edition.** Below.

**(e) Three importers that "my change broke" were broken on main already** —
same file, same line, same exception, before and after. Filed as `qou-9q4h`.

---

## 3. α: the correction that matters most

I filed `qou-rbdi` claiming the CODATA registry has no fine-structure entry, and
that 41 files were off-canon against the owner's CODATA-2022 ruling. **Three of
its claims were wrong.**

- **`codata.py` DOES carry α** — `fine-structure constant` = 7.2973525643e-3 and
  `inverse fine-structure constant` = 137.035999177, already CODATA 2022. I
  grepped the *parser source*; the data lives in `data/allascii.txt`, which the
  parser reads.
- **The 41 files are a deliberate determination choice**, and
  `experimental_constants.py:150` says so three lines above the constant I called
  stale: *"DELIBERATE determination choice, not a stale edition. The Cs-recoil
  value is retained on purpose; CODATA-2022 would be a different determination,
  not merely newer digits."*
- **The `CODATA_ALPHA_INV` naming item was already found**, documented and
  deliberately retained by a sibling probe.

The physics, measured at dps 25:

| determination | value | files |
|---|---|---|
| Parker et al. 2018, Cs recoil (Berkeley) | 137.035999046 | — |
| CODATA 2018, Cs-weighted | 137.035999084 | 41 |
| CODATA 2022, incorporating both | 137.035999177 | 19 |
| Morel et al. 2020, Rb recoil (LKB) | 137.035999206 | 2 |

**Cs vs Rb: 7.6σ.** An open experimental tension. CODATA 2018 → 2022 is
**4.43σ**, and `alpha_em_schwinger_ladder_probe.py:114` asserts
`schwinger_brings_alpha_within_3sigma` — so a blind edition bump can flip a
physics verdict, and that 4.43σ *is* the Cs-vs-Rb tension surfacing in a probe's
conclusion.

**The fix, and why the shape matters.** α is now in `CANON`, **sourced from the
CODATA table rather than typed** (so a CANON row can never itself become the
hardcoded literal the gate catches), and carried as **three determinations** —
the same structure as `q0`/`q0_muon`, for the same reason:

```
single CODATA-2022 canonical    63 NEW   (38 of them determination choices)
three determinations            25 NEW   (all genuine truncations)
DIVERGENT 134 -> 96 · baseline 218 -> 243
```

A single canonical would have encoded one side of a live disagreement into a
gate and scored 41 deliberate files as defects.

---

## 4. `Vol(4_1)`: fixed, because there is no determination question

```
VOL_FIGURE_EIGHT     = 2.029883212819307  # ± 1e-12 (numerical precision)
VOL_FIGURE_EIGHT_ERR = 1e-12
```

Filed under "Knot volumes (SnapPy 3.3.2)" as a *measured* quantity. But
`Vol(4_1) = 2·Cl_2(π/3)` is exact. The float was 1.49e-16 from exact — **0.15× the
entire L1 budget** (1 ppQ = 1e-15) spent on one constant, and a Python float
injected into mpmath chains.

Now `2 * _mpm.clsin(2, _mpm.pi / 3)`, exact at ambient precision (`rel err 0.0`
at dps 50). `_ERR` retained at `0.0` — an exact constant has no measurement
uncertainty, and `mass-from-q-symbolic` imports the name.

Verified rather than assumed: the old 1e-12 term was **2.2e-5** of the dominant
`m_μ/m_e` term and its removal moves `rel_hbar_sq` by **2.45e-10** relative. All
6 in-repo importers were run; the 3 that fail, fail identically on main.
`probe-topological-mass-formula.witness.json` regenerated with **provenance-only
changes and no moved value** — so the change is numerically inert on recorded
outputs.

---

## 5. Two decisions that are genuinely yours

### 5a. The 25 α truncations — drain, or leave?

`137.0359991` (23 files) and `137.035999` (2). Both are short. The problem is
what to lengthen them *to*: `137.0359991` is **simultaneously** a prefix of
CODATA-2022 and the 10-figure rounding of CODATA-2018.

| option | pro | con |
|---|---|---|
| **1. Leave baselined** | zero risk; no physics verdict moves | 25 short literals stay; each is ~0.56 ppb from any determination |
| **2. Drain to CODATA 2022** | one canonical, gate goes quiet | takes a side in a 7.6σ open tension across 23 files; can flip a 3σ assertion |
| **3. Drain per-file to the author's determination** | correct | needs 23 reads, on a front `qou-aemx` owns |
| **4. Mark each intentional** | records intent | most are not deliberate; the marker would be a lie |

**Recommendation (judgement, not a finding): 1 now, 3 later via `qou-aemx`.**
0.56 ppb is far inside every L2 target these probes are scored against, so the
truncations are not currently costing accuracy — they cost *reproducibility*,
which is worth fixing carefully rather than fast.

### 5b. `qou-4kc0` — exclude other detectors' report witnesses?

`cal4-disguise-hunt` is a carrier for 86 witness-copy findings and
`codata-truncation-audit` for 10. Neither is a producer's output; both are lists
of literals a detector *found*.

| option | pro | con |
|---|---|---|
| **1. Exclude + re-derive the threshold** | correct | most work; the `<= 3` cut must be re-justified |
| **2. Exclude via a declared list** | auditable | decays unless maintained |
| **3. Structural discriminator** (a report carries `file`/`line` beside the literal) | no list to maintain | needs validating against the corpus first |
| **4. Nothing** | zero risk | 96 findings keep an inflated count, hiding an unmeasured number of real copies |

**Recommendation: 3, validated against 2.** A name-pattern match
(`audit`/`hunt`/`scan`) is explicitly *not* acceptable — AGENTS.md's
detector-blindness taxonomy is largely a catalogue of pattern-matchers going
wrong, and this audit has contributed two rows to it already.

---

## 6. Still blocked on other sessions

- **`qou-742w`** — the M1 leading constants typed into twelve scripts at 12
  digits. Blocked on whether `RHO_INF = 0.979796195657` is `2√6/5` (they part
  company at the 6th significant digit, rel 3.05e-07) or a measured limit. That
  changes what the fix is; it is the M1 epic's call.
- **`qou-43v0`** — `bar_pairing_binding_observable.py:187` writes the chi-cache
  path its own docstring calls an input. The two payloads have **disjoint** key
  sets, so this is two producers sharing a path, not one stale copy. Which
  payload owns it is `qou-49vn`'s open question.
- **`qou-9q4h`** — three importers die on `mpf.__format__`. One line each; the
  fix needs a run that writes witnesses.

---

## 7. What I would not repeat

Every correction above came from measuring something I had already asserted.
The three that cost the most:

1. **Grepping a parser instead of the data it serves.** `codata.py` has no `alpha`
   in its source and every α in its table.
2. **Not reading the file I was citing.** The rationale for the "stale" constant
   was three lines above it.
3. **Not running the corpus-grep before filing.** The naming item was already
   found, fixed and documented by a sibling.

The discipline that worked: measure the *canonical* before draining toward it;
baseline a detector change in **both** directions; and run the consumers rather
than reasoning about whether they would break.
