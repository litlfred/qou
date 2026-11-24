import { remark } from "../../schema/builders";

export default remark({
  label: "rem:reeb-bundle-remark",
  title: "The three structures of the Reeb bundle",
  interprets: "def:reeb-bundle",
  uses: [
    "def:reeb-bundle",
    "def:exceptional-divisor",
    "ex:q-reeb-vector-field",
  ],
});
