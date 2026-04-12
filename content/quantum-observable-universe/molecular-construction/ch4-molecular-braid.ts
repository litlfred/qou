import { definition } from "../../schema/builders";

/**
 * CH₄ molecular braid: tetrahedral methane from braid optimization.
 */
export default definition({
  label: "def:ch4-molecular-braid",
  title: "Methane $CH_4$ as a molecular braid",
  lean: {
    decl: "QOU.Molecular.CH4Braid",
    validation: "not_checked",
  },
  uses: [
    "def:molecular-braid",
    "def:covalent-bond-shared-trefoil",
    "def:h2-molecular-braid",
  ],
  tags: [
    "methane",
    "CH4",
    "tetrahedral",
    "single-bond",
    "molecular-braid",
  ],
});
