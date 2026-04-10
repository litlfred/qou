import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-scale-catalan",
  title: "Binding energy scale $\\alpha = m_e \\times 8G$",
  uses: [
    "thm:topological-mass",
    "def:borromean-baryon",
  ],
});
