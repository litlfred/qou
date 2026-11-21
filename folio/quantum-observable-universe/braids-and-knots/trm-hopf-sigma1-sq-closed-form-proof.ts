import { proof } from "../../schema/builders";

export default proof({
  label: "prf:trm-hopf-sigma1-sq-closed-form",
  title: "Proof of trm hopf sigma1 sq closed form",
  uses: ["prop:trm-hopf-sigma1-sq-closed-form"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body: "The numerical check `computations/probe_F_n_categorical_derivation.py` (witness `computations/F-n-categorical-derivation-probe.witness.json`, 2/2 assertions) validated the convention-C coefficients and has not been re-run under convention D; regenerating it is a producer change. Moved out of the proof prose 2026-11-15.",
    },
  ],
});
