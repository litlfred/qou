# 5₂ part 2c-2 — wall-crossing at the substrate bar-pair; φ_odd sharpening obstructed (honest, localized)

**Date:** 2026-07-18 · **Branch:** `claude/5two-part2c-wall-crossing-barpair-2026-07-18`
· **Tier:** research probe (scope-(a); no `c_k` wired; no fit). Consolidates one
tranche: applying the certified (250) wall-crossing determinant identity at the
substrate bar-pair and testing whether φ_odd can be sharpened beyond the #3987
preliminary −0.004145.

Probe: [`computations/probes/qbeta_g3_5two_wall_crossing_barpair.py`](../../computations/probes/qbeta_g3_5two_wall_crossing_barpair.py)
· witness `computations/probes/qbeta-g3-5two-wall-crossing-barpair.witness.json`.

## What part 2c-1 handed over

`qbeta_g3_5two_deformed_bilinear.py` (part 2c-1) certified the (250) wall-crossing
determinant identity — the exact `q → q⁻¹` (bar) transform of the deformed
H-blocks — at **generic** `(x,y,z,q)` to 1e-45, and pointed at part 2c-2: "apply
(250) at the substrate bar-pair → φ_odd at derived precision."

φ_odd is the intrinsic bar-odd phase of the 5₂ σ3 conjugate-pair
(`φ_odd = arg a₂ + arg b₂`, the deviation of the bar-side amplitude `b₂` from the
conjugation-symmetry prediction `b₂ = conj(a₂)`). The odd-channel capstone
([`2026-07-18-qbeta-odd-channel-cornering-capstone.md`](2026-07-18-qbeta-odd-channel-cornering-capstone.md))
established that this σ3-pair is a **permanent non-amphichiral bar-odd carrier**
but is **anchor-smooth** (~7 orders below the c₃ swing scale). So φ_odd is a
**dictionary datum** — the intrinsic bar phase of the 5₂ σ3-pair — not the carrier
of the c₃ anchor swing (which is representational). "Sharpening" means pinning its
exact value for the dictionary.

## Structural finding — the substrate is exactly the (250) degeneracy node (C1)

At the substrate q₀:

- τ = i·t/2π is **purely imaginary**, so the bar-pair `(q = e^{−t} = 0.90092,
  q̄ = q⁻¹ = 1.10998)` is **entirely REAL**.
- The substrate sits **exactly on the block pole lattice**: `x = e^{u_sub} = q⁻²`
  (`u_sub = 2t`) to 1e-46.
- The (250) θ-triple prefactor
  `θ(−x q^{−1/2}; q)·θ(−q^{−1/2}; q)·θ(−x⁻¹ q^{−1/2}; q)` is **exactly zero** at
  the substrate (the first two factors vanish identically). ⇒ the (250) identity is
  **0/0** at the physical point.

So **φ_odd lives exactly at the lattice node where the classical factor the (250)
identity strips vanishes.** The wall-crossing tool is certified in the substrate
*neighbourhood* (off-lattice, `q` near `e^{−t}`: the printed (250) reading
reproduces the H⁻ branch to <1e-35), but the exact substrate point is a 0/0 node —
the same pole-lattice degeneracy that made the raw bar-split degenerate in the
`barodd_substrate` probe (#3962). The (250) tool does **not** dissolve that
degeneracy; it relocates it into the explicit (vanishing) θ-triple.

## The core result — the φ_odd extraction is precision-UNSTABLE (S1)

The #3987 σ3-pair strip solves a 2×2 system at two ray points `(τ, 1.02τ)`. Two
facts about that solve at the substrate wreck it:

1. The classical prefactor is **exponentially large**: on the ray
   `2πiτ = −t`, so `e^{V_σ/2πiτ} = e^{−V_σ/t}` with `Re(−V_σ/t) ≈ 34.5` for the
   σ3-pair — magnitude `e^{34.5} ≈ 10^{15}`. The strip extracts a **~10⁻² phase
   residual** sitting on top of this — needing ~15+ extra guard digits just to
   see it, and far more as the σ3-real saddle (`Re(−V/t) ≈ 74`, `e^{74} ≈ 10^{32}`)
   leaks in.
2. The two ray points are only `2 %` apart, so the 2×2 rows are **near-parallel** —
   the solve is intrinsically ill-conditioned.

The consequence is a **precision-dependent bimodal result** — sweeping the mpmath
working precision (`dps`) with the committed machinery:

| dps | \|a₂\| | φ_odd (2-loop) | branch |
|---|---|---|---|
| 40 | 0.958 | −0.004145 | physical (near-unit) — #3987 |
| 45 | 0.958 | −0.004145 | physical |
| 50 | 4.4×10⁻⁵³ | +0.899 | **spurious collapse** |
| 60 | 0.958 | −0.004145 | physical |
| 70 | 4.4×10⁻⁵³ | +0.899 | spurious collapse |

The extraction lands on the physical near-unit-amplitude branch (`|a₂| ≈ 0.96`,
φ_odd ≈ −0.004) only at "lucky" precisions (dps 40, 45, 60, 80, 150, 200) and
collapses to a **spurious null-space branch** (`|a₂| ≈ 10⁻⁵³…10⁻⁴²⁷`,
φ_odd ≈ +0.90 / +0.038) at others (dps 50, 100, 300) — **non-monotonically in
dps**, and the collapse **recurs at high precision** (dps 100, 300 collapse; a
robust `K=40`, dps-scaled-radius average still collapses at dps 100). High
precision therefore does **not** robustly rescue the extraction. Where it does
land on the physical branch, the value carries ~4 % dependence on the
circle-average scheme (−0.003999 with `K=40` / dps-scaled radius vs −0.004145 with
the committed `K=12, r=10⁻⁴`), i.e. it is pinned to only **~1 significant figure**.
The #3987 preliminary −0.004145 is thus a legitimate physical-branch value but is
**precision- and scheme-delicate**, not a converged number.

The 1-loop vs 2-loop values at a physical-branch precision (−0.000163 vs
−0.004145, a ~25× swing, `O(τ²) ≈ 3×10⁻⁴` ≈ the value) show the value is *also*
loop-truncation-dominated even where the solve is stable.

## The multi-loop sharpening attempt — obstructed (S2)

To beat the 2-loop truncation, we solved the σ3-pair amplitudes **and** their
higher per-saddle loop coefficients simultaneously from `N` exact ray evaluations
(saddle exponents `V_σ / δ_σ` fixed from the Lean-proved cubic, `c₁` from the
printed (238)) — an exact inversion of the known transseries form against exact
data (not a fit). It gives **no trustworthy limit**, for two compounding reasons:

- **The condition number explodes** with loop order. At dps 60:
  `cond ≈ 156 → 2.0×10⁶ → 4.5×10⁹ → 3.8×10¹³ → 4.9×10¹⁷` for loops `≤1…≤5`. Each
  added order loses more digits than it adds.
- **The result is precision-branch-dependent.** At dps 60 the sequence reads
  `−0.00444 → −0.00107 → −0.00169 → −0.00177 → −0.00178` — whose small-Δ tail
  *looks* like convergence to ≈ −0.0018, but that tail sits entirely at
  `cond > 10¹²` (untrustworthy), and at a spurious-collapse precision (dps 50) the
  *same* extraction lands in a completely different range `[0.5, 4.2]` rad
  (`4.23 → 0.51 → 1.47 → 2.98 → 3.16`). The apparent dps-60 limit −0.0018 is
  therefore a **precision-branch + ill-conditioning artifact**, not a derived
  value — it is neither precision-robust nor consistent with the 2-loop −0.0044.

  > A mechanical "last-3 within 1e-4" check with only a lax `cond < 10³⁰` gate
  > *does* flag the dps-60 tail as "converged to −0.0018" — this is exactly the
  > kind of spurious convergence the probe's **strict** gate (tractable
  > `cond < 10¹²` **and** S1 precision-stability `n_phys = 4`) is built to reject.
  > Reporting −0.0018 as a "sharpened φ_odd" would be laundering an
  > ill-conditioned fit as a derivation; it is not claimed.

The obstruction is **structural, not a bad parametrization**: at the small
substrate `τ ≈ 0.0166` the loop-correction columns `τ^k` are numerically
indistinguishable from an amplitude rescaling (they collapse toward the constant
column over any ray window narrow enough for the single-pair asymptotics to hold),
while widening the window breaks the two-saddle model (the contour-absent
magnitude-dominant σ3-real saddle re-enters and higher loops matter). There is no
good window — matching the "numerics lane is exhausted" finding of the earlier
dictionary-diagnostic tranche (#4009-area).

## Verdict (scope-(a); honest OPEN, precisely localized)

- **Certified:** the substrate geometry (real bar-pair; `x = q⁻²` on the block
  pole lattice; (250) θ-triple = 0), and the (250) wall-crossing tool in the
  substrate neighbourhood.
- **Established:** the #3987 preliminary −0.004145 is the **2-loop** value. It is
  both (i) **precision-/scheme-delicate** — the on-lattice extraction is bimodal
  (physical branch vs spurious collapse) non-monotonically in dps, and where
  physical the value ranges −0.003999…−0.004145 (~1 sig fig) — and (ii)
  **loop-truncation-dominated** (25× swing 1→2 loop). It **cannot** be promoted to
  derived precision from the printed 2-loop (238) data + ray numerics.
- **Localized remaining step:** a derived φ_odd needs higher-loop (238)-type
  coefficients (`c₂, c₃, …` — printed-data-blocked in `2012.00062v3` §6.2) **or** a
  resummation of the σ3 transseries. It is **not** obtainable by deeper numerics at
  the substrate τ-window, and the (250) block identity does not isolate the
  saddle Stokes constants that φ_odd is built from.
- φ_odd = −0.004145 **stands as a 2-loop PRELIMINARY** (dictionary datum for the
  anchor-smooth, permanent 5₂ σ3-pair carrier).

No fit; no `c_k` wired; scope-(a) throughout. The scope-(a) label is exact: this
constrains the *method* (ray numerics + printed 2-loop cannot pin φ_odd), not any
ingredient — the σ3-pair intrinsic phase remains a valid non-amphichiral bar-odd
carrier, its exact value simply deferred to higher-loop data or resummation.
