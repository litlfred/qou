---
name: lean-substantive-pass
roles: [collaborator, owner]
user_invocable: true
description: >
  Convert abstract `holds : Prop` / `claim : Prop` placeholder Lean
  stubs into typed sub-claim contexts with manuscript-semantic
  field names. Three escalation levels: hand-craft per-block
  (highest fidelity), bulk-script with `.work/bulk-split-holds.py`
  (split on numbered sub-claims), and docstring enrichment with
  `.work/enrich-subclaim-docstrings.py` (extract first-sentence
  summaries from .md). Use this skill after `local/lean-generation`
  has created the placeholder stubs and the backlog is structurally
  closed.
allowed-tools: Read Edit Write Bash Grep Glob Skill
---

# /lean-substantive-pass

The job of this skill is to take an abstract `class FooContext where
... holds : Prop` placeholder and turn it into a typed sub-claim
context. Three levels of fidelity, escalating:

```
Level 1 (hand-crafted, ~5-30 min/block)
  └── typed Real/Nat fields + named sub-claims with full manuscript context
Level 2 (bulk-script split, ~seconds/block)
  └── numbered claim_i, claim_ii, ..., claim_N : Prop (count from .md numbered list)
Level 3 (docstring enrichment, ~seconds/block)
  └── /-- Manuscript sub-claim (i) — <first-sentence-from-md>. -/
```

## 0. When to invoke

- After `local/lean-generation` has populated `.lean` stubs with
  `holds : Prop` placeholders (the "backlog closure" pass).
- Before `local/lean-completeness-audit` reports trivial-skeleton
  status — typed sub-claims downgrade the audit verdict from
  "structural placeholder" to "named structural placeholder".
- After resolving a `.md` block's `uses[]` cone (so the manuscript
  content is stable enough to encode as Lean types).

## 1. Recognised manuscript patterns

The pass works because manuscript propositions follow consistent
shapes. Recognise these and apply the matching Lean encoding:

| Pattern in .md | Lean encoding |
|----------------|---------------|
| `$\boxed{lhs = rhs}$` or `$\boxed{lhs \leq rhs}$` | `claim_boxed_identity : lhs = rhs` with `lhs, rhs : ℝ` abstract fields |
| `1. ... 2. ... 3. ...` numbered list | `claim_i, claim_ii, claim_iii : Prop` (split into N) |
| `\begin{cases} ... \end{cases}` piecewise | conditional sub-claims `cond_i → result_i = ...` |
| "is an equivalence relation" with refl/sym/trans | three sub-claims; theorem proves `Equivalence ctx.rel` |
| Table of moves (R1/R2/R3/Markov-I/II) | one `claim_<move_name>` Prop per row |
| "exists and is unique" | `claim_existence : ∃ x, P x` + `claim_uniqueness : ∀ x y, P x → P y → x = y` |
| Numerical formula `Q = ... × m_e × ...` | typed `claim_formula : Q = ... * m_e * ...` |
| Polynomial recurrence `a_{n+2} = X · a_{n+1} + a_n` | `noncomputable def + theorem ... : rfl` |
| Matrix identity `T_pp · T_nn = I` | entry-level equalities `entry_00 = 1 ∧ entry_11 = 1` |

## 2. Type-field heuristics

When a block uses standard QOU vocabulary, declare these fields:

| Manuscript word | Lean field |
|-----------------|-----------|
| substrate parameter `q` | `q : ℝ` (+ `q_gt_one : 1 < q` when needed) |
| Hecke parameter `h = q − q⁻¹` | `h : ℝ` + `h_eq : h = q - q⁻¹` |
| proton count `Z` | `Z : ℕ` |
| neutron count `N` | `N : ℕ` |
| mass number `A = Z + N` | `A : ℕ` + `A_eq : A = Z + N` |
| electron mass `m_e` | `m_e : ℝ` (CODATA input) |
| categorical object `A` | `CategoricalObj : Type` |
| Hecke algebra `H_n(q)` | `HeckeAlgebra : Type` or `HeckeAlgebra : ℕ → Type` |
| partition `λ ⊢ n` | `PartitionIdx : Type` |
| braid representative | `Braid : Type` |
| LP shadow price | `shadow_price : ℝ` or named per channel |
| classical Plancherel | `w_λ : PartitionIdx → ℝ` |
| q-deformed Wedderburn | `w_tilde : PartitionIdx → ℝ` |

Per AGENTS.md §7c (archimedean wall), keep types generic unless the
specific construction requires `ℝ`. `Matrix R d₁ d₂`,
`Polynomial R`, `Finset.sum` are all generic-typeclass-friendly.

## 3. Workflow

### Step 3.1 — Survey

```bash
# Count remaining placeholders by chapter
grep -lr "^  holds : Prop\|^  claim : Prop\|^  claim_i : Prop" \
  content/quantum-observable-universe/lean/QOU/ 2>/dev/null \
  | awk -F'/QOU/' '{print $2}' | awk -F/ '{print $1}' \
  | sort | uniq -c | sort -rn
```

Pick the largest chapter; commit to finishing it before moving on.

### Step 3.2 — Bulk-split (Level 2)

Run the bulk-split script first to convert single `holds : Prop`
into `claim_i, claim_ii, ..., claim_N : Prop` based on numbered
sub-claims in the .md:

```bash
python3 .work/bulk-split-holds.py
```

Output: split count + rename count. Both are mechanical.

### Step 3.3 — Docstring enrichment (Level 3)

Run the enrichment script to add first-sentence-from-md summaries
to each generic sub-claim docstring:

```bash
python3 .work/enrich-subclaim-docstrings.py
```

After this, every `claim_i, claim_ii, ...` carries a manuscript-
fragment summary in its docstring — enough for downstream readers
to know what each sub-claim asserts.

### Step 3.4 — Hand-craft (Level 1)

For high-value blocks (mass formulas, predicted observables,
foundational propositions), hand-craft each sub-claim with:

1. Read `.md` to identify the structural pattern (table 1 above).
2. Read `.lean` to see current placeholder fields.
3. Apply the matching Lean encoding (table 1) and type fields
   (table 2).
4. Re-state the theorem as a conjunction (or `Equivalence`,
   `∀ k`, etc.) that proves directly from the named sub-claim
   fields by `⟨...⟩` constructor.
5. The body remains `sorry`-free **only** when every sub-claim is
   a class hypothesis (no need to discharge); else stays `sorry`.

Example: see Descartes batch 1 commit `014132c8d` and BraidKnot
batch 2 commit `f13953512` for hand-crafted patterns.

## 4. Patterns that emerged in practice

These are anti-patterns to **avoid**:

- **Don't rename `holds` → `claim` without checking the .md.** If
  the .md has numbered sub-claims, split into `claim_i, claim_ii,
  ...` instead.
- **Don't use generic `claim_i, claim_ii, ...` names when the
  manuscript has clear semantic identifiers.** Use names like
  `claim_i_spectral_decomposition`, `claim_ii_pair_production`,
  etc.
- **Don't introduce `Finset.univ.sum` / `Finset.univ.prod` without
  importing** `Mathlib.Algebra.BigOperators.Group.Finset.Defs`.
- **Don't use `q := ...` named-argument syntax inside class
  field types** — it's only valid in term-mode binders. Use a
  named field `s : ℝ` with `s_eq : s = q - q⁻¹` instead.
- **Don't break the four-claim conjunction with `refine ⟨..., ?_⟩`
  if the entire conjunction can be discharged constructively.**
  Use `⟨ctx.claim_i, ctx.claim_ii, ...⟩` directly when every
  sub-claim is a context field.

## 5. Sub-skills delegated

- `local/lean-generation` — populates stubs initially.
- `local/lean-build-fix` — fixes any compilation errors from the
  typed sub-claim encoding (missing imports, syntax errors).
- `local/lean-completeness-audit` — measures coverage afterwards.
- `local/proof-conciseness` — tightens the final theorem proofs
  once they're typed.

## 6. Author-ask templates

For ambiguous block-level shape choice:

> Block `<label>` has manuscript text with both a boxed identity
> (`B = ... × m_e × ...`) and three sub-bullets. Should the Lean
> encoding be: 1) single `claim_boxed_identity` typed `=`,
> 2) split into `claim_i_xxx, claim_ii_yyy, claim_iii_zzz`,
> 3) both (boxed identity + sub-bullets each as their own field)?

For unrecognised structural patterns:

> Block `<label>` has narrative text describing `<concept>` but no
> recognisable boxed identity / numbered list / table / cases.
> Should I: 1) keep single `claim : Prop`, 2) hand-craft typed
> fields based on my reading of the manuscript intent, 3) defer
> until you provide a structural template?

## 7. Output

End the run with:

- Coverage summary (chapter X: K/N blocks hand-crafted,
  M/N split, 0 single-Prop remaining).
- Any queued author questions (in `.work/author-questions.md`).
- Pointer to the modified `.lean` files for review.
