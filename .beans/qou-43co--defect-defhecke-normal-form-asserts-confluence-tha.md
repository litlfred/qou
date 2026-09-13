---
# qou-43co
title: 'DEFECT: def:hecke-normal-form asserts confluence that QOU''s own Lean refutes at n=4'
status: todo
type: bug
priority: high
created_at: 2026-08-09T18:27:58Z
updated_at: 2026-09-13T12:38:53Z
---

`content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md` says of
the three-rule system (Hecke relation, far commutativity, Yang-Baxter in the
shortlex-decreasing direction):

> This reduction is confluent, making the normal form independent of rule order.

That is exactly the system `heckeRewritingSystem` in
`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean`, and
`NotAGSBasis.hecke_not_gs_basis_four` in that file is a machine-checked
REFUTATION at n = 4: the overlap of the Yang-Baxter rule for (sigma_2, sigma_3)
(lm = s3 s2 s3) with the far-commutation rule for (sigma_3, sigma_1)
(lm = s3 s1) over the word s3 s2 s3 s1 has S-polynomial

    s2 s3 s2 s1 - s3 s2 s1 s3

and both words are irreducible for the system, so the S-polynomial is a nonzero
normal form and the system is not confluent. The Lean module header states this
outright and records that the axiom `hecke_is_gs_basis` was deleted for being
false, not merely unproved.

So the manuscript block asserts, uncited, precisely what the folio's own
sorry-free Lean disproves. Fix the block, do not just add a citation.

WHAT THE REPAIR NEEDS (all three sources agree on the shape):
- HeckeGS.lean:461 names the missing family itself:
  sigma_i sigma_{i-1} ... sigma_j sigma_i -> sigma_{i-1} sigma_i sigma_{i-1} ... sigma_j,
  of which s3 s2 s1 s3 -> s2 s3 s2 s1 is the first instance. That is the
  Bokut-Shiao completion, now citable as [bokut2001].
- [kimlee2018] Prop. 3.1 shows the same shape on the Temperley-Lieb quotient:
  the GS basis needs the two extra families E_{i,j}E_i - E_{i-2,j}E_i (i > j)
  and E_j E_{i,j} - E_j E_{i,j+2} (i > j) beyond the defining relations.
- The q-deformed type-A statement itself is Kang-Lee-Lee-Oh 2002 (see the
  sibling bean); [bokut2001] is a Coxeter-GROUP theorem and does not by itself
  license the H_n(q) claim.

Two acceptable outcomes: (a) restate the block over the COMPLETED rewriting
system and cite the completion; or (b) drop the confluence sentence and say the
normal form is defined by a fixed rule order, with a pointer to
`NotAGSBasis.hecke_not_gs_basis_four` for why order-independence fails. Either
way `def:hecke-normal-form` currently has no `cites` field at all and carries
the `groebner-shirshov` tag.

Surfaced by relevance triage of the nine-PDF batch (library/fd58d8e1...pdf and
library/arxiv-1808.05026v1/1808.05026v1.pdf); ledger rows carry the join.


## Re-measured 2026-09-13 on main `9fb403c42` — LIVE, not stale, and there is a THIRD defect

This bean is from 2026-08-09. Checked rather than assumed, because a month-old
bean in this corpus is as likely to be drained as live. All three of its claims
hold, and the block has one more problem it does not name.

### 1. The false claim is still there

`content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md:6`:

> This reduction is confluent, making the normal form independent of rule order.

### 2. The refutation is still there, and is SORRY-FREE

`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean`:

| decl | line | kind |
|---|---|---|
| `NotAGSBasis.hecke_not_gs_basis_four` | 651 | `theorem` — `¬ IsGrobnerShirshovBasis … (heckeRewritingSystem 4 …)` |
| `hecke_is_gs_basis_false` | 671 | `theorem` — the former axiom is false, by the above |

`grep -c sorry` over that file returns **1**, and that one occurrence is inside a
docstring reading *"with no hypothesis and no `sorry`"*. So both are genuine,
unconditional refutations, not `sorry`-carrying statements.

### 3. The two objects ARE the same object — checked, not assumed

AGENTS.md §"Grep the claim SHAPE, not only the topic" exists because this step
gets skipped. The `.md`'s three rules against `heckeRewritingSystem` (line 169):

| `.md` | Lean |
|---|---|
| 1. `σᵢ² → (q − q⁻¹)σᵢ + 1` | `heckeRelation i hp`, `lm = [i,i]` (line 229) |
| 2. `σᵢσⱼ → σⱼσᵢ`, `\|i−j\| ≥ 2` | `farCommRelation i j` for `i > j+1`, `lm = [i,j]` (line 254) |
| 3. Yang–Baxter | `yangBaxterRelation i j` for `j = i+1`, `lm = [j,i,j]` (line 242) |

Same three rules, same system. So the bean's identification is correct.

### 4. 🛑 NEW — the Yang–Baxter arrow in the `.md` points the WRONG WAY

Not in this bean, and independent of the confluence claim. Line 4 reads

> 3. Yang--Baxter: $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$ (in the shortlex-decreasing direction).

The LHS `σᵢ σᵢ₊₁ σᵢ` is shortlex **smaller** than the RHS `σᵢ₊₁ σᵢ σᵢ₊₁` (equal
length, and `i < i+1` at the first letter). So the arrow as written reduces the
smaller word to the larger — **increasing**, which is the opposite of what its
own parenthetical claims, and it would not terminate.

The Lean has it right: `yb_lm` (line 513) proves `lm = [⟨3⟩,⟨2⟩,⟨3⟩]`, i.e. the
rule reduces `σᵢ₊₁ σᵢ σᵢ₊₁ → σᵢ σᵢ₊₁ σᵢ`. The parenthetical describes the Lean's
actual direction; the arrow contradicts both.

So the sentence is self-contradictory in isolation, which means it can be fixed
without settling the confluence question — a **separable**, uncontroversial repair.

Rule 2 has a milder version of the same gap: the `.md` gives no orientation at
all, while the Lean fixes `i > j`. Without an orientation, rule 2 is symmetric
and the system trivially fails to terminate.

### 5. Still no `cites`

Confirmed: `hecke-normal-form.ts` has no `cites` field.

### Not acted on — this is a math-content change and needs author consent

Per the standing rule for this repo, a change to a mathematical claim in a
content block is not an agent's call. The bean's own options (a) restate over the
COMPLETED system and cite the completion, or (b) drop the confluence sentence and
say the normal form is fixed by rule order, remain the decision. Defect 4 is the
one piece that is arguably mechanical (the block contradicts itself), but it sits
in the same three lines, so it is being put to the author together rather than
patched underneath a live question.
