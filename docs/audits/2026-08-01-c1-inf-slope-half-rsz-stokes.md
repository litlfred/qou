# C1's ∞ slope-½ singularity → RSZ q-Borel resolution + Stokes data (2026-08-01)

**Branch:** `claude/c3-w2-inf-stokes-2026-08-01`. **Feeds:** W2 (bean `qou-xufp`), the
Birkhoff-matrix ∞-side of the C1 module. **Analysis + literature mapping — grounds the ∞
residual in RSZ; no closure. One Lean building block landed (`QBorelKernel`).**

## The residual, precisely

The W2 witnesses (merged #4461) established: the C1 module `L1 = (q²x−1)σ² − (q−1)σ − (q−1)`
is **Fuchsian at 0** (exponents = roots of `t²+(q−1)t+(q−1)`) but **irregular at ∞**, Newton
polygon slope **½** (single edge `(2,0)→(0,1)`, re-confirmed from the companion). The
Fuchsian (integral-slope) connection-matrix recipe — read from the Di Vizio–Ramis–Sauloy–Zhang
survey (`library/equations-aux-q-differences/Equations_aux_q-differences.pdf`) — gives the 0-side canonical solution; the
∞-side needs the wild (q-Gevrey/Stokes) theory. This doc maps that ∞ residual to the
Ramis–Sauloy–Zhang Astérisque 355 (`library/arxiv-0903.0853v3/0903.0853v3.pdf`); the two are distinct sources.

## What RSZ §3.3 gives (p. 39)

A singularity of **level `d`** (here slope ½ ⇒ `d = 2`, the denominator of the slope) is
resolved by the **q-Borel transform**

  `B_{q,d}(∑ fₙ zⁿ) = ∑ (fₙ / tₙ) ξⁿ`,   kernel `(tₙ)` with `tₙ = q^{n−d}·t_{n−d}`, growth `q^{n²/2d}`.

- **Level `d = 1`:** canonical kernel `tₙ = q^{n(n−1)/2}` (Jacobi theta coefficient). ← **formalized here** (`QBorelKernel`, `qBorelKernel_succ : t_{n+1}=q^n·tₙ`).
- **Level `d = 2` (C1's slope ½):** the family is built from Jacobi theta functions and one
  must choose **square roots `B₁,B₂` of `A₁,A₂`** (the ramification intrinsic to a
  non-integral slope). After the q-Borel/ramified transform the slope becomes integral.
- **Stokes data:** the isoformal analytic classes form `F(P₁,P₂) ≅ Matr_{r₁,r₂}(ℂ)^d`
  (RSZ §3.3, Birkhoff–Guenther normal form). For C1 (`r₁=r₂=1`, `d=2`) this is `ℂ²` — **two
  Stokes multipliers**. These are the wild part of the ∞ connection datum, theta-valued via
  the `tₙ` kernel.

## The honest map

| C1 datum | RSZ object | status |
|---|---|---|
| ∞ slope ½ | level `d = 2` singularity | witness-confirmed |
| resolving transform | q-Borel `B_{q,2}`, theta kernel `tₙ` | kernel (`d=1`) formalized (`QBorelKernel`) |
| ramification | square roots `B₁,B₂` of the leading blocks | **open** (compute the `A_i`) |
| Stokes data | `F(P₁,P₂) ≅ ℂ²` — two multipliers `U ∈ ℂ²` | **open** (the RSZ-wild residual) |
| why theta-valued | ratio of same-multiplier q-characters is elliptic | proved (`QCharacter.ratio_qInvariant`) |

## Residual (beaned `qou-xufp`) — genuinely multi-session

Computing the two Stokes multipliers `U ∈ ℂ²` for C1 requires: (i) the level-2 ramified
q-Borel transform with the theta family; (ii) the `d`-th roots `B₁,B₂` of the slope blocks;
(iii) the cohomological/normal-form extraction of `U` (RSZ §4–5, Birkhoff–Malgrange–Sibuya
q-analog). This is RSZ-wild-theory-level work, not a session brick. What landed: the
level-1 q-Borel kernel (`QBorelKernel`) and the ellipticity source (`QCharacter`) — the two
concrete building blocks. No fit; nothing wired; no `symbol=C1` claim.

-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (§3.3 q-Borel, §4 Stokes)
-- Ref: [manuscript] docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md (C1 = L1, slope ½)
