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
import { existsSync, readFileSync } from "node:fs";
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
for (let i = 0; i < argv.length; i++) {
  if (argv[i] === "--block") {
    const tsPath = argv[++i];
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
