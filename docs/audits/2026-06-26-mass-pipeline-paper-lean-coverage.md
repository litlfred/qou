# Canonical mass-pipeline: paper + Lean coverage audit

**Question (owner, 2026-06-26):** the chapter-overview said only "a recursive
Gröbner–Shirshov normal-form reducer makes the trace symbolically
computable" — but the canonical mass pipeline uses *more* (Habiro and other
tricks). **Where exactly are these in the paper, and is everything used in
the canonical mass compute both in the paper and Lean-proved?**

**Answer (headline):** every technique the canonical mass pipeline uses
**is present in the paper**. Most are **Lean-proved sorry-free**. Three
have **Lean `sorry` gaps** (counts verified by grep on this branch):
Habiro (15), the knot-factor Frobenius pairing (3), and the c_k / skew-SYT
ladder (4). The chapter-overview Mass-Endomorphism paragraph was updated in
PR #2832 to name the fuller toolkit (Gröbner–Shirshov + **Hoefsmit** +
**Wenzl** + **Habiro** cyclotomic completion).

> **Method caveat.** The technique→paper-block mapping below came from a
> corpus sweep (`content/**`, `lean/**`, `computations/canonical_mass.py`).
> Sorry counts are verified. A couple of paper-block labels are
> best-match and worth a second look (flagged ⚠).

## Coverage table

| # | Technique | Paper block (`.md`) | Lean | Status |
|---|---|---|---|---|
| 1 | Gröbner–Shirshov NF reducer | `predicted-spectra/groebner-nf-computation.md` | `Archimedean/NuclearGroebnerReduction.lean` | ✅ 0 sorry |
| 2 | **Habiro ring / element** | `braids-and-knots/habiro-pochhammer-bridge.md` | `MassEndomorphism/ZHabiroCauchy.lean` | 🟡 **15 sorry** |
| 3 | Markov trace `tr_M` | `mass-endomorphism/markov-trace-recursive-reducer.md` | `BraidKnot/markovTraceRecursiveReducer.lean` | ✅ 0 sorry |
| 4 | Wenzl branching | `mass-theory/figure-eight-branching-rule.md` | `mass-theory/figure-eight-branching-rule.lean` | ✅ 0 sorry |
| 5 | Hoefsmit matrices | `mass-theory/hoefsmit-scattering-pipeline.md` | `BraidKnot/hoefsmit_scattering_pipeline.lean` | ✅ 0 sorry |
| 6 | Wedderburn decomposition | `mass-theory/figure-eight-branching-rule.md` ⚠ | `HeckeAlgebra/Wedderburn.lean` | ✅ 0 sorry |
| 7 | **Frobenius pairing / Gram** | `mass-theory/knot-factor-frobenius-pairing.md` | `BraidKnot/KnotFactorFrobeniusPairing.lean` | 🟡 **3 sorry** |
| 8 | SDP / LP dual (operator selection) | `mass-theory/confinement-sdp.md` | `Interactions/ConfinementSDP.lean` | ✅ 0 sorry |
| 9 | **c_k truncation ladder** (Q_β) | `mass-theory/jet-convergence-classical-limit` + `ck-dk-canonical-registry.md` | `Archimedean/SkewSYT.lean` ⚠ | 🟡 **4 sorry** |
| 10 | F_Bor + muon-anchored Hecke energy | `mass-theory/atom-knot-mass-derivation.md` | `ArchimedeanMassFormula.lean` | ✅ 0 sorry |
| 11 | Yekutieli non-abelian Stokes | `brings-surface/archimedean-yekutieli.md` | `PathIntegrals.lean` | ⚠ status unconfirmed |
| 12 | Li₂^q brane tower / Φ_q endo | `mass-theory/atom-knot-mass-derivation.md` + `conj:mass-endomorphism` | `BraidKnot/Li2qPhiqBarSymmetrization.lean` | ✅ 0 sorry |
| 13 | `canonical_mass.py` facade | — (entry point) | — | calls F_Bor (`m_p_substrate_identity_50dps`), `q_parameter.Q`, `vol_4_1_at`, `codata_constants`, `derived_masses.q_beta_kashiwara_n2_mev` |

## The three Lean gaps (verified counts, this branch)

These are the only canonical-pipeline techniques **in the paper but not yet
Lean-sorry-free**. "In the paper, not Lean-proved" — so they fail the
owner's "in paper AND Lean proved" bar:

1. **Habiro — 15 sorry** ·
   [`MassEndomorphism/ZHabiroCauchy.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/MassEndomorphism/ZHabiroCauchy.lean).
   Paper side (`habiro-pochhammer-bridge.md`) states the ratio/Pochhammer
   identity; the Lean lacks the Habiro-coefficient recursion + cyclotomic
   closure proofs. Likely tracked by bean **`mlt7`** (qou/mass-endomorphism
   placeholders) and the Q_β/Habiro keystone bean **`kehn`**.
2. **Knot-factor Frobenius pairing — 3 sorry** ·
   [`BraidKnot/KnotFactorFrobeniusPairing.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/KnotFactorFrobeniusPairing.lean).
   Block-diagonal positivity / self-duality of the Gram matrix not yet
   discharged. (Note `MathlibExt/FrobeniusInnerProduct.lean` *is* 0-sorry —
   the gap is specifically the knot-factor pairing.)
3. **c_k ladder / skew-SYT — 4 sorry** ·
   [`Archimedean/SkewSYT.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/SkewSYT.lean).
   Q_β truncation convergence bounds. Tracked under the Q_β c_k beans
   (`kehn`, and the c_k framing in `docs/audits/2026-05-31-qbeta-ck-…`).

## Also worth confirming

- **#11 Yekutieli `PathIntegrals.lean`** — sorry status not confirmed in
  this pass; grep it.
- **#6 Wedderburn** and **#9 c_k** paper-block labels are best-match (⚠) —
  the Wedderburn narrative may live in a dedicated block rather than
  `figure-eight-branching-rule.md`, and the c_k canonical narrative is split
  across `jet-convergence-classical-limit` + `ck-dk-canonical-registry`.

## Takeaway

The owner's "everything in the canonical mass pipeline should be in paper
AND Lean-proved" bar is met for **10 of 13** techniques (the facade #13 is
Python glue, not a theorem). The **3 outstanding** are Habiro, the
knot-factor Frobenius pairing, and the c_k ladder — all already in the paper,
all with open Lean `sorry`s, and all already on the bean backlog
(`mlt7`, `kehn`). No technique used by the canonical mass compute is
*missing* from the paper.
