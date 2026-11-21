import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.Notation
import QOU.Archimedean.HyperbolicVolumeIndependence

/-!
# QOU.Archimedean.JetOrderIndependence — the gap-closing reduction

**§3b-cond conditional theorem** for content block
[`conj:three-knot-jet-order-independence`](../../../quantum-observable-universe/predicted-spectra/three-knot-jet-order-independence.md):
*Jet-order algebraic independence (QOU-attackable reduction)*.

This file formalises the **reduction** that closes the deep
algebraic-independence conjecture
([`conj:hyperbolic-volume-transcendence`](../../../quantum-observable-universe/mass-theory/hyperbolic-volume-transcendence.md))
*relative to two narrower, QOU-native inputs*:

1. `JetOrderIndependence` — finite jet-order independence: the order-`N`
   cyclotomic-coefficient Jacobian of the three coloured-Jones series
   `J_{4₁}, J_{5₂}, J_{𝓑₃}` has full rank `3` from the Reid-1991 base
   order onward. Decidable per order (a Gröbner–Shirshov normal form),
   so this is the QOU-*attackable* weakening.
2. `SurrealParallelTransportBound` — the **bridge**: the surreal
   parallel-transport error of the categorical connection on the
   projective state fibre `ℂP¹`, as `q` deforms toward the
   root-of-unity (volume-conjecture) limit, has vanishing archimedean
   shadow, uniformly in the jet order.

The reduction `hyperbolicVolumeIndependence_of_reduction` derives
`HyperbolicVolumeIndependence` from these two *plus the bridge step*
`JetTransportImpliesIndependence` (the Nesterenko-type transfer from
finite jet data to the infinite-order polynomial statement), each
conjectural per §3b-cond. It does NOT prove the deep conjecture; it
converts a Grothendieck-period dead end into named internal QOU
targets whose conditional structure is visible at every call site.

## The surreal parallel-transport bound — geometric content + open issues

The coloured-Jones invariant `J_K(q)` is the **holonomy** of the
categorical (Yekutieli non-abelian Stokes / KZ) connection, parallel-
transported along the substrate `q`-deformation path on the projective
state fibre `𝒮 = P ×_G ℂP¹`. The hyperbolic volume is the leading
asymptotics of that holonomy at the singular limit:
`Vol(K) = lim_{n→∞} (2π/n)·log|J_K(e^{2πi/n})|`. The **surreal error
bound** measures the transport error as `q` approaches that singular
(root-of-unity) point; it is surreal (non-Archimedean) precisely
because the limit point is a singularity of the connection, so the
error is an *infinitesimal* in the surreal field, not a real number.

The class field `transportShadow N` is the **archimedean realification**
(`τ`-shadow) of that fibre-level surreal infinitesimal at jet order `N`.
The conjectural content `shadow_vanishes` packages the three open issues
that must hold for the bridge:

- **(I1) Uniformity in jet order.** The transport error must be bounded
  *uniformly* across all truncation orders `N`; otherwise order-`N`
  independence does not transfer to the limit. On `ℂP¹` this is uniform
  control of the connection's curvature along the deformation path,
  independent of `N`. Non-uniform error growing with `N` breaks the
  bridge.
- **(I2) Archimedean projection (the fibre-vs-observable wall).** The
  error lives at the **fibre** level (surreal, possibly carrying the
  `Im(q)` structure of AGENTS.md's fibre/archimedean box); the volume is
  **archimedean** (`Im(q₀)=0`, real). The bridge needs the surreal
  infinitesimal to project to *exactly* `0` under `τ`. A non-infinitesimal
  archimedean shadow injects a spurious polynomial relation among the
  volumes and independence fails — this is why the field is named a
  *shadow*.
- **(I3) Monodromy separation at the singular limit.** Transport around
  the cusp is flat only at generic `q`; at the root-of-unity limit the
  holonomy picks up cusp/modular monodromy. The bound must separate the
  physical holonomy (`→ Vol`) from the monodromy artifact. Open: is the
  monodromy contribution surreal-controlled, or does it leak into the
  real volume?

`shadow_vanishes : ∀ N, transportShadow N = 0` is the assertion that
(I1)+(I2)+(I3) all hold — the single conjectural input of the bridge.
-/

namespace QOU.Archimedean

/-- **Jet-order independence (weak, QOU-attackable conjecture).**

    `jacobianRank N` is the rank of the order-`N` cyclotomic-coefficient
    Jacobian of the three coloured-Jones series `J_{4₁}, J_{5₂}, J_{𝓑₃}`
    (a `3 × (N+1)` matrix over `ℚ[q,q⁻¹]`). `full_rank` asserts it is the
    full rank `3` from the Reid-1991 base order `N ≥ 3` onward — finite
    and decidable per order via a Gröbner–Shirshov elimination normal
    form. -/
class JetOrderIndependence where
  /-- Rank of the order-`N` coefficient Jacobian of the three series. -/
  jacobianRank : ℕ → ℕ
  /-- Full rank `3` from the base order onward (Reid-1991 anchors `N=3`). -/
  full_rank : ∀ N, 3 ≤ N → jacobianRank N = 3

/-- **Transport-error data — the shadows as *given* data (2026-08-09).**

    `shadow N` is the archimedean (`τ`) realification of the fibre-level
    surreal parallel-transport error on the projective state fibre `ℂP¹` at
    jet order `N`, as `q` deforms toward the volume-conjecture limit, split
    into its physical-holonomy (`→ Vol`) and cusp/modular-monodromy parts.

    **Why a structure and not class fields.**  The conjecture is about *one
    specific* object — the transport error of the categorical connection.
    When the shadows are *fields of the class*, an instance gets to **choose**
    the very functions it is supposed to constrain, and the constant-zero
    choice satisfies everything by `rfl`.  That is precisely how the previous
    encoding was discharged for free.  Carrying them as data, and taking that
    data as a **class parameter** below, forces every consumer to name the
    error it is assuming about. -/
structure TransportErrorData where
  /-- Archimedean (`τ`) shadow of the surreal transport error at order `N`. -/
  shadow : ℕ → ℝ
  /-- Physical-holonomy part of the shadow (the `→ Vol` contribution). -/
  physical : ℕ → ℝ
  /-- Cusp/modular-monodromy part of the shadow (the limit-only artifact). -/
  monodromy : ℕ → ℝ
  /-- **(I3) Monodromy separation.**  The shadow splits into its physical and
      monodromy parts.  This is a *structural* property of the supplied data,
      not a conjectural input. -/
  decomposes : ∀ N, shadow N = physical N + monodromy N

/-- **Surreal parallel-transport bound (the bridge), as a predicate ON given
    error data.**

    The two conjectural inputs (I2) and (I3-second) are asserted *about the
    supplied* `E`; the class can no longer manufacture its own shadow.
    (I1 uniformity and the composition are derived below.) -/
class SurrealParallelTransportBound (E : TransportErrorData) : Prop where
  /-- **(I2) Archimedean projection (fibre-vs-observable wall).**  The
      physical part is a fibre-level surreal infinitesimal, so its
      archimedean shadow `τ`-projects to `0`.  *Conjectural input.* -/
  physical_archimedean_zero : ∀ N, E.physical N = 0
  /-- **(I3, second half) Monodromy is fibre-level.**  The cusp/modular
      monodromy carries `Im(q)` structure but no real shadow.
      *Conjectural input.* -/
  monodromy_archimedean_zero : ∀ N, E.monodromy N = 0

namespace SurrealParallelTransportBound

variable {E : TransportErrorData}

/-- **(I3 ∘ I2 composition — PROVED).**  The total transport shadow of `E`
    vanishes at every order, from `E`'s structural decomposition together with
    both parts' archimedean shadows vanishing. -/
theorem transport_shadow_vanishes [PT : SurrealParallelTransportBound E]
    (N : ℕ) : E.shadow N = 0 := by
  rw [E.decomposes N, PT.physical_archimedean_zero N,
      PT.monodromy_archimedean_zero N]
  norm_num

/-- **(I1) Uniformity in jet order — PROVED (derived).**  With the per-order
    shadow vanishing, the transport error is uniformly bounded across all jet
    orders (with constant `0`); no `N`-dependent blow-up can corrupt the limit
    transfer. -/
theorem transport_uniform_bound [SurrealParallelTransportBound E] :
    ∃ C : ℝ, ∀ N, |E.shadow N| ≤ C :=
  ⟨0, fun N => by simp [transport_shadow_vanishes (E := E) N]⟩

/-! ### The residual vacuity, stated as a theorem rather than left as a trap

Parameterising stops the class from *choosing* its shadow, but it cannot stop
a consumer from instantiating at the zero error.  Rather than leave that as a
latent trap — the shape that let the previous encoding pass every audit — it
is recorded below as a pair of theorems.  Read together they say exactly what
an instance is worth: **`[SurrealParallelTransportBound E]` carries no
information until `E` is pinned down**, and it carries real information as
soon as it is. -/

/-- The identically-zero transport error. -/
def trivialError : TransportErrorData where
  shadow := fun _ => 0
  physical := fun _ => 0
  monodromy := fun _ => 0
  decomposes := fun _ => by norm_num

/-- **The bound is vacuous at the zero error (PROVED).**  So an instance
    `[SurrealParallelTransportBound E]` for an *unspecified* `E` asserts
    nothing: it is satisfiable.  Any downstream result must say which `E`. -/
instance trivialError_bound : SurrealParallelTransportBound trivialError where
  physical_archimedean_zero := fun _ => rfl
  monodromy_archimedean_zero := fun _ => rfl

/-- **…and non-vacuous at any error with a non-zero physical shadow
    (PROVED).**  This is the content the parameterisation buys: for a
    *specific* `E` coming from the actual connection, the bound is a real
    constraint that can fail. -/
theorem not_bound_of_physical_ne_zero {N : ℕ} (h : E.physical N ≠ 0) :
    ¬ Nonempty (SurrealParallelTransportBound E) :=
  fun ⟨PT⟩ => h (PT.physical_archimedean_zero N)

/-- **Non-vacuity on the monodromy channel (`qou-ufm1`).**
Any non-zero monodromy shadow `E.monodromy N ≠ 0` refutes
`SurrealParallelTransportBound E`. -/
theorem not_bound_of_monodromy_ne_zero {N : ℕ} (h : E.monodromy N ≠ 0) :
    ¬ Nonempty (SurrealParallelTransportBound E) :=
  fun ⟨PT⟩ => h (PT.monodromy_archimedean_zero N)

/-- **Non-vacuity on the total shadow (`qou-ufm1`).**
Because `E.shadow N = E.physical N + E.monodromy N`, any non-zero total shadow
`E.shadow N ≠ 0` refutes `SurrealParallelTransportBound E`. -/
theorem not_bound_of_shadow_ne_zero {N : ℕ} (h : E.shadow N ≠ 0) :
    ¬ Nonempty (SurrealParallelTransportBound E) :=
  fun ⟨PT⟩ => h (@transport_shadow_vanishes E PT N)

/-- **Exact characterisation of `SurrealParallelTransportBound E` (`qou-ufm1`).**
The parameterised class is inhabited if and only if both the physical and
monodromy shadows of `E` vanish at every jet order `N`. -/
theorem surrealParallelTransportBound_iff :
    Nonempty (SurrealParallelTransportBound E) ↔
      (∀ N, E.physical N = 0) ∧ (∀ N, E.monodromy N = 0) := by
  constructor
  · rintro ⟨PT⟩
    exact ⟨PT.physical_archimedean_zero, PT.monodromy_archimedean_zero⟩
  · rintro ⟨hphys, hmono⟩
    exact ⟨⟨hphys, hmono⟩⟩

end SurrealParallelTransportBound

/-- **Gap-closing reduction — the bridge step (§3b conjectural class).**

    The Nesterenko-type transfer: *given* finite jet-order independence
    and the surreal parallel-transport bound, the full algebraic
    independence `no_relation` follows.  The transfer from the finite
    jet data + vanishing fibre shadow to the infinite-order polynomial
    statement is the bridge's mathematical content; it is recorded as a
    conjectural class so the conditional structure is visible at every
    call site (per §3b-cond).

    **History (2026-06-10).**  An earlier version "derived"
    `HyperbolicVolumeIndependence` here as a 5-line `def` — but only
    against a vacuous placeholder shape of that class
    (`residual = 0`), which made the reduction appear Lean-verified
    while carrying no mathematical content.  With the real class
    (`no_relation`, declared in `HyperbolicVolumeTranscendence` §7)
    the bridge step is honestly conjectural. -/
class JetTransportImpliesIndependence (E : TransportErrorData)
    [JetOrderIndependence] [SurrealParallelTransportBound E] : Prop where
  /-- The independence witness produced by the bridge. -/
  nonempty_independence : Nonempty HyperbolicVolumeIndependence

/-- **Gap-closing reduction (§3b-cond conditional form).**

    The deep algebraic-independence conjecture `HyperbolicVolumeIndependence`
    follows from the two QOU-native inputs — finite jet-order independence
    (`full_rank`) and the surreal parallel-transport bound (reduced to its
    two named physical inputs (I2)+(I3), with (I1) + composition proved as
    `transport_shadow_vanishes`) — *modulo the bridge step*
    `JetTransportImpliesIndependence`.  It is a `def` (not an `instance`)
    to avoid competing with the standalone conjectural witness in
    `HyperbolicVolumeIndependence`. -/
noncomputable def hyperbolicVolumeIndependence_of_reduction
    (E : TransportErrorData)
    [JetOrderIndependence] [SurrealParallelTransportBound E]
    [R : JetTransportImpliesIndependence E] :
    HyperbolicVolumeIndependence :=
  R.nonempty_independence.some

/-! ### GB-elimination certificate (discharging `JetOrderIndependence`)

The weak conjecture asks that the order-`N` cyclotomic-coefficient
Jacobian of the three coloured-Jones series has full rank `3`.  Per
order this is a finite, decidable Gröbner–Shirshov *elimination* test:
row-reduce the `3 × (N+1)` coefficient matrix to echelon form and check
the three pivots are non-zero — equivalently, that a `3 × 3` minor of
the eliminated form has non-zero determinant.

The order-3 minor below is the GB-eliminated (row-echelon) form of the
order-`≤2` jet-coefficient data at the Reid-1991 base order, recorded by
its three pivots.  These are **witnessed from the framework's own
canonical Markov traces** (`jet_order_pivots.py`): the h-jet expansion
about `q = 1` of `tr_M(K)` for the canonical braid words of `4₁`, `5₂`,
`𝓑₃` gives the jet-Jacobian rows `(1/4, −1, 55/16)`, `(1/2, 0, −1/16)`,
`(1, 0, 0)`, with elimination determinant `1/16 ≠ 0` and LU pivots
`(1/4, 2, 1/8)`.  The certificate `jetOrder3_certificate`
(`elimination determinant = ∏ pivots ≠ 0`) is the genuine, sorry-free
content: `(1/4)·2·(1/8) = 1/16 ≠ 0`, so the order-3 Jacobian has full
rank `3` and the three series are jet-order independent at the base
order. -/

/-- The elimination determinant at one order = product of the three
    GB-eliminated pivots of the order-`N` minor of `(4₁, 5₂, 𝓑₃)`. -/
def eliminationDet (p : ℚ × ℚ × ℚ) : ℚ := p.1 * p.2.1 * p.2.2

/-- **GB-elimination certificate — general order (PROVED, sorry-free).**
    At any order, three non-zero eliminated pivots give a non-singular
    echelon minor (non-zero determinant), hence full rank `3` and
    jet-order independence at that order.  This is the order-uniform form
    of the certificate: every order is the same finite determinant test,
    parametric in the pivots the GB elimination produces. -/
theorem eliminationDet_ne_zero {p : ℚ × ℚ × ℚ}
    (h1 : p.1 ≠ 0) (h2 : p.2.1 ≠ 0) (h3 : p.2.2 ≠ 0) :
    eliminationDet p ≠ 0 :=
  mul_ne_zero (mul_ne_zero h1 h2) h3

/-- `jacobianRank` defined *from* the certificate: full rank `3` exactly
    when the order-`N` pivot product is non-zero, else deficient.  This
    makes `JetOrderIndependence.full_rank` a derived consequence of the
    GB certificate rather than a bare assertion. -/
def jacobianRankFromPivots (pivots : ℕ → ℚ × ℚ × ℚ) (N : ℕ) : ℕ :=
  if eliminationDet (pivots N) ≠ 0 then 3 else 0

/-- **`JetOrderIndependence` from a per-order GB certificate.**  Given that
    the eliminated pivots are non-zero at every order `≥ 3`, the
    `full_rank` field is *proved* (not asserted) via the general
    certificate `eliminationDet_ne_zero`.  Plug in the compute witness's
    pivots to discharge the conjecture at every certified order. -/
noncomputable def JetOrderIndependence.ofPivots (pivots : ℕ → ℚ × ℚ × ℚ)
    (h : ∀ N, 3 ≤ N →
      (pivots N).1 ≠ 0 ∧ (pivots N).2.1 ≠ 0 ∧ (pivots N).2.2 ≠ 0) :
    JetOrderIndependence where
  jacobianRank := jacobianRankFromPivots pivots
  full_rank N hN := by
    obtain ⟨h1, h2, h3⟩ := h N hN
    unfold jacobianRankFromPivots
    rw [if_pos (eliminationDet_ne_zero h1 h2 h3)]

/-- GB-eliminated jet-order pivots, **witnessed from the framework's own
    canonical Markov traces** (not representative).  The h-jet expansion
    about `q = 1` of `tr_M(K)` for `K ∈ {4₁, 5₂, 𝓑₃}` (canonical braid
    words `(σ₁σ₂⁻¹)²`, `σ₁⁻¹σ₂σ₁⁻¹σ₂²`, `(σ₁σ₂⁻¹)³`) gives the order-2
    coefficient vectors `(1/4, −1, 55/16)`, `(1/2, 0, −1/16)`, `(1, 0, 0)`;
    their `3×3` jet-Jacobian has elimination determinant `1/16 ≠ 0`, with
    LU pivots `(1/4, 2, 1/8)`.  Source:
    `computations/jet_order_pivots.py` →
    `jet-order-pivots.witness.json`.  The constant extension certifies
    full rank `3` at every order via `ofPivots`; higher-order pivots come
    from the same compute at higher jet truncation.

    -- Ref: [leitner2026] conj:three-knot-jet-order-independence -/
def jetPivots : ℕ → ℚ × ℚ × ℚ := fun _ => (1/4, 2, 1/8)

/-- **GB-elimination certificate at the Reid-1991 base order (PROVED,
    witnessed).**  `∏ pivots = (1/4)·2·(1/8) = 1/16 ≠ 0` — the actual
    elimination determinant of the canonical trace jet-Jacobian — so
    the order-3 Jacobian has full rank `3` and the three series are
    jet-order independent at the base order. -/
theorem jetOrder3_certificate : eliminationDet (jetPivots 3) ≠ 0 := by
  norm_num [eliminationDet, jetPivots]

/-! ### Rank-monotonicity: full rank at every order *from the base order*

`JetOrderIndependence.full_rank` is **not** an independent claim at each
order — mathematically it propagates from the single base-order
certificate.  The order-`N` coefficient Jacobian is `3 × (N+1)`; its first
three columns are the witnessed base-order minor `jetJacobianBase`, whose
determinant is `1/16 ≠ 0`.  An invertible `3×3` block forces rank `≥ 3`
(`Matrix.rank_submatrix_le`), while the row count `3` forces rank `≤ 3`
(`Matrix.rank_le_height`), so the order-`N` Jacobian has rank exactly `3`
for every `N`, rank being monotone in the column count.

This file formalizes the **two endpoints** of that argument, not the
order-`N` Jacobian itself: (1) the base minor is full-rank
(`jetJacobianBase_rank`, via invertibility), and (2) the abstract
monotonicity principle (`jacobianRank_eq_three_of_base`).  Discharging the
principle's hypotheses (`Monotone`, `≤ 3`, base `= 3`) for the *concrete*
order-`N` Jacobian — the column-extension/submatrix linkage stated above —
is the remaining structural input, not a lemma proved in this file. -/

/-- Witnessed base-order jet-Jacobian: rows are the order-`≤2` coefficient
    vectors of `tr_M(K)` about `q = 1` for `K ∈ {4₁, 5₂, 𝓑₃}`.  Source:
    `computations/jet_order_pivots.py`. -/
def jetJacobianBase : Matrix (Fin 3) (Fin 3) ℚ :=
  !![1/4, -1, 55/16; 1/2, 0, -1/16; 1, 0, 0]

/-- The witnessed elimination determinant `det = 1/16 ≠ 0` (matches
    `jetOrder3_certificate`'s `∏ pivots = 1/16`). -/
theorem jetJacobianBase_det : jetJacobianBase.det = 1 / 16 := by
  have _ : jetJacobianBase 0 0 = 1 / 4 := rfl
  have _ : jetJacobianBase 0 1 = -1 := rfl
  rw [Matrix.det_fin_three]
  simp [jetJacobianBase]
  norm_num

/-- The base minor is invertible (`det = 1/16 ≠ 0`). -/
theorem jetJacobianBase_isUnit : IsUnit jetJacobianBase := by
  rw [Matrix.isUnit_iff_isUnit_det, jetJacobianBase_det]
  exact isUnit_iff_ne_zero.mpr (by norm_num)

/-- **Base-order full rank (PROVED, witnessed).**  The base minor is
    invertible, hence has rank `3`. -/
theorem jetJacobianBase_rank : jetJacobianBase.rank = 3 := by
  have hu : IsUnit jetJacobianBase := jetJacobianBase_isUnit
  have hr := Matrix.rank_of_isUnit jetJacobianBase hu
  have hc : Fintype.card (Fin 3) = 3 := rfl
  exact hr.trans hc

/-- **Rank-monotonicity principle.**  A rank function that is monotone
    (rank cannot drop when columns are added), bounded by the row count
    `3`, and equal to `3` at the base order is `3` at every order `≥ 3`.
    This is the structural reason `full_rank` propagates from the base
    order without per-order computation. -/
theorem jacobianRank_eq_three_of_base {r : ℕ → ℕ} (hmono : Monotone r)
    (hle : ∀ N, r N ≤ 3) (hbase : r 3 = 3) {N : ℕ} (hN : 3 ≤ N) : r N = 3 :=
  le_antisymm (hle N) (hbase ▸ hmono hN)

/-! ### Why this file declares **no** global instances (2026-08-09)

Both conjectures above were previously discharged by global instances that
carried no mathematical content.  Per AGENTS.md §3b-tax — *"An unproved primary
is honestly represented by a content-bearing class with no instance; do not
fabricate a trivial instance to close it"* — they are removed.  This is the
same failure mode this file's own history note records for
`HyperbolicVolumeIndependence` on 2026-06-10, recurring one class down.

**(1) `SurrealParallelTransportBound` — the instance was vacuous.**  It read

```
  transportShadow := fun _ => 0 ; physicalShadow := fun _ => 0
  monodromyShadow := fun _ => 0 ; …_archimedean_zero := fun _ => rfl
```

Because `transportShadow` is a class *field*, the instance gets to **choose**
the shadow, and the constant-zero choice satisfies (I2) and (I3) by `rfl`.  So
`[SurrealParallelTransportBound]` was discharged for free, and with it every
downstream conditional — including `hyperbolicVolumeIndependence_of_reduction`,
whose whole point is to expose the conditional structure at each call site.
The two "PROVED" lemmas `transport_shadow_vanishes` and
`transport_uniform_bound` remain valid: they are honest statements *about a
given* `SurrealParallelTransportBound`, and are unaffected by the removal.

**Redesigned the same day (bean `qou-ijhk`).**  Removing the instance stops the
free discharge but does not by itself make the class content-bearing — any
future instance could re-pick the zero functions.  So the shadows were moved
out of the class into `TransportErrorData` and the class now takes that data as
a **parameter**: `SurrealParallelTransportBound (E : TransportErrorData)`.  A
consumer must now name the error it assumes about, and that name propagates
through `JetTransportImpliesIndependence E` and
`hyperbolicVolumeIndependence_of_reduction E` to every call site.

The residual vacuity that parameterisation *cannot* remove — one may still
instantiate at the zero error — is no longer left as a latent trap.  It is
recorded as the pair `trivialError_bound` (the bound holds at the zero error,
so an instance for an unspecified `E` asserts nothing) and
`not_bound_of_physical_ne_zero` (for an `E` with a non-zero physical shadow the
bound is a real constraint that fails).  Together they state exactly what an
instance is worth.  Supplying the `E` that actually comes from the categorical
connection still requires a Lean definition of the transport error, which
remains open.

**(2) `JetOrderIndependence` — the instance fabricated its data.**  It applied
`ofPivots` to `jetPivots = fun _ => (1/4, 2, 1/8)`, a **constant** extension of
the order-3 pivots to every order, thereby asserting `full_rank` at all
`N ≥ 3` — which *is* the open conjecture.  The genuine content is kept and is
unchanged: `jetPivots` (the witnessed base-order pivots), `jetOrder3_certificate`
(`∏ pivots = 1/16 ≠ 0`, sorry-free), `jetJacobianBase_rank = 3`,
`eliminationDet_ne_zero`, `ofPivots` and `jacobianRank_eq_three_of_base`.  What
is dropped is only the step from "certified at the base order" to "holds at
every order".  To discharge the conjecture honestly, feed `ofPivots` the
per-order pivots actually produced by `computations/jet_order_pivots.py` at
higher jet truncation, or discharge `jacobianRank_eq_three_of_base`'s
hypotheses for the concrete order-`N` Jacobian (the column-extension linkage
this file already flags as "the remaining structural input").

Consumers that want the conditional form bind the classes explicitly per
§3b-cond, which is exactly the visibility the reduction was written to provide.
-/

end QOU.Archimedean
