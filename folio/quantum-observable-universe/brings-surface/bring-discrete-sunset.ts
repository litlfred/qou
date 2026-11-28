import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-discrete-sunset",
  title: "The exact discrete sunset on the Bring map graph",
  lean: { ref: "qou:QOU.Brings.DiscreteSunset.discrete_sunset" },
  uses: ["prop:bring-spectral-sunset-selection", "prop:bring-reflection-parity"],
  tags: ["brings-surface", "harmonics", "representation-theory", "two-loop", "selection-rule", "graph-laplacian"],
  proofs: ["prf:bring-discrete-sunset"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Bean `qou-u81q`, owner card 2026-11-28 (\"Both\"). Lean, sorry-free, by `decide +kernel` on integer matrices: `QOU/BringsSurface/BringDiscreteSunset.lean`. Probe: `computations/probes/bring_discrete_sunset_probe.py`. This is the combinatorial Laplacian of the 1-skeleton of the map, not the hyperbolic Laplacian; it is a finite model of the selection rule, and its numbers are not eigenvalues of the surface.",
    },
  ],
});
