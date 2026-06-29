# Δ_λ canonical residual — synthesis map (2026-06-29)

**Branch:** `claude/delta-lambda-imme-synthesis-bcoeff-2026-06-29`. Consolidates
#3089 (10A−5 + writhe Z-correction + mirror cancellation) and #3104 (IMME degree-2
+ same-T). **Discipline:** near-match tier; no fit (Δ_λ gate); not wired.

## The one-line map

The canonical-binding residual `Δ_λ = B_AME / B_pred` on the Jones–Markov path
(`binding_canonical.py`), as a function of mass number `A` and isospin
projection `T₃ = (Z−N)/2`, is the **Isobaric Multiplet Mass Equation** shape:

$$ \log_{q_0}\Delta_\lambda(A, T_3) \;=\; \underbrace{a(A)}_{\text{isoscalar}}
   \;+\; \underbrace{b(A)\,T_3}_{\text{bar-odd writhe}}
   \;+\; \underbrace{c(A)\,T_3^2}_{\text{bar-even, small}} \;+\;\dots $$

Three terms, two parity channels (under the mirror `T₃ → −T₃`), each isolated by
a different finite difference. All three are pinned by direct compute on the
light isobaric multiplets.

## Term-by-term

### `a(A)` — the isoscalar leading term (bar-even)

The `T₃=0` value. Equals the near-integer `q₀`-power `q₀^{10A−5}` **only for
A ≤ 4** (D, T, ⁴He: exponent 15, 25, 35, exact to ≤0.27 units). The slope test
(#3089: ⁶Li/⁷Li/⁷Be) **refuted its continuation** at A ≥ 5 — `log Δ_λ` flattens
(slope 10 → ~0.4 at the ⁴He shell) because `B_pred` saturates (~0.7–0.8) while
`B_AME` grows ~linearly. So `a(A)` is a light-nucleus coincidence as a power law;
the crossing-sum arithmetic `σ+σ⁻¹ = 10A−2` (Lean `crossing_sum_cancels`) stands
but does not extrapolate as a global binding exponent.

### `b(A)` — the bar-odd writhe Z-correction (linear; the dominant correction)

The mirror difference `f(+T₃) − f(−T₃) = 2·b·T₃` isolates it (Lean
`imme_mirror_diff`, refining `mirror_baseline_cancels`). It is the bar-ODD
**writhe** `σ−σ⁻¹ = 4Z` (Z-only), with the per-nucleon p≠n seed proton `+3` ≠
neutron `+1` fixing the **sign** (proton excess penalised). Measured values:

| A | b (q₀-exponent units) |
|---|---|
| 3 (³He/T) | −1.34 |
| 6 (⁶Be/⁶He) | −1.73 |
| 8 (⁸B/⁸Li) | −1.80 |
| 10 | _(pending compute)_ |
| 12 | _(pending compute)_ |

**Trend (item 3 characterization).** `b(A)` grows then **saturates** (−1.34 →
−1.73 → −1.80): sub-linear in A, despite the writhe itself growing as `4Z ∼ 2A`.
The saturation is the same `log`-compression that flattens `a(A)` — the residual
is a *ratio* whose logarithm grows slowly. Physically `b` is the IMME
charge-asymmetry coefficient (Coulomb-displacement + n–p mass term); in real
nuclei the MeV-level `b` grows ~`A^{2/3}` (Coulomb), but here it is the *residual
exponent's* odd part, which saturates. **Honest status:** `b(A)` is an
observational trend consistent with a Coulomb-displacement reading; a
parameter-free categorical derivation is **not** claimed (3–5 points, no fit).

### `c(A)` — the bar-even quadratic (small, A-independent)

The triplet second difference `f(+1) + f(−1) − 2·f(0) = 2·c` isolates it (Lean
`imme_triplet_2nd_diff`). The **raw** `c` (−1.24 at A=6, −3.44 at A=8) was almost
entirely **T=0/T=1 contamination**: the `T₃=0` ground states (⁶Li, ⁸Be) are T=0,
not the T=1 isobaric analog. Correcting to the analog state (measured `E_x`:
3.563, 16.626 MeV — #3104) **collapses** `c`:

| A | c (raw) | c (same-T, clean) |
|---|---|---|
| 6 | −1.24 | −0.11 |
| 8 | −3.44 | −0.10 |
| 10 | _(pending)_ | _(pending)_ |
| 12 | _(pending)_ | _(pending)_ |

So the genuine quadratic is **small (≈−0.1) and A-independent** — the residual is
**linear-(writhe)-dominated** (`|b| ≈ 1.8 ≫ |c| ≈ 0.1`).

## The two Askey structures (one per quantum number)

- **Body-order `n`:** the b-ladder `a(n+2) = 2cosh(10η₀)·a(n+1) − a(n)` (the `10`
  is the per-nucleon slope) is a three-term recurrence → continuous q-Hermite /
  Al-Salam–Chihara in the **Askey q-scheme**.
- **Isospin `T₃`:** the IMME is the **degree-2 truncation** — Wigner's rank-≤2
  isotensor = the Askey–Racah cutoff (Lean `imme_third_diff_zero`: `Δ³ = 0`, no
  `d·T₃³` — a falsifiable prediction for a fourth multiplet member).

## Net status

- **Form: established** (IMME degree-2; Lean-proved parity algebra).
- **`a(A)`: light-nucleus power law only** (refuted A≥5, scope-(a)).
- **`b(A)`: dominant, saturating; Coulomb-displacement candidate** (observational,
  no derivation).
- **`c(A)`: small ≈−0.1, A-independent** (the residual is writhe-linear-dominated).
- **Not wired; no fit.** Closure would need an owner reversal of the Δ_λ fit-gate.
- **Open:** A=10/12 confirmation (pending compute); a categorical origin for the
  small `c`; whether `b(A)`'s saturation is the categorical Coulomb.
