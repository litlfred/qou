# Coordination — Δ_λ magnitude derivation (hibinv + hratio + SP2 + Stokes-3)

**Date:** 2026-07-27 · **Branch:** `claude/delta-lambda-magnitude-derivation-2026-07-27`
**Milestone bean:** `qou-ksxr`

## Notation (2026-07-27, owner directive: avoid collision with substrate u = b·ℏ_q²)

| Symbol | Meaning |
|--------|--------|
| `𝔲_K(q₀) = ln q₀ + i·ϑ_K(q₀)` | Full Neumann-Zagier deformation parameter on the character variety of knot K, at substrate q₀ |
| `ln q₀` | Real/boost part of `𝔲_K` (proved, meridian holonomy, knot-independent) |
| `ϑ_K(q₀)` | Angular/spin part of `𝔲_K` (open, knot-dependent — different particles = different ϑ) |
| `u = b·ℏ_q²` | Substrate ladder quantity (existing, NOT the same as `𝔲_K`) |
| `A_ω = 3` | GGM Stokes constant for 4₁ (integer, literature-proved) |

**Key distinction:** `ϑ_K` depends on the **knot** K (= the particle). Different particles (= different braid closures) trace different curves on the character variety, so their angular deformation differs. The boost `ln q₀` is universal (meridian holonomy); the spin `ϑ_K` is the particle-specific datum.

## Goal

Derive (or honestly bound / gap-document) the magnitude of Δ_λ through the
chain: braid word → cusp-torus closed geodesic → integer winding (m,ℓ) →
meridian log-holonomy → alien-calculus Stokes constant → |S| → |Δ_λ|.

Two proved inputs already in hand:
- Meridian holonomy Re 𝔲_K = ln q₀ (sorry-free, `meridian-holonomy-boost.md`)
- Im 𝔙₄₁(u) = (√3/4)(Re²u − Im²u) (proved `imV₄₁`)

## Workplan (5 tasks, strict Lean discipline)

### T1 — `hibinv` (bean `qou-rp5f`)
**Prove i/b-periodicity of Ψ/Φ ratio everywhere.**

Current state: `ratio_ibinv_periodic` in `CyclicDilogPentagon.lean` proves
periodicity off the dual pole lattice. Extending to all of ℂ needs the
**identity theorem**: a continuous function periodic on a dense set is periodic
everywhere — which `QOU.Common.periodic_of_continuous_of_eqOn_dense` already
provides. The gap is: (a) the ratio Ψ/Φ is continuous (requires entireness
from T2), (b) the complement of the dual pole lattice is dense (a discreteness
fact about the `1/b`-lattice).

**Honest assessment:** T1 and T2 are coupled — hibinv needs the ratio to be
continuous, which requires it to be entire (T2's hratio). Clean ordering is
T2 first, T1 second. If T2 is open, T1 stays open. Will attempt both and
report the dependency honestly.

### T2 — `hratio` (bean `qou-cons`)
**Prove entireness of Ψ/Φ ratio (divisor cancellation).**

The hard open input. Two FaddeevPhi solutions at the same `b` are meromorphic;
`MeromorphicSameOrder.lean` proves their order-difference is doubly periodic
(so the ratio is elliptic). Entireness requires: the two solutions share the
same zero/pole lattice (divisor cancellation ⇒ ratio has only removable
singularities ⇒ entire).

**Honest assessment:** This is the genuine mathematical content. The physical
`Φ_b` (Faddeev's contour integral) has a specific pole structure (simple poles
at `z = −ib(n+½) − i(m+½)/b` for n,m ∈ ℤ≥0). Two solutions at the same `b`
share this lattice by the contour-integral representation. But formalizing this
requires either (a) a Lean-level contour-integral construction of `Φ_b` (not
available — `FaddeevPhi` axiomatizes only the q-difference equations), or (b) a
purely algebraic divisor argument from the difference equations. Route (b) is
the only tractable one; it requires showing the q-difference equations pin the
pole locations. **This may not close in one session.** If it doesn't: bean the
gap with the precise remaining statement.

### T3 — SP2 probe (bean `qou-gjs2`)
**Identify the geometric mechanism for the hypersensitive spin part.**

The spin-part derivation branch (`claude/udeform-spin-part-derivation-2026-07-27`)
established:
- Smooth geometric candidates (boost + fibre holonomy) REFUTED (scope-(a))
- Need ϑ_K > ln q₀ ≈ 0.104 AND hypersensitivity (slope ~2.2e6)
- The `1/u³` ladder-inversion artifact explains the slope magnitude
  (`qbeta_c3_imq_qstar_ladder_amplification_probe.py`)

**Probe plan:** The `1/u³` ladder decomposition shows the hypersensitivity is a
*representation artifact* (smooth prefactor ≈ 2.37 amplified by 1/u³ ≈ 1.62e6).
The physical quantity is the *smooth prefactor*, not the slope. Test whether the
smooth prefactor + A_ω = 3 + the proved Im 𝔙₄₁ formula compose to give |S| at
the two anchors. This is the derive-then-check route:
compute from upstream, compare to the anchors, report match or miss honestly.

### T4 — Stokes-3 identification (bean `qou-fgte`)
**Test GGM integer A_ω = 3 against the corpus κ-tower.**

The κ-tower amplitudes (`qbeta_modular_resurgence_stokes_probe.py`, Option D)
found `2πC_n → 3` but could not identify the Stokes constant at 7 rungs (below
entropy bar). Probe: with the corrected Im 𝔙₄₁ formula and the GGM Stokes
matrix S⁰ = [[1,0],[−3,1]], compute the predicted |S| at each anchor from
the integer datum + ϑ_K (no fit). Compare to anchor targets
S(muon) = +0.00968298, S(proton) = −0.03945936.

**Honest assessment:** This is the crux test. If the integer 3 + the geometric
formula reproduce the anchor magnitudes, the chain closes. If not, the Stokes
constant is not the direct source of |Δ_λ| — which is itself a valuable negative.

### T5 — Δ_λ assembly (bean `qou-w49j`)
**Compose the full chain IF T1–T4 close.**

Conditional on T1+T2 (rigidity forces A_ω) + T3+T4 (magnitude derivation):
write the derivation assembling braid → cusp → (m,ℓ) → A_ω → S → Δ_λ as a
content block + Lean statement (`S_K(q₀) = A_ω · Im 𝔙₄₁(𝔲_K(q₀))` with
`𝔲_K = ln q₀ + i·ϑ_K`). If any upstream task is open, T5 stays open with
a precise dependency list (bean, not sorry).

## Discipline

- **Strict Lean discipline** (AGENTS.md §"Strict Lean Discipline", 2026-07-27):
  no sorry, no trivial true, no laundering, no axiom-as-proof.
- **Derive-then-check:** every value comes from geometry, never fitted to anchors.
- **Bean the gap:** if a derivation can't close, create a bean with the precise
  open statement. That's the exit. Do not weaken, do not please.
- **Anti-fit:** the integer 3 is the GGM-derived datum; the anchors are
  verification targets, not inputs.

## Priority order

T4 (Stokes-3 identification probe) → T3 (SP2 probe) → T2 (hratio) → T1 (hibinv) → T5 (assembly)

Rationale: T4 is the fastest falsification — if the integer 3 doesn't reproduce
|S|, the entire chain is scope-(a) and T1/T2/T5 are moot for this route. T3
sharpens the smooth prefactor needed for T4. T2/T1 are the Lean rigidity tasks,
longer but decoupled from the probe. T5 is conditional on all others.
