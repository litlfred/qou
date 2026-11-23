import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:coulomb-strong-ratio-q-rational",
  title:
    "Coulomb/strong ratio $\\tanh(\\ln q)$ is the q-rational $(q^2-1)/(q^2+1)$",
  tags: ["coulomb", "ratio", "tanh", "q-rational", "identity", "lean"],
  lean: {
    ref: "qou:QOU.Braiding.coulomb_strong_ratio_q_rational",
    validation: "not_checked",
  },
  uses: ["def:coulomb-charge"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; for mixed crossing signs it acquires the multiplicity factor $\\tfrac{n_+ + n_-}{n_+ - n_-}$ and is not a constant of the framework ([decomposition](#prop:crossing-energy-decomposition), item 4)." },
  ],
});
