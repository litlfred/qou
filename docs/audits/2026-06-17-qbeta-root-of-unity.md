# Q_β c_k ladder — root-of-unity / Ohtsuki–Habiro element of the FORCED knot (4₁ / Hopf): NEGATIVE

**Date:** 2026-06-17
**Branch / PR:** `claude/qbeta-root-of-unity-2026-06-17`
**Probe:** [`computations/probes/qbeta_root_of_unity_probe.py`](../../computations/probes/qbeta_root_of_unity_probe.py)
**Witness:** [`computations/probes/qbeta-root-of-unity.witness.json`](../../computations/probes/qbeta-root-of-unity.witness.json)
**Discipline:** STRUCTURAL only, ANTI-FITTING. No c_k value is claimed or wired.
The four-session flip-flop guard
([`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md))
is respected.

> **⮕ Registry impact:** confirms §3 line "a genuine c_3 Habiro element, if it
> exists, must be complex-analytic / root-of-unity, not a real-q formula." This
> audit closes the *complex / root-of-unity* lead **for the forced candidates** —
> the only candidates the anti-fitting discipline admits. c_3 stays EMPIRICAL.

## The question (the ONE surviving Q_β lead)

The real-q / cyclotomically-localised class is REFUTED
([`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md);
real-q probe PR #2452): empirical `c_3` swings **−2.88 %** between the proton
and muon anchors (`dc_3/dq ≈ 4.6×10⁶`), so no smooth real `f(q)` can track it.
Per AGENTS.md §"Im(q) at fibre vs observable level", the only surviving form is
a **fibre-level, complex-analytic / root-of-unity** element `F(q)` whose
archimedean evaluation at each q₀ anchor reproduces `c_3` at *that* anchor.

This probe asks the sharpened version: **is the c_k ladder the root-of-unity /
Ohtsuki–Habiro invariant of a substrate-FORCED knot?**

## The anti-fitting discipline (the whole point)

Independent c_k data points are few: `c_2 = −1` (canonical, Lean-proved,
Taylor-exact) and `c_3 ≈ −2.0693` (empirical); `c_4..c_10` are polynomials in
`c_3` and `b²`. Matching a knot invariant to `c_2, c_3` is meaningful **only**
if the knot and root of unity are FORCED by the framework with **zero free
choices**. Exactly two forced candidates exist:

| candidate | why it is forced |
|---|---|
| **figure-eight 4₁** | q₀ is fixed by `Vol(4₁) = 2Λ(π/3) ≈ 2.02988`; the Kashaev/volume knot |
| **Hopf link** | the canonical registry hint `c_3 = −2 = J_Hopf(q=1)` |

Trefoil 3₁ (non-hyperbolic, `D(z)=0`) is a CONTROL. **No knot/root-of-unity
scan is performed** — a scan to "find a match" would itself be a fit, and the
answer would be NEGATIVE by construction.

## What the probe computes (all formulas literature-verified)

The genuine quantum invariants of each forced candidate, each verified against
a published value **before** any comparison:

| check | result |
|---|---|
| `J_{4₁}(N=1; q₀) = 1` (Habiro/G-L unknot normalisation) | PASS |
| `J_{4₁}(N=2; t) = V_{4₁}(t)` Jones polynomial (G-L convention, q=t) | PASS |
| Kashaev growth → `Vol(4₁)`: `(2π/N)(log\|⟨4₁⟩_N\| − (3/2)log N) → 2.02988` | PASS (0.42 %→0.21 %→0.11 % for N=200,400,800) |
| `V_Hopf(t=1) = −2` (the registry hint) | PASS |
| `V_K(t=1) = 1` (trefoil control) | PASS |

The figure-eight colored Jones uses the Garoufalidis–Le cyclotomic form
`J_{4₁}(N;q) = Σ_{n=0}^{N−1} q^{−nN} ∏_{j=1}^{n} (1−q^{N−j})(1−q^{N+j})`, which
reproduces `V_{4₁}` exactly at N=2 (the N^{3/2}/√3 volume-conjecture prefactor
is included in the growth check).

## Result — parameter-free comparison to c_2, c_3

**(a) figure-eight 4₁.**

- **Ohtsuki loop series** (knot-canonical rationals `a_1=11/12, a_2=697/288,
  a_3=724351/51840 = 0.917, 2.420, 13.97`): no parameter-free relation to
  `c_3 = −2.069`. `|err vs c_3| = 1.44, 2.17, 7.75` — not close, no sign match
  for the odd-loop coefficient.
- **Colored Jones at the substrate q₀** (real): `J_{4₁}(N;q₀) = 1.033, 1.093,
  1.190, 1.343` for N=2..5 — all near 1, none near `−2.069` under any natural
  normalisation.

**(b) Hopf link.** The registry hint `V_Hopf(t=1) = −2` is the **only**
near-`c_3` value, and:
1. it **misses `c_3` by 3.35 %** (`−2` vs `−2.0693`), and
2. it is the **q→1 CLASSICAL limit** — a *value*, not a root-of-unity / Habiro
   structure. At q=1 the quantum deformation is trivial; there is **no Ohtsuki
   series** there. `V_Hopf(t=q₀) = −2.352` (moves the *wrong* way, +14 % vs
   `c_3`); the Reshetikhin–Turaev `(2,2)` value at q₀ is `+2.044` (positive,
   wrong sign).

**(c) trefoil 3₁ control.** `V_{3₁}(q₀) = 0.960` — as expected, the
non-hyperbolic control bears no relation to either target.

## Verdict — HONEST NEGATIVE

**No FORCED candidate reproduces `c_2` AND `c_3` parameter-free.**

The complex / root-of-unity fibre-element lead is therefore **ALSO closed for
the forced candidates** — the only ones the anti-fitting discipline admits.

- The Hopf `−2` is the classical-limit coincidence already recorded in the
  registry (3.35 % off, `J_Hopf(q=1)`), **not** a root-of-unity Habiro structure.
- The 4₁ Ohtsuki loop coefficients and colored-Jones values bear no
  parameter-free relation to `c_3`.
- `c_3` anchor-rigidity (real-q falsification, PR #2452 / 2026-06-04 audit)
  **stands**: a genuine fibre element would have to be a complex-analytic
  object whose evaluation *tracks* the −2.88 % cross-anchor swing, and neither
  forced knot's invariant supplies one without a tuned index/normalisation.

This does **not** refute the *abstract* possibility of a complex fibre element
(the `complex-c3-fibre-probe` left that structurally plausible); it shows that
**the two framework-forced knots do not realise it**. Since the discipline bars
scanning further knots/roots, the productive root-of-unity direction for `c_3`
is exhausted at the structural level. `c_3` stays EMPIRICAL (registry §3).

## Relation to prior root-of-unity work

- [`2026-06-13-qbeta-root-of-unity-residue-program.md`](2026-06-13-qbeta-root-of-unity-residue-program.md)
  (#2240) probed which `Φ_d` the **content-Casimir `μ_λ`** carries (ζ₂ all
  modes, ζ₆ three modes, ζ₄ absent at the summed level). That is the *kernel
  cyclotomic structure* question. **This** audit is the orthogonal *forced-knot
  invariant* question, and is also negative.
- [`qbeta-complex-c3-fibre-probe`](../../computations/probes/qbeta-complex-c3-fibre-probe.witness.json)
  tested abstract complex-`c_3(q)` candidate *forms*; it did NOT compute the
  actual forced-knot invariants. This probe fills that gap.

## No production change

Per the registry flip-flop guard: nothing is wired. `c_2 = −1` remains the only
canonical rung; `c_3` remains EMPIRICAL near-match.
