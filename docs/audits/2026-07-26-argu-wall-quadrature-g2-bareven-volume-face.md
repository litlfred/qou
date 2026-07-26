# The arg(u) wall is a quadrature effect: the bar-even Volume face (g₂) is maximal where the bar-odd CS face (c₃) freezes

**Date:** 2026-07-26 · **Branch:** `claude/trefoil-pinched-limit-e2-g2-2026-07-26` (PR #4319) ·
**Axis:** Δ_λ binding — μ₀ −9% closure, `g₂` vs the Q_β `c₃` arg(u) wall · **Owner steer:** *"Push"*
(into the arg(u) phase, joint c₃/g₂ attack) · **Tier:** structural (Lean-exact) + measurement
(scope-(a); no fit; nothing wired).

## 0. The joint-attack question

The μ₀ bar-even `g₂` and the Q_β bar-odd `c₃` reduce to the two bar-parity faces of one
Neumann–Zagier meridian-deformation object (PR #4319 §4). The `c₃` front (PR #4293) concluded its
front on a **wall**: the anchor swing lives only in the non-perturbative phase `arg(u)`, and the
substrate freezes it. Does that same wall block `g₂`? Corpus-grep first (the wall is real and
recent); then the honest question — does it *transfer* to the bar-even side?

## 1. The c₃ wall (corpus, proved)

[`QOU/QBeta/ArgUPhaseBranchSelection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ArgUPhaseBranchSelection.lean)
(#4293, sorry-free): the NZ **bar-odd / Chern–Simons** face is

  `nzImVolume r φ = (√3/2)·r²·sin(2φ)`,  `r = |u|`, `φ = arg u`,

and `nzImVolume_real_ray`: `nzImVolume r 0 = 0`. The substrate meridian coordinate `u = 2·log q₀` is
a **nonnegative real** (`φ = 0`), so the CS face is **frozen** — `sin(2·0) = 0`. Combined with #4288
(the magnitude `|u|²` is anchor-smooth), `c₃`'s percent swing has nowhere to sit: the wall.

## 2. The result — g₂ is the cos-quadrature partner, MAXIMAL on the real ray

`g₂` is the NZ **bar-even / Volume** face — the **cos-quadrature partner** of `nzImVolume`:

  `nzReVolume r φ = (√3/2)·r²·cos(2φ)`.

Formalized sorry-free
([`QOU/MassTheory/NZBarEvenVolumeFace.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/NZBarEvenVolumeFace.lean),
`lean`-direct exit 0):

- **`nzReVolume_real_ray`**: `nzReVolume r 0 = (√3/2)·r²` — on the *same* real ray `φ=0`, `cos 0 = 1`,
  so the bar-even face is at its **peak**, not zero.
- **`nzReVolume_real_ray_ne_zero` / `_pos`**: `r ≠ 0 ⟹ nzReVolume r 0 > 0` — **not frozen**, the
  structural opposite of the CS face.
- **`nzReVolume_phase_even`**: `nzReVolume r (−φ) = nzReVolume r φ` — the bar-even face is **even** in
  `φ` (`cos`), so `φ = 0` is a **stationary extremum** (zero phase-slope); the bar-odd face is *odd*
  (`sin`), so `φ = 0` is its *steepest* point (value 0, maximal slope).

Probe [`nz_bareven_volume_face_probe.py`](../../computations/deltalambda/nz_bareven_volume_face_probe.py)
(3/3): at `φ=0`, `nzIm = 0` (c₃ frozen), `nzRe = (√3/2)r²` (g₂ peak); Pythagorean
`nzRe² + nzIm² = (3/4)r⁴` puts **all** the NZ quadratic in the bar-even face at the substrate; phase
slopes `d(nzIm)/dφ|₀ = √3 r²` (max) vs `d(nzRe)/dφ|₀ = 0` (stationary).

## 3. Verdict — g₂ lives where c₃ dies; the wall does not transfer

> **The arg(u) wall is a *quadrature* effect.** The real substrate ray `φ = 0` is exactly the point
> where the CS face (`c₃`) is **null** and the Volume face (`g₂`) is at its **peak**. The wall that
> freezes `c₃` **leaves `g₂` maximal and doubly anchor-smooth** (magnitude `r²` smooth per #4288 *and*
> phase-stationary). `g₂` does **not** inherit the c₃ wall.

**This corrects** the earlier-draft pessimism (PR #4319, a prior commit) that put `r` in the same
frozen phase as `c₃`. The two are in *quadrature*, not the same channel. Consequently `g₂` is a
well-defined geometric coefficient — the **trefoil's bar-even NZ (Volume-face) cusp modulus** — with
leading value `1` (the coloring `c+1 = −1·h²`, #4319); `r = g₂ − 1` is how far that modulus sits from
`1`, a definite computable number, **not** a frozen-phase or non-perturbative-swing quantity.

## 4. Scope (honest)

**scope-(a).** Proved: the quadrature structure — the bar-even face is maximal/stationary on the real
ray where the bar-odd is frozen. **Not** derived: `g₂`'s value / `r` (that is the trefoil bar-even NZ
modulus; the `√3/2` here is the figure-eight cusp modulus, illustrative of the *form* only — the
trefoil's own modulus is `g₂`'s leading value). Anti-laundering stands: the Lean proves the
quadrature/parity structure, not `g₂`. Nothing wired.

## 5. Next

Compute the **trefoil's** bar-even NZ Volume-face cusp modulus (the `nzReVolume` coefficient for the
trefoil, not the figure-eight `√3/2`) at the substrate `r = |u| = barOdd(q₀)`. It is a definite,
anchor-smooth, phase-stationary geometric number — the leading `g₂` — with `r = g₂ − 1` the
sub-leading (NZ `u⁴`) correction. This is now a well-posed cusp-geometry computation, *not* a
non-perturbative phase problem.

Refs: [`NZBarEvenVolumeFace.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/NZBarEvenVolumeFace.lean);
probe [`nz_bareven_volume_face_probe.py`](../../computations/deltalambda/nz_bareven_volume_face_probe.py);
c₃ wall [`ArgUPhaseBranchSelection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ArgUPhaseBranchSelection.lean)
+ [`2026-07-25-argu-phase-branch-selection.md`](2026-07-25-argu-phase-branch-selection.md);
PR #4319 (`2026-07-26-trefoil-coloring-pinned-bareven-scale-h2.md`); #4288 (magnitude smooth).
