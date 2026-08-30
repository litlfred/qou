import QOU.BraidKnot.HeckeMurphy
import QOU.BraidKnot.Specht
import QOU.BraidKnot.ColSuperstandardTableau
import QOU.BraidKnot.HeckeCellular
import QOU.BraidKnot.HeckeTypeAPresentationEquiv
import QOU.Mathlib.SchenstedRSKBurnside

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
    [DecidablePred (· ∈ youngSubgroup n h t)] :
    QOU.Hecke.IwahoriHecke K q n :=
  (antiAutTw K q n (Tw K q n (dAt n h s))).unop
    * murphySum K q n {w | w ∈ youngSubgroup n h t}
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

end QOU.BraidKnot.HeckeMurphyYoung
