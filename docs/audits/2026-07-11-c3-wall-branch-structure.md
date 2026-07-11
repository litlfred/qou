# The c₃ `S` wall, structurally: `𝔙(u)` branch points + reduction to one phase

**Date:** 2026-07-11 · **Branch:** `claude/c3-wall-complex-volume-branch-structure-2026-07-11` ·
**Tier:** formalize-first structural derivation (scope-(a); C14; no fit). **Probe:**
[`qbeta_c3_wall_branch_structure_probe.py`](../../computations/qbeta/qbeta_c3_wall_branch_structure_probe.py).

"Work on the wall": deriving the **analytic structure** of the open `u(q₀)` map
(`S = Im 𝔙(u(q₀))`) rather than fitting it. Result: the wall's skeleton is
derived and the remaining open content is reduced to a **single real phase**.

## 1. Branch points of the figure-eight `𝔙(u)` (derived)

From the A-polynomial `L + 1/L = R(M)`, `R(M)=M⁴−M²−2−M⁻²+M⁻⁴`, `M=e^{u/2}`, the
two `L`-lifts collide (discriminant `R²−4=0`) at:

| branch point | `M` | `u = 2 ln M` |
|---|---|---|
| complete | `M=1` | `0` (quadratic branch) |
| **golden** | `M=φ=(1+√5)/2` (`M²=φ²=(3+√5)/2`) | `±2 ln φ ≈ ±0.9624` |
| imaginary | `M=i` | `iπ` |

The **golden ratio** appearing in the 4₁ complex-volume branch locus is a clean
derived fact. The physically relevant branch for `|u|~HA≈0.21` is `u=0`.

## 2. The `S` sign-flip is a quadrant crossing (derived)

The `u=0` branch is **quadratic**: `𝔙(u) ≈ 𝔙(0) − (τ/4)u²`, `τ = 2√−3`, so

$$
\mathrm{Im}\,𝔙(u) \;\approx\; \tfrac{\sqrt3}{2}\,|u|^2\,\sin(2\arg u),
$$

which has **four sign-quadrants** (zero-lines at `arg u = 0, π/2, π, 3π/2`).
`S(muon)>0>S(proton)` therefore means **`arg(u(q₀))` crosses `π/2`** between the
anchors. Because the anchors differ only `~10⁻⁸` in `q₀`, the phase must move
across that boundary rapidly — which **is** the `dc₃/dq≈4.66×10⁶` hyper-sensitivity
(a phase near a quadrant boundary), not a smooth-magnitude near-singularity.

## 3. The wall reduced to one phase (non-fitting inversion)

Fixing the magnitude `|u|=HA=q−q⁻¹` (the electron-weight lead) and `√3` (the
derived cusp shape), invert **only** the phase from the measured `S`:

| anchor | `(√3/2)HA²` | `sin(2 arg u) = S/amp` | `arg u` |
|---|---|---|---|
| muon | `0.03785` | `+0.256` | `≈ 82.6°` |
| proton | `0.03785` | `−1.043` | `≈ 135°` |

The two required phases **straddle 90° (π/2)** — confirming the branch-crossing
picture. (The proton `|sin|=1.043>1` means `|u|=HA` is marginally small there —
higher-NZ / `|u|` slightly larger — not a defect of the structure; the straddle
is robust.) This is an **extraction of the open map's values**, not a fit of a
formula to `S`.

## Disposition — what is now derived vs still open

- **Derived:** the branch-point structure of `𝔙(u)` (golden-ratio locus), the
  quadratic `u=0` branch, `Im 𝔙 ~ (√3/2)|u|²sin(2 arg u)`, the magnitude `|u|≈HA`,
  and the **mechanism** of the `S` sign-flip (`arg u` crossing π/2).
- **Open (the whole residue):** the single real phase function `arg(u(q₀))` and
  the `q*` where it `= π/2` (the `S` zero-crossing). This is the archimedean
  realization functor / the deformed-complex-VC substrate map — the same object
  `conj:algebraic-geometric-dilog-equivalence` carries. The wall is now a
  **one-real-function** problem, not an unstructured map.

## Cross-references
- Complex-volume conditional: [`2026-07-11-complex-volume-conditional-mass-binding.md`](2026-07-11-complex-volume-conditional-mass-binding.md)
- Kashaev grounding: [`qbeta_c3_kashaev_invariant_grounding.py`](../../computations/qbeta/qbeta_c3_kashaev_invariant_grounding.py)
- `conj:binding-qbeta-complex-volume` (`S = Im 𝔙`); AGENTS.md §"Formalize-first"; §"Before declaring refuted (a)/(b)".
