import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hoefsmit-ew-cell-content",
  title:
    "Hoefsmit cell-content identification of the EW triplet inside $\\mathrm{End}_R(V^{\\otimes 6})$ (categorical existence)",
  lean: {
    ref: "qou:QOU.IwahoriHecke.Hoefsmit.HoefsmitSeminormalBasis",
    validation: "not_checked",
  },
  uses: ["prop:knot-operator-lp-selection"],
  tags: [
    "hoefsmit",
    "cell-content",
    "seminormal-form",
    "wedderburn-decomposition",
    "electroweak",
    "ew-triplet",
    "disjoint-strand-pair",
    "non-uniform-plancherel",
    "n-six",
    "closure-tier-b",
    "phase-2-sprint-5-discharge",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** The Hoefsmit cell-content arithmetic is correct\n(verified by the witness enumeration); the open inputs are:\n\n1. **The $W \\leftrightarrow \\sigma_1^4$, $Z \\leftrightarrow \\sigma_3^6$,\n $H \\leftrightarrow \\sigma_5^8$ identification** — currently a\n structural proposal motivated by disjoint-strand-pair commutativity\n plus matching twist parameters $k = 2, 3, 4$ to the EW link triplet.\n Needs a categorical-physics block (the \"categorical Higgs mechanism\"\n item from\n `conj:force-carrier-knot-vs-link-dichotomy`\n §Status) discharging the boson-to-strand-pair assignment.\n2. **The non-uniform Plancherel weight derivation** — the\n multiplicities $(2, 1, 3, 3, 1, 2)$ are read off from the\n tableaux enumeration; promoting them to a closed-form\n $q$-rational requires identifying their generating function in\n the Hoefsmit cell-content arithmetic.\n3. **Refinement of upstream blocks** — the existing\n [`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness)\n and\n [`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization)\n should be edited to reference this $n = 6$ formulation.",
    },
  ],
});
