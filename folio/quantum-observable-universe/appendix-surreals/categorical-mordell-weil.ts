import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-mordell-weil",
  lean: {
    ref: "qou:QOU.AppendixSurreals.CategoricalMordellWeil",
    validation: "not_checked",
  },
  title:
    "Categorical Mordell--Weil group, $q$-Tate--Shafarevich group, and $q$-deformed $L$-function",
  uses: [
    "conj:tannaka-krein-isomorphism",
    "prop:descartes-elliptic-curve",
    "def:local-q-zeta-function",
  ],
  tags: [
    "birch-swinnerton-dyer",
    "elliptic-curve",
    "l-function",
    "mordell-weil",
    "tate-shafarevich",
    "categorical",
    "fibre-functor",
  ],
  cites: ["tate1974"],
});
