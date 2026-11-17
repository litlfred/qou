import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:brings-is-qou",
  label: "rem:brings-is-qou-verification",
  title: "Verification of the QOU data for Bring's surface",
  uses: [
    "rem:three-euler-characteristics",
    "prop:brings-is-qou",
    "def:brings-surface",
    "thm:qu-to-qou",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-17",
      body:
        "**RESOLVED 2026-11-17 — trace identity removed.** Item 4 wrote `chi(A) = tr(id_A) = 2 - 2g = -6`; the middle equality identified the categorical trace with the topological Euler characteristic, which `rem:three-euler-characteristics` calls a collision of names (owner ruling 2026-09-15). Item 4 now states `chi_eu(M_0) = 2 - 2g = -6` only. Nothing in the verification used the trace. Bean `qou-qhcr`, PR #8365.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"The obstruction classes $\\kappa_n \\neq 0$ persist at every level by [motivic perpetual obstruction](#thm:motivic-perpetual-obstruction) applied with $\\chi(A) = -6$.\"",
    },
  ],
});
