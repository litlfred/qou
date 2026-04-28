import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-hecke-eigensheaf",
  lean: { ref: "qou:QOU.QHeckeEigensheaf", validation: "not_checked" },
  title: "$q$-Hecke eigensheaf",
  uses: ["def:q-hecke-operator"],
  tags: ["geometric-langlands", "hecke-algebra", "eigensheaf"],
});
