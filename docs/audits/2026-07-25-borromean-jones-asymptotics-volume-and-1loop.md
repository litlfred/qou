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

## Result 2 — subleading: power `p ≈ 3/2` and 1-loop `c₀ ≈ −1.417`

Producer [`borromean_jones_1loop_torsion.py`](../../computations/probes/borromean_jones_1loop_torsion.py).
Fixing `Vol = 8G` and fitting `log|J| − (N/2π)Vol = p·log N + c₀ + d/N` over the
tail `N ≥ 16`; a 4-parameter free-slope fit cross-checks:

| coefficient | Vol-fixed fit | free-slope cross-check |
|---|---|---|
| slope `a` (→ `a·2π` vs 8G) | — (fixed) | 1.16596 → **7.3259** (8G = 7.3277) |
| **power `p`** | **1.50639** | 1.52207 |
| **1-loop `c₀`** | **−1.41658** | −1.46810 |
| `1/N` coeff `d` | 1.94324 | — |

Two findings:

1. **The power is the knot-like `3/2`**, not a larger multi-cusp power — even
   though 𝓑₃ has **three** cusps. Under the corpus's `J_{B,1}=1` normalization the
   reduced Kashaev invariant of the Borromean rings grows with the same `N^{3/2}`
   prefactor as a 1-cusp knot (both fits: 1.506 / 1.522).
2. **The 1-loop constant `c₀ ≈ −1.417` is measured** (`exp c₀ ≈ 0.243`). The
   free-slope fit *independently re-confirms* the volume (7.326, rel 2.4e-4 —
   tighter than Result 1, since it does not force the `(3/2)` power).

## What is NOT claimed (anti-fit discipline)

By the 1-loop conjecture (Dimofte–Garoufalidis arXiv:1102.4847), `exp c₀` is fixed
by the **adjoint Reidemeister torsion** `τ(𝓑₃)` of the complete hyperbolic
structure. The corpus carries **no** Borromean adjoint torsion (grep 2026-07-25),
so `c₀` here is an honest **measurement**, not a verified `τ`-match. Per the
invariant list §1(f) (anti-fit: "no constant chosen from a menu because it lands
near a target") we deliberately do **not** hunt for a coincidental `c₀ → τ`
identity. Turning the measurement into a match requires the **independent**
computation of `τ(𝓑₃)` from the octahedral Neumann–Zagier data — the bounded
follow-up.

## Where this leaves W1

The leading (volume) and the power (`3/2`) terms any honest `index ↔ tr_M` bridge
must share are now anchored/measured on the Jones side. The **actual** bridge —
the subleading torsion / state-integral identification connecting `I_𝓑₃` to
`tr_M(β_Bor)` — remains the research-paper-scale open gap, pursued index-side on
beans `qou-zezz` / `qou-yaz9` (DGG state-integral / charge dictionary). The next
Jones-side rung is `τ(𝓑₃)` via octahedral NZ, to test `c₀` against.

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md
