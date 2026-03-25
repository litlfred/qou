import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-jet",
  title: "Categorical jet object",
  lean: {
    decl: "QOU.CategoricalJet",
    validation: "axioms_only",
  },
  uses: ["def:quantum-universe", "def:categorical-connection"],
  tags: ["jet"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-jet-0.svg", blockIndex: 0, hash: "2604ff8ef04c" },
  ],

});
