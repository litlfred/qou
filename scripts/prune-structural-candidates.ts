#!/usr/bin/env bun
/**
 * Across every tranche, find the edges that need no editorial reading.
 *
 * A block whose **prose links** a target its `uses[]` omits is contradicting
 * itself: the narrative sends the reader there, and the dependency declaration
 * says they need not go. That is a defect rather than a judgement, which is why
 * tranche 9's five were applied without the two-reader standard.
 *
 * This finds the rest — but it does NOT decide them. A link is prima facie
 * evidence and no more: prose can link a block to contrast with it, to say "not
 * to be confused with", or to point forward at what comes next. So for each
 * candidate this prints the **linking sentence**, and a human or agent reads
 * that one sentence rather than the whole block.
 *
 * It also refuses two classes outright, mechanically:
 *   - restoring would make the edge point FORWARD (regresses the detangler axis)
 *   - restoring would create a CYCLE (the target already reaches the source)
 *
 * Usage: `bun run scripts/prune-structural-candidates.ts`
 */
import { existsSync, readFileSync } from "fs";
import { resolve } from "path";
import { buildContentGraph } from "../folio-assistant/cat-harness/content/pipeline/content-graph";
import { pointsForward } from "../folio-assistant/cat-harness/content/pipeline/qa-checkers-extended";

const REPO = resolve(import.meta.dir, "..");
const AUDIT = resolve(REPO, "docs/audits/2026-08-10-transitive-prune-overreach.md");

/** Every (source, target) the audit records, as a flat list. */
function auditEdges(): Array<[string, string]> {
  const lines = readFileSync(AUDIT, "utf-8").split("\n");
  const start = lines.findIndex((l) => l.startsWith("## Every still-unreachable edge"));
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

const g = buildContentGraph(resolve(REPO, "folio"), REPO);

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

/** The sentence containing the link, trimmed to something readable. */
function linkingSentence(prose: string, target: string): string {
  const needle = `](#${target})`;
  const at = prose.indexOf(needle);
  if (at < 0) return "";
  // Walk out to sentence boundaries, ignoring the periods inside the link.
  let s = prose.lastIndexOf(". ", Math.max(0, at - 120));
  if (s < 0) s = Math.max(0, at - 240); else s += 2;
  let e = prose.indexOf(". ", at + needle.length);
  if (e < 0) e = Math.min(prose.length, at + needle.length + 160); else e += 1;
  return prose.slice(s, e).replace(/\s+/g, " ").trim();
}

// The twelve tranche targets, in index order.
const TARGETS = [
  "thm:jones-markov-trace", "def:hecke-normal-form", "def:borromean-baryon",
  "def:crossing-energy", "rem:conway-normal-form", "def:habiro-ring",
  "def:motivic-substrate", "def:archimedean-realization-functor",
  "def:q-from-epsilon", "def:hadron", "def:categorical-neutron",
  "def:categorical-proton",
];

const edges = auditEdges();
let candidates = 0, refusedForward = 0, refusedCycle = 0;

for (const target of TARGETS) {
  const sources = edges
    .filter(([, t]) => t === target)
    .map(([s]) => s)
    .filter((s) => g.nodes.has(s) && !g.out(s, "editorial").includes(target) && !reaches(s, target));

  const hits: string[] = [];
  for (const s of sources) {
    const md = g.nodes.get(s)!.ts.replace(/\.ts$/, ".md");
    if (!existsSync(md)) continue;
    const prose = readFileSync(md, "utf-8");
    if (!prose.includes(`](#${target})`)) continue;

    const fwd = pointsForward(s, target);
    // Adding s -> target closes a loop exactly when target already reaches s.
    const cycle = reaches(target, s);

    let refusal = "";
    if (fwd === undefined) refusal = "REFUSED — unplaced, cannot cost the ordering";
    else if (fwd) { refusal = "REFUSED — would point FORWARD"; refusedForward++; }
    else if (cycle) { refusal = "REFUSED — would create a CYCLE"; refusedCycle++; }
    else candidates++;

    hits.push(
      `  ${refusal ? "✗" : "→"} ${s}${refusal ? `\n      ${refusal}` : ""}\n` +
      `      "${linkingSentence(prose, target)}"`,
    );
  }
  if (hits.length) {
    console.log(`\n══ ${target}  (${hits.length} prose-linked)`);
    console.log(hits.join("\n"));
  }
}

console.log(
  `\nCandidates clear of forward/cycle refusals: ${candidates}` +
  `  ·  refused forward: ${refusedForward}  ·  refused cycle: ${refusedCycle}`,
);
console.log(
  `\nA link is prima facie evidence, not a verdict. Read each sentence above: if it ` +
  `\ncontrasts with the target, disclaims it, or points ahead rather than back, it is ` +
  `\nnot a prerequisite and does not belong in uses[].`,
);
