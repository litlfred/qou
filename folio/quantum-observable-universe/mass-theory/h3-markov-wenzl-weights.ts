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
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "refined-framing",
      date: "2026-06-13",
      body:
        "Scoped to the Jones/Temperley–Lieb trace (the Borromean rings' Jones polynomial). The framework's mass/binding pipeline uses a different trace — the full-Hecke Ocneanu Markov trace (the excised convention C, z = 1/(q^{1/2}+q^{-1/2}), Wenzl Schur-principal), whose three-row weight is y_(1^3) ≠ 0 for q ≠ 1 — proven canonical in docs/audits/2026-05-05-y-lambda-tr-m-equivalence-proof.md. The two coincide at q=1 and on writhe-0 observables (so physical masses are insensitive) but diverge at q≠1. These closed forms must not be read as the general tr_M y_λ consumed by y_lambda_wenzl_bridge_numeric. Owner adjudication 2026-06-13 (full-Hecke canonical; scope the prop, do not re-normalize the pipeline).",
      see: "docs/audits/2026-06-13-wenzl-trace-normalization-prop-compute-mismatch.md",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "**The 2026-06-13 adjudication above has been reversed, and the scoping " +
        "caveat with it.** That note rests on the pipeline using a *different* " +
        "trace from this block: it scopes these closed forms to the " +
        "Jones/Temperley–Lieb trace and warns they \"must not be read as the " +
        "general tr_M y_λ\", because the pipeline ran the full-Hecke Ocneanu " +
        "trace — the excised **convention C** — with y_(1^3) ≠ 0. Its closing " +
        "instruction was \"full-Hecke canonical; scope the prop, do not " +
        "re-normalize the pipeline\". " +
        "The owner ruling of **2026-08-09** excised that trace. Production is " +
        "**convention D**, z = q^3/(q^2+1) — and convention D *is* the " +
        "Jones/Temperley–Lieb trace: the registry names it \"SU(2)/Temperley-Lieb " +
        "(Jones) decomposition\", and `thm:jones-markov-trace` records that " +
        "convention D \"lands on the Jones–Temperley–Lieb normalisation exactly\". " +
        "So every clause of the old note inverts. The pipeline no longer uses a " +
        "different trace — it uses **this** one. y_(1^3) = 0 rather than ≠ 0, and " +
        "exactly: the pin z(q^2+1) = q^3 forces it " +
        "(`TemperleyLiebTower.conventionD_kills_antisymmetriser`). The two traces " +
        "no longer \"diverge at q ≠ 1\", because only one of them is in " +
        "production. And these closed forms are no longer a scoped special case " +
        "to be kept away from `y_lambda_wenzl_bridge_numeric` — under D they are " +
        "the general ones. " +
        "The old note is kept rather than deleted: it is the record of a " +
        "superseded owner adjudication, and the 2026-06-13 audit it cites should " +
        "be read as history, not as current scope. Bean `qou-emyt`.",
    },
  ],
});
