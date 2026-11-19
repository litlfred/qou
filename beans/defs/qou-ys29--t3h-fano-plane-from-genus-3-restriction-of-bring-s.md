---
# qou-ys29
title: 'T3h: Fano plane from genus-3 restriction of Bring surface — derive octonions from geometry'
status: in-progress
type: task
priority: critical
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-04T10:18:37Z
updated_at: 2026-11-19T16:48:42Z
parent: qou-8lxd
---

CONJECTURED DERIVATION CHAIN (user insight, 2026-08-04):

SM fermions exhaust at genus 3 (unmapped-torus-knots.md: "Standard Model
fermions exhaust at genus 3"). The tau T(2,7) and charm are the genus-3
matter generators. The natural automorphism group of genus-3 curves is
PSL(2,7) = GL(3,F_2) = Aut(Fano plane) (168 elements; Klein quartic is
the Hurwitz surface at genus 3). The Fano plane encodes the octonion
multiplication table (7 imaginary units, 7 lines, each line = associative
triple). And Stab_{G_2}(e) = SU(3) is already proved (color-su3-from-g2).

So the chain is:
  Bring (genus 4, S_5) ⊃ genus-3 Seifert surfaces
  → PSL(2,7) = Aut(Klein quartic) = Aut(Fano)
  → Fano plane = octonion multiplication table
  → G_2 = Aut(O) ⊃ SU(3) = Stab(e)
  → color SU(3) DERIVED from Bring geometry

If this works, it replaces the current "import octonions ad hoc" with a
geometric derivation: the octonionic structure IS the genus-3 restriction
of the Bring surface's coordinate system.

SPECIFIC TESTS:
1. Does the genus-3 Seifert surface of T(2,7) embed in Bring's genus-4
   surface as a codimension-1 subsurface? (Topologically: genus 4 → genus 3
   by pinching one handle.)
2. Does the S_5 symmetry of Bring restrict on the genus-3 subsurface to a
   subgroup containing PSL(2,7)? Note: |PSL(2,7)| = 168, |S_5| = 120, so
   PSL(2,7) is NOT a subgroup of S_5. This is a potential obstruction.
   Alternative: the genus-3 surface may not inherit Bring's S_5 but carry
   its OWN PSL(2,7) symmetry.
3. Do the 7 genus-3 torus-knot generators (the 7 imaginary octonion units)
   map to the 7 points of the Fano plane under the Klein quartic's
   automorphisms?
4. Does the associator structure (the Fano lines = associative triples)
   reproduce the octonionic multiplication table?

ANTI-FITTING: The chain must be a DERIVATION, not a coincidence. The key
test: does the genus-3 restriction of Bring force PSL(2,7) structure, or
is PSL(2,7) merely compatible? If forced → derivation. If merely
compatible → numerology.

OBSTRUCTION RESOLVED (web research 2026-08-04):
|PSL(2,7)| = 168 > |S_5| = 120, so PSL(2,7) is NOT a subgroup of S_5.
BUT: S_4 (order 24) is a MAXIMAL subgroup of BOTH S_5 AND PSL(2,7)!
  - In S_5: S_4 = point-stabilizer (index 5)
  - In PSL(2,7): S_4 = point/line-stabilizer of Fano (index 7)
  - S_4 is the BRIDGE between the two symmetry groups

DEGENERATION MECHANISM (Harris-Morrison, moduli theory):
Pinching an S_4-invariant 1-cycle on Bring (g=4) → nodal genus-3 curve.
The S_4 symmetry survives. The normalized genus-3 limit can then enhance
to full PSL(2,7) = Hurwitz-maximal at g=3 (the Klein quartic IS the
maximal curve at genus 3).

ADDITIONAL FINDING: PSL(2,7) embeds directly as a FINITE SUBGROUP of
SU(3) (the Blichfeldt group of order 168). This means the Fano-plane
symmetry doesn't just "correspond to" color SU(3) — it SITS INSIDE it.

REVISED CHAIN:
  Bring (g=4, S_5) → pinch S_4-invariant cycle → genus-3 nodal curve
  ↓ (normalize: S_4 symmetry survives)
  genus-3 curve with S_4 → enhances to PSL(2,7) (Hurwitz maximum)
  ↓ (PSL(2,7) = GL(3,F_2) = Aut(Fano))
  Fano plane structure → octonion multiplication (det3, Lean-proved)
  ↓ (PSL(2,7) ⊂ SU(3) as Blichfeldt group)
  color SU(3) DERIVED from Bring degeneration


RELATED: T3d (octonion G_2 route), T3b (distinct-fibre groupoid),
fivefold-symmetry-table row 3 ("Borromean B_3 (color SU(3))").

CORPUS EVIDENCE ALREADY PRESENT:

1. OctonionCocycle.lean (BringsSurface module!) — det3 invariant under
   GL(3,F_2) = PSL(2,7). Line 80: "the concrete tie between the (Z/2)^3
   octonion sign structure and the genus-3 (Klein-quartic, PSL(2,7)=Fano)
   home of the octonion product." The Lean proof is sorry-free.

2. docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md §95:
   "The natural *surface* home of the full octonion product is genus 3 —
   the Klein quartic, Aut = PSL(2,7) (order 168) = the Fano-plane /
   octonion-multiplication symmetry, which does have a 7-dim irrep."

3. Same audit EXCLUDES the direct S_5-equivariant route:
   - H^1(Sigma_4)^{S_5} = 0, so no S_5-invariant line exists (can't be 1 of O)
   - S_5 irreps are {1,4,5,6} — no 7, so Im(O) can't carry S_5 irrep
   - H^1(Sigma_4) = 4+4 as S_5-module, not 1+7

4. The audit identifies TWO routes to full O:
   a. McKay/E_8 route: A_5 → E_8 → integral octonions (lattice level)
   b. Colour → G_2 extension: extend SU(3) to full G_2 via G_2/SU(3)=S^6

5. jet-planck-steps-table2-data.md: Step 7 (septic) = genus 3 = tau + charm.
   SM fermions exhaust at genus 3 (unmapped-torus-knots.md line 19).

KEY INSIGHT (user 2026-08-04): The genus-3 Seifert surfaces of the particle
knots (T(2,7) etc.) might not need to "inherit" S_5 from Bring at all.
They live as SUBSURFACES of Bring but carry their OWN PSL(2,7) symmetry
(the natural symmetry of genus-3 curves). The question is whether the
*embedding* of the genus-3 subsurface into Bring's coordinate system
makes the Fano structure computable from Bring data.

REFINED CHAIN:
  Bring (g=4, S_5) contains genus-3 subsurfaces (Seifert surfaces)
  ↓ (embedding, not restriction of S_5)
  genus-3 surface carries its own PSL(2,7) = Aut(Fano)
  ↓ (Albuquerque-Majid: O = R_F[(Z/2)^3], dF = det3)
  det3 invariant under GL(3,F_2) = PSL(2,7) [Lean: sorry-free]
  ↓ (Günaydin-Gürsey: fix e → SU(3))
  color SU(3) = Stab_{G_2}(e) DERIVED

CONTRAST WITH McKay ROUTE:
  Bring S_5 → A_5 → binary icosahedral 2I → McKay → E_8 → integral O
  (lattice level, not surface level; longer chain but theorem-backed)

The genus-3 route is MORE DIRECT but LESS THEOREM-BACKED. The McKay route
has each step proved. The genus-3 route needs test 1 (embedding exists)
and the PSL(2,7) structure to be computable from Bring coordinates.

COMPUTATIONAL PROGRESS (2026-08-04, session 2):

1. PSL(2,7) irreps verified: {1, 3, 3̄, 6, 7, 8}
   ∑d² = 1+9+9+36+49+64 = 168 = |G| ✓
   (computations/psl27_irrep_verification.py + witness)

2. S₄ Fano action verified: (computations/s4_fano_action.py)
   - S₄ = Stab(pt) in PSL(2,7), |S₄| = 24 ✓
   - S₄ acts TRANSITIVELY on 3 lines through fixed point
   - S₄ acts TRANSITIVELY on 4 lines NOT through fixed point
   - S₄ acts TRANSITIVELY on 6 remaining points
   - 3 local lines PARTITION 6 remaining pts into 3 PAIRS

   KEY RESULT: S₄ preserves the "local Fano" at the fixed point.
   The 3 local lines encode the 3 octonion triples through that
   imaginary unit. S₄ permutes these triples transitively.

3. Content block updated: color-su3-from-g2.md now includes the
   PSL(2,7) irrep dimensions and physical interpretation.

REMAINING OPEN QUESTIONS:
- Does pinching an S₄-invariant 1-cycle on Bring (g=4) actually
  produce a genus-3 nodal curve? (Algebraic geometry, not computed)
- Does the normalized genus-3 limit enhance S₄ → PSL(2,7)?
  (Expected: the Klein quartic is Hurwitz-maximal at g=3)
- Is the Seifert surface of T(2,7) a literal subsurface of Bring?
  (Topological, needs separate investigation)



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update — 2026-11-16 (`litlfred/qou#8149`, `e824457ca8e0ff4e0b85644c5478eebd2c3c8d56`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/Eightfold/G2IsotropyComplexThreefold.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Proves `bring_klein_s4_order_bridge`: $\gcd(|S_5|=120, |\mathrm{PSL}_2(\mathbb{F}_7)|=168) = 24 = |S_4|$, $\neg(168 \mid 120)$, $\neg(7 \mid 120)$ (formalizing the exact group-order obstruction preventing $\mathrm{PSL}_2(\mathbb{F}_7)$ from embedding into $\mathrm{Aut}(\Sigma_{\mathrm{Bring}}) = S_5$), $[\mathrm{PSL}_2(\mathbb{F}_7) : S_4] = 7$ (Fano points/lines), and $[S_5 : S_4] = 5$ (Bring covering sheets).
  - Proves `fano_local_nonlocal_line_partition`: fixing $e_1$ splits the 7 Fano lines into `3` local lines through $e_1$ (which form the 3 complex lines of $W \cong \mathbb{C}^3$ under $J = L_{e_1}$) and `4` non-local lines disjoint from $e_1$ ($3 + 4 = 7$).
- **Probe & Witness (`computations/probes/ribbon_twist_z6_hypercharge_hirzebruch_probe.py` + `ribbon-twist-z6-hypercharge-hirzebruch.witness.json`)**: `allPassed: true` (`q0Anchor: "independent"`).



## Progress Update (2026-11-19)
Wave-6B 80-dps probe `bring_fano_octonion_blichfeldt_su3_probe.py` (`scriptHash = 016e4e86c0bb`) Red-Team PASSED (`0` blockers); companion Lean module `QOU/Eightfold/BringGenusThreeFanoOctonionAndBlichfeldtSU3.lean` (`1,302` lines) completing verification.
