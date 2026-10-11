#!/usr/bin/env bun
/**
 * Ingest a document into qou's `library/`, using the split platform's
 * ingestion pipeline (litlfred/cat-harness-tools) rather than a local copy.
 *
 * Bean qou-15n1 (session epic qou-uwxm), owner 2026-10-10.
 *
 * ## Why a driver, and not `bun run cat ingest`
 *
 * `cat-harness-tools/scripts/ingest-document.ts` is the one entry point the
 * platform documents, but its staging directory and its destination library
 * are both resolved against `HARNESS_ROOT` — the cat-harness instance — and
 * `--harness` / `$CAT_HARNESS_ROOT` accept only a directory whose
 * `cat-harness.json` names `cat-harness`. So it cannot be pointed at qou, and
 * run as-is it files the document into cat-harness's own library.
 *
 * This driver imports that module's EXPORTED decisions — `planFor` (which rung
 * reads the file and why), `withDerivedArms` (images, vector labels, blocks),
 * `bibSlug`, the L1 gate `checkEntry`, and `buildEntryNodes` (the entry's
 * JSON-LD) — and supplies qou's paths. Nothing about *what* the pipeline does
 * is re-implemented here: two implementations of "what is a section" is the
 * drift the platform keeps paying for, and this would be a third.
 *
 * ## Where the tools come from
 *
 * `$CAT_HARNESS_TOOLS`, else `../cat-harness-tools`, else
 * `../fa-index/cat-harness-tools`. That clone must sit, as a real directory,
 * beside clones of `cat-harness`, `folio-assistant-core`,
 * `folio-assistant-sci`, `bootstrap` and `bootstrap-tools` (its
 * `HARNESS_ROOT` resolution needs the cat-harness sibling, and the JSON-LD
 * writers need all of them to bind instance prefixes), and have had
 * `bun install`. Recipe:
 *
 *   mkdir ../fa-index && cd ../fa-index
 *   for r in cat-harness cat-harness-tools folio-assistant-core \
 *            folio-assistant-sci bootstrap bootstrap-tools; do
 *     git clone --depth 1 https://github.com/litlfred/$r; done
 *   git init -q && for r in cat-harness cat-harness-tools folio-assistant-core \
 *            folio-assistant-sci bootstrap bootstrap-tools; do
 *     printf '[submodule "%s"]\n\tpath = %s\n' $r $r >> .gitmodules; done
 *   (cd cat-harness-tools && bun install)
 *   pip install -r cat-harness-tools/python/requirements.txt The tools commit is
 * printed and written into the entry's `ingest-provenance.json`, so a later
 * reader knows which pipeline produced it — the qou pin
 * (`.folio-assistant-pin`) does not cover these repos.
 *
 * Usage (from the qou root):
 *   bun run scripts/library-ingest.ts FILE.pdf [FILE.pdf ...] [--dry-run] [--force]
 *
 * `--force` replaces an existing `library/<slug>/`. Without it an existing
 * entry is skipped, never overwritten: library entries carry agent-written
 * `summary.json`s and duplicate verdicts that a re-ingest would destroy.
 *
 * Exit: 0 all ingested/skipped, 1 any failed, 2 any undetermined.
 */
import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";

const QOU = resolve(import.meta.dir, "..");
const TOOLS_CANDIDATES = [
  process.env.CAT_HARNESS_TOOLS,
  join(QOU, "..", "cat-harness-tools"),
  join(QOU, "..", "fa-index", "cat-harness-tools"),
].filter((p): p is string => !!p);
const TOOLS = resolve(TOOLS_CANDIDATES.find((p) => existsSync(join(p, "scripts", "ingest-document.ts"))) ?? "");
if (!existsSync(join(TOOLS, "scripts", "ingest-document.ts"))) {
  console.error(`cat-harness-tools not found (tried ${TOOLS_CANDIDATES.join(", ")}) — set $CAT_HARNESS_TOOLS.`);
  process.exit(1);
}
// The tools must sit in an INDEX checkout: a directory with its own `.git` and
// a `.gitmodules` naming each instance clone. Without it the platform disagrees
// with itself about where the checkout is: `block-kinds.ts` hardcodes
// `cat-harness/..`, while `content-context.ts` asks `checkoutRootFor`, which
// stops at cat-harness's own `.git` and then binds only the `cat-harness:`
// prefix, so `l1-blocks.ts` throws on `folio-assistant-core:Prose`. Do NOT
// paper over that with `FOLIO_FIXTURE_CHECKOUT` naming the same directory:
// `declaredDirectories` then scans every instance twice and dies on
// `content adapter "paper" is declared twice` (measured 2026-10-11).
if (!existsSync(join(dirname(TOOLS), ".gitmodules"))) {
  console.error(`${dirname(TOOLS)} is not an index checkout (no .gitmodules) — see the recipe in this file's header.`);
  process.exit(1);
}
// findContentRepoRoot() (inside buildEntryNodes) walks up from the CWD.
process.chdir(QOU);

const ingest = await import(join(TOOLS, "scripts", "ingest-document.ts"));
const { checkEntry } = await import(join(TOOLS, "scripts", "check-l1-complete.ts"));
const { buildEntryNodes } = await import(join(TOOLS, "content", "pipeline", "gen-library-jsonld.ts"));

const toolsSha = new TextDecoder()
  .decode(Bun.spawnSync(["git", "-C", TOOLS, "rev-parse", "HEAD"]).stdout)
  .trim();

const LIBRARY = join(QOU, "library");
const STAGING_ROOT = join(QOU, "ingest-staging");

const args = process.argv.slice(2);


const dry = args.includes("--dry-run");
const force = args.includes("--force");
const files = args.filter((a) => !a.startsWith("--"));
if (files.length === 0) {
  console.error("usage: bun run scripts/library-ingest.ts FILE [FILE ...] [--dry-run] [--force]");
  process.exit(1);
}

console.log(`cat-harness-tools ${toolsSha.slice(0, 12)} (${TOOLS})`);
let failed = 0;
let undetermined = 0;

for (const f of files) {
  const pdf = resolve(f);
  const slug: string = ingest.bibSlug(pdf);
  const staging = join(STAGING_ROOT, slug);
  const out = join(LIBRARY, slug);
  const plan = ingest.withDerivedArms(ingest.planFor(pdf, undefined, STAGING_ROOT), pdf, STAGING_ROOT, staging, LIBRARY);

  console.log(`\n${basename(pdf)} -> library/${slug}/`);
  console.log(`  rung: ${plan.rung}`);
  console.log(`  why:  ${plan.why}`);

  if (plan.rung === "undetermined") {
    console.error("  NOT ingested: rung undetermined (a wrong rung reads as ingested while its structure is wrong).");
    undetermined++;
    continue;
  }
  if (existsSync(out) && !force) {
    console.log("  SKIPPED: library entry exists (pass --force to replace it).");
    continue;
  }
  if (dry) {
    for (const s of plan.steps) console.log(`  would run: ${s.join(" ")}`);
    continue;
  }

  rmSync(staging, { recursive: true, force: true });
  mkdirSync(STAGING_ROOT, { recursive: true });
  let ok = true;
  for (const s of plan.steps) {
    const started = Date.now();
    const r = Bun.spawnSync(s, { stdout: "inherit", stderr: "inherit" });
    if (r.exitCode !== 0) {
      const recorded = ingest.recordedUndetermined(s, r.exitCode, started);
      if (recorded !== undefined) {
        console.log(`  ${basename(s[1] ?? "")}: UNDETERMINED, recorded in ${recorded} — continuing`);
        continue;
      }
      console.error(`  ${s[1]} failed (exit ${r.exitCode}) — stopping this document.`);
      ok = false;
      break;
    }
  }
  if (!ok) {
    failed++;
    continue;
  }

  const verdict = checkEntry(staging);
  if (!ingest.mayPromote(verdict.requirements)) {
    const unmet = verdict.requirements.filter((r: { state: string }) => r.state === "unmet");
    console.error(`  NOT promoted — ${unmet.length} requirement(s) unmet; staged output left at ${relative(QOU, staging)}/`);
    for (const r of unmet) console.error(`    ${r.name.padEnd(22)} ${r.detail}`);
    failed++;
    continue;
  }

  const nodes = buildEntryNodes(slug, staging, out);
  if (nodes.state === "unreadable") {
    console.error(`  NOT promoted — JSON-LD nodes could not be built (${nodes.rung} input unreadable).`);
    failed++;
    continue;
  }

  // Keep the source PDF with the entry, as every existing qou entry does.
  const kept = join(staging, basename(pdf));
  if (!existsSync(kept)) cpSync(pdf, kept);

  writeFileSync(
    join(staging, "ingest-provenance.json"),
    JSON.stringify(
      {
        $schema: "qou-ingest-provenance/v1",
        source: basename(pdf),
        rung: plan.rung,
        why: plan.why,
        tools: { repository: "litlfred/cat-harness-tools", commit: toolsSha },
        driver: "scripts/library-ingest.ts",
      },
      null,
      2,
    ) + "\n",
  );

  if (existsSync(out)) rmSync(out, { recursive: true, force: true });
  mkdirSync(dirname(out), { recursive: true });
  cpSync(staging, out, { recursive: true });
  rmSync(staging, { recursive: true, force: true });
  if (nodes.state === "built") {
    for (const n of nodes.files) {
      mkdirSync(dirname(join(out, n.path)), { recursive: true });
      writeFileSync(join(out, n.path), n.content);
    }
  }
  console.log(
    `  ✓ promoted (L1 gate passed${nodes.state === "built" ? `, ${nodes.files.length} JSON-LD node file(s)` : ""})`,
  );
}

console.log(`\ndone: ${files.length} file(s), ${failed} failed, ${undetermined} undetermined`);
process.exit(undetermined ? 2 : failed ? 1 : 0);
