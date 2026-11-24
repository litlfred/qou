import { remark } from "../../schema/builders";

export default remark({
  label: "rem:derived-atom-normal-form",
  title: "Inductive reduction and normal form of the derived atom",
  interprets: "def:derived-atom",
  tags: ["atom", "groebner-shirshov"],
  uses: [
    "def:derived-atom",
  ],
});
