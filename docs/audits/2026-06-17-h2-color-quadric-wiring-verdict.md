# h₂ Hermitian color quadric — wiring verdict

**Date:** 2026-06-17
**Type:** Read-only wiring investigation (no compute / content edited).
**Question:** Should the h₂ Hermitian color quadric be wired into compute, or
is it recoverable from already-wired quantities / intentionally narrative-only?

## Verdict: **(C) NARRATIVE-ONLY BY DESIGN — correctly unwired.**

h₂ is a **C₅-equivariant Galois organizing invariant on the Bring quintic
resolvents** (geometry), not a binding/energy input on the Hecke Markov trace.
It is a *defining constraint of the color-tube variety*, not a number that any
mass/binding formula evaluates. It is **not** the C₅-symmetrised version of the
wired Hopf-link L± cross-color terms — those live on a different object (the
H₃(q) Hecke algebra). No new compute is warranted.

---

## Evidence chain

### 1. What h₂ is for — a *constraint defining the color-tube variety* (option (c))

`h₂(c) = σ·c_b + c_r·c_g` is defined in
[`aggregate-color-quantities.md`](../../content/quantum-observable-universe/brings-surface/aggregate-color-quantities.md) L9-10,
as one of a family of **C₅-equivariant aggregate quantities** in the color-tube
coordinates (σ, c_r, c_g, c_b):

- `p₁(c) = σ + c_r + c_g + c_b` (first power sum, L6),
- `h₂(c) = σ c_b + c_r c_g` (Hermitian quadric, L9),
- `χ_ζ(c) = ζ⁻¹σ + ζ⁻²c_r + ζ⁻³c_g + ζ⁻⁴c_b` (C₅ character, L12),
- `h₃(c) = σ²c_g + c_b²c_r + c_r²σ + c_g²c_b` (Hermitian cubic, L15).

The text states (L21-25) the subscript on h_k denotes the **degree of the
C₅-equivariant invariant**: "h₂ pairs conjugate resolvents (w_k with w_{5−k})
and h₃ pairs squared resolvents in the skip-one pattern. The character χ_ζ is
the ζ-weighted sum — the Fourier dual of p₁." These are organizing invariants of
the cyclic Galois action.

They feed the resolvent-shift relations (L27-44):
`S = p₁(c) + 4z`, `D = χ_ζ(c) − z`, `z = S/D` (using ∑ζ⁻ᵏ = −1).

h₂ then appears **as a constraint defining the variety**, in
[`color-tube-constraints.md`](../../content/quantum-observable-universe/brings-surface/color-tube-constraints.md):

- Shifted quadric (L20-26): `h₂(c) + z·p₁(c) + 2z² = 0`, i.e. `σb + rg = −z(σ+r+g+b) − 2z²`.
- Shifted cubic (L31-36): `h₃(c) + z(p₁(c)² − 2h₂(c)) + 3z²p₁(c) + 4z³ = 0`.
- Reduced cubic (L41-45) eliminates h₂ entirely: `h₃(c) + z·p₁(c)² + 5z²p₁(c) + 8z³ = 0`.

L47-49: "All three equations are polynomial over ℤ in z, r, g, b, σ; they
therefore define affine varieties over ℤ." So h₂ is a **defining equation of the
color-tube variety**, not a scalar observable. It is *eliminable* (the reduced
cubic removes it). Both `aggregate-color-quantities` and
`intrinsic-color-cubic-pairing` are **`remark` blocks** that
`interprets: "def:color-tube-coordinates"` — interpretive, no logical claim,
no Lean.

### 2. The color coordinates (σ, c_r, c_g, c_b) — never numerically realized as the quadric

The coordinates are *Lagrange resolvents of the Bring quintic*:
`c_r = w₂ − z, c_g = w₃ − z, c_b = w₄ − z`, `σ = w₁ − z`
([`color-tube-coordinates.md`](../../content/quantum-observable-universe/brings-surface/color-tube-coordinates.md) L7-13).

The one script that *does* numerically realize "the three color sheets" is
[`flavor_dependent_cusp_shape.py`](../../computations/flavor_dependent_cusp_shape.py):
it solves the **color-tube cubic** `c³+(4z+1)c²+(6z²+3z+1)c+(4z³+3z²+2z+1)=0`
at fixed z=q₀ (L86-97, matching `def:color-tube-cubic` Vieta data), getting roots
`{c_real, c_+, c_−}` = the three sheets (L157-171). But what it evaluates on those
roots is the **Bloch–Wigner dilog D(c)** (L82-83, 173-179) as a candidate
flavor-split mechanism — **not h₂**. A grep of the entire compute tree for the
quadric `σ·c_b + c_r·c_g` (or `h_2` / "hermitian quadric") returns **zero hits in
any binding/mass script**. (The many `h2`/`h_2` compute hits are all the
ℏ_q²-power expansion `h^k`, e.g. `yekutieli_*_h2_extraction.py`, or molecular
LP-binding — an unrelated symbol collision.)

The other "Bring color-tube" probe,
[`probe_k_ud_bring_color_tube_empirical_baseline.py`](../../computations/probe_k_ud_bring_color_tube_empirical_baseline.py),
uses a *different* "color-tube weight" `1/(1 − h_q·q^{10+k})` (L75-84) — the
genus-class exponent ladder, explicitly EXPLORATORY/AUDIT-ONLY (L1-8, set_audit_only
L195) — also not the (σ,c_r,c_g,c_b) quadric.

**Conclusion:** the color-tube coordinates are numerically realized (as cubic
roots), but the *quadric h₂ on them* is never evaluated, and the realization that
exists feeds a dilog probe, not a production binding formula.

### 3. h₂ is NOT recoverable from / the same as the wired L± + Gram — they are different objects

The audit hypothesis (h₂ = C₅-symmetrised version of the Hopf-link L± terms) is
**refuted**. The L± cross-color terms wired in
[`knot-basis-color-content.md`](../../content/quantum-observable-universe/brings-surface/knot-basis-color-content.md)
are products of **independent formal Hecke variables φ_i, ψ_j** in **H₃(q)**:

- L₊ = σ₀σ₁ coefficient = `φ₀ψ₁`; L₋ = σ₁σ₀ coefficient = `φ₁ψ₀` (L67-68).
- These are the word-length-2 NF entries of a Gröbner–Shirshov product of two
  "photons with color content" `γ = 𝟏 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁` in the Iwahori–
  Hecke algebra (L1-22, L85-90: "cross-color products").
- σ₀, σ₁ are the **color axes**; the variables are independent (L95-97).

This is a quadratic in *Hecke generator coefficients* over `ℤ[q^{±1}]`. h₂ is a
quadratic in *Bring quintic resolvent coordinates* over `ℤ[z]`. They are
quadratics on **structurally distinct objects**:

| | h₂ (Bring quadric) | L± (Hopf cross-color) |
|---|---|---|
| object | Lagrange resolvents of Bring quintic | H₃(q) Hecke algebra |
| variables | σ, c_r, c_g, c_b = w_k − z (geometry) | φ_i, ψ_j formal Hecke coeffs |
| ring | ℤ[z] | ℤ[q^{±1}] |
| role | defining constraint of color-tube variety (eliminable) | NF coefficients of a trace-algebra product |
| symmetry | C₅ Galois grading | S₃ color-axis grading in H₃ |

The [`2026-06-16-mass-trace-phase-c5-vs-u1.md`](2026-06-16-mass-trace-phase-c5-vs-u1.md)
audit settled exactly this distinction (its claim #2, L59-75): "The C₅ ζ-action
is **never applied to the Markov trace / Jones polynomial** anywhere in the
corpus. Color is a grading on the *Bring geometry*; mass-modulus is on the *Hecke
Markov trace*. Different objects." Its refinement section (L116-159) clarifies
that color *does* live on the trace algebra **as an S₃ discrete grading on
(φ₀,φ₁,φ₀₁)** — i.e. the L± content — but that this S₃ grading and the C₅ Bring
resolvent grading meet only one level up, at S₂×S₃ ⊂ S₅. So h₂ and L± are not the
same quadratic in two bases; there is no change-of-basis identity to document.

### 4. No mass/binding formula references h₂ or the Bring color quadric

Grep of `content/` + `computations/` for the quadric `σ·c_b + c_r·c_g` feeding
any mass/binding compute: **zero hits**. The only consumer of the quadric is the
geometric constraint chain in `color-tube-constraints.md` (spacetime recovery /
shifted quadric / shifted cubic), which is Bring's-surface variety geometry. The
trace-algebra color-grading block
[`mass-modulus-em-phase-color-grading.md`](../../content/quantum-observable-universe/mass-endomorphism/mass-modulus-em-phase-color-grading.md)
L4 references `H₂(q)⊕H₃(q)` and the σ₀/σ₁ color axes — the L± content — and never
the h₂ Bring quadric.

---

## Why correctly unwired (the design rationale)

1. **h₂ is a defining constraint of a variety, not an observable.** The mass/
   binding pipeline evaluates the *Hecke Markov trace* `tr_M(ρ(β))` and its
   Wedderburn/Frobenius decomposition. h₂ lives on the orthogonal Bring-geometry
   leg (the C₅ Galois substrate), where its job is to cut out the color-tube
   variety inside ℙ¹(ℂ)×𝔸³. It is even *eliminable* (the reduced cubic removes
   it). There is nothing to "wire into binding."

2. **The genuine color-on-trace content is already wired — as L±, not h₂.** The
   cross-color Hopf dressing that *does* feed the trace algebra is the
   φ₀ψ₁/φ₁ψ₀ L± content (`knot-basis-color-content.md`, pyhecke gram), and it is
   wired. h₂ is the Bring-geometry partner of the χ_ζ Galois grading, a different
   object; importing it into binding would conflate the two legs the
   2026-06-16 audit explicitly kept separate.

3. **The only numerical realization of the sheets feeds a dilog probe, not h₂.**
   `flavor_dependent_cusp_shape.py` realizes the three color sheets and evaluates
   D(c) on them (an exploratory flavor-split mechanism), confirming the geometry
   is computable when needed — but the quadric h₂ itself is never the thing
   evaluated, because it is a constraint, not a scalar the framework predicts.

## Recommendation

No new compute. If documentation clarity is wanted, the single eliminable line
"h₂ is a C₅-Galois defining invariant of the color-tube variety (eliminated by
the reduced cubic), not a binding input; the color content that reaches the trace
algebra is the L± Hopf dressing (`knot-basis-color-content`)" could be added to
the `aggregate-color-quantities` block prose — but the current state is already
correct, and that note partly duplicates the 2026-06-16 audit. Treat the
"one unwired quadratic" finding as **explained, not actionable**.
