# The residual `r ≈ 0.87%` lives in the octahedral χ-coloring frame — and the deuteron is a *torus knot* (flat octahedra)

**Date:** 2026-07-25 · **Branch:** `claude/octahedral-chi-coloring-frame-r-2026-07-25` ·
**Axis:** Δ_λ binding magnitude — the μ₀ −9% closure, residual after the bar-parity split ·
**Owner steer:** *"record the frame-narrowing; coordinate to #4158."* ·
**Tier:** structural narrowing + a solid new topological fact (scope-(a); **no fit**; nothing wired).

## 0. Where this sits

The μ₀ −9% deuteron closure has been narrowed by two convergent routes:

- **Route A — Magnus** (#4158, [`2026-07-24-eunit-magnus-order2.md`](2026-07-24-eunit-magnus-order2.md)):
  the inter-crossing Magnus tower is **dead** (deuteron word `σ₁³` is single-generator,
  `Ω_{k≥2}=0`), so the survivor is the **per-crossing** localization; the exact forward
  decomposition is `−9.21% = bar-odd t=(v−v⁻¹)/[2]_v (5.21%) ⊕ bar-even h²=(v−v⁻¹)²[2]_v² (4.37%)`.
- **Route B — octahedral** (merged #4127,
  [`2026-07-19-octahedral-four-dilogarithm-missing-tetrahedra.md`](2026-07-19-octahedral-four-dilogarithm-missing-tetrahedra.md)
  + [`FourDilogFirstOrder.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/FourDilogFirstOrder.lean)):
  each crossing = one ideal octahedron = 4 quantum dilogarithms (2509.02354); μ₀ = the
  single-tetrahedron first-order truncation; the linear order `e₁` is bar-odd, the quadratic
  order `e₂` is bar-even (`e1_bar_odd`, `e2_bar_even`, sorry-free).

The two routes **converge on the same bar-parity split** (`octahedral_barsplit_convergence_probe.py`,
5/5): linear ↔ −t (bar-odd), `e₂` ↔ h² (bar-even). `t + h² = 9.58%` vs the `9.21%` gap. The **only**
remaining open is the **bar-even `e₂` coefficient** `g₂ = (bar-even gap)/h² ≈ 1.00865`; the residual
`r = g₂ − 1 ≈ 0.008652` (0.87%) is *not* a `(v−v⁻¹)`/`[2]_v` ladder unit
([`2026-07-25-eunit-g2-derivation-attempt.md`](2026-07-25-eunit-g2-derivation-attempt.md): the
closest `h³` is bar-odd, blocked; `cosh→9/8` overshoots; Magnus→0). This note records **where `r`
actually lives** and a **new solid topological fact** that reframes it.

## 1. Solid new fact: the deuteron is a *torus knot*, so its octahedra are *flat*

The deuteron braid word is `σ₁³` (Route A). **Its closure is the trefoil `T(2,3)` — a torus knot,
not a hyperbolic knot** (SnapPy `Link(braid_closure=[1,1,1]).exterior()`):

| quantity | value | meaning |
|---|---|---|
| `volume` | **0** | non-hyperbolic (Bloch–Wigner `D(z)=0`) |
| `solution_type` | **contains flat tetrahedra** | the ideal tetrahedra are *degenerate* (real shapes) |
| shapes `z` | **{½, 2}** | **real**, and a **reciprocal pair** `z₁ = 1/z₀` |
| `π₁` | `⟨a, b ∣ a²b³⟩` | the standard `T(2,3)` torus-knot group |

This is the structural reason for the **mass/binding asymmetry** recorded in §3 of the octahedral
audit, now made exact:

- **Mass** uses `Vol(K) = Σ Im Φ_q` (the imaginary / Bloch–Wigner side). For the deuteron
  **`Vol = 0`** — the volume side literally *vanishes* because the shapes are real. Consistent: the
  deuteron contributes no hyperbolic volume.
- **Binding** `μ₀` uses the **real** phase `(q−q⁻¹) = Re Φ_q` side — the side that *survives* the
  flat degeneracy. So the μ₀ −9% closure is intrinsically a **real-shape** (degenerate-octahedron)
  computation, not a hyperbolic-volume one. The 4 dilogarithms are still present combinatorially
  (one octahedron per crossing) but their **imaginary parts are zero**; only the real (phase)
  channel carries the binding.

**Corollary (why the ladder search failed).** `r` was searched for as a `(v−v⁻¹)`/`[2]_v` power
(the algebraic ladder). But those are the *hyperbolic-deformation* units. For a **flat** octahedron
the shapes are pinned at the real reciprocal pair `{½, 2}`, and the deformation that carries `r` is
the **coloring** (boundary-parabolic holonomy) shift off the flat locus — a *different* coordinate
from the algebraic ladder. That is exactly why `r` is not in the ladder: it is a **frame**
(χ-coloring) quantity, not an algebra-ladder quantity.

## 2. The frame: a *single* shape modulus with an *exact* reciprocal partner

`2509.02354`'s positive-crossing factorization is
`R = (1/N)·Z_b·(Z_r ⊗ Z_l)·Z_t` with near-conjugate tetrahedron arguments, giving the natural
**conjugate pairing** `(Z_b, Z_t) / (Z_l, Z_r)`. For the deuteron this pairing is concrete: the flat
shapes are the **reciprocal pair** `{½, 2}`, and the bar involution `q ↦ q⁻¹` (`v ↦ 1/v`) acts on
ideal-tetrahedron shapes as **`z ↦ 1/z`** (the standard shape-parameter bar symmetry).

**Computed correction (the gluing algebra sharpens — and revises — the first pass).** The companion
probe [`deuteron_octahedral_gluing_probe.py`](../../computations/deltalambda/deuteron_octahedral_gluing_probe.py)
extracts the trefoil's rect-form gluing equations from SnapPy and finds the single edge equation
`z₀(1−z₁)/(1−z₀) = −1` is **equivalent to `z₀·z₁ = 1` identically** — satisfied by `z₁ = 1/z₀` for
*every* `z₀` along the whole 1-parameter gluing variety. So:

> **The two flat tetrahedra are EXACT bar-reciprocals, and reciprocity is *deformation-invariant* —
> the χ-coloring never breaks it.** There is *no* reciprocal asymmetry to measure.

This **revises** the naïve first-pass reading ("`r` = χ-coloring asymmetry across the reciprocal
pair"): that asymmetry is *identically zero*. The correct frame is the **single shape modulus `z₀`**
(its partner is pinned to `1/z₀`), deformed by the **meridian holonomy** through the map
`H(z₀) = z₀/(z₀−1)`, inverse `z₀ = H/(H−1)`; the complete/flat parabolic value `H = −1` gives
`z₀ = ½`. The bar-**odd** reciprocal combination `log(z₀z₁) ≡ 0` on the variety (nothing to break);
the surviving order parameter is the bar-**even** symmetric combination `s(z₀) = z₀ + 1/z₀`, flat
value `5/2`. So:

> **`r = g₂ − 1` is a bar-EVEN function of the substrate's deformation of the single modulus `z₀`**
> (the deviation of `s(z₀)` from `5/2`), driven by the coloring's meridian-holonomy `H(q₀)` — **not**
> a reciprocal asymmetry. This matches the Route-A/Route-B bar-even (`e₂ = h²`) localization: the
> whole open is one bar-even modulus deformation.

(The flat combinations are suggestive — `s = 5/2`, `z₀−1/z₀ = −3/2`, with `s² − (3/2)² = 4` — but
pattern-matching `5/2, 3/2` to observables is exactly the forbidden §2e scan; not done.)

## 3. What is (and is not) closed

| statement | status |
|---|---|
| deuteron `σ₁³` closure = trefoil `T(2,3)`, torus knot, `Vol=0`, flat shapes `{½,2}` | **solid** (SnapPy) |
| flat/real shapes ⇒ binding is the `Re Φ_q` (phase) channel; mass `Vol`-side vanishes here | **solid** (structural) |
| bar involution acts as `z ↦ 1/z`; `{½,2}` is a bar-conjugate reciprocal pair | **solid** |
| edge gluing eqn ⟺ `z₀·z₁ = 1` **identically** ⇒ the flat pair is an *exact* bar-reciprocal, deformation-invariant | **solid** (SnapPy gluing algebra) |
| ∴ `r` is **not** a reciprocal asymmetry (that is `≡ 0`); the frame is the *single* modulus `z₀`, partner `1/z₀` | **solid** (corrects the first pass) |
| `r ≈ 0.87%` is a bar-**even** function of the substrate deformation of `z₀` via the meridian holonomy `H(q₀)` (map `z₀ = H/(H−1)`) | **narrowed hypothesis** |
| the *value* `r = 0.008652` — needs the coloring `H(q₀)` map derived | **OPEN — to derive, never to fit** |

**Anti-fit (STRICT).** `r` is a ~0.4–0.9% single number; the §2e entropy bound forbids scanning
`[2]_v`/`(v−v⁻¹)` powers (or octahedral counts, or coloring parameters) for a match. Deriving `r`
requires *computing* the deuteron crossing's octahedral coloring shift forward and reading off the
reciprocal-pair asymmetry — the companion probe
[`deuteron_octahedral_gluing_probe.py`](../../computations/deltalambda/deuteron_octahedral_gluing_probe.py)
sets up that computation (SnapPy gluing data; forward; no tuning to `r`). Nothing here is wired to
production; the anti-laundering rule stands (no axiom/class carrying `r` counts as a derivation).

## 4. Coordination

- **#4158** (Route A, Magnus): this note *converges* — it names the frame the Magnus per-crossing
  survivor lives in (the flat/real octahedral coloring) and adds the solid torus-knot fact that
  explains why `Vol=0` on the binding side. Posted as a convergence comment.
- **Sibling angle-structure/normal-surface front** (beans `qou-h8yc` W9,
  [`2026-07-24-angle-structure-lp-sdp-dictionary.md`](2026-07-24-angle-structure-lp-sdp-dictionary.md);
  `qou-099h` B3, [`2026-07-25-deltalambda-normal-surface-collective-candidate.md`](2026-07-25-deltalambda-normal-surface-collective-candidate.md)):
  that front works the **Borromean** (`𝓑₃`, α-cluster, hyperbolic, 8 tetrahedra) octahedral/angle
  data. This note works the **deuteron** (trefoil, torus, flat). Distinct manifolds, shared
  machinery (ideal-triangulation gluing) — the reciprocal-pair frame here is the `Vol=0` analog of
  their positive-volume angle structures. Flagged for cross-reference.

Refs: `library/arxiv-2509.02354v2/2509.02354v2.pdf` (McPhail-Snyder–Reshetikhin, holonomy 4-dilogarithm); #4158
`2026-07-24-eunit-magnus-order2.md`; #4127 `2026-07-19-octahedral-four-dilogarithm-missing-tetrahedra.md`
+ `FourDilogFirstOrder.lean`; `2026-07-25-eunit-g2-derivation-attempt.md`;
`octahedral_barsplit_convergence_probe.py`.
