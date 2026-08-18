---
# qou-5380
title: q0-anchor-consistency audit witness is stale by one count -- gswz_program_convention_immunity lacks a q0 anchor
status: todo
type: task
priority: normal
created_at: 2026-08-18T20:53:26Z
updated_at: 2026-08-18T20:54:17Z
---

Found by running the FULL `scripts/precision-gates.sh` (not `--changed`) on
2026-08-18. All blocking gates were green; the run flagged one stale committed
audit witness.

**The count really moved**, so this is genuine staleness, not provenance drift:

    computations/audits/q0-anchor-consistency-audit.witness.json
      Q0_ANCHOR_MISSING: 1891 -> 1892
      new entry: gswz_program_convention_immunity.witness.json  (detail: "")

That witness landed on main in `1cdeb043aa` (audit(epsm): convention-immunity of
the programme MEASURED). It carries no q0 anchor, so the audit's missing-count
is one higher than the committed copy records.

**NOT refreshed here, deliberately.** Regenerating in this container also
rewrites the environment block downward — sympy 1.12 -> 1.14.0 but
mpmath 1.4.1 -> 1.3.0, and clarabel 0.11.1 dropped entirely (not installed
here). Committing that would trade a one-count staleness for a worse
provenance record, and it would mix an unrelated audit refresh into a
probe-precision PR. Same reasoning a prior agent used on this exact witness
during the #4973 prepare-merge.

**For whoever takes it:** refresh in an environment with clarabel and
mpmath 1.4.1 present, so only the count moves. Then either give
gswz_program_convention_immunity a q0 anchor (if it should have one) or confirm
it is legitimately anchor-free and the count is correct at 1892.
