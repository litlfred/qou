#!/usr/bin/env bun
/**
 * Where qou reads and writes a block's QA verdict, after the split.
 *
 * Owner ruling 2026-10-10 (issue #7642): block QA splits the way the platform
 * splits it. The two halves now live in two places:
 *
 * - the DERIVED report (`block-qa/v1`) at
 *   `test/results/block-qa/<repo-relative block root>.qa.json`. That directory
 *   is gitignored. Its durable copy is the `cat/cat-harness/qa-reports` branch,
 *   keyed by commit. Fetch it before reading:
 *   `bun run folio-assistant/cat-harness/scripts/qa-store.ts fetch --ref main`;
 * - the JUDGEMENTS (every entry whose `reviewer.kind` is not `script`) in
 *   `test/attestations/block-qa/<same mirror>.attestations.json`
 *   (`qa-attestations/v1`). These stay on main.
 *
 * Before the split, every qou script built `<root>.qa.json` beside the block by
 * hand. At the current platform pin, `qa-sweep` already wrote to the results
 * tree, while those qou scripts kept reading the sibling. So a sweep refreshed
 * nothing the scripts could see, and once a results file existed, any verdict
 * appended to the sibling was hidden from the platform. This module removes
 * that split-brain by giving qou the platform's own answer. It does not
 * re-derive any rule:
 *
 * - paths come from `qa-paths.ts` (`blockQaPath`, `existingBlockQaPath`);
 * - the judgement half is written through `resolvePrior` + `finalizeCriteria`
 *   (`schemas/qa-attestations.ts`), the same calls `qa-sweep` makes. So a
 *   judgement reaches the store, is read back, and only then is the derived
 *   projection saved.
 *
 * CLI, for the Python writers, which are not given a second implementation:
 *
 *   bun folio/pipeline/block-qa-io.ts path  <block root|.ts|.md>          # print the read path (or nothing)
 *   bun folio/pipeline/block-qa-io.ts save  <block root|.ts|.md> <report.json> [--mode attesting|script]
 *   bun folio/pipeline/block-qa-io.ts list  [<dir under the repo>]        # one "<block root>\t<report path>" per line
 *
 * `save` exits 0 when written, 1 when the attestation store refused (nothing
 * written), and 2 on usage errors.
 *
 * @module folio/pipeline/block-qa-io
 */
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";

import { blockQaPath, existingBlockQaPath, findContentRepoRoot, BLOCK_QA_RESULTS_DIR, BLOCK_QA_SUFFIX } from "../../folio-assistant/cat-harness/content/pipeline/qa-paths.ts";
import { loadQaReport, saveQaReport } from "../../folio-assistant/cat-harness/content/pipeline/qa-utils.ts";
import { blockAttestationKey, finalizeCriteria, refusalLine, resolvePrior } from "../../folio-assistant/cat-harness/schemas/qa-attestations.ts";

/** The qou checkout root (this file is `folio/pipeline/block-qa-io.ts`). */
export const REPO_ROOT = resolve(import.meta.dir, "..", "..");

/** `foo.md`, `foo.ts`, `foo.qa.json` or `foo` -> the absolute block root `…/foo`. */
export function blockRootOf(p: string): string {
  const abs = resolve(p);
  for (const ext of [BLOCK_QA_SUFFIX, ".md", ".ts", ".lean"]) if (abs.endsWith(ext)) return abs.slice(0, -ext.length);
  return abs;
}

/**
 * The instance a block belongs to: the nearest ancestor that holds `.git` or an
 * instance declaration (`qou.json`), which is the platform's own rule. For a
 * block in this checkout that is {@link REPO_ROOT}. For a throwaway block
 * outside any instance (the tests) it is the block's own directory, so nothing
 * is written outside the block's tree.
 */
export function instanceRootOf(blockRoot: string): string {
  const root = blockRootOf(blockRoot);
  return findContentRepoRoot(root, dirname(root));
}

/** Where a NEW verdict is written: always the results tree, never the sibling. */
export function blockQaWritePath(blockRoot: string): string {
  const root = blockRootOf(blockRoot);
  return blockQaPath(instanceRootOf(root), root);
}

/**
 * The verdict to READ: the results tree first, then the legacy sibling, or
 * `undefined` when neither exists. An `undefined` result is only "unaudited"
 * if the results tree has been fetched; see {@link resultsTreePresent}.
 */
export function blockQaReadPath(blockRoot: string): string | undefined {
  const root = blockRootOf(blockRoot);
  return existingBlockQaPath(instanceRootOf(root), root);
}

/**
 * Has this checkout got a results tree at all? When it has not, every reader
 * would see no verdicts at all and report the corpus as clean. That is the
 * `dh4f` defect, so a reader must say so instead of passing.
 */
export function resultsTreePresent(): boolean {
  const d = join(REPO_ROOT, BLOCK_QA_RESULTS_DIR);
  return existsSync(d) && readdirSync(d).length > 0;
}

export const FETCH_HINT =
  "no block-QA results tree in this checkout (test/results/block-qa is empty). Fetch it first: " +
  "bun run folio-assistant/cat-harness/scripts/qa-store.ts fetch --ref main";

/**
 * Every block verdict under `dir`, as (block root, report path) pairs, read the
 * way {@link blockQaReadPath} reads: a results-tree report shadows a legacy
 * sibling for the same block.
 */
export function listBlockQa(dir: string = join(REPO_ROOT, "folio")): Array<{ blockRoot: string; path: string }> {
  const out = new Map<string, string>();
  const walk = (d: string, f: (abs: string) => void) => {
    let names: string[];
    try {
      names = readdirSync(d);
    } catch {
      return;
    }
    for (const n of names.sort()) {
      if (n === "node_modules" || n.startsWith(".")) continue;
      const abs = join(d, n);
      let isDir = false;
      try {
        isDir = statSync(abs).isDirectory();
      } catch {
        continue;
      }
      if (isDir) walk(abs, f);
      else if (n.endsWith(BLOCK_QA_SUFFIX) && !n.endsWith(".script-qa.json")) f(abs);
    }
  };
  const absDir = resolve(dir);
  const results = join(REPO_ROOT, BLOCK_QA_RESULTS_DIR);
  walk(join(results, relative(REPO_ROOT, absDir)), (abs) => {
    const root = join(REPO_ROOT, relative(results, abs).slice(0, -BLOCK_QA_SUFFIX.length));
    out.set(root, abs);
  });
  walk(absDir, (abs) => {
    const root = abs.slice(0, -BLOCK_QA_SUFFIX.length);
    if (!out.has(root)) out.set(root, abs);
  });
  return [...out.entries()].map(([blockRoot, path]) => ({ blockRoot, path })).sort((a, b) => a.blockRoot.localeCompare(b.blockRoot));
}

/** The block's current report (results tree, else sibling), or `undefined`. */
export function loadBlockQa(blockRoot: string): any | undefined {
  const p = blockQaReadPath(blockRoot);
  return p ? loadQaReport(p) : undefined;
}

/**
 * Save a block's report the split way. `attesting` (the default) means the
 * writer added or changed a judgement: its non-script entries go to the store
 * first and are read back. `script` means it only touched script entries, so
 * the judgement half is taken from the store whatever the report says.
 *
 * Returns the derived path written, or a refusal line, in which case NOTHING
 * was written.
 */
export function saveBlockQa(
  blockRoot: string,
  report: any,
  mode: "attesting" | "script" = "attesting",
): { ok: true; path: string } | { ok: false; reason: string } {
  const root = blockRootOf(blockRoot);
  const prior = loadBlockQa(root);
  const inst = instanceRootOf(root);
  const res = resolvePrior(inst, blockAttestationKey(inst, root), prior);
  if (!res.ok) return { ok: false, reason: refusalLine("block-qa-io", relative(inst, root), res) };
  report.criteria = finalizeCriteria(res, report.criteria ?? {}, mode);
  const path = blockQaWritePath(root);
  saveQaReport(path, report);
  return { ok: true, path };
}

if (import.meta.main) {
  const [cmd, a, b, ...rest] = process.argv.slice(2);
  if (cmd === "path" && a) {
    const p = blockQaReadPath(a);
    if (p) console.log(p);
    process.exit(0);
  }
  if (cmd === "list") {
    if (!resultsTreePresent()) console.error(`block-qa-io: WARNING ${FETCH_HINT}`);
    for (const { blockRoot, path } of listBlockQa(a ?? join(REPO_ROOT, "folio"))) console.log(`${blockRoot}\t${path}`);
    process.exit(0);
  }
  if (cmd === "save" && a && b) {
    const mi = rest.indexOf("--mode");
    const mode = (mi >= 0 ? rest[mi + 1] : "attesting") as "attesting" | "script";
    if (mode !== "attesting" && mode !== "script") {
      console.error(`block-qa-io: --mode must be attesting|script, got ${mode}`);
      process.exit(2);
    }
    const r = saveBlockQa(a, JSON.parse(readFileSync(b, "utf-8")), mode);
    if (!r.ok) {
      console.error(r.reason);
      process.exit(1);
    }
    console.log(r.path);
    process.exit(0);
  }
  console.error("usage: block-qa-io.ts path <block> | list [dir] | save <block> <report.json> [--mode attesting|script]");
  process.exit(2);
}
