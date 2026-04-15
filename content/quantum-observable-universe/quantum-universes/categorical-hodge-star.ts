import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-hodge-star",
  title: "Categorical Hodge star",
  lean: {
    decl: "QOU.CatHodgeInvolution",
    validation: "not_checked",
  },
  uses: ["def:higher-forms"],
  examples: ["ex:hodge-su2"],
  tags: ["hodge-star"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-hodge-star-0.svg", blockIndex: 0, hash: "20a1de92f2ef" },
  ],

});
