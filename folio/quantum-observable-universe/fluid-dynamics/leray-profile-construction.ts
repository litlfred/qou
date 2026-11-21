import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:leray-profile",
  label: "rem:leray-profile-construction",
  title: "Truncations of the Leray system for a discretely self-similar profile",
  uses: ["prop:leray-profile", "def:substrate-parameter"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body: "Rewritten on owner instruction (wall 4 of bean qou-innq). The earlier text gave half-integer spin components ($j = 1/2$), which do not occur for a velocity field on $\\mathbb{R}^3$; described a $j = 1/2$-only reduction as one second-order ODE in $r$, which is $s$-independent and so the steady case excluded by Necas-Ruzicka-Sverak; and fixed the period by the root-of-unity scaling $\\lambda_\\kappa$, which conflicts with def:substrate-parameter. It also asserted 5 coupled ODEs without giving their coefficients. The same three claims remain in prop:leray-profile and conj:regularity-breakdown item 3; changing those is a separate owner decision.",
    },
  ],
  tags: ["leray", "self-similar", "blowup-profile", "representation-theory", "construction"],
});
