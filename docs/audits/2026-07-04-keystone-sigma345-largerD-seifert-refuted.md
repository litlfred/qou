# Keystone value-map redirect (i) — Σ(3,4,5) larger-D Seifert vacuum row does NOT host the 4-class target; the whole compact-modular route is q₀-blind

**Date:** 2026-07-04
**Bean:** [`s013`](../../.beans/s013--keystone-value-map-colored-lawrence-rozansky-s-mat.md) (the keystone value step)
**Follows:** [`2026-07-02-keystone-valuemap-genuine-smatrix.md`](2026-07-02-keystone-valuemap-genuine-smatrix.md) — settled Σ(2,3,5) negative (D=2, golden row) and listed three redirects; this closes redirect **(i)**.
**Script:** [`computations/probes/keystone_valuemap_sigma345_dm6.py`](../../computations/probes/keystone_valuemap_sigma345_dm6.py)
**Witness:** [`computations/probes/keystone-valuemap-sigma345-dm6.witness.json`](../../computations/probes/keystone-valuemap-sigma345-dm6.witness.json)
**Status:** redirect (i) refuted. Scope (a) on the specific manifold; scope-(b) structural softener (q₀-independence) recorded but **not** over-claimed as a hard exclusion of a single-q₀ coincidence.

## The lead

The 2026-07-02 refutation of the Σ(2,3,5) route noted that its false-theta
modular family is only **D = 2**-dimensional (golden vacuum row ∝
(sin π/5, sin 2π/5), ratio φ), whereas the keystone target

$$\mathrm{bwS0}(\lambda) = \frac{d_q(\lambda)}{D}\quad\text{at } n=5$$

is a **4-class** family with ratios (1, 4.110, 5.220, 6.220). The one un-run
redirect was a **larger-D Seifert manifold**: Σ(3,4,5) is the smallest
pairwise-coprime Brieskorn sphere with
$D(3,4,5) = \tfrac{(3-1)(4-1)(5-1)}{4} = 6$ and **γ = 4 flat connections** —
exactly the number of bwS0 classes.

## What was computed (validated, not fabricated)

The already-validated Hikami machinery (eq. 3.1 characters, eq. 3.8 modular
S-matrix — the identical generic code from the (2,3,5) probe, re-pointed to
`PVEC = (3,4,5)`, `P = 60`) was extended and re-anchored:

| Anchor | Result |
|---|---|
| Independent components (χ-table dedup) | **D = 6**, reps (1,1,1),(1,1,2),(1,1,3),(1,1,4),(1,2,1),(1,2,2) — matches the formula |
| **S² = I** (involution — the anti-fabrication anchor; a sign/factor error breaks it) | max \|S²−I\| = **4.4×10⁻⁵⁰** ✓ |
| Vacuum row orthonormality ‖row‖² = 1 | **1.0** (exact) ✓ |

The genuine vacuum row (row of the (1,1,1) class), sorted magnitudes, gives
ratios over the smallest entry:

$$(1,\ 1,\ \sqrt2,\ \varphi,\ \varphi,\ 2.2882\ldots).$$

Every ratio is **bounded by ≈ 2.29** — the golden pair φ reappears (twice),
alongside √2 and 2.288. The bwS0 target needs a spread up to **6.22**.

## The verdict

**Best-matching 4-subset of the Σ(3,4,5) vacuum row vs the target: max relative
error 69%.** No 4-subset reproduces (1, 4.110, 5.220, 6.220).

- **Scope (a) — the manifold.** The genuine Σ(3,4,5) D=6 modular vacuum row does
  not carry the 4-class keystone value map. Refuted as-is.

- **Scope-(b) softener — why the compact-modular route is the wrong *kind* of
  object (invariant cited, but not over-claimed).** The genuine modular
  S-matrix entries $\sqrt{32/P}\prod_j \sin(P\,\ell_j\ell'_j\pi/p_j^2)$ are
  **rational-angle sines — algebraic constants independent of the substrate
  q₀**. The bwS0 targets are q-integers at q₀ and move with it: the probe
  measures $\partial(\text{target})/\partial q_0 = (0,\ 1.91,\ 3.85,\ 3.85)
  \neq 0$. A fixed geometric tuple therefore cannot *track* the q₀-dependent
  target as the modulus varies — a compact-modular match could only ever be a
  single-point coincidence at the substrate value. **We do not upgrade this to
  a hard exclusion** (a single-q₀ coincidence is logically possible per the
  (a)/(b) discipline); the numerical test above shows it simply does not occur
  for Σ(3,4,5), and the structural point explains *why the search should not
  continue among compact Seifert modular rows at all*.

## Consequence for the keystone program

Redirect (i) (larger-D Seifert modular vacuum rows) is closed. Combined with the
2026-07-02 Σ(2,3,5) result, **both compact-modular geometric routes are
exhausted**, and the q₀-blindness argument explains it structurally: the
compact modular data of *any* Brieskorn/Seifert sphere is a substrate-agnostic
set of algebraic constants, while bwS0 = d_q/D is an explicit non-constant
function of q₀.

This **confirms the 2026-07-02 screen-probe redirect**: the only geometric
object that can be q₀-dependent — and hence could realise bwS0 without a
coincidence — is the **non-compact q-Bessel vacuum row** (Hahn–Exton q-Bessel at
real q₀ > 1, the SU_q(2)→E_q(2) contraction). The remaining redirects from the
2026-07-02 note stand: (ii) the Ẑ/GPPV side (Murakami 2205.01282, colored /
b-decorated blocks) and (iii) the non-geometric representation-theoretic status
of `BWVacuumRowIsHecke`. Redirect (i) is no longer among them.

No fit; the S-matrix is transcribed verbatim from the validated (2,3,5) probe
with only PVEC/P changed; nothing wired; CAL-1/2/3 untouched.

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694 (eqs. 3.1, 3.8)
