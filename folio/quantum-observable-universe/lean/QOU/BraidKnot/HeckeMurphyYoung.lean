import QOU.BraidKnot.HeckeMurphy
import QOU.BraidKnot.Specht
import QOU.BraidKnot.ColSuperstandardTableau
import QOU.BraidKnot.HeckeCellular
import QOU.BraidKnot.HeckeTypeAPresentationEquiv
import QOU.Mathlib.SchenstedRSKBurnside
import QOU.BraidKnot.NumSYTBridge
import QOU.BraidKnot.SpechtStandardBasisCore
import Mathlib.LinearAlgebra.Dimension.DivisionRing

/-!
# QOU.BraidKnot.HeckeMurphyYoung — Murphy's `x_λ` over the *actual* Young subgroup

`QOU.BraidKnot.HeckeMurphy` proves `σ_i · x_S = q · x_S` for any finite set of permutations
closed under right multiplication by `s_i`, and specialises it to an arbitrary `Subgroup`.
This file connects that to the Young subgroup a *tableau* actually has, which is what makes
it Murphy's `x_λ` rather than a statement about an abstract subgroup.

## The join, and why it is only bookkeeping

The two clusters were built independently and index their symmetric groups differently:

* the **Specht** cluster works over `Equiv.Perm (Fin (Specht.nOf μ))`, where `nOf μ = μ.card`;
* the **Hecke** cluster works over `Equiv.Perm (Fin (n + 1))`, because `IwahoriHecke K q n` has
  `n` generators and so models `S_{n+1}`.

Given `μ.card = n + 1` these are the same group, and the corpus already carries the transport
(`Equiv.permCongrHom (finCongr h)`, used by `SpechtClassification.transportPermHom`). So the
bridge is a `Subgroup.map`, not new mathematics — but it is the point at which the `q`-deformed
side can finally name the combinatorial object the `q = 1` side has had all along.

`Specht.rowStab t` is exactly the Young subgroup `S_λ`: the stabiliser of the row pattern of
`t`, i.e. the permutations preserving each row of `t` setwise. It is `MulAction.stabilizer`, so
it is a `Subgroup` by construction and carries a `DecidablePred` instance
(`Specht.instDecidableMemRowStab`) — which is what `murphySum`'s `Finset.filter` needs.

## What this does and does not establish

It gives the eigenvector property for the **genuine** `x_λ`. It is still **not** the Murphy
basis: that the `m_{st} = T_{d(s)}^* x_λ T_{d(t)}` are a basis, and cellular axioms (C1)/(C3),
remain open. What has changed is that those are now stated against objects that exist —
`colSuperstandard` for the reference tableau `t^λ`, `partitionDom` for the dominance order —
rather than against combinatorics that would have to be built. Bean `qou-phir`.
-/

namespace QOU.BraidKnot.HeckeMurphyYoung

open QOU.BraidKnot.HeckeMurphy
open QOU.Hecke.TwBasis
open QOU.Hecke.IwahoriHecke (σ)

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-- **The Young subgroup of a tableau, at the Hecke algebra's index.**

`Specht.rowStab t` lives over `Fin (Specht.nOf μ)`; `h : Specht.nOf μ = n + 1` transports it to
`Fin (n + 1)`, where `IwahoriHecke K q n` acts. Pure re-indexing — `Equiv.permCongrHom` is a
`MulEquiv`, so the image is a subgroup isomorphic to `rowStab t`. -/
noncomputable def youngSubgroup {μ : YoungDiagram} (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (t : QOU.BraidKnot.Specht.Tableau μ) : Subgroup (Equiv.Perm (Fin (n + 1))) :=
  (QOU.BraidKnot.Specht.rowStab t).map (Equiv.permCongrHom (finCongr h)).toMonoidHom

/-- **Murphy's `x_λ` is a `q`-eigenvector, for the Young subgroup of an actual tableau.**

`σ_i · x_λ = q · x_λ` whenever `s_i` lies in the (transported) row stabiliser of `t`. This is
the defining property of `x_λ`, now stated about the combinatorial object it is supposed to be
about rather than about an abstract subgroup. -/
theorem σ_mul_murphySum_young {μ : YoungDiagram} (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (t : QOU.BraidKnot.Specht.Tableau μ) (i : Fin n)
    [DecidablePred (· ∈ youngSubgroup n h t)]
    (hi : sw i ∈ youngSubgroup n h t) :
    σ K q n i * murphySum K q n {w | w ∈ youngSubgroup n h t}
      = q • murphySum K q n {w | w ∈ youngSubgroup n h t} :=
  σ_mul_murphySum_subgroup K q n i _ hi


/-! ## `d(t)`: the permutation carrying the reference tableau to `t`

Murphy's `m_{st} = T_{d(s)}^* · x_λ · T_{d(t)}` needs, for each tableau `t`, the permutation
`d(t)` with `t = t^λ · d(t)`, where `t^λ` is a fixed reference tableau of shape `λ`.

Both exist already and the definition is a one-liner, because `Specht.Tableau μ` is *literally*
an `Equiv`: `Fin (nOf μ) ≃ μ.cells`. So two tableaux of the same shape differ by a permutation
of the labels, obtained by composing one with the other's inverse. The reference tableau is
`ColSuperstandardTableau.colSuperstandard`.
-/

open QOU.BraidKnot.ColSuperstandardTableau in
/-- **`d(t)`** — the permutation of labels carrying the column-superstandard reference tableau
`t^λ` to `t`. A composite of two `Equiv`s, since a tableau *is* an `Equiv`. -/
noncomputable def dOf {μ : YoungDiagram} (t : QOU.BraidKnot.Specht.Tableau μ) :
    Equiv.Perm (Fin (QOU.BraidKnot.Specht.nOf μ)) :=
  (colSuperstandard μ).trans t.symm

open QOU.BraidKnot.ColSuperstandardTableau in
/-- `d(t^λ) = 1`: the reference tableau is carried to itself by the identity. -/
@[simp] theorem dOf_colSuperstandard (μ : YoungDiagram) :
    dOf (colSuperstandard μ) = 1 :=
  Equiv.ext fun _ => by simp [dOf]

open QOU.BraidKnot.ColSuperstandardTableau in
/-- **The defining property of `d(t)`**: transporting the reference tableau along `d(t)`
recovers `t`. This is what makes `d` the right object to conjugate `x_λ` by. -/
theorem colSuperstandard_trans_dOf {μ : YoungDiagram}
    (t : QOU.BraidKnot.Specht.Tableau μ) :
    (dOf t).symm.trans (colSuperstandard μ) = t :=
  Equiv.ext fun _ => by simp [dOf]

/-- `d` is injective: distinct tableaux of the same shape give distinct permutations. This is
what will make the Murphy family indexed by *pairs of tableaux* rather than over-counted. -/
theorem dOf_injective {μ : YoungDiagram} :
    Function.Injective (dOf (μ := μ)) := by
  intro s t h
  have := congrArg (fun d => (Equiv.symm d).trans (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ)) h
  simpa [colSuperstandard_trans_dOf] using this

/-! ## The anti-involution on the `T_w` side, and `m_{st}`

`antiAut` (cellular axiom (C2), #6158) lives on the `IwahoriHeckeOfSn` presentation, while
`Tw`, `murphySum` and `basisTwOfSn` live on `QOU.Hecke.IwahoriHecke`. Murphy's
`m_{st} = T_{d(s)}^* · x_λ · T_{d(t)}` needs both at once, so the anti-involution has to be
carried across `algEquiv`.

Mathlib supplies the missing functor: `AlgEquiv.op : (A ≃ₐ[R] B) ≃ (Aᵐᵒᵖ ≃ₐ[R] Bᵐᵒᵖ)`. The
transport is then a three-step composite, and it is the last piece needed before `m_{st}` is
*definable* — which is what makes cellular axioms (C1) and (C3) statable at all.
-/

/-- **The cellular anti-involution, transported to the `T_w` presentation.**

`H → HoS → HoSᵐᵒᵖ → Hᵐᵒᵖ`, the outer two steps being `algEquiv` and its `AlgEquiv.op`. -/
noncomputable def antiAutTw :
    QOU.Hecke.IwahoriHecke K q n →ₐ[K] (QOU.Hecke.IwahoriHecke K q n)ᵐᵒᵖ :=
  ((AlgEquiv.op (QOU.BraidKnot.Hecke.algEquiv K q n)).toAlgHom).comp
    ((QOU.BraidKnot.Hecke.antiAut K q n).comp
      (QOU.BraidKnot.Hecke.algEquiv K q n).symm.toAlgHom)

/-- `d(t)` at the Hecke algebra's index — `dOf t` transported along `μ.card = n + 1`, the same
re-indexing `youngSubgroup` uses. -/
noncomputable def dAt {μ : YoungDiagram} (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (t : QOU.BraidKnot.Specht.Tableau μ) : Equiv.Perm (Fin (n + 1)) :=
  Equiv.permCongrHom (finCongr h) (dOf t)

/-- **Murphy's `m_{st}`**, at last definable: `T_{d(s)}^* · x_λ · T_{d(t)}`, with `*` the
transported cellular anti-involution and `x_λ` the Murphy element of `t`'s Young subgroup.

This is a *definition*, not a theorem. That the `m_{st}` form a basis is cellular axiom (C1)
and remains open; so does (C3). What has changed is that both can now be *written down* —
every ingredient is a named object rather than something to be built first. -/
noncomputable def murphyM {μ : YoungDiagram} (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (s t : QOU.BraidKnot.Specht.Tableau μ)
    [DecidablePred (· ∈ youngSubgroup n h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ))] :
    QOU.Hecke.IwahoriHecke K q n :=
  (antiAutTw K q n (Tw K q n (dAt n h s))).unop
    * murphySum K q n {w | w ∈ youngSubgroup n h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ)}
    * Tw K q n (dAt n h t)

/-! ## Toward (C1): the Murphy family has exactly the right size

Cellular axiom (C1) asks that `{m_{st}}`, indexed by **pairs of standard tableaux of the same
shape**, be a **basis** of `H_n(q)`. A basis claim is two claims — spanning and independence —
but for a finite family in a finite-dimensional space, either one plus a **cardinality match**
gives the other. So the cheap half is worth isolating.

Both ingredients already exist in this corpus, and neither had to be built:

* `QOU.Mathlib.rskBurnsideHolds` — `∑_{p ⊢ n} (#SYT p)² = n!`, the RSK/Burnside identity, proved
  for **every** `n` from a Robinson–Schensted correspondence built in-repo (the pinned Mathlib has
  no RSK). That sum counts exactly the pairs `(s,t)` of standard tableaux of a common shape — the
  Murphy index set.
* `QOU.Hecke.TwBasis.finrank_eq_factorial` — `dim_K H_n(q) = (n+1)!`, transported to the other
  presentation on #6158 as `basisTwOfSn`.

Putting them together is two lines, and the content is worth stating plainly: **the Murphy family
is not over- or under-counted.** (C1) therefore reduces from *"is a basis"* to *"spans"* **or**
*"is independent"* — whichever is easier — with the other following by dimension count. That is a
real reduction of the remaining work, obtained entirely from results the corpus already held.
-/

/-- **The Murphy index set has exactly `dim_K H_n(q)` elements.**

The left side counts pairs of standard tableaux of a common shape — the `(s,t)` indexing
`murphyM` — via the RSK/Burnside identity; the right is the Hecke algebra's dimension. Their
agreement is what makes (C1) a one-sided question. -/
theorem murphyIndex_card_eq_finrank :
    ∑ p : Nat.Partition (n + 1), (QOU.Mathlib.dimSYT p) ^ 2
      = Module.finrank K (QOU.Hecke.IwahoriHecke K q n) := by
  rw [QOU.Hecke.TwBasis.finrank_eq_factorial K q n]
  exact QOU.Mathlib.rskBurnsideHolds (n + 1)

/-! ## The Murphy index as a type — making (C1) a `Basis` statement

`murphyIndex_card_eq_finrank` above compares a *sum* to a dimension. To state (C1) as what it
actually is — `Module.Basis I K (H_n q)` — the index must be a **type**, and its cardinality
must be the same `n!`.

`MurphyIndex n` is that type: a partition together with an **ordered pair** of standard tableaux
of its shape, which is exactly the `(s,t)` that `murphyM` consumes. Its cardinality is the RSK
sum, so (C1) can now be written down as a basis claim over a type of known size.
-/

/-- **The Murphy index**: a partition of `n`, with an ordered pair of standard tableaux of that
shape. Exactly the data `murphyM` takes. -/
def MurphyIndex (n : ℕ) : Type :=
  Σ p : Nat.Partition n,
    QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape p) ×
      QOU.Mathlib.StandardYoungTableau (QOU.Mathlib.partitionShape p)

instance (n : ℕ) : Finite (MurphyIndex n) := by
  unfold MurphyIndex; infer_instance

/-- **`#MurphyIndex n = n!`** — the index type has exactly the dimension of `H_{n-1}(q)`.

`Nat.card` of a sigma of pairs is `∑_p (#SYT p)²`, which is the RSK/Burnside identity. So the
Murphy family is indexed by a type of exactly the right size, and (C1) — `Module.Basis
(MurphyIndex (n+1)) K (H_n q)` — is a well-posed claim whose two halves each imply the other. -/
theorem murphyIndex_card (n : ℕ) : Nat.card (MurphyIndex n) = n.factorial := by
  have h : Nat.card (MurphyIndex n)
      = ∑ p : Nat.Partition n, (QOU.Mathlib.dimSYT p) ^ 2 := by
    unfold MurphyIndex QOU.Mathlib.dimSYT QOU.Mathlib.numStandardYoungTableaux
    rw [Nat.card_sigma]
    exact Finset.sum_congr rfl fun p _ => by rw [Nat.card_prod, sq]
  rw [h]
  exact QOU.Mathlib.rskBurnsideHolds n

/-! ## The anchor of the family: `m_{t^λ t^λ} = x_λ`

The triangularity argument that gives (C1) is an induction over the dominance order, and every
such induction needs a base. Here it is the **reference pair**: at `s = t = t^λ` the conjugating
factors collapse, because `d(t^λ) = 1` and `T_1 = 1`, so `m_{st}` is `x_λ` itself.

Cheap, but load-bearing twice over: it anchors the induction, and it is the first check that
`murphyM` was assembled correctly — if the conjugation were mis-oriented, this would not reduce.
-/

@[simp] theorem dAt_colSuperstandard {μ : YoungDiagram}
    (h : QOU.BraidKnot.Specht.nOf μ = n + 1) :
    dAt n h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ) = 1 := by
  rw [dAt, dOf_colSuperstandard, map_one]

/-- **`m_{t^λ, t}` drops its left factor.** `d(t^λ) = 1`, so `T_{d(t^λ)}^* = 1`. -/
theorem murphyM_colSuperstandard_left {μ : YoungDiagram}
    (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (t : QOU.BraidKnot.Specht.Tableau μ)
    [DecidablePred (· ∈ youngSubgroup n h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ))] :
    murphyM K q n h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ) t
      = murphySum K q n {w | w ∈ youngSubgroup n h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ)} * Tw K q n (dAt n h t) := by
  simp [murphyM]

/-- **The anchor: `m_{t^λ t^λ} = x_λ`.** Both conjugating factors are `1`, so the reference pair
of the Murphy family is the Murphy element itself — the base case of the dominance induction. -/
theorem murphyM_colSuperstandard_diag {μ : YoungDiagram}
    (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    [DecidablePred (· ∈ youngSubgroup n h
      (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ))] :
    murphyM K q n h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ)
        (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ)
      = murphySum K q n {w | w ∈ youngSubgroup n h
          (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ)} := by
  simp [murphyM]

/-! ## Coefficients in the `T_w` basis

The triangularity argument behind (C1) is entirely a statement about **coefficients**: `m_{st}`
should expand in `{T_w}` with a unit diagonal entry and strictly-dominance-lower off-diagonal
ones. So the first thing needed is the ability to read a coefficient off, and the first object
whose coefficients are worth knowing is `x_λ` itself.

They are as simple as possible — `x_λ` is a **sum of distinct basis vectors**, so its coordinate
function is the indicator of the summation set. `coe_basisTwOfField` is what makes this immediate:
the basis vectors *are* the `T_w`.
-/

/-- **The coordinates of `x_S` in the `T_w` basis are the indicator of `S`.**

Immediate, because `x_S = ∑_{w ∈ S} T_w` is a sum of *distinct* basis vectors — but it is the
computation every later coefficient argument starts from. -/
theorem repr_murphySum (S : Finset (Equiv.Perm (Fin (n + 1))))
    (w : Equiv.Perm (Fin (n + 1))) :
    (QOU.Hecke.TwBasis.basisTwOfField K q n).repr (murphySum K q n S) w
      = if w ∈ S then 1 else 0 := by
  have hb : ∀ v : Equiv.Perm (Fin (n + 1)),
      Tw K q n v = QOU.Hecke.TwBasis.basisTwOfField K q n v := by
    intro v
    rw [QOU.Hecke.TwBasis.coe_basisTwOfField]
  simp only [murphySum, hb, map_sum, Finsupp.coe_finset_sum, Finset.sum_apply,
    Module.Basis.repr_self, Finsupp.single_apply]
  simp [Finset.sum_ite_eq, eq_comm]

/-- **`T_1` appears in `x_S` with coefficient `1`** whenever `S` is a subgroup — in particular for
a Young subgroup, since `1 ∈ S_λ`.

This is the candidate leading term: every `x_λ` has a distinguished unit coefficient, which is
what a triangularity argument needs at the diagonal. -/
theorem repr_murphySum_one_of_subgroup
    (H : Subgroup (Equiv.Perm (Fin (n + 1)))) [DecidablePred (· ∈ H)] :
    (QOU.Hecke.TwBasis.basisTwOfField K q n).repr
        (murphySum K q n {w | w ∈ H}) 1 = 1 := by
  rw [repr_murphySum]
  simp

/-! ## The index bridge, and `lead`

`murphyIndex_card` above matches **cardinalities**. To get `lead` we need the **bijection**, and
every piece of it already exists — this is assembly, not construction.

* `Equiv.subtypeSigmaEquiv` (Mathlib) turns a subtype of a `Σ` into a `Σ` over a subtype;
* `partitionShapeEquiv` (`SchenstedPartitionShape`) re-indexes Young diagrams with `n` cells by
  `Nat.Partition n`, and its `_apply` lemma is `rfl`, so the fibres match definitionally;
* `Schensted.rskEquiv` (`SchenstedRSKEquiv`) is the Robinson–Schensted correspondence itself.

The first two are exactly the composition inside `card_pairs_eq_sum`'s proof, used there only for
its effect on cardinalities. Lifting it to the `Equiv` costs nothing.

## Why this is the answer to `lead_inj`

`Triangular`'s `α` is forced to be the **basis index type** — its field is `v : ι → (α →₀ R)`, so
`α` is whatever indexes the coordinate vectors, here `Equiv.Perm (Fin (n+1))`. `lead` therefore
cannot carry `λ` alongside; it must land in permutations. Since
`|MurphyIndex m| = m! = |S_m|`, **injective ⟺ bijective**, and the canonical bijection between
permutations and same-shape tableau pairs is RSK.

So `lead := murphyIndexEquivPerm` is injective **because it is an `Equiv`** — `lead_inj` is
discharged by `Equiv.injective`, with no combinatorial argument at all.

This is what refutes the earlier candidate `d(s)⁻¹ w_λ d(t)`: that map could never have been a
bijection, because `λ ↦ w_λ` already collapses distinct partitions
(`computations/hecke/murphy_lead_injectivity_probe.py`).
-/

/-- **The index bridge**: RSK's codomain is `MurphyIndex n`, re-indexed.

`{X : Σ μ, SYT μ × SYT μ // X.1.cells.card = n} ≃ MurphyIndex n`, by `subtypeSigmaEquiv` then
`partitionShapeEquiv`. Both steps are already used, for their cardinality shadow only, inside
`QOU.Mathlib.card_pairs_eq_sum`. -/
noncomputable def murphyIndexEquivRSKCodomain (n : ℕ) :
    {X : (Σ μ : YoungDiagram,
        QOU.Mathlib.StandardYoungTableau μ × QOU.Mathlib.StandardYoungTableau μ) //
      X.1.cells.card = n} ≃ MurphyIndex n :=
  (Equiv.subtypeSigmaEquiv
      (fun μ : YoungDiagram =>
        QOU.Mathlib.StandardYoungTableau μ × QOU.Mathlib.StandardYoungTableau μ)
      (fun μ : YoungDiagram => μ.cells.card = n)).trans
    (Equiv.sigmaCongrLeft' (QOU.Mathlib.partitionShapeEquiv n).symm)

/-- **`MurphyIndex n ≃ S_n`** — the Robinson–Schensted correspondence, stated on the index type
the Murphy family actually uses. -/
noncomputable def murphyIndexEquivPerm (n : ℕ) :
    MurphyIndex n ≃ Equiv.Perm (Fin n) :=
  (murphyIndexEquivRSKCodomain n).symm.trans (QOU.Mathlib.Schensted.rskEquiv n).symm

/-- **`lead`** — the leading permutation of a Murphy basis element, taken to be its RSK image.

Landing in `Equiv.Perm (Fin n)` is forced: it is the index type of the `T_w` basis, hence of the
coordinate vectors `Triangular` quantifies over. -/
noncomputable def lead (n : ℕ) : MurphyIndex n → Equiv.Perm (Fin n) :=
  murphyIndexEquivPerm n

/-- **`lead_inj`** — cellular axiom (C1)'s first `Triangular` field, discharged.

No combinatorial content: `lead` is an `Equiv`, so injectivity is `Equiv.injective`. The work was
in identifying the right map, not in proving this. -/
theorem lead_injective (n : ℕ) : Function.Injective (lead n) :=
  (murphyIndexEquivPerm n).injective

/-! ## 8. The Murphy family, and the route to (C1) that Mathas actually takes

### Why `Triangular` is NOT the route — a measured refutation

The obvious plan was to feed `m_{st}` to the corpus's linear-independence lever
`QOU.BraidKnot.SpechtStandardBasis.Triangular` against the `T_w` basis, with the RSK
bijection `lead` of §7 as the leading map. `lead_inj` is then free (`lead_injective`).
**That plan is dead, and not merely for RSK.** An exact enumeration of the `T_w`-supports
of every `m_{st}` — `computations/hecke/murphy_supp_rsk_probe.py`, integer arithmetic
throughout, complete at `n = 3, 4, 5` — establishes both halves:

* **RSK is not even a legal leading map.** `diag_unit` forces `lead x ∈ supp (m x)`, and
  `RSK⁻¹(s,t)` lies in that support for only `1/6`, `3/24`, `11/120` of the indices
  (`11/120` with the other `(P,Q)` orientation: `3/6`, `9/24`, `23/120`). The smallest
  witness is hand-checkable: at `n = 3`, `λ = (2,1)`, `s = t = tλ`, we have
  `d(s) = d(t) = 1`, so `m_{st} = x_λ = T_1 + T_{s₁}` with support `{1, s₁}`, while
  `RSK⁻¹(s,t) = s₂`, which is not in it.
* **No leading map works at all.** If `(≤, lead)` satisfied `Triangular`, the order's
  maximum `M` would satisfy: `M ∈ supp (m x) → lead x = M`, so by injectivity `M` lies in
  **exactly one** support; deleting that index and `M` leaves the same problem one size
  down. So a `Triangular` structure exists iff this peeling never stalls. At `n = 3` it
  stalls immediately — each of the six permutations lies in **at least two** of the six
  supports (multiplicities `4, 2, 4, 2, 2, 2`), because `x_{(3)} = Σ_{w ∈ S₃} T_w` alone
  already has full support. It stalls after 1 of 24 indices at `n = 4` and 5 of 120 at
  `n = 5`.

This is a **scope-(b) structural exclusion** in the sense of AGENTS.md: the invariant cited
is the peeling argument above (the order-maximum must lie in exactly one support), and the
`n = 3` check is exhaustive rather than sampled. It excludes *this lever applied to this
pair of bases* — it says nothing against the Murphy basis itself, which is a theorem.

### The route that does work

Mathas takes the other road, and it needs no triangularity ([mathas1999], Thm 3.20):

> *"Lemma 3.9 and Lemma 3.14 show that `M` spans `H`. By Theorem 1.11 we know that `H` is a
> free `R`-module of rank `n!`. However `|M| = Σ_λ |Std(λ)|²` and it is well-known that this
> sum is equal to `n!` (for example, use the Robinson–Schensted correspondence). Thus `M` is
> a basis of `H`."*

Every ingredient but spanning is already sorry-free in this corpus:

| Mathas' ingredient | here |
|---|---|
| `H` free of rank `n!` | `QOU.Hecke.TwBasis.finrank_eq_factorial` |
| `Σ_λ (f^λ)² = n!` via RSK | `murphyIndex_card`, `murphyIndexEquivPerm` |
| spanning | **open** — the one remaining input |

So `basisOfSpanning` below is the whole of (C1) *given* spanning, and it is a genuine
derivation rather than an assumption dressed up: the hypothesis is Mathas' Lemma 3.14, the
conclusion (`Module.Basis`) is derived from it together with the two counts. -/

open QOU.BraidKnot.SpechtStandardBasis (sytToTableau) in
/-- The family `m_{st}` built from `murphyM`, indexed by `MurphyIndex (n + 1)` — a partition
of `n + 1` with an ordered pair of standard tableaux of that shape, which is Murphy's index
set. The two `StandardYoungTableau` types in the corpus are reconciled by
`NumSYTBridge.toBraidKnotSYT`, and the filling by `SpechtStandardBasis.sytToTableau`.

**Corrected 2026-08-31.** `murphyM` previously summed over `youngSubgroup n h t` —
the *second tableau's own* row stabiliser, a different conjugate subgroup for each `t`,
where Murphy's `x_λ` is **one fixed** subgroup for every pair of the shape. That family was
rank-deficient at every `n` tested (`5/6`, `23/24`, `117/120`), so it could not span and was
not Murphy's family. It now sums over the reference tableau's row stabiliser.

The guard that caught it is `run_rank_guard` in
`computations/hecke/murphy_supp_rsk_probe.py` (exact arithmetic at `q = 7`): the fixed-`x_λ`
family is full rank `6/6`, `24/24`, `120/120`. **That is evidence, not proof** — it says the
spanning hypothesis below is no longer measured *unsatisfiable*, not that it holds for all
`n`, which is Mathas' Lemma 3.14 and still open.

Note the reference tableau itself is a red herring: `colSuperstandard` (column-major) is as
good as Murphy's row-superstandard `t^λ` — both are full rank. The subgroup was the defect.
Audit: `docs/audits/2026-08-31-murphy-basis-triangular-lever-refuted.md` §3-ter. -/
noncomputable def murphyFamily (x : MurphyIndex (n + 1)) :
    QOU.Hecke.IwahoriHecke K q n := by
  classical
  exact murphyM K q n (QOU.Mathlib.partitionShape_card x.1)
    (sytToTableau (toBraidKnotSYT x.2.1)) (sytToTableau (toBraidKnotSYT x.2.2))

noncomputable instance instFintypeMurphyIndex (n : ℕ) : Fintype (MurphyIndex n) :=
  Fintype.ofEquiv _ (murphyIndexEquivPerm n).symm

/-- `#MurphyIndex n = n!` as a `Fintype.card` — the `Nat.card` form is `murphyIndex_card`.
This is Mathas' `|M| = Σ_λ |Std(λ)|² = n!`, transported along RSK. -/
theorem murphyIndex_fintypeCard (n : ℕ) : Fintype.card (MurphyIndex n) = n.factorial := by
  classical
  rw [Fintype.card_congr (murphyIndexEquivPerm n), Fintype.card_perm, Fintype.card_fin]

/-- **(C1) modulo spanning** — Murphy's basis theorem, reduced to its one open input.

A family indexed by `MurphyIndex (n + 1)` that spans `H_n(q)` **is** a basis, because the
index set has exactly `finrank` elements. Stated for an arbitrary family `m` so that the
reduction is visibly independent of what `m` is; `murphyBasisOfSpanning` specialises it to
`murphyFamily`. Nothing here assumes the conclusion: spanning goes in, a `Basis` comes out,
and the bridge between them is `murphyIndex_fintypeCard` + `finrank_eq_factorial`. -/
noncomputable def basisOfSpanning (m : MurphyIndex (n + 1) → QOU.Hecke.IwahoriHecke K q n)
    (hspan : ⊤ ≤ Submodule.span K (Set.range m)) :
    Module.Basis (MurphyIndex (n + 1)) K (QOU.Hecke.IwahoriHecke K q n) := by
  classical
  refine basisOfTopLeSpanOfCardEqFinrank m hspan ?_
  rw [murphyIndex_fintypeCard, QOU.Hecke.TwBasis.finrank_eq_factorial]

/-- **The Murphy basis, given Mathas' spanning lemma (Thm 3.20).**

Spanning goes in as an explicit hypothesis and the `Module.Basis` comes out, derived from it
together with `murphyIndex_fintypeCard` and `finrank_eq_factorial`. The conclusion is not
among the hypotheses, so this is a derivation, not an assumption dressed as infrastructure.

What it does **not** claim: that anything spans. `murphyFamily` is now measured full rank at
`n = 3, 4, 5` (see its docstring), so the hypothesis is at least satisfiable-looking, but
Lemma 3.14 is the open input and this lemma is silent about it —
"conditional-proved ≠ premise-established". `basisOfSpanning` above is the same statement for
an arbitrary family, and is the form to reach for when the family is not yet fixed. -/
noncomputable def murphyBasisOfSpanning
    (hspan : ⊤ ≤ Submodule.span K (Set.range (murphyFamily K q n))) :
    Module.Basis (MurphyIndex (n + 1)) K (QOU.Hecke.IwahoriHecke K q n) :=
  basisOfSpanning K q n (murphyFamily K q n) hspan

/-- Linear independence given spanning — the (C1) half the `Triangular` route was meant to
supply. Same standing caveat as `murphyBasisOfSpanning`: it proves `spans → independent`, and
says nothing about whether the family spans. -/
theorem murphyFamily_linearIndependent
    (hspan : ⊤ ≤ Submodule.span K (Set.range (murphyFamily K q n))) :
    LinearIndependent K (murphyFamily K q n) := by
  classical
  refine linearIndependent_of_top_le_span_of_card_eq_finrank hspan ?_
  rw [murphyIndex_fintypeCard, QOU.Hecke.TwBasis.finrank_eq_factorial]


/-! ## 9. Step 2 of spanning: the one-column shape already gives every `T_w`

Mathas' spanning argument (the input `basisOfSpanning` is missing) is three steps, and the
first is already in the corpus. Reading the statements rather than the sentence that cites
them:

1. **`{T_w}` spans `H_n(q)`** — `QOU.Hecke.TwBasis.basisTwOfField`.
2. **Every `T_w` *is* a Murphy element of the one-column shape** — this section.
3. **Lemma 3.14** straightens row-standard pairs to standard ones, moving up in dominance.
   Since `(1ⁿ)` is the dominance-minimum, everything is reachable from step 2.

Step 2 is where the one-column shape earns its place. Its Young subgroup is **trivial** — every
row has length one, so the row stabiliser is `{1}` — hence `x_{(1ⁿ)} = T_1 = 1` and
`m_{st} = T_{d(s)}^* · 1 · T_{d(t)}`. Every filling of a single column is row-standard, so
`d(t)` ranges over the whole symmetric group; taking `s` to be the reference tableau gives
`m = T_{d(t)}`, i.e. every basis element. So the **row-standard** Murphy family spans
immediately, and spanning reduces to straightening alone.

> **The index set is the catch, and it is not a technicality.** Steps 2 and 3 concern the family
> indexed by **row-standard** pairs — `n!` per shape — whereas `MurphyIndex` and `murphyFamily`
> are over **standard** pairs, `(f^λ)²` per shape. At the one-column shape the standard family
> has exactly **one** element where the row-standard family has `n!`. So spanning cannot even be
> *stated* for `murphyFamily` directly; a row-standard-indexed family has to exist first, and the
> corpus has no row-standard tableau type. That gap is the whole of step 3, not an indexing
> detail. Bean `qou-phir`.

What is proved here is the algebraic core of step 2, which needs no such type: the trivial
Young subgroup contributes `1`, and the two-sided conjugates of that `1` already span. -/

/-- **The trivial Young subgroup contributes `1`.** `x_{(1ⁿ)} = Σ_{w ∈ {1}} T_w = T_1 = 1`.

The one-column shape `(1ⁿ)` has every row of length one, so its row stabiliser is trivial and
its Murphy element is the identity — which is what makes step 2 of the spanning argument free. -/
@[simp] theorem murphySum_singleton_one :
    murphySum K q n {1} = 1 := by
  rw [murphySum, Finset.sum_singleton, Tw_one]

/-- **Step 2: the one-column Murphy elements already span `H_n(q)`.**

`{T_u · x_{(1ⁿ)} · T_v}` spans, because `x_{(1ⁿ)} = 1` and the `T_w` are a basis: take `u = 1`
and the family already contains every `T_v`. So the row-standard Murphy family spans as soon as
the `T_w` do, and **the whole of the spanning input to `basisOfSpanning` is Lemma 3.14's
straightening** — moving a row-standard pair to standard pairs of dominating shape.

Stated over the conjugating pair rather than over tableaux precisely because the row-standard
tableau type does not exist yet (see the section note): this is the algebraic content, and it
does not have to wait for the indexing. -/
theorem span_murphySum_one_conjugates_eq_top :
    Submodule.span K (Set.range (fun p : Equiv.Perm (Fin (n + 1)) × Equiv.Perm (Fin (n + 1)) =>
        Tw K q n p.1 * murphySum K q n {1} * Tw K q n p.2)) = ⊤ := by
  classical
  refine top_le_iff.mp ?_
  rw [← (QOU.Hecke.TwBasis.basisTwOfField K q n).span_eq]
  refine Submodule.span_le.mpr ?_
  rintro x ⟨v, rfl⟩
  refine Submodule.subset_span ⟨(1, v), ?_⟩
  simp


end QOU.BraidKnot.HeckeMurphyYoung
