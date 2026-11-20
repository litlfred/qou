import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:higgs-vacuum-residual-idempotent",
  label: "rem:higgs-vacuum-residual-graviton",
  title: "Graviton candidate 3: the symmetric square of the Higgs-vacuum residual",
  uses: [
    "prop:higgs-vacuum-residual-idempotent",
    "conj:mass-endomorphism",
    "conj:g-action-on-substrate",
  ],
  tags: ["graviton", "categorical-higgs", "residual", "interpretation", "open-problem"],
});
