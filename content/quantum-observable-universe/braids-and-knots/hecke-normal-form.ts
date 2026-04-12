import { definition } from "../../schema/builders";

export default definition({
  label: "def:hecke-normal-form",
  title: "Hecke normal form in $H_n(q)$",
  lean: {
    decl: "QOU.Braiding.HeckeNormalForm",
    validation: "not_checked",
  },
  uses: [
    "rem:hecke-algebra-from-braiding",
    "def:substrate-parameter",
  ],
  tags: [
    "hecke-algebra",
    "normal-form",
    "groebner-shirshov",
    "canonical-basis",
  ],
});
