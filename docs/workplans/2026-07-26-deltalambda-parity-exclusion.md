# Work-plan — Δ_λ parity exclusion (Route 2, first step)

**Branch:** `claude/deltalambda-parity-exclusion-2026-07-26` · **Axis:** Δ_λ binding — μ₀ −9% closure ·
**Builds on:** #4387 (deuteron bar-parity = signed H₆ partition-conjugation parity; self-conjugate
`(3,2,1)` bar-odd). **Discipline:** formalize-first, no fit, scope-labelled; nothing wired.

## The idea

My #4387 parity finding gives the channel decomposition of the deuteron binding
`B = m_e Σ_{λ⊢6} w_λ χ^λ Δ_λ`:

- bar-even `g₂` ← conjugate-pair **asymmetries** `Δ_λ − Δ_{λ'}` (vanish on the self-conjugate);
- bar-odd `t` ← pair-**symmetric** parts + the self-conjugate `(3,2,1)`.

**Immediate consequence (the exclusion):** any **conjugation-symmetric** dressing `Δ_λ = Δ_{λ'}` gives
`g₂ = 0`. Since `g₂ ≈ 1 ≠ 0`, **no conjugation-symmetric `Δ_λ` can produce the deuteron's bar-even
binding.** This is a scope-**(b)** structural exclusion (proved invariant: conjugation symmetry ⇒
zero bar-even), complementing the KL-positivity prune.

**Verified (30 dps):** the Markov weight `w_λ`, classical `dim(λ)²`, and the hook-form q-dimension are
all conjugation-symmetric → all excluded as `Δ_λ`. The conjugation-**covariant** Wenzl principal
specialization `s_λ(1,q,…,q^{n-1})` is *not* symmetric → **not** excluded — which independently
selects exactly the weight the s5-so3 keystone identified as the production weight. Convergence, not
fishing.

## Steps (microcommits)

1. **[this commit]** work-plan.
2. **Lean** `ConjugationSymmetricDeltaExcluded.lean` — over `Fintype I` + involution `c`: the reindex
   lemma `Σ T_{cλ}Δ_λ = Σ T_λ Δ_{cλ}` and the exclusion `Δ∘c = Δ ⇒ bar-even total = 0`. Sorry-free.
3. **Probe** — classify candidate `Δ_λ` families by conjugation symmetry (excluded vs surviving);
   verify the bar-even total vanishes for a symmetric `Δ`; confirm the principal specialization is
   asymmetric (survives). 25–30 dps, no fit.
4. **Audit doc** — state the scope-(b) exclusion, the surviving class (covariant / principal
   specialization), and the convergence with the keystone.

## Scope

DERIVED: a structural exclusion narrowing the `Δ_λ` search (symmetric families out; covariant class
in). NOT derived: the `Δ_λ` magnitudes themselves (still the Track-A gate). No fit; nothing wired.
