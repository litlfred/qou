import { table } from "../../schema/builders";

export default table({
  label: "tbl:vortex-intensity-modes-table-data",
  title: "Classical fluid concepts and their $q$-deformed analogues",
  caption:
    "Six classical fluid-dynamics concepts (Kelvin waves, circulation, " +
    "breakdown states, stability eigenvalues, superfluid quantisation, " +
    "Reynolds number) paired with their QOU $q$-deformed analogues and " +
    "the discreteness source that the $q$-deformation supplies.",
  uses: ["rem:vortex-intensity-modes"],
  tags: ["vortex", "fluid-dynamics", "q-deformation", "summary-table"],
});
