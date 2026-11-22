/-
Copyright (c) 2026 litlfred. All rights reserved.

# The three-way wrong sign on `b₃` has ONE root, and uniform attraction does not escape it

Bean `qou-q8vl`; parents `qou-brng`, `qou-rwhv`, `qou-ix0x`. Formalize-first
(AGENTS.md §"Formalize-first probe discipline"): the structural claim is proved before any
numerical search over candidate interface letters.

## The problem this addresses

Three independent constructions give the connected three-body channel the wrong sign against
AME2020, which wants `b₃(³H) = +1.8081` and `b₃(³He) = +1.0443` MeV:

* the **count channel** (`qou-ix0x`, PR #7193) — `countChannel > 0` for `q₀ > 1`, where an
  attractive term is required;
* the **Ursell/Mayer cumulant** (`qou-rwhv`, PR #7198) — `b₃ = −φᵀ₃ < 0` by the alternation;
* the **dominant summand** (`qou-m8f3`, PR #7200) — exactly chain-edge additive, so `b₃ = 0`.

They look like three separate failures. They are one, and this file states it: **every bond
scalar the framework derives lies in the open interval `(0,1)`**, and that single fact decides
the sign in all three settings.

## What is new here, and what was already proved elsewhere

Already in the corpus, and **cited rather than restated** — the corpus-grep for this file found
each of these, and the novelty claim below is what survived it:

* `UrsellPartitionFunctionB3.b3corpus_neg` — bonds in `(0,1)` ⟹ `b₃ < 0`, **for a bond set
  where all three edges are present**;
* `AggregatorConvexity.wMult_b3_nonpos` — the **equal-bond** multiplicative cumulant is
  non-positive for every `f > −2`, attraction included. So "uniform attraction does not
  escape" is **already held at equal bonds**; what is new below is the *distinct*-bond chain;
* `QBeta.SingleCrossingAlwaysBinds.interface_mem_Ioo` / `single_crossing_binds` — the
  production family `σ + d·1`, `d ∈ [−h, 0]`, is confined to `(0,1)` and always binds. This
  file does **not** restate that; an earlier draft did, and it was a duplicate;
* `QBeta.InterfaceScalar.mu_sum_eq_one` — the two isospin-projector channels satisfy
  `μ₊ + μ₋ = 1` identically;
* `QBeta.InterfaceScalar.stacked_crossing_gt_one` — the two-crossing bond has `h·z + 1 > 1`.

Nothing had connected them. The gaps this file closes:

### 1. The chain is NOT covered by `b3corpus_neg`, and not by `wMult_b3_nonpos` either

The production `A = 3` word is a **chain**: `atom_braid_word_3A` lays down `A − 1` interfaces
in a line, so ³H `= p–n–n` carries bonds `{pn, nn}` and ³He `= p–p–n` carries `{pp, pn}` — the
third pair is *not bonded*. A missing bond is `f = 1` (the identity letter, `μ = 1`, `g = 0`),
and `b3corpus_neg`'s hypothesis is `f₁₃ < 1` **strictly**. So the theorem that is quoted for
the exclusion does not in fact apply to the shape the production word has. `wMult_b3_nonpos`
does not close the gap either: it is the **equal-bond** statement, and the two chain bonds are
of different types (`pn` and `nn` for ³H, `pp` and `pn` for ³He) with measurably different
factors. `b3corpus_chain_neg` supplies the missing case.

### 2. 🛑 Uniform attraction does NOT flip the chain sign

On a chain `φᵀ₃ = g₀₁·g₁₂`, a **product of two** Mayer variables — so its sign is invariant
under flipping *both* bonds from repulsive to attractive. Making every bond attractive leaves
`b₃ < 0` exactly as before (`b3corpus_chain_neg_of_same_sign` covers both cases in one
statement).

This corrects the escape hatch as it is currently written down. The Ursell audit §4 and the
AGENTS.md "Extensive-term frontier" bullet both say a positive term "needs a bond factor above
1". That is **necessary but not sufficient**: on a two-bond chain what is needed is that
*exactly one* of the two bonds exceed 1 (`b3corpus_chain_pos_iff`). A uniformly attractive
word is still wrong-signed.

### 3. The required pattern is sign-MIXED — and it is the isospin fact

³H needs `sign(g_pn) ≠ sign(g_nn)`; ³He needs `sign(g_pp) ≠ sign(g_pn)`. Both hold together
iff `g_pn` is opposite in sign to **both** like-pair bonds. Since `B_e = −α·log μ_e` is
positive exactly when `μ_e < 1`, that reads: *the unlike pair binds and the like pairs do
not* — which is the observed two-nucleon spectrum (the deuteron binds; the diproton and the
dineutron do not). So `b₃ > 0` and the correct two-body boundness pattern are **the same
condition**, not two independent ones. This is an observation about what the condition *is*,
not a construction chosen to meet it.

### 4. Both derived families are excluded from supplying it

* production letters: `d ≤ 0` caps `μ` at `z < 1`, so every bond is binding
  (`production_bond_mem_Ioo`);
* projector channels: `μ₊ + μ₋ = 1` is an **identity**, so an attractive channel `μ₊ > 1`
  forces `μ₋ < 0` (`attractive_projector_forces_negative_partner`) and `log μ₋` does not
  exist — the complementary channel has no real binding at all.

The second is the sharper exclusion: it is not an inequality that some other `q` might
reverse, it is a partition of unity.

## 🛑 SCOPE — what this does not do

**Scope (b)** for the sign, invariant named: the chain product structure of `φᵀ₃` together
with `(0,1)`-confinement of every derived bond. **Scope (a)** for everything else.

**🛑 It does NOT say a bond factor above `1` is the only escape.** That would be false:
`AggregatorConvexity.b3Agg_nonneg_of_convexOn` gives `b₃ ≥ 0` for any aggregator `Φ` that is
convex through the origin, with no bond factor leaving `(0,1)` at all. The statement here is
narrower and is about the *multiplicative* assembly only — within it, and on a chain, the sign
is the product of two Mayer signs.

A further caution against the obvious pattern: the raw stacked-bond factors `μ(σ^m)` do **not**
alternate by parity. Measured in `stacked_interface_writhe_normalised_probe.py`, `μ > 1` at
`m = +2, +4, +5, +6, +7, +8` — `+5` and `+7` are odd. An "even attracts, odd repels" reading is
refuted by the corpus's own table and must not be asserted.

It does **not** propose a letter with `μ > 1`. `stacked_crossing_gt_one` exhibits one (`σ²`),
but the topological argument that would select `σ²` assigns it to the *distinguishable* pair,
and `QBeta.InterfaceScalar.content_keyed_interface_refuted` plus the deuteron ordering
(`mu_singlet_lt_mu_triplet`) already exclude that assignment — it binds the diproton and
unbinds the deuteron. Choosing `σ²` for the like pairs *because* it yields `b₃ > 0` would be
selection against the target, which AGENTS.md §"NO FITTING" forbids. The gap stays open.

It also does not touch magnitude. `qou-brng` is untouched.

-- Ref: [leitner2026] .beans/qou-q8vl, docs/audits/2026-09-12-ursell-partition-function-for-b3.md
-/

import QOU.MassTheory.UrsellPartitionFunctionB3
import QOU.QBeta.InterfaceScalar
import Mathlib.Tactic

namespace QOU.MassTheory.B3SignOneRoot

open QOU.MassTheory.UrsellPartitionFunctionB3

/-! ### The chain: the bond set the production word actually has -/

variable {R : Type*} [CommRing R]

/-- **A missing bond is `f = 1`.** The production `A = 3` word bonds only adjacent nucleons,
so one of the three pairs carries no interface letter; its Mayer variable is `g = f − 1 = 0`.
On that bond set the third Ursell function collapses from four connected graphs to one — the
single path — and is a **product**. -/
theorem phi3_chain (g01 g12 : R) : phi3 g01 0 g12 = g01 * g12 := by
  unfold phi3; ring

/-- The corpus three-body cumulant on a chain, in closed form. -/
theorem b3corpus_chain (f01 f12 : R) :
    b3corpus f01 1 f12 = -((f01 - 1) * (f12 - 1)) := by
  unfold b3corpus W Z3; ring

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **The chain is not covered by `b3corpus_neg`.** That theorem needs all three bond factors
strictly inside `(0,1)`; the chain's absent bond sits at exactly `1`. Supplied here: bonds in
`(0,1)` on the two present edges still force `b₃ < 0`. -/
theorem b3corpus_chain_neg {f01 f12 : K} (h01 : 0 < f01 ∧ f01 < 1) (h12 : 0 < f12 ∧ f12 < 1) :
    b3corpus f01 1 f12 < 0 := by
  rw [b3corpus_chain]
  have : 0 < (1 - f01) * (1 - f12) := mul_pos (by linarith [h01.2]) (by linarith [h12.2])
  nlinarith

/-- **🛑 THE CORRECTION — uniform attraction does not escape.** On a chain `φᵀ₃` is a product
of two Mayer variables, so flipping *both* bonds from repulsive to attractive leaves the sign
of `b₃` unchanged. Both cases in one statement: whenever the two bonds sit on the same side of
`1`, `b₃ < 0`.

So "a positive term needs a bond factor above 1" is necessary, not sufficient. -/
theorem b3corpus_chain_neg_of_same_sign {f01 f12 : K}
    (h : (1 < f01 ∧ 1 < f12) ∨ (f01 < 1 ∧ f12 < 1)) :
    b3corpus f01 1 f12 < 0 := by
  rw [b3corpus_chain]
  rcases h with ⟨a, b⟩ | ⟨a, b⟩
  · have : 0 < (f01 - 1) * (f12 - 1) := mul_pos (by linarith) (by linarith)
    linarith
  · have : 0 < (1 - f01) * (1 - f12) := mul_pos (by linarith) (by linarith)
    nlinarith

/-- **The sharp condition.** On a two-bond chain the cumulant is positive exactly when the two
bonds lie on opposite sides of `1` — i.e. **exactly one** of them is attractive. -/
theorem b3corpus_chain_pos_iff {f01 f12 : K} :
    0 < b3corpus f01 1 f12 ↔ (f01 - 1) * (f12 - 1) < 0 := by
  rw [b3corpus_chain]; constructor <;> intro hyp <;> linarith

/-- **Restated as the mixed-sign requirement**, in the form the two `A = 3` chains impose:
one bond binding (`f < 1`) and the other anti-binding (`f > 1`). -/
theorem b3corpus_chain_pos_of_mixed {f01 f12 : K} (h01 : f01 < 1) (h12 : 1 < f12) :
    0 < b3corpus f01 1 f12 := by
  rw [b3corpus_chain_pos_iff]
  have : 0 < (1 - f01) * (f12 - 1) := mul_pos (by linarith) (by linarith)
  nlinarith

/-! ### Why no derived bond family can supply the mixed sign -/

/-- **The production interface family is confined to `(0,1)`** — *not proved here*. That is
`QBeta.SingleCrossingAlwaysBinds.interface_mem_Ioo` (`μ ≤ z < 1` whenever `q³ < q² + 1`, which
the substrate anchor satisfies with 24 % to spare). What this file adds is the consequence:
fed into `b3corpus_chain_neg`, it makes the production chain negative whatever the typing. The
hypothesis below is therefore stated as what it is — an input from that file. -/
theorem production_chain_b3_neg {f01 f12 : K}
    (h01 : 0 < f01 ∧ f01 < 1) (h12 : 0 < f12 ∧ f12 < 1) :
    b3corpus f01 1 f12 < 0 :=
  b3corpus_chain_neg h01 h12

/-- **The projector family cannot supply it either, and this is an identity not an
inequality.** `μ₊ + μ₋ = 1` (`QBeta.InterfaceScalar.mu_sum_eq_one`), so two positive channel
scalars are both below `1`. -/
theorem projector_bonds_lt_one {mp mm : K} (hsum : mp + mm = 1) (hp : 0 < mp) (hm : 0 < mm) :
    mp < 1 ∧ mm < 1 := by
  constructor <;> linarith

/-- **…and buying an attractive channel costs the partner its binding entirely.** If one
isospin channel is made anti-binding (`μ₊ > 1`), the partition of unity puts the other at
`μ₋ < 0`, where `−α·log μ₋` is not a real number. So the projector decomposition cannot host a
sign-mixed bond pair even in principle. -/
theorem attractive_projector_forces_negative_partner {mp mm : K}
    (hsum : mp + mm = 1) (hp : 1 < mp) : mm < 0 := by linarith

/-- **The one root, assembled.** If both chain bonds come from any family confined to `(0,1)` —
the production letters by `SingleCrossingAlwaysBinds.interface_mem_Ioo`, the isospin channels by
`projector_bonds_lt_one` — then the connected three-body cumulant is negative. One hypothesis,
one conclusion; the three constructions differ only in what they compute *around* it.

Stated with the confinement as an explicit hypothesis rather than derived, so that a future
family escaping `(0,1)` is visible as a failed hypothesis and not a hidden one. -/
theorem confined_bonds_force_b3_neg {f01 f12 : K}
    (h01 : 0 < f01 ∧ f01 < 1) (h12 : 0 < f12 ∧ f12 < 1) :
    b3corpus f01 1 f12 < 0 :=
  b3corpus_chain_neg h01 h12

/-! ### Anti-vacuity — every hypothesis is load-bearing -/

/-- **`(0,1)`-confinement is load-bearing, not decoration.** A mixed pair does give the AME
sign, so `confined_bonds_force_b3_neg` is not vacuously true of everything. -/
theorem mixed_pair_gives_positive_b3 :
    ∃ f01 f12 : ℚ, f01 < 1 ∧ 1 < f12 ∧ 0 < b3corpus f01 1 f12 := by
  refine ⟨1/2, 2, by norm_num, by norm_num, ?_⟩
  rw [b3corpus_chain]; norm_num

/-- **And uniform attraction is genuinely not enough** — a concrete both-above-`1` pair with a
negative cumulant, so `b3corpus_chain_neg_of_same_sign`'s first disjunct has content. -/
theorem both_attractive_still_negative :
    ∃ f01 f12 : ℚ, 1 < f01 ∧ 1 < f12 ∧ b3corpus f01 1 f12 < 0 := by
  refine ⟨2, 3, by norm_num, by norm_num, ?_⟩
  rw [b3corpus_chain]; norm_num

/-- **The chain really is different from the triangle.** With all three bonds present and equal
the cumulant stays negative, but the *reason* differs: there `φᵀ₃` has a sum of four terms, not
a single product. Exhibited so the chain collapse is not mistaken for a general fact. -/
theorem triangle_phi3_has_four_terms (g : R) :
    phi3 g g g = g * g * g + g * g + g * g + g * g := by
  unfold phi3; ring

end QOU.MassTheory.B3SignOneRoot
