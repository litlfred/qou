# The exact `r` needs the geometric quantum-dilog regular part — the honest research frontier of the g₂ chain

**Date:** 2026-07-26 · **Branch:** `claude/geometric-qdilog-amplitude-r-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, the exact residual `r = g₂ − 1` · **Owner steer:** *"1 2"*
(merge #4345, then push the geometric quantum-dilog amplitude) · **Tier:** one principled evaluation
+ honest frontier (scope-(a); **no fit; no scan**; nothing wired).

## 0. Where the whole chain stands

`g₂ = 1 + r`. Across the chain: `g₂_leading = 1` is exact (real coloring, #4339); the octahedral
tetrahedron shape carrying the bar-even structure is exactly `z' = −h²` (from the pinned rep, #4345);
`r` is the shapes→`e₂` nonlinearity. This note evaluates the amplitude on that pinned shape and
reports the honest state — including where fishing would begin, so it is not crossed.

## 1. The one principled evaluation (no scan)

The semiclassical amplitude of a tetrahedron of shape `z` in the octahedral state integral is the
dilogarithm `Li₂(z)` (the saddle of the geometric quantum dilog). Evaluated **once** on `z' = −h²`:

- `Li₂(z')/z' = 0.9893` — **order 1**, confirming `g₂ ~ 1`'s **scale**.
- Leading nonlinearity `Li₂(z)/z ≈ 1 + z/4 = 1 − h²/4 = 0.9891` — the dilog gives **`−1.07%`**.

But `r = g₂ − 1 = +0.87%`. **Opposite sign, different magnitude.** So the naive semiclassical `Li₂`
nonlinearity is **not** `r`.

## 2. Why — the wall (honest)

The exact `r` needs two things this evaluation does not have:

1. **The *geometric* quantum-dilog regular part** (2509.02354 §5.2, the pinched limit) — its finite
   part, *not* the naive `Li₂` saddle. The trefoil crossings are pinched (`ζ⁰ ∈ ℤ`, degenerate); the
   §5.2 regularization has its own finite part, which is the correct amplitude.
2. **All four octahedral shapes** `z_r, z_t, z_l, z_b`. This chain has **one** (`z' = −h²`, the
   equatorial cross-ratio of the four strand-endpoints); the other three need the octahedron's **apex
   data** `P±` — the per-crossing octahedral developing map, which SnapPy does not supply (it collapses
   the torus knot to the degenerate 2-tet).

**Where fishing would begin — and is refused.** Trying different dilog forms (`Li₂` vs Rogers `L` vs
Bloch–Wigner) or different shapes until one lands on `1.00865` is exactly the §2e forbidden scan (a
single ~0.9% target has far too little information content to identify against a menu of special
functions). This note does **one** principled evaluation and stops; it does not scan.

## 3. Net — the g₂ chain's honest terminus

| statement | status |
|---|---|
| `g₂ = 1 + r` decomposition; `g₂_leading = 1` (real coloring) | **derived, exact** (#4339) |
| the octahedral tetrahedron shape = `−h²` (from the pinned rep) | **derived, exact** (#4345) |
| the amplitude is `dilog(shape)`, order 1 ⇒ `g₂ ~ 1` scale | **confirmed** (this note) |
| the exact `r = +0.87%` | **OPEN** — geometric §5.2 regular part + the 4-shape octahedron |

This is a **single, well-posed, non-fishing research object**: the geometric quantum-dilogarithm
(2509.02354 §5.2, pinched finite part) evaluated on the four octahedral shapes of the deuteron
crossing, of which one is the exact `−h²`. The QOU-side inputs are all pinned (`m = q₀`, the coloring,
the shape); what remains is a piece of special-function geometry (the geometric quantum dilog and the
octahedral apex data) that is genuine research, not a quick evaluation. **Recommendation: pause the
`g₂` chase here** — the framework is fully documented and the remaining step is a self-contained
special-function computation a future session (or a specialist) can pick up without re-deriving
anything.

Refs: probe [`geometric_qdilog_amplitude_r_frontier_probe.py`](../../computations/deltalambda/geometric_qdilog_amplitude_r_frontier_probe.py);
#4345 (shape `= −h²` from rep); #4339 (`g₂_leading = 1`); #4315 (octahedral `e₂`);
`library/arxiv-2509.02354v2/2509.02354v2.pdf` §5.2 (geometric quantum dilog, pinched limit).
