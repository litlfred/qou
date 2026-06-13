import { remark } from "../../schema/builders";

export default remark({
  label: "rem:option-e-isospin-test",
  title:
    "Option E ($c_\\lambda$ Kashiwara crystal weight) and the $T = {}^3\\mathrm{He}$ isospin invariance",
  interprets: "prop:crystal-isospin-degeneracy",
  uses: ["rem:isospin-mass-split-em-localisation"],
  tags: [
    "kashiwara-crystal",
    "option-e",
    "isospin",
    "tritium",
    "helium-3",
    "delta-i",
    "canonical-braid",
    "h-followup",
  ],
  cites: ["kashiwara1991", "lecouvey2007"],
  authorNotes: [
    {
      kind: "status",
      body: "**Empirical falsification, expected outcome.**  The probe was\ndesigned to *test* whether Option E preserves the Hopf-antipode\ninvariance under canonical $\\bowtie_K$-coupled words, and the\nresult is a clean **no** (relative split $\\sim 19$).  The\nexplanation is structural (transpose-asymmetric $c_\\lambda$), not\nnumerical, so the result is robust under precision changes.\n\nThe witness assertion\n`option_e_breaks_S_invariance_as_structurally_expected` in\n[`option-e-isospin-probe.witness.json`](../../../folio-assistant/computations/probes/option-e-isospin-probe.witness.json)\nis **true** when $\\Delta W_c > 10^{-3}$ — i.e., it *passes* when\nthe falsification fires.  CI therefore sees a clean 1/1 PASS even\nthough the underlying mathematical claim is the *opposite* of\nisospin-invariance.  Downstream audits should treat this as a\n**structural finding** (Option E is not σ-/$S$-invariant) and\nroute any binding-energy claim through the symmetrised variant\nsuggested above or through the Markov-trace observable (which IS\ninvariant per\n[Hopf-antipode invariance](#prop:spin-involution-lp-dual-invariance)).",
    },
  ],
});
