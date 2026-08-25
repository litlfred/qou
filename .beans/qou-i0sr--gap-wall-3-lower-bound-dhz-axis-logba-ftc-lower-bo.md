---
# qou-i0sr
title: 'GAP WALL-3 lower bound: dH(z-axis) ≥ |log(b/a)| (FTC lower bound)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T13:02:37Z
updated_at: 2026-08-16T14:01:26Z
---

T2 geodesic-uniqueness, WALL-3 LOWER bound. UPPER bound + existence LANDED
(PR #5236, HyperbolicGeodesicZAxis.lean: dH (0,0,a) (0,0,b) ≤ ofReal|log(b/a)|,
via the constant-speed vertical segment vseg, sorry-free).

OPEN: dH (zpt a) (zpt b) ≥ ofReal|log b − log a|, i.e. every admissible γ from
(0,0,a) to (0,0,b) has pathLenH γ ≥ ofReal|log(b/a)|. Combined with the upper
bound this yields the exact z-axis distance AND that vseg is an IsHypMinimizer
(its `minimal` field).

Derivation (standard, the crux):
  pathLenH γ = ∫⁻_{Icc 0 1} ofReal(‖γ'‖/z)      [z(t) := (γ t) 2]
    ≥ ∫⁻_{Icc 0 1} ofReal(|z'|/z)                [coord bound |(γ' t) 2| ≤ ‖γ' t‖]
    = ∫⁻_{Icc 0 1} ofReal(|(log∘z)'|)            [(log∘z)' = z'/z, z>0]
    ≥ ofReal|∫_0^1 (log∘z)'|                      [|∫|≤∫||  +  ofReal↔lintegral bridge]
    = ofReal|log z(1) − log z(0)| = ofReal|log b − log a|   [FTC]

Lean friction points (why it stalls, each a real Mathlib-API chunk):
 1. coord bound |(v) 2| ≤ ‖v‖ on EuclideanSpace — via abs_inner_le_norm with
    single 2 1 (EuclideanSpace.inner_single_right), or EuclideanSpace.norm_eq +
    Finset.single_le_sum. (SMALL, reusable.)
 2. z'(t) = (γ' t) 2 : z = EuclideanSpace.proj 2 ∘ γ, proj 2 is a CLM. (SMALL.)
 3. (log∘z)' = z'/z : (Real.hasDerivAt_log (z t ≠ 0)).comp. (SMALL.)
 4. ∞-length case split: if pathLenH γ = ∞ the bound is trivial; else finite
    lintegral of ‖γ'‖/z ⇒ |(log∘z)'| = |z'|/z has finite lintegral ⇒ integrable.
 5. FTC ∫_0^1 (log∘z)' = log b − log a : intervalIntegral.integral_eq_sub_of_
    hasDerivAt needs log∘z continuous on [0,1] (z continuous & >0) + interval-
    integrability of the derivative. Measurability of deriv γ on [0,1] needed.
 6. |∫_0^1 h| ≤ ∫_0^1 |h| (intervalIntegral.abs_integral_le_integral_abs) then
    ofReal(∫_0^1 |h|) = ∫⁻_{Ioc/Icc} ofReal|h| bridge
    (ofReal_integral_eq_lintegral_ofReal / MeasureTheory.integral for nonneg).

Points 4–6 are the substantial part (measurability of deriv, integrability from
finite lintegral, FTC hypotheses, Bochner↔lintegral bridge). Est. multi-hundred
lines. This is the "Mathlib has no hyperbolic geometry" reason.

File: content/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicGeodesicZAxis.lean



---
UPDATE 2026-08-16 (PR #5253, branch claude/t2-wall-close-2026-08-16): LANDED sorry-free.
Was nearly immediate given the merged FTC lower bound dH_ge_logHeight: specialise it to
z-axis points (heights a, b). Added to HyperbolicGeodesicZAxis.lean:
  dH_zpt_ge          : ofReal|log(b/a)| ≤ dH (zpt a) (zpt b)
  dH_zpt             : dH (zpt a) (zpt b) = ofReal|log(b/a)|   (EXACT, with dH_zpt_le)
  pathLenH_vseg_eq_dH: the vertical segment is a genuine z-axis length-minimiser.
#print axioms = [propext, Classical.choice, Quot.sound]. Pending merge; human closes.
