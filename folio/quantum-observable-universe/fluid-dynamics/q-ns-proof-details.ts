import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-ns-nonlinear-uniqueness",
  label: "rem:q-ns-proof-details",
  title: "Proof details: nonlinear estimates, enstrophy evolution, and uniqueness",
  uses: [
    "prop:q-ns-nonlinear-uniqueness",
    "thm:quantum-peter-weyl",
  ],
  tags: ["proof", "enstrophy", "ladyzhenskaya", "gronwall", "uniqueness"],
});
