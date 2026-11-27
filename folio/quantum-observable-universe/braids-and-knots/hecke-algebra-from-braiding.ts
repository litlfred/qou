import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:jones-markov-trace",
  label: "rem:hecke-algebra-from-braiding",
  title: "The Iwahori--Hecke algebra $H_n(q)$ as a categorical quotient",
  tags: [
    "hecke-algebra",
    "braiding",
    "substrate-parameter",
    "categorical",
    "groebner-basis",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation regression guard (`qou-x60n`): `2026-08-23-free-prop-real-module-probe.lean` (`zero_generators_rejected`) verifies `QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra` enforces equational Hecke relations rather than bare `Prop` fields.",
      see: "docs/audits/2026-08-23-free-prop-real-module-probe.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation regression guard (`qou-x60n`): `2026-08-23-trivial-global-instance-probe.lean` verifies `triv_hecke` and `triv_wedderburn` in `QOU.Mathlib.HeckeAlgebra` are explicit `def`s rather than global `PUnit` instances.",
      see: "docs/audits/2026-08-23-trivial-global-instance-probe.lean",
    },
  ],
});
