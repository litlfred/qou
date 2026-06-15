# B_qCLT isospin splitting is Coulomb, not categorical chirality — a symbolic A-scaling proof

**Date:** 2026-06-15
**Branch:** `claude/mirror-isospin-coulomb-2026-06-15`
**Scope:** exploratory analysis — no production rewire; the only free input is a single length scale, explicitly flagged.
**Compute:** [`mirror_isospin_coulomb_split.py`](../../computations/mirror_isospin_coulomb_split.py) (symbolic sympy derivation + AME2020 validation).

## Question

The factorized q-CLT binding form `B_qCLT_fac` (PRs #2320 / #2323) splits the
tritium / helium-3 mirror pair through bond-type composition — ³H carries an n–n
bond, ³He a p–p bond, with `L_nn > L_pp` — but over-predicts the split by ~2×.
Does a parameter-free correction (a damping factor `κ`, or a combination with the
exact-trace form `B_sym`) reproduce the measured isospin splitting across the mass
range?

## Setup

For a mirror pair `(Z,N) ↔ (N,Z)` the strong/categorical binding is
charge-symmetric; only the isospin-breaking term differs. At `α = E₀`:

- `B_qCLT_fac split = B_qCLT_fac(Z,N) − B_qCLT_fac(N,Z)`
- `B_sym split = B_sym(Z,N) − B_sym(N,Z)`
- `AME split = B_AME(Z,N) − B_AME(N,Z)` (the measured isospin splitting)

Two light mirror pairs admit a clean test: ³H/³He (A=3) and ⁷Li/⁷Be (A=7).
`B_qCLT_fac` is pure combinatorics on the three bond-type sub-braid ratios
(`L_pp, L_pn, L_nn`), so its split is computable for any pair; `B_sym` needs the
per-nucleus Markov trace.

## Finding 1 — the A=3 "`B_sym − B_qCLT_fac = AME`" relation is a coincidence

At A=3 the over-split factors are strikingly near-integer, and the
exact-minus-mean-field difference reproduces the measured split:

| | AME | `B_qCLT_fac` | `B_sym` |
|---|--:|--:|--:|
| ³H/³He split (MeV) | 0.764 | 1.514 (1.98×) | 2.271 (2.97×) |

`B_sym split − B_qCLT_fac split = 0.757` vs AME `0.764` (99.1%).

This suggests a parameter-free prescription, *physical split = exact-trace split −
mean-field bond split*. It does **not** survive the second mirror pair: at A=7 the
q-CLT over-split factor is **1.18×**, not ~2×. The near-integer 1:2:3 pattern is an
A=3 accident.

## Finding 2 — symbolic proof: the two splits have incompatible A-scaling

Let `A = Z + N`. Elementary algebra (sympy-verified) gives both candidate splits a
common isospin factor `(Z−N)(A−1)`:

```
Coulomb numerator      Z(Z−1) − N(N−1)  =  (Z−N)(A−1)
categorical numerator  C(N,2) − C(Z,2)  = −(Z−N)(A−1)/2
```

Substituting into the binding forms:

```
categorical (B_qCLT_fac) split = E₀ (L_nn − L_pp) (N−Z)(A−1) / A        [∝ A^(−1)]
Coulomb split                  = K_C (Z−N)(A−1) / A^(1/3)               [∝ A^(−1/3)]
```

with `K_C = (3/5) α_EM ℏc / r₀`. The over-split is therefore

```
over-split = categorical / Coulomb = E₀ (L_pp − L_nn) / (K_C · A^(2/3))   ∝  A^(−2/3).
```

This is a non-constant function of A. Hence **no A-independent damping factor `κ`
can map the categorical chirality split onto the physical split** — the
discrepancy is intrinsically A-dependent, growing as `A^(2/3)`. The A=3 value
`κ ≈ 1/2` is specific to A=3 and provably cannot generalize.

## Finding 3 — the Coulomb form fits both mirror pairs with one length scale

Solving the Coulomb split for `r₀` per pair:

| mirror pair | AME split (MeV) | Coulomb `r₀` (fm) | categorical `κ` needed |
|---|--:|--:|--:|
| ³H/³He (A=3) | 0.764 | 1.569 | 0.504 |
| ⁷Li/⁷Be (A=7) | 1.644 | 1.648 | 0.845 |

A single `r₀ ≈ 1.61 fm` reproduces both mirror splits to **4.9%**, where the
categorical `κ` is inconsistent (0.50 vs 0.85). The over-split A-scaling prediction
`(7/3)^(2/3) = 1.76` matches the observed `1.98/1.18 = 1.68` to ~5%.

## Verdict

The isospin splitting that `B_qCLT_fac` over-predicts is **Coulomb**
(charge-symmetry breaking, scaling `Z(Z−1)/A^(1/3)`), not a categorical-trace
chirality effect (scaling `A^(−1)`). To correct `B_qCLT` for mirror nuclei, add an
explicit Coulomb term rather than damping the categorical chirality:

```
B_qCLT_corrected(Z,N) = B_base(trace, isospin-symmetric)
                        − (3/5)(α_EM ℏc / r₀) · Z(Z−1) / A^(1/3).
```

The functional form is parameter-free; the single remaining degree of freedom is
the length `r₀ ≈ 1.61 fm`, currently fitted to the mirror splits. **Whether `r₀`
derives from the framework's substrate length** (the hyperbolic-volume scale that
sets `E₀`) is the open question this analysis isolates. The result independently
reproduces the merged q-Bessel audit (#2318): the Z-dependent (isospin) coefficient
is not derivable from the categorical bond ratios alone.

## Honesty / caveats

- Two mirror pairs (A=3, A=7). The `r₀` consistency (4.9%) is encouraging but
  `n = 2`; more pairs (¹¹B/¹¹C, ¹³C/¹³N, …) would test the single-`r₀` claim and are
  computable from AME alone.
- The Coulomb correction is standard nuclear physics; the contribution here is the
  symbolic proof that the categorical trace has the *wrong A-scaling* to be it, and
  the identification of `r₀` as the sole missing input.
- `B_sym` at A=7 (⁷Be trace) was not computed (environment gap); the q-CLT
  over-split factor breaking 2 → 1.18 alone refutes the A=3 pattern.
- Cached bond-type ratios `L_pp = 0.6945`, `L_pn = 0.9292`, `L_nn = 1.2370`
  (`tr_m_atom_zn` at `q₀`, 50 dps, this session) are recorded for reproducibility;
  the script recomputes them live via the canonical trace.

## Follow-ups

1. Extend the Coulomb-`r₀` test to ¹¹B/¹¹C, ¹³C/¹³N, ¹⁵N/¹⁵O (AME-only, no trace).
2. Ask whether `r₀ ≈ 1.61 fm` is fixed by the substrate hyperbolic-volume length
   (would make the isospin correction fully parameter-free).
3. Formalize Findings 1–2 (the `(Z−N)(A−1)` factorization + `A^(−2/3)` over-split)
   in Lean — elementary algebra over ℤ, env-permitting.
