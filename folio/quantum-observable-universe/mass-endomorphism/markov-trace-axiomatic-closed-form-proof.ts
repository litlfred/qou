import { proof } from "../../schema/builders";

export default proof({
  label: "prf:markov-trace-axiomatic-closed-form",
  title: "Proof of markov trace axiomatic closed form",
  uses: ["prop:markov-trace-axiomatic-closed-form"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-26",
      body:
        "The numerical witness in this proof was **convention C** (`z = sqrt(q)/(q+1)`) " +
        /* <!-- literal-source: excised convention-C evaluation of Step-4 closed form at muon pin --> */
        "evaluated at the **muon** pin: `tr_M ~ 1.63315357`, giving " +
        "`rho_p^CODATA ~ 1124.3`. The statement block had already been " +
        "migrated to convention D at the proton pin (`1.88432`, `974.44`), so the proof " +
        "contradicted the theorem it proves by 15%. Both numbers are reproduced exactly " +
        "by this block's own Step-4 closed form under the respective `z`, which is what " +
        "identifies the cause as the convention rather than a stale evaluation: " +
        "`z_C = 0.499320334184 -> 1.63315337745` and `z_D = 0.612688037146 -> 1.88431946725`. " +
        "Migrated to D-at-proton; cross-checked against the production witness " +
        "`option-b-proton-mass-full-chain.witness.json` (`tr_M_at_q0.proton = " +
        "1.884319467254976`), which agrees to 12 digits. The superseded `char_fast` " +
        "paragraph (`~ 1.6334`, \"matches to 4 significant digits\", attributing " +
        "the gap to seminormal roundoff) was removed: it described agreement between two " +
        "convention-C evaluations, and the statement already records the seminormal " +
        "route's agreement under D.",
      see: "docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md",
    },
  ],
  computation: {
    engine: "sympy",
    script: "computations/option_b_proton_mass_full_chain.py",
    witness: [
      "computations/option-b-proton-mass-full-chain.witness.json",
      "computations/markov/markov-trace-axiomatic-multi-atom.witness.json",
      "computations/markov/markov-trace-atomic-proton-full.witness.json",
      "computations/markov/markov-trace-recursive.witness.json",
      "computations/probes/markov-reduction-h3-to-h4-conventions.witness.json",
      "computations/probes/trm-proton-five-values-census.witness.json",
    ],
    status: "verified",
  },
});
