import { definition } from "../../schema/builders";

/**
 * H₂ molecular braid: the simplest covalent molecule.
 * Two protons + two electrons in H₄(q).
 */
export default definition({
  label: "def:h2-molecular-braid",
  title: "Hydrogen molecule $H_2$ as a braid in $H_4(q)$",
  lean: { ref: "qou:QOU.Molecular.H2Braid",
    validation: "not_checked",
  },
  uses: ["def:covalent-bond-shared-trefoil"],
  tags: [
    "hydrogen",
    "H2",
    "covalent-bond",
    "molecular-braid",
    "prototype",
  ],
  computation: {
    engine: "python",
    script: "computations/hh-vertex-volume.py",
    witness: [
      "computations/hh-trefoil-corrected.witness.json",
      "computations/hh-vertex-volume.witness.json",
    ],
    status: "experimental",
  },
});
