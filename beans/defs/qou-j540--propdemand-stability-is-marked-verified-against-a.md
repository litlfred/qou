---
# qou-j540
title: prop:demand-stability is marked verified against a float64 witness blind at Z=82 — and its successor is not a drop-in replacement
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T13:54:58Z
updated_at: 2026-11-15T22:26:00Z
parent: qou-9nnz
---

## The decision

`folio/quantum-observable-universe/nuclear-interactions/demand-stability.ts`
(the proposition **`prop:demand-stability`** — the block stating when a derived
atom is beta-stable, shell-closed, or doubly magic) carries

```ts
computation: {
  script:  "computations/all_nuclides_sdp_admissibility.py",
  witness: "computations/all-nuclides-sdp-admissibility.witness.json",
  status:  "verified",
}
```

That producer is **superseded**, and its successor's first line says so —
`all_nuclides_sdp_admissibility_mp.py` opens *"Supersedes
`all_nuclides_sdp_admissibility.py` on two counts, both of which were live
defects rather than refinements."* The block still points at the superseded one
and still says `verified`.

**What needs deciding is not whether to repoint it.** It is that the obvious
repoint is *wrong*, because the two producers do not measure the same
population — so somebody has to choose what `prop:demand-stability` should be
verified against. That is a paper question.

## Why the obvious fix does not work — measured

| | superseded (f64) | successor (mp) |
|---|---:|---:|
| population | AME2020 chart | synthetic **(Z, N) grid** |
| rows | 3,558 | 4,932 |
| NF overflow rows | **1,337 (37.6 %)** | 0 |
| distinct Z / max Z | 78 / 77 | 93 / 92 |
| solvable isotopes at Z=50 | 42 | 161 |
| solvable isotopes at **Z=82** | **0** | 161 |
| rows at **Z=126** | **0** | **0** |

The successor's grid is **magic-Z dense on purpose**: Z ∈ {2, 8, 20, 28, 50, 82}
each get N = 0…160 (161 rows), every other Z gets 47. So it is not the AME chart
with the overflow fixed — it is a different sampling that happens to cover the
magic numbers well.

**Z = 126 is absent from BOTH.** The successor's docstring criticises the f64
version for *"`Z = 126` had no rows at all"*; the successor has none either. Do
not read the supersession as having closed that.

## Why it matters for the paper specifically

The block's three claims are about **shell closure and magic numbers**. The
witness backing them could not solve a single isotope at **Z = 82** — a magic
number, and one of the two the block's "doubly magic" clause is about. So the
evidence cited is blind precisely where the claim is strongest. The f64
`build_atom_nf` overflowed above A ≈ 163; that is not a precision nuisance, it
is a **coverage hole shaped like the claim**.

The superseded witness's own headline numbers inherit it:
`b_permitted_count_scalar_lp = 2221` out of 3,558 — but 1,337 of the
non-permitted are *overflow rows*, not physics. Read literally, 2221/3558 is a
62 % admissibility rate; read correctly, it is 2221/2221 of what could be
computed. The successor's docstring makes the same point: *"the witness's own
'permitted-nuclei count' was an overflow cutoff being read as physics."*

Note `b_permitted_count_frobenius = 0` (0 of 3,558) is a *separate* issue with
its own three probes (`frobenius_admissibility_diagnostic.py`,
`frobenius_admissibility_net_row_probe.py`, `frobenius_repose_probe.py`, bean
`qou-vd7j`) and is **not** explained by overflow. Do not fold the two together.

## Options

**A. Repoint the block to the mp producer + witness, keep `verified`.**
- *Means*: the citation names the non-float64 producer.
- *Costs*: one `.ts` edit.
- *Risks*: **misstates what was verified.** The mp run is a synthetic grid, not
  the AME chart; the block's stability criteria are about real nuclides. Also
  still no Z = 126.
- *Commits to*: treating a grid scan as verification of a chart-wide claim.

**B. Repoint and downgrade `status` to `partial` (or the schema's nearest),
with the coverage stated in the block's `authorNotes`.**
- *Means*: cite the sound producer, and say what it does and does not cover.
- *Costs*: one `.ts` edit plus an author note; no compute.
- *Risks*: low. Nothing numeric moves; the paper gains an accurate hedge.
- *Commits to*: nothing further — a later AME-chart mp run can restore
  `verified`.

**C. Run the mp producer over the AME2020 chart, then repoint with `verified`.**
- *Means*: actually verify the claim over the population it is about.
- *Costs*: a real compute — 3,558 nuclides at 50 dps with an LP each. The f64
  version's 3,558 rows took its own run; mpmath + clarabel per nucleus will be
  substantially slower, and Pb-208 alone reaches `nf_net ≈ -1.2e+499`. Needs the
  long-compute logging discipline and probably an overnight run.
- *Risks*: the numbers may not support the claim once Z ≥ 82 is visible — which
  is the point of running it, and is a *good* risk.
- *Commits to*: owning whatever the full chart says, including a negative.

**D. Do nothing.**
- The block keeps citing a superseded float64 producer and keeps saying
  `verified`. Nothing breaks; no number moves. The exposure is a reader
  following the citation to a witness that cannot see Z = 82.

## Default if nobody acts

**D.** Nothing changes. The block stays as it is and the superseded witness
stays in the raw-float64 backlog at 336 fields, undrainable (draining a
superseded producer is work with no consumer).

## Blast radius, in real terms

Repointing touches **one file**, `demand-stability.ts`. Nothing else reads the
superseded witness for a *number*: the other references are an audit-doc
narrative (`2026-08-02-gemini-q-saddle-offset-salvage.md` quotes the 2221/3558),
three Frobenius probes that cite it as *context* for the 0/3558, and provenance
audits that key on the path. No Lean, no other content block.

## Recommendation — my judgement, not a finding

**B.** It is the only option that makes the citation true today at no compute
cost, and it does not pre-empt C. A is actively worse than D because it swaps a
known-blind witness for a differently-blind one while keeping the word
`verified`. C is the right *eventual* answer and should be its own bean once
someone has the compute budget.

## Also recorded: I re-derived the 111/100 measurement the corpus already had

Screening this producer I found `pyhecke.gram._Q_FRAC = Fraction(111, 100)` —
the "exact in ℚ" Fraction layer is exact at **q = 1.11**, which is **1.93e-5
relative (19,295 ppb)** from the substrate pin `q₀ = 1.1099785827513808`, with
`h` off by **1.86e-4**. That is ~1.75e11× larger than the float64 resolution the
NO-FLOAT64 discipline protects.

This is **not a finding** — the corpus already holds it, in four places I should
have grepped first: `gram.py` lines 309 / 460 / 694 / 765 (*"the *approximate*
rational q = 111/100 (≈ 2e-4 from q_0)"*), a dedicated linter
`computations/lint_q_approximation.py`, and the successor's own docstring, which
states my exact figure: *"`_Q_FRAC = Fraction(111, 100)`, i.e. q = 1.11, which is
1.93e-5 relative from the canonical q_0 … Exact arithmetic over a 4-digit q is
~11 digits WORSE than the f64 it would replace."*

Recording it because the two "2e-4" and "1.93e-5" figures describe **different
quantities** and will otherwise get "corrected" into each other: 1.93e-5 is the
relative gap on **q**, 1.86e-4 is the relative gap on **h**. Both are right.

The reusable lesson is mine: I screened the producer before grepping the stem,
and spent a pass re-measuring a documented trap.

## 2026-11-15 — Owner Ruling `Q-9NNZ-1 = 1` Executed (`litlfred/qou#8048`)

- **Owner Ruling (`Q-9NNZ-1 = 1`):** Repoint `prop:demand-stability` to `all_nuclides_sdp_admissibility_mp.py` & scope the grid in `demand-stability.md`.
- **Implementation (`litlfred/qou#8048`, commit `7cc1ea945da3aafb646f31234adc81d8872b2519`):**
  1. Updated `folio/quantum-observable-universe/nuclear-interactions/demand-stability.ts` (`prop:demand-stability`) `computation` to `engine: "python+mpmath"`, `script: "computations/all_nuclides_sdp_admissibility_mp.py"`, and `witness: "computations/all-nuclides-sdp-admissibility-mp.witness.json"`.
  2. Documented in `folio/quantum-observable-universe/nuclear-interactions/demand-stability.md` the `mp` witness's synthetic magic-$Z$-dense $(Z, N)$ grid (`4,932` rows, `0` NF overflow rows, full $N \in [0, 160]$ scans at magic proton shells $Z \in \{2, 8, 20, 28, 50, 82\}$ and full $Z \in [0, 92]$ scans at magic neutron shells $N \in \{2, 8, 20, 28, 50, 82, 126\}$, with $Z = 126$ out of grid range) vs the superseded float64 AME2020 sweep (`1,337 / 3,558` NF overflow rows, `0 / 43` solvable isotopes at $Z = 82$).
- **Status:** Kept `in-progress` pending merge of `litlfred/qou#8048` and owner sign-off.
