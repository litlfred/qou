import { table } from "../../schema/builders";

export default table({
  label: "tbl:yang-mills-mass-gap-table-data",
  title: "Speculative dictionary between Wightman Yang--Mills and QOU objects",
  uses: [
    "conj:yang-mills-mass-gap",
    "quantum-observable-universe:def:q-yang-mills-levi",
  ],
  tags: ["extracted-table", "yang-mills", "dictionary"],
});
