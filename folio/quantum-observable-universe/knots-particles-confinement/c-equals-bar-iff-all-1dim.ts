import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c-equals-bar-iff-all-1dim",
  lean: { ref: "qou:QOU.ParticleInteractions.CBar.trace_conj_eq_trace_bar" },
  title:
    "Charge conjugation equals the bar involution on the characters of $H_3(q)$",
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Restated. The block previously claimed that $C = \\mathrm{bar}$ holds " +
        "if and only if every irreducible representation is one-dimensional, so " +
        "only at $H_2(q)$. That claim was false: the identity also holds on $(2,1)$ of $H_3$ " +
        "(exact check: 5460 words on $(2,1)$, 0 mismatches). The label is kept " +
        "so references resolve. Scoped on 2026-11-21 to what the Lean sibling " +
        "proves: $n = 3$, $\\lambda = (2,1)$, every braid word. The " +
        "one-dimensional case is a two-line check in the narrative proof and is " +
        "not in Lean. The extension to every " +
        "$n$ and every $\\lambda$ by Tits deformation is written out as a remark " +
        "after the proof and is not formalised. The paragraphs that read $H_2$ as " +
        "a distinguished lepton level are removed, since nothing distinguishes it " +
        "here and the electron is $\\sigma_0\\sigma_1\\sigma_0 \\in B_3$ " +
        "(owner ruling 2026-11-21).",
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
