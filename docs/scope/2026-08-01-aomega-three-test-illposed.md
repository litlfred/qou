# qou-l15q: the 4₁→5₂ test for "why 3" is ill-posed as designed — rank 2 vs rank 3

**Date:** 2026-08-01 · **Bean:** `qou-l15q` (arc successor to `qou-bbsy`) · **Tier:** scope correction, pre-compute.
**No probe was run. Nothing fitted, nothing wired.** This note exists because reading
the corpus before computing (AGENTS.md §anti-guessing) invalidated the test design.

## The design that failed

#4447 certified that `A_ω = 3` is the **Stokes structure constant** of 4₁:

$$
S^+_{12}(q) + S^+_{21}(q) = 3\,S^+_{11}(q)
$$

exact as an integer q-series (GGM 2012.00062 symmetry eq 65), Lean-formalized in
[`StokesSymmetryConstant.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstant.lean).
Bean `qou-l15q` proposed deciding **why 3** by computing the analogous constant `c`
for 5₂, since two structural candidates split sharply there:

| candidate | 4₁ | 5₂ prediction |
|---|---|---|
| (A) \|disc(trace field)\| | \|−3\| = 3 ✓ | **23** |
| (B) \|Alexander middle coeff\| | \|+3\| = 3 ✓ | **3** |

## Why it does not work

The corpus already carries the 5₂ Stokes machinery
([`qbeta_5two_stokes_barodd_index_probe.py`](../../computations/probes/qbeta_5two_stokes_barodd_index_probe.py),
GGM §6 eqs 24–29, 100a/b, 102, 112–124). Reading it:

| knot | Stokes matrix | q→0 limit | off-diagonal integers |
|---|---|---|---|
| 4₁ | **2×2** | `[[1,3],[0,1]]` (eq 60) | **one**: 3 |
| 5₂ | **3×3** | `[[1,4,0],[0,1,0],[−3,−9,1]]` (eq 100a) | **three**: 4, −3, −9 |

The rank is the number of flat connections, which tracks the degree of the trace
field (4₁: quadratic, `ℚ(√−3)`; 5₂: cubic, disc −23). So:

1. **There is no single "the 5₂ Stokes constant"** to compare against 23 or 3.
   The test presupposed a scalar that does not exist at rank 3.
2. **The symmetry eq (65) is a rank-2 statement.** It has no 3×3 analogue in GGM;
   the structural relation they give for 5₂ is the *inversion* relation
   `S⁺(q)ᵀ·S⁻(q) = 1` (Conjecture 1(b), eq 4), which constrains a matrix pair and
   does not isolate an integer.

## What the 5₂ integers do and do not say

- **23 does not appear** among {4, −3, −9}. That is *not* a clean refutation of
  candidate A, because the quantity A predicts (a single Stokes constant) is not
  defined here — one cannot refute a prediction the test cannot evaluate.
- **3 does appear**, as `|−3|` (the (3,1) entry). This is **not evidence for
  candidate B.** Selecting one of three off-diagonal integers *post hoc* because it
  matches is precisely the numerology this repo forbids (AGENTS.md §anti-fit). With
  three integers available, hitting any given small number is unremarkable.
- Likewise, combinations that reach 23 (e.g. `3·9 − 4`) are **not** recorded as
  findings. Free choice of combining rule over three integers can reach almost any
  target; a rule must be *derived* before its output counts.

**Both candidates therefore remain untested, not decided.** No support and no
refutation for either.

## What a well-posed test needs

Before any 5₂ number can adjudicate "why 3", one must first fix **which Stokes
datum plays the `A_ω` role at rank > 2** — a derivation, not a choice. That is the
same channel-identification gap #4447 recorded on the 4₁ side (`A_ω` is σ₁σ₂ while
the proven x-refinement is σ₁σ₁, and the σ₁σ₂ x-refinement is absent from the
literature). Concretely, one of:

1. **Derive the role from the T5 channel.** `A_ω` enters as
   `S_K = A_ω·κ·(ln²q₀ − ϑ_K²)`; deriving which matrix element that coefficient is
   would fix the rank-3 generalization by construction rather than by pattern.
2. **Find a rank-general symmetry.** If GGM's eq (65) is the rank-2 shadow of a
   general relation, its rank-3 form would supply the constant. The inversion
   relation is the candidate to interrogate.
3. **Test candidate A on another rank-2 knot instead** — a knot whose trace field
   is quadratic, where "the" Stokes constant is well-defined exactly as for 4₁, and
   where |disc| ≠ |Alexander middle coefficient| so the candidates still separate.
   This is the cheapest well-posed route and does not require solving (1) or (2).

Route 3 is the recommended next step: it keeps the original falsifiable structure
and only changes the test knot to one where the question is meaningful.

## Cross-references

- Bean `qou-l15q` (re-scoped by this note); predecessor `qou-bbsy` (#4447).
- [`2026-08-01-3bp8-entirety-and-channel-correctness.md`](../audits/2026-08-01-3bp8-entirety-and-channel-correctness.md) §2 (the channel gap), §4 (the structure constant).
- AGENTS.md §"Before declaring refuted" (why this is *untested*, not refuted);
  §"Axiomatization is NOT a Proof"; §anti-fit.
