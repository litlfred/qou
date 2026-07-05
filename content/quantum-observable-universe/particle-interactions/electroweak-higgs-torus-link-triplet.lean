import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.EWHiggsTorusLinkTriplet — the electroweak identification conjecture lattice

The physical identification `W↔T(2,4)`, `Z↔T(2,6)`, `H↔T(2,8)` is **not**
one monolithic conjecture. It decomposes into an honest §3b conjecture
lattice (primary/dependent per §3b-tax, dependency threaded through
`[instance]` binders) sitting on top of a **provable** genus/enumeration
core (the sibling `prop:electroweak-triplet-bring-embedding`, proved
sorry-free).

LaTeX label (of the top node): `conj:electroweak-higgs-torus-link-triplet`.

## The lattice

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| `EWSelectionPrinciple`   | primary   | —              | EW carriers are the nontrivial, strictly sub-saturating even-twist links (`0 < g < 4`) |
| `EWSectorEnumeration`    | dependent | C1             | those carriers are exactly `{T(2,4),T(2,6),T(2,8)}` |
| `EWChargeDiscriminator`  | primary   | —              | which link is the charged `W±` vs neutral `Z/H` |
| `EWSpinDiscriminator`    | primary   | —              | scalar `H` vs vector `W/Z` (deepest gap) |
| `EWHiggsTorusLinkTriplet`| dependent | C1, C3, C4     | the full identification |

The provable half — `genus(T(2,2k)) = k-1`, the `{1,2,3}` enumeration,
and the `g ≤ 4 = g(Σ₄)` embedding — lives in
`prop:electroweak-triplet-bring-embedding`. The irreducible residual is
exactly C1 (selection, strongly grounded in the corpus genus-filtration
saturation story), C3 (charge), and C4 (spin). A link's genus does **not**
see spin, so C4 is not addressed by any genus/embedding argument — it is
stated as an open primary conjecture, not papered over.

`sorry`-free: this file declares only conjecture **classes** (no
`instance` fabricated to "close" them) plus the `crossings` data; there
are no `sorry`s and no vacuous `: True` bodies.

## References

- [manuscript] particle-interactions/electroweak-higgs-torus-link-triplet
- [manuscript] particle-interactions/electroweak-triplet-bring-embedding (provable core)
-/

namespace QOU.ParticleInteractions

/-! ## The conjecture lattice (formal §3b classes)

The Seifert genus of the even 2-component torus link `T(2, 2k)` is `k - 1`
and the Bring surface has genus `g(Σ₄) = 4`; both facts are Lean-proved in
the sibling `prop:electroweak-triplet-bring-embedding`. Here we use the raw
`k - 1` / `4` inline so this file stays self-contained. -/

/-- **C1 (PRIMARY) — electroweak selection principle.**

    The electroweak carrier sector consists of the *nontrivial, strictly
    sub-saturating* even-twist 2-component torus links: those with Seifert
    genus `g` in the window `0 < g < 4 = g(Σ₄)`. This is the sub-saturating
    complement of the genus-4-**saturating** force-carrier knots
    `{T(2,9), T(3,5)}` (corpus: `genus-filtration-ideal` "saturates"; the
    Hopf link `T(2,2)` has genus `0` = trivial/vacuum). The window bound is
    the genuine hypothesis; the field carries it as a
    parameter-quantified inequality, not the conclusion. -/
-- @conjecture: primary
class EWSelectionPrinciple where
  /-- Carrier predicate on the twist parameter `k` of `T(2, 2k)`. -/
  isCarrier : ℕ → Prop
  /-- Every carrier link is nontrivial (`genus = k-1 > 0`) and strictly
      below the genus-4 saturation (`genus < 4`). -/
  subSaturating : ∀ k, isCarrier k → 0 < k - 1 ∧ k - 1 < 4
  /-- The window is realised (non-vacuous): the `k = 2` (`W±`) link is a
      carrier. -/
  carrier_realised : isCarrier 2

/-- **C2 (DEPENDENT on C1) — sector enumeration.**

    Given the selection principle, the electroweak carriers are exactly
    `k ∈ {2, 3, 4}` — the triplet `T(2,4), T(2,6), T(2,8)`. The forward
    inclusion `carrier ⊆ {2,3,4}` already follows from C1's window bound
    (proved as `ew_enumeration` in the sibling proposition); the
    conjectural content here is the *reverse* inclusion — that all three
    are realised as carriers. -/
-- @conjecture: dependent (on EWSelectionPrinciple)
class EWSectorEnumeration [EWSelectionPrinciple] where
  /-- The carrier set is exactly `{2, 3, 4}`. -/
  carriers_eq : ∀ k, EWSelectionPrinciple.isCarrier k ↔ (k = 2 ∨ k = 3 ∨ k = 4)

/-- **C3 (PRIMARY) — charge discriminator.**

    OPEN. A link's Seifert genus does not see electric charge, so no
    genus/embedding argument distinguishes the charged `W±` from the
    neutral `Z, H`. The class states the hypothesis that the minimal-genus
    carrier (`k = 2`, `W±`) carries unit charge magnitude and the two
    higher carriers (`k = 3, 4`; `Z, H`) are neutral — to be derived,
    if at all, from bar-self-duality / amphichirality data, not from the
    link genus. -/
-- @conjecture: primary
class EWChargeDiscriminator where
  /-- Electric-charge magnitude `|Q|` assigned to the carrier of twist `k`. -/
  chargeMagnitude : ℕ → ℕ
  /-- `W±` (`k=2`) is charged; `Z` (`k=3`), `H` (`k=4`) are neutral. -/
  charge_assignment :
    chargeMagnitude 2 = 1 ∧ chargeMagnitude 3 = 0 ∧ chargeMagnitude 4 = 0

/-- **C4 (PRIMARY) — spin discriminator.**

    The DEEPEST OPEN GAP. Link/genus data is spin-blind: nothing in the
    torus-link topology of `T(2,2k)` determines whether the carrier is a
    scalar or a vector. The class states the hypothesis that `W` (`k=2`)
    and `Z` (`k=3`) are spin-1 vectors while `H` (`k=4`) is a spin-0
    scalar (spin recorded doubled, so `spin 1 ↦ 2`, `spin 0 ↦ 0`). This
    is genuinely open and is not addressed by any argument in the
    embedding proposition. -/
-- @conjecture: primary
class EWSpinDiscriminator where
  /-- Doubled spin `2·s` assigned to the carrier of twist `k`. -/
  spinDouble : ℕ → ℕ
  /-- `W` (`k=2`), `Z` (`k=3`) are vectors (`2s = 2`); `H` (`k=4`) is a
      scalar (`2s = 0`). -/
  spin_assignment :
    spinDouble 2 = 2 ∧ spinDouble 3 = 2 ∧ spinDouble 4 = 0

/-- **C_top (DEPENDENT on C1, C3, C4) — the full electroweak identification.**

    `W ↔ T(2,4)`, `Z ↔ T(2,6)`, `H ↔ T(2,8)`: the crossing counts are
    `(4, 6, 8)`, with the charge and spin assignments supplied by the
    (open) discriminators C3 and C4. This is the top node of the lattice
    — it rests on the conjectural selection principle (C1) and the two
    open discriminators, so it is a *dependent* conjecture, honestly
    carrying all three as `[instance]` binders. -/
-- @conjecture: dependent (on EWSelectionPrinciple, EWChargeDiscriminator, EWSpinDiscriminator)
class EWHiggsTorusLinkTriplet
    [EWSelectionPrinciple] [EWChargeDiscriminator] [EWSpinDiscriminator] where
  /-- Crossing counts of the `(W, Z, H)` carrier links. -/
  crossings : Fin 3 → ℕ
  /-- The identification: crossings `(4, 6, 8)`, charges `(1, 0, 0)` via
      C3, doubled spins `(2, 2, 0)` via C4. -/
  identification :
    crossings 0 = 4 ∧ crossings 1 = 6 ∧ crossings 2 = 8 ∧
    EWChargeDiscriminator.chargeMagnitude 2 = 1 ∧
    EWChargeDiscriminator.chargeMagnitude 3 = 0 ∧
    EWChargeDiscriminator.chargeMagnitude 4 = 0 ∧
    EWSpinDiscriminator.spinDouble 2 = 2 ∧
    EWSpinDiscriminator.spinDouble 3 = 2 ∧
    EWSpinDiscriminator.spinDouble 4 = 0

end QOU.ParticleInteractions
