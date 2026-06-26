import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While using a Discrete Fourier Transform (DFT) to diagonalize a cyclic action is standard, the explicit $n=5$ Bring-surface formalization with the modular zeta-power reduction is a non-trivial mathematical contribution. (Note that the quadric/cubic constraint transforms mentioned in the examples are stated as part of the framework but not fully formalized)." },
  ],
  label: "prop:lagrange-resolvent-transform",
  title:
    "Discrete Fourier transform diagonalises $C_5$ on the Bring's surface",
  tags: ["lagrange", "resolvent", "fourier", "c5", "brings-surface"],
  lean: { ref: "qou:QOU.BringsSurface.lagrange_resolvent_transform",
    validation: "not_checked",
  },
  uses: [
    "def:brings-surface",
  ],
  examples: ["rem:lagrange-resolvents"],
});
