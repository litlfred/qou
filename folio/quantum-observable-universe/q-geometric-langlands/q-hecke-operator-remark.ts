import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-hecke-operator",
  label: "rem:q-hecke-operator-remark",
  title: "Hecke relation for the hmBcHecke operators",
  uses: ["def:q-hecke-operator", "prop:braid-action-tensor"],
});
