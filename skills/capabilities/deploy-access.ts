import type { CapabilityDefinition } from "../framework/types.js";

export const deployAccess: CapabilityDefinition = {
  id: "deploy-access",
  name: "Deployment Access",
  description: "SSH or API access to the deployment server for managing the remote MCP instance.",
  detection: { method: "env-var", variable: "FOLIO_DEPLOY_KEY" },
};
