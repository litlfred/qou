import { proposition } from "../../schema/builders";

/**
 * Threading link T(2,6) emerges from LP dual as optimal π configuration.
 */
export default proposition({
  label: "prop:benzene-threading-emergence",
  lean: {
    decl: "QOU.MolecularConstruction.benzene_threading_emergence",
    file: "QOU/MolecularConstruction.lean",
    validation: "not_checked",
  },
  title: "Threading link $T(2,6)$ emerges as the LP-optimal $\\pi$ configuration",
  uses: [
    "def:benzene-molecular-braid",
    "prop:h2-lp-dual-binding",
    "prop:co2-lp-dual-binding",
  ],
  tags: [
    "benzene",
    "threading-link",
    "delocalization",
    "LP-dual",
    "aromatic",
    "emergence",
  ],
});
