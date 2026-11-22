/-
# QOU.Hecke.ClosedFormInterfaceFactors — Phase-5q closed-form interface factors

Fibre-level (pre-archimedean, generic field — AGENTS.md §7c) formalization of
the algebraic layer of the Phase-5q closed form

  tr_M(𝓑_K) = tr_M³(𝓑_p)^Z · tr_M³(𝓑_n)^N · ∏_i f_i(q),
  f_pp = z,   f_nn = z − h,   f_pn = z − h·(1/2 − δ(q)/4),

with Markov parameter `z = q³/(q²+1)` (**convention D**, canonical per the
owner ruling of 2026-08-15), Hecke skein parameter
`h = q − q⁻¹`, and the PROVEN leading flavor split
`δ(q) = (q−1)²·(1−q⁻⁴)/3` (conj:flavor-split-substrate-mass; the posited
subleading `(1+ℏ_q³)` correction was de-wired 2026-06-29 and is NOT used).

Everything is stated in the variable `s` with `q = s²` over a generic
`{R : Type u} [Field R]`:

  z = s⁶/(s⁴+1),   h = s² − s⁻²,
  δ = (s²−1)²·(1 − s⁻⁸)/3.

**The `s` substitution is now vestigial.** It existed to express `√q` without
`Real.sqrt`, so the file could stay on the substrate side of the AGENTS.md §7c
wall while carrying convention C's `z = 1/(√q + 1/√q)`. Convention D has no
square root in it, so `s` buys nothing here any more; rewriting the file in `q`
is a separate follow-up (see the `markovZ` docstring). Migrated 2026-08-26,
bean `qou-cxjq` — this module's header is where that bean started, because it
stated the substitution in plain English and every detector read past it.

## Two different involutions are both called "bar" in this file

Read the word with its object attached; they are not the same map and one is
convention-dependent while the other is not.

* **The `q`-bar**, `q ↦ q⁻¹` (in `s`: `s ↦ s⁻¹`). This is §3's subject, and it
  is the one the convention change moves.
* **The skein bar**, crossing reversal `σ ↦ σ⁻¹`. This is what "bar-symmetric"
  means in `QOU.BraidKnot.interface_knot_markov_z_bar_symmetric`, which is
  about `τ_M(α·(σ + σ⁻¹)) = (2z − h)·τ_M(α)`, and it is what the §5 epithets
  mean. It is a statement about crossings, not about `q`, so it survives any
  convention for `z` untouched.

`z − h/2` is symmetric under the **skein** bar (it is the average of the two
chiralities). Whether it is *also* invariant under the **`q`**-bar is
convention-dependent — and the two conventions answer oppositely:

* **Convention C.** `q`-bar fixes `z` and flips `h`, so `z − h/2 ↦ z + h/2`:
  **not** invariant, defect `h`.
* **Convention D (canonical).** `q`-bar sends `z ↦ z/q⁴`, and under D that
  weight is not merely a scaling — it is *exactly* the shift `z ↦ z − h`
  (`markovZ_weight_eq_shift`, an identity, not an approximation). So
  `z − h/2 ↦ (z − h) + h/2 = z − h/2`: **invariant**
  (`strictAvg_bar_invariant`), and `z − h/2` is precisely the `q`-bar
  symmetriser `(z(q) + z(q⁻¹))/2` (`strictAvg_eq_bar_symmetriser`).

The sign flip on `h` is what *produces* the invariance under D, not what
prevents it. A 2026-08-26 revision of this header asserted non-invariance
"under either convention" on the strength of that flip; the C half of that
sentence was right and the D half was the C result generalised. Corrected
2026-08-26 (this file's §3a), consistent with
`QOU.MassTheory.strictPn_eq_barSymmetriser`, which has proved the D statement
since PR #5769.

None of this reaches `f_pn` itself: the canonical bring-color-weighted factor
`z − h(1/2 − δ/4)` is **not** `q`-bar invariant, because `δ` is bar-odd only up
to weight (`flavorDelta_bar`). See §5 and bean `qou-1oxx`.

## What is proved sorry-free here

* the defining form of the Markov parameter, `z_D = q²·(q + q⁻¹)⁻¹`
  (`markovZ_eq_sq_mul_inv_sum`);
* `q`-bar behaviour under `s ↦ s⁻¹`: `z` bar-COVARIANT of weight `−4`
  (`z(q⁻¹) = z(q)/q⁴`), `h` bar-odd, `δ(q⁻¹) = −q²·δ(q)`, and the induced
  action on the factors;
* the exact cubic-vanishing factorization
  `δ = (q−1)³(q³+q²+q+1)/(3q⁴)` — third-order zero at `q = 1` — and the
  structural identity `δ = ℏ_q²·h·[2]_q/3`;
* factor algebra: `f_pp·f_nn = z² − z·h`, `f_pp + f_nn = 2z − h`,
  `f_pn = (f_pp+f_nn)/2 + h·δ/4` (bring-color-weighted p-n factor =
  skein-symmetric chirality average + flavor-split correction), and the
  division-free
  bridging form `4·f_pn = 4z − (2−δ)·h`;
* confluence at `q = 1`: all three factors collapse to `z(1) = 1/2`-slot
  value `markovZ 1` (since `h(1) = 0`);
* the interface-list assembly layer: for any interface multiset the closed
  form's product `∏_i f_i` equals `f_pp^{#pp}·f_nn^{#nn}·f_pn^{#pn}`, and
  for the canonical `p^Z n^N` ordering of `closed_form_tau_M.
  canonical_interface_kinds` (protons first, then neutrons: `Z−1` p-p
  bonds, one p-n bond, `N−1` n-n bonds) the closed form specialises to
  `τ_p^Z·τ_n^N·f_pp^{Z−1}·f_nn^{N−1}·f_pn`, with the deuteron instance
  `τ_p·τ_n·f_pn`;
* the trace bridge: via the existing `QOU.Hecke.MarkovTrace` class, the
  Markov trace of each bridge crossing `σ_i + d_k·1` equals the matching
  interface factor when `z_param = markovZ s`
  (`trace_interface_bond`, extending `trace_bond_crossing` of
  `MarkovBondFactor.lean` to the three named bond kinds).

## What is NOT claimed here (honest boundary)

The identification of the full `H_{3A}` Markov trace of the canonical atom
braid with the bond-factorized product for general `A` (the cross-level
Markov-axiom word induction) is not carried by the `MarkovTrace` class yet
— the same gap documented at `markov_trace_unique` and in
`MarkovBondFactor.lean`. That analytic step is verified exactly in ℚ at
rational `s`-points for D and T, and to 1e-49 at the four anchor atoms, by
`computations/probe_9b_laurent_degree_10a5.py` (11/11 assertions) and the
Phase-5q witness `closed-form-tau-M-verification-phase5q.witness.json`.
This module proves the complete algebraic layer downstream of that step.

## Relation to existing modules (reconciliation 2026-07-06, PR #3247)

The ABSTRACT fold form of the interface product is already formalized in
`mass-theory/interface-knot-markov-z.lean` (`interfaceTrace` over
`List Bool` with generic `z`/`z−h`, plus the skein-bar-symmetric averaged
`2z−h` form) — that module carried the bean-`s1ik` subsumption finding
(PR #3329), together with the Phase-5l constituent multiplicativity
proved separately. THIS module is the EXPLICIT-factor complement, not a
duplicate: it names the three bond kinds with the proven flavor split
`δ(q)` (so `f_pn = (f_pp+f_nn)/2 + h·δ/4`, absent from the abstract
fold), proves per-factor `q`-bar behaviour and the `δ` cubic
factorization, assembles the canonical `Z/N` product, and bridges each
named factor to the `MarkovTrace` class via the `(c, d)` bond data of
`MarkovBondFactor.lean`.

## References

- [jones1987] https://doi.org/10.2307/1971403
- [leitner2026] prop:constit-factor-tau-M-proton-identity (Phase 5l)
- [leitner2026] prop:interface-knot-markov-z (Phase 5c.1)
- [leitner2026] conj:flavor-split-substrate-mass (PR #690 leading split)
- computations/closed_form_tau_M.py (conventions; bring_color_weighted)
- computations/probe_9b_laurent_degree_10a5.py (exact-ℚ verification)
-/

import QOU.Hecke.MarkovTrace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.Hecke.ClosedForm

universe u

variable {R : Type u} [Field R]

/-! ## §1. The primary parameters in the square-root variable `s` (q = s²) -/

/-- Markov parameter in **convention D**, `z_D = q³/(q²+1)`, written in the
square-root variable `s` (`q = s²`) as `s⁶/(s⁴+1)`.

**Migrated from convention C 2026-08-26 (bean `qou-cxjq`).** This read
`s/(s²+1)`, which at `q = s²` is `√q/(q+1)` — convention C. This file's
docstring is where the whole bean started: it states the `s`-substitution in
plain English, and every detector missed it because the convention was hidden by
a change of variable rather than a change of form.

**The `s` apparatus is now VESTIGIAL, and that is the follow-up this commit does
not do.** The entire reason for `s` was to express `√q` without `Real.sqrt`, so
the file could stay on the substrate side of the AGENTS.md §7c wall. Convention D
has no square root in it at all — `q³/(q²+1)` is rational in `q` directly — so
the substitution buys nothing here any more, and `s⁶/(s⁴+1)` is strictly uglier
than the `q` form it encodes. Rewriting the file in `q` is the right cleanup and
is a separate, larger change across 22 theorems; doing it in the same commit as
the convention migration would make both unreviewable.

Migrated in place because this module has **zero importers** — verified by module
import, not by name grep — so no recorded statement outside it changes meaning. -/
def markovZ (s : R) : R := s ^ 6 / (s ^ 4 + 1)

/-- Hecke skein parameter `h = q − q⁻¹ = s² − s⁻²`. -/
def heckeH (s : R) : R := s ^ 2 - (s ^ 2)⁻¹

/-- Substrate Planck parameter `ℏ_q = 1 − q⁻¹` (in `s`: `1 − s⁻²`). -/
def hbarQ (s : R) : R := 1 - (s ^ 2)⁻¹

/-- Quantum integer `[2]_q = q + q⁻¹` (in `s`: `s² + s⁻²`). -/
def quantumTwo (s : R) : R := s ^ 2 + (s ^ 2)⁻¹

/-- PROVEN leading flavor split `δ(q) = (q−1)²·(1−q⁻⁴)/3`
(conj:flavor-split-substrate-mass, `_li_2_q_util.flavor_split_leading`).
In `s`: `(s²−1)²·(1−s⁻⁸)/3`. -/
def flavorDelta (s : R) : R := (s ^ 2 - 1) ^ 2 * (1 - ((s ^ 2) ^ 4)⁻¹) / 3

/-! ## §2. The three interface factors -/

/-- p-p interface factor `f_pp = z` (positive crossing, Markov axiom). -/
def fPP (s : R) : R := markovZ s

/-- n-n interface factor `f_nn = z − h` (negative crossing, Markov axiom +
Hecke skein `σ⁻¹ = σ − h·1`). -/
def fNN (s : R) : R := markovZ s - heckeH s

/-- Bring-color-weighted p-n interface factor
`f_pn = z − h·(1/2 − δ/4)` (canonical convention since 2026-06-01,
`closed_form_tau_M.closed_form_ratio` with the PROVEN leading `δ`). -/
def fPN (s : R) : R := markovZ s - heckeH s * (1 / 2 - flavorDelta s / 4)

/-! ## §3. √q form and bar-involution behaviour (`s ↦ s⁻¹`, i.e. `q ↦ q⁻¹`) -/

/-- **`z_D = q² · (q + q⁻¹)⁻¹`**: the defining form of the Markov parameter in
convention D, written in `s` with `q = s²`.

**Replaces `markovZ_eq_inv_sqrt_sum` (2026-08-26, bean `qou-cxjq`).** That
theorem said `z = (s + s⁻¹)⁻¹`, i.e. `1/(√q + 1/√q)` — the convention-C defining
identity. It is **false** under convention D and was re-derived, not repaired:
`(s + s⁻¹)⁻¹ = s/(s²+1) = √q/(q+1)`, which is convention C by definition.

The D form keeps the same `1/(x + x⁻¹)` shape but evaluates it at `x = q` rather
than `x = √q`, and rescales by `q²` — which is exactly the factorisation
`z_D = q² · g(q)` of `QOU.BraidKnot.markovZD_eq_sq_mul_kernel`. The rescaling is
not cosmetic: no argument at all sends `g` to `z_D`, by
`no_kernel_instantiation_is_conventionD`. -/
theorem markovZ_eq_sq_mul_inv_sum (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0) :
    markovZ s = (s ^ 2) ^ 2 * (s ^ 2 + (s ^ 2)⁻¹)⁻¹ := by
  unfold markovZ
  have hs2 : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  field_simp

/-- Helper: `(s⁻¹)² + 1` is a unit multiple of `s² + 1`. -/
theorem inv_sq_add_one_eq (s : R) (hs : s ≠ 0) :
    (s⁻¹) ^ 2 + 1 = (s ^ 2)⁻¹ * (s ^ 2 + 1) := by
  field_simp
  ring

/-- **`z_D` is bar-COVARIANT of weight `−4`, not bar-even**:
`z_D(q⁻¹) = z_D(q) / q⁴` (in `s`: divided by `s⁸`).

**Replaces `markovZ_bar` (2026-08-26, bean `qou-cxjq`), which does not survive
the convention change.** That theorem asserted `z(q⁻¹) = z(q)` — *"`z` is
bar-even"* — and it is a genuine property of convention C:
`z_C(q⁻¹) = √(q⁻¹)/(q⁻¹+1) = √q/(q+1) = z_C(q)` identically. Convention D is
neither bar-even nor bar-odd: `z_D(q⁻¹) = 1/(q³+q)` against `z_D(q) = q³/(q²+1)`,
equal only at `q = 1`.

So this is a theorem that **does not survive**, not a proof that needed
repairing — the second such in this bean, after the bar-antisymmetry result in
`nuclear-interactions/q-beta-cos-resummation.lean`, and the first stated as a
named headline result.

**What survives is better than nothing: the bar structure is graded rather than
destroyed.** The involution still acts on `z` cleanly, with weight `q⁻⁴` instead
of trivially. Any downstream argument that used bar-evenness as a *symmetry* must
now carry that weight; an argument that only needed `z` to have *some* definite
bar behaviour still has one.

Independently corroborated from the p-n side by `qou-1oxx` ("the canonical p-n
convention is not bar-invariant") and `QOU.QBeta.ZBarParity`. -/
theorem markovZ_bar_weight (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0) :
    markovZ s⁻¹ = markovZ s / (s ^ 2) ^ 4 := by
  have hs4 : s ^ 4 ≠ 0 := pow_ne_zero 4 hs
  have hinv : (s⁻¹) ^ 4 + 1 = (s ^ 4)⁻¹ * (s ^ 4 + 1) := by
    field_simp
    ring
  have hd : (s⁻¹) ^ 4 + 1 ≠ 0 := by
    rw [hinv]; exact mul_ne_zero (inv_ne_zero hs4) h4
  unfold markovZ
  rw [div_eq_iff hd]
  field_simp
  ring

/-- **`h` is bar-odd**: `h(q⁻¹) = −h(q)` — the Hecke skein parameter changes
sign under the bar involution (the skein swaps `σ ↔ σ⁻¹`). -/
theorem heckeH_bar (s : R) : heckeH s⁻¹ = - heckeH s := by
  unfold heckeH
  rw [inv_pow, inv_inv]
  ring

/-- **`δ` bar behaviour**: `δ(q⁻¹) = −q²·δ(q)` (in `s`: `−s⁴·δ`). The flavor
split is bar-odd up to the weight-two factor `q²` — consistent with its
`ℏ_q²·h·[2]_q/3` decomposition (`ℏ_q(q⁻¹) = −q⁻¹·ℏ_q(q)` twice, `h` odd,
`[2]_q` even). -/
theorem flavorDelta_bar (s : R) (hs : s ≠ 0) :
    flavorDelta s⁻¹ = -(s ^ 4) * flavorDelta s := by
  unfold flavorDelta
  field_simp
  ring

/-- Bar swap on the factors: the positive-crossing factor is bar-COVARIANT of
weight `−4`, `f_pp(q⁻¹) = f_pp(q)/q⁴`.

**Re-derived, not repaired (2026-08-26, bean `qou-cxjq`).** The convention-C
statement was `fPP s⁻¹ = fPP s` — bar-*invariance* — proved by one-line delegation
to `markovZ_bar`. Since `f_pp = z` definitionally, this theorem is exactly as
strong as the bar behaviour of `z`, and inherits the weight that
`markovZ_bar_weight` records. -/
theorem fPP_bar_weight (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0) :
    fPP s⁻¹ = fPP s / (s ^ 2) ^ 4 := markovZ_bar_weight s hs h4

/-- Bar swap on the factors: the negative-crossing factor goes to
`z/q⁴ + h` — **bar still exchanges the crossing chirality**, now against a
weight-`−4` `z`.

**This is the part of the C-era `fNN_bar` that survives.** That theorem read
`f_nn(q⁻¹) = f_pp(q) + h(q)`, and its content was two independent facts: the
sign flip on `h` (bar-odd — the skein swaps `σ ↔ σ⁻¹`) and the bar-invariance of
`z`. Only the second is convention-dependent, so the chirality exchange — the
part the name is about — is untouched; the `z` term carries `q⁻⁴`.

Concretely: `heckeH_bar` is used verbatim, `markovZ_bar` is replaced by
`markovZ_bar_weight`, and the `+ h` on the right-hand side is unchanged. -/
theorem fNN_bar_weight (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0) :
    fNN s⁻¹ = fPP s / (s ^ 2) ^ 4 + heckeH s := by
  unfold fNN
  rw [markovZ_bar_weight s hs h4, heckeH_bar s]
  unfold fPP
  ring

/-! ## §3a. Under convention D the bar weight *is* a shift, and the strict
average is bar-invariant -/

/-- **The weight-`−4` scaling and the `−h` shift are the same map.**

`z/q⁴ = z − h` is an identity of convention D, not a coincidence at one point:

  `z/q⁴ = q³/(q⁴(q²+1)) = 1/(q(q²+1))`,
  `z − h = q³/(q²+1) − (q²−1)/q = (q⁴ − (q⁴−1))/(q(q²+1)) = 1/(q(q²+1))`.

This is the fact that reconciles `markovZ_bar_weight` ("bar scales `z` by
`q⁻⁴`") with `QOU.MassTheory.barZ` ("bar sends `z` to `z − h`"): the two
statements are the same statement. Reading the weight as a *mere* rescaling —
one that leaves an `h` uncancelled — is what makes the strict average look
bar-broken under D when it is not. -/
theorem markovZ_weight_eq_shift (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0) :
    markovZ s / (s ^ 2) ^ 4 = markovZ s - heckeH s := by
  unfold markovZ heckeH
  field_simp
  ring

/-- **The `q`-bar of `z` is the shift by `−h`**: `z(q⁻¹) = z(q) − h(q)`.

The `s`-variable twin of `QOU.MassTheory.barZ`; obtained by composing
`markovZ_bar_weight` with `markovZ_weight_eq_shift`. -/
theorem markovZ_bar_eq_shift (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0) :
    markovZ s⁻¹ = markovZ s - heckeH s := by
  rw [markovZ_bar_weight s hs h4, markovZ_weight_eq_shift s hs h4]

/-- **The bar carries the p-p factor onto the n-n factor exactly**, with no
residual weight: `f_pp(q⁻¹) = f_nn(q)`. -/
theorem fPP_bar_eq_fNN (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0) :
    fPP s⁻¹ = fNN s := by
  unfold fPP fNN
  exact markovZ_bar_eq_shift s hs h4

/-- **…and back**: `f_nn(q⁻¹) = f_pp(q)`. Together with `fPP_bar_eq_fNN` this
says the two like-flavour factors are a single two-element orbit of the
involution — the sharp form of `fNN_bar_weight`, whose right-hand side
`z/q⁴ + h` is `f_pp` written the long way round. -/
theorem fNN_bar_eq_fPP (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0) :
    fNN s⁻¹ = fPP s := by
  unfold fNN fPP
  rw [markovZ_bar_eq_shift s hs h4, heckeH_bar s]
  ring

/-- **The strict-averaged interface factor is the `q`-bar symmetriser**:
`z − h/2 = (z(q) + z(q⁻¹))/2`.

`s`-variable twin of `QOU.MassTheory.strictPn_eq_barSymmetriser`. -/
theorem strictAvg_eq_bar_symmetriser (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0)
    (h2 : (2 : R) ≠ 0) :
    markovZ s - heckeH s / 2 = (markovZ s + markovZ s⁻¹) / 2 := by
  rw [markovZ_bar_eq_shift s hs h4]
  field_simp
  ring

/-- **The strict-averaged interface factor is `q`-bar INVARIANT under
convention D**: `z(q⁻¹) − h(q⁻¹)/2 = z(q) − h(q)/2`.

Being a symmetriser (`strictAvg_eq_bar_symmetriser`) it could hardly be
otherwise. The `2 ≠ 0` hypothesis is not boilerplate: in characteristic 2 the
average is not defined and the statement degenerates, exactly as in
`QOU.MassTheory.PnInterfaceBarStructure`, which assumes `CharZero` for the
same reason. Stated separately because it is the claim that the header of this
file briefly denied: the bar flips the sign of `h`, and *that flip is exactly
what cancels the shift* `z ↦ z − h`.

Convention C behaves oppositely — there `z` is bar-fixed, so the flipped `h`
has nothing to cancel against and the defect is `h`. -/
theorem strictAvg_bar_invariant (s : R) (hs : s ≠ 0) (h4 : s ^ 4 + 1 ≠ 0)
    (h2 : (2 : R) ≠ 0) :
    markovZ s⁻¹ - heckeH s⁻¹ / 2 = markovZ s - heckeH s / 2 := by
  rw [markovZ_bar_eq_shift s hs h4, heckeH_bar s]
  field_simp
  ring

/-! ## §4. Structure of the flavor split `δ` -/

/-- **Structural identity** `δ = ℏ_q² · h · [2]_q / 3`
(conj:flavor-split-substrate-mass; `_li_2_q_util.flavor_split_leading`
docstring). -/
theorem flavorDelta_eq_hbar_form (s : R) (hs : s ≠ 0) :
    flavorDelta s = hbarQ s ^ 2 * heckeH s * quantumTwo s / 3 := by
  unfold flavorDelta hbarQ heckeH quantumTwo
  field_simp
  ring

/-- **Exact cubic-vanishing factorization** (the leading-order identity):

  `δ(q) = (q−1)³ · (q³+q²+q+1) / (3q⁴)`,

exhibiting the third-order zero of the flavor split at `q = 1` exactly —
the algebraic content of the `δ ≈ (4/3)(q−1)³` leading order. Stated in
`s` with `q = s²`. -/
theorem flavorDelta_factored (s : R) (hs : s ≠ 0) (h3 : (3 : R) ≠ 0) :
    flavorDelta s
      = (s ^ 2 - 1) ^ 3 * (s ^ 6 + s ^ 4 + s ^ 2 + 1) / (3 * s ^ 8) := by
  unfold flavorDelta
  field_simp
  ring

/-- `δ(1) = 0`: no flavor split at the classical point `q = 1`. -/
theorem flavorDelta_one : flavorDelta (1 : R) = 0 := by
  norm_num [flavorDelta]

/-- `h(1) = 0`: the skein parameter vanishes at `q = 1`. -/
theorem heckeH_one : heckeH (1 : R) = 0 := by
  norm_num [heckeH]

/-! ## §5. Factor algebra -/

/-- `f_pp · f_nn = z² − z·h`: the p-p/n-n product needed by the closed
form's Laurent-degree bookkeeping (probe 9b). Pure ring identity. -/
theorem fPP_mul_fNN (s : R) :
    fPP s * fNN s = markovZ s ^ 2 - markovZ s * heckeH s := by
  unfold fPP fNN
  ring

/-- `f_pp + f_nn = 2z − h`: twice the strict-averaged interface factor
`z − h/2`, the combination symmetric under the **skein** bar `σ ↦ σ⁻¹`
(`interface_knot_markov_z_bar_symmetric`).

Under convention D it is **also** invariant under the `q`-bar of §3, because
the bar exchanges the two summands exactly (`fPP_bar_eq_fNN`,
`fNN_bar_eq_fPP`) rather than merely rescaling them — see
`strictAvg_bar_invariant`. Under convention C it was not: there `q`-bar fixes
`z` while flipping `h`, so `z − h/2 ↦ z + h/2`. -/
theorem fPP_add_fNN (s : R) :
    fPP s + fNN s = 2 * markovZ s - heckeH s := by
  unfold fPP fNN
  ring

/-- **The bring-color-weighted p-n factor is the skein-symmetric chirality
average plus the flavor-split correction**:

  `f_pn = (f_pp + f_nn)/2 + h·δ/4`.

At `δ = 0` this recovers the strict-averaged convention `z − h/2`; the
`h·δ/4` term is the quaternionic color-tube asymmetry
(`closed_form_tau_M` §"bring_color_weighted"). -/
theorem fPN_eq_skein_avg_add_flavor (s : R) (h2 : (2 : R) ≠ 0) :
    fPN s = (fPP s + fNN s) / 2 + heckeH s * flavorDelta s / 4 := by
  have h4 : (4 : R) ≠ 0 := by
    have h : (4 : R) = 2 * 2 := by norm_num
    rw [h]
    exact mul_ne_zero h2 h2
  unfold fPN fPP fNN
  field_simp
  ring

/-- Division-free bridging form `4·f_pn = 4z − (2 − δ)·h` — the shape used
by the Markov-step identity `τ_M(α·(4σ − (2−δ)h·1)) = (4z − (2−δ)h)·τ_M(α)`
(cf. `QOU.BraidKnot.interface_knot_markov_z_bar_symmetric` for the δ = 0
case). -/
theorem fPN_four_mul (s : R) (h2 : (2 : R) ≠ 0) :
    4 * fPN s = 4 * markovZ s - (2 - flavorDelta s) * heckeH s := by
  have h4 : (4 : R) ≠ 0 := by
    have h : (4 : R) = 2 * 2 := by norm_num
    rw [h]
    exact mul_ne_zero h2 h2
  unfold fPN
  field_simp
  ring

/-- Confluence at `q = 1`: the n-n factor collapses onto the p-p factor
(`h(1) = 0`). -/
theorem fNN_one : fNN (1 : R) = fPP 1 := by
  unfold fNN fPP
  rw [heckeH_one]
  ring

/-- Confluence at `q = 1`: the p-n factor collapses onto the p-p factor
(`h(1) = 0` kills both the averaging and the flavor terms). -/
theorem fPN_one : fPN (1 : R) = fPP 1 := by
  unfold fPN fPP
  rw [heckeH_one]
  ring

/-! ## §6. Interface-list assembly of the closed form -/

/-- The three interface kinds of the canonical atomic braid `𝓑_K`
(`closed_form_tau_M.canonical_interface_kinds`): p-p (positive crossing),
n-n (negative crossing), p-n (bring-color-weighted averaged crossing). -/
inductive InterfaceKind : Type
  | pp
  | nn
  | pn
  deriving DecidableEq, Repr

/-- Per-interface factor `f_i(q)` of the closed form. -/
def interfaceFactor (s : R) : InterfaceKind → R
  | .pp => fPP s
  | .nn => fNN s
  | .pn => fPN s

/-- The interface product `∏_i f_i(q)` over an interface list. -/
def closedFormProduct (s : R) (ks : List InterfaceKind) : R :=
  (ks.map (interfaceFactor s)).prod

/-- **Assembly layer of the Phase-5q closed form**: the full closed-form
value `tr_M³(𝓑_p)^Z · tr_M³(𝓑_n)^N · ∏_i f_i(q)` from the two `H₃`
building blocks (`closed_form_tau_M.closed_form_tau_M`). -/
def closedFormTauM (s tauP tauN : R) (Z N : ℕ)
    (ks : List InterfaceKind) : R :=
  tauP ^ Z * tauN ^ N * closedFormProduct s ks

/-- The interface product depends only on the interface **census**:
`∏_i f_i = f_pp^{#pp} · f_nn^{#nn} · f_pn^{#pn}`. -/
theorem closedFormProduct_eq_pow_counts (s : R) (ks : List InterfaceKind) :
    closedFormProduct s ks
      = fPP s ^ ks.count .pp * fNN s ^ ks.count .nn
          * fPN s ^ ks.count .pn := by
  induction ks with
  | nil => simp [closedFormProduct]
  | cons k rest ih =>
    have hstep : closedFormProduct s (k :: rest)
        = interfaceFactor s k * closedFormProduct s rest := by
      simp [closedFormProduct]
    cases k <;>
      simp only [hstep, ih, interfaceFactor, List.count_cons] <;>
      simp <;>
      ring

/-- Canonical interface list of the `p^Z n^N` ordering
(`closed_form_tau_M.canonical_interface_kinds`, bring_color_weighted
labels): `Z−1` p-p bonds, then one p-n bond (when both species are
present), then `N−1` n-n bonds. Nat subtraction handles the `Z = 0` /
`N = 0` edge cases exactly as the Python (`A < 2 → []`). -/
def canonicalInterfaceKinds (Z N : ℕ) : List InterfaceKind :=
  List.replicate (Z - 1) .pp
    ++ (if 0 < Z ∧ 0 < N then [.pn] else [])
    ++ List.replicate (N - 1) .nn

/-- **Canonical closed form** for an atom with `Z ≥ 1` protons and `N ≥ 1`
neutrons:

  `tr_M(𝓑_K) = τ_p^Z · τ_n^N · f_pp^{Z−1} · f_nn^{N−1} · f_pn`. -/
theorem closedFormTauM_canonical (s tauP tauN : R) (Z N : ℕ)
    (hZ : 0 < Z) (hN : 0 < N) :
    closedFormTauM s tauP tauN Z N (canonicalInterfaceKinds Z N)
      = tauP ^ Z * tauN ^ N
          * (fPP s ^ (Z - 1) * fNN s ^ (N - 1) * fPN s) := by
  unfold closedFormTauM canonicalInterfaceKinds closedFormProduct
  rw [if_pos ⟨hZ, hN⟩]
  simp only [List.map_append, List.prod_append, List.map_replicate,
    List.prod_replicate, List.map_cons, List.map_nil, List.prod_cons,
    List.prod_nil, interfaceFactor]
  ring

/-- **Deuteron instance** (`Z = N = 1`, the `H₆` anchor of the exact-ℚ
verification): `tr_M(𝓑_D) = τ_p · τ_n · f_pn`. -/
theorem closedFormTauM_deuteron (s tauP tauN : R) :
    closedFormTauM s tauP tauN 1 1 (canonicalInterfaceKinds 1 1)
      = tauP * tauN * fPN s := by
  have h := closedFormTauM_canonical s tauP tauN 1 1 one_pos one_pos
  simpa using h

/-! ## §7. Trace bridge: interface factors as Markov-trace bond expectations -/

/-- Constant coefficient `d_k` of the bridge crossing `σ + d_k·1` realising
interface kind `k` (p-p: `0`; n-n: `−h`; p-n: `−h·(1/2 − δ/4)`) — the
`(c, d)` data of `MarkovBondFactor.lean` with `c = 1` throughout. -/
def bondD (s : R) : InterfaceKind → R
  | .pp => 0
  | .nn => - heckeH s
  | .pn => - (heckeH s * (1 / 2 - flavorDelta s / 4))

/-- Each interface factor is the conditional expectation `z + d_k` of its
bridge crossing. -/
theorem interfaceFactor_eq_bond_expectation (s : R) (k : InterfaceKind) :
    interfaceFactor s k = markovZ s + bondD s k := by
  cases k <;>
    simp only [interfaceFactor, bondD, fPP, fNN, fPN] <;>
    ring

section TraceBridge

variable {n : ℕ} {q : R} {A : Type u}
  [Ring A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]
  [MT : MarkovTrace n q A]

/-- **Trace bridge**: when the Markov trace's `z_param` is the closed form's
`markovZ s`, the trace of the bridge crossing `σ_i + d_k·1` is exactly the
interface factor `f_k(q)` — connecting the Phase-5q factors to the
`QOU.Hecke.MarkovTrace` class (single-bond case; the two-bond case follows
from `trace_bond_pair_factorizes`, and the general `A`-bond factorization
awaits the cross-level Markov axiom, per the module docstring). -/
theorem trace_interface_bond (s : R) (hz : MT.z_param = markovZ s)
    (i : Generator n) (k : InterfaceKind) :
    MT.trace (HA.embed i + bondD s k • (1 : A)) = interfaceFactor s k := by
  rw [map_add, map_smul, MT.trace_gen, MT.normalised, smul_eq_mul, mul_one,
    hz, interfaceFactor_eq_bond_expectation]

end TraceBridge

end QOU.Hecke.ClosedForm
