import { definition } from "../../schema/builders";

/**
 * The molecular braid: extending atomic braids to multi-atom systems
 * by Hopf-linking pre-computed atomic braids with shared electron trefoils.
 */
export default definition({
  label: "def:molecular-braid",
  title: "Molecular braid $H_{N_{\\mathrm{mol}}}(q)$",
  lean: { ref: "qou:QOU.Molecular.MolecularBraid",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-normal-form",
    "def:universal-ilp-algorithm",
  ],
  tags: [
    "molecular",
    "hecke-algebra",
    "covalent-bond",
    "iterative-construction",
  ],
});
