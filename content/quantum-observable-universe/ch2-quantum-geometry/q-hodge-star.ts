import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-hodge-star",
  title: "$q$-Hodge star",
  tags: ["hodge-star", "deformation"],
  lean: {
    decl: "QOU.QHodgeStar",
    validation: "not_checked",
  },
  uses: ["def:categorical-hodge-star", "def:substrate-parameter"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/q-hodge-star-0.svg", blockIndex: 0, hash: "16b5a585f00c" },
  ],

});
