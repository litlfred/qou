import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-trefoil-cinquefoil-channel",
  title:
    "The trefoil $+$ cinquefoil channel in Bring's $\\Sigma_4$",
  lean: {
    ref: "qou:QOU.BringChiralCinquefoil.bring_trefoil_cinquefoil_channel",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script:
      "computations/bring_trefoil_cinquefoil_channel.py",
    witness: [
      "computations/bring-trefoil-cinquefoil-channel.witness.json",
    ],
  },
  uses: [
    "prop:torus-embeddable-complete",
    "prop:x5-z5-automorphism",
    "def:hyperelliptic-quintic",
    "prop:lagrange-resolvent-transform",
    "prop:genus-maximal-descent",
    "rem:color-tube-cubic",
  ],
  cites: [
    "washington1997",
    "bolza1887",
  ],
  tags: [
    "brings-surface",
    "torus-knot",
    "trefoil",
    "cinquefoil",
    "chirality",
    "zeta5",
    "quintic",
    "sqrt5",
    "seifert-genus",
    "S5",
  ],
});
