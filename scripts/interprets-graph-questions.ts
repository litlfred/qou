#!/usr/bin/env bun
/**
 * Evidence for the two questions that counting `interprets` opened.
 *
 * `interprets` became an editorial edge on 2026-08-15 (folio-assistant bean
 * `i8ad`). That was the right call — a remark interpreting a proposition cannot
 * be followed without it — but it made two pre-existing conditions visible, and
 * neither is the tool's to decide:
 *
 *   1. **Editorial cycles.** The `uses[]`-only graph was made acyclic
 *      deliberately (#4881). With `interprets` counted it is not, and each
 *      cycle says a reader must read A before B and B before A.
 *   2. **Forward-pointing `interprets` edges.** A remark placed before the
 *      block it interprets. `detangler-no-forward-ref` builds its own
 *      `uses`-only adjacency, so it cannot see these — they are real forward
 *      references outside what the gate counts.
 *
 * For each, this prints what a person needs in order to choose: which field
 * carries each leg of a cycle (an `interprets` leg is a structural claim, a
 * `uses` leg is a curated entry — they are not equally easy to change), and for
 * each forward edge how far it reaches and what sits between.
 *
 * It proposes nothing. Both questions are editorial.
 *
 * Usage: `bun run scripts/interprets-graph-questions.ts`
 */
import { resolve } from "path";
import { buildContentGraph } from "../folio-assistant/cat-harness-tools/pipeline/content-graph";
import { blockPlacement, pointsForward } from "../folio-assistant/cat-harness-tools/pipeline/qa-checkers-extended";

const REPO = resolve(import.meta.dir, "..");
const g = buildContentGraph(resolve(REPO, "folio"), REPO);

/** Which authored field carries the edge a -> b, if any. */
function fieldOf(a: string, b: string): string {
  const e = g.outEdges(a, "editorial").find((x) => x.to === b);
  return e?.editorialField ?? "?";
}

// ── 1. Editorial cycles ─────────────────────────────────────────────
const WHITE = 0, GREY = 1, BLACK = 2;
const colour = new Map<string, number>();
const cycles: string[][] = [];
function dfs(n: string, stack: string[]): void {
  colour.set(n, GREY);
  stack.push(n);
  for (const m of g.out(n, "editorial")) {
    const c = colour.get(m) ?? WHITE;
    if (c === GREY) cycles.push([...stack.slice(stack.indexOf(m)), m]);
    else if (c === WHITE) dfs(m, stack);
  }
  stack.pop();
  colour.set(n, BLACK);
}
for (const n of g.nodes.keys()) if ((colour.get(n) ?? WHITE) === WHITE) dfs(n, []);

console.log(`# Editorial cycles: ${cycles.length}\n`);
console.log(
  `Each says a reader must read A before B *and* B before A. The \`field\` column\n` +
  `is what makes these decidable: an \`interprets\` leg is a single structural\n` +
  `claim about what a block is *about*, a \`uses\` leg is one entry in a curated\n` +
  `list. Breaking the cycle at the \`uses\` leg is usually an edit; breaking it at\n` +
  `the \`interprets\` leg usually means the block is misclassified.\n`,
);

for (const cyc of cycles) {
  console.log(`## ${cyc[0]}`);
  console.log(`\n| from | to | field |`);
  console.log(`|---|---|---|`);
  for (let i = 0; i < cyc.length - 1; i++) {
    console.log(`| \`${cyc[i]}\` | \`${cyc[i + 1]}\` | **${fieldOf(cyc[i], cyc[i + 1])}** |`);
  }
  const kinds = cyc.slice(0, -1).map((l) => `${l} (${g.nodes.get(l)?.kind ?? "?"})`);
  console.log(`\nBlocks: ${kinds.join(", ")}\n`);
}

// ── 2. Forward-pointing interprets edges ────────────────────────────
const forward: Array<{ from: string; to: string; gap: number; chapter: string }> = [];
for (const e of g.edges) {
  if (e.kind !== "editorial" || e.editorialField !== "interprets") continue;
  if (pointsForward(e.from, e.to) !== true) continue;
  const a = blockPlacement(e.from);
  const b = blockPlacement(e.to);
  if (a.status !== "ok" || b.status !== "ok") continue;
  forward.push({ from: e.from, to: e.to, gap: b.within - a.within, chapter: a.chapter });
}
forward.sort((x, y) => y.gap - x.gap);

console.log(`\n# Forward-pointing \`interprets\` edges: ${forward.length}\n`);
console.log(
  `A remark placed before the block it interprets. \`detangler-no-forward-ref\`\n` +
  `builds its own \`uses\`-only adjacency, so **the gate cannot see these** — they\n` +
  `are real forward references outside what it counts.\n\n` +
  `\`gap\` is how many block positions the reader must jump. A small gap is often\n` +
  `deliberate (a remark introducing what comes next); a large one is the shape\n` +
  `the detangler arc has been removing.\n`,
);
console.log(`| gap | from | to | chapter |`);
console.log(`|---|---|---|---|`);
for (const f of forward) {
  console.log(`| ${f.gap} | \`${f.from}\` | \`${f.to}\` | ${f.chapter.split("/").pop()} |`);
}

console.log(
  `\n---\n\nNeither list is a proposal. Widening the gate to count these moves a number\n` +
  `five merged PRs were measured against, and breaking a cycle changes what a\n` +
  `block claims to be about. Both are editorial decisions.\n`,
);
