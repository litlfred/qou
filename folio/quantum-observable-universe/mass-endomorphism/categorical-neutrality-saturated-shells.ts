import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-neutrality-saturated-shells",
  title:
    "Categorical neutrality of saturated shells: full-twist identity action on $\\Phi_n$ at magic $n$",
  lean: {
    ref: "qou:QOU.ShellNeutrality.SaturatedShellConjecture",
    validation: "not_checked",
  },
  uses: ["conj:mass-endomorphism"],
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
    "ariki1996",
    "jucys1974",
    "murphy1992",
    "mathas1999",
  ],
  tags: [
    "magic-numbers",
    "shell-closure",
    "full-twist",
    "global-section",
    "categorical-neutrality",
    "ribbon-element",
    "framing-anomaly",
    "open-problem",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/full_twist_root_of_unity_probe.py",
    witness: [
      "computations/full-twist-delta-n2-verification.witness.json",
      "computations/probes/full-twist-root-of-unity-probe.witness.json",
    ],
    status: "experimental",
  },
});
