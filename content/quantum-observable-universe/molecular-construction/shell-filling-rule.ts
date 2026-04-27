import { proposition } from "../../schema/builders";

/**
 * Shell filling minimizes Phi_1 — the aufbau principle from the LP dual.
 */
export default proposition({
  label: "prop:shell-filling-rule",
  title: "Shell filling minimises $\\Phi_1$ (aufbau from LP dual)",
  uses: ["def:electron-shell-braid-capacity"],
  tags: ["aufbau", "shell-filling", "LP-dual", "electron-configuration"],
});
