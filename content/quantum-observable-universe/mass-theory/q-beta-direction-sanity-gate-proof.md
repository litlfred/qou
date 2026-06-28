## Proof sketch

**The gate (rejection lemma):** if a candidate's substrate-evaluation
gives $|F(q_0) - F_{\text{target}}(q_0)| / F_{\text{target}}(q_0) > 10$,
the candidate fails the gate. Here $F_{\text{target}}(q_0) \approx 0.998$
is the target ladder product computed above. The 10$\times$ threshold is
loose by design — it catches order-of-magnitude direction errors (like
the $z < 1$ vs target $> 1$ case) without false-positives on small
canonical deviations that survive into the more precise §4(a) radius-
of-convergence test.

The lower bound on threshold is set by the cross-anchor swing magnitude:
the substrate $u_0$ varies by only 210 ppb between
proton and muon anchors, so any threshold tighter than ~10$\times$ would be
testing the cross-anchor invariant (a) rather than direction sanity
(d). The two gates are deliberately complementary. $\blacksquare$
