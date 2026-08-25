import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-bar-antisymmetry",
  title: "Proof of skein bar antisymmetry",
  uses: ["prop:skein-bar-antisymmetry"],
  authorNotes: [
    {
      kind: "note",
      body: "Case-split collapse candidates (working channel, not for\npublication): `braids-and-knots/commutative-crossing-energy`\n(separate positive/negative crossing computations → one\ncomputation + bar-apply); `braids-and-knots/phase-scoped-applicability`\n(per-crossing-sign Slater feasibility → one feasibility check +\nbar-apply); the Jones-polynomial state-sum decomposition ($L_+$\nand $L_-$ contributions enumerated → bar-equivariant sum).",
    },
  ],
});
