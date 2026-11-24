import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-reeb",
  label: "ex:q-reeb-vector-field",
  title: "$q$-Deformed Reeb vector field",
  lean: { ref: "qou:QOU.qReebVectorField", validation: "not_checked" },
  uses: ["ex:q-lie-bracket"],
  tags: ["reeb", "archimedean"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation twin-audit (`qou-x60n`): `2026-09-05-archimedean-twins-are-instantiations-probe.lean` (`qReeb_arch_is_generic`) proves the `ℝ`-valued q-Reeb expression is the generic field form instantiated at `(field p)⁻¹`.",
      see: "docs/audits/2026-09-05-archimedean-twins-are-instantiations-probe.lean",
    },
  ],
});
