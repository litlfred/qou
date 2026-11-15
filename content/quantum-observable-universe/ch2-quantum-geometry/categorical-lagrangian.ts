import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-lagrangian",
  title: "Categorical Lagrangian",
  tags: ["lagrangian", "dirac", "endomorphism"],
  lean: {
    decl: "QOU.CategoricalLagrangian",
    validation: "not_checked",
  },
  uses: ["def:categorical-dirac-operator"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-lagrangian-0.svg", blockIndex: 0, hash: "d261ff00882b" },
  ],

});
