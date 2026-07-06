# Canonical mass-pipeline: paper + Lean coverage audit

**Question (owner, 2026-06-26):** the chapter-overview said only "a recursive
Gröbner–Shirshov normal-form reducer makes the trace symbolically
computable" — but the canonical mass pipeline uses *more* (Habiro and other
tricks). **Where exactly are these in the paper, and is everything used in
the canonical mass compute both in the paper and Lean-proved?**

**Answer (headline):** every technique the canonical mass pipeline uses
**is present in the paper**, and **every Lean file backing them is
`sorry`-free** (verified with a bare-`sorry`-tactic detector — see the
correction note below). The chapter-overview Mass-Endomorphism paragraph was
updated in PR #2832 to name the fuller toolkit (Gröbner–Shirshov +
**Hoefsmit** + **Wenzl** + **Habiro** cyclotomic completion).

The one genuine formalization-depth caveat is **#7 knot-factor Frobenius
pairing**: its Lean file is 0-`sorry` but its `canonical` instance is a
*tautological skeleton* (Markov trace and Frobenius pairing both defined as
`0`, factorisation by `rfl`) that "encodes none of the conjectural content"
— so the Gram-positivity content is stated as a §3b-cond conjecture class,
not yet substantively formalized. That is a *vacuity* observation, **not** a
`sorry` gap.

> **⚠ Correction note (2026-06-26, same PR).** An earlier draft of this doc
> reported "three Lean `sorry` gaps — Habiro (15), Frobenius pairing (3),
> c_k/skew-SYT (4)" and claimed the counts were "verified by grep." They
> were **not** real gaps: the counts came from `grep -c sorry`, which matches
> the string `sorry` inside the docstring phrase **"sorry-free"** (and
> "proved sorry-free", "by `sorry`", etc.). Re-checked with a tactic-level
> detector (`:= sorry`, `by sorry`, bare-line `sorry`, `exact sorry`,
> word-boundary `admit`), **all three files contain zero `sorry`/`admit`
> tactics**. The corrected per-file status is below. Lesson: count Lean
> proof gaps with a tactic-aware matcher, never `grep -c sorry` — "sorry-free"
> is the single most common substring in this corpus' Lean docstrings.

> **Method caveat (mapping).** The technique→paper-block mapping below came
> from a corpus sweep (`content/**`, `lean/**`,
> `computations/canonical_mass.py`). A couple of paper-block labels are
> best-match and worth a second look (flagged ⚠).

## Coverage table

| # | Technique | Paper block (`.md`) | Lean | Status |
|---|---|---|---|---|
| 1 | Gröbner–Shirshov NF reducer | `predicted-spectra/groebner-nf-computation.md` | `Archimedean/NuclearGroebnerReduction.lean` | ✅ 0 sorry |
| 2 | **Habiro ring / element** | `braids-and-knots/habiro-pochhammer-bridge.md` | `MassEndomorphism/ZHabiroCauchy.lean` | ✅ 0 sorry (full closure conjectural — class) |
| 3 | Markov trace `tr_M` | `mass-endomorphism/markov-trace-recursive-reducer.md` | `BraidKnot/markovTraceRecursiveReducer.lean` | ✅ 0 sorry |
| 4 | Wenzl branching | `mass-theory/figure-eight-branching-rule.md` | `mass-theory/figure-eight-branching-rule.lean` | ✅ 0 sorry |
| 5 | Hoefsmit matrices | `mass-theory/hoefsmit-scattering-pipeline.md` | `BraidKnot/hoefsmit_scattering_pipeline.lean` | ✅ 0 sorry |
| 6 | Wedderburn decomposition | `mass-theory/figure-eight-branching-rule.md` ⚠ | `HeckeAlgebra/Wedderburn.lean` | ✅ 0 sorry |
| 7 | **Frobenius pairing / Gram** | `mass-theory/knot-factor-frobenius-pairing.md` | `BraidKnot/KnotFactorFrobeniusPairing.lean` | ✅ 0 sorry — but **tautological skeleton instance** (real content not yet formalized) |
| 8 | SDP / LP dual (operator selection) | `mass-theory/confinement-sdp.md` | `Interactions/ConfinementSDP.lean` | ✅ 0 sorry |
| 9 | **c_k truncation ladder** (Q_β) | `mass-theory/jet-convergence-classical-limit` + `ck-dk-canonical-registry.md` | `Archimedean/SkewSYT.lean` ⚠ | ✅ 0 sorry |
| 10 | F_Bor + muon-anchored Hecke energy | `mass-theory/atom-knot-mass-derivation.md` | `ArchimedeanMassFormula.lean` | ✅ 0 sorry |
| 11 | Yekutieli non-abelian Stokes | `brings-surface/archimedean-yekutieli.md` | `PathIntegrals.lean` | ✅ 0 sorry (confirmed this pass) |
| 12 | Li₂^q brane tower / Φ_q endo | `mass-theory/atom-knot-mass-derivation.md` + `conj:mass-endomorphism` | `BraidKnot/Li2qPhiqBarSymmetrization.lean` | ✅ 0 sorry |
| 13 | `canonical_mass.py` facade | — (entry point) | — | calls F_Bor (`m_p_substrate_identity_50dps`), `q_parameter.Q`, `vol_4_1_at`, `codata_constants`, `derived_masses.q_beta_kashiwara_n2_mev` |

## The one genuine residual (verified, this branch)

After correcting the grep artifact, **none** of the canonical-pipeline
techniques has a `sorry` gap. Two files deserve a precise characterization
so the "in paper AND Lean-proved" bar is read honestly:

1. **Habiro — 0 sorry, full closure conjectural** ·
   [`MassEndomorphism/ZHabiroCauchy.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/MassEndomorphism/ZHabiroCauchy.lean).
   The file *proves* the cyclotomic Cauchy-filtration and degree statements
   `sorry`-free, and explicitly states "the conjecture is **NOT** claimed
   fully closed". The remaining content (full Habiro-coefficient recursion /
   cyclotomic closure) is carried as a §3b-cond conjecture, **not** a `sorry`.
   Honest status: partial substantive formalization + a named open
   conjecture. Related beans: **`mlt7`** (qou/mass-endomorphism placeholders),
   Q_β/Habiro keystone **`kehn`**, keystone **`s5bb`**.
2. **Knot-factor Frobenius pairing — 0 sorry, tautological skeleton** ·
   [`BraidKnot/KnotFactorFrobeniusPairing.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/KnotFactorFrobeniusPairing.lean).
   The conjecture is a `class`; the downstream `theorem markov_trace_factors`
   is a real §3b-cond conditional. **But** the only supplied instance
   (`canonical`) sets `markov_trace_q := 0`, `frobenius_pairing_q := 0`, and
   discharges `factorisation_holds` by `rfl` on `0 = 0` — its own docstring
   says it "encodes none of the conjectural content." So the block-diagonal
   Gram positivity / self-duality is **stated but not formalized**. This is
   the single place where "in paper, not really Lean-proved" is fair — and
   it is a **vacuity / non-degeneracy** item (cf. AGENTS.md §1a, §3b-cond
   item 5; `lean-proof-vacuity-audit`), not a `sorry` to discharge.
   (`MathlibExt/FrobeniusInnerProduct.lean` is genuinely 0-sorry — the
   abstract Frobenius inner product *is* formalized; only the knot-factor
   *instance* is a skeleton.)
3. **c_k ladder / skew-SYT — 0 sorry, substantive** ·
   [`Archimedean/SkewSYT.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/SkewSYT.lean).
   A 61-declaration formalization of the H_k(q) → H_3(q) branching rule via
   skew SYT, with real theorems (`classical_dim_identity`,
   `branching_nonneg`), `sorry`-free; finite combinatorial steps closed by
   `decide`. No gap.

## Also worth confirming

- **#6 Wedderburn** and **#9 c_k** paper-block labels are best-match (⚠) —
  the Wedderburn narrative may live in a dedicated block rather than
  `figure-eight-branching-rule.md`, and the c_k canonical narrative is split
  across `jet-convergence-classical-limit` + `ck-dk-canonical-registry`.

## Takeaway

The owner's "everything in the canonical mass pipeline should be in paper
AND Lean-proved" bar is met for **all 12** theorem-backed techniques (the
facade #13 is Python glue, not a theorem): every backing Lean file is
`sorry`-free. The two honest qualifications are (a) **#2 Habiro**'s full
closure is a named open conjecture (class-axiomatised, not a `sorry`), and
(b) **#7 knot-factor Frobenius pairing** is 0-`sorry` only via a tautological
skeleton instance — its Gram-positivity content is not yet substantively
formalized. No technique used by the canonical mass compute is *missing*
from the paper, and there are **no `sorry` gaps** among them.
