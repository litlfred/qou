/**
 * Preload script to inject the qou-specific values registry
 * into the generic folio-assistant pipeline.
 *
 * The platform pipeline is dependency-injected: it calls
 * `getValueRegistry()` (which throws unless `configureValueRegistry()`
 * has run) and resolves `lean.ref` URIs through the configured Lean
 * package registry. Run via `bun run --preload ../scripts/preload-registry.ts ...`
 * from `content/`; ES-module imports below resolve relative to this
 * file (repo `scripts/`), so the in-repo `folio-assistant/` symlink is
 * reached via `../folio-assistant/`.
 */

import { configureValueRegistry } from "../folio-assistant/content/pipeline/value-registry-di";
import { WITNESSED_VALUES, lookupValue, verifiedNames } from "../content/values/registry";
import { configureLeanPackages } from "../folio-assistant/schemas/lean-packages";
import { LEAN_PACKAGES } from "../schemas/lean-packages";

configureValueRegistry({
  WITNESSED_VALUES,
  lookupValue,
  verifiedNames,
});

configureLeanPackages(LEAN_PACKAGES);
