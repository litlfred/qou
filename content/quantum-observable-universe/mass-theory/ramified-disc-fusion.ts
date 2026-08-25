import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ramified-disc-fusion",
  // The ref now names a DECLARATION, not the module.
  //
  // Target: `resolvent_agreement`, whose own docstring says it satisfies the
  // third claim of this block's narrative — the cyclic monodromy generator
  // (rgb) acts on the Lagrange resolvent by multiplication by ζ⁻¹.
  //
  // Claims 1 (fusion into a single degree-3 ramified disc) and 2 (monodromy
  // C₃, Galois closure S₃) are NOT formalised; the module supplies only
  // `galois_group_order : Fintype.card S₃ = 6` alongside them.
  lean: {
    ref: "qou:QOU.BraidsKnots.RamifiedDiscFusion.resolvent_agreement",
    validation: "not_checked",
  },
  title: "Ramified-disc fusion at the foundry boundary",
  tags: [
    "ramified-cover",
    "monodromy",
    "exceptional-divisor",
    "s3-galois",
    "boundary-disc",
  ],
  uses: [
    "def:reeb-bundle",
    "def:color-sector-coords",
    "rem:rho-s3-holonomy-exposition",
  ],
});
