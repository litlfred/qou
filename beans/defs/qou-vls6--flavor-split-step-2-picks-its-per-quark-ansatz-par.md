---
# qou-vls6
title: Flavor-split Step 2 picks its per-quark ansatz partly by agreement with experiment (-0.67%)
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T10:30:38Z
updated_at: 2026-10-11T07:50:29Z
parent: qou-d8c7
---

observations/flavor-split-substrate-proof.md Step 2 justifies the ansatz (mu_d - mu_u)/mu_avg ~ h_q^2 hbar_q/sqrt q by three conditions. Condition (c) is 'numerical agreement to -0.67% at q = q0'. Choosing a formula because it matches the target is selection against the target, which §NO FITTING excludes. Conditions (a) and (b) alone (bar-odd, leading order (q-1)^3) do not single out this form. The ansatz also sits on the convention-C pair-Skein denominator (M6 1a). Next step: state the ansatz as a fit (label it), or find what derives it. Found during M6 (qou-2cof), 2026-10-10.

## 2026-10-10: labelled as a fit
flavor-split-substrate-proof.md Step 2 now carries a dated note saying eq. (2) is a fitted ansatz. Condition (a) also turns out false as stated: f(1/q) = -q^2 f(q) (sympy), so f is antisymmetric only up to q^2. Condition (b) holds: leading term 4(q-1)^3. Open: a derivation that replaces the fit. Stays open.

### Cross-link (2026-10-11)

δ (leading) is **DERIVED**, not fitted — closed form in q, sorry-free `theorem flavor_split_substrate` (HadronicMass.lean:826), −0.10 % residual; it is the **subleading** `(1+ℏ_q³)` that is POSITED and de-wired. Record: [`2026-10-11-atom-word-provenance.md`](../../docs/audits/2026-10-11-atom-word-provenance.md).
