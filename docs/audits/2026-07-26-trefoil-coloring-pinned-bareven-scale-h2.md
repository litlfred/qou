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
2. **The pin's power is now RESOLVED — corpus-justified, not fished (update).** The convention is
   authoritative in the corpus: [`meridian-holonomy-boost.md`](../../content/quantum-observable-universe/braids-and-knots/meridian-holonomy-boost.md)
   — *"the meridian holonomy of the cusp torus is multiplication by the substrate parameter `q`"* —
   with the boost identity `barEven(q)² − barOdd(q)² = 4`, `barEven(q) = q+q⁻¹` (the meridian trace),
   `barOdd(q) = q−q⁻¹`, formalized sorry-free (`holonomy_hyperbola`, `barEven_mul`, `barOdd_mul`). A
   meridian holonomy with trace `q+q⁻¹` has eigenvalue **`m = q₀`** — *not* `√q₀`. So `c(q₀)+1 =
   −(q₀−q₀⁻¹)² = −barOdd(q₀)² = −h²` is the corpus convention, fixed **independently** of the h²
   match. Sibling PR #4288 (meridian-holonomy `c₃` anchor) uses the *same* `barOdd(q)=q−q⁻¹`
   deformation (for the bar-**odd** `c₃`); my `−barOdd(q)²` is exactly its NZ-quadratic observable
   `S ∝ u²` (`u = 2 log q₀ ≈ q−q⁻¹`), read on the bar-**even** side. The pin is not a free choice.
3. **Anti-laundering.** The Lean proves the *algebraic identity* `c+1 = −(m−1/m)²`, not `g₂`. Nothing
   is wired to production.

## 4. Piece (2): `g₂` reduces to the bar-EVEN face of the trefoil's cusp-shape — converging with the `c₃` front

The bar-even scale `−h² = −barOdd(q₀)²` is not an isolated fact — it is the trefoil-deformation
instance of the corpus **cusp-shape bar-parity** object
([`cusp-shape-bar-parity.md`](../../content/quantum-observable-universe/braids-and-knots/cusp-shape-bar-parity.md),
Lean `cusp_barParity_split`, sorry-free). That block splits a cusp shape `x` along the bar-involution
into a **barEven (Volume) face** and a **barOdd (CS) face**; for the figure-eight `4₁` (`ω = e^{iπ/3}`)
it gives `barEven(ω) = 1` (the Volume normalization `2cos(π/3)`) and `barOdd(ω)² = −3` (the `√−3`
Chern–Simons modulus). My trefoil result `c(q₀)+1 = −barOdd(q₀)² = −h²` is the **`q₀`-deformed analog
of the `4₁` `barOdd² = −3`** — the squared-CS-modulus (bar-even) face.

This yields the reduction and a convergence:

- **`g₂` (bar-even) is the barEven / squared-CS face of the deformed trefoil's cusp shape.** Sibling
  PR #4288's `c₃` (bar-**odd**) is the barOdd / CS face of the **same** Neumann–Zagier cusp-shape
  object (`CVol(u) = Vol − (τ/4)u² + …`, `u = 2 log q₀ ≈ q−q⁻¹`). So the μ₀ **bar-even** closure
  (`g₂`) and the Q_β **bar-odd** anchor (`c₃`) reduce to the **two bar-parity faces of one object** —
  the deformed-trefoil cusp shape / meridian-holonomy. Independent fronts, one open link.
- **The natural coefficient is `1`.** The coloring deviation is `c+1 = −1·h²` (coefficient *exactly*
  1); `g₂ ≈ 1.0087 = 1 + r`, `r ≈ 0.0087`. This *suggests* the leading bar-even coefficient is `1`
  with `r` the higher-order (NZ `u⁴` / `e₂` cross-term) residual — but note the caveat: `c(q₀)` is the
  representation's coloring parameter, and deriving that the binding **`e₂` inherits coefficient
  exactly 1** still requires the shapes → `e₂` map. Stated as a lead, not a claim.

## 5. Net and next

**Net (this PR):** (i) the coloring is one-parameter, fully substrate-pinned — the #4315 anti-fishing
branch is closed; (ii) the pin `m = q₀` is corpus-authoritative (meridian holonomy = multiplication
by `q`), not fished; (iii) the bar-even scale is *exactly* `−h² = −barOdd(q₀)²`; (iv) `g₂` reduces to
the **barEven face of the trefoil's cusp shape**, converging with the sibling `c₃` bar-odd front on
one Neumann–Zagier object.

**Next:** the coefficient `g₂` (and `r`) is the trefoil's deformed cusp-shape barEven face / the `e₂`
finite part — the open `CuspShapeBarParity` link for a *torus* knot (`Vol = 0` makes the Volume face
subtle), the same object the `c₃` front is blocked on. Deriving it is a genuine (technical, not
fishing) obstruction; the two closures should be attacked together.

**Where `r` lives — the arg(u) wall is a QUADRATURE effect (corrected; PR #4319 follow-up commit).**
The `c₃` front proved (PR #4293) the NZ **bar-odd / CS** face `nzImVolume = (√3/2)r²·sin(2φ)` is
**frozen on the real substrate ray** `φ=0` (`sin 0 = 0`) — that is the c₃ wall. But `g₂` is the
**bar-even / Volume** face, the **cos-quadrature partner** `nzReVolume = (√3/2)r²·cos(2φ)`, which at
the *same* `φ=0` is `(√3/2)r²` — **maximal, not frozen** — and *even* in `φ`, so `φ=0` is a
*stationary extremum* (zero phase-slope: doubly anchor-smooth). Formalized sorry-free
([`NZBarEvenVolumeFace.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/NZBarEvenVolumeFace.lean):
`nzReVolume_real_ray`, `_ne_zero`, `_pos`, `nzReVolume_phase_even`). So **the wall that freezes `c₃`
leaves `g₂` maximal and stable — `g₂` lives exactly where `c₃` dies.** (This *corrects* an earlier
draft of this paragraph that put `r` in the same frozen phase as `c₃`; the two are in *quadrature*,
not the same channel.) Consequence: `g₂` is a well-defined, anchor-smooth, phase-stationary
coefficient — the **trefoil's bar-even NZ (Volume-face) cusp modulus** — with leading value `1` (the
coloring `c+1 = −1·h²`); `r = g₂ − 1` is simply how far that geometric modulus sits from `1`, a
definite computable number, *not* a frozen-phase quantity. The μ₀ bar-even and Q_β bar-odd closures
are the two quadrature faces of one NZ object; the real substrate ray is exactly where CS (`c₃`) is
null and Volume (`g₂`) peaks.

Refs: probe [`trefoil_coloring_pinned_bareven_probe.py`](../../computations/deltalambda/trefoil_coloring_pinned_bareven_probe.py);
Lean [`TrefoilColoringBarEven.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TrefoilColoringBarEven.lean);
#4315 (`2026-07-26-octahedral-e2-coloring-quadratic-pinched-wall.md`); #4309, #4301; #4158 (`h²` gap);
`library/arxiv-2509.02354v2/2509.02354v2.pdf`.
