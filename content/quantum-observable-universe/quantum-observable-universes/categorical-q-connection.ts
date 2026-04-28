import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-connection",
  title: "Categorical $q$-deformed connection",
  tags: ["connection", "deformation"],
  lean: { ref: "qou:QOU.CategoricalQConnection",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-connection",
    "def:categorical-reeb",
  ],
});
