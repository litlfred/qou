import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:y-lambda-closed-form-wenzl-bridge",
  title:
    "Closed form for Jones-Markov $y_\\lambda$ via Wenzl Schur-element bridge ($Q = q^2$, $z_{\\mathrm{GL}} = q z$)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.y_lambda_closed_form_wenzl_bridge",
    validation: "not_checked",
  },
  uses: [
    // conj:alpha-k-derivation-procedure removed (qou-tm3c): the closed form is Wenzl's Schur-element formula (wenzl1988, orellana1998) with Chlouveraki's uniqueness; it avoids the linear-system route that conjecture describes.
  ],
  cites: ["wenzl1988", "orellana1998", "chlouveraki2016"],
  tags: [
    "y-lambda",
    "schur-element",
    "wenzl",
    "orellana",
    "convention-bridge",
    "closed-form",
    "q-rational",
    "principal-specialization",
  ],
});
