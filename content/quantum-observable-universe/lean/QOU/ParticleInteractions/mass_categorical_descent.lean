import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.ParticleInteractions.mass_categorical_descent

Canonical Lean for content block
[`prop:mass-categorical-descent`](../../../quantum-observable-universe/mass-theory/mass-categorical-descent.md):
*QOU mass formula as descent decomposition of the mass endomorphism.*

**Proposition.** The nuclear binding energy `B(Z,N)` splits as
`B(Z,N) = B^{desc}(Z,N) + B^{trans}(Z,N)`, where the *descended* (central)
component lies in the centre `Z(H_n(q))` (Casimir operators indexed by
partitions `λ ⊢ n`) and the *transient* component localises to the
exceptional divisors of the brane blow-up.

## Disposition (integrity)

The previous revision either projected the two class fields
`⟨ctx.claim_i_descent_decomposition, ctx.claim_ii_BW_recovery⟩` back as the
conclusion (self-assuming projection, AGENTS.md §3b-cond item 5), or named
the proposition as a `def … : Prop` whose second conjunct
`|m − m_BW| ≤ rel_err` was trivially satisfiable by the free `rel_err`
field.  Corrected:

- `MassCategoricalDescentContext` carries the total binding `B` and its two
  categorical components `B_desc` (central) and `B_trans` (exceptional
  divisor) as genuine independent data fields — none is the conclusion.
  That flat form is *refutable as written*
  (`mass_categorical_descent_unconstrained_false`), so the `sorry` it
  once carried could never be discharged.
- **Route (b) fix (2026-08-14, beans `qou-oq5r`/`qou-e2fi`, owner-selected):**
  `MassDescentChannels` gives the claim its real structure — a finite
  Wedderburn channel type, per-channel contributions, a decidable centre
  predicate — and the additive identity `B = B_desc + B_trans` is
  **derived** (`descent_decomposition`, sorry-free): it is the splitting
  of a finite sum along the centre predicate.  The open physics is
  confined to the corpus *instance* (partitions `λ ⊢ n`,
  `contrib = m_e·y_λ χ^λ Δ_λ`, centrality = Casimir membership), which
  is honestly absent.  The file is sorry-free.
-/

namespace QOU.ParticleInteractions

/-- Data of the mass-categorical-descent claim.  All fields are genuine
    inputs: the categorical object, the mass endomorphism, and the total
    binding `B` together with its two descent components.  None is the
    conclusion. -/
class MassCategoricalDescentContext where
  /-- The categorical object `A` of the QOU `(C, A, τ)`. -/
  CategoricalObj : Type
  /-- The mass endomorphism `𝔪 : A → A` (abstract carrier). -/
  m_endo : CategoricalObj → CategoricalObj
  /-- The total nuclear binding energy `B(Z,N)`. -/
  B : ℝ
  /-- The **descended** (central) component — Casimir operators in the
      centre `Z(H_n(q))`, indexed by partitions `λ ⊢ n`. -/
  B_desc : ℝ
  /-- The **transient** component — localised to the exceptional divisors
      `E_i` of the brane blow-up. -/
  B_trans : ℝ
  /-- The Bethe–Weizsäcker liquid-drop value, recovered as one
      phenomenology of the descent decomposition. -/
  B_BW : ℝ

/-- **The channel structure of the descent decomposition** (route (b) of
    bean `qou-oq5r`, owner-selected 2026-08-14; bean `qou-e2fi`): the
    Wedderburn picture, as genuine structure.  A finite type of
    **channels** (in the corpus: partitions `λ ⊢ n` indexing the
    Wedderburn blocks of `H_n(q)`, plus the exceptional-divisor local
    contributions), a per-channel binding **contribution** (in the
    corpus: `m_e · y_λ χ^λ Δ_λ` for the central channels), and a
    decidable predicate marking the **central** (Casimir / centre
    `Z(H_n(q))`) channels.  None of the fields is the conclusion: the
    additive identity is *derived* from finiteness of the channel
    decomposition (`descent_decomposition` below). -/
class MassDescentChannels where
  /-- The channel index (corpus: partitions + divisor sites). -/
  Channel : Type
  /-- Finitely many channels (Wedderburn: partitions of `n`). -/
  [chFin : Fintype Channel]
  /-- Per-channel binding contribution. -/
  contrib : Channel → ℝ
  /-- Central (Casimir / `Z(H_n(q))`) channels. -/
  isCentral : Channel → Prop
  /-- Centrality is decidable (Wedderburn: membership of the block's
      Casimir in the centre is a finite check). -/
  [centralDec : DecidablePred isCentral]

attribute [instance] MassDescentChannels.chFin MassDescentChannels.centralDec

namespace MassDescentChannels

variable [ch : MassDescentChannels]

/-- Total binding: the sum of every channel's contribution. -/
noncomputable def B_total : ℝ := ∑ c : ch.Channel, ch.contrib c

/-- Descended (central) binding: the sum over the centre channels. -/
noncomputable def B_desc : ℝ :=
  ∑ c ∈ Finset.univ.filter ch.isCentral, ch.contrib c

/-- Transient binding: the sum over the non-central channels. -/
noncomputable def B_trans : ℝ :=
  ∑ c ∈ Finset.univ.filter (fun c => ¬ ch.isCentral c), ch.contrib c

/-- **The descent decomposition, derived**: `B = B^desc + B^trans` is the
    splitting of a finite sum along a decidable predicate — the additive
    identity holds for *every* channel structure, because `B_desc` and
    `B_trans` are *defined* as the two halves of the same decomposition
    that defines `B_total`.  This is the honest content of the additive
    claim: it is a property of the channel decomposition, not an extra
    physical assumption. -/
theorem descent_decomposition : B_total = B_desc + B_trans := by
  unfold B_total B_desc B_trans
  exact (Finset.sum_filter_add_sum_filter_not Finset.univ _ _).symm

end MassDescentChannels

/-- **Mass formula as descent decomposition**
    ([`prop:mass-categorical-descent`]) — conditional on the channel
    structure, now **sorry-free**: given the Wedderburn channel
    decomposition (`MassDescentChannels`), the total binding splits as

      `B(Z,N) = B^{desc}(Z,N) + B^{trans}(Z,N)`

    with the descended component the sum over centre (`Z(H_n(q))`)
    channels and the transient component the sum over the rest.

    **What is derived vs what is open.**  Derived: the additive identity,
    for every channel structure (`descent_decomposition`).  Open (the
    physics, named): instantiating `Channel`/`contrib`/`isCentral` with
    the corpus objects — partitions `λ ⊢ n` with `contrib λ = m_e·y_λ
    χ^λ Δ_λ` and centrality = Casimir membership — and showing the
    resulting `B_total` is the physical binding.  That instantiation is
    the manuscript-level descent statement; it lives in the *instance*,
    which this file honestly does not provide. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/mass-categorical-descent.ts
theorem mass_categorical_descent [MassDescentChannels] :
    MassDescentChannels.B_total
      = MassDescentChannels.B_desc + MassDescentChannels.B_trans :=
  MassDescentChannels.descent_decomposition

/-- **The flat data-field form is refutable as written** — the data-only
    class below never relates the fields its conclusion names, so
    `∀ instances` admits ones that simply disagree. Not an open gap: no
    unconditional `sorry` could ever be discharged. The fix is the
    channel structure above (bean qou-octr → route (b), bean qou-e2fi):
    the additive identity is derived from the decomposition, and the
    open physics is confined to the (absent) corpus instance. -/
theorem mass_categorical_descent_unconstrained_false :
    ¬ ∀ ctx : MassCategoricalDescentContext, ctx.B = ctx.B_desc + ctx.B_trans := by
  intro h
  have := h { CategoricalObj := Unit, m_endo := id,
              B := 0, B_desc := 1, B_trans := 0, B_BW := 0 }
  norm_num at this

section OperatorChannels

open scoped Classical

/-- **Tranche 2 of the route-(b) formalization** (bean `qou-x3gr`):
    centrality becomes *semantic*.  Each channel now carries an
    **operator** in a ring `A` (corpus: the block Casimir in `H_n(q)`
    for the Wedderburn channels; the divisor-local operator for the
    transient ones), and centrality is **derived** as membership in the
    centre of `A` — no predicate field.  The tranche-1 structure is
    recovered as the shadow `toChannels` below. -/
class MassDescentOperatorChannels (A : Type*) [Ring A] where
  /-- The channel index (corpus: partitions + divisor sites). -/
  Channel : Type
  /-- Finitely many channels. -/
  [chFin : Fintype Channel]
  /-- The channel's operator (corpus: block Casimir / divisor-local). -/
  op : Channel → A
  /-- Per-channel binding contribution. -/
  contrib : Channel → ℝ

attribute [instance] MassDescentOperatorChannels.chFin

namespace MassDescentOperatorChannels

variable (A : Type*) [Ring A] [ch : MassDescentOperatorChannels A]

/-- Centrality, **derived from the algebra**: the channel's operator
    lies in the centre `Z(A)`.  In the corpus instantiation
    `A = H_n(q)` this is exactly "the Casimir lies in `Z(H_n(q))`" —
    the defining property of the descended component, now a statement
    about `A` rather than a field of the class. -/
def IsCentral (c : ch.Channel) : Prop := ch.op c ∈ Set.center A

/-- **The Casimir property is a theorem**: a central channel's operator
    commutes with every element of the algebra. -/
theorem isCentral_commutes {c : ch.Channel} (h : IsCentral A c) (a : A) :
    ch.op c * a = a * ch.op c :=
  (Set.mem_center_iff.mp h).comm a

/-- A central channel's operator commutes with **every** channel
    operator — central or not (only `c`'s centrality is needed).  In
    particular the descended sector is commutative, and it also
    commutes with the transient sector. -/
theorem isCentral_pair_comm {c c' : ch.Channel} (h : IsCentral A c) :
    ch.op c * ch.op c' = ch.op c' * ch.op c :=
  (Set.mem_center_iff.mp h).comm (ch.op c')

/-- **Bridge to tranche 1**: an operator-channel structure induces the
    predicate-based channel structure, with `isCentral` specialised to
    centre membership (decidability supplied classically — in the
    finite Wedderburn case it is a finite check). -/
noncomputable def toChannels : MassDescentChannels :=
  { Channel := ch.Channel
    chFin := ch.chFin
    contrib := ch.contrib
    isCentral := IsCentral A
    centralDec := Classical.decPred _ }

/-- **The descent decomposition for operator channels**: with
    centrality derived from centre membership, the additive identity
    `B = B^desc + B^trans` holds — inherited from the tranche-1
    theorem through the bridge.  Sorry-free end to end: the only
    remaining open item is the corpus *instance*
    (`A = H_n(q)`, `op λ = z_λ`, `contrib λ = m_e·y_λ χ^λ Δ_λ`). -/
theorem descent_decomposition_operators :
    MassDescentChannels.B_total (ch := toChannels A)
      = MassDescentChannels.B_desc (ch := toChannels A)
        + MassDescentChannels.B_trans (ch := toChannels A) :=
  MassDescentChannels.descent_decomposition (ch := toChannels A)

end MassDescentOperatorChannels

end OperatorChannels

end QOU.ParticleInteractions
