import { remark } from "../../schema/builders";

// Was prf:topological-mass-dilogarithm. The block it argued for is now the
// conjecture conj:topological-mass-dilogarithm (owner card, 2026-11-21:
// "Demote both"), so the argument is recorded as a sketch, not a proof.
export default remark({
  label: "rem:topological-mass-dilogarithm-sketch",
  renamedFrom: ["prf:topological-mass-dilogarithm"],
  title: "Argument sketch for the symmetric $q$-dilogarithm evaluation",
  interprets: "conj:topological-mass-dilogarithm",
  uses: ["conj:topological-mass-dilogarithm"],
});
