import type { CapabilityDefinition } from "../framework/types.js";

export const llmApi: CapabilityDefinition = {
  id: "llm-api",
  name: "LLM API Access",
  description: "An Anthropic API key is available for programmatic Claude usage.",
  detection: { method: "env-var", variable: "ANTHROPIC_API_KEY" },
};
