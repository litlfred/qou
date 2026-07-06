/-
  Pachner–Pentagon (Borromean) — §3b conjecture-class axiomatisation.

  conj:pachner-pentagon-borromean (D15): the Pachner 2–3 move on the ideal-
  tetrahedron decomposition of `S³ ∖ 𝓑₃` realises the q-dilogarithm pentagon
  at the Turaev–Viro / Reshetikhin–Turaev state-sum level, and the Borromean
  Markov-trace `h⁴ = −3/4` coefficient (`BorromeanMarkovTrace`, this
  namespace) is the Pachner-invariant Φ_q state-sum evaluation.

  HONEST STATUS (AGENTS.md §"open"/§"refuted" discipline — do NOT over-state):
  • Pachner-2–3-invariance ⟺ Φ_q pentagon is STANDARD TQFT (Turaev–Viro /
    Reshetikhin–Turaev); carried by the `pachner_invariant` field.
  • The Φ_q pentagon itself is established upstream
    (`QRogersPentagonArchimedean`, `pentagon_uv_commutation`).
  • The SPECIFIC identification "the h⁴ coefficient OF the Pachner-invariant
    state sum = −3/4" is CONJECTURAL and currently UN-EXHIBITED: the natural
    (u,v)-specialisation probe `computations/probes/pentagon_to_borromean_h4_probe.py`
    (witness `computations/pentagon-to-borromean-h4-probe.witness.json`,
    `matches_borromean_target_within_1pct = false` for EVERY specialisation
    tested) does not reproduce −3/4.  So this class is deliberately left with
    NO instance — the missing categorical (u,v) specialisation IS the §3b
    conjectural content (the "sorry" is the absence of a witness, not a hole
    in a proof).  This is a scope-limited negative per AGENTS.md: the natural
    specialisations fail; no structural invariant excludes a Pachner→h⁴ route.
  • Downstream results take `[PachnerPentagonBorromean R]` as a hypothesis and
    are fully verified by Lean (they consume the class fields; they do not
    re-derive the conjecture).

  Mirrors the `Kashaev.VolumeConjecture` conjecture-class pattern (a
  conjectural identity carried as a class field, no global axiom).

  FAITHFUL BASE RING (§7c).  Stated over a generic `{R : Type*} [CommRing R]`
  with the `h⁴ = −3/4` identification written division-free as
  `4 · coeff = −3` (exactly as `BorromeanMarkovTrace` avoids division over a
  CommRing).  No field, no ordering, no archimedean construct.

  -- Ref: [manuscript] conj:pachner-pentagon-borromean
  -- Ref: [turaev2010] https://doi.org/10.1515/9783110221831
  -- Ref: [kashaev1997] https://doi.org/10.1007/BF00768318
-/
import Mathlib.Algebra.Ring.Defs

namespace QOU.BraidsAndKnots

/-- **conj:pachner-pentagon-borromean (D15)** as a §3b conjecture-class over a
    generic value ring `R` (the state-sum / coefficient ring).

    An instance is a CONJECTURAL WITNESS — the categorical `(u,v)`
    specialisation that makes the Pachner-invariant Φ_q state-sum h⁴
    coefficient equal the Borromean Markov-trace `−3/4`.  The natural-
    specialisation probe currently exhibits NO such witness (see header), so
    no instance is provided. -/
class PachnerPentagonBorromean (R : Type*) [CommRing R] where
  /-- Abstract ideal triangulations of `S³ ∖ 𝓑₃`. -/
  Tri : Type
  /-- The Turaev–Viro / Reshetikhin–Turaev Φ_q state sum on a triangulation. -/
  stateSum : Tri → R
  /-- Pachner 2–3 relatedness of two triangulations. -/
  PachnerRelated : Tri → Tri → Prop
  /-- **Pachner 2–3 invariance** — STANDARD given the Φ_q pentagon: the state
      sum is constant on 2–3-related triangulations. -/
  pachner_invariant : ∀ {T T' : Tri}, PachnerRelated T T' → stateSum T = stateSum T'
  /-- The 8-ideal-octahedron decomposition of `S³ ∖ 𝓑₃` (Thurston). -/
  borOctahedral : Tri
  /-- Its 16-ideal-tetrahedron refinement, one 2–3 move away. -/
  borTetrahedral : Tri
  /-- The two canonical Borromean decompositions are 2–3-related. -/
  borromean_pachner_related : PachnerRelated borOctahedral borTetrahedral
  /-- The `h⁴` coefficient extracted from the Pachner-invariant state sum. -/
  h4_stateSum_coeff : R
  /-- **CONJECTURAL** identification with the Borromean Markov-trace coefficient
      (`tr_M(β_Bor) = 1 − (3/4)·h⁴ − …`, `BorromeanMarkovTrace`), written
      division-free as `4·coeff = −3`.  UN-EXHIBITED — this field is the §3b
      conjectural content. -/
  four_h4_eq_neg_three : 4 * h4_stateSum_coeff = -3

namespace PachnerPentagonBorromean
variable {R : Type*} [CommRing R] [c : PachnerPentagonBorromean R]

/-- **Consequence (sorry-free given the class).** The 8-octahedron and
    16-tetrahedron Borromean decompositions yield the SAME Φ_q state sum —
    triangulation-independence of the Borromean invariant, derived from
    Pachner invariance + their 2–3-relatedness.  This is the content the
    Gemini "flips compose to the identity" picture refers to, made precise. -/
theorem borromean_decompositions_agree :
    c.stateSum c.borOctahedral = c.stateSum c.borTetrahedral :=
  c.pachner_invariant c.borromean_pachner_related

/-- **Consequence (sorry-free given the class).** The conjectural Pachner→h⁴
    identification: the state-sum h⁴ coefficient equals the Borromean
    Markov-trace `−3/4` (division-free form). -/
theorem borromean_h4_via_pachner :
    4 * c.h4_stateSum_coeff = -3 :=
  c.four_h4_eq_neg_three

end PachnerPentagonBorromean

end QOU.BraidsAndKnots
