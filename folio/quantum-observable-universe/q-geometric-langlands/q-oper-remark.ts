import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-oper",
  label: "rem:q-oper-remark",
  title: "Rank-2 hmBcopers as hmBcSturm--Liouville operators",
  uses: ["def:q-oper", "def:q-flat-connection"],
});
