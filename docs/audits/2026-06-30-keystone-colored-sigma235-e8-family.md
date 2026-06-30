# Keystone: λ-colored Σ(2,3,5) WRT gives the E₈-exponent family — 4↔4 correspondence to bwS0

**Date:** 2026-06-30
**Branch:** `claude/keystone-super-schurweyl-lead-2026-06-30`
**Status:** Structural advance on the residual keystone frontier. No fit; direct `Ψ = W_λ` not asserted.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Probe:** [`computations/probes/keystone_colored_sigma235_wrt.py`](../../computations/probes/keystone_colored_sigma235_wrt.py) · **Witness:** [`keystone-colored-sigma235-wrt.witness.json`](../../computations/probes/keystone-colored-sigma235-wrt.witness.json)
**Takes the open step pinpointed by:** [`2026-06-22-keystone-modular-category-identification.md`](2026-06-22-keystone-modular-category-identification.md) + the bare probe [`keystone_habiro_wrt_s3_2i_probe.py`](scripts/keystone_habiro_wrt_s3_2i_probe.py).

## The frontier this advances

The keystone reduced to one open field — `bwS0 λ = d_q(λ)/D` (`KeystoneVerlindeSMatrixBridge.lean`,
`BWVacuumRowIsHecke`): does the geometric BW/WRT(S³/2I) data realize that specific unit vector? The
modular-category identification settled the *arena* (non-compact `E_q(2)` / Hahn–Exton q-Bessel at
real `q₀ > 1`, bridged by the Habiro ring) and the bare-invariant probe computed the
**closed-manifold** WRT(Σ(2,3,5)) number `Ψ(1/q₀) = 2.3296`. Its verdict pinpointed the open step:

> the λ-family needs the WRT TQFT with **λ-colored insertions** (colored Σ(2,3,5) invariants /
> S-matrix), not the bare closed-manifold number.

This note takes that step.

## The colored construction (no fit — pure surgery arithmetic + the same false theta)

The Lawrence–Zagier false theta `Ψ(q) = Σ χ(n) q^{n²/120}` of Σ(2,3,5) has support on the residues
`n ≡ 30·(1 ± 1/2 ± 1/3 ± 1/5) (mod 60) = {1,11,19,29}` — the ρ-shift of the SU(2) WRT surgery
presentation (`P = p₁p₂p₃ = 30 = h(E₈)`). A Wilson line on the **order-5 exceptional fibre** — the
icosahedral / A₅ fibre, the keystone's own fibre — colored by the SU(2) colour `α` replaces
`1/5 → α/5`, giving the colour-α support `R(α) = {30·(1 ± 1/2 ± 1/3 ± α/5) mod 60}`:

| colour α | support R(α) | Ψ^{(α)}(1/q₀) |
|--:|---|--:|
| 1 | {1, 11, 19, 29} | 2.329577 |
| 2 | {7, 13, 17, 23} | 2.530556 |
| 3 | {7, 13, 17, 23} | 2.530556 |
| 4 | {1, 11, 19, 29} | 2.329577 |

- **α=1 reproduces the bare support** `{1,11,19,29}` and `Ψ ≈ 2.330` — validates the colour formula
  against the independent bare probe.
- **α=2 gives `{7,13,17,23}`** — the *complementary* four E₈ exponents.
- **The two lowest colours generate ALL EIGHT E₈ exponents** `{1,7,11,13,17,19,23,29}` (α=3,4 fold
  back to α=2,1 — the icosahedral `α ↔ 5−α`).

So the colored insertions lift the bare single invariant to an **E₈-exponent-indexed family** — the
structural object the bare number lacked.

## The colour↔block correspondence (the new finding)

The 8 E₈ exponents pair under the Coxeter involution `e ↔ h − e = 30 − e` into **4 dual pairs**; the
n=5 `bwS0` family collapses under conjugation `λ ↔ λ′` into **4 classes**. The two align 4↔4, and
**monotonically in magnitude**:

| E₈ dual pair {e, 30−e} | bwS0 conjugation class | bwS0 |
|---|---|--:|
| {1, 29} | (5) ~ (1⁵) | 0.088052 |
| {7, 23} | (4,1) ~ (2,1,1,1) | 0.361867 |
| {11, 19} | (3,2) ~ (2,2,1) | 0.459672 |
| {13, 17} | (3,1,1) self-conj | 0.547724 |

The **wall pair `{1,29}`** (extremal exponents) ↔ the trivial/sign blocks (smallest `bwS0`); the
**center pair `{13,17}`** (closest to `h/2 = 15`) ↔ the self-conjugate `(3,1,1)` (largest `bwS0`).
The Coxeter involution `e ↔ 30−e` on the colored-fibre exponents mirrors the **transpose / chirality
ℤ₂** `λ ↔ λ′` on the `W_λ` blocks — the same ℤ₂ that the keystone's `S_{0λ} = S_{0λ′}` symmetry and
the `archimedean-chirality` Reeb involution carry. This is precisely the bosonic-colour foreclosure's
decisive obstruction (`W_λ = W_{λ′}`) being *supplied* by the colored construction rather than
violated.

## Scope / discipline ((a) structural advance, value step remaining)

- **No fit.** The colour formula `1/5 → α/5` is the standard fibre-coloring of the surgery
  presentation; α=1 reproducing the bare invariant validates it. A direct numerical
  `Ψ^{(α)} = W_λ` equality is a type mismatch (q-series scalar vs S-matrix row) and is **not**
  asserted.
- **What is established:** the colored Σ(2,3,5) family *exists*, is *E₈-exponent-indexed*, and maps
  **4↔4 monotone** onto the `bwS0` conjugation classes at n=5 (the lepton-generation block). This is
  the geometric carrier the residual frontier required, with an explicit colour↔block correspondence.
- **Remaining value step:** the exact pair→class assignment normalization (the `D` that turns the
  colored q-series scalars into `bwS0(λ) = d_q(λ)/D`) and its numerical realization. Now standing on
  an explicit colored family rather than a single closed-manifold number.

## Cross-references

- [`2026-06-22-keystone-modular-category-identification.md`](2026-06-22-keystone-modular-category-identification.md) — settled the arena; named "λ-colored insertions" as the open step.
- [`2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md`](2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md) — excluded the *naive SU(2) spin-j* modular data (≤2-row coverage); the colored fibre construction here is the richer object that gate left open.
- [`2026-06-22-keystone-wrt-schurweyl-higher-colour-foreclosure.md`](2026-06-22-keystone-wrt-schurweyl-higher-colour-foreclosure.md) — the `W_λ = W_{λ′}` obstruction the Coxeter involution here supplies.
- [PR #2503](https://github.com/litlfred/qou/pull/2503) — the DG attack plan whose Step-1 this feeds.
