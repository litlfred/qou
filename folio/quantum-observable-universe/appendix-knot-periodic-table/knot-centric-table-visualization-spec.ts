import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:shell-transition-knot",
  label: "rem:knot-centric-table-visualization-spec",
  title:
    "Continuous $q$-deformation of the periodic grid from $q = 1$ to $q_0$",
  tags: [
    "periodic-table",
    "knot-centric",
    "visualization",
    "simulator",
    "appendix",
  ],
  uses: [
    "prop:shell-structure-eigenvalues",
    "rem:knot-atom-diagrams",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_wave3_periodic_table_synthesis_probe.py",
    witness: "computations/probes/nuclear-wave3-periodic-table-synthesis.witness.json",
    status: "verified",
  },
});
