import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:q-gl-fiber-functor",
  label: "rem:q-gl-automorphic-observability",
  title: "Automorphic--spectral duality as observability",
  uses: [
    "thm:q-gl-fiber-functor",
    "def:quantum-observable-universe",
    "prop:fibre-functor-rigidity",
  ],
  tags: ["geometric-langlands", "observability", "duality"],
});
