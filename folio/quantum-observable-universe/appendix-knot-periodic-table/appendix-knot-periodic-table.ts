import { chapter, section } from "../../schema/builders";

/**
 * Annex A: Master Braid-Operator, Particle, Nuclear, and Molecular Reference Atlas.
 *
 * Consolidates the pre-Archimedean braid/Hecke operator dictionary (over generic R),
 * the Archimedean calibration & 80-digit Fréchet–Jacobian uncertainty protocol,
 * the five uniform six-column Master Reference Tables (Tables A.1–A.5), and the
 * Z = 0..118 nuclide registry and interactive knot-periodic-table simulators.
 */
export default chapter({
  tabLabel: "A",
  title: "Master Braid-Operator, Particle, Nuclear, and Molecular Reference Atlas",
  label: "app:knot-periodic-table",
  sections: [
    section({
      title: "Pre-Archimedean braid and Hecke operator dictionary",
      label: "sec:hecke-operations",
      blocks: [
        "hecke-operations",
        "hecke-operations-table2-data",
        "hecke-operations-table1-data",
        "borromean-gluon-content",
        "knot-operator-basis-table-intro",
        "knot-operator-basis-table",
        "knot-operator-basis-table-table1-data",
        "knot-operator-basis-table-table2-data",
        "knot-operator-basis-table-table3-data",
        "knot-operator-basis-table-table4-data",
      ],
    }),
    section({
      title: "Calibration protocol, Fréchet--Jacobian error propagation, and Master Tables A.1--A.5",
      label: "sec:master-atlas-calibration",
      blocks: [
        "master-atlas-calibration-jacobian",
        "per-observable-100x-status-dashboard",
        "master-atlas-particles",
        "master-atlas-hadrons",
        "master-atlas-decays",
        "master-atlas-nuclides-summary",
        "master-atlas-molecules",
        "particle-nf-table",
        "particle-nf-table-table-data",
        "hadron-level-knot-table",
        "hadron-level-knot-table-data",
        "gluon-model-comparison",
      ],
    }),
    section({
      title: "Nuclide registry ($Z = 0\\ldots 118$) and light-atom knot diagrams",
      label: "sec:knot-periodic-table",
      blocks: [
        "knot-atom-diagrams",
        "knot-atom-diagrams-sim",
        "knot-periodic-table",
        "recursive-atom-knot-atlas",
        "recursive-atom-knot-atlas-registry",
        "recursive-atom-knot-atlas-interpretation",
        "recursive-atom-knot-atlas-sdp-uniqueness-wiring",
        "recursive-atom-knot-atlas-open-problems",
      ],
    }),
    section({
      title: "Knot-centric periodic table and interactive visualisations",
      label: "sec:knot-centric-table",
      blocks: [
        "knot-centric-table-intro",
        "knot-centric-table",
        "knot-centric-table-visualization-spec",
        "knot-centric-table-table1-data",
        "knot-centric-table-table2-data",
        "knot-centric-table-table3-data",
        "knot-periodic-table-sim",
      ],
    }),
  ],
});
