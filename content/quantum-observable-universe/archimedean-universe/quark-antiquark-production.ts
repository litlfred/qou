import { definition } from "../../schema/builders";

export default definition({
  label: "def:quark-antiquark-production",
  title: "Quark--antiquark production from pair creation",
  tags: [
    "quark",
    "antiquark",
    "pair-production",
    "hopf-link",
    "meson",
    "hecke-algebra",
    "colored-photon",
  ],
  lean: { ref: "qou:QOU.Archimedean.QuarkAntiquarkProduction",
    validation: "not_checked",
  },
  uses: ["def:breit-wheeler-pair-production"],
});
