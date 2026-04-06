import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:q-gl-fiber-functor",
  label: "rem:q-gl-automorphic-observability",
  title: "Automorphic--spectral duality as observability",
  uses: [
    "conj:q-gl-fiber-functor",
    "def:quantum-observable-universe",
    "rem:fibre-functor-rigidity",
  ],
  tags: ["geometric-langlands", "observability", "duality"],
});
