import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-action",
  title: "Categorical action",
  tags: ["action", "categorical"],
  lean: {
    decl: "QOU.CategoricalAction",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-universe",
    "def:quantum-observable-universe",
    "def:categorical-connection",
    "def:substrate-parameter",
    "def:q-hodge-star",
    "rem:categorical-action-notation",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-action-0.svg", blockIndex: 0, hash: "ace2c42d8e04" },
  ],

});
