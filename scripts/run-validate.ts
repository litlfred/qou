#!/usr/bin/env bun
/**
 * Run the validation pipeline, injecting the domain-specific values registry
 * into the folio-assistant generic platform.
 */

import { resolve } from "path";
import { configureValueRegistry } from "../../FolioAssistant/content/pipeline/value-registry-di";
import { WITNESSED_VALUES, lookupValue, verifiedNames } from "../content/values/registry";
import { validateObjects } from "../../FolioAssistant/content/pipeline/validate";

// Inject the values registry
configureValueRegistry({
  WITNESSED_VALUES,
  lookupValue,
  verifiedNames,
});

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
