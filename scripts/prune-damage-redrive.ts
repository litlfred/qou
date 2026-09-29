#!/usr/bin/env bun
/**
 * Re-drive the transitive-prune damage audit against the corpus as it is TODAY.
 *
 * `docs/audits/2026-08-10-transitive-prune-overreach.md` records every edge two
 * bulk prunes removed without preserving reachability — 785 of them, measured on
 * 2026-08-10. Restoration is meant to happen in reviewed tranches, and `main`
 * moves daily, so a tranche reviewed against the audit's figures is reviewed
 * against a corpus that no longer exists. This re-reads the audit's edge list
 * and asks, for each edge, what is true now.
 *
 * ## Editorial edges only, deliberately
 *
 * `ContentGraph`'s accessors default to the UNION of editorial and formal
 * edges. That is the right default for "what breaks if this changes?" and the
 * wrong one here: prn1 is about what a *reader* can reach through `uses[]`.
 * Folding in Lean edges would count paths no reader can follow and make the
 * damage look smaller than it is. Every call below passes `"editorial"`.
 *
 * ## What it does not do
 *
 * It does not restore anything. A prune applied a mechanical rule across the
 * corpus without reading; restoring mechanically would repeat that error in the
 * opposite direction. This produces the candidate list a reader works from.
 *
 * Usage: `bun run scripts/prune-damage-redrive.ts [--all]`
 *   --all   list every still-lost edge, not just the ranked summary
 */
import { readFileSync } from "fs";
import { resolve } from "path";
import { buildContentGraph } from "../folio-assistant/cat-harness/content/pipeline/content-graph";

const REPO = resolve(import.meta.dir, "..");
const AUDIT = resolve(REPO, "docs/audits/2026-08-10-transitive-prune-overreach.md");
const SECTION = "## Every still-unreachable edge";

/** The audit's per-source bullet list: `### \`src\`` followed by `- \`target\``. */
function parseAuditEdges(): Array<[string, string]> {
  const lines = readFileSync(AUDIT, "utf-8").split("\n");
  const start = lines.findIndex((l) => l.startsWith(SECTION));
  if (start < 0) throw new Error(`"${SECTION}" not found in ${AUDIT}`);
  const out: Array<[string, string]> = [];
  let src = "";
  for (const line of lines.slice(start + 1)) {
    const h = line.match(/^###\s+`([^`]+)`/);
    if (h) { src = h[1]; continue; }
    const b = line.match(/^-\s+`([^`]+)`/);
    if (b && src) out.push([src, b[1]]);
  }
  return out;
}

const claimed = parseAuditEdges();
const g = buildContentGraph(resolve(REPO, "folio"), REPO);

/** Is `to` reachable from `from` through EDITORIAL edges alone? */
function reaches(from: string, to: string): boolean {
  const seen = new Set<string>([from]);
  const stack = [from];
  while (stack.length) {
    for (const n of g.out(stack.pop()!, "editorial")) {
      if (n === to) return true;
      if (!seen.has(n)) { seen.add(n); stack.push(n); }
    }
  }
  return false;
}

const tally = { sourceGone: 0, targetGone: 0, reDeclared: 0, reachableAgain: 0, stillLost: 0 };
const stillLost = new Map<string, string[]>();
const reDeclared = new Map<string, string[]>();

for (const [from, to] of claimed) {
  if (!g.nodes.has(from)) { tally.sourceGone++; continue; }
  if (!g.nodes.has(to)) { tally.targetGone++; continue; }
  if (g.out(from, "editorial").includes(to)) {
    tally.reDeclared++;
    reDeclared.set(from, [...(reDeclared.get(from) ?? []), to]);
    continue;
  }
  if (reaches(from, to)) { tally.reachableAgain++; continue; }
  tally.stillLost++;
  stillLost.set(from, [...(stillLost.get(from) ?? []), to]);
}

const declaresNothing = [...stillLost.keys()].filter((b) => g.out(b, "editorial").length === 0);

console.log(`prune-damage re-drive — audit 2026-08-10 vs corpus today\n`);
console.log(`  audit edges parsed             ${claimed.length}   (audit: 785)`);
console.log(`  source block gone              ${tally.sourceGone}`);
console.log(`  target block gone              ${tally.targetGone}`);
console.log(`  edge re-declared since         ${tally.reDeclared}`);
console.log(`  reachable again via a path     ${tally.reachableAgain}`);
console.log(`  STILL LOST                     ${tally.stillLost}`);
console.log(`  across blocks                  ${stillLost.size}   (audit: 335)`);
console.log(`  of which declare nothing       ${declaresNothing.length}   (audit: 80)`);

const ranked = [...stillLost.entries()].sort((a, b) => b[1].length - a[1].length);
console.log(`\n── still lost, by block (top 25 of ${ranked.length}) ──`);
for (const [b, ts] of ranked.slice(0, 25)) {
  const flag = g.out(b, "editorial").length === 0 ? "  [declares nothing]" : "";
  console.log(`  ${String(ts.length).padStart(3)}  ${b}${flag}`);
}
if (ranked.length > 25) {
  console.log(`  … ${ranked.length - 25} more blocks not shown; pass --all for every edge`);
}

if (process.argv.includes("--all")) {
  console.log(`\n── every still-lost edge ──`);
  for (const [b, ts] of ranked) {
    console.log(`\n### ${b}`);
    for (const t of ts) console.log(`- ${t}`);
  }
}

/**
 * A target lost by MANY sources at once is the prune's signature, and the
 * strongest mechanical signal available: one bulk rule stripped it corpus-wide
 * and nothing put it back. Still a candidate for a reader, not a verdict.
 */
const byTarget = new Map<string, string[]>();
for (const [b, ts] of stillLost) for (const t of ts) byTarget.set(t, [...(byTarget.get(t) ?? []), b]);
console.log(`\n── most-widely-lost targets (top 15) ──`);
for (const [t, srcs] of [...byTarget.entries()].sort((a, b) => b[1].length - a[1].length).slice(0, 15)) {
  console.log(`  ${String(srcs.length).padStart(3)} sources lost  ${t}`);
}
