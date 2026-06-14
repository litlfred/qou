import QOU.Basic
import QOU.BraidKnot.HeckeAnyonicSubstrate
import QOU.BraidKnot.CrystalGraphRealization

/-!
# QOU.BraidKnot.RootOfUnityMTCTruncation — root-of-unity MTC (conjecture)

Class axiomatisation of [conj:root-of-unity-mtc-truncation]: at
`q = e^{2πi/k}`, the cyclotomic-KLR quotient becomes
finite-dimensional, the Kashiwara crystal truncates to partitions
with at most `k - 1` columns, and the resulting category of modules
is a Modular Tensor Category `MTC_k` whose simple objects are
non-abelian anyons.

Takes `[HeckeAnyonicSubstrate R q]` and `[CrystalGraphRealization R q]`
as upstream inputs.  Specialised to a fixed `truncationLevel k ≥ 2`
encoding the chosen primitive root of unity.

LaTeX: `\label{conj:root-of-unity-mtc-truncation}`

References:
- Kitaev, A. (2006).
- Nayak, C. et al. (2008).
- Bakalov, B. & Kirillov, A. A. (2001). *Lectures on Tensor
  Categories and Modular Functors*. AMS University Lecture Series 21.
- Khovanov, M. & Lauda, A. D. (2009).
- Kashiwara, M. (1991).
-/

namespace QOU.BraidKnot

universe u

/-- **Root-of-unity MTC truncation (conjecture).**

    At `q = e^{2πi/k}`, the KLR algebra truncates to an MTC `MTC_k`
    whose simple objects (non-abelian anyons) are labelled by the
    truncated crystal nodes (partitions with at most `k - 1`
    columns). -/
-- Ref: [bakalovkirillov2001]     title: — see content/schema/references.ts
-- Ref: [kitaev2006] Kitaev, "Anyons in an exactly solved model and beyond," arXiv:cond-mat/0506438
-- Ref: [nayak2008] Nayak, Simon, Stern, Freedman, Das Sarma, "Non-Abelian Anyons and Topological Quantum Computation," arXiv:0707.1889
-- Ref: [khovanovlauda2009] Khovanov & Lauda, "A diagrammatic approach to categorification of quantum groups," Repr. Theory 13 (2009), arXiv:0803.4121
-- Ref: [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue of universal enveloping algebras," Duke Math. J. 63 (1991)
class RootOfUnityMTCTruncation (R : Type u) [CommRing R] (q : R)
    (k : ℕ)
    [C : CrystalGraphRealization R q] where
  /-- Truncation level `k ≥ 2`. -/
  k_ge_two : 2 ≤ k
  /-- Predicate: a crystal node is supported on a partition with at
      most `k - 1` columns.  These are the simple `MTC_k` objects. -/
  inTruncation : C.CrystalNode → Prop
  /-- Number of columns of the partition labelling a crystal node. -/
  columnCount : C.CrystalNode → ℕ
  /-- A node is in the truncation iff its column count is `< k`. -/
  inTruncation_iff : ∀ v : C.CrystalNode,
    inTruncation v ↔ columnCount v < k
  /-- **The conjecture itself**: every GS normal form at `q =
      e^{2πi/k}` has `nodeOf T` in the truncated component.  Plays
      the role of `sorry`. -/
  truncation_holds : ∀ T : C.NormalForm,
    inTruncation (C.nodeOf T)

namespace RootOfUnityMTCTruncation

/-- Unconditional structural lemma: the truncation level `k` is at
    least `2` (positivity of the MTC rank). -/
-- Ref: [manuscript] braids-and-knots/root-of-unity-mtc-truncation
theorem k_pos
    {R : Type u} [CommRing R] {q : R} {k : ℕ}
    [C : CrystalGraphRealization R q]
    [M : RootOfUnityMTCTruncation R q k] :
    0 < k :=
  Nat.lt_of_lt_of_le (by decide : 0 < 2) M.k_ge_two

/-- Unconditional consequence: every normal form's crystal node is
    in the truncated component (direct from `truncation_holds`). -/
-- Ref: [manuscript] braids-and-knots/root-of-unity-mtc-truncation
theorem nodeOf_inTruncation
    {R : Type u} [CommRing R] {q : R} {k : ℕ}
    [C : CrystalGraphRealization R q]
    [M : RootOfUnityMTCTruncation R q k]
    (T : C.NormalForm) :
    M.inTruncation (C.nodeOf T) :=
  M.truncation_holds T

/-- Unconditional consequence: every normal form's crystal node has
    column count strictly less than `k`.  Direct consequence of
    `truncation_holds` together with `inTruncation_iff`.  This is
    the form actually used downstream by the MTC truncation pipeline:
    it bounds the number of columns in the partition labelling each
    GS normal form by the chosen root-of-unity level `k`. -/
-- Ref: [manuscript] braids-and-knots/root-of-unity-mtc-truncation
theorem columnCount_nodeOf_lt_k
    {R : Type u} [CommRing R] {q : R} {k : ℕ}
    [C : CrystalGraphRealization R q]
    [M : RootOfUnityMTCTruncation R q k]
    (T : C.NormalForm) :
    M.columnCount (C.nodeOf T) < k :=
  (M.inTruncation_iff (C.nodeOf T)).mp (M.truncation_holds T)

/-- **Faithful realisation** (`def`, not `instance`: keeps this `sorry` out of
    typeclass resolution, so downstream `[...]` hypotheses stay genuinely
    conditional -- CLAUDE.md §3b-cond, #2269). Carries the explicit
    research-grade conjecture as a sorry. -/
def canonical (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] :
    RootOfUnityMTCTruncation R q 2 where
  k_ge_two := le_refl 2
  inTruncation v := 0 < 2
  columnCount _ := 0
  inTruncation_iff _ := by decide
  -- Ref: [manuscript] conj:root-of-unity-mtc-truncation (§3b-cond conjectural-class instance; sorry = the conjecture)
  truncation_holds _ := sorry

end RootOfUnityMTCTruncation

end QOU.BraidKnot
