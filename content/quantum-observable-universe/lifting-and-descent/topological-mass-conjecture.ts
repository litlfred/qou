import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:topological-decomposition-mass",
  title: "Topological decomposition of mass (archimedean form)",
  tags: ["mass", "topological-decomposition", "divisor", "vortex"],
  uses: ["thm:topological-mass", "cor:quantum-dilogarithm"],
});
