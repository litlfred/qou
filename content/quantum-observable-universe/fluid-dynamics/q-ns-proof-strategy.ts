import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:q-ns-wellposedness",
  label: "rem:q-ns-proof-strategy",
  title: "Proof strategy: three mechanisms for $q$-deformed regularity",
  uses: [
    "prop:q-ns-nonlinear-uniqueness",
    "thm:quantum-peter-weyl",
  ],
  tags: ["proof-strategy", "regularity", "enstrophy", "UV-damping"],
});
