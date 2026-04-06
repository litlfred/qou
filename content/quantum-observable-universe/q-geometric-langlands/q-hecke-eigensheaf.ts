import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-hecke-eigensheaf",
  lean: { decl: "QOU.QHeckeEigensheaf", validation: "not_checked" },
  title: "$q$-Hecke eigensheaf",
  uses: [
    "def:q-hecke-operator",
    "def:q-local-system",
  ],
  tags: ["geometric-langlands", "hecke-algebra", "eigensheaf"],
});
