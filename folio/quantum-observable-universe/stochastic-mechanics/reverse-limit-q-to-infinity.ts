import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:reverse-limit-q-to-infinity",
  title:
    "Reverse limit $q \\to \\infty$ — symmetric counterpart of Kashiwara crystal $q \\to 0$ via bar involution (algebraic fragment)",
  lean: {
    ref: "qou:QOU.IwahoriHecke.TypeA.ReverseLimitQToInfinity",
    validation: "not_checked",
  },
  uses: [
    "def:bar-involution",
    "prop:crystal-isospin-degeneracy",
  ],
  cites: [
    "kashiwara1991",
    "lusztig1990",
  ],
  tags: [
    "reverse-limit",
    "q-to-infinity",
    "duality-d13",
    "kashiwara-paired",
    "bar-paired",
    "closure-tier-b",
    "phase-2-sprint-3-discharge",
    "partial-closure-algebraic",
  ],
});
