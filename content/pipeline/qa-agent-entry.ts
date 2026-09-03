#!/usr/bin/env bun
/**
 * Append an agent (or human) reviewer entry to a block's QA sidecar.
 *
 * The adjudication counterpart of the script scanners: a sub-agent that
 * has read a block in full records its verdict per criterion without
 * hand-editing JSON. Entries are APPENDED to the criterion's array
 * (script candidates are preserved; the freshest entry whose field_hash
 * matches the current sources wins, per the block-qa/v1 convention).
 *
 *   bun run content/pipeline/qa-agent-entry.ts \
 *     --block   <path to block .md>            (required)
 *     --criterion <criterion-id>               (required)
 *     --result  pass|fail|warn|n/a             (required)
 *     [--severity critical|major|minor]
 *     [--evidence "<what was found / why the verdict>"]
 *                                              (REQUIRED for fail|warn)
 *     [--notes    "<fix applied / fix proposed / scope note>"]
 *     [--id       <reviewer id>]               (default: agent:session)
 *
 * The field_hash is computed from the block's CURRENT .md/.ts content,
 * so run this AFTER any prose fix, and the entry certifies the fixed
 * state.
 *
 * @module content/pipeline/qa-agent-entry
 */
import { createHash } from "node:crypto";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { basename, dirname, join } from "node:path";

function arg(name: string): string | undefined {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

const blockMd = arg("block");
const criterion = arg("criterion");
const result = arg("result");
const severity = arg("severity");
const evidence = arg("evidence");
const notes = arg("notes");
const reviewerId = arg("id") ?? "agent:session";

if (!blockMd || !criterion || !result) {
  console.error(
    "usage: qa-agent-entry.ts --block <block.md> --criterion <id> " +
      "--result pass|fail|warn|n/a [--severity ...] " +
      "[--evidence ...] (required for fail|warn) " +
      "[--notes ...] [--id ...]",
  );
  process.exit(2);
}
if (!["pass", "fail", "warn", "n/a"].includes(result)) {
  console.error(`invalid --result: ${result}`);
  process.exit(2);
}
// A verdict that asserts a violation must say what it found. The block-qa/v1
// schema already states this on `result` ("fail = violated (evidence must cite
// file:line + verbatim quote)") but never enforced it, so 1302 fail/warn
// entries carry an empty evidence string and assert a failure that is nowhere
// on record. This is the agent-side counterpart of the rule already pinned for
// script checkers: a checker that cannot read its evidence has not verified
// anything.
//
// The bar is deliberately NON-EMPTY, not quote-shaped. Some legitimate
// evidence is a bare `file.lean:1` pointer, and demanding a verbatim quote
// would push authors toward inventing one.
//
// `pass` and `n/a` are exempt on purpose: a verdict that found nothing has
// nothing to quote, and requiring evidence there would push the sweep toward
// empty ceremony from the other side.
if ((result === "fail" || result === "warn") && !evidence?.trim()) {
  console.error(
    `--result ${result} requires --evidence: a verdict that asserts a ` +
      `violation must cite what it found (file:line + quote where possible).`,
  );
  process.exit(2);
}
if (!existsSync(blockMd)) {
  console.error(`no such block .md: ${blockMd}`);
  process.exit(2);
}

const dir = dirname(blockMd);
const root = basename(blockMd, ".md");
const tsPath = join(dir, `${root}.ts`);
const leanPath = join(dir, `${root}.lean`);
const qaPath = join(dir, `${root}.qa.json`);

const sha12 = (s: string) =>
  createHash("sha256").update(s).digest("hex").slice(0, 12);

let reviewedSha = "unknown";
try {
  reviewedSha = execFileSync("git", ["rev-parse", "HEAD"]).toString().trim();
} catch {
  /* ignore */
}

let doc: any = {};
if (existsSync(qaPath)) {
  try {
    doc = JSON.parse(readFileSync(qaPath, "utf8"));
  } catch {
    console.error(`unparseable sidecar (fix by hand first): ${qaPath}`);
    process.exit(1);
  }
}
doc.$schema ??= "block-qa/v1";
doc.criteria ??= {};
doc.criteria[criterion] ??= [];

// Hash every sibling that exists, `.lean` included.  A criterion that reads the
// Lean -- `da-lean-narrative-divergence`, `da-vacuous`, `da-circular`,
// `wall-side-correct`, `proof-statement-integrity` -- is not resolvable against
// a block version unless the `.lean` is in its staleness key, so without this a
// verdict about the Lean survives arbitrary later edits to that Lean.
//
// SCOPE, measured 2026-08-29, because the obvious reading over-states it: this
// is a LATENT bug, not the explanation for any live incident.  Across all 3,617
// sidecars, on Lean-reading criteria, agent verdicts that carry a field_hash on
// blocks that have a `.lean`: 114 already record the key, 4 do not (all
// `proof-statement-integrity`).  The other writers get it right; this entry
// point is simply the one whose code does not.
//
// In particular this did NOT cause the em-coupling incident that prompted the
// look (bean `qou-aemx`).  Those `da-lean-narrative-divergence` verdicts carry
// NO field_hash at all -- they come from `local/qa-agent-drain`, which is the
// separate defect tracked in `qou-pwut`, and which this change does not touch.
const entry: any = {
  field_hash: {
    md: sha12(readFileSync(blockMd, "utf8")),
    ...(existsSync(tsPath) ? { ts: sha12(readFileSync(tsPath, "utf8")) } : {}),
    ...(existsSync(leanPath) ? { lean: sha12(readFileSync(leanPath, "utf8")) } : {}),
  },
  result,
  reviewer: { kind: "agent", id: reviewerId, version: "v1" },
  reviewed_at: new Date().toISOString(),
  reviewed_sha: reviewedSha,
};
if (severity) entry.severity = severity;
if (evidence?.trim()) entry.evidence = evidence;
if (notes) entry.notes = notes;

doc.criteria[criterion].push(entry);
doc.updated_at = entry.reviewed_at;
writeFileSync(qaPath, JSON.stringify(doc, null, 2) + "\n");
console.log(`${qaPath}: ${criterion} <- agent ${result}`);
