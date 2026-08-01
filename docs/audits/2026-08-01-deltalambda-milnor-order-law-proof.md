# General Milnor order law — all-A lower bound `order(D_A) ≥ 2(A−1)` PROVED

**Date:** 2026-08-01
**Branch:** `claude/deltalambda-milnor-order-law-proof-2026-08-01` (PR #4471)
**Lean:** [`content/quantum-observable-universe/lean/QOU/MassTheory/MilnorOrderLawGeneral.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MilnorOrderLawGeneral.lean) (lean-direct exit 0, sorry-free)
**Predecessor:** #4389 [`MilnorParitySignLaw.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MilnorParitySignLaw.lean)

## The question

The leading Milnor order of the `A`-component Brunnian trace deficit
`D_A(h) = 1 − τ_A(h)` (`h = q − q⁻¹`) is claimed to be `leadingOrder A = 2(A−1)`.
#4389 proved this **only at A=3** (`borromean_deficit_order`, from the Borromean
closed form) and merely **recorded A=4 as a measured `def`** (`tauL4MeasuredOrder
:= 6.06`, #4378). Two data points are not a theorem. Can the all-A law be proved
from structure rather than measured order-by-order?

## What was proved (formalize-first, honest tiers made visible in the types)

The length-`A` iterated commutator of **pure-braid band generators** `A_{ij}`
carries one factor of `h²` per commutator level. Formalized as an **h-adic
filtration** on a generic algebra (`{R} [CommRing R]`, `{A} [Ring A] [Algebra R
A]`, §7c-clean; `ℝ` only for the A=3 tightness anchor):

| Object | Statement |
|--------|-----------|
| `HasOrder h k x` | `∃ c, x = algebraMap R A (h^k) · c` (divisible by `h^k`, `h` central) |
| `HasOrder.mul` | orders **add** under product (`p + q`) |
| `HasOrder.commutator` | orders **add** under `[x,y] = xy − yx` (`p + q`) — the h²-per-level engine |
| `HasOrder.trace` | an R-linear `τ` sends order-`k` to an `h^k`-divisible scalar |
| `iterCommTower` | left-normed tower `V(n+1) = [c(n+1), V n]`, each `c i` of order 2 |
| `iterCommTower_hasOrder` | **induction on n**: `HasOrder (2(n+1)) (V n)` |
| `brunnian_deficit_order_lower_bound` | **★ all-A:** `τ(w_A)` divisible by `h^{leadingOrder A} = h^{2(A−1)}` |

The single structural input is `A_{ij} − 1` divisible by `h` (each pure-braid band
generator lies in `ker(B_n ↠ S_n)`, i.e. `→ 1` at `q = 1`) — the topologically
verified fact underlying #4378's strand-forgetting `d_k` Brunnian check. It is
encoded as the hypothesis `∀ i, HasOrder h 2 (c i)` (each commutator building
block already an order-2 object), threaded honestly through the type — not asserted
as a numerical premise.

## Tier reached — epistemic status (STRICT, in the types)

| Claim | Status | Where |
|-------|--------|-------|
| `order(D_A) ≥ 2(A−1)` for **ALL** A ≥ 2 | **PROVED** (structural, 0 free params) | `brunnian_deficit_order_lower_bound` |
| `order(D_3) = 4` exactly (bound tight) | **PROVED** (cofactor(0) = 3/4 ≠ 0) | `borromean_tight_slice`, `borromean_cofactor_ne_zero_at_zero` |
| `order(D_4) = 6` | **MEASURED** (cited #4378) | `tauL4MeasuredOrder` |
| `order(D_A) = 2(A−1)` for ALL A (exact) | **OPEN** — conjecture class, NO instance | `MilnorExactOrderConjecture` |

**This is Tier 2 (bound) + honest partial, a genuine advance over #4389's two
isolated points.** The all-A **lower bound** is a real universal theorem; the exact
`=` case (leading coefficient ≠ 0 = length-A Milnor μ̄ nonvanishing) is genuinely
open and stated as a content-bearing conjecture class with **no instance** — the
honest open state. No flat `theorem general_order : leadingOrder A = 2(A−1)` is
asserted: that would launder the two-point pattern into a universal exact claim
(anti-laundering / "sorry-free ≠ derived" / "conditional-proved ≠
premise-established"). The A=3 tight slice is proved and shown to discharge the A=3
slice of the conjecture; the conditional `exact_order_of_conjecture` is verified
modulo the single open class instance (§3b-cond).

**Free parameters: 0.** Nothing fitted; the per-level h² input is a derivable
structural fact (pure braid → identity at q=1), the crossing/leading-coefficient
nonvanishing is left honestly open.

## Scope discipline (per AGENTS.md "refuted/ruled-out" + "open" STRICT)

This does **not** claim the exact order law; it proves a **lower bound** and leaves
the tightness open. It does not re-declare any closed item open (corpus-grep:
#4389/#4360/#4378 are the direct predecessors and are built upon, not
re-litigated). The bound is a scope-(b) structural statement backed by a proved
invariant (the h-adic filtration adds orders under commutator — proved in Lean),
so it is a legitimate universal claim, not a scope-(a) measured negative.

## Relation to #4389 and the deficit-sign work

Complementary. #4389 handles the **sign** law `sign(D_A) = (−1)^(A−1)` (A=3 proved,
A=4 measured, general conditional). This file handles the **order** law. Together
they pin both the magnitude scale (`h^{2(A−1)}`, this file, all-A lower bound) and
the sign (#4389). The magnitude/μ₃ closure work (#4463, #4404) is a distinct angle
(leading-coefficient *value*, not its order) — the exact-order conjecture here is
exactly the "leading coefficient ≠ 0" premise those probes measure.

## Files

- Lean: `content/quantum-observable-universe/lean/QOU/MassTheory/MilnorOrderLawGeneral.lean`
- Audit: this file
- Ledger row: `docs/coordination/option-e.md`
