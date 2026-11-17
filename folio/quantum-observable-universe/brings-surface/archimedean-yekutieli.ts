import { example } from "../../schema/builders";

export default example({
  interprets: "thm:qu-to-qou",
  label: "ex:archimedean-yekutieli",
  title: "Bring's surface and $q$-flatness obstructions",
  tags: ["archimedean-universe", "yekutieli", "brings-surface", "motivic-galois"],
  uses: [
    "rem:mass-geometric-drag",
    "rem:chirality-trefoil",
    "rem:kummer-tower",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-17",
      body:
        "**OPEN — trace identity.** The block attaches `chi(A) = -6` to the lifting obstruction classes `kappa_n`. Whether the obstruction pairs with the genus or with a trace of `A` decides whether this is a rename or a substantive claim. Under the owner ruling of 2026-09-15, `tr(id_A) = dim_q(A)` is a q-dependent quantum dimension, and `-6` is `chi_eu(M_0)`, the topological Euler characteristic of the base curve (`rem:three-euler-characteristics`). Flagged open on owner instruction 2026-11-17 (Bring foundations cleanup); the bare `chi(A)` here was not renamed because the step uses a trace identity, not only the genus. Bean `qou-qhcr`.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"the perpetual non-vanishing $\\kappa_n \\neq 0$ implies\"",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"The non-vanishing obstruction classes $\\kappa_n$ obstruct smooth lifting at every level, creating\"",
    },
  ],
});
