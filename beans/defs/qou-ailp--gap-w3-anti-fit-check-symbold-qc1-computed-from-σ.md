---
# qou-ailp
title: 'GAP W3: anti-fit check symbol(D_q)=C1 computed from Σ independently (kernel_eq_symbol, no target-matching)'
status: in-progress
pr: 8194
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T01:47:27Z
updated_at: 2026-10-04T15:19:32Z
parent: qou-frzo
---


## The wall (W3 / G3 of the C1↔SW leg) — the anti-fit gate

Parent: `qou-3cgi`; downstream of W1 (`qou-d8de`) + W2 (`qou-xufp`). The final,
STRICT step: `prolongationSymbol j = kernel j` (Lean class field `kernel_eq_symbol`),
i.e. the symbol coefficients of `D_q` (from W2) equal the proved C1 coefficients
`[m+2]_q b_{m+2} = b_{m+1} + b_m`.

**This is a gate, not a computation.** C1 is *already* fixed by the binding
recurrence. A match is meaningful ONLY if `D_q` and its symbol were computed from Σ
**independently** (W1+W2), never constructed "so that" the symbol is C1. Building
`D_q` to reproduce the binding terms is a **fit**, not a derivation — forbidden by
§"Axiomatization is NOT a Proof" / anti-laundering; may not be wired to production as
canonical.

**Honest disposition:** once W1+W2 produce an *independent* symbol, W3 is a finite
coefficient comparison (Lean/sympy). If it matches → the keystone identification is
derived. If it does NOT match → honest scope-(a) negative (this D_q construction does
not reproduce C1), recorded, not buried. Either outcome is a valid result; a forced
match is not.

## Progress (PR #8194)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/W1SpectralRigidityAndEllipticInvolution.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/w1-spectral-rigidity-and-elliptic-involution.witness.json` (`scriptHash: 5e848ba624fe`, `scriptCommitSha: 62bd8cb179998d43808552b8955ff0b3857febae`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8194 (`b0ca85df1a1275572e6a829fccdff9eb4eff2fe0`).
