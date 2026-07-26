# g₂ leading value is exactly 1 (real coloring) — and a calibration of the #4319 quadrature carrier

**Date:** 2026-07-26 · **Branch:** `claude/trefoil-bareven-nz-modulus-g2-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, the bar-even coefficient `g₂` · **Owner steer:** *"2 1"*
(merge #4319, then compute the trefoil bar-even NZ cusp modulus) · **Tier:** exact symbolic
calibration + sharpening (scope-(a); no fit; nothing wired).

## 0. What "compute the modulus" turned up

Attempting the trefoil's bar-even NZ modulus, two exact facts sharpen the picture **and** flag a
labeling refinement I owe on the merged #4319.

## 1. Two exact facts (probe, symbolic — no fit)

- **A. The coloring is EXACT, coefficient exactly 1.** `c(m) + 1 = −(m − m⁻¹)²` *identically* (the
  difference simplifies to `0`), so at `m = q₀` it is `−(q₀−q₀⁻¹)² = −h²` with coefficient **exactly
  1** — there is **no higher-order term in the coloring**. Hence `g₂`'s coloring-level bar-even
  coefficient is `1`; the residual `r = g₂ − 1` is **not** in the coloring.
- **B. The complex-volume `u²` term is purely IMAGINARY.** For the trefoil (non-abelian A-polynomial
  branch `l = −m⁶`), `𝔙(u) = (π/2)u − (3i/4)u² + …` (`u = 2 log m`). The `u²` coefficient `−3i/4` is
  purely imaginary, so at the real substrate ray (`u` real, `φ = 0`) the complex-volume `u²` term is
  purely **bar-odd (CS)**, and its **bar-even (`Re 𝔙` / Volume) part vanishes**.

## 2. Calibration of #4319 (honest, per the corpus re-scope discipline)

PR #4319's quadrature audit (`NZBarEvenVolumeFace.lean`) schematised `g₂` as the complex-volume
Volume face `nzReVolume = (√3/2)r²·cos(2φ)`, **maximal** at `φ = 0` (vs the bar-odd CS face
`nzImVolume = sin`, frozen). Fact B shows this identification is **imprecise**: for the *trefoil* the
`Re 𝔙` (Volume) face `u²` part **vanishes** at `φ = 0` — so `Re 𝔙` is *not* `g₂`'s carrier.

**The correct carrier is the REAL coloring** `c + 1 = −h²` (bar-even, **nonzero** at the substrate,
coefficient exactly 1) — the object that drives binding via the real phase `Re Φ_q`. Refinement, not
reversal:

> **#4319's conclusion "g₂ lives where c₃ dies" STANDS** — a bar-even object *is* nonzero at the real
> substrate ray while the bar-odd CS face (`c₃`) is frozen. But the bar-even object is the **real
> coloring**, not `Re 𝔙`. The `nzReVolume` Lean is correct *abstract* quadrature; its `g₂`
> identification is corrected here to the real coloring. (The `√3/2` figure-eight modulus was flagged
> illustrative in #4319; fact B now shows why it does not transfer literally to the trefoil.)

## 3. The sharpening — and where `r` actually lives

- **`g₂` leading value = 1, exactly** (the real coloring `c + 1 = −1·h²`, an exact identity — not a
  leading term). This is the cleanest statement of "the trefoil bar-even modulus": at coloring level
  it is `1`.
- **`r = g₂ − 1 ≈ 0.00865` is entirely the shapes→`e₂` NONLINEARITY.** The coloring `c` feeds the
  octahedral shapes `z_j`; the binding bar-even coefficient is the pairwise `e₂ = Σ_{i<j} a_i a_j` of
  the shape *amplitudes*, which departs from the linear coloring term at second order. That departure
  is `r` — the `#4315` pinched-limit octahedral `e₂`. It is **not** in the coloring (exact) and
  **not** in the frozen CS phase (fact B / the `c₃` wall); it is the genuine remaining computation.

## 4. Scope (honest)

**scope-(a).** Derived: `g₂` leading `= 1` (exact, real coloring); the carrier calibration (real
coloring, not `Re 𝔙`); the localization of `r` to the shapes→`e₂` nonlinearity. **Not** derived: the
value of `r` (the pinched-limit octahedral `e₂` finite part, `#4315` — a genuine hard computation).
Anti-laundering stands: the exact facts are algebraic; no axiom/class carries `g₂` or `r`; nothing
wired.

## 5. Net across the g₂ chain (6 merged PRs + this)

deuteron = torus knot → single modulus purely bar-odd (Lean) → `g₂` is the octahedral `e₂` → trefoil
coloring one-parameter, pin corpus-fixed, scale `−h²` exact → `g₂` = cusp-shape barEven face,
converged with `c₃` → the `c₃` arg(u) wall does **not** transfer (quadrature) → **`g₂` leading `= 1`
exact (real coloring); `r` = the shapes→`e₂` nonlinearity.** The one number left (`r ≈ 0.87%`) is now
pinned to a single, well-posed, non-fishing object: the pinched-limit octahedral `e₂` finite part.

Refs: probe [`g2_leading_exact_coloring_vs_complexvol_probe.py`](../../computations/deltalambda/g2_leading_exact_coloring_vs_complexvol_probe.py);
#4319 (`NZBarEvenVolumeFace.lean`, `2026-07-26-argu-wall-quadrature-g2-bareven-volume-face.md`);
#4315 (pinched-limit octahedral `e₂`); `TrefoilColoringBarEven.lean` (`c+1 = −(m−1/m)²`, exact).
