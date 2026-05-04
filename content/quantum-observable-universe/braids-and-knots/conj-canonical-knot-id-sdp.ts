import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:canonical-knot-id-sdp",
  title:
    "Canonical knot identification for ${}^2$H, ${}^3$H, ${}^3$He from the confinement SDP",
  uses: [
    "prop:confinement-categorical",
    "prop:atom-knot-mass-derivation",
    "prop:delta-max-uniform-bound",
    "thm:frobenius-codim-universal",
    "conj:brane-tower-z-habiro",
  ],
  tags: [
    "knot-identification",
    "sdp",
    "confinement",
    "canonical",
    "deuterium",
    "tritium",
    "helium-3",
    "gap-a",
    "audit",
  ],
});
