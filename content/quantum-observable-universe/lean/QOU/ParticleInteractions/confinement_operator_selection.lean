/-!
# QOU.ParticleInteractions.confinement_operator_selection — topological Brunnian selection

**Canonical** for content block
[`prop:confinement-operator-selection`](../../../quantum-observable-universe/particle-interactions/confinement-operator-selection.md):
*Confinement operator selection via topological Brunnian minimality*.

The confinement operator is selected by a **topological** principle: a confined
`n`-quark state is the closure of the **crossing-minimal nontrivial Brunnian**
`n`-braid (confinement ⇔ no proper subset of quarks can be isolated ⇔ every
proper sublink is trivial). This replaces the earlier *minimum-action on the
6×6 Frobenius Gram matrix* framing, which was **refuted**: `NF(𝓑₃)` is ≈ 99.8%
the identity `γ` (the maximum-cost channel), so any cost-minimising
operator-space program selects the smallest-cost mesonic `L±` instead — never
`𝓑₃` (see `docs/audits/2026-06-17-b3-dense-sdp-lever-closed.md` and
`computations/probes/b3_dense_sdp_wedderburn_projector.py`).

The general statement yields the **baryon/meson dichotomy as a theorem**:
nontrivial Brunnian links require ≥ 3 components, so confinement (a nontrivial
Brunnian braid) exists iff `n ≥ 3` — `n = 2` (mesons) has none and falls back to
pairwise `L±` binding, while `n = 3` (baryons) selects the minimal Brunnian link,
the Borromean braid `𝓑₃ = (σ₀σ₁⁻¹)³`.

This is a **placeholder context-class**: the Brunnian predicate, the existence
dichotomy, and crossing-minimality are axiomatised as class fields carrying the
computational witnesses (`computations/probes/b3_brunnian_selection_scope.py`,
`b3_brunnian_minimality_enumeration.py`); the theorem composes them. Minimality
is witnessed *among 3-braid closures* (the framework's setting), not proved as
full link-theoretic uniqueness. Upgrading to a closed Lean proof requires
formalising the Brunnian predicate over an actual braid-group model and the
finite enumeration.
-/

namespace QOU.ParticleInteractions

/-! ## Braid-group word model — the Borromean linking signature is machine-proved

A concrete 3-strand braid-word model. A letter is a generator index
(`0` = σ₀ swapping the strands at positions 0,1; `1` = σ₁ swapping positions 1,2)
with a sign. Tracking strand positions through the word, `signedCrossings`
accumulates the signed crossing count per unordered strand pair (`= 2·lk`), and
`crossingCounts` the unsigned count. For the Borromean braid `(σ₀σ₁⁻¹)³` both are
proved by `decide`: every pairwise linking number vanishes (the Brunnian
*signature* — a necessary condition for Brunnian) while every pair still crosses
twice (geometrically interwoven). This replaces the *axiomatized* signature with
a machine-checked fact; the full Brunnian property (each 2-sublink is the
*unknot/unlink*, not merely `lk = 0`) and crossing-minimality remain axiomatized
in the classes below — they need unknot recognition / the finite enumeration
(`computations/probes/b3_brunnian_*`), beyond core Lean. -/
namespace BraidModel

/-- A 3-braid letter: generator index (`0`/`1`) and sign (`true` = positive). -/
abbrev Letter := Nat × Bool

/-- The Borromean braid word `(σ₀ σ₁⁻¹)³`. -/
def borromean : List Letter :=
  [(0, true), (1, false), (0, true), (1, false), (0, true), (1, false)]

/-- Strand occupying each of the 3 positions. -/
abbrev Pos := Nat × Nat × Nat

/-- Add signed crossing `s` to the accumulator slot for the unordered pair {x,y}. -/
def addPair (acc : Int × Int × Int) (x y : Nat) (s : Int) : Int × Int × Int :=
  let (c01, c02, c12) := acc
  if (x = 0 ∧ y = 1) ∨ (x = 1 ∧ y = 0) then (c01 + s, c02, c12)
  else if (x = 0 ∧ y = 2) ∨ (x = 2 ∧ y = 0) then (c01, c02 + s, c12)
  else (c01, c02, c12 + s)

/-- One braid letter: cross the two strands at the generator's positions
    (recording the signed crossing) then swap them. -/
def step (state : Pos × (Int × Int × Int)) (L : Letter) : Pos × (Int × Int × Int) :=
  let (pos, acc) := state
  let (p0, p1, p2) := pos
  let s : Int := if L.2 then 1 else -1
  match L.1 with
  | 0 => ((p1, p0, p2), addPair acc p0 p1 s)
  | _ => ((p0, p2, p1), addPair acc p1 p2 s)

/-- The three pairwise signed crossing sums (`= 2·lk` per pair). -/
def signedCrossings (w : List Letter) : Int × Int × Int :=
  (w.foldl step ((0, 1, 2), (0, 0, 0))).2

/-- The three pairwise unsigned crossing counts. -/
def crossingCounts (w : List Letter) : Nat × Nat × Nat :=
  (w.foldl (fun (st : Pos × (Nat × Nat × Nat)) L =>
      let (pos, acc) := st
      let (p0, p1, p2) := pos
      let (n01, n02, n12) := acc
      let add := fun (x y : Nat) =>
        if (x = 0 ∧ y = 1) ∨ (x = 1 ∧ y = 0) then (n01 + 1, n02, n12)
        else if (x = 0 ∧ y = 2) ∨ (x = 2 ∧ y = 0) then (n01, n02 + 1, n12)
        else (n01, n02, n12 + 1)
      match L.1 with
      | 0 => ((p1, p0, p2), add p0 p1)
      | _ => ((p0, p2, p1), add p1 p2))
    ((0, 1, 2), (0, 0, 0))).2

/-- **Brunnian linking signature** (machine-proved): every pairwise linking
    number of the Borromean braid vanishes (`2·lk = 0` per pair). -/
theorem borromean_linking_signature : signedCrossings borromean = (0, 0, 0) := by
  decide

/-- **Geometric nontriviality** (machine-proved): every pair of strands crosses
    twice — pairwise unlinked (`lk = 0`) yet interwoven, the Borromean hallmark. -/
theorem borromean_crossing_counts : crossingCounts borromean = (2, 2, 2) := by
  decide

end BraidModel

/-- General topological confinement selection. A confined `n`-quark bound state
    is the closure of the crossing-minimal nontrivial **Brunnian** `n`-braid. -/
class BrunnianConfinement where
  /-- Braids on `n` strands. -/
  Braid : Nat → Type
  /-- The closure is a nontrivial link (not the unlink). -/
  Nontrivial : (n : Nat) → Braid n → Prop
  /-- Every proper sublink of the closure is the unlink (Brunnian). -/
  Brunnian : (n : Nat) → Braid n → Prop
  /-- Diagram crossing number. -/
  crossings : (n : Nat) → Braid n → Nat
  /-- The selected confinement braid on `n` strands, when one exists. -/
  confine : (n : Nat) → Option (Braid n)
  /-- (G1, existence dichotomy) a nontrivial Brunnian braid — hence a confined
      state — exists iff `n ≥ 3` (Brunnian links require ≥ 3 components).
      `n = 2` (mesons) has none; the baryon/meson split is structural. -/
  exists_iff_three_le :
    ∀ n, (∃ b : Braid n, confine n = some b) ↔ 3 ≤ n
  /-- (G2, selection) the selected braid is nontrivial Brunnian and
      crossing-minimal among all nontrivial Brunnian `n`-braids. -/
  is_minimal_brunnian :
    ∀ n (b : Braid n), confine n = some b →
      Nontrivial n b ∧ Brunnian n b ∧
      (∀ b' : Braid n, Nontrivial n b' → Brunnian n b' → crossings n b ≤ crossings n b')

/-- The `n = 3` (baryon) specialisation: the confinement operator is the
    Borromean braid `𝓑₃ = (σ₀σ₁⁻¹)³` in the Hecke algebra `H₃(q)`. -/
class BorromeanConfinement extends BrunnianConfinement where
  /-- The Hecke algebra `H₃(q)` carrier. -/
  HeckeAlgebra : Type
  /-- Image of a braid under the Hecke representation. -/
  rep : {n : Nat} → Braid n → HeckeAlgebra
  /-- The Borromean operator `𝓑₃ ∈ H₃(q)`. -/
  B3 : HeckeAlgebra
  /-- The braid word `(σ₀σ₁⁻¹)³ ∈ H₃(q)`. -/
  borromean_word : HeckeAlgebra
  /-- Sub-claim — definitional identity `𝓑₃ = (σ₀σ₁⁻¹)³`. -/
  borromean_identity : B3 = borromean_word
  /-- Sub-claim — the `n = 3` topological selection is the Borromean braid. -/
  confine_three : ∃ b : Braid 3, confine 3 = some b ∧ rep b = B3

/-- **Content statement.** The confinement operator is the crossing-minimal
    nontrivial Brunnian `n`-braid: it exists iff `n ≥ 3` (baryon/meson
    dichotomy), is the unique-by-minimality Brunnian selection, and at `n = 3`
    equals the Borromean braid `𝓑₃ = (σ₀σ₁⁻¹)³`. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/confinement-operator-selection.ts
theorem confinement_operator_selection [ctx : BorromeanConfinement] :
    (∀ n, (∃ b : ctx.Braid n, ctx.confine n = some b) ↔ 3 ≤ n) ∧
    (∀ n (b : ctx.Braid n), ctx.confine n = some b →
        ctx.Nontrivial n b ∧ ctx.Brunnian n b ∧
        (∀ b' : ctx.Braid n, ctx.Nontrivial n b' → ctx.Brunnian n b' →
            ctx.crossings n b ≤ ctx.crossings n b')) ∧
    ctx.B3 = ctx.borromean_word ∧
    (∃ b : ctx.Braid 3, ctx.confine 3 = some b ∧ ctx.rep b = ctx.B3) :=
  ⟨ctx.exists_iff_three_le, ctx.is_minimal_brunnian,
   ctx.borromean_identity, ctx.confine_three⟩

end QOU.ParticleInteractions
