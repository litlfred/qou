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
import { configureValueRegistry } from "../folio-assistant/cat-harness-tools/pipeline/value-registry-di";
import { configureReferenceRegistry } from "../folio-assistant/cat-harness-tools/pipeline/references-registry-di";
import { WITNESSED_VALUES, lookupValue, verifiedNames } from "../folio/values/registry";
import { configureChapterProfiles } from "../folio-assistant/cat-harness-tools/pipeline/chapter-profile-registry-di";
import {
  CHAPTER_EXPECTED_REGIMES, CATEGORICAL_CHAPTERS, ARCHIMEDEAN_CHAPTERS,
  TERMS_NEEDING_DEFINITIONS, LEAN_MODULE_CHAPTERS,
} from "../folio/values/chapter-profiles";
import { configureLeanPackages } from "../folio-assistant/folio-assistant-sci/pipeline/lean-formal-ref";
import { LEAN_PACKAGES } from "../schemas/lean-packages";
import { validateObjects } from "../folio-assistant/cat-harness-tools/pipeline/validate";

// Inject the domain-specific registries into the generic platform.
configureValueRegistry({
  WITNESSED_VALUES,
  lookupValue,
  verifiedNames,
});
configureLeanPackages(LEAN_PACKAGES);
// qou's chapter profiles (bean folio-assistant-saqd). The platform's checker
// module registers its own copy when it loads; this call runs after that
// import, and the last call wins.
configureChapterProfiles({
  chapterExpectedRegimes: CHAPTER_EXPECTED_REGIMES,
  categoricalChapters: CATEGORICAL_CHAPTERS,
  archimedeanChapters: ARCHIMEDEAN_CHAPTERS,
  termsNeedingDefinitions: TERMS_NEEDING_DEFINITIONS,
  leanModuleChapters: LEAN_MODULE_CHAPTERS,
});

const args = process.argv.slice(2);
const strict = args.includes("--strict");
const positional = args.filter(a => !a.startsWith("--"));
const dir = resolve(positional[0] || "folio/quantum-observable-universe");

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
 * `folio/schema/references.ts`, so a syntactically broken bibliography —
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
  const bib = await import("../folio/schema/references");
  const n = bib.references?.length ?? 0;
  if (n === 0) {
    console.error("  ✗ folio/schema/references.ts parsed but holds no entries");
    process.exit(1);
  }
  // Hand the loaded bibliography to the platform's registry (was --strict only until 2026-11-21).
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
  //
  // And do not read the 13 as one defect. Measured by importing this module
  // (810 entries) rather than grepping for a spelling, they split two ways:
  //
  //   * TEN keys appear ONLY in `.ts` cites[] arrays -- zero in any .md prose,
  //     zero in any Lean `-- Ref:`. They support no written claim, so nothing a
  //     reader sees is broken; they are metadata whose key was never added.
  //   * `manuscript` is a different thing entirely: AGENTS.md §1 instructs
  //     authors to use `[manuscript]` when no published reference exists, and
  //     4436 Lean `-- Ref:` sites do exactly that -- against a key that is not
  //     among the 810. The work it means IS held, as `leitner2026`.
  //
  // So the second class is a convention with no backing, not a typo, and its
  // fix is a decision (alias entry vs. re-key the convention) rather than
  // research. Both are recorded in bean `qou-cite`.
  // UN-GATED 2026-11-21 (bean qou-cite, step 4 of its own plan): every cites[]
  // key in folio/quantum-observable-universe now resolves, measured under
  // --strict at platform 82b3899 with zero cites-resolve issues, so the check
  // runs on every validate. The history below is why it was gated.
  configureReferenceRegistry({
    references: bib.references,
    referenceMap: bib.referenceMap,
    CSLEntrySchema: bib.CSLEntrySchema,
  });
  console.log(`  bibliography: ${n} entries, parses; registry configured (cites-resolve ON)\n`);
} catch (err) {
  console.error("  ✗ folio/schema/references.ts DOES NOT PARSE — every citation "
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
