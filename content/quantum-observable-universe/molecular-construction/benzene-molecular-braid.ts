import { definition } from "../../schema/builders";

/**
 * Benzene molecular braid: C₆H₆ with delocalized π electrons.
 */
export default definition({
  label: "def:benzene-molecular-braid",
  title: "Benzene $C_6H_6$ as a molecular braid",
  lean: { ref: "qou:QOU.Molecular.BenzeneBraid",
    validation: "not_checked",
  },
  uses: ["def:ch4-molecular-braid"],
  tags: [
    "benzene",
    "C6H6",
    "aromatic",
    "delocalization",
    "threading-link",
    "molecular-braid",
  ],
});
