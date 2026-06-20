# Q_β Wenzl-Habiro keystone ansatz — NEGATIVE

**Date:** 2026-06-01
**Branch:** `claude/qbeta-wenzl-habiro-keystone-2026-06-01`
**Probe script:** [`computations/probes/qbeta_wenzl_habiro_ansatz_probe.py`](../../computations/probes/qbeta_wenzl_habiro_ansatz_probe.py)
**Witness:** [`computations/probes/qbeta-wenzl-habiro-ansatz-probe.witness.json`](../../computations/probes/qbeta-wenzl-habiro-ansatz-probe.witness.json)
**Master ledger:** [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
**Status:** **NEGATIVE** — no cyclotomic Wenzl factor `W(u)` × pair-specific `D(u)` ansatz reproduces both `c_2 = −1` (Taylor-exact, PROVED) AND `c_3 = −2.0693…` (cal-anchored) as a clean structural identity.

---

## TL;DR

This probe tested the hypothesis
   `Q_β-Habiro(u) = W(u) · D(u)`
where `W(u)` is a Wenzl-style cyclotomic factor encoding the level-2
SU(2) annihilator at q = ζ_8 (PR #1625 categorical witness) and
`D(u)` is a pair-specific Δ from (p, n). The acceptance criterion
was: **does D(u) collapse to a clean closed form (constant or
low-degree polynomial) when c_2, c_3 are matched exactly?**

Across 9 cyclotomic / Pochhammer-ratio surrogate W(u) candidates,
**0 produce a pure-constant D(u)**, and the 1 "DEGREE_1_D" match
(W = −u²) is trivial: it simply re-encodes `c_2 = −1` and the
empirical `c_3 = −2.0693…` as the first two Taylor coefficients of
D — i.e. it is a refactoring, not a structural derivation.

For every Wenzl-shaped W(u) with W(0) = 1 (W1, W3, W4, W5, W7, W9
in the probe), the Taylor structure forces D to begin
`d_0 = d_1 = 0, d_2 = c_2 = −1, d_3 = c_3 = −2.0693…` — meaning
the Wenzl factor leaves c_2 and c_3 entirely absorbed by D's
Taylor expansion. The categorical content of W is not engaged at
the c_2 / c_3 level.

**This is the expected outcome given PR #1625's framing**: the
ζ_8 cancellation acts via **Wenzl-annihilator-forced linear
relations on the Markov-trace decomposition** for *atomic-step
pair-differences* (D−n, ³He−D, ⁴He−³He), NOT as a multiplicative
prefactor of the single-particle Q_β Habiro element. The probe
formally tests, and rules out, the multiplicative-prefactor
reframing.

---

## Retracted secondary observation — c_4..c_7 = 0 was a fitting tautology

> **2026-06-01 correction (post-Gemini review).** An earlier
> version of this audit reported "c_4..c_7 below CODATA
> resolution" as a *surprise finding*. That claim is
> **WITHDRAWN**. The recursive extraction loop
> (formerly `extract_higher_c_k`) used the update
> `Q_prev ← Q_prev · (1 + c_k · u^k)` with
> `c_k = (Q_codata/Q_prev − 1) / u^k`. After substitution
> `1 + c_k·u^k = Q_codata/Q_prev`, hence
> `Q_prev ← Q_prev · (Q_codata/Q_prev) = Q_codata` **exactly**
> after iteration `k = 3`. All subsequent iterations
> have `ratio_m1 = 0`, mechanically forcing
> `c_4 = c_5 = c_6 = c_7 = 0` **regardless of Q_β experimental
> precision**. This is a tautological single-point fit, not
> a precision-floor observation. Code removed; cache rebuilt
> with c_2 and c_3 only.

The bug invalidated the "secondary observation" but does not
change the structural fact that *Q_β experimental precision
does not constrain c_k for k ≥ 4* — it just doesn't constrain
them to **0**; it simply doesn't constrain them at all. The
correct framing:

- **c_2 = −1**: Lean-proved Taylor-exact (independent of any
  cal anchor)
- **c_3 = −2.0693…**: measured at canonical q_0 from `Q_codata`
  + the proved c_2 (8-digit precision)
- **c_4, c_5, …**: unconstrained by current Q_β experimental
  precision

**Implication for the 1ppQ Q_β goal** (unchanged from the
retracted observation): the actual keystone is a structural
derivation of `c_3` from `q_0` algebraically, not extending the
precision ladder. The eigenphase/scaling map direction (per
`docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`
ε-order analysis: c_3 lives at u³ = ε⁶ while the per-block −2
lives at √u = ε¹, so the "match" is structurally cross-order,
not a value identity — the missing piece is a 5-ε-order
eigenphase rescaling) remains the right next move.

---

## Results table

| W(u) candidate | Leading order | D(u) structure | Verdict |
|---|---|---|---|
| W1: `(1−u^8)/(1−u^4)^2` | u⁰ | generic Taylor, d_0=d_1=0, d_2=-1, d_3=c_3_emp | absorbed |
| W3: `(u^4+1)/(u^2+1)` (Φ_8/Φ_4) | u⁰ | generic Taylor | absorbed |
| W4: `(u^4+1)^2` (Φ_8²) | u⁰ | generic Taylor | absorbed |
| W5: `u^4+1` (Φ_8) | u⁰ | generic Taylor | absorbed |
| W6: `u(u²+1)(u⁴+1)` | u¹ | generic shift | absorbed |
| W7: `(1−u^4)/(u^4+1)` | u⁰ | generic Taylor | absorbed |
| W8: `−u²` | u² | DEGREE_1: D = 1 + c_3_emp·u | **trivial refactor** |
| W9: `1 − u²` | u⁰ | generic Taylor | absorbed |
| W10: `(1−u)(1−u²)` (Poch_2) | u⁰ | generic | absorbed |

**No PURE_CONSTANT_D match.** W8 = -u² is the only DEGREE_1_D, but
it is trivially the statement "factor out u² and let D = 1 + (c_3
empirical) · u + ..." — i.e. a coordinate change, not a structural
identity.

---

## Why this falsifies the multiplicative-prefactor reframing

The PR #1625 categorical witness (`docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`)
identifies the Wenzl annihilator at q = ζ_8 as the source of the
universal Φ_8 cancellation in *atomic-step Habiro pair-differences*
`Δa_m(X − Y)`. Specifically:

`S_6(ζ_8) + Δa_7(ζ_8) · 8 = 0`  for all atomic-step pairs (D−n,
³He−D, ⁴He−³He), and the categorical content is the Wenzl-forced
linear relation `Σ_{λ: first-col ≥ 4} y_λ(ζ_8) · χ^λ(β_K; ζ_8) = 0`
on the Markov-trace decomposition.

This is **a relation on PAIR-DIFFERENCES of full Habiro elements**,
not a multiplicative prefactor on individual Habiro elements. The
Wenzl factor's contribution to a single nucleon's Habiro element
`Σ_m a_m(p)·(u;u)_m` is invisible at the Markov-trace level — it
shows up only when one computes the **difference** of two nucleon
Habiro coefficient sequences.

Hence the Q_β-Habiro element — which is *not* a pair-difference but
a single-particle β-decay amplitude — receives NO direct Wenzl
factor. The ansatz `Q_β-Habiro = W · D` is structurally misaligned
with the actual location of Wenzl content in the canonical chain.

---

## Structural narrowing for next session

What the probe DOES NOT rule out, and what should be attempted
next:

1. **The Wenzl factor acts on `Δ Q_β` between (p) and (n).** If we
   define `Δ Q_β = Q_β(n) − Q_β(p)` or similar pair-difference,
   the Wenzl annihilator may produce a structural identity in the
   pair-difference. But Q_β is a single observable (the n → p β-
   decay width), so pair-differencing here is not a natural
   operation — this direction is unlikely.

2. **The eigenphase/scaling map f.** Per the ε-order audit
   (`docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`):
   per-block `Δtr_M` contributions are O(√u) (ε¹, leading -2/-1/-2)
   while ladder c_3 is at O(u³) (ε⁶). The 5-ε-order gap means the
   "missing piece" is a SCALING MAP `f: Δtr_M(√u) ↦ Q_β(u³)`, NOT
   a value identity for c_3. The map `f` should be derived from
   the canonical chain's Archimedean functor τ.

3. **CAL-3 elevation.** If Q_β is treated as a calibration anchor
   (CAL-3, alongside CAL-1 = m_e and CAL-2 = pion mass), then the
   "1ppQ Q_β" goal as currently framed is a category mistake —
   CAL anchors are *inputs*, not predictions. The current 3-CAL
   discipline (m_e, Q_β, m_π) has Q_β as CAL-2, NOT a prediction.
   Per AGENTS.md `## Precision goals`, Q_β's L2 target (≤ 7.8 ppb)
   currently misses by 1279 ppb (164× miss), and **the cleanest
   path is to declare Q_β not a prediction at all but a
   calibration constant** — at which point N=7 / 1ppQ becomes a
   downstream m_n / Δ_pn question, not a Q_β question.

4. **Habiro recursion from `α_EM = [2]_q · (1−h²α)`.** PR #1511's
   α_EM closure is parallel to the Q_β closure target. Its
   structure is `[2]_q · (1 − h²α)`. A direct analog for Q_β
   would be `[2]_q · F(h, q_0)` for some categorical F — this is
   what the probe should test next.

---

## Symbolic verification of c_2 = -1 (algebraic, not numerical)

The probe DOES algebraically verify that `c_2 = −1` is reproduced
exactly by every candidate W via D's Taylor expansion, but with the
caveat that this is trivially true: the Taylor matching is forced
by linear algebra, not by the structure of W. The Lean-proved
status of c_2 = −1 (from `QOU.BraidKnot.N2_factor`) holds
independently.

The probe records:
- Empirical Q_codata is published to 8 digits, so c_3 is extracted
  to ~10⁻⁶ precision and c_4..c_7 are not extractable at all.
- W6 (= u(u²+1)(u⁴+1), leading order u¹) gives a generic D with
  d_1 = c_2 = −1 (shifted index) but d_2 = c_3_emp, again absorbed.
- The unique "DEGREE_1_D" (W8 = −u²) is a coordinate change, not
  a derivation.

---

## What "POSITIVE" would have looked like

For the ansatz to have closed Q_β-Habiro structurally, the probe
would need to find SOME W(u) (preferably the Pochhammer ratio W1
or the cyclotomic Φ_8/Φ_4 W3) for which D(u) collapses to:

- **D(u) = constant** (PURE_CONSTANT_D): "Q_β-Habiro = W(u) · d_0"
  — the entire ladder fixed by W alone.
- **D(u) = constant + d_1·u** (DEGREE_1_D with d_0 ≠ 0): "Q_β-Habiro
  = W(u) · (d_0 + d_1·u)" — c_4+ fixed by W alone, c_3 by d_1.

In either case, c_4 through c_7 would be **predicted** by the
Wenzl factor's Taylor expansion, not extracted from Q_codata
recursively. This would be the 1ppQ keystone.

The probe shows that no such W exists in the cyclotomic /
Pochhammer-ratio surrogate space.

---

## Pushed commit SHA

See top of `docs/coordination/1ppq-qbeta.md` for the canonical
ledger pointer once this branch is pushed.

## Cross-references

- PR #1625 ζ_8 categorical witness: [Level-2 SU(2) Wenzl identification](2026-06-01-qbeta-habiro-zeta8-categorical-witness.md)
- Universal M=7 boundary: [Δa_m partial-sum scan](2026-06-01-qbeta-habiro-delta-am-partial-sum-scan.md)
- All-10-pairs Φ_8 proton-conditional: [10-pair universality](2026-06-01-qbeta-habiro-all-10-pairs-phi8-universality.md)
- Wenzl tower FALSIFIED: [ζ_n tower probe](2026-06-01-qbeta-habiro-wenzl-tower-zeta-n.md)
- ε-order audit (c_3 accidental coincidence): [order audit](2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md)
- Cal-anchored vs derived tier discipline: [c_3 q_0-stability verdict](2026-05-31-qbeta-c3-q0-stability-verdict.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
