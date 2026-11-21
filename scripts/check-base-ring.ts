/**
 * Run the `wall-base-ring-minimal` checker (folio-assistant
 * `qa-checkers-voice.ts::checkBaseRingMinimal`) over one or more content
 * blocks, so a §7c de-specialisation edit can be VERIFIED rather than assumed.
 *
 * Companion to `check-wall-side.ts`. Same resolution discipline: the block's
 * `lean.ref` is resolved through the pipeline's own `resolveCanonicalLean`,
 * never a hand-rolled prefix walk. A checker script that scores a different
 * file from the sweep it is meant to reproduce is worse than no checker
 * script -- see that file's header for the worked failure (77/1191 blocks
 * mis-resolved onto import-only aggregators, reporting PASS on live fails).
 *
 * The criterion reads ONLY the `.lean` (unlike `wall-side-correct`, which
 * also reads the `.md`/`.ts` acknowledgement). It is advisory: `warn`, not
 * `fail`. Archimedean-side files pass outright -- a field is legitimate
 * post-wall -- so every hit here is on the algebraic side, where §7c asks
 * for the weakest typeclass that admits the construction.
 *
 * Usage:
 *   bun run scripts/check-base-ring.ts <block.lean> [...]
 *   bun run scripts/check-base-ring.ts --block <block.ts> [...]
 *   bun run scripts/check-base-ring.ts --sweep <dir> [--json <out.json>]
 *
 * Exit 0 iff every named block passes (0 hits).
 */
import { existsSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { checkBaseRingMinimal } from "../folio-assistant/folio-assistant-sci/pipeline/qa-checkers-wall.ts";
import {
  resolveCanonicalLean,
  type LakeTreeCache,
} from "../folio-assistant/cat-harness-tools/pipeline/qa-utils.ts";
import { configureLeanPackages } from "../folio-assistant/folio-assistant-sci/pipeline/lean-formal-ref";
import { LEAN_PACKAGES } from "../schemas/lean-packages";
import { dirname, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

/** One shared Lake-tree cache for the whole run.
 *
 *  `resolveCanonicalLean` falls through to a basename map and a decl->file
 *  scan of the entire Lake tree. Without a cache it rebuilds both **per
 *  block**, which on a 3400-block sweep is quadratic and never finishes.
 *  The parameter exists precisely for bulk callers (`qa-utils.ts` §"pass a
 *  `LakeTreeCache` for bulk"); a sweep that omits it is a performance bug,
 *  not merely slow. */
const LAKE_CACHE: LakeTreeCache = new Map();

/** Repo root, anchored on this file's own location (`scripts/` -> one up)
 *  rather than `process.cwd()`, so `resolveCanonicalLean` finds the Lake
 *  tree no matter which directory the script is invoked from. */
const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");

/** Install the lean.ref resolver layer and declare qou's Lake packages, as
 *  run-validate.ts and preload-registry.ts do. Without it the package
 *  registry is empty and every `lean.ref` without a sibling `.lean`
 *  resolves to nothing (bean qou-i2ed). */
configureLeanPackages(LEAN_PACKAGES);

const argv = process.argv.slice(2);
if (argv.length === 0) {
  console.error(
    "usage: bun run scripts/check-base-ring.ts <block.lean> [...]\n" +
    "       bun run scripts/check-base-ring.ts --block <block.ts> [...]\n" +
    "       bun run scripts/check-base-ring.ts --sweep <dir> [--json <out>]\n\n" +
    "  <block.lean>      direct mode: score the named .lean\n" +
    "  --block <.ts>     manifest mode: resolve the block's `lean.ref` into\n" +
    "                    the library tree, then score THAT file -- which is\n" +
    "                    how qa-sweep actually calls the checker\n" +
    "  --sweep <dir>     every block manifest under <dir>, worst-first\n" +
    "  --json <out>      also write the worklist as JSON (sweep mode)",
  );
  process.exit(2);
}

/** Resolve a block manifest's `lean.ref` to a file on disk: sibling
 *  `<root>.lean` first, then the pipeline's own `resolveCanonicalLean`.
 *  Delegates rather than re-deriving -- see the module docstring. */
function resolveLeanFromManifest(tsPath: string): string | undefined {
  const base = tsPath.replace(/\.ts$/, "");
  const sibling = `${base}.lean`;
  if (existsSync(sibling)) return sibling;
  const src = readFileSync(tsPath, "utf-8");
  const m = src.match(/ref:\s*"([^"]+)"/);
  if (!m) return undefined;
  return resolveCanonicalLean(m[1], REPO_ROOT, LAKE_CACHE) ?? undefined;
}

/** A flag whose required argument is missing must say so, not crash. */
function requireArg(flag: string, value: string | undefined): string {
  if (value === undefined || value.startsWith("-")) {
    console.error(`check-base-ring: ${flag} requires a path argument.\n`);
    console.error("usage: bun run scripts/check-base-ring.ts [options]");
    console.error("  --sweep <dir>       check every block manifest under <dir>");
    console.error("  --block <file.ts>   check a single block manifest");
    console.error("  --json  <out.json>  write the sweep worklist as JSON");
    process.exit(2);
  }
  return value;
}

const targets: { lean: string; label: string; ts?: string }[] = [];
let jsonOut: string | undefined;
let sweepMode = false;

/** `--sweep <dir>`: every block manifest under <dir> that carries a
 *  `lean.ref`, scored the way qa-sweep does. Gives the true current
 *  warning list rather than a hand-assembled shortlist. */
function sweep(dir: string) {
  const out: string[] = [];
  const walk = (d: string) => {
    for (const e of readdirSync(d, { withFileTypes: true })) {
      const p = `${d}/${e.name}`;
      if (e.isDirectory()) walk(p);
      else if (e.name.endsWith(".ts") && !e.name.endsWith(".d.ts")) out.push(p);
    }
  };
  walk(dir);
  for (const tsPath of out) {
    let src: string;
    try { src = readFileSync(tsPath, "utf-8"); } catch { continue; }
    if (!/lean:\s*{/.test(src)) continue;
    const lean = resolveLeanFromManifest(tsPath);
    if (!lean) continue;
    targets.push({ lean, ts: tsPath, label: tsPath });
  }
}

for (let i = 0; i < argv.length; i++) {
  if (argv[i] === "--sweep") {
    sweepMode = true;
    sweep(requireArg("--sweep", argv[++i]));
  } else if (argv[i] === "--json") {
    jsonOut = requireArg("--json", argv[++i]);
  } else if (argv[i] === "--block") {
    const tsPath = requireArg("--block", argv[++i]);
    const lean = resolveLeanFromManifest(tsPath);
    if (!lean) {
      console.log(`SKIP  [unresolved lean.ref]  ${tsPath}`);
      continue;
    }
    targets.push({ lean, ts: tsPath, label: `${tsPath}  ->  ${lean}` });
  } else {
    targets.push({ lean: argv[i], label: argv[i] });
  }
}

type Row = {
  block?: string;
  lean: string;
  result: string;
  hits: number;
  lines: { line: number; src: string }[];
};

/** One row per *distinct* .lean: several blocks can share a library file
 *  (an aggregate module backing a cluster of blocks), and scoring it once
 *  per block would triple-count the same hits into the worklist. */
const byLean = new Map<string, Row>();

for (const t of targets) {
  if (byLean.has(t.lean)) continue;
  const r = checkBaseRingMinimal(t.lean);
  let src: string[] = [];
  try { src = readFileSync(t.lean, "utf-8").split("\n"); } catch { /* unreadable */ }
  byLean.set(t.lean, {
    block: t.ts ? relative(REPO_ROOT, t.ts) : undefined,
    lean: relative(REPO_ROOT, t.lean),
    result: r.result,
    hits: (r.hits ?? []).length,
    lines: (r.hits ?? []).map((h) => ({
      line: h.line,
      src: (src[h.line - 1] ?? "").trim().slice(0, 160),
    })),
  });
}

const rows = [...byLean.values()].sort((a, b) => b.hits - a.hits);
const warned = rows.filter((r) => r.hits > 0);

if (sweepMode) {
  for (const r of warned) {
    console.log(`${String(r.hits).padStart(4)}  ${r.lean}`);
  }
  console.log(
    `\n${rows.length - warned.length}/${rows.length} distinct .lean pass;` +
    ` ${warned.length} warn, ${warned.reduce((s, r) => s + r.hits, 0)} hits total`,
  );
} else {
  for (const r of rows) {
    console.log(`${r.hits === 0 ? "PASS" : "WARN"}  (${r.hits})  ${r.lean}`);
    for (const l of r.lines) console.log(`        ${l.line}: ${l.src}`);
  }
  console.log(`\n${rows.length - warned.length}/${rows.length} pass`);
}

if (jsonOut) {
  writeFileSync(jsonOut, JSON.stringify(warned, null, 1));
  console.log(`wrote ${warned.length} rows -> ${jsonOut}`);
}

process.exit(warned.length === 0 ? 0 : 1);
