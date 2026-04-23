import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-ext-deriv",
  title: "Categorical $q$-deformed exterior derivative",
  tags: ["exterior-derivative", "deformation"],
  lean: { ref: "qou:QOU.CategoricalQExtDeriv",
    validation: "leanok",
  },
  uses: [
    "def:categorical-connection",
    "def:substrate-parameter",
    "prop:positive-definite-dagger",
  ],
  examples: ["ex:q-ext-deriv", "ex:q-lie-bracket", "ex:q-connection", "ex:q-reeb-vector-field", "ex:q-reeb-flow", "ex:q-torsion-leaf"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-q-ext-deriv-0.svg", blockIndex: 0, hash: "1098849523c8" },
  ],

});
