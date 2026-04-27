import { definition } from "../../schema/builders";

export default definition({
  label: "def:borromean-baryon",
  title: "Borromean baryon",
  tags: ["borromean", "baryon", "unknot", "color-confinement", "link"],
  lean: { ref: "qou:QOU.Braiding.BorromeanBaryon",
    validation: "not_checked",
  },
  uses: ["def:hadron"],
});
