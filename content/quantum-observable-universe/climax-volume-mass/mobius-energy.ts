import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mobius-energy",
  lean: { ref: "qou:QOU.Braiding.mobius_energy",
    validation: "not_checked",
  },
  title: "Categorical recovery of Möbius energy",
  tags: ["mobius-energy", "categorical-mass", "knot-energy", "q-deformation"],
  uses: [
    "def:categorical-action",
    "thm:topological-mass",
    "rem:frobenius-simplification",
  ],
  proofs: ["prf:mobius-energy"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/mobius-energy-0.svg", blockIndex: 0, hash: "1582a4fa10bb" },
  ],
});
