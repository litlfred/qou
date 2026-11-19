import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-kummer-specialisation-consequence",
  title: "Consequence for NS regularity",
  interprets: "prop:ns-kummer-specialisation",
  uses: ["thm:qu-to-qou", "prop:ns-kummer-specialisation", "thm:ns-singularity-descartes"],
  tags: ["kummer", "obstruction", "navier-stokes", "blowup"],
  authorNotes: [
    {
      kind: "deprecated",
      body: "An earlier jet-tower formulation claimed complementary-summand non-cancellation inside H^2(S, G_m) and on Sigma; retracted because H^2(S, G_m) = 0 on a closed curve and H^2(Sigma, -) = 0 on a 1D locus.",
    },
  ],
});
