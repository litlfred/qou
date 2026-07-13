# Keystone C8: the super-exponential growth is PROVED modulo two SYT identities (exact identity + Cauchy–Schwarz)

> **Scope up front.** "PROVED" here means the *arithmetic core* — Cauchy–Schwarz,
> the involution-number bound, and the reduction (A)+(B)+(C) ⇒ super-exp — is
> Lean-proved sorry-free. Two Standard-Young-Tableau-dependent inputs remain
> **carried hypotheses**: (A) the branching identity `Σ f^λ f^{λ/(2,1)} = k!/3`
> and (C) the skew↪straight bound `Σ f^{λ/(2,1)} ≤ I(k)`. See the "proved vs
> carried" table below; both need `StandardYoungTableau`, which Mathlib lacks.

**Date:** 2026-07-11 · **Axis:** s5-so3-keystone (geometric `W_λ`) + GAP-A-3 ·
**Owner steer:** "open s5-so3 gate" (the gate is owner-reversed for the geometric
`W_λ` construction; this discharges the C8 Lean target). **No fit; no closure.**
**Compute:** [`computations/keystone_c8_superexp_proof.py`](../../computations/keystone_c8_superexp_proof.py) ·
**Lean:** [`QOU/BraidKnot/KeystoneC8SuperExpBound.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneC8SuperExpBound.lean)

## What this upgrades

Necessary condition **C8**
([2026-07-11-keystone-wlambda-superexp-necessary-condition](2026-07-11-keystone-wlambda-superexp-necessary-condition.md))
required the Plancherel-weighted branched sum

    w_std(k) = (1/k!) Σ_{λ⊢k} (f^λ)² · f^{λ/(2,1)}  =  E_Planch[f^{λ/(2,1)}]

to grow **super-exponentially**, and flagged the Lean target as *"a super-exponential
lower bound on `E_Planch[f^{λ/(2,1)}]` — a self-contained combinatorial lemma."* This
note supplies a **rigorous proof** of that lower bound (previously only verified
`k≤10`).

## The proof (three steps)

1. **Exact identity (A):** `S1(k) := Σ_{λ⊢k} f^λ f^{λ/(2,1)} = k!/3`. The classical
   branching identity `Σ_λ f^λ f^{λ/μ} = k!·f^μ/|μ|!` with `μ=(2,1)` (`f^μ=2`,
   `|μ|!=6`) gives `k!·2/6 = k!/3`. Exact, verified `k=3..12` (`k!/3`: 2, 8, 40, 240,
   1680, 13440, …).
2. **Cauchy–Schwarz (B):** with weights `g_λ = f^{λ/(2,1)} ≥ 0`,
   `(Σ f^λ g_λ)² ≤ (Σ (f^λ)² g_λ)(Σ g_λ)` ⇒ `(k!/3)² ≤ (k!·w_std)·Σ g_λ`.
3. **Skew ↪ straight (C):** `Σ_{λ⊢k} f^{λ/(2,1)} ≤ Σ_{λ⊢k} f^λ = I(k)` (a skew SYT
   of `λ/(2,1)` injects into a straight SYT of `λ` by prepending a fixed `(2,1)`-SYT;
   `Σ_λ f^λ = I(k)` is the involution/telephone number — the `q=1` value of the QOU
   na-Stokes period `S(n) = Σ_λ dim_q(λ)`).

Combining: **`w_std(k) ≥ k!/(9·I(k))`**, and `k!/I(k)` is super-exponential
(`I(k) ~ (k/e)^{k/2} e^{√k−1/4}/√2` while `k! ~ (k/e)^k √(2πk)` ⇒ `k!/I(k) ~
(k/e)^{k/2}·poly`). The bound is tight to within a small constant (at `k=10`:
`w_std=159.7`, `k!/(9·Σf^{λ/(2,1)})=130.6`, `k!/(9·I(k))=42.5`). ∎ (super-exp class)

## What is Lean-proved vs carried (the "Young-tableau infra" honesty)

Mathlib has `YoungDiagram` and `SemistandardTableau` but **no** `StandardYoungTableau`,
hook-length formula, or `f^λ`. So the file proves everything *except* the two
SYT-dimension identities:

| Ingredient | Status in Lean |
|---|---|
| Cauchy–Schwarz (B) | **proved** (`weighted_cs`, from Mathlib `sum_mul_sq_le_sq_mul_sq` via `Real.sqrt`) |
| Involution numbers `I(k)` | **concrete** (`involutionNumber` recurrence) + `involution_le_factorial : I n ≤ n!` proved |
| Arithmetic reduction (A)+(B)+(C) ⇒ bound | **proved** (`c8_lower_bound`, sorry-free) |
| (A) `Σ f^λ f^{λ/(2,1)} = k!/3` | **carried hypothesis** — needs `StandardYoungTableau` |
| (C) `Σ f^{λ/(2,1)} ≤ I(k)` | **carried hypothesis** — needs `StandardYoungTableau` |

The two carried inputs are the *minimal irreducible* SYT-dependent facts — the same
`StandardYoungTableau` + hook-length infrastructure the keystone's **Identity I**
needs ([`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) line 40 / #2634).
Building that in Mathlib would discharge (A)/(C) too; that is the open fill (shared
with Identity I, so it is *one* infra fill serving both).

## Tier-1 fix: the `StandardYoungTableau` type Mathlib lacks now exists in-tree

[`QOU/BraidKnot/YoungTableauStandard.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/YoungTableauStandard.lean)
supplies the missing infrastructure (bean `08a2`, Tier 1), turning the two
**carried `f g : ℝ` hypotheses** above into **stated propositions about real SYT
counts** — the honest §1a "queue it" disposition, not opaque parameters:

| Declaration | Status |
|---|---|
| `StandardYoungTableau μ` / `SkewStandardYoungTableau outer inner` | **new structures** — fillings by `{0,…,\|μ\|−1}`, row/col-strict (the type Mathlib has for SSYT but not SYT) |
| `fDim μ = Nat.card (StandardYoungTableau μ)` = `f^μ`; `fDimSkew` = `f^{λ/μ}` | **defined** |
| `entry_lt_card` (every entry `< \|μ\|`) | **proved** — genuine non-vacuity, from the `content` field |
| `involutionNumber_pos` (`I(n) ≥ 1`) | **proved** (two-step induction + `omega`) |
| `c8_superexp` (unconditional `k!/(9·I(k)) ≤ (Σ (f^λ)² f^{λ/(2,1)})/k!`, `k ≥ 3`) | **proved** — all arithmetic/casts real; gaps only via the 3 RSK sorries it invokes |
| (A) `branching_two_one` (`3·Σ f^λ f^{λ/(2,1)} = k!`) | **`sorry` + `-- Ref:[sagan2001]`** (branching rule, Thm 3.10.2) |
| (C) `skew_le_straight` (`Σ f^{λ/(2,1)} ≤ Σ f^λ`) | **`sorry` + `-- Ref:[sagan2001]`** (§4) |
| `sum_fDim_eq_involution` (`Σ f^λ = I(k)`) | **`sorry` + `-- Ref:[sagan2001]`** (RSK for involutions, §3.1) |

lean-direct `EXIT=0`; the **only** three `sorry`s are the deep RSK-family
identities Mathlib cannot yet prove (no hook-length, no RSK). This is **not** a
closure: it builds the type + isolates and cites the remaining classical fill
(shared with Identity I). Restating (A) as `3·Σ = k!` avoids a lossy ℕ-division
cast; the `k ≥ 3` guard keeps the branching statement honest (`(2,1) ⊄ λ` for
`k < 3`).

## The μ/e ↔ binding cross-link (why the keystone carries it)

`I(k) = Σ_λ f^λ` is exactly the `q=1` value of the QOU na-Stokes **binding** period
`S(n) = Σ_λ dim_q(λ)` (the q-involution number,
[PR #3545](https://github.com/litlfred/qou/pull/3545) audit Part 1). So the C8
super-exp bound — a keystone (μ/e mass) necessary condition — is proved *through the
same involution-number combinatorics* that governs binding. A single geometric `W_λ`
must simultaneously meet the μ/e gates and this binding-side super-exp growth
(#3548), and that joint constraint is now a theorem modulo the two SYT identities.

## Scope (STRICT)

This **adds a proof of a necessary condition**; it does **not** construct the
geometric `W_λ`, set a scale, wire anything, or close the keystone. No fit. The
owner-gated open object (the colored Σ(2,3,5) WRT / `E_q(2)` q-series realizing
`W_λ`) is untouched — this only makes the C8 test it must pass a proved theorem
rather than a numerical observation.
