# The deuteron trefoil coloring is one-parameter (anti-fishing resolved) and deviates from flat by an exact bar-even `−(m−1/m)² = −h²`

**Date:** 2026-07-26 · **Branch:** `claude/trefoil-pinched-limit-e2-g2-2026-07-26` ·
**Axis:** Δ_λ binding — the μ₀ −9% closure, the pinched-limit `e₂`/`g₂` computation ·
**Owner steer:** *"3"* (bank the narrowing, then attempt the pinched-limit compute fresh) ·
**Tier:** representation solve + an exact bar-even identity + honest scope (scope-(a); **no fit to
g₂**; nothing wired).

## 0. Where this sits

#4315 (merged) reduced `g₂` to *"the octahedral `e₂` finite part in the pinched limit"*, with the
wall *"solve the trefoil coloring and pin all DOF, or the residual freedom is the wall."* This note
attacks that wall directly and removes its anti-fishing branch.

## 1. The trefoil coloring is one-parameter — fully substrate-pinned

The deuteron `σ₁³` = trefoil `⟨u,v | uvu = vuv⟩`. Its irreducible `SL₂(ℂ)` representations form a
**one-parameter** family. Writing `ρ(u) = [[m,1],[0,m⁻¹]]`, `ρ(v) = [[m,0],[c,m⁻¹]]` (meridian
eigenvalue `m`, parabolic `m=1`), the braid relation `uvu = vuv` **forces the off-diagonal coloring**

  `c(m) = −(m⁴ − m² + 1)/m²`.

Cross-checks (probe, 3/3):

- **Reducibility ⟺ Alexander polynomial.** `c(m) = 0 ⟺ m⁴ − m² + 1 = 0 ⟺ m² = e^{±iπ/3}` — exactly
  the roots of the trefoil Alexander polynomial `Δ(t) = t² − t + 1`. The rep is correct.
- **Parabolic `m = 1 ⟹ c = −1`** — the flat/pinched rep (the degenerate torus-knot structure of
  PR #4301).

Because the substrate pins the **single** knob `m ↔ q₀`, the coloring has **no residual freedom**.
This is the key anti-fishing result:

> **The downstream `e₂`/`g₂` is a *forward number*, not a scan.** #4315's wall had two branches —
> "residual coloring freedom" (⇒ fishing hazard) vs "mechanical rep→shape computation." This closes
> the first branch: there is no residual freedom to tune.

## 2. The coloring deviation is an exact bar-even square = `−h²` at `m = q₀`

**Exact identity** (probe + Lean `trefoilColoring_add_one`, generic field):

  `c(m) + 1 = −(m − m⁻¹)²`.

`m − m⁻¹` is bar-**odd** (`m ↦ m⁻¹` negates it), so the deviation from the flat value `−1` is
bar-**even** — the parity of the `g₂` correction. At the substrate pins:

| pin | `c(m) + 1 = −(m − m⁻¹)²` |
|---|---|
| `m = q₀` (quantum meridian) | `−(q₀ − q₀⁻¹)² = −h²` **exactly** (the #4158 bar-even gap, `h = q − q⁻¹`) |
| `m = √q₀` (`v`-level) | `−(v − v⁻¹)² = −h²/[2]_v²` |
| `m = 1` (flat) | `0` |

So the trefoil coloring's bar-even deviation is **exactly `−h²`** at the quantum-meridian pin — an
*exact identity*, not a fit. This **identifies the bar-even scale of the closure as `h²`**,
independently reproducing the scale the #4158 Magnus route found empirically.

## 3. Honest scope (anti-fishing, STRICT)

Three disciplined caveats — this is a **lead**, not a closure:

1. **Scale, not coefficient.** The identity gives the bar-even *scale* `h²`. The *coefficient*
   `g₂ ≈ 1.0087` is the `e₂` finite part in the pinched limit (#4315), **still to compute**. `c(m)`
   is the representation's coloring parameter feeding the shapes `z_j`; it is not `e₂` itself.
2. **The pin's power is open.** `m = q₀` gives `−h²`; `m = √q₀` gives `−(v−v⁻¹)²`. Which power is the
   substrate's meridian is set by the quantum-group coloring convention and must be justified
   **independently** — choosing `m = q₀` *because* it lands on `h²` would be the forbidden §2e fit.
   Flagged **open**, not claimed.
3. **Anti-laundering.** The Lean proves the *algebraic identity* `c+1 = −(m−1/m)²`, not `g₂`. Nothing
   is wired to production.

## 4. Net progress and next

**Net:** the #4315 wall's *anti-fishing* branch is resolved (the coloring is one-parameter, fully
pinned — no freedom to tune), and the bar-even scale is *exactly* `h²` at the quantum-meridian pin.
What remains for `g₂` is purely the **mechanical, non-fishing** computation: map the pinned rep
`ρ(m=q₀)` to the four octahedral shapes `z_{r,t,l,b}` (cross-ratios of the developing map,
2509.02354 eq 4.11–4.14) and evaluate the bar-even `e₂` finite part in the pinched limit — plus the
independent justification of the pin's power. No coloring can be tuned; `g₂` either emerges as a
forward number or the pinched-limit regularization is exposed as the true (technical, not fishing)
obstruction.

Refs: probe [`trefoil_coloring_pinned_bareven_probe.py`](../../computations/deltalambda/trefoil_coloring_pinned_bareven_probe.py);
Lean [`TrefoilColoringBarEven.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TrefoilColoringBarEven.lean);
#4315 (`2026-07-26-octahedral-e2-coloring-quadratic-pinched-wall.md`); #4309, #4301; #4158 (`h²` gap);
`uploads/2509.02354v2.pdf`.
