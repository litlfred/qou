import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:madelung-fluid",
  label: "rem:madelung-divisor-topology",
  title: "Divisor topology of the wavefunction zero-locus",
  uses: ["rem:madelung-fluid", "prop:topological-decomposition-mass"],
  tags: ["divisor", "vortex", "blowup", "linking"],
});
