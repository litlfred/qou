import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:leray-profile",
  label: "rem:leray-profile-construction",
  title: "Truncations of the Leray system for a discretely self-similar profile",
  uses: ["def:leray-profile", "def:substrate-parameter", "rem:leray-profile-exclusions"],
  cites: ["necas-ruzicka-sverak1996", "tsai1998", "chae2013adss"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body: "Rewritten on owner instruction (wall 4 of bean qou-innq). The earlier text gave half-integer spin components ($j = 1/2$), which do not occur for a velocity field on $\\mathbb{R}^3$; described a $j = 1/2$-only reduction as one second-order ODE in $r$, which is $s$-independent and so the steady case excluded by Necas-Ruzicka-Sverak; and fixed the period by the root-of-unity scaling $\\lambda_\\kappa$, which conflicts with def:substrate-parameter. It also asserted 5 coupled ODEs without giving their coefficients. The same three claims were removed from prop:leray-profile (now def:leray-profile) and conj:regularity-breakdown item 3 on 2026-11-21 (issue #8864, owner decision).",
    },
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "Boundary condition corrected (issue #8864): the earlier text required decay faster than $r^{-3/2}$ (square-integrability). That class is excluded: a bounded $L^2$ profile is in $L^3$, and Chae (arXiv:1306.0305, Thm 1.1) excludes discretely self-similar blow-up with profile continuous in $s$ with values in $L^3$. The admissible decay is $r^{-1}$. The Necas--Ruzicka--Sverak hypothesis is also corrected from $V \\in L^2$ to $V \\in L^3$. Any Galerkin search set up with the old decay condition targets an excluded class.",
    },
  ],
  tags: ["leray", "self-similar", "blowup-profile", "representation-theory", "construction"],
});
