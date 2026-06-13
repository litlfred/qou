import { proposition } from "../../schema/builders";

/**
 * Threading link T(2,6) emerges from LP dual as optimal π configuration.
 */
export default proposition({
  label: "prop:benzene-threading-emergence",
  lean: { ref: "qou:QOU.Molecular.benzene_threading_emergence", validation: "not_checked" },
  title: "Threading link $T(2,6)$ emerges as the LP-optimal $\\pi$ configuration",
  uses: [
    "def:benzene-molecular-braid",
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
