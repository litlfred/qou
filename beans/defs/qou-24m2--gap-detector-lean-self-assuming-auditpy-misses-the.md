---
# qou-24m2
title: 'GAP (detector): lean-self-assuming-audit.py misses the CLASS-INSTANCE self-assuming variant - the exact pattern AGENTS.md 3b-cond rule 5 names. DeltaLambdaSignRule.burnside was ''class C where claim : <conclusion>'' + ''theorem burnside [ctx : C] ... := ctx.claim ...'' and the detector scored 0 candidates on it. Two independent causes: (1) BINDER regex only matches round-bracket ''(h : T)'', so instance-implicit ''[ctx : C]'' never enters the binder map; (2) the bare-identifier guard re.fullmatch(''[A-Za-z_][A-Za-z0-9_]*'', proof) rejects a projection APPLICATION like ''ctx.claim n ps hc hn''. Fix: also parse ''[name : Type]'' binders, and match proofs of the form ''<binder>.<field> <args>'' where the class field''s declared type equals the conclusion. Cross-ref PR #4695 (8 P->P theorems), PR #4712 (triviality sweep), bean qou-q407, qou-z3k1.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T00:15:05Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-5p7n
---


## 2026-08-22 — FIXED, and a THIRD cause was found that this bean did not name
Both prescribed causes fixed in scripts/lean-self-assuming-audit.py:
 (1) binder parsing now covers `[name : T]` (BINDER_INST) and `{name : T}` (BINDER_IMPL), not just
     round brackets, so an `[ctx : C]` binder finally enters the binder map;
 (2) a projection APPLICATION `<binder>.<field> <args>` is now matched (PROJ_APP) and flagged when
     the class field's declared type equals the conclusion — reported as a distinct
     `variant: "class-field-is-conclusion"` so it is separable from the original bare-identifier rule.
Class field types are parsed per-file (parse_classes); CROSS-FILE classes are NOT resolved, which is
a remaining known limit, stated in the function docstring rather than left implicit.

THIRD cause, found while testing and not named in this bean: the conclusion was taken from the LAST
top-level `:`. Every binder colon is bracketed, so the only top-level colons are the conclusion
separator and any binder INSIDE the conclusion — e.g. `: forall ps : List Nat, P ps` made the
"conclusion" `List Nat, P ps`, which can never match anything. Taking the FIRST top-level colon is
correct for both rules. Without this the fix still reported 0 on the bean's own example shape: my
first fixture (which had a forall-conclusion, like the real `ctx.claim n ps hc hn` case) stayed
invisible until this was fixed. So the bean's two causes were necessary but not sufficient.

Verified: two fixtures, including negative controls — a class carrying a genuine HYPOTHESIS whose
theorem does real work (`Nat.le_of_lt ctx.positive`) and a projection whose field type differs from
the conclusion are both correctly NOT flagged (1 of 3 fixture theorems flagged). Corpus: 0 -> 5
candidates over 3031 files. Adjudication of those 5 is bean qou-sa5c; spot-check of one (LpDuality)
confirms a genuine, already-documented instance rather than noise.

## Round 88 Formalization (`litlfred/qou#8471`)
- Formalized in `QOU.Foundations.BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit` (`folio/quantum-observable-universe/lean/QOU/Foundations/BraidPlaceholderResweepArchimedeanMarkerPartitionConditionalEdgeCollisionBaseOrderPivotExtensionInstanceProjectionAudit.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`e47fb91c9186e83c35ba5f8afe823fc02682f7fa` -> `eb5a105f27408ec654ee82cac266aca18e9361f3`, `scriptHash = scriptSha256 = 76b0a54b7612529d0460197f1a503d128d9ca3acb85f7c16e201490dd4b263d6`).
- PR: https://github.com/litlfred/qou/pull/8471

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Measured: PR #8471 / #8474 / #8481 (2026-11-18, `QOU/Foundations/*` new files) do **not** resolve this bean. Each adds a standalone Lean file whose structures hold the bean's own audit counts as `Int` fields, with a `canonical…` def filling in the counts and theorems such as `x*x = 0 ↔ x = 0`. No corpus file named by this bean is touched, so the defect it tracks is unchanged by those PRs. Read from the PR patches; not merged.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.
