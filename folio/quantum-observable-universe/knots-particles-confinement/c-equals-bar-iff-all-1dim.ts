import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c-equals-bar-iff-all-1dim",
  lean: { ref: "qou:QOU.ParticleInteractions.CBar.trace_conj_eq_trace_bar" },
  title:
    "Charge conjugation equals the bar involution on every irreducible character",
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Restated. The block previously claimed that $C = \\mathrm{bar}$ holds " +
        "if and only if every irreducible representation is one-dimensional, so " +
        "only at $H_2(q)$. That claim was false: $C$ together with " +
        "$q \\mapsto q^{-1}$ is a ring involution, and Tits deformation gives " +
        "$C = \\mathrm{bar}$ on every irreducible character for every $n$ " +
        "(exact check: 5460 words on $(2,1)$ of $H_3$, 0 mismatches). The label " +
        "is kept so references resolve. The Lean sibling proves the case " +
        "$n = 3$, $\\lambda = (2,1)$ for every braid word; the general case is " +
        "the narrative proof. The paragraphs that read $H_2$ as a distinguished " +
        "lepton level are removed, since nothing distinguishes it here and the " +
        "electron is $\\sigma_0\\sigma_1\\sigma_0 \\in B_3$ (owner ruling 2026-11-21).",
    },
  ],
  cites: [
    "jones1987",
    "wenzl1988c",
  ],
  tags: [
    "charge-conjugation",
    "bar-involution",
    "CPT",
    "standard-representation",
    "matter-antimatter",
    "tits-deformation",
  ],
});
