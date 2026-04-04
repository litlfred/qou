import { example } from "../../schema/builders";

export default example({
  label: "ex:torus-ns-regular",
  title: "The torus quantum universe: $\\chi(A) = 0$ and NS regularity",
  uses: [
    "def:ns-obstruction",
    "def:quantum-universe",
    "prop:ns-kummer-specialisation",
    "thm:ns-singularity-descartes",
  ],
  tags: [
    "example",
    "torus",
    "euler-characteristic",
    "ns-regular",
    "contrast",
  ],
});
