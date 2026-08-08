---
# qou-24m2
title: 'GAP (detector): lean-self-assuming-audit.py misses the CLASS-INSTANCE self-assuming variant - the exact pattern AGENTS.md 3b-cond rule 5 names. DeltaLambdaSignRule.burnside was ''class C where claim : <conclusion>'' + ''theorem burnside [ctx : C] ... := ctx.claim ...'' and the detector scored 0 candidates on it. Two independent causes: (1) BINDER regex only matches round-bracket ''(h : T)'', so instance-implicit ''[ctx : C]'' never enters the binder map; (2) the bare-identifier guard re.fullmatch(''[A-Za-z_][A-Za-z0-9_]*'', proof) rejects a projection APPLICATION like ''ctx.claim n ps hc hn''. Fix: also parse ''[name : Type]'' binders, and match proofs of the form ''<binder>.<field> <args>'' where the class field''s declared type equals the conclusion. Cross-ref PR #4695 (8 P->P theorems), PR #4712 (triviality sweep), bean qou-q407, qou-z3k1.'
status: todo
type: task
created_at: 2026-08-08T00:15:05Z
updated_at: 2026-08-08T00:15:05Z
---

