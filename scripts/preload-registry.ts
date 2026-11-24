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
 * reached via `../folio-assistant/`, and the root-mounted layers via `../`.
 */

import { existsSync } from "node:fs";
import { join } from "node:path";
import { WITNESSED_VALUES, lookupValue, verifiedNames } from "../folio/values/registry";
import { LEAN_PACKAGES } from "../schemas/lean-packages";

// qou reaches the platform two ways while the layer layout is adopted (owner
// ruling 2026-11-24, "1 qou is platform later"): the layers mounted at the
// repository root from index.lock.json, and the older `folio-assistant/` link.
// Each is its own module instance, so the registry is configured in every one
// that is on disk: a caller importing either finds it configured.
const ROOT = join(import.meta.dir, "..");
for (const base of [ROOT, join(ROOT, "folio-assistant")]) {
  const di = join(base, "cat-harness-tools/pipeline/value-registry-di.ts");
  const lean = join(base, "folio-assistant-sci/pipeline/lean-formal-ref.ts");
  if (!existsSync(di) || !existsSync(lean)) continue;
  const { configureValueRegistry } = await import(di);
  const { configureLeanPackages } = await import(lean);
  configureValueRegistry({ WITNESSED_VALUES, lookupValue, verifiedNames });
  configureLeanPackages(LEAN_PACKAGES);
}
