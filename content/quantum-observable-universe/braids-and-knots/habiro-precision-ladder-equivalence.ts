import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-precision-ladder-equivalence",
  title:
    "Precision-ladder coefficients are Habiro integer evaluations",
  lean: {
    ref: "qou:QOU.BraidKnot.habiro_integral",
  },
  uses: [
    "thm:jones-markov-trace",
    "prop:q-schur-y-lambda-closed-form",
    "prop:mass-endomorphism-tower",
  ],
  cites: [
    "habiro2000",
    "jones1987",
    "wenzl1988",
  ],
  tags: [
    "habiro-ring",
    "precision-ladder",
    "cyclotomic-integrality",
    "1ppQ",
    "categorical-derivation",
  ],
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the existence of the Habiro expansion for quantum invariants with integer coefficients is a standard result in quantum topology, its novel application here is using the strictly finite nature of this algebraic ladder to eliminate arbitrary truncation choices in evaluating physical mass differences, anchoring the observable spectrum directly to the exact cyclotomic integrality of the trace." },
    {
      kind: "note",
      date: "2026-05-28",
      body: "**Scope note.** A historical 'precision ladder' wrote the $q$-deformed observables as a product $\\prod_k (1 + c_k (b\\hbar_q^2)^k)$ and identified per-rung coefficients $c_k$. Those $c_k$ are **not** the Taylor coefficients of the exact Habiro sum: the genuinely-derived expansion (e.g. the $\\tau_M$ form, `prop:tau-M-asymptotic-rep-theory`) is derived only at low order ($k=1$ via the Kashiwara $\\tilde f_1$ matrix element), and the higher $c_k$ used to reach experiment-grade accuracy were tuned against the experimental value, not evaluated from the integer $a_m$. They depend on the (unproven) choice of intermediate form and are excluded from the canonical chain. What this proposition asserts is only the **integrality and finiteness** of the $a_m$ — which is verified — not any bridge from the $a_m$ to those ladder $c_k$.",
    },
  ],
});
