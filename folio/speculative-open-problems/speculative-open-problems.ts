import { paper, chapterRef } from "../schema/builders";

/**
 * Speculative Formulations of Classical Open Problems in the Quantum Observable Universe.
 *
 * Companion document recording speculative problem framings, dictionary
 * analogies, and surreal-number heuristics for the Yang--Mills, Riemann,
 * Birch--Swinnerton-Dyer, P versus NP, and Collatz problems, separated from
 * the proved algebra of On the Mechanics of Quantum Observable Universes.
 */
export default paper({
  title:
    "Speculative Formulations of Classical Open Problems in the Quantum Observable Universe",
  authors: ["Frederick Carl Leitner"],
  affiliations: [],
  date: "2026-11-28",
  abstract:
    "This companion paper collects the speculative formulations of five classical " +
    "open problems within the Quantum Observable Universe (QOU) framework: the " +
    "Yang--Mills existence and mass gap problem, the Riemann hypothesis, the " +
    "Birch and Swinnerton-Dyer conjecture, the P versus NP problem, and the " +
    "Collatz problem, together with cross-problem surreal-number and " +
    "Kummer-obstruction comparison tables. None of these formulations proves, " +
    "settles, or reduces the corresponding classical problem. Proved algebraic " +
    "identities---crossing-energy positivity, finite-field Hasse--Weil bounds, " +
    "categorical Hom-group vanishing, matrix-word trace complexity, Laurent " +
    "polynomial cycle classification, and surreal order inequalities---remain " +
    "in the main monograph under neutral mathematical names. Each chapter here " +
    "separates those established algebraic facts from the unproved dictionary " +
    "identifications, cost-model choices, and standard-part hypotheses that " +
    "would be needed to connect them to the classical open problems.",
  macros: {
    nn:    { tex: "\\mathfrak{n}",  unicode: "$\\mathfrak{n}$" },
    frakr: { tex: "\\mathfrak{r}",  unicode: "𝔯" },
    frakg: { tex: "\\mathfrak{g}",  unicode: "𝔤" },
    frakb: { tex: "\\mathfrak{b}",  unicode: "𝔟" },
    frakI: { tex: "\\mathfrak{I}",  unicode: "ℑ" },
    frakK: { tex: "\\mathfrak{K}",  unicode: "𝔎" },
    frakP: { tex: "\\mathfrak{P}",  unicode: "𝔓" },
    ordw:  { tex: "{\\mathrm{ord}_{\\omega}}",  unicode: "ord_ω" },
  },
  chapters: [
    chapterRef({ dir: "introduction" }),
    chapterRef({ dir: "yang-mills-framing" }),
    chapterRef({ dir: "riemann-hypothesis-framing" }),
    chapterRef({ dir: "birch-swinnerton-dyer-framing" }),
    chapterRef({ dir: "p-vs-np-framing" }),
    chapterRef({ dir: "collatz-framing" }),
    chapterRef({ dir: "cross-problem-unification" }),
  ],
});
