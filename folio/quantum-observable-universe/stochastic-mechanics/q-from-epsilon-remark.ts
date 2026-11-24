import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-from-epsilon-remark",
  title: "The substrate parameter as a derived quantity",
  interprets: "def:q-from-epsilon",
  tags: ["definition-commentary"],
  uses: [
    "def:q-from-epsilon",
    "def:reeb-epsilon",
  ],
});
