# Eigenfunction relation → weight kernel: the link is ring-class, and wₙ(K) does not close by fit

**Date:** 2026-07-11
**Branch:** `claude/q-stokes-kernel-eigenfunction-y0pso2`
**PR:** [#3545](https://github.com/litlfred/qou/pull/3545)
**Lean:** [`QOU/Mass/BindingEigenfunctionTwoTier.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingEigenfunctionTwoTier.lean)
**Probes:** [`computations/binding_wn_derive_or_refute.py`](../../computations/binding_wn_derive_or_refute.py)
**Builds on:** [2026-06-27 lever1 cyclotomic kernel](2026-06-27-lever1-qinvolution-cyclotomic-kernel.md),
[2026-06-26 q-involution/q-Hermite id](2026-06-26-binding-period-qinvolution-qhermite-identification.md),
[2026-07-03 θ_λ Reeb/na-Stokes jet filtration](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md)

## The question

Does the na-Stokes binding period's **eigenfunction relation** inform the open
**weight kernel** `wₙ(K)` of `conj:binding-manybody-eq-jet-filtration`
(`B(K) = Σ_{n=2}^{A} mₑ·a_D^(n)·wₙ(K)`, `wₙ` the output of a q-difference
recursion `G(qx;q)=R(q,x)G(x;q)`)? And can `wₙ(K)` be closed now?

The na-Stokes period is `a_D^(n)=S(n)/n`, `S(n)=Σ_{λ⊢n} dim_q(λ)` (q-involution
number; `q→1` → involution/telephone numbers, A000085). Its eigenfunction
relation is the monic three-term recurrence `S(n)=S(n−1)+c_n·S(n−2)`,
`c_n:=(S(n)−S(n−1))/S(n−2)`.

## Part 1 — the two-tier eigenfunction structure (Lean-certified)

Exact symbolic + 50-dps numerics (`c_n/[n−1]_q` at the muon-canonical q₀):

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `c_n/[n−1]_q` | 1.000000 | 1.000000 | 1.005390 | 1.016141 | 1.030051 | 1.049498 | **1.071963** |

- **Tier 1 (seed).** `c₂=[1]_q=1`, **`c₃=[2]_q` exact** (`c3_eq_qbr2`, sorry-free).
  From the q-hook closed forms `S(1)=1, S(2)=2, S(3)=2+[2]_q`.
- **Tier 2 (tail).** First deviation `q²·D(4)=(q−1)²·Φ₃` (`D4_habiro_factor`),
  `D(n):=S(n)−(S(n−1)+[n−1]_q S(n−2))`. Universal `(q−1)²` double root +
  cyclotomic leading factor — the Habiro-ring signature.

### Adversarial re-scoping (STRICT — these are in the Lean docstring)

1. **`[n−1]_q` is 2 points, not a pattern.** `c_n−[n−1]_q` is exactly 0 only at
   `n=2,3`; nonzero from `n=4`. `c₂` is near-trivial, so `c₃=[2]_q` is the single
   nontrivial seed coincidence.
2. **"Habiro" = leading-factor only.** `(q−1)²` universal ✓, leading factors
   cyclotomic (Φ₃/Φ₅/Φ₆/Φ₇), but `D(6),D(7),D(8)` carry **non-cyclotomic**
   cofactors (exact factorizations in the probe). "Habiro-class" is a
   ring-membership claim about leading structure, not a purely-cyclotomic claim.
3. **The fork (decisive).** `S(n)` does **not** obey the clean Rogers–Szegő
   recurrence `μ(n)=μ(n−1)+[n−1]_q μ(n−2)`; it forks from the crossing moment
   `μ_q` — **+0.3 % at n=4 → +7.9 % at n=8**. `q→1` limits agree (both `=I(n)`);
   `q₀`-values do not. The clean q-Hermite / **q-Fourier eigenbasis is `μ_q`'s**,
   not `S(n)`'s, and `μ_q` was owner-dropped 2026-06-26 (collapses past ⁴He).

## Part 2 — how the eigenfunction relation informs the weight kernel: (a) ring-class, not determination

The earlier framing "the na-Stokes recurrence supplies `R(q,x)`'s backbone /
is a consistency condition on `R`" is **overstated**. Corrected scope, matching
the [2026-06-27 audit's own caveat](2026-06-27-lever1-qinvolution-cyclotomic-kernel.md)
("not a claim that the towers are the same element"):

- **(a) scope-limited positive.** The binding deviation `D(m)` and the Q_β `c_k`
  ladder both (i) resist low-order q-holonomic closure and (ii) carry cyclotomic
  Habiro structure — corroboration at the **ring** level (both in the
  cyclotomic-completion / Habiro ring).
- **NOT (b).** They are **different localizations** (binding `D(m)`: real-q `ℤ[q]`;
  Q_β `c_k`: `ζ₄`-fibre / complex, leading `√2·Φ₂`). Same ring, **not** the same
  element. The eigenfunction relation gives `wₙ(K)`/`R(q,x)` a *derived target*
  (the `D(m)` tower) to reproduce — it does **not** determine `R`.

This also answers **"the c_k Habiro w/ recursion rules"**: yes, `kehn`'s Q_β `c_k`
Habiro element is the recursion-rule object — but it is a *different localization*,
and fitting its Φ₂ is the explicitly-forbidden "seventh ansatz". It cannot be
borrowed to close the binding weight by fitting.

## Part 3 — can `wₙ(K)` close now? Derive-or-refute (no fit)

AME2020 anchors D/T/³He/⁴He, `a_D^(n)=S(n)/n`, `mₑ=0.51099895` MeV.

> **CORRECTION (2026-07-11, after coordination with [#3534](https://github.com/litlfred/qou/pull/3534)).**
> An earlier version of this section declared K-independent (body-order) weights
> **structurally excluded (b)** from the *raw* AME split `B(T)=8.48 ≠ B(³He)=7.72`
> (9.9 %). **That was an over-claim** (the exact refuted-discipline trap): the raw
> split is almost entirely **Coulomb**, a separable known effect. #3534
> Coulomb-corrects to the strong binding `B_strong` and finds ³H/³He agree to
> **2.73 %** (charge-symmetry breaking); an independent estimate here
> (`E_C(³He) = ⅗·Z(Z−1)·e²/(4πε₀R) ≈ 0.8–1.0 MeV`) restores the mirror pair to
> within ~1–3 %. **So a K-independent body-order `wₙ` IS admissible.** The (b)
> claim is **re-scoped to (a)** below; the raw numbers stand, only the scope was
> wrong.

**(a) Ad-hoc constant-ratio kernels do not close (scope-a).** On the
Coulomb-corrected `B_strong`, body-order weights `w₂,w₃,w₄` are admissible and
extractable (#3534: `4.353, 9.331, 15.919`, ratios 2.143/1.706, no fit). But no
parameter-free *constant-ratio* kernel `R(q,n)` reproduces them to 5 %: geometric
22.7 %, `[n]_q` 29.4 %, `a_D` self-ratio 37.6 %, `∝n` 30.0 %, `[n]_q²` 6.9 %
(lone near-miss) — #3534 Part (i). A tuned recursion is the banned 7th Δ_λ ansatz.

**Underdetermination of a general K-dependent kernel.** With `wₙ(K)` fully
K-dependent, each isotope contributes `A−1` unknowns (`w₂..w_A`) against **1**
equation `B(K)`. Inverting the anchors for a per-isotope `wₙ` is a **fit** — the
forbidden move (Δ_λ gate, "no seventh fit-based ansatz"). Body-order admissibility
(above) is the *constrained* case (`wₙ` shared across K); even there the closed
form is open.

**Verdict.** `wₙ(K)` does **not** close now. Body-order weights are admissible on
`B_strong`, but no derived constant-ratio kernel reaches 5 % and a tuned one is
banned; closure needs a *derived* `R(q,x)` (the open q-difference kernel /
owner-gated s5-so3 keystone), so any `wₙ` from the anchors is a fit and cannot
honestly improve binding. The **non-fit** routes are (i) expansion in the
**q-Hermite basis** the eigenfunction relation identifies (#3534 Part ii — but see
the fork caveat in Part 1: `S(n)` is not the clean RS moment, so this is the
Habiro-dressed basis, not clean q-Hermite) and (ii) Option-1 of the
[2026-07-03 audit](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md):
`wₙ(K) =` hyperbolic link-volume of the n-body sub-cluster (a topological
invariant) — both untested, both non-fit.

## Consequence for `conj:binding-manybody-eq-jet-filtration`

**Not provable now** (recorded answer). The conjecture's three deep inputs remain
open: (1) the super-exponential `a_D^(n)` magnitude, (2) the na-Stokes identity
`a_D^(n)=lw(n−1)` (owner-gated keystone #1765), and (3) the weight `wₙ(K)`. This
work sharpens (3): body-order weights are *admissible* on the Coulomb-corrected
`B_strong` (#3534), but no derived constant-ratio kernel reaches 5 % and a tuned
one is a banned ansatz — closure needs the derived `R(q,x)`.
`prop:jet-filtration-binding-extensive` (the *qualitative* extensivity) stays the
proved core; the *quantitative* closure is unchanged (open).

## Reproduce

```bash
python3 computations/binding_wn_derive_or_refute.py
```

EXPLORATORY — no production wiring, no fitted constant. Anti-laundering: the Lean
file certifies the two-tier *algebra*; it does not improve any mass/binding number.
