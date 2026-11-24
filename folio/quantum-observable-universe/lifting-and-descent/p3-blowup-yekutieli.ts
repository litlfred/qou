import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:blowup-yekutieli",
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-88nf`): `2026-08-30-conditional-classes-still-vacuous-after-bundle-removal.lean` records replacing the vacuous blow-up rate existential on `QOU.AlgebraicSubstrate.BlowupYekutieli` with this proposition's obstruction-vanishing equivalence.",
      see: "docs/audits/2026-08-30-conditional-classes-still-vacuous-after-bundle-removal.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation refutability witness (`qou-x60n`, `qou-88nf`): `2026-08-30-qns-carriers-are-refutable.lean` proves refutation (`¬ BlowupYekutieli 0 False`) and level-3 non-vanishing obstruction satisfiability for `BlowupYekutieli`.",
      see: "docs/audits/2026-08-30-qns-carriers-are-refutable.lean",
    },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): The [regularity breakdown](#conj:regularity-breakdown) at $q = 1$ is a **cohomological obstruction** in the [Yekutieli lifting](#prop:yekutieli-lifting) framework." },
  ],
  lean: { ref: "qou:QOU.FluidDynamics.BlowupYekutieli" },
  title:
    "Blowup mechanism as Yekutieli lifting obstruction in the brane tower",
  uses: [
    // conj:regularity-breakdown removed (2026-06-08 §3b): this prop is the
    // unconditional reformulation "NS blowup ⟺ obstruction level n*", not a
    // result that assumes blow-up occurs; conjecture kept as a prose cross-ref.
    "prop:descent-condition",
    "def:local-cohomology-group",
    "rem:vortex-reconnection",
  ],
  tags: [
    "blowup",
    "yekutieli",
    "obstruction",
    "cohomology",
    "brane-tower",
    "gerbe",
    "millennium-problem",
  ],
});
