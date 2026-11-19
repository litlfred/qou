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
    {
      kind: "note",
      body:
        "Packaged in Lean as the typeclass QOU.AppendixSurreals.OSReflectionPositivity; full formalisation of OS reconstruction also requires categorical C*-completion Frobenius structures and Wightman reconstruction, neither currently in Mathlib.",
    },
  ],
});
