# Δ_λ magnitude — Vector 2 (the √5 bridge): is `m` a Σ(2,3,5) S-matrix vacuum-row entry?

**Date:** 2026-07-18 · **Axis:** per-isotope binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`,
magnitude front · **Tier:** exploratory probe (scope-(a); **no fit**; nothing wired) ·
**Verdict:** **honest negative** — the √5 *ceiling* is a genuine algebraic coincidence
with the icosahedral S-matrix eigenvalue, but the exchange magnitude `m` is **not** one of
its vacuum-row entries.

Producer: [`computations/deltalambda/deltalambda_icosahedral_smatrix_magnitude_probe.py`](../../computations/deltalambda/deltalambda_icosahedral_smatrix_magnitude_probe.py)
· witness `computations/deltalambda/deltalambda-icosahedral-smatrix-magnitude.witness.json`.
Executes **Vector 2** of the attack-vector map
([`docs/audits/2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md) §4),
the highest-value lead.

## 1. The hypothesis (parameter-free, no fit)

The magnitude wall of the Δ_λ closure is now a **single** real scalar `m ∈ (0, 1/√5)`
(#3924, [`b4_slater_antisymmetrizer_exchange_sign.py`](../../computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py)):
the connected `[1⁴]` cumulant is `b₄ = −ln det(I + m·S)` with the ⁴He K₄ writhe-sign
exchange matrix `S`, whose spectrum is exactly `{±√5, ±1}`, giving
`det(I+mS) = (1−5m²)(1−m²)` and the positivity/physicality ceiling `m < 1/√5 = 0.44721`.

The ceiling `1/√5` **is** the inverse of the icosahedral eigenvalue `√5`, and the corpus
already derives the Σ(2,3,5) (binary-icosahedral) modular S-matrix **exactly** in ℚ(√5)
([`lr_modulus_identification_sigma235.py`](../../computations/lr_modulus_identification_sigma235.py)):
the flat-connection amplitudes are `A_m(α) = (2/√5)·sin(αmπ/5)` and the folded-MTC / Ê₈
vacuum rows are `S_{0λ} = d_{ζ^m}(λ)/D(ζ^m)` with `D_E8(ζ^m)² = 10 ± 2√5`,
`D_MTC(ζ^m)² = 5 ± √5`. **Hypothesis:** `m` equals a *specific parameter-free entry* of that
vacuum row — a proved algebraic coincidence, not a fit tuned to the data.

## 2. Method — E₀-free forward test (`m` fixed BEFORE comparison)

For each light isotope, build the complete-graph writhe-sign exchange matrix `S_A`
(pp=+1, nn=−1, pn=±1; diag 0), form `G = m·S_A`, and take the connected dimensionless
binding `𝒟_A(m) = −ln det(I + m·S_A)`. The det closed forms — **algebraic-preflight
verified** against `mp.det` at `m ∈ {0.1, 0.3, 0.42}` to `1e-30`, and the ⁴He spectrum
`{±√5,±1}` re-verified — are:

| isotope | `(Z,N)` | triangle flux `abc` | `det(I+mS)` |
|---|---|---|---|
| D | (1,1) | — | `1 − m²` |
| ³He | (2,1) | `+1` | `1 − 3m² + 2m³` |
| ³H | (1,2) | `−1` | `1 − 3m² − 2m³` |
| ⁴He | (2,2) | — | `(1 − 5m²)(1 − m²)` |

The determinant is **not** blind to the ³H/³He mirror: the 3-body triangle-flux invariant
`abc = ∏(edge signs)` is `+1` for ³He (ppn̄) and `−1` for ³H (pnn̄), a conjugation invariant,
so the two mirror partners get *different* determinants. This is the sharp diagnostic.

Because `𝒟_A/𝒟_{A'}` is **E₀-independent** (the `E₀ → MeV` unit dressing is the separately
open scalar), the parameter-free test is the **ratio** test against AME2020 (non-circular):

| ratio | model | AME2020 target |
|---|---|---|
| `ρ_4` | `𝒟_4/𝒟_2` | `B(⁴He)/B(D) = 12.720` |
| `ρ_3He` | `𝒟_3He/𝒟_2` | `B(³He)/B(D) = 3.4695` |
| `ρ_3H` | `𝒟_3H/𝒟_2` | `B(³H)/B(D) = 3.8129` |
| `mirror` | `𝒟_3H/𝒟_3He` | `B(³H)/B(³He) = 1.0990` |

**Coherent gate.** A candidate closes the bridge only if **one** parameter-free `m`
reproduces **all four** ratios simultaneously (≤5%). A single ratio grazing across a finite
menu is a menu coincidence, not a realisation (the discipline of
[`keystone_qhankel_eq2_vacuum_row.py`](../../computations/probes/keystone_qhankel_eq2_vacuum_row.py)).
`m` is **never** solved from the deficits — that would be the forbidden 7th ansatz.

## 3. Candidate palette (finite, forced by the S-matrix)

| candidate | value | vs ceiling `0.44721` | result |
|---|---:|---|---|
| `1/√5` (K₄ eigenvalue / ceiling) | 0.44721 | boundary | `det_4 = 0`, unphysical |
| `(2/√5)·sin(π/5)` — raw vacuum-row `A_1(1)` | 0.52573 | **above** | EXCLUDED by ceiling |
| `(2/√5)·sin(2π/5)` — raw vacuum-row `A_1(2)` | 0.85065 | **above** | EXCLUDED by ceiling |
| `2/√5` — vacuum-row scale | 0.89443 | **above** | EXCLUDED by ceiling |
| `1/D_MTC(ζ²) = 1/√(5−√5)` | 0.60150 | **above** | EXCLUDED by ceiling |
| `1/D_MTC(ζ) = 1/√(5+√5)` — folded-MTC `S_00` | 0.37175 | below | forward-tested → fails |
| `1/D_E8(ζ) = 1/√(10+2√5)` — Ê₈ `S_00` | 0.26287 | below | forward-tested → fails |
| `1/D_E8(ζ²) = 1/√(10−2√5)` — Ê₈ `S_00(ζ²)` | 0.42533 | below | forward-tested → **ρ_4 only** |
| `1/φ²` (golden, natural) | 0.38197 | below | forward-tested → fails |

**Finding 1 (structural).** The **raw** vacuum-row entries `(2/√5)sin(π/5)`,
`(2/√5)sin(2π/5)`, `2/√5` — the literal `(2/√5)(sin π/5, sin 2π/5)` row the hypothesis
pointed at — **all exceed the physicality ceiling** `1/√5`. The exchange magnitude cannot be
a raw vacuum-row amplitude; only the vacuum-row **normalizations** `1/D` and the golden
`1/φ²` survive `m < 1/√5`.

## 4. Forward-test result

| candidate `m` | `ρ_4` err | `ρ_3He` err | `ρ_3H` err | `mirror` err | coherent? |
|---|---:|---:|---:|---:|:--:|
| `1/√(5+√5)` = 0.37175 | 0.301 | 0.276 | 0.285 | 0.774 | ✗ |
| `1/√(10+2√5)` = 0.26287 | 0.456 | 0.245 | 0.023 | 0.355 | ✗ |
| `1/√(10−2√5)` = 0.42533 | **0.004** | 0.289 | 0.568 | **1.204** | ✗ |
| `1/φ²` = 0.38197 | 0.270 | 0.278 | 0.325 | 0.836 | ✗ |

**No parameter-free `m` reproduces all four ratios.**

**Finding 2 (the sharp diagnostic).** The Ê₈ second-flat-connection normalization
`S_00(ζ²) = 1/√(10−2√5) = 0.42533` reproduces the ⁴He/D ratio **strikingly**
(model 12.77 vs AME 12.72, **0.4%**), but the **same** `m`:

- **over-splits the ³H/³He mirror**: model `2.42×` vs AME `1.10×` (120% error), and
- **over-binds ³H / under-binds ³He** at the 3-body level (`ρ_3H` model 5.98 vs AME 3.81).

The ⁴He/D near-match is a **single-ratio hit** across a finite menu (menu-coincidence
caution) — **not** a coherent realisation. It echoes the map's #3943 finding: the det
route's triangle-flux over-splits the mirror (≈2.4× here, ≈2.25× there) where the data
splits by only ≈1.10×, so the residual is **collective / non-additive**, not a mis-set
per-pair magnitude.

**Structural context (why no `m` works).** As `m → 0`, `𝒟_A ≈ (m²/2)·A(A−1)`
(`Tr S_A² = A(A−1)`), so `ρ_4 → 6`, `ρ_3 → 3`, `mirror → 1`. Matching `ρ_4 = 12.72` forces
`m` near the ceiling; matching `mirror = 1.10` forces `m` small. These pull in opposite
directions — a fundamental A-scaling-vs-mirror tension no single scalar resolves. This is a
scope-(a) statement about *this construction alone*, not a proved exclusion of the `√5`
ingredient.

## 5. Verdict (scope-(a), no fit)

The `1/√5` **ceiling** is a genuine algebraic coincidence with the Σ(2,3,5) S-matrix
eigenvalue `√5` — that much is real and permanent. But the **magnitude scalar `m` is not a
vacuum-row entry**: the raw row entries exceed the ceiling, and among the surviving
normalizations the only one that matches ⁴He/D fails the 3-body and over-splits the mirror.
The √5 bridge, *as a magnitude identification*, does **not** close: this construction, alone,
does not reproduce the four-isotope binding ratios. Consistent with the standing reading that
the missing term is **collective / many-body**, not a per-pair constant. **No fit; nothing
wired.**

What remains genuinely open (not excluded here): a *collective* / graph-level object at the
`⁴He` locality (map Vectors 1 and 4), and whether the E₀→MeV dressing plus a many-body
(non-det-of-pairs) correction reconciles the A-scaling with the mirror.

## Cross-references

- Attack-vector map: [`2026-07-18-deltalambda-attack-vector-map.md`](2026-07-18-deltalambda-attack-vector-map.md) §4 (Vector 2)
- Magnitude structure (`det`, ceiling): #3924 [`b4_slater_antisymmetrizer_exchange_sign.py`](../../computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py)
- Σ(2,3,5) S-matrix vacuum row (EXACT ℚ(√5)): [`lr_modulus_identification_sigma235.py`](../../computations/lr_modulus_identification_sigma235.py)
- AME cumulant target: [`b4_value_cumulant_target_probe.py`](../../computations/probes/b4_value_cumulant_target_probe.py)
- Menu-coincidence discipline: [`keystone_qhankel_eq2_vacuum_row.py`](../../computations/probes/keystone_qhankel_eq2_vacuum_row.py)
- Gate ruling / open-for-all: [`2026-07-13-delta-lambda-gate-open-for-all.md`](2026-07-13-delta-lambda-gate-open-for-all.md)
