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
import { basename, dirname, join, resolve } from "node:path";

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
const qaPath = join(dir, `${root}.qa.json`);

const REPO_ROOT = resolve(import.meta.dir, "..", "..");

/**
 * The block's Lean file: the sibling when it exists, else the library file
 * its `lean.ref` names.
 *
 * The sibling-only version of this was a silent no-op on every block whose
 * Lean lives at the Lake path. Measured on `main` 2026-09-03, over blocks
 * carrying a `qou:` ref: **867 have a sibling `.lean`** (hashed correctly)
 * and **390 do not**, of which **180 have a library file at the ref**. On
 * those 180 the entry omitted `lean`/`lean_statement` entirely, so a verdict
 * on a Lean-reading criterion could never be fresh — `entryIsFresh` sees an
 * expected hash absent and a current hash present, returns false, and the
 * criterion re-queues for an agent forever. That is how a `proof-statement-
 * integrity` adjudication recorded on `thm:six-term-mass-formula-complete`
 * left `needs-agent` at 1 immediately after being written.
 *
 * Resolution is DELEGATED, not reimplemented. `resolveCanonicalLean` is the
 * resolver the sweep itself uses (`folio-assistant/cat-harness-tools/pipeline/qa-utils.ts`
 * §"Canonical lean.ref resolution (single source of truth)"), and its rules
 * are not obvious — it rejects a direct module-path hit whose file does not
 * declare the named decl, so an import-only aggregator like `QOU/BraidKnot.lean`
 * does not swallow a ref. A second, simpler resolver here would resolve some
 * refs to a DIFFERENT file than the sweep does, and hashing a different file
 * reproduces this bug in a form that looks correct.
 *
 * `folio-assistant/` is gitignored (miga), so the import is dynamic and
 * guarded: without the clone the sibling path still works and library-Lean
 * blocks degrade to today's behaviour rather than crashing.
 */
async function resolveLean(): Promise<string | undefined> {
  const sibling = join(dir, `${root}.lean`);
  if (existsSync(sibling)) return sibling;
  const utils = join(REPO_ROOT, "folio-assistant/cat-harness-tools/pipeline/qa-utils.ts");
  if (!existsSync(tsPath) || !existsSync(utils)) return undefined;
  const m = readFileSync(tsPath, "utf8").match(/ref:\s*"([^"]+)"/);
  if (!m) return undefined;
  try {
    // The platform resolver returns `undefined` for EVERY ref until a
    // formalism layer is installed (it logs "[formal-ref] No formalism layer
    // is installed"). This entry point never installed one, so the
    // library-path branch above was a silent no-op again: measured
    // 2026-11-16, 48 agent verdicts written by this script on library-Lean
    // blocks carry no `lean` hash and read stale from the moment they were
    // written. Install the Lean layer with qou's package list, exactly as
    // `scripts/run-validate.ts` does.
    const sci = join(REPO_ROOT, "folio-assistant/folio-assistant-sci/pipeline/lean-formal-ref.ts");
    const pkgs = join(REPO_ROOT, "schemas/lean-packages.ts");
    if (existsSync(sci) && existsSync(pkgs)) {
      const { configureLeanPackages } = await import(sci);
      const { LEAN_PACKAGES } = await import(pkgs);
      configureLeanPackages(LEAN_PACKAGES);
    }
    const { resolveCanonicalLean } = await import(utils);
    return resolveCanonicalLean(m[1], REPO_ROOT);
  } catch {
    return undefined; // no clone / stale clone — sibling behaviour, not a crash
  }
}

/**
 * Statement-level hash, when the criterion's granularity calls for it.
 *
 * `proof-statement-integrity` declares `lean_granularity: "statement"`, so
 * `entryIsFresh` compares `lean_statement` — but ONLY when both the entry and
 * the current bundle carry one; otherwise it falls back to the whole-file
 * `lean`, which over-invalidates. So omitting this is safe and writing a hash
 * computed by a DIFFERENT lexer is not: it would never match, which is
 * indistinguishable from the file having changed.
 */
async function statementHash(path: string): Promise<string | undefined> {
  const sig = join(REPO_ROOT, "folio-assistant/folio-assistant-sci/pipeline/lean-signature.ts");
  if (!existsSync(sig)) return undefined;
  try {
    const { leanStatementHash } = await import(sig);
    return leanStatementHash(path);
  } catch {
    return undefined;
  }
}

const leanPath = await resolveLean();
const leanStatement = leanPath ? await statementHash(leanPath) : undefined;

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
// 2026-09-03: that scope note counted only blocks with a SIBLING `.lean`, and
// so measured the smaller half of the defect. See `resolveLean` above for the
// library-path half — 180 blocks whose Lean lives at the Lake path, on which
// the lean keys were omitted entirely rather than merely one of them.
//
// In particular this did NOT cause the em-coupling incident that prompted the
// look (bean `qou-aemx`).  Those `da-lean-narrative-divergence` verdicts carry
// NO field_hash at all -- they come from `local/qa-agent-drain`, which is the
// separate defect tracked in `qou-pwut`, and which this change does not touch.
const entry: any = {
  field_hash: {
    md: sha12(readFileSync(blockMd, "utf8")),
    ...(existsSync(tsPath) ? { ts: sha12(readFileSync(tsPath, "utf8")) } : {}),
    ...(leanPath ? { lean: sha12(readFileSync(leanPath, "utf8")) } : {}),
    ...(leanStatement ? { lean_statement: leanStatement } : {}),
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
