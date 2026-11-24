import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-categorical-transport",
  title: "Categorical transport equation",
  tags: ["glossary", "transport", "jet-bundle", "q-deformation"],
  uses: [
    "def:categorical-instanton",
    "def:categorical-q-ext-deriv",
    "def:categorical-jet",
  ],
  defines: ["categorical-transport"],
  lean: { ref: "qou:QOU.CategoricalTransport",
    validation: "leanok",
  },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-transport-0.svg", blockIndex: 0, hash: "0d2b87d744cb" },
    { mime: "image/svg+xml", url: "rendered/categorical-transport-1.svg", blockIndex: 1, hash: "7e120dce8f91" },
  ],
});
