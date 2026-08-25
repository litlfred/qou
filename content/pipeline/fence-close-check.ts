#!/usr/bin/env bun
/**
 * Find fenced blocks that are never closed.
 *
 * Under CommonMark a **closing** fence carries no info string. So a file
 * that opens ` ```tex `, ends the diagram, and opens ` ```tex ` again has
 * two fence lines and **one** block — still open — with everything after
 * the first opener treated as raw passthrough. That aborts the LaTeX build.
 *
 * Counting fences for parity does not catch it. The file that prompted this
 * check had an even count and was broken; a parity scan over the whole
 * corpus reported zero problems while two files were unbuildable. The fix
 * is to walk the fences in order and flag any info-string fence seen while
 * a block is already open.
 *
 *   bun run content/pipeline/fence-close-check.ts [path ...]
 *
 * Exits 1 if any file has an unclosed block.
 *
 * @module content/pipeline/fence-close-check
 */
import { readFileSync, globSync } from "node:fs";

export interface Problem {
  file: string;
  openedAt: number;
  /** Line of the info-string fence that could not close it, if any. */
  blockedAt?: number;
  info: string;
}

export function check(files: string[]): Problem[] {
  const out: Problem[] = [];
  for (const file of files) {
    let text: string;
    try { text = readFileSync(file, "utf8"); } catch { continue; }
    let openInfo: string | null = null;
    let openLine = 0;
    text.split("\n").forEach((line, i) => {
      const m = /^(`{3,})(.*)$/.exec(line);
      if (!m) return;
      const info = m[2].trim();
      if (openInfo === null) { openInfo = info; openLine = i + 1; return; }
      if (info) {
        // A fence with an info string cannot close the open block; it is
        // literal content, and the block carries on from here.
        out.push({ file, openedAt: openLine, blockedAt: i + 1, info: openInfo });
        openInfo = info; openLine = i + 1;
      } else {
        openInfo = null;
      }
    });
    if (openInfo !== null) out.push({ file, openedAt: openLine, info: openInfo });
  }
  return out;
}

if (import.meta.main) {
  const args = process.argv.slice(2);
  const files = args.length ? args : globSync("content/**/*.md");
  const problems = check(files);
  if (!problems.length) {
    console.log(`no unclosed fenced blocks in ${files.length} files`);
    process.exit(0);
  }
  for (const p of problems) {
    console.log(`${p.file}:${p.openedAt}  \`\`\`${p.info} block is never closed`
      + (p.blockedAt ? ` — line ${p.blockedAt} carries an info string, so it does not close it` : ""));
  }
  process.exit(1);
}
