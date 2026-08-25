---
# qou-24m2
title: 'GAP (detector): lean-self-assuming-audit.py misses the CLASS-INSTANCE self-assuming variant - the exact pattern AGENTS.md 3b-cond rule 5 names. DeltaLambdaSignRule.burnside was ''class C where claim : <conclusion>'' + ''theorem burnside [ctx : C] ... := ctx.claim ...'' and the detector scored 0 candidates on it. Two independent causes: (1) BINDER regex only matches round-bracket ''(h : T)'', so instance-implicit ''[ctx : C]'' never enters the binder map; (2) the bare-identifier guard re.fullmatch(''[A-Za-z_][A-Za-z0-9_]*'', proof) rejects a projection APPLICATION like ''ctx.claim n ps hc hn''. Fix: also parse ''[name : Type]'' binders, and match proofs of the form ''<binder>.<field> <args>'' where the class field''s declared type equals the conclusion. Cross-ref PR #4695 (8 P->P theorems), PR #4712 (triviality sweep), bean qou-q407, qou-z3k1.'
status: todo
type: task
created_at: 2026-08-08T00:15:05Z
updated_at: 2026-08-08T00:15:05Z
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
