import Mathlib.Tactic

/-!
# The Γ₀(5) hauptmodul gate: `t₅(τ₀) = −10` (exact rational, machine-checked arithmetic)

Bring's curve has modulus `τ₀` fixed by `j(τ₀) = −121945/32` and `j(5τ₀) = −25/2`
(Braden–Disney-Hogg arXiv:2208.13692 §2.2; the sibling record
`QOU/Archimedean/BringEllipticFactor.lean` carries these literature values). By
Riera–Rodríguez Thm 1 the residual gauge on Bring's modulus inside `Sp(8, ℤ)` is
**Γ₀(5)** — `τ` is unique only mod Γ₀(5) — so the *invariant* coordinate of the
modulus is the genus-0 hauptmodul of `X₀(5)`,

    t₅(τ) = (η(τ)/η(5τ))⁶,

related to `j` by the classical level-5 modular relation
`j(τ) = (t² + 250t + 3125)³ / t⁵`. At `j(τ₀) = −121945/32` this gives the sextic
`(t² + 250t + 3125)³ + (121945/32)·t⁵ = 0`, whose relevant real root is the **exact
rational** `t = −10` (uploaded-papers audit idea A2,
`docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md` §"New exact facts";
η-quotient numerics at τ₀ ≈ −0.5 + 0.186676i confirm, and the companion probe
`computations/probes/bring_hauptmodul_gate_probe.py` re-verifies both exactly and
numerically). The Fricke partner is `5³/t₅(τ₀) = −25/2 = j(5τ₀)`.

**The gate.** Any q₀ ↦ τ dictionary (the open input named in
`docs/audits/2026-07-18-alpha-em-tau-correspondence.md`) is physical only through
Γ₀(5)-invariants, and must therefore land on the Γ₀(5)-class with `t₅ = −10` — a
discrete, parameter-free pass/fail in the style of the keystone `144·C(n)` gate: a
candidate dictionary missing `t₅ = −10` is refuted with no precision search. Note
`τ₀` itself is transcendental (Schneider); only its invariants are exact — conflating
the two re-imports the precision trap (audit idea A2, "Risk").

This file machine-checks the **arithmetic content** of the gate over ℚ (§7c: no ℝ
needed): that `t = −10` is a root of the sextic (equivalently of its ℤ-cleared form),
and the Fricke-companion arithmetic. The *modular* statements (that `t₅` is the
hauptmodul, that `j = (t²+250t+3125)³/t⁵`, RR92 Thm 1's Γ₀(5) gauge) are cited
literature, not formalized here — this module asserts only the exact arithmetic they
reduce to at `τ₀`.

-- Ref: [riera-rodriguez-1992] The period matrix of Bring's curve, Pacific J. Math.
--       154 (1992) — Thm 1 (p. 184): the stabiliser of Bring's half-plane τc in
--       Sp(8,ℤ) is SpS₅ × SpΓ₀(5), with SpΓ₀(5) acting on τ by Möbius maps
--       (residual gauge Γ₀(5) on Bring's modulus); the 5 | p condition is Lemma 1
--       (pp. 183–184).
-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692 — j(τ₀) =
--       −121945/32, j(5τ₀) = −25/2, τ₀ ≈ −0.5 + 0.186676i.
-- Ref: [braden-northover-2012] SIGMA 8 (2012) 065 — corrected j(τ₀)/j(5τ₀)
--       labelling (RR92 swaps the two equations).
-/

namespace QOU.Archimedean.BringHauptmodulGate

/-- **`t = −10` is a root of the level-5 sextic at `j(τ₀) = −121945/32`:**
`(t² + 250t + 3125)³ + (121945/32)·t⁵ = 0` at `t = −10`. This is the exact-rational
content of `t₅(τ₀) = −10`. -/
theorem hauptmodul_sextic_root :
    (((-10 : ℚ) ^ 2 + 250 * (-10) + 3125) ^ 3 + (121945 / 32) * (-10 : ℚ) ^ 5) = 0 := by
  norm_num

/-- The ℤ-cleared form of the same root: `32·(t² + 250t + 3125)³ + 121945·t⁵ = 0`
at `t = −10`, entirely over ℤ. -/
theorem hauptmodul_sextic_root_int :
    (32 * (((-10 : ℤ) ^ 2 + 250 * (-10) + 3125) ^ 3) + 121945 * (-10 : ℤ) ^ 5) = 0 := by
  norm_num

/-- The defining relation in the `j = (t² + 250t + 3125)³ / t⁵` direction:
at `t = −10` the numerator `(t² + 250t + 3125)³ = 725³` equals `j·t⁵` with
`j = −121945/32`, i.e. `j(τ₀)·(−10)⁵ = 725³ = 381 078 125`. -/
theorem j_tau0_times_t5 :
    ((-121945 / 32 : ℚ)) * (-10 : ℚ) ^ 5 = ((-10 : ℚ) ^ 2 + 250 * (-10) + 3125) ^ 3 := by
  norm_num

/-- **Fricke companion.** The Fricke involution sends `t₅ ↦ 5³/t₅`; at `t₅(τ₀) = −10`
this gives `5³/(−10) = −25/2`, which is exactly the literature value `j(5τ₀) = −25/2`
— an internal consistency check tying the two published j-invariants through the one
rational hauptmodul value. -/
theorem fricke_companion : (5 : ℚ) ^ 3 / (-10) = -25 / 2 := by
  norm_num

end QOU.Archimedean.BringHauptmodulGate
