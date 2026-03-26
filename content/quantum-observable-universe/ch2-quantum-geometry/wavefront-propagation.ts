import { remark } from "../../schema/builders";

export default remark({
  label: "rem:wavefront-propagation",
  title: "Wavefront propagation and the categorical Dirac equation",
  tags: ["wavefront", "dirac", "propagation", "photon", "instanton"],
  uses: [
    "def:categorical-dirac-operator",
    "def:categorical-lagrangian",
    "prop:variational-equations",
    "def:categorical-instanton",
  ],
});
