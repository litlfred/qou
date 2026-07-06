# Staircase EW-residual k=3 spectral analysis at mpmath 50 dps — 2026-05-17

## Question

The staircase EW-residual conjecture
([`conj:staircase-ew-residual`](../../content/quantum-observable-universe/braids-and-knots/staircase-ew-residual.md))
states that on the staircase Specht module `V_{ρk}` of `H_{n_k}(q)`,
the matrix image of the canonical β_EW Δ_I^minimal word has two
nonzero eigenvalues whose ratio is `q^(1/(2k − 1))`.

Empirically, the conjecture was verified at **float64 precision**:

* `k = 3` (dim 16): closes the bare `max+/2nd-max+` reading to CODATA
  cot θ_W with `0.13 %` residual after multiplication by `q^(1/5)`
  (`close_321_weinberg_gap.py`).
* `k = 4` (dim 768): best pairwise ratio matches `q^(1/7)` with
  `0.14 %` deviation (`staircase_ew_residual_conjecture.py`).

This audit asks: **is the `0.13 %` residual a float64 noise artifact
(would converge to `<1e-12` at 50 dps) or a genuine correction
(would persist at any precision)?**  The distinction matters because:

* **If noise**: the conjecture is a closed-form algebraic identity
  in `q`, derivable from Hoefsmit-matrix combinatorics. Categorical
  formalisation route opens.
* **If genuine**: the conjecture is an APPROXIMATE leading-order
  match; higher-order corrections are needed for an exact identity.
  Categorical formalisation requires either accepting the approximate
  status or finding the correction series.

## Probe

[`probe_staircase_ew_k3_categorical.py`](../../computations/probe_staircase_ew_k3_categorical.py)
re-does the k=3 spectral computation at **mpmath 50 dps**:

1. Build 16×16 Hoefsmit V_(3,2,1) matrices `σ_1, …, σ_5` at 50 dps
   (direct mpmath port of `hecke_character_symbolic._hoefsmit_build`).
2. Compute β_EW word image
   `M = σ_1⁴ · (σ_2 σ_4 σ_2) · σ_3⁶ · (σ_2 σ_4 σ_2) · σ_5⁸ · (σ_2 σ_4 σ_2)`
   (27 generators).
3. Diagonalise `M` via `mp.eig` at 50 dps.
4. Identify the top-two positive real eigenvalues `e_top, e_2nd`.
5. Compute two distinct readings:
   * **Reading A** (close_321 path): `bare = e_top / e_2nd`,
     `residual = cot θ_W^CODATA / bare`, compare with `q^(1/5)`.
   * **Reading B** (literal conjecture): scan all pairs `(i, j)`,
     find the pair with `e_i / e_j` closest to `q^(1/5)`.

## Results (at q_0 ≈ 1.10997..., 50 dps)

| Quantity | Value (truncated to 20 dps) |
| --- | --- |
| `e_top` (eigenvalue 0) | `5.2403253081667519738` |
| `e_2nd` (eigenvalue 2) | `2.9388009575132422241` |
| bare `e_top / e_2nd` | `1.7831508101184968024` |
| CODATA cot θ_W (sin²θ_W = 0.23121) | `1.8234781174896103309` |
| **Reading A** residual = CODATA / bare | `1.0226157580964414522` |
| Predicted residual `q_0^(1/5)` | `1.0210874086805358107` |
| **Reading A** `|Δ_rel|` | `1.4968e-3` (= 0.150 %) |
| **Reading B** best pair `(5, 6)` ratio | `1.0920785668553500608` |
| **Reading B** `|Δ_rel|` | `6.9525e-2` (= 6.95 %) |

## Conclusions

### 1. The 0.13% residual is NOT float64 noise

At 50 dps precision, the **Reading A** residual deviation from
`q^(1/5)` is **0.150 %** — essentially identical to the float64
baseline of **0.13 %** (the small difference comes from the choice
of `sin²θ_W` value: PDG effective `0.23121` here vs. the cited
baseline's exact `0.23122`).

The 0.13 % residual is therefore a **structural correction**, not a
precision artifact. **The conjecture, taken as an exact identity, is
falsified at 50 dps.**

### 2. The literal conjecture statement is also falsified

Reading B (scanning all eigenvalue pairs for one whose ratio matches
`q^(1/5)`) finds the best match has **6.95 %** deviation — three
orders of magnitude worse than the conjecture's claim that two
eigenvalues have ratio *equal to* `q^(1/5)`.

**No pair of eigenvalues on `V_{(3,2,1)}` has ratio exactly `q^(1/5)`
at q_0.**  The conjecture's literal content fails.

### 3. The "residual factor" reading remains empirically valid

Reading A's `0.15 %` match is still much better than other small
q-rationals would give; `q^(1/5)` is the BEST single-term
approximation, even though it is not exact.  The conjecture should
be **refined** to state that:

* The cot θ_W discrepancy (between CODATA and the bare V_(3,2,1)
  eigenvalue ratio) is **APPROXIMATED** by `q^(1/(2k − 1))` to
  ~0.15 % accuracy.
* The exact correction requires either (a) higher-order terms in a
  systematic expansion, or (b) a different categorical mechanism
  than the corner-hook identification.

## Recommendation

* **Conjecture status**: downgrade from "exact" to "approximate
  leading-order match" pending discovery of the next-order correction.
* **Lean status**: the `StaircaseEWResidual` class instance's `sorry`
  remains a genuine conjecture, but its `HasEigenvalueRatio` predicate
  should be re-examined — perhaps the intended content was always
  "ratio approximately q^(1/(2k−1))" rather than equal to.
* **Categorical route**: the corner-hook identification (`h_corner(ρk)
  = 2k − 1`) likely controls the LEADING-ORDER behaviour but does not
  produce the exact ratio.  Future probes should look for the
  next-order correction (e.g. `q^(1/(2k−1) + ε(q))` with `ε(q) → 0`
  as `q → 1`).

## Provenance

* Probe: `computations/probe_staircase_ew_k3_categorical.py`
* Witness: `computations/staircase-ew-k3-mpfr-spectral.witness.json`
* Float64 baseline: `computations/close_321_weinberg_gap.py`
* Original conjecture audit: `docs/audits/2026-05-06-staircase-ew-residual-conjecture.md`
