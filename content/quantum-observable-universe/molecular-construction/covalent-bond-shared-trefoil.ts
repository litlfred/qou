import { definition } from "../../schema/builders";

/**
 * Covalent bond as a shared electron trefoil Hopf-linked
 * across two nuclei.
 */
export default definition({
  label: "def:covalent-bond-shared-trefoil",
  title: "Covalent bond as shared electron trefoil",
  lean: { ref: "qou:QOU.Molecular.CovalentBond",
    validation: "not_checked",
  },
  uses: ["def:molecular-braid"],
  tags: [
    "covalent-bond",
    "trefoil",
    "hopf-link",
    "electron-sharing",
  ],
});
