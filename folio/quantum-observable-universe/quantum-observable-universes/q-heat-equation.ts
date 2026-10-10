import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-heat-equation",
  title: "$q$-Heat equation",
  tags: ["q-laplacian", "heat-equation", "reeb-flow", "evolution"],
  lean: { ref: "qou:QOU.QHeatEquation",
    validation: "not_checked",
  },
  uses: [
    "def:q-harmonic-form",
    "prop:substrate-radial-coordinate",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `quantum-observable-universes/q-heat-equation.lean` " +
        "uses `ℝ` as the **time** parameter of an evolution equation (`evolves : ∀ (t : ℝ) (x : S), …`). " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
