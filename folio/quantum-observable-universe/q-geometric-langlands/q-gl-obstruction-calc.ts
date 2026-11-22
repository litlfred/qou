import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-gl-obstruction-calc",
  lean: { ref: "qou:QOU.q_gl_obstruction_calc", validation: "not_checked" },
  title: "Obstruction to $q$-flatness",
  proofs: ["prf:q-gl-obstruction-calc"],
  // The flatness condition the obstruction is an obstruction TO.
  // def:quantum-characteristic-classes, fixed in the same statement
  // (kappa_0 = e(xi) in H^2(S, G_m)), is omitted: it is already reached
  // through this cone.
  uses: ["def:q-flat-connection"],
  tags: ["geometric-langlands", "yekutieli", "obstruction"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Owner ruling (card, 2026-11-15: fix, keep H^2). The HKR identification of HH^2(U_q, Ad) with H^2(S, G_m) and the trace isomorphism are now named hypotheses (H-HKR), (H-tr), not consequences of HKR. Intrinsic and connection-dependent curvature are kept apart, so q-flat connections can exist when kappa_0 != 0, in line with item 4. The reduction kappa_0 mod n stays in H^2(S, G_m)/n; the earlier reading in H^2(mu_n) is dropped, since Kummer puts H^2(G_m)/n inside H^3(mu_n). The Lean sibling was not changed.",
    },
  ],
});
