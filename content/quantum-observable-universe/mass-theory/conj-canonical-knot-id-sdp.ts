import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:canonical-knot-id-sdp",
  title:
    "Canonical knot identification for ${}^2$H, ${}^3$H, ${}^3$He from the confinement SDP",
  uses: [
    "prop:delta-max-uniform-bound",
    "conj:brane-tower-z-habiro",
  ],
  tags: [
    "tier:E",
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
  lean: {
    // Points at the SORRY-FREE ³He uniqueness closure (interior
    // case, batch 13).  The abstract `canonical_T_w_subsingleton`
    // currently delegates to `strict_complementarity_unique` which
    // still has a sorry for the general kernel-uniqueness step;
    // this manifest cites the proven concrete instance instead.
    ref: "qou:QOU.BraidKnot.helium3_uniqueness_closed",
  },
});
