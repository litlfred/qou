import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-q-ext-deriv",
  title: "Categorical $q$-deformed exterior derivative",
  tags: ["exterior-derivative", "deformation"],
  lean: {
    decl: "QOU.CategoricalQExtDeriv",
    validation: "leanok",
  },
  uses: [
    "def:categorical-connection",
    "def:substrate-parameter",
    "def:positive-definite-dagger",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-q-ext-deriv-0.svg", blockIndex: 0, hash: "1098849523c8" },
  ],

});
