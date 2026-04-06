import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:q-ns-wellposedness",
  label: "rem:q-ns-proof-strategy",
  title: "Proof strategy: three mechanisms for $q$-deformed regularity",
  uses: [
    "thm:q-ns-wellposedness",
    "prop:kelvin-dispersion-derivation",
    "rem:planck-reynolds",
    "thm:quantum-peter-weyl",
    "prop:q-spectral-sobolev",
    "prop:q-ns-nonlinear-uniqueness",
  ],
  tags: ["proof-strategy", "regularity", "enstrophy", "UV-damping"],
});
