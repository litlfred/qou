import Mathlib.Tactic
import QOU.MathlibExt.DisjointBlockTraceLaw

/-!
# The single-crossing chain factorises into a bond product

Bean `qou-301d`. Probe evidence: `computations/onedim/production_word_cross_term_probe.py`.

## What this file adds

`QOU.MathlibExt.DisjointBlockTrace` proves the **disjoint-block law**

    DisjointBlockMultiplicative T :  ∀ n, ∀ a ∈ H n, ∀ b ∈ shifted n,  tr (a * b) = tr a * tr b

from one structural hypothesis about the algebra (`TowerSpan`), and its own
docstring says in terms: *"Nothing here derives the bond product."* That is the
gap this file closes.

The production atom word is not a bare product of blocks. It is a **chain**

    B₀ · s₀ · B₁ · s₁ · ⋯ · B_{A-1}

in which consecutive nucleon blocks are separated by a single **interface
letter** `sₖ = g mₖ + dₖ • 1` — one crossing plus a scalar. Measured on the
corpus's own producer (`mass_at_3A_proper.atom_braid_word_3A`, 35 letters at
`A = 3`): nucleon blocks sit on generator pairs `(0,1)`, `(3,4)`, `(6,7)` and the
two interfaces are the single generators **2** and **5**. So block `k` lives at
levels `3k, 3k+1` and interface `k` is the generator `3k+2` between block `k` and
block `k+1`.

`tr_chainWord` below states and proves that such a chain's trace is

    tr (chain) = (∏ₖ tr Bₖ) · (∏ₖ (z + dₖ))

— the **bond product**, with one factor `z + dₖ` per interface and no cross term.

## 🛑 The join is NOT a new hypothesis, and that is this file's main result

The step the disjoint-block law does not obviously supply is the one where the
interface crossing has block material on **both** sides:

    SingleCrossingJoin T :  ∀ m, ∀ a ∈ H m, ∀ b ∈ shifted (m+1),
                              tr (a * g m * b) = z * tr a * tr b

This was expected to need a new axiom — the connected-sum step — because the
obvious route dies: (T3) `tr (a * g m) = z * tr a` absorbs a generator only at
the **right end** of a word, and cyclicity applied to `a * g m * b` only produces
`tr (a * b * g m)`, whose left factor `a * b` is **not** in `H m` (`b` lives
strictly above `m`). That route is genuinely dead.

**It is nonetheless a two-line theorem** (`singleCrossingJoin_of_disjointBlock`),
and the move is to stop trying to move `b` and instead **group `a * g m` into one
element and apply the disjoint-block law one level higher**:

    a ∈ H m  and  g m ∈ H (m+1)   ⟹   a * g m ∈ H (m+1)     (H (m+1) is a Subalgebra)
    b ∈ shifted (m+1)                                        (hypothesis)
    ⟹ tr ((a * g m) * b) = tr (a * g m) * tr b               (L1 AT LEVEL m+1)
                          = z * tr a * tr b                  (T3 at level m)

The hidden assumption in the dead route was that the law had to be applied at
level `m`, the level the interface sits at. `DisjointBlockMultiplicative` is
universally quantified over the level, and level `m+1` is the one that fits: it
is exactly the level at which `a * g m` is a single admissible left factor.

**This is the second time this exact error has been made on this object**, which
is why it is recorded rather than quietly fixed. `DisjointBlockTraceLaw`'s own
`🛑 CORRECTED 2026-09-07` block records that `TwoSidedMarkov` was introduced as
*"the one input `MarkovTrace` does not carry"* and turned out to be a four-line
theorem of (T1) + (T3). The present case is the same shape one level up: a
property that looks like it needs a new axiom because the *first* instantiation
tried does not work.

## What is therefore conditional on what

Everything below is conditional on `DisjointBlockMultiplicative` and **nothing
else** — no new hypothesis is introduced anywhere in this file. Composing with
`DisjointBlockTrace.disjointBlock_of_towerSpan`, the whole bond product reduces
to **`TowerSpan` plus the quadratic relation**, i.e. to the single algebraic gap
the corpus had already isolated. `chainFactorizes_of_towerSpan` records that
composition so the reduction is machine-checked rather than asserted.

`TowerSpan` itself is not proved here or anywhere in the corpus, and it is not
provable from `MarkovTrace`: the structure carries no hypothesis constraining how
`H (m+1)` is generated, so `H` may be any monotone family of subalgebras
containing the generators. Per AGENTS.md §"Axiomatization is NOT a Proof", the
bond product is therefore **still not unconditionally derived** — but the
condition is now one classical, citable structure theorem rather than two
independent unknowns.

## Measured evidence (not re-measured here)

In `H₆` at the proton pin, 60 dps: `tr(B₀·B₁) = tr(B₀)·tr(B₁)` with relative
deviation **exactly 0.0**; and `tr(B₀·s·B₁) = tr(B₀)·(z+d)·tr(B₁)` at
`d = 0, −h/2, −h` with relative deviation ~5e-61, the arithmetic floor. On the
production `A = 3` word in `H₉`, `tr_M(W_atom) = tr_free · ∏(z+d)` with
`Δ = −2.67e-62` (rel 9.17e-61) against a threshold of 0.0417 for a cross term to
matter. So the identity proved here is measured true; what was missing was the
proof.

## The downstream reading, stated narrowly

`three_body_cumulant_vanishes` is the division-free form of *"the chain carries
no genuine three-body term"*: with `W` the full three-block chain,

    tr W · tr B₀ · tr B₁ · tr B₂ = tr (B₀ s₀ B₁) · tr (B₁ s₁ B₂) · tr (B₀ B₂)

which is the standard cumulant condition `W₁₂₃ W₁ W₂ W₃ = W₁₂ W₁₃ W₂₃`, i.e. the
vanishing of the connected three-body cumulant of `log tr`. It is stated
multiplicatively because `R` is a bare `CommRing` and has no logarithm.

🛑 **This is NOT the statement that `b₃ = 0` in the sense of
`QOU.MassTheory.UrsellPartitionFunctionB3`, and the two must not be conflated.**
That file's `b3corpus` is the Boolean cumulant of the *multiplicative assembly*
`W(S) = 1 − Z_S`, and `b3corpus_eq_neg_phi3` proves it equals `−φᵀ₃`, which for a
chain is `−g₀₁·g₁₂ ≠ 0`. The present theorem is about `Z_S = tr W_atom / tr
W_free` **itself** being exactly bond-multiplicative — AGENTS.md's *"the log
assembly is exactly pairwise (`b₃ = 0`)"* — which is the input that file's
docstring assumes when it writes `Z_S = ∏_{e ⊆ S} f_e`. Exact bond
multiplicativity of `Z` and non-vanishing of `φᵀ₃` are consistent: `φᵀ₃` is
defined by the cluster property `Z_S = Σ_π ∏_B φᵀ_B`, not by a cumulant of `log`.

**One correction of an upstream citation, made here rather than in that file.**
`UrsellPartitionFunctionB3`'s docstring justifies `Z_S = ∏_e f_e` by
*"connected-sum multiplicativity of the Markov trace
(`QOU.MathlibExt.MonotoneWordFactorizes.tr_stabWord_eq_prod_tr`)"*. That name
resolves — checked, not assumed — but note it is a *declaration* name whose
namespace omits a word its **file** name carries: the source is
`QOU/MathlibExt/MonotoneWordTraceFactorizes.lean`, whose `namespace` is
`QOU.MathlibExt.MonotoneWordFactorizes`. Both spellings appear in the corpus and
each is correct for a different thing; do not "fix" either. That theorem
is about **ascending** words, and per `DisjointBlockTraceLaw`'s docstring the
production word is **not** ascending under owner ruling `qou-hu1f` — one
nucleon's generator sequence is `[0,1,0,1,0,1,0,0,1,0,0]`, in which the maximal
level occurs four times. So the cited theorem does not cover the word it is cited
for. `tr_chainWord` below does cover it, conditionally on
`DisjointBlockMultiplicative`. That file is not edited here.

-- Ref: [manuscript] bean qou-301d; Kassel–Turaev, *Braid Groups*, ch. 4 (Markov
-- trace and the Ocneanu conditional expectation); Jones 1987 for the
-- connected-sum multiplicativity this is the algebraic shadow of.
-/

namespace QOU.MathlibExt.SingleCrossingChain

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-! ## 1. The connected-sum join -/

/-- **The single-crossing join**: cutting a word along one interface crossing
with block material on both sides multiplies the two traces and the Markov
parameter.

`a` is the material at or below level `m`, `g m` is the interface crossing, and
`b` is the material strictly above. At `b = 1` this is exactly (T3), so the
property is a genuine generalisation of the stabilisation axiom rather than a
weakening of it (`markov_of_singleCrossingJoin`).

Stated as a `def … : Prop` rather than a `class` deliberately: it is **proved**
below, so a `[SingleCrossingJoin T]` binder would misrepresent a theorem as an
assumption. -/
def SingleCrossingJoin : Prop :=
  ∀ m : ℕ, ∀ a ∈ T.H m, ∀ b ∈ shifted T (m + 1),
    T.tr (a * T.g m * b) = T.z * T.tr a * T.tr b

/-- **The main result: the join is a theorem of the disjoint-block law.**

Two lines, and no hypothesis beyond `DisjointBlockMultiplicative`. The whole
content is the choice of *level*: the disjoint-block law is applied at `m + 1`,
not at `m`, with `a * g m` as a single left factor. See the module docstring for
why the level-`m` route is genuinely dead and why this was expected to need a new
axiom. -/
theorem singleCrossingJoin_of_disjointBlock (hdb : DisjointBlockMultiplicative T) :
    SingleCrossingJoin T := by
  intro m a ha b hb
  have hag : a * T.g m ∈ T.H (m + 1) :=
    (T.H (m + 1)).mul_mem (T.H_mono (Nat.le_succ m) ha) (T.g_mem m)
  rw [hdb (m + 1) _ hag b hb, T.markov m a ha]

/-- **Anti-vacuity: the property has at least (T3)'s content.** Its `b = 1` case
is the stabilisation axiom, so `SingleCrossingJoin` is not a predicate whose body
ignores its arguments — it constrains `tr`, `g` and `z` jointly. -/
theorem markov_of_singleCrossingJoin (h : SingleCrossingJoin T)
    (n : ℕ) (a : A) (ha : a ∈ T.H n) :
    T.tr (a * T.g n) = T.z * T.tr a := by
  have := h n a ha 1 (shifted T (n + 1)).one_mem
  simpa [T.tr_one] using this

/-! ## 2. The affine interface letter

An interface is not a bare crossing: it is `g m + d • 1`, one crossing plus a
scalar. Expanding, the crossing term is the join above and the scalar term is the
disjoint-block law one level up; the two combine into a single factor `z + d`. -/

/-- **The affine-letter lemma.** One interface letter contributes exactly
`z + d`.

Stated with the join and the disjoint-block law as *separate* hypotheses so the
anatomy is visible: the `g m` term needs the first, the `d • 1` term needs the
second. `tr_affine_letter` immediately below drops the first, since it follows
from the second. -/
theorem tr_affine_letter_of_join (hsc : SingleCrossingJoin T)
    (hdb : DisjointBlockMultiplicative T) (m : ℕ)
    (a : A) (ha : a ∈ T.H m) (b : A) (hb : b ∈ shifted T (m + 1)) (d : R) :
    T.tr (a * (T.g m + d • (1 : A)) * b) = (T.z + d) * T.tr a * T.tr b := by
  have hexp : a * (T.g m + d • (1 : A)) * b = a * T.g m * b + d • (a * b) := by
    rw [mul_add, add_mul, mul_smul_comm, mul_one, smul_mul_assoc]
  have hplain : T.tr (a * b) = T.tr a * T.tr b :=
    hdb (m + 1) a (T.H_mono (Nat.le_succ m) ha) b hb
  rw [hexp, map_add, map_smul, hsc m a ha b hb, hplain]
  simp only [smul_eq_mul]
  ring

/-- **The affine-letter lemma on the disjoint-block law alone.** -/
theorem tr_affine_letter (hdb : DisjointBlockMultiplicative T) (m : ℕ)
    (a : A) (ha : a ∈ T.H m) (b : A) (hb : b ∈ shifted T (m + 1)) (d : R) :
    T.tr (a * (T.g m + d • (1 : A)) * b) = (T.z + d) * T.tr a * T.tr b :=
  tr_affine_letter_of_join T (singleCrossingJoin_of_disjointBlock T hdb) hdb m a ha b hb d

/-! ## 3. The chain

A chain is a list of links, each carrying a block, the level of the interface
crossing that **follows** it, and that interface's affine coefficient, together
with a final block. So a list of `N` links describes `N + 1` blocks and `N`
interfaces: `B₀ s₀ B₁ s₁ ⋯ s_{N-1} B_N`. Interface `k` sits between block `k` and
block `k + 1`, matching the measured layout (`A = 3`: links at levels 2 and 5,
blocks on `(0,1)`, `(3,4)`, `(6,7)`). -/

/-- The word a chain spells out. -/
def chainWord (T : MarkovTrace R A) : List (A × ℕ × R) → A → A
  | [], last => last
  | (b, m, d) :: rest, last => b * (T.g m + d • (1 : A)) * chainWord T rest last

@[simp] theorem chainWord_nil (last : A) : chainWord T [] last = last := rfl

@[simp] theorem chainWord_cons (b : A) (m : ℕ) (d : R)
    (rest : List (A × ℕ × R)) (last : A) :
    chainWord T ((b, m, d) :: rest) last
      = b * (T.g m + d • (1 : A)) * chainWord T rest last := rfl

/-- **The layering condition.** Each block sits at or below its own right
interface, and everything to its right sits strictly above that interface. These
are exactly the two memberships the affine-letter lemma consumes, and nothing
more is assumed. -/
inductive Layered (T : MarkovTrace R A) (last : A) : List (A × ℕ × R) → Prop
  | nil : Layered T last []
  | cons {b : A} {m : ℕ} {d : R} {rest : List (A × ℕ × R)}
      (hblock : b ∈ T.H m)
      (htail : chainWord T rest last ∈ shifted T (m + 1))
      (hrest : Layered T last rest) : Layered T last ((b, m, d) :: rest)

/-- **The chain factorisation.** A layered chain's trace is the product of its
block traces times the product of its bond factors — one `z + dₖ` per interface,
and no cross term.

Conditional on `DisjointBlockMultiplicative` and nothing else. -/
theorem tr_chainWord (hdb : DisjointBlockMultiplicative T) (last : A)
    (L : List (A × ℕ × R)) (hL : Layered T last L) :
    T.tr (chainWord T L last)
      = (L.map (fun p => T.tr p.1)).prod * (L.map (fun p => T.z + p.2.2)).prod
          * T.tr last := by
  induction hL with
  | nil => simp
  | @cons b m d rest hblock htail hrest ih =>
      rw [chainWord_cons, tr_affine_letter T hdb m b hblock _ htail d, ih]
      simp only [List.map_cons, List.prod_cons]
      ring

/-! ### Discharging the layering condition from per-block data

`Layered`'s `htail` field is a statement about a whole tail, which is what the
induction needs but not what a caller has. The two lemmas here rebuild it from
per-block memberships and a level bound. -/

/-- `shifted` is antitone: a higher floor is a smaller subalgebra. -/
theorem shifted_antitone {n n' : ℕ} (h : n ≤ n') : shifted T n' ≤ shifted T n := by
  refine Algebra.adjoin_le ?_
  intro x hx
  simp only [Set.mem_iUnion, Set.mem_insert_iff, Set.mem_singleton_iff] at hx
  obtain ⟨k, hk⟩ := hx
  have hsplit : n' + k = n + (n' - n + k) := by omega
  rcases hk with rfl | rfl
  · rw [hsplit]; exact g_mem_shifted T n _
  · rw [hsplit]; exact ginv_mem_shifted T n _

/-- A chain word all of whose blocks and interface levels sit above `n` is itself
in `shifted n`. -/
theorem chainWord_mem_shifted (n : ℕ) (last : A) (hlast : last ∈ shifted T n) :
    ∀ L : List (A × ℕ × R),
      (∀ p ∈ L, p.1 ∈ shifted T n) → (∀ p ∈ L, n ≤ p.2.1) →
      chainWord T L last ∈ shifted T n := by
  intro L
  induction L with
  | nil => intro _ _; simpa using hlast
  | cons p rest ih =>
      intro hblocks hlevels
      obtain ⟨b, m, d⟩ := p
      have hb : b ∈ shifted T n := hblocks _ (List.mem_cons_self ..)
      have hm : n ≤ m := hlevels _ (List.mem_cons_self ..)
      have hg : T.g m ∈ shifted T n := by
        have := g_mem_shifted T n (m - n)
        rwa [show n + (m - n) = m by omega] at this
      have hone : d • (1 : A) ∈ shifted T n :=
        Subalgebra.smul_mem _ (Subalgebra.one_mem _) d
      have htail : chainWord T rest last ∈ shifted T n :=
        ih (fun q hq => hblocks q (List.mem_cons_of_mem _ hq))
           (fun q hq => hlevels q (List.mem_cons_of_mem _ hq))
      rw [chainWord_cons]
      exact Subalgebra.mul_mem _
        (Subalgebra.mul_mem _ hb (Subalgebra.add_mem _ hg hone)) htail

/-! ## 4. The reduction to `TowerSpan`, and the production layout -/

/-- **The whole bond product reduces to the single gap the corpus already had.**
Composing with `DisjointBlockTrace.disjointBlock_of_towerSpan`: `TowerSpan` plus
the quadratic relation give the chain factorisation. No second hypothesis is
introduced anywhere in this file.

`TowerSpan` remains unproved and has no Hecke instance — see its own docstring
and AGENTS.md §"Axiomatization is NOT a Proof". -/
theorem chainFactorizes_of_towerSpan [TowerSpan T]
    (hquad : ∀ m : ℕ, ∃ h : R, T.g m * T.g m = h • T.g m + 1)
    (last : A) (L : List (A × ℕ × R)) (hL : Layered T last L) :
    T.tr (chainWord T L last)
      = (L.map (fun p => T.tr p.1)).prod * (L.map (fun p => T.z + p.2.2)).prod
          * T.tr last :=
  tr_chainWord T (disjointBlock_of_towerSpan T hquad) last L hL

/-- The join, reduced the same way — this is the item the file was opened to
settle, and it lands on `TowerSpan` rather than on a new axiom. -/
theorem singleCrossingJoin_of_towerSpan [TowerSpan T]
    (hquad : ∀ m : ℕ, ∃ h : R, T.g m * T.g m = h • T.g m + 1) :
    SingleCrossingJoin T :=
  singleCrossingJoin_of_disjointBlock T (disjointBlock_of_towerSpan T hquad)

/-- **The production `A = 3` layout.** Blocks on generator pairs `(0,1)`,
`(3,4)`, `(6,7)`; interfaces the single generators `2` and `5`. The hypotheses
are exactly *"block `k` is generated at levels `≥ 3k` and lies at or below level
`3k+2`"*, which is what the producer's word satisfies by construction. -/
theorem tr_atomChain_three (hdb : DisjointBlockMultiplicative T)
    (B₀ B₁ B₂ : A) (d₀ d₁ : R)
    (hB₀ : B₀ ∈ T.H 2) (hB₁H : B₁ ∈ T.H 5)
    (hB₁s : B₁ ∈ shifted T 3) (hB₂s : B₂ ∈ shifted T 6) :
    T.tr (B₀ * (T.g 2 + d₀ • (1 : A)) * (B₁ * (T.g 5 + d₁ • (1 : A)) * B₂))
      = T.tr B₀ * T.tr B₁ * T.tr B₂ * ((T.z + d₀) * (T.z + d₁)) := by
  have hB₂s3 : B₂ ∈ shifted T 3 := shifted_antitone T (by norm_num) hB₂s
  have hg5 : T.g 5 ∈ shifted T 3 := by
    have := g_mem_shifted T 3 2
    norm_num at this
    exact this
  have hone : d₁ • (1 : A) ∈ shifted T 3 :=
    Subalgebra.smul_mem _ (Subalgebra.one_mem _) d₁
  have htail : B₁ * (T.g 5 + d₁ • (1 : A)) * B₂ ∈ shifted T 3 :=
    Subalgebra.mul_mem _
      (Subalgebra.mul_mem _ hB₁s (Subalgebra.add_mem _ hg5 hone)) hB₂s3
  have hinner : T.tr (B₁ * (T.g 5 + d₁ • (1 : A)) * B₂)
      = (T.z + d₁) * T.tr B₁ * T.tr B₂ :=
    tr_affine_letter T hdb 5 B₁ hB₁H B₂ hB₂s d₁
  rw [tr_affine_letter T hdb 2 B₀ hB₀ _ htail d₀, hinner]
  ring

/-- **The three-body connected cumulant of the chain vanishes**, in the
division-free form `W₁₂₃ · W₁ · W₂ · W₃ = W₁₂ · W₁₃ · W₂₃`.

The non-adjacent pair `B₀ B₂` carries no interface, so its trace is the bare
product — that is the disjoint-block law at level 3, and it is what makes the
identity an equality rather than a definition.

🛑 Read the module docstring before citing this: it is the vanishing of the
cumulant of `log tr`, **not** of `QOU.MassTheory.UrsellPartitionFunctionB3`'s
`b3corpus`, which is the cumulant of `1 − Z` and is `−φᵀ₃ ≠ 0` on a chain. -/
theorem three_body_cumulant_vanishes (hdb : DisjointBlockMultiplicative T)
    (B₀ B₁ B₂ : A) (d₀ d₁ : R)
    (hB₀ : B₀ ∈ T.H 2) (hB₁H : B₁ ∈ T.H 5)
    (hB₁s : B₁ ∈ shifted T 3) (hB₂s : B₂ ∈ shifted T 6) :
    T.tr (B₀ * (T.g 2 + d₀ • (1 : A)) * (B₁ * (T.g 5 + d₁ • (1 : A)) * B₂))
        * T.tr B₀ * T.tr B₁ * T.tr B₂
      = T.tr (B₀ * (T.g 2 + d₀ • (1 : A)) * B₁)
          * T.tr (B₁ * (T.g 5 + d₁ • (1 : A)) * B₂)
          * T.tr (B₀ * B₂) := by
  have hB₂s3 : B₂ ∈ shifted T 3 := shifted_antitone T (by norm_num) hB₂s
  have hfull := tr_atomChain_three T hdb B₀ B₁ B₂ d₀ d₁ hB₀ hB₁H hB₁s hB₂s
  have h01 : T.tr (B₀ * (T.g 2 + d₀ • (1 : A)) * B₁) = (T.z + d₀) * T.tr B₀ * T.tr B₁ :=
    tr_affine_letter T hdb 2 B₀ hB₀ B₁ hB₁s d₀
  have h12 : T.tr (B₁ * (T.g 5 + d₁ • (1 : A)) * B₂) = (T.z + d₁) * T.tr B₁ * T.tr B₂ :=
    tr_affine_letter T hdb 5 B₁ hB₁H B₂ hB₂s d₁
  have h02 : T.tr (B₀ * B₂) = T.tr B₀ * T.tr B₂ :=
    hdb 3 B₀ (T.H_mono (by norm_num) hB₀) B₂ hB₂s3
  rw [hfull, h01, h12, h02]
  ring

/-! ## 5. Anti-vacuity

Per AGENTS.md §3b-tax and the `verification-harness` discipline: a conditional
theorem whose hypothesis nothing can satisfy is vacuously true, and a property
whose body ignores its arguments is `True` however it is spelled. Both are
checked here, and the honest weakness of the available witness is made
machine-checked rather than left as prose — mirroring
`DisjointBlockTrace.towerSpan_of_constant`. -/

/-- **Satisfiability.** The one-dimensional tower over `R` with generator a fixed
unit satisfies the disjoint-block law, so every theorem above is conditioned on
something inhabited and none is vacuously true. -/
theorem disjointBlock_unitMarkovTrace {R₀ : Type*} [CommRing R₀] (u : R₀ˣ) :
    DisjointBlockMultiplicative (OcneanuTrace.unitMarkovTrace u) := by
  intro n a _ b _
  exact mul_comm a b ▸ rfl

/-- **…and so is the join**, by the main theorem. -/
theorem singleCrossingJoin_unitMarkovTrace {R₀ : Type*} [CommRing R₀] (u : R₀ˣ) :
    SingleCrossingJoin (OcneanuTrace.unitMarkovTrace u) :=
  singleCrossingJoin_of_disjointBlock _ (disjointBlock_unitMarkovTrace u)

/-- **🛑 The witness is DEGENERATE, and this makes that precise.**

If every `shifted n` is contained in the scalars then the disjoint-block law
holds using nothing about disjointness, nothing about the tower, and nothing
about `g`: `tr (a · r) = r · tr a = tr a · tr (r)` is linearity. So a witness
whose shifted subalgebras are scalar exercises **none** of what the law asserts.

`unitMarkovTrace`'s algebra *is* `R`, where `⊥ = ⊤`, so it is exactly such a
witness — satisfiability only, not evidence that the hypothesis is reasonable in
any interesting tower. This mirrors `towerSpan_of_constant` in the parent file,
for the same reason: the corpus has no tower with a genuinely growing filtration,
because Mathlib has no Hecke tower. -/
theorem disjointBlock_of_shifted_le_bot
    (h : ∀ n : ℕ, shifted T n ≤ (⊥ : Subalgebra R A)) :
    DisjointBlockMultiplicative T := by
  intro n a _ b hb
  obtain ⟨r, rfl⟩ := Algebra.mem_bot.1 (h n hb)
  have hcomm : a * algebraMap R A r = r • a := by
    rw [Algebra.algebraMap_eq_smul_one, mul_smul_comm, mul_one]
  have hscal : T.tr (algebraMap R A r) = r := by
    rw [Algebra.algebraMap_eq_smul_one, map_smul, T.tr_one, smul_eq_mul, mul_one]
  rw [hcomm, map_smul, hscal, smul_eq_mul]
  ring

/-- The degeneracy applies to the witness above: over `A = R` the scalars are
everything. -/
theorem shifted_unitMarkovTrace_le_bot {R₀ : Type*} [CommRing R₀] (u : R₀ˣ) (n : ℕ) :
    shifted (OcneanuTrace.unitMarkovTrace u) n ≤ (⊥ : Subalgebra R₀ R₀) := by
  intro x _
  exact Algebra.mem_bot.2 ⟨x, rfl⟩

/-- Over `A = R` the scalars are everything, so `shifted` is the whole algebra —
the other half of the degeneracy recorded above. -/
theorem mem_shifted_unitMarkovTrace {R₀ : Type*} [CommRing R₀] (u : R₀ˣ)
    (n : ℕ) (x : R₀) : x ∈ shifted (OcneanuTrace.unitMarkovTrace u) n :=
  (bot_le : (⊥ : Subalgebra R₀ R₀) ≤ shifted (OcneanuTrace.unitMarkovTrace u) n)
    (Algebra.mem_bot.2 ⟨x, rfl⟩)

/-- **The chain hypothesis is satisfiable at non-trivial length**, so
`tr_chainWord` is not vacuous for want of a layered list. A two-link chain (three
blocks) at the production levels 2 and 5, over the unit tower. -/
theorem layered_unitMarkovTrace_two {R₀ : Type*} [CommRing R₀] (u : R₀ˣ)
    (B₀ B₁ B₂ : R₀) (d₀ d₁ : R₀) :
    Layered (OcneanuTrace.unitMarkovTrace u) B₂ [(B₀, 2, d₀), (B₁, 5, d₁)] :=
  Layered.cons Algebra.mem_top (mem_shifted_unitMarkovTrace u 3 _)
    (Layered.cons Algebra.mem_top (mem_shifted_unitMarkovTrace u 6 _) Layered.nil)

/-- **The conclusion is not a tautology**: on the unit tower the two sides are
genuinely different expressions that happen to agree, and the bond factors are
`u + dₖ` rather than `1`. -/
theorem tr_chainWord_unit_two {R₀ : Type*} [CommRing R₀] (u : R₀ˣ)
    (B₀ B₁ B₂ d₀ d₁ : R₀) :
    (OcneanuTrace.unitMarkovTrace u).tr
        (chainWord (OcneanuTrace.unitMarkovTrace u) [(B₀, 2, d₀), (B₁, 5, d₁)] B₂)
      = B₀ * B₁ * B₂ * (((u : R₀) + d₀) * ((u : R₀) + d₁)) := by
  show B₀ * ((u : R₀) + d₀ • (1 : R₀)) * (B₁ * ((u : R₀) + d₁ • (1 : R₀)) * B₂)
      = B₀ * B₁ * B₂ * (((u : R₀) + d₀) * ((u : R₀) + d₁))
  simp only [smul_eq_mul, mul_one]
  ring

end QOU.MathlibExt.SingleCrossingChain
