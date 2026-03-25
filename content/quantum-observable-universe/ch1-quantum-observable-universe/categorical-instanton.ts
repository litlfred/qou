import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-instanton",
  title: "Categorical instanton",
  tags: ["instanton", "self-dual"],
  lean: {
    decl: "QOU.CategoricalInstanton",
    validation: "leanok",
  },
  uses: [
    "def:quantum-observable-universe",
    "def:categorical-connection",
    "def:q-hodge-star",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-instanton-0.svg", blockIndex: 0, hash: "6acc58fe5e35" },
  ],

});
