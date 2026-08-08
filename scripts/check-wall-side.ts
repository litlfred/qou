/**
 * Run the `wall-side-correct` checker (folio-assistant
 * `qa-checkers-voice.ts::checkWallSide`) over one or more content blocks,
 * so a §7c acknowledgement edit can be VERIFIED rather than assumed.
 *
 * The criterion reads the acknowledgement from the block `.md` and the
 * `.ts` `authorNotes` only -- never from the `.lean` docstring -- so a
 * file whose module comment already says "Archimedean realisation" still
 * fails until the note reaches a sibling the checker actually reads.
 *
 * Usage:  bun run scripts/check-wall-side.ts <block.lean> [...]
 * Exit 0 iff every named block passes.
 */
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { checkWallSide } from "../folio-assistant/content/pipeline/qa-checkers-voice.ts";

const argv = process.argv.slice(2);
if (argv.length === 0) {
  console.error(
    "usage: bun run scripts/check-wall-side.ts <block.lean> [...]\n" +
    "       bun run scripts/check-wall-side.ts --block <block.ts> [...]\n\n" +
    "  <block.lean>      sibling mode: .md/.ts looked up next to the .lean\n" +
    "  --block <.ts>     manifest mode: resolves the block's `lean.ref` into\n" +
    "                    the library tree, then checks with THAT block's\n" +
    "                    .md/.ts as the acknowledgement sources -- which is\n" +
    "                    how qa-sweep actually calls the checker\n" +
    "                    (`checkWallSide(p.md, p.lean, p.ts)`).",
  );
  process.exit(2);
}

/** Resolve a block manifest's `lean.ref` to a file on disk, mirroring the
 *  pipeline's lookup order: sibling `<root>.lean` first, then
 *  `<lakeRoot>/<Decl/Path>.lean` under the package's Lake root. */
function resolveLeanFromManifest(tsPath: string): string | undefined {
  const base = tsPath.replace(/\.ts$/, "");
  const sibling = `${base}.lean`;
  if (existsSync(sibling)) return sibling;
  const src = readFileSync(tsPath, "utf-8");
  const m = src.match(/ref:\s*"([^:"]+):([^"]+)"/);
  if (!m) return undefined;
  const decl = m[2];
  // qou -> content/quantum-observable-universe/lean
  const lakeRoot = "content/quantum-observable-universe/lean";
  // Try progressively shorter prefixes: the trailing component of the decl
  // path is usually the theorem name, not part of the file path.
  const parts = decl.split(".");
  for (let n = parts.length; n > 0; n--) {
    const cand = `${lakeRoot}/${parts.slice(0, n).join("/")}.lean`;
    if (existsSync(cand)) return cand;
  }
  return undefined;
}

const targets: { lean: string; md?: string; ts?: string; label: string }[] = [];

/** `--sweep <dir>`: every block manifest under <dir> that carries a
 *  `lean.ref`, checked the way qa-sweep does. Gives the true current
 *  failing list rather than a hand-assembled shortlist. */
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
    const mdPath = tsPath.replace(/\.ts$/, ".md");
    targets.push({
      lean,
      md: existsSync(mdPath) ? mdPath : undefined,
      ts: tsPath,
      label: tsPath,
    });
  }
}

/** A flag whose required argument is missing must say so, not crash.
 *
 * `--sweep` and `--block` each consume the next argv entry. When it is absent,
 * `undefined` reached `readdirSync`/`readFileSync` and the script died with a
 * bare `ERR_INVALID_ARG_TYPE` stack trace naming an internal line — which reads
 * as "the checker is broken", not "you forgot the path". That is the same
 * failure shape this batch keeps finding: a tool reporting its own misuse as a
 * result. Cf. the unknown-option guard added to
 * `content/pipeline/lean-vacuity-axiom-audit.ts` (#4712). */
function requireArg(flag: string, value: string | undefined): string {
  if (value === undefined || value.startsWith("-")) {
    console.error(`check-wall-side: ${flag} requires a path argument.\n`);
    console.error("usage: bun run scripts/check-wall-side.ts [options]");
    console.error("  --sweep <dir>       check every block manifest under <dir>");
    console.error("  --block <file.ts>   check a single block manifest");
    process.exit(2);
  }
  return value;
}

for (let i = 0; i < argv.length; i++) {
  if (argv[i] === "--sweep") {
    sweep(requireArg("--sweep", argv[++i]));
  } else if (argv[i] === "--block") {
    const tsPath = requireArg("--block", argv[++i]);
    const lean = resolveLeanFromManifest(tsPath);
    if (!lean) {
      console.log(`SKIP  [unresolved lean.ref]  ${tsPath}`);
      continue;
    }
    const mdPath = tsPath.replace(/\.ts$/, ".md");
    targets.push({
      lean,
      md: existsSync(mdPath) ? mdPath : undefined,
      ts: tsPath,
      label: `${tsPath}  ->  ${lean}`,
    });
  } else {
    const base = argv[i].replace(/\.lean$/, "");
    targets.push({
      lean: argv[i],
      md: existsSync(`${base}.md`) ? `${base}.md` : undefined,
      ts: existsSync(`${base}.ts`) ? `${base}.ts` : undefined,
      label: argv[i],
    });
  }
}

let failed = 0;
for (const t of targets) {
  const leanPath = t.lean;
  const mdPath = t.md ?? "";
  const tsPath = t.ts ?? "";
  const r = checkWallSide(
    mdPath && existsSync(mdPath) ? mdPath : undefined,
    leanPath,
    tsPath && existsSync(tsPath) ? tsPath : undefined,
  );
  const mark = r.result === "pass" ? "PASS" : "FAIL";
  if (r.result !== "pass") failed++;
  const sib = [
    mdPath && existsSync(mdPath) ? "md" : "-",
    tsPath && existsSync(tsPath) ? "ts" : "-",
  ].join("/");
  console.log(`${mark}  [${sib}]  ${t.label}`);
  for (const h of r.hits ?? []) {
    console.log(`        ${h.text.slice(0, 150)}`);
  }
}
console.log(`\n${targets.length - failed}/${targets.length} pass`);
process.exit(failed === 0 ? 0 : 1);
