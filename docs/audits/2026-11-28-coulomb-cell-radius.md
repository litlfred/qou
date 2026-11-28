# The Coulomb length: what is left is one number, the cell radius c (qou-mbfv, from G3)

Date: 2026-11-28. Beans `qou-tcl3`, `qou-mbfv`. Follows PR #9859 (size law `ε³·A = const`).
No Lean change: the statement below is the size law of `QOU/Nuclear/CoulombBlockSize.lean`
with `v` written in pion units.

## 1. Where the length stands

`coulomb_energy.nuclear_radius_fm` uses `R = c·λ̄_π·A^{1/3}` with `c = 1`.

| piece | status |
|---|---|
| unit `λ̄_π = ħc/m_π` | CAL-3, the admissible orthogonal meson scale (AGENTS.md calibration table) |
| `A^{1/3}` | derived under (H1) homogeneity and (H2) additive volume, PR #9859 |
| `c` (nucleon cell radius in pion units) | **selected** (`c = 1`). This is the only number left |

So the "one length" of #9859 is not a missing unit. It is one dimensionless coefficient.

## 2. Two candidate values, recorded side by side (owner card open; neither adopted)

* **Arm A, `c = 1`** (current): each nucleon is a ball of radius `λ̄_π`.
* **Arm B, `c³ = 3/2`, `c = 1.1447`**: (H2) applied at the strand level. The pion has 2 strands
  and the nucleon 3, so with one volume per strand and the pion's size taken as `λ̄_π`, the
  nucleon cell has `3/2` of the pion's volume.

**Disclosure.** Arm B was written down after the #9691 table, which shows the A = 3 miss, had
been read. It is therefore not a blind pre-registration and must not be adopted on its numbers.

## 3. Comparison only (AME2020 mirror splits; `coulomb_energy_mev`, derived shape)

| pair | AME ΔB (MeV) | arm A (c = 1) | arm B (c³ = 3/2) |
|---|---|---|---|
| ³H/³He | 0.7638 | 0.948 (+24.1 %) | 0.828 (+8.4 %) |
| ⁷Li/⁷Be | 1.6439 | 1.917 (+16.6 %) | 1.674 (+1.9 %) |
| ¹⁵N/¹⁵O | 3.5367 | 3.469 (−1.9 %) | 3.031 (−14.3 %) |
| ³⁹K/³⁹Ca | 7.3068 | 6.848 (−6.3 %) | 5.982 (−18.1 %) |
| ⁴¹Ca/⁴¹Sc | 7.2780 | 7.089 (−2.6 %) | 6.193 (−14.9 %) |

`c` only rescales every row by `1/c`, so no value of it can fix the light rows and the heavy rows
together. The sign of the miss changes between ⁷Li and ¹⁵N on both arms, at the same place as
the shape-factor switch (q-Hankel for A ≤ 4, the imported ball above, PR #9699). So the
remaining pattern is a **shape** effect, not a length effect. The next lever is a derived shape
for A ≥ 5 (p-shell), which would replace the imported ball.

Scope (a). No measured value is in any proof.
