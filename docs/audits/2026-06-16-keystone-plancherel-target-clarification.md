# Keystone target clarification — `W_λ` is the q-Plancherel measure, NOT the production trace weight (2026-06-16)

**Branch:** `claude/keystone-plancherel-target-clarification-2026-06-16`
**Context:** the s5-so3 keystone ([`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md))
is reduced to one owner-gated problem: a Wu-manifold SU(3)/SO(3) Sasakian S¹-equivariant
index reproducing the Ocneanu weights `W_λ = d_q(λ)²/[n]_q!`. This note pins **exactly
which weight system** that is, to prevent a natural-but-wrong conflation.

## Finding

`W_λ = d_q(λ)²/[n]_q!` (the keystone target) is the **q-Plancherel measure**. It is
**not** the production Jones–Markov weight `y_λ` (the Wenzl *principal* Schur
specialization `s_λ(1,q,q²,…)`) that the nuclear-atom mass trace uses
([`docs/audits/2026-06-16-s5-s3-symmetry-review-and-suq3-trace-question.md`](2026-06-16-s5-s3-symmetry-review-and-suq3-trace-question.md)).
Verified at q₀, λ⊢5:

| λ⊢5 | `y_λ` (principal spec) | `W_λ = d_q²/[5]!` (Plancherel) |
|---|---|---|
| (5) | **0.11815** (peak) | 0.00762 |
| (4,1) | 0.10938 | 0.12862 |
| (3,2) | 0.06172 | 0.20754 |
| (3,1,1) | 0.01677 | **0.29467** (peak) |
| (2,2,1) | 0.00775 | 0.20754 |
| (2,1,1,1) | **−0.00093** (signed) | 0.12862 |
| (1⁵) | 0.00009 | 0.00762 |

The two weight systems are **distinct and not proportional**: `y_λ` is signed and
peaks at the one-row (5); `W_λ` is conjugation-symmetric (the Plancherel hallmark:
`W_λ = W_{λ'}`) and peaks at the middle block (3,1,1). They differ by up to ~15–40×.

## Why it matters

- **The geometric index must reproduce the q-Plancherel measure specifically** —
  `d_q(λ)²/[n]_q!`, the conjugation-symmetric measure for which the Markov trace is
  the symmetric/regular trace — *not* the principal-specialization weight used for
  nuclear masses. The two are different sectors (lepton tower n=5 Plancherel vs
  nuclear atom n=3A principal-spec), correctly weighted differently.
- **Do not bridge them.** A natural shortcut — "the keystone `W_λ` is the same as the
  production trace weight, already characterized" — is **false**. The keystone target
  stands alone.
- **Plancherel has its own geometric handle.** The conjugation symmetry `W_λ = W_{λ'}`
  and the `d_q²/[n]!` form (RSK / Plancherel growth) are a *more* structured target
  than a generic weight — the natural object for an equivariant-index/heat-kernel
  argument. This is a (modest) positive: the index problem is to reproduce the
  **q-Plancherel measure**, which is exactly the measure produced by the Schur–Weyl
  `V^{⊗n}` decomposition under the symmetric (dimension-squared) pairing.

## Coordination note

The ledger states the sibling A≥3 compute (#2369/#2371/#2372) "produces `W_λ`
algebraically." Those nuclear-atom computes use `y_λ` (principal spec), not the
Plancherel `W_λ` — different sector, different weight. Worth confirming with the
keystone author that the n=5 lepton weighting is the **Plancherel** `d_q²/[5]!`
(as the verifier `s5so3_ingredient4_markov_weighting_facts.py` uses) and not the
principal specialization, so the geometric target is unambiguous.

## Scope

Pure clarification (no production change). The keystone's open object — the Sasakian
equivariant index reproducing the q-Plancherel measure — remains owner-gated
differential geometry, unchanged by this note.
