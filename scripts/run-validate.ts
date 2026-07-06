#!/usr/bin/env bun
/**
 * Run the validation pipeline, injecting the domain-specific values registry
 * into the folio-assistant generic platform.
 *
 * Standalone alternative to `bun run validate`; resolves the in-repo
 * `folio-assistant/` symlink via `../folio-assistant/` (imports are relative
 * to this file in repo `scripts/`).
 */

import { resolve } from "path";
import { configureValueRegistry } from "../folio-assistant/content/pipeline/value-registry-di";
import { WITNESSED_VALUES, lookupValue, verifiedNames } from "../content/values/registry";
import { configureLeanPackages } from "../folio-assistant/schemas/lean-packages";
import { LEAN_PACKAGES } from "../schemas/lean-packages";
import { validateObjects } from "../folio-assistant/content/pipeline/validate";

// Inject the domain-specific registries into the generic platform.
configureValueRegistry({
  WITNESSED_VALUES,
  lookupValue,
  verifiedNames,
});
configureLeanPackages(LEAN_PACKAGES);

const args = process.argv.slice(2);
const strict = args.includes("--strict");
const positional = args.filter(a => !a.startsWith("--"));
const dir = resolve(positional[0] || "content/quantum-observable-universe");

console.log(`Validating content objects in: ${dir}${strict ? " [strict]" : ""}\n`);

const result = await validateObjects(dir, { strict });

for (const issue of result.issues) {
  const icon = issue.level === "error" ? "✗" : issue.level === "warning" ? "⚠" : "ℹ";
  const file = issue.file ? ` (${issue.file})` : "";
  console.log(`  ${icon} [${issue.block}]${file}: ${issue.message}`);
}

console.log(`\n${result.valid ? "✓ Valid" : "✗ Invalid"} — ${result.issues.length} issue(s)`);
process.exit(result.valid ? 0 : 1);
