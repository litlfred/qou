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
import { configureReferenceRegistry } from "../folio-assistant/content/pipeline/references-registry-di";
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
  // Hand the loaded bibliography to the platform's registry — UNDER --strict ONLY.
  //
  // Without this, `cites-resolve` NO-OPS ("no reference registry configured")
  // and every `cites[]` entry goes unvalidated against `references.ts`. The
  // three members below are exactly `ReferenceRegistryAPI`, and this file
  // already has them loaded for the parse check above.
  //
  // Why --strict and not always: the check has NEVER run in this folio, and its
  // first run finds 13 unresolved citation keys across 10 blocks. Configuring it
  // unconditionally would take the default `run-validate` from `Valid — 14` to
  // `Invalid — 23` for everyone, on a backlog nobody has triaged. Several of the
  // 13 look like wrong-year typos of held entries (`dimofte-gaiotto-gukov2014`
  // vs the held `…2013`) and others are plainly distinct works (`macdonald1971`
  // "Spherical Functions" vs the held `macdonald1995`), so the fix is per-citation
  // research, not a rename sweep — repointing a citation at a different paper is
  // worse than a broken link. Bean `qou-cite`.
  //
  // Measured under --strict (platform 21498cc): 288 issues with the registry
  // forced off, 297 with it on. That is +9 for ten new citation lines, because
  // configuring the registry also SILENCES the `ℹ no reference registry
  // configured` line, which was itself being counted. 288 − 1 + 10 = 297.
  //
  // Do not read 297 as the citation debt: --strict also enables
  // `term-mention-coverage`, and 288 of the 297 are unwrapped glossary mentions
  // with no relation to citations.
  if (strict) {
    configureReferenceRegistry({
      references: bib.references,
      referenceMap: bib.referenceMap,
      CSLEntrySchema: bib.CSLEntrySchema,
    });
  }
  console.log(`  bibliography: ${n} entries, parses`
    + (strict ? "; registry configured (cites-resolve ON)" : "") + "\n");
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
