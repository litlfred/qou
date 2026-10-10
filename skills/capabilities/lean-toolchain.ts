import type { CapabilityDefinition } from "../framework/types.js";

export const leanToolchain: CapabilityDefinition = {
  id: "lean-toolchain",
  name: "Lean 4 Toolchain",
  description: "Lean 4 compiler and Lake build system are installed and match the project toolchain.",
  detection: { method: "command", command: "lean --version" },
};
