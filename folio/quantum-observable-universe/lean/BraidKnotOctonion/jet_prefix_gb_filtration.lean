import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp

/-!
# QOU.BraidKnot.jet_prefix_gb_filtration

**Proposition** ([`conj:jet-prefix-gb-filtration`](../../../mass-theory/jet-prefix-gb-filtration.md)).

*Define the Gröbner–Shirshov-filtered prefix `β_k^GS` of an atomic braid word
`T_w ∈ H_{3A}(q)` as the projection onto the filtration stratum*

    β_k^GS := σ_{k-3}(T_w) ∈ J^{k-3}(q) / J^{k-2}(q).

*The jet-level prefix evaluates as*

    a_k(β_k^GS) = tr_M^{[ℓ]}(β_k^GS) / Σ_λ w_λ · dim Res^{H_k}_{H_3}(V_λ).

## 2026-09-03 — the Lean asserted a claim the block never makes

`JetPrefixGbFiltrationContext` carried `CategoricalObj`, `JetOrder` and
`GbDepth` as data plus `claim_jet_prefix_eq_gb_depth : JetOrder = GbDepth`,
and `jet_prefix_gb_filtration` returned that field — AGENTS.md §3b-cond
item 5.  With both naturals chosen by the instance, the "proposition" was
*two numbers I picked are equal*, and `CategoricalObj` was never used at all.

**But the projection is not the main defect here.** The encoded claim —
*"the jet-prefix filtration order coincides with the GB-filtration depth"* —
**appears nowhere in the block**.  The `.md` defines `β_k^GS` and states an
evaluation formula for `a_k`; it says nothing about an order equalling a
depth.  This is not a weakened statement, it is a **different** one, and the
substitute happens to be trivially satisfiable.

**And the docstring blamed the `.md` for its own truncation.**  The class
docstring said the proposition was *"truncated in the sibling .md"*, and the
declaration docstring's "Proposition statement (from manuscript)" read, in
full, *"Define the"*.  The `.md` is neither truncated nor short: it carries
both display equations above and a closing paragraph.  What was truncated was
the copy into this file.

## Disposition: name the block's actual claim (AGENTS.md §1a, disposition 3)

`jet_prefix_gb_filtration` now states the **evaluation formula** — the
block's mathematical content — over caller-supplied data, and asserts none of
it.  `trM_eq_of_jet_prefix` derives the cleared-denominator form, which is
the one consequence available without the filtration machinery.

## The nonzero-denominator hypothesis is load-bearing

Lean's `x / 0 = 0`, so with an empty partition set the formula reads
`a_k = 0` and is *satisfied* by `a_k = 0` — telling you nothing.  That is a
convention artefact, not mathematics, which is why `trM_eq_of_jet_prefix`
takes `Σ_λ w_λ · dim Res ≠ 0` explicitly rather than leaving it implicit in
the division.

## What is still unencoded

Everything that makes the formula about braids: `H_{3A}(q)`, the atomic braid
word `T_w`, the Gröbner–Shirshov filtration `J^•(q)` and its strata, the
symbol map `σ_{k-3}`, the partial Markov trace `tr_M^{[ℓ]}`, and the
restriction multiplicities `dim Res^{H_k}_{H_3}(V_λ)` — all are reals and
finite sums the caller supplies.

The closest true statement to the deleted claim is an **indexing** fact: the
symbol map's index and the stratum's lower index agree (`σ_{k-3}` into
`J^{k-3}/J^{k-2}`), so the stratum has width one.  Encoding it needs the
filtration itself, which is not here; it is recorded so the deleted field is
not mistaken for having had a defensible reading.

Bean `qou-z9ws`.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/jet-prefix-gb-filtration.md
-/

namespace QOU.BraidKnot

/-- **The jet-level prefix evaluation**
([`conj:jet-prefix-gb-filtration`](../../../mass-theory/jet-prefix-gb-filtration.md)),
as a proposition over caller-supplied data:

    a_k = tr_M^{[ℓ]}(β_k^GS) / Σ_λ w_λ · dim Res^{H_k}_{H_3}(V_λ).

**Named, not asserted.**  See the module docstring for what the previous
encoding claimed instead, and for what this formula would need in order to be
about braids rather than about reals. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/jet-prefix-gb-filtration.md
def jet_prefix_gb_filtration {P : Type} (partitions : Finset P)
    (w dimRes : P → ℝ) (a_k trM : ℝ) : Prop :=
  a_k = trM / (partitions.sum fun lam => w lam * dimRes lam)

/-- **The cleared-denominator form**, derived.

When the weighted restriction-multiplicity sum is nonzero, the evaluation is
equivalent to `a_k · Σ_λ w_λ · dim Res = tr_M^{[ℓ]}`.

The hypothesis is doing real work rather than tidying: Lean's `x / 0 = 0`
means that with a vanishing denominator the formula is *satisfied* by
`a_k = 0` and constrains nothing, so the division alone does not carry the
mathematical content. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/jet-prefix-gb-filtration.md
theorem trM_eq_of_jet_prefix {P : Type} {partitions : Finset P}
    {w dimRes : P → ℝ} {a_k trM : ℝ}
    (hne : (partitions.sum fun lam => w lam * dimRes lam) ≠ 0)
    (h : jet_prefix_gb_filtration partitions w dimRes a_k trM) :
    a_k * (partitions.sum fun lam => w lam * dimRes lam) = trM := by
  simp only [jet_prefix_gb_filtration] at h
  rw [h]
  field_simp

/-- **The evaluation is refutable at freely-chosen data**, which is why it is
named rather than carried as a `sorry`.

With no partitions the denominator is `0`, so the right-hand side is `0` and
`a_k = 1` fails. -/
theorem not_jet_prefix_gb_filtration_of_free_data :
    ¬ jet_prefix_gb_filtration (∅ : Finset ℕ) (fun _ => 0) (fun _ => 0) 1 0 := by
  simp [jet_prefix_gb_filtration]

end QOU.BraidKnot
