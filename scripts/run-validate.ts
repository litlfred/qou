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
import { realpathSync } from "fs";
import { execFileSync } from "child_process";
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

/**
 * Resolve the platform (`folio-assistant`) commit actually being used.
 *
 * The checkers live in the separate `litlfred/folio-assistant` repo, reached
 * through an unpinned symlink that `scripts/setup-folio-assistant.sh` points at
 * a sibling clone of the DEFAULT branch. So the issue count this script prints
 * is a function of *two* inputs — the corpus and the platform — and only one of
 * them is visible in `git log`.
 *
 * Observed 2026-08-08: the same corpus commit (`455013fcf5`) reported
 * `10 issue(s)` against platform `e1030e8` and `29 issue(s)` against `e3c2d6b`,
 * on one machine in one session. Neither run was wrong; the baseline simply was
 * not well-defined, and two agents spent effort disagreeing about it. Printing
 * the SHA makes every quoted baseline self-describing. See bean `vbase` — the
 * real fix is to pin the platform, which this does not do.
 */
function platformVersion(): string {
  try {
    const link = realpathSync(resolve(import.meta.dir, "../folio-assistant"));
    const sha = execFileSync("git", ["-C", link, "rev-parse", "--short", "HEAD"], {
      encoding: "utf-8",
      stdio: ["ignore", "pipe", "ignore"],
    }).trim();
    return sha ? `${sha} (${link})` : `unknown (${link})`;
  } catch {
    return "unknown — could not resolve folio-assistant";
  }
}

console.log(`Validating content objects in: ${dir}${strict ? " [strict]" : ""}`);
console.log(`  platform (folio-assistant): ${platformVersion()}\n`);

/**
 * The bibliography has to PARSE before anything else is worth reporting.
 *
 * `validateObjects` checks content blocks and never imports
 * `content/schema/references.ts`, so a syntactically broken bibliography —
 * every `\cite{}` in the paper unresolvable, `references.bib`
 * un-regenerable — was reported as "✓ Valid". Measured by breaking it on
 * purpose: `bun` refused the file with `Expected ";"` while this script
 * printed `Valid — 27 issue(s)` (bean qou-3vgs).
 *
 * One dynamic import settles it, because importing is exactly what fails.
 * Counting the entries as well, since a file that parses to an empty array
 * would also pass a bare import.
 */
try {
  const bib = await import("../content/schema/references");
  const n = bib.references?.length ?? 0;
  if (n === 0) {
    console.error("  ✗ content/schema/references.ts parsed but holds no entries");
    process.exit(1);
  }
  console.log(`  bibliography: ${n} entries, parses\n`);
} catch (err) {
  console.error("  ✗ content/schema/references.ts DOES NOT PARSE — every citation "
    + "in the paper is unresolvable until this is fixed:");
  console.error(`    ${err instanceof Error ? err.message : String(err)}`);
  process.exit(1);
}

const result = await validateObjects(dir, { strict });

for (const issue of result.issues) {
  const icon = issue.level === "error" ? "✗" : issue.level === "warning" ? "⚠" : "ℹ";
  const file = issue.file ? ` (${issue.file})` : "";
  console.log(`  ${icon} [${issue.block}]${file}: ${issue.message}`);
}

console.log(`\n${result.valid ? "✓ Valid" : "✗ Invalid"} — ${result.issues.length} issue(s)`);
process.exit(result.valid ? 0 : 1);
