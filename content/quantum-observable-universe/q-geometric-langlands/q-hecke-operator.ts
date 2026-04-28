import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-hecke-operator",
  lean: { ref: "qou:QOU.QHeckeOperator", validation: "not_checked" },
  title: "$q$-Hecke operator",
  uses: [
    "prop:braid-action-tensor",
    "def:q-local-system",
  ],
  tags: ["geometric-langlands", "hecke-algebra", "q-deformation"],
});
