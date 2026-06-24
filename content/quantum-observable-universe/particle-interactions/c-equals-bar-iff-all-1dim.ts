import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c-equals-bar-iff-all-1dim",
  proofs: ["prf:c-equals-bar-iff-all-1dim"],
  lean: { ref: "qou:QOU.ParticleInteractions.two_only_unit_squares" },
  title:
    "Charge conjugation equals bar involution iff all irreps are one-dimensional",
  uses: ["prop:lepton-meson-torus-knot-dictionary"],
  cites: [
    "jones1987",
    "wenzl1988c",
  ],
  tags: [
    "charge-conjugation",
    "bar-involution",
    "CPT",
    "lepton",
    "meson",
    "standard-representation",
    "matter-antimatter",
  ],
});
