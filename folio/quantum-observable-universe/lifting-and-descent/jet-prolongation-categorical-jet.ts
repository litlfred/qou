import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:jet-prolongation-categorical-jet",
  lean: { ref: "qou:QOU.LiftingDescent.jp_categorical_jet",
    validation: "not_checked",
  },
  title: "Categorical jet object $J^1(A)$ inherits the Frobenius--Hopf structure",
  tags: ["kahler-differential", "frobenius-hopf", "jet-bundle", "deformation"],
  uses: [],
  proofs: ["prf:jet-prolongation-categorical-jet"],
});
