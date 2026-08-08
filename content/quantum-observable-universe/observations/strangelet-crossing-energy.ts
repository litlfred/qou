import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Corrected (claim 2).** This block read the vanishing Coulomb charge " +
        "as leaving the crossing energy in the *symmetric* channel with " +
        "multiplicity $\\tfrac{1}{2}(n_+ + n_-)$, i.e. " +
        "$N\\cdot\\tfrac{1}{2}(n_+ + n_-)(q + q^{-1})$. That inherits the " +
        "exchanged multiplicities corrected upstream in `def:coulomb-charge`: " +
        "$Q = \\tfrac{1}{2}(n_+ - n_-)$ is the coefficient of the **bar-even** " +
        "channel, so $Q = 0$ *annihilates* that channel rather than leaving it " +
        "as the whole. Directly from `def:crossing-energy`, $Q = 0$ gives " +
        "$n_+ = n_-$ and $\\mathfrak{E}_{\\mathrm{cross}} = n_+(q - q^{-1})$ — " +
        "purely **bar-odd**. The block had both the channel and the sign of the " +
        "$q^{\\pm 1}$ combination wrong. Pinned as registry entry " +
        "`R1-em-strangelet-q-zero-bar-odd`. The former title (\"purely strong\") " +
        "asserted the withdrawn bar-odd/bar-even-to-force identification and is " +
        "retitled channel-neutrally.",
      see: "docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md",
    },
  ],
  label: "prop:strangelet-crossing-energy",
  lean: { ref: "qou:QOU.Observations.strangelet_crossing_energy", validation: "not_checked" },
  title:
    "Crossing energy of strange quark matter is purely bar-odd",
  tags: [
    "strangelet",
    "strange-quark-matter",
    "crossing-energy",
    "coulomb-charge",
    "electromagnetic-neutrality",
    "witten",
  ],
});
