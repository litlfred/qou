import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:brings-is-qou",
  label: "rem:brings-is-qou-verification",
  title: "Verification of the QOU data for Bring's surface",
  uses: [
    "prop:brings-is-qou",
    "def:brings-surface",
    "thm:qu-to-qou",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-17",
      body:
        "**OPEN — trace identity.** Item 4 writes `chi(A) = tr(id_A) = 2 - 2g = -6`. The middle equality is the identification that `rem:three-euler-characteristics` calls a collision of names; the outer two equalities hold for `chi_eu(M_0)`. Under the owner ruling of 2026-09-15, `tr(id_A) = dim_q(A)` is a q-dependent quantum dimension, and `-6` is `chi_eu(M_0)`, the topological Euler characteristic of the base curve (`rem:three-euler-characteristics`). Flagged open on owner instruction 2026-11-17 (Bring foundations cleanup); the bare `chi(A)` here was not renamed because the step uses a trace identity, not only the genus. Bean `qou-qhcr`.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"The obstruction classes $\\kappa_n \\neq 0$ persist at every level by [motivic perpetual obstruction](#thm:motivic-perpetual-obstruction) applied with $\\chi(A) = -6$.\"",
    },
  ],
});
