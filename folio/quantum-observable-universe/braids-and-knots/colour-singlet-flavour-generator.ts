import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:colour-singlet-flavour-generator",
  lean: {
    ref: "qou:BraidKnotOctonion.HopfColourTensorBraid.singlet_rescale",
    validation: "not_checked",
  },
  title: "On colour singlets the rescaled strand braid is the flavour Hecke generator",
  tags: ["braid-group", "colour", "hecke-algebra", "quantum-group", "markov-trace"],
  uses: [
    "prop:braid-action-tensor",
    "thm:jones-markov-trace",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-22",
      body:
        "Working assumption (owner, 2026-11-22): the three states of a strand are the three " +
        "colours, carried by the tensor braiding with the gl₆ coideal as cross-check. Owner " +
        "card choice 2026-11-22: hadron formulas use the rescaled generator −q·X = b. Record: " +
        "`docs/coordination/owner-rulings.md`; impact map " +
        "`docs/audits/2026-11-22-strand-colour-downstream-impact.md`; issue #9106, PR #9107.",
    },
  ],
});
