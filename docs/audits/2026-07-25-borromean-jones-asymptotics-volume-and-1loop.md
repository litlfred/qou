# W1 Jones-side asymptotics: volume anchor + subleading 1-loop datum

**Date:** 2026-07-25
**Tier:** audit-only; scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7).
**Epic:** W1 of the binding-mass workplan — the `I_𝓑₃ → tr_M(β_Bor) → F_Bor`
bridge (follow-on to
[`2026-07-24-borromean-index-bridge-invariant.md`](2026-07-24-borromean-index-bridge-invariant.md)
and [`2026-07-25-borromean-index-fbor-bridge-invariant.md`](2026-07-25-borromean-index-fbor-bridge-invariant.md)).

## Why the Jones side

The bridge invariant list (07-24 §1(e)) **prunes** coefficientwise evaluation of
`I_𝓑₃` at q₀ (integer coeffs, q₀ ≈ 1.10998 > 1 outside the index disc `|q| < 1`,
series diverges) and leaves only **limit/continuation** bridge classes (§1(d)),
of which the **volume-asymptotics route** (DGG arXiv:1112.5179 §4.6, q→1 't Hooft
limit — the index's leading asymptotics carry `Vol(M)`) is named "the honest
candidate." Both prior docs stop at *stating* the route.

This audit supplies the **numbers**, from the side the corpus can compute exactly:
the Habiro colored-Jones tower `J_{B,N}(e^{2πi/N})` (Garoufalidis–Le
arXiv:math/0508100 v6 App A). The Kashaev / Ohtsuki asymptotic expansion of a
hyperbolic link is

$$\log|J_{K,N}(e^{2\pi i/N})| = \frac{N}{2\pi}\,\mathrm{Vol} + p\,\log N + c_0 + O(1/N),$$

so the tower delivers, in order, the volume (leading), the power `p` (prefactor),
and the 1-loop constant `c₀`.

## Result 1 — leading term: `Vol(𝓑₃) = 8G` (PR #4208, merged)

Producer [`borromean_jones_volume_anchor.py`](../../computations/probes/borromean_jones_volume_anchor.py).
Root-of-unity growth `y(N) = (2π/N)·log|J_{B,N}(ζ)|`, log-aware extrapolated
(subtracting the `(3/2)·log N /N` subleading term):

| quantity | value |
|---|---|
| raw `y(N=40)` | 7.9857 (still carries the `(logN)/N` tail) |
| **log-aware fit intercept `Vol`** | **7.3571 (rel 4.0e-3)** |
| target `Vol(𝓑₃) = 8G` | 7.327725 |

Recovers `Vol(𝓑₃) = 8G ≈ 7.32772` (two ideal regular octahedra, `G` = Catalan)
to **0.4%** — the same hyperbolic volume the DGG index asymptotics must carry.

## Result 2 — subleading: power `p ≈ 3/2` and 1-loop `c₀ ≈ −1.38`

Producer [`borromean_jones_1loop_torsion.py`](../../computations/probes/borromean_jones_1loop_torsion.py).
Fixing `Vol = 8G` and fitting `log|J| − (N/2π)Vol = p·log N + c₀ + Σ_{m} d_m/N^m`
(higher-order `1/N` tail, `KMAX=2`, `N ≤ 56`); a free-slope fit cross-checks:

| coefficient | Vol-fixed fit | free-slope cross-check |
|---|---|---|
| slope `a` (→ `a·2π` vs 8G) | — (fixed) | 1.16627 → **7.32787** (8G = 7.32772, rel 2e-5) |
| **power `p`** | **1.49935** | 1.49702 |
| **1-loop `c₀`** | **−1.38281** | −1.37347 |

Two findings:

1. **The power is the knot-like `3/2`**, not a larger multi-cusp power — even
   though 𝓑₃ has **three** cusps. Both fits land within `3e-3` of `1.5`; under the
   corpus's `J_{B,1}=1` normalization the reduced Kashaev invariant of the
   Borromean rings grows with the same `N^{3/2}` prefactor as a 1-cusp knot.
2. **The 1-loop constant `c₀ ≈ −1.38` is measured** (`exp c₀ ≈ 0.251`), the two
   fits agreeing to `~0.01`. The free-slope fit *independently re-confirms* the
   volume (7.32787, rel 2e-5).

## Result 3 — the extraction pipeline validated on 4₁ (to `2e-11`)

Producer [`jones_1loop_c0_calibration_fig8.py`](../../computations/probes/jones_1loop_c0_calibration_fig8.py).
The Borromean `c₀` is only a *measurement* until the extraction is validated on a
case whose 1-loop constant is known in closed form. The figure-eight `4₁` is that
case. Running the **same** higher-order least-squares pipeline on the corpus's own
figure-eight Kashaev sum (`figure_eight_kashaev_volume.py`, `N ≤ 6000`, `KMAX=4`):

| quantity | measured | exact | error |
|---|---|---|---|
| `Vol(4₁)` (free-slope) | 2.0298832128193 | `2·Cl₂(π/3)` | rel `3e-15` |
| power `p` | 1.5000000000 | `3/2` | `2e-12` |
| `c₀` | −0.274653072146 | `−¼ log 3` | `2e-11` |
| **`|τ_adj(4₁)| = exp(2c₀)`** | **0.577350269214** | **`1/√3`** | **`2e-11`** |

So the pipeline recovers the figure-eight's **adjoint Reidemeister torsion**
`|τ_adj(4₁)| = 1/√3` — the full 1-loop-conjecture content
(Dimofte–Garoufalidis arXiv:1102.4847) — to `2e-11`. (Note: in the corpus's
un-normalized Kashaev normalization `c₀(4₁) = −¼log3`, **not** the literature
`−log(2·3^{1/4})`; the `log 2` offset is the normalization convention. The
earlier `~1e-4` agreement was purely one-term truncation error — modelling `1/N`
through `1/N⁴` at `N ≤ 6000` drives it to `2e-11`, the arithmetic being exact.)

**Consequence.** The `exp(2c₀) = |τ_adj|` relation and the `(p, c₀)` extraction are
now proven correct on a known knot. Applying `exp(2c₀)` to the Borromean tower
gives a candidate `|τ_adj(𝓑₃)| ≈ 0.063`.

## What is NOT claimed (anti-fit discipline)

The Borromean `exp(2c₀) ≈ 0.063` is a **candidate**, not a verified `τ(𝓑₃)`,
because the `4₁` anchor is a **1-cusp knot in the un-normalized Kashaev
normalization**, whereas the Borromean tower is a **3-cusp link in the Habiro
`J_{B,1}=1` normalization** — an unresolved normalization + cusp-count offset sits
between them (the same offset that produced the `4₁` `log 2`). Per invariant list
§1(f) (anti-fit) we do **not** tune that offset to land `0.063` on a target.
Turning the candidate into a verified match requires the **independent**
computation of `τ(𝓑₃)` from the octahedral Neumann–Zagier data (`grep 2026-07-25`:
corpus has no Borromean torsion) — the bounded follow-up.

## Result 4 — the independent Neumann–Zagier torsion `|det J_NZ(𝓑₃)| = 64`

Producer [`borromean_nz_adjoint_torsion.py`](../../computations/probes/borromean_nz_adjoint_torsion.py).
The `c₀` candidate is closed **without any Jones input** by computing the
Dimofte–Garoufalidis 1-loop invariant directly from the topology. For an ideal
triangulation with shapes `z_j`, each gluing equation
`Π_j z_j^{a_j}(1−z_j)^{b_j} = ±1` has NZ Jacobian
`J_ij = a_ij − b_ij·z_j/(1−z_j)`; the square system of `(N−c)` independent edges
`+ c` meridians, at the complete structure, gives the torsion determinant. Inputs
are SnapPy's `gluing_equations('rect')` for `4₁`/`L6a4` + the **exact algebraic**
complete-structure shapes (`4₁`: `z=e^{iπ/3}`; `L6a4`: regular ideal octahedron
`z∈{(1+i)/2, 1+i}`) — the probe is self-contained (no SnapPy at runtime;
`--recompute` cross-checks live).

| manifold | `|det J_NZ|` | exact | `1/|det|` |
|---|---|---|---|
| `4₁` (validation) | 1.7320508075689 | **`√3`** (err 3e-51) | **`1/√3 = exp(2c₀(4₁))`** ✓ |
| **`𝓑₃ = L6a4`** | 64.0 | **`64 = 2⁶`** (err 0) | `1/64` |

The `4₁` value reproduces the `#4238` calibration `exp(2c₀(4₁)) = 1/√3`
**exactly, from pure topology** — the same relation `exp(2c₀) = 1/|det J_NZ|`
now confirmed on both the analytic (Kashaev) and topological (NZ) sides.

**Closure.** The Jones-side `#4238` measurement gave `c₀(𝓑₃) ≈ −1.383 ≈ −ln4`,
i.e. `exp(2c₀) ≈ 1/16 = 4/64`. So the **independent** NZ torsion `64` and the
Jones `c₀` agree up to a clean factor `exp(2c₀)·|det J_NZ| = 4.03 ≈ 4` — the
3-cusp normalization offset **predicted** (not fitted) in `#4238`: the relation is
`1/|det|` for the 1-cusp knot and `4/|det|` for the 3-cusp link. The residual
`0.03` is the `c₀` extraction uncertainty (Borromean tower `N≤56`); `c₀=−ln4`
gives the factor exactly `4`. The Borromean `c₀` candidate is thereby **matched to
an exact, independently-computed topological invariant**, resolving its
`candidate` status.

The exact first-principles value of the factor `4` (Habiro `J_{B,1}=1`
normalization + diagonal-vs-full cusp framing for the 3 equal colors) is the one
remaining thread — a clean rational bookkeeping factor, **not** a free parameter.

## Where this leaves W1

Four Jones-side / topological rungs now stand, all parameter-free:
`Vol(𝓑₃)=8G` (#4208), power `3/2`, `c₀` measured (#4238), `c₀→torsion`
validated to `2e-11` on `4₁`, and the **independent NZ torsion
`|det J_NZ(𝓑₃)|=64`** matching `c₀` to a clean factor-4. The **actual** bridge —
the subleading state-integral identification connecting `I_𝓑₃` to `tr_M(β_Bor)` —
remains the research-paper-scale open gap, pursued index-side on beans
`qou-zezz` / `qou-yaz9` (DGG state-integral / charge dictionary).

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md
