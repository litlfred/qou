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
  // Detangler forward-ref demote (bean foxn): def:breit-wheeler-pair-production
  // (predicted-spectra, a later chapter) is referenced only as a parenthetical
  // narrative pointer in the .md ("([pair production](#def:...))"); the
  // derivation uses its own φ₀₁=0 specialization. Demoted from a hard uses[]
  // dependency to that narrative link (which still resolves document-wide).
  uses: [],
});
