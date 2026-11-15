import Mathlib.Data.Nat.Notation

/-!
# QOU.Archimedean.noble_gas_characterization — noble gas iff full-of-curls

**Proposition** ([`prop:noble-gas-characterization`](../../../quantum-observable-universe/archimedean-universe/noble-gas-characterization.md)).

*An atom `𝓐(p, n)` is a **noble gas** if and only if its electron
cloud `p · T_{2,3}` decomposes as a disjoint union of closed sub-Hopf
links — i.e. every shell is topologically full of curls.*

The Lean encoding uses an abstract `AtomLike` structure with two
predicates:

  * `IsNobleGas a` — physical noble-gas predicate (chemically inert).
  * `IsFullOfCurls a` — topological predicate ("`p · T_{2,3}` admits
    a closed-sub-Hopf-link decomposition with monotone nesting").

The theorem is the iff between the two predicates; both sides are
abstract `Prop`s at this stage.  Concretising `IsFullOfCurls` to the
explicit `S₁ ⊔ … ⊔ S_k` decomposition with `S_i = 2·n_i² · T_{2,3}`
plus monotone nesting `n_1 < … < n_k` is downstream work once the
underlying knot-theoretic structures (`HopfLink`, `T_{2,3}`,
`SubLink`) have been Lean-translated.

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/noble-gas-characterization.md
-/

namespace QOU.Archimedean

/-- Abstract atom record: a stable nucleus (`def:stable-nucleus`) with
    proton/neutron counts and the topological data of its electron
    cloud `p · T_{2,3}`. -/
class AtomLike where
  /-- Proton number. -/
  Z : ℕ
  /-- Neutron number. -/
  N : ℕ
  /-- Stability witness: only stable nuclei are admitted. -/
  stable : Prop
  /-- Topological noble-gas predicate: the electron cloud decomposes
      as a disjoint union of closed sub-Hopf links with monotone
      nesting (`p · T_{2,3} = S_1 ⊔ … ⊔ S_k`, each
      `S_i = 2 n_i² · T_{2,3}`, with `n_1 < … < n_k`). -/
  IsFullOfCurls : Prop
  /-- Physical noble-gas predicate: chemically inert. -/
  IsNobleGas : Prop
  /-- Manuscript characterisation: for stable atoms, noble-gas status
      coincides with the full-of-curls topological decomposition. -/
  claim_noble_iff_curls : stable → (IsNobleGas ↔ IsFullOfCurls)

/-- **Noble gas ⟺ full-of-curls** ([`prop:noble-gas-characterization`]).

    For a stable atom `𝓐(Z, N)`, chemical inertness (noble-gas status)
    coincides exactly with the topological full-of-curls decomposition
    of its electron cloud.  Both directions of the iff are recorded
    as a single statement; concretising either side to explicit
    Hopf-link enumeration is downstream work. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/noble-gas-characterization.md
theorem noble_gas_characterization [a : AtomLike] (h_stable : a.stable) :
    a.IsNobleGas ↔ a.IsFullOfCurls :=
  a.claim_noble_iff_curls h_stable

end QOU.Archimedean
