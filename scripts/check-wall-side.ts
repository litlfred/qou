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
import { existsSync } from "node:fs";
import { checkWallSide } from "../folio-assistant/content/pipeline/qa-checkers-voice.ts";

const args = process.argv.slice(2);
if (args.length === 0) {
  console.error("usage: bun run scripts/check-wall-side.ts <block.lean> [...]");
  process.exit(2);
}

let failed = 0;
for (const leanPath of args) {
  const base = leanPath.replace(/\.lean$/, "");
  const mdPath = `${base}.md`;
  const tsPath = `${base}.ts`;
  const r = checkWallSide(
    existsSync(mdPath) ? mdPath : undefined,
    leanPath,
    existsSync(tsPath) ? tsPath : undefined,
  );
  const mark = r.result === "pass" ? "PASS" : "FAIL";
  if (r.result !== "pass") failed++;
  const sib = [existsSync(mdPath) ? "md" : "-", existsSync(tsPath) ? "ts" : "-"]
    .join("/");
  console.log(`${mark}  [${sib}]  ${leanPath}`);
  for (const h of r.hits ?? []) {
    console.log(`        ${h.text.slice(0, 150)}`);
  }
}
console.log(`\n${args.length - failed}/${args.length} pass`);
process.exit(failed === 0 ? 0 : 1);
