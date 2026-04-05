import { prose } from "../../schema/builders";

export default prose({
  label: "sec:q-gl-intro-prose",
  title: "Introduction to $q$-Geometric Langlands",
  uses: [
    "def:quantum-observable-universe",
    "def:substrate-parameter",
    "prop:categorical-dq-squared",
    "def:quantum-characteristic-classes",
    "rem:kummer-filtration-obstruction",
    "rem:fibre-functor-rigidity",
  ],
});
