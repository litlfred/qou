import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-connection",
  title: "Categorical $q$-deformed connection",
  tags: ["connection", "deformation"],
  lean: {
    decl: "QOU.CategoricalQConnection",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-connection",
    "def:categorical-reeb",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-q-connection-0.svg", blockIndex: 0, hash: "b98993abe1fc" },
  ],

});
