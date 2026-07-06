import { prose } from "../../schema/builders";

export default prose({
  label: "prose:knot-periodic-table",
  title: "Knot-periodic table of the elements",
  uses: [
    "prop:shell-structure-eigenvalues",
    "thm:generation-completeness",
    "rem:knot-exhaustiveness",
  ],
  tags: [
    "knot",
    "periodic-table",
    "mass",
    "generation",
    "torus-knot",
    "proton",
    "neutron",
    "transfer-matrix",
    "skein-polynomial",
    "appendix",
    "fermion",
    "boson",
  ],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
