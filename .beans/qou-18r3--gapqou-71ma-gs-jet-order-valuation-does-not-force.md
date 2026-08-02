---
# qou-18r3
title: 'GAP/qou-71ma: GS jet-order valuation does NOT force single-degree selection (crux answered NEGATIVE)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T13:47:14Z
updated_at: 2026-08-02T13:47:33Z
---

Epic qou-r2nh. Alias of the orchestrator bean qou-71ma (not committed in this checkout).

VERDICT (NEGATIVE, sorry-free — PR #4574): the GS jet-order valuation = Lusztig
a-function n(λ) supplies the grade VALUE (bottom fake-degree grade + its parity =
the derived chirality sign) but does NOT force the single-degree / top-cohomology
CONCENTRATION. A valuation is degree-blind; formalized at n=5:
G_λ (concentrated) and H_λ (honest coinvariant/fake-degree object) share BOTH the
valuation n(λ) AND the ungraded Wedderburn dim, yet differ in signed Euler char;
only G_λ = Δ_λ. Sharp mechanism (fakeCoeff_at_valuation_eq_one): at grade n(λ) the
natural object carries coefficient 1 (monic leading term of f_λ(q)), not dim V_λ.

This is the third/last candidate forcing mechanism to fall: count (#4559) / SDP
(#4570) / jet-order valuation (this). Does NOT reopen Δ_λ's VALUE (= two substrate
scalars: jet-order parity + Wedderburn dim). Residual (a DIFFERENT leg): the open
primary conjecture DeltaLambdaDTRealization — whether a genuine graded substrate
structure (not a valuation) forces the concentration / the DT moduli 𝓑_λ.

Lean: content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaJetOrderDegreeSelection.lean (lean-verify exit 0).
Audit: docs/audits/2026-08-02-deltalambda-jetorder-degree-selection.md.
