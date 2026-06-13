import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:h3-markov-wenzl-weights",
  title:
    "Closed-form Jones/Temperley–Lieb weights on $H_3(q)$ (Borromean Jones polynomial): $y_{(3)} = [4]_q/[2]_q^3$, $y_{(2,1)} = 1/[2]_q^2$, $y_{(1^3)} = 0$",
  lean: { ref: "qou:QOU.BraidsAndKnots.h3_markov_wenzl_weights" },
  uses: [
    "prop:borromean-markov-trace-closed-form",
  ],
  cites: [
    "jones1987",
  ],
  tags: [
    "wenzl-weights",
    "markov-trace",
    "temperley-lieb",
    "q-deformation",
    "categorical-derivation",
    "closed-form",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-06-13",
      body:
        "Scoped to the Jones/Temperley–Lieb trace (the Borromean rings' Jones polynomial). The framework's mass/binding pipeline uses a different trace — the full-Hecke Ocneanu Markov trace (z = 1/(q^{1/2}+q^{-1/2}), Wenzl Schur-principal), whose three-row weight is y_(1^3) ≠ 0 for q ≠ 1 — proven canonical in docs/audits/2026-05-05-y-lambda-tr-m-equivalence-proof.md. The two coincide at q=1 and on writhe-0 observables (so physical masses are insensitive) but diverge at q≠1. These closed forms must not be read as the general tr_M y_λ consumed by y_lambda_wenzl_bridge_numeric. Owner adjudication 2026-06-13 (full-Hecke canonical; scope the prop, do not re-normalize the pipeline).",
      see: "docs/audits/2026-06-13-wenzl-trace-normalization-prop-compute-mismatch.md",
    },
  ],
});
