import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-hodge-star",
  title: "$q$-Hodge star",
  tags: ["hodge-star", "deformation"],
  lean: { ref: "qou:QOU.QHodgeStar",
    validation: "not_checked",
  },
  uses: ["def:categorical-hodge-star", "def:substrate-parameter"],
});
