import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lagrange-resolvent-transform",
  proofs: ["prf:lagrange-resolvent-transform"],
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
