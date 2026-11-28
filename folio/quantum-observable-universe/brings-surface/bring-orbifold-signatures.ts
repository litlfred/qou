import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-orbifold-signatures",
  title: "Orbifold signatures of the symmetry quotients of Bring's surface",
  lean: { ref: "qou:QOU.Brings.OrbifoldSignatures.cone_orders_derived" },
  uses: ["prop:bring-harmonic-types", "prop:bring-reflection-parity"],
  tags: ["brings-surface", "orbifold", "representation-theory", "quotients"],
  proofs: ["prf:bring-orbifold-signatures"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Bean `qou-u81q`, owner card 2026-11-28 (\"Both\"). Lean, sorry-free: `QOU/BringsSurface/BringOrbifoldSignatures.lean`. The cone points of every `B/H` are derived from class distributions and fixed-cell counts. The `B/(H × c)` table is computed by `computations/probes/bring_orbifold_signatures_probe.py` and checked in Lean for consistency (orbifold Euler characteristic, mirror criterion, valid underlying surfaces); it is not derived there. The class distributions of the 19 subgroup classes come from the enumeration probe of `bring-symmetry-quotients`.",
    },
  ],
});
