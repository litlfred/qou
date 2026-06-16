/**
 * Preload script to inject the qou-specific values registry
 * into the generic FolioAssistant pipeline.
 */

import { configureValueRegistry } from "../../FolioAssistant/content/pipeline/value-registry-di";
import { WITNESSED_VALUES, lookupValue, verifiedNames } from "../content/values/registry";
import { configureLeanPackages } from "../../FolioAssistant/schemas/lean-packages";
import { LEAN_PACKAGES } from "../schemas/lean-packages";

configureValueRegistry({
  WITNESSED_VALUES,
  lookupValue,
  verifiedNames,
});

configureLeanPackages(LEAN_PACKAGES);
