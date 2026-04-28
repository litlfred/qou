import { prose } from "../../schema/builders";

export default prose({
  label: "sec:q-gl-intro-prose",
  title: "Introduction to $q$-Geometric Langlands",
  uses: [
    "prop:categorical-dq-squared",
    "rem:kummer-filtration-obstruction",
    "rem:fibre-functor-rigidity",
  ],
});
