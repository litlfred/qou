import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:os-reflection-positivity-from-reeb",
  title:
    "Osterwalder--Schrader reflection positivity from the Reeb $\\mathbb{Z}_2$",
  lean: {
    ref: "qou:QOU.AppendixSurreals.OSReflectionPositivity",
    validation: "not_checked",
  },
  uses: [
    "prop:reeb-u1-chart-swap",
    "thm:categorical-reeb-exists",
    "def:contact-affine-chart",
    "def:frobenius-hopf-substrate",
    "def:archimedean-realization-functor",
    "rem:yang-mills-surreal-bound",
    "thm:quantum-gap-collapse",
    "rem:kashaev-as-archimedean-realization",
  ],
  cites: [
    "osterwalder1973",
    "osterwalder1975",
    "glimm1981",
    "faddeev1994",
  ],
  tags: [
    "tier:S",
    "yang-mills",
    "mass-gap",
    "millennium-problem",
    "wightman-axioms",
    "osterwalder-schrader",
    "reflection-positivity",
    "reeb",
    "open-problem",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): 3. **Mathlib infrastructure.** A complete proof requires a Frobenius structure on the categorical $C^*$-completion and the Wightman reconstruction theorem—neither in Mathlib today. The conjecture is packaged as the typeclass `QOU.AppendixSurreals.OSReflectionPositivity`, with one field stating the positivity inequality. Granting the class instance, the surreal bound completes OS reconstruction." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This follow-up programme is stated as [Wenzl positivity at $q_0$ implies substrate $C^*$-Frobenius positivity](#conj:wenzl-positivity-implies-substrate-positivity). Closing that bridge conjecture makes the substrate axiom derived from Wenzl's classical result, discharging the OS-reflection-positivity-as-axiom assumption." },
  ],
});
