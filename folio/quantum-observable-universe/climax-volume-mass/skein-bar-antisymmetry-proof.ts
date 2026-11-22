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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Connection to substrate bar T-duality.**\n\nBar-antisymmetry of (S) is the **algebraic origin** of the\nsubstrate-level bar T-duality\n([bar T-duality substrate](#prop:bar-t-duality-substrate)):\nthe Markov trace $\\mathrm{tr}_M \\colon H_n(q) \\to \\mathbb{C}(q)$\ncommutes with $\\overline{\\,\\cdot\\,}$ up to sign on antisymmetric\nelements, so the geometric bar-pairing on the moduli of\n$\\mathcal{E}_q$ inherits its sign structure from (S)." },
  ],
});
