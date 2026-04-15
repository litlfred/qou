import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:categorical-reeb-exists",
  title: "Existence of the categorical Reeb derivation",
  lean: {
    decl: "QOU.CategoricalReeb.ofWeightDecomposition",
    validation: "not_checked",
  },
  uses: ["def:categorical-reeb"],
  proofs: ["prf:categorical-reeb-exists"],
  tags: ["existence", "reeb", "derivation"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-reeb-exists-0.svg", blockIndex: 0, hash: "3cea3e5ef931" },
  ],

});
