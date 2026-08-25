import { definition } from "../../schema/builders";

export default definition({
  label: "def:localized-hadron",
  title: "Localized hadron",
  tags: ["hadron", "knot", "localized", "categorical"],
  lean: { ref: "qou:QOU.LocalizedHadron",
    validation: "not_checked",
  },
  uses: ["def:hadron"],
});
