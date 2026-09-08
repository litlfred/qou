---
# qou-tv6l
title: Sweep the withdrawn Q_beta simple-pole evidence out of 8 durable artifacts
status: todo
type: task
priority: normal
created_at: 2026-08-23T22:22:28Z
updated_at: 2026-09-08T08:47:48Z
---

qou-8ofm / qou-frch (2026-08-10) established that the SDP c_k extractor emitted the model's accuracy floor as data, and that R(q0) being a single scalar means at most ONE rung is determinable. Both fixed the producer; neither swept the consumers. PR #1727's simple-pole verdict was read off k=8,9,10, which are deep in the stalled range, so all three cited signatures (flat c_k*u^k, ratio test -> 1/u, branch-fit beta=0.999) are the same arithmetic identity, and residue A = 1.804e-15 is the floor rescaled by u_subst. Measured against the extractor's own quotients: |c_k u^k| = floor to 1e-21, ratio -> 1/u to 2.4e-15. Audit: docs/audits/2026-08-23-qbeta-simple-pole-evidence-is-the-residual-floor.md. NOT refuted: the pole's existence (independent support in PR #1713 radius-of-convergence and PR #2454 algebraic Q_A(silver)=0). Withdrawn: that this evidence establishes the pole TYPE or its RESIDUE. The Lean is a 3b-cond conditional class and is unaffected; only its docstring's empirical justification is. Artifacts to sweep: q-beta-radius-of-convergence-gate.lean:11 docstring; docs/coordination/1ppq-qbeta.md (rows 2026-06-02 / 06-03 / 06-22, dead-ends table, open-target table); the 2026-06-02 originating audit; 2026-06-04 residue-a-unblock-kernel-scope; 2026-06-04 precision-ceiling plan+verdict; 2026-06-04 residue-a-followup plan+verdict; 2026-06-04 mixed-chains-plan; 2026-06-22 two-pole-ladder. Not done unilaterally: the rewrite is opinionated and spans a coordination ledger.

SHARPENED by the convention finding: PR #1727's floor f = 2.118e-13 was the muon + convention-C floor, so the simple-pole evidence is C-frame as well as floor-derived. The floor IDENTITY is arithmetic and frame-independent; only the floor's magnitude is frame-dependent. That is a second, independent reason the eight downstream artifacts cannot be quoted as they stand, and it means the sweep should scope them to C rather than merely annotate the floor issue.


## 2026-09-08 — ZERO of the 8 artifacts had been swept. One is now scoped; seven are the owner's.

Pulled off the `qou-bstl` completion-candidate queue, flagged by `d5eeff99c5a`
("the Q_beta simple-pole evidence is the residual-floor identity"). That commit
landed the AUDIT — the artifact this bean cites as already existing — not the
sweep. False positive.

But re-measuring it turned up something worse than "partial": **the sweep is
0 of 8, sixteen days after the finding landed.**

  * `q-beta-radius-of-convergence-gate.lean` still opened with the four
    withdrawn signatures quoted verbatim as establishing the pole —
    `c_k·u_subst^k -> 2.118e-13 for k = 8,9,10 (0.02% spread)`,
    `branch-fit beta = 0.999`, `cross-anchor shift = 210 ppb` — with no
    scoping note anywhere in the file.
  * `docs/coordination/1ppq-qbeta.md` has **zero** matches for
    `residual-floor`, `residual floor`, `floor identity`, or the audit's
    filename. The ledger does not know the finding exists.

**Note the shape.** This bean opens by describing `qou-8ofm` / `qou-frch` as
"Both fixed the producer; neither swept the consumers." That is exactly what
then happened to this bean: the audit was written, the consumers were not
touched, and the bean recording the recurrence recurred. The audit doc even
quotes the retraction's own warning — *"Prose caveats do not stop downstream
consumption"* — and then went unconsumed for sixteen days.

### What I did, and why only this much

Scoped **one** artifact: the Lean docstring. Under the 2026-09-07 ask-first
directive this qualifies under exemption 2 (derived from the corpus) — the
audit `docs/audits/2026-08-23-qbeta-simple-pole-evidence-is-the-residual-floor.md`
fixes the answer, and a reviewer checks my banner against that file rather than
against my reasoning. The withdrawn text is **struck-in-place, not deleted**,
per this corpus's own convention for a superseded claim.

The banner says exactly what the audit says and no more: the pole is NOT
refuted, the *evidence for its type and residue* is withdrawn, the three
"independent" signatures are one arithmetic identity, the residue is the floor
rescaled, and the floor's magnitude (not the identity) is convention-C and
muon-pinned. Independent support for the pole's existence — PR #1713, PR #2454
— is named as surviving. Two in-file pointers added at `u_substrate` and at
`RadiusOfConvergenceGateClass` so a reader landing mid-file meets the banner;
both say the class is a §3b-cond hypothesis and unaffected, which is this
bean's own position.

Verified: `lean -DautoImplicit=false -s 65536` **exit 0** (66 s, restored olean
cache, real import cone). No proof, statement, constant or number changed.

### The seven that remain are NOT mine, and this bean already said so

*"Not done unilaterally: the rewrite is opinionated and spans a coordination
ledger."* That still holds for the ledger rows, the six audit docs, and any
re-characterisation of what PR #1727 concluded — none of those are fixed by a
corpus artifact in the way one docstring's withdrawn quotation is. Remaining:

    docs/coordination/1ppq-qbeta.md   rows 2026-06-02 / 06-03 / 06-22,
                                      dead-ends table, open-target table
    docs/audits/2026-06-02  the originating audit
    docs/audits/2026-06-04  residue-a-unblock-kernel-scope
    docs/audits/2026-06-04  precision-ceiling plan + verdict
    docs/audits/2026-06-04  residue-a-followup plan + verdict
    docs/audits/2026-06-04  mixed-chains-plan
    docs/audits/2026-06-22  two-pole-ladder

Bean stays `todo`.
