import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "By reinterpreting the conventional reciprocal node bar-duality (phi^-2 / phi^2) as a two-sided stability margin, this skew-dual framing provides a mathematically novel boundary condition for bounding spectral gaps." },
  ],
  label: "prop:golden-skew-dual-node",
  title:
    "Skew-dual golden node at $q = \\varphi^2$ under the bar involution $q \\leftrightarrow q^{-1}$",
  tags: [
    "golden-ratio",
    "bar-involution",
    "skew-symmetry",
    "elliptic-degeneration",
    "stability-margin",
    "substrate-parameter",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.golden_skew_dual_node",
    validation: "not_checked",
  },
  uses: ["rem:golden-ratio-degeneration"],
});
