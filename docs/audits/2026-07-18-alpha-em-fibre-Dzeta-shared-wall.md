# α_EM shared-wall gate — FIBRE side: `D(ζ) ∉ {8, 8π}` — falsified on BOTH sides

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure ↔ W_λ keystone shared wall ·
**Tier:** measurement (scope-(a) **negative**; no `α_k` wired; no fit; `1/(8π)` stays a
phase-4 identification). **Branch:** `claude/alpha-em-fibre-Dzeta-shared-wall-2026-07-18`.
Completes the ONE piece the observable-side self-test (#3871) explicitly left open.

## What was tested

The merged shared-wall acceptance gate (#3853) reduced the α_EM ↔ W_λ hypothesis to
one falsifiable number: the two walls are one (via a nonabelian `S₀₀ = 1/D`) **iff** the
keystone total quantum dimension

$$D \;=\; \sqrt{\textstyle\sum_\lambda d_\lambda^2}\;\in\;\{\,b_1 = 8,\ \pi\!\cdot\! b_1 = 8\pi \approx 25.133\,\}.$$

The observable-side run (#3871) evaluated the **full untruncated real-`q₀`** side:
`D(q₀) = √(Σ_{λ⊢5} d_q(λ)²) = 11.357 ∉ {8, 8π}` ⇒ falsified there. It left exactly one
case untested — the **fibre-side level-truncated *admissible*** `D(ζ)` at a root of unity
`ζ`, "a different (smaller) number than the observable-side untruncated `D(q₀)`" (#3871
§"Still open"). **This audit runs the gate on that fibre-side `D(ζ)`.**

## Corpus-fixed data — NO scan (the anti-fitting requirement)

Every datum is independently fixed upstream by the merged keystone chain; **the root, the
level, and the admissible set are not free parameters** (choosing `ζ` or the level to make
`D = 8` would be the forbidden fit):

| datum | fixed value | fixed by |
|---|---|---|
| root of unity `ζ` | `e^{iπ/5}` (order `2p₃ = 10`, the order-5-fibre holonomy of Σ(2,3,5)), Galois-indexed by the two flat connections `m = 1,2` (`ζ, ζ²`); **not** the level root `ζ_N`, **not** `e^{2πi/30}` | #3822 / #3685 |
| admissible set | the 9 affine-`Ê₈` McKay nodes, marks `(1,2,3,4,5,6,4,2,3)` = dims of the 2I irreps (`Σ mark² = 120 = |2I|`) | McKay `2I↔Ê₈` (#3685, #2424) |
| truncation | mark-5 node has `[5]_ζ = sin(π)/sin(π/5) = 0` (verified `≈7e-43`), so the admissible support folds **2:1** onto the `r = 5` alcove `{1,2,3,4}` — the folded modular category is **SU(2)₃** (`k = 3`, `r = k+2 = 5`) | #3822 fold |
| value map | `d_ζ(λ) = [mark(λ)]_ζ = sin(mark·mπ/5)/sin(mπ/5)` | #3685 |

The corpus already established the fibre-side total quantum dimensions in **exact `ℚ(√5)`**
(#3822, `lr_modulus_identification_sigma235.py`): `D_{Ê₈}(ζ^m)² = Σ_{9 nodes}[mark]²_{ζ^m}
= 10 ± 2√5` and `D_{MTC}(ζ^m)² = 5 ± √5`, with `D_{Ê₈}² = 2·D_{MTC}²` (the 2:1 fold). This
probe reuses those values (numeric cross-check `< 1e-35`; the exact leg is #3822's, cited)
and simply **feeds them to the #3853 gate**.

## Result — falsified on the fibre side

```
                    D(ζ)        D/8       D/8π      ∈{8,8π}?
  Ê₈  m=1 (ζ)      3.804226    0.47553   0.15137     NO
  MTC m=1 (ζ)      2.689994    0.33625   0.10703     NO      = √(5+√5) = SU(2)₃ √5/(√2 sin(π/5))
  Ê₈  m=2 (ζ²)     2.351141    0.29389   0.09355     NO
  MTC m=2 (ζ²)     1.662508    0.20781   0.06615     NO
  targets:  b₁ = 8,   π·b₁ = 8π = 25.1327
```

For **all four** corpus-fixed readings (both flat connections × both the `Ê₈`-node and the
folded-`MTC` normalizer) `D(ζ) ∈ {1.66, 2.35, 2.69, 3.80} ∉ {8, 8π}`. The naive `S₀₀ = 1/D`
identification fails on the fibre side too.

## Both sides now closed — `b₁ = 8` is bracketed but hit by neither

| side | keystone total quantum dimension `D` | vs `b₁ = 8` |
|---|---|---|
| **fibre** (truncated, `ζ = e^{iπ/5}`) | `D(ζ) ∈ {1.66, 2.35, 2.69, 3.80}` | all `< 8` |
| **observable** (untruncated, real `q₀`) | `D(q₀) = 11.357` (#3871) | `> 8` |

`b₁ = 8` sits **between** the two sides and equals **neither**. There is no corpus-fixed
root / level / normalization at which the keystone total quantum dimension is `8` or `8π`.
So the α_EM per-loop measure `1/(π b₁)` and the W_λ keystone `1/D` are **distinct
normalizations at every corpus-fixed evaluation** — the two walls are fully distinct
objects. The tempting two-for-one (close α_EM *and* the m_p/m_μ keystone with one `D = 8`)
is settled: **falsified on both sides.**

## Scope — a scope-(a) negative, NOT a structural exclusion

Per the anti-over-claim discipline (§"Before declaring 'refuted'"): this refutes the
**specific** identification "photon `b₁` = keystone total quantum dimension `D`", tested
against the corpus's fixed data, at the last untested case (the fibre root). It does **not**
exclude every conceivable link between `b₁` and the keystone — `b₁` could still enter the
photon measure via a route **other than the total quantum dimension** (a per-irrep `d_λ`, an
index, or a different combination — the alternative #3871 also left open). Recorded as (a).
No proved invariant forbids the ingredient, so no (b) claim is made.

## Why this is a positive contribution

The #3853 gate was built to be **falsifiable**; #3871 fed it the observable side and it
returned NO, leaving the fibre side as the one open case. This audit feeds it the corpus's
fixed fibre data — no scan, no tuning — and it returns NO there too. That **closes** the
shared-wall unification on both sides, preventing future agents from chasing it, and
sharpens where a real link (if any) must live (a non-`D` route: per-irrep, index, or
combination). No number was tuned; `1/(8π)` remains a phase-4 identification.

## Method note

`mpmath` at 40 dps; the four `D(ζ)` values cross-checked against #3822's exact `ℚ(√5)`
closed forms `10 ± 2√5`, `5 ± √5` (and the fold `D_{Ê₈}² = 2 D_{MTC}²`, and the SU(2)₃
closed form `√5/(√2 sin(π/5))`) to `< 1e-35`. The exact `ℚ(√5)` derivation of those closed
forms is #3822's, machine-validated and cited, not re-run here.

## Cross-references

- Gate: #3853, [`alpha_em_wlambda_shared_wall_acceptance_gate_probe.py`](../../computations/alpha_em/alpha_em_wlambda_shared_wall_acceptance_gate_probe.py)
- Observable-side falsification: [`2026-07-18-alpha-em-shared-wall-gate-falsified-observable-side.md`](2026-07-18-alpha-em-shared-wall-gate-falsified-observable-side.md) (#3871)
- Fibre modular data (exact `ℚ(√5)`): #3822, [`2026-07-17-lr-modulus-identification.md`](2026-07-17-lr-modulus-identification.md), [`lr_modulus_identification_sigma235.py`](../../computations/lr_modulus_identification_sigma235.py)
- McKay `2I↔Ê₈` value map: #3685, [`2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md`](2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md)
- Unitarity/normalization gate framing (`Σ_λ W_λ = Z(q) < 1`): [`2026-07-17-keystone-wlambda-unitarity-normalization-gate.md`](2026-07-17-keystone-wlambda-unitarity-normalization-gate.md)
- Keystone modular data: `KeystoneVerlindeSMatrixBridge.lean`; ledger [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
- Probe: [`computations/alpha_em/alpha_em_fibre_Dzeta_shared_wall_test_probe.py`](../../computations/alpha_em/alpha_em_fibre_Dzeta_shared_wall_test_probe.py) · Witness: [`alpha-em-fibre-Dzeta-shared-wall-test.witness.json`](../../computations/alpha_em/alpha-em-fibre-Dzeta-shared-wall-test.witness.json) (2 assertions, all passed)
