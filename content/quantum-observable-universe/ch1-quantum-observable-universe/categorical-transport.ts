import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-transport",
  lean: { decl: "QOU.CategoricalTransport" },
  status: "stated",
  title: "Categorical transport equation",
  tags: ["transport", "jet-bundle", "q-deformation"],
  uses: [
    "def:categorical-instanton",
    "def:categorical-q-ext-deriv",
    "def:categorical-jet",
  ],
  lean: {
    decl: "QOU.CategoricalTransport",
    validation: "leanok",
  },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-transport-0.svg", blockIndex: 0, hash: "0d2b87d744cb" },
    { mime: "image/svg+xml", url: "rendered/categorical-transport-1.svg", blockIndex: 1, hash: "45cc49efb3f7" },
  ],

});
