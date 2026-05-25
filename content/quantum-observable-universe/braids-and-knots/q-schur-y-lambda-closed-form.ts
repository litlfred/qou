import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-schur-y-lambda-closed-form",
  title:
    "q-Schur Plancherel weights $y_\\lambda(q)$ on $H_n(q)$ — closed form via $q$-content principal specialization",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.QSchurYLambdaClosedForm",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-normal-form",
    "def:bar-involution",
  ],
  cites: [
    "wenzl1988",
    "jones1987",
    "macdonald1979",
  ],
  tags: [
    "q-schur",
    "closed-form",
    "markov-trace",
    "principal-specialization",
    "content-sum",
    "axiom-class",
    "non-scholarly-voice-exception",
  ],
});
