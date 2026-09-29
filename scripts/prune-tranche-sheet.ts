#!/usr/bin/env bun
/**
 * Build the evidence sheet for one restoration tranche.
 *
 * `prune-damage-redrive.ts` shows that the prune damage cuts far better by
 * TARGET than by source: one foundational definition was stripped from 10-21
 * blocks at once, so "must a reader have read T before these?" is a single
 * editorial question with many applications. This assembles what a reader needs
 * to answer it for one target.
 *
 * For each source that lost `T` it reports:
 *
 *   - **prose link** — the narrative contains `](#T)`. This is the decisive
 *     signal in the other direction: the prose is *sending the reader there*,
 *     so the block plainly depends on it and `uses[]` omitting it is a defect
 *     rather than a judgement call.
 *   - **prose mention** — the narrative names the concept without linking.
 *     Suggestive, not decisive; a block can mention a theorem it does not
 *     depend on.
 *   - **lean** — the block's Lean file references the declaration `T` owns.
 *     Evidence about the FORMAL relation, which is not the editorial one, so it
 *     is reported and never treated as an answer. A proof can invoke a lemma no
 *     reader needs to have read.
 *   - **declares now** — so a reader can see what the block does carry.
 *   - **restoring points** — whether the restored edge would run FORWARD, i.e.
 *     at a target later in the same chapter. That is what
 *     `detangler-no-forward-ref` counts and what the `fwr` arc has been
 *     reducing, so a correct restoration can silently undo correct ordering
 *     work. `n/a` when either block is unplaced — unknown, not safe.
 *
 * None of these is a verdict. The `uses-editorial-review` two-reader standard
 * governs what is applied; this only removes the busywork from their reading.
 *
 * Usage: `bun run scripts/prune-tranche-sheet.ts <target-label>`
 */
import { existsSync, readFileSync } from "fs";
import { resolve } from "path";
import { buildContentGraph } from "../folio-assistant/cat-harness/content/pipeline/content-graph";
import { pointsForward } from "../folio-assistant/cat-harness/content/pipeline/qa-checkers-extended";

const REPO = resolve(import.meta.dir, "..");
const AUDIT = resolve(REPO, "docs/audits/2026-08-10-transitive-prune-overreach.md");

const target = process.argv[2];
if (!target) {
  console.error("usage: bun run scripts/prune-tranche-sheet.ts <target-label>");
  process.exit(2);
}

/** Sources the audit records as having lost `target`. */
function auditSourcesFor(t: string): string[] {
  const lines = readFileSync(AUDIT, "utf-8").split("\n");
  const start = lines.findIndex((l) => l.startsWith("## Every still-unreachable edge"));
  const out: string[] = [];
  let src = "";
  for (const line of lines.slice(start + 1)) {
    const h = line.match(/^###\s+`([^`]+)`/);
    if (h) { src = h[1]; continue; }
    const b = line.match(/^-\s+`([^`]+)`/);
    if (b && b[1] === t && src) out.push(src);
  }
  return out;
}

const g = buildContentGraph(resolve(REPO, "content"), REPO);

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

/** The concept words to look for when there is no explicit link. */
function conceptTerms(label: string): string[] {
  const slug = label.replace(/^[a-z]+:/, "");
  // "jones-markov-trace" -> ["jones", "markov trace", "markov-trace"]
  const words = slug.split("-");
  const terms = new Set<string>([slug.replace(/-/g, " "), slug]);
  for (let i = 0; i < words.length - 1; i++) terms.add(`${words[i]} ${words[i + 1]}`);
  return [...terms];
}

const terms = conceptTerms(target);
const targetNode = g.nodes.get(target);
const targetDecl = targetNode?.leanRef?.replace(/^[^:]*:/, "");

const sources = auditSourcesFor(target).filter(
  (s) => g.nodes.has(s) && !g.out(s, "editorial").includes(target) && !reaches(s, target),
);

console.log(`# Tranche: restore \`${target}\`?\n`);
console.log(`Target exists: ${targetNode ? "yes" : "**NO — target block is gone**"}`);
if (targetDecl) console.log(`Target Lean decl: \`${targetDecl}\``);
console.log(`Sources that lost it and still cannot reach it: **${sources.length}**\n`);
console.log(`| source | kind | prose link | prose mention | lean | declares now | restoring points |`);
console.log(`|---|---|---|---|---|---|---|`);

const linked: string[] = [];
let noNarrative = 0;
let notPlaced = 0;
const forward: string[] = [];
for (const s of sources) {
  const n = g.nodes.get(s)!;
  const md = n.ts.replace(/\.ts$/, ".md");
  const leanPath = n.ts.replace(/\.ts$/, ".lean");

  // A file that does not exist was not searched. Reporting that as "—" in the
  // same column as "searched and found nothing" is the exact defect this whole
  // arc is about: an absent baseline reading as a clean answer. Say `n/a`.
  let link: string;
  let mention: string;
  if (!existsSync(md)) {
    noNarrative++;
    link = mention = "*n/a — no .md*";
  } else {
    const prose = readFileSync(md, "utf-8");
    const hasLink = prose.includes(`](#${target})`);
    if (hasLink) linked.push(s);
    link = hasLink ? "**YES**" : "no";
    const hits = terms.filter((t) => prose.toLowerCase().includes(t.toLowerCase()));
    mention = hits.length ? hits.join(", ") : "no";
  }

  let lean: string;
  if (!targetDecl) lean = "*n/a — target has no lean.ref*";
  else if (!existsSync(leanPath)) lean = "*n/a — no .lean*";
  else lean = readFileSync(leanPath, "utf-8").includes(targetDecl.split(".").pop()!) ? "yes" : "no";

  // Cost the edge BEFORE anyone writes it. Restoring `s -> target` adds a
  // uses[] entry, and if the target sits later in the same chapter that is a
  // forward reference — the metric the detangler arc has been reducing. A
  // correct restoration can silently undo correct ordering work.
  const fwd = pointsForward(s, target);
  let direction: string;
  if (fwd === undefined) { direction = "*n/a — unplaced*"; notPlaced++; }
  else if (fwd) { direction = "**FORWARD**"; forward.push(s); }
  else direction = "backward";

  console.log(
    `| \`${s}\` | ${n.kind} | ${link} | ${mention} | ${lean} | ${g.out(s, "editorial").length} | ${direction} |`,
  );
}

if (forward.length || notPlaced) {
  console.log(
    `\n**${forward.length} of ${sources.length} would point FORWARD if restored**` +
    (notPlaced ? ` (${notPlaced} could not be placed, so they are unknown, not safe)` : "") + `.`,
  );
  if (forward.length) {
    console.log(
      `\nEach adds a forward reference to a chapter the detangler arc has been ` +
      `untangling. Restoring these needs \`foreshadows[]\`, a relocation, or a ` +
      `deliberate decision to accept the edge — not a bulk apply:\n`,
    );
    for (const s of forward) console.log(`- \`${s}\``);
  }
} else {
  console.log(`\n**None of the ${sources.length} would point forward if restored.**`);
}

const searched = sources.length - noNarrative;
console.log(
  `\n**${linked.length} of ${searched} searchable blocks link to the target from their prose** ` +
  `(${noNarrative} of ${sources.length} have no \`.md\` and were not searched at all).`,
);
if (linked.length) {
  console.log(
    `\nFor those, the narrative is sending the reader to \`${target}\` while \`uses[]\` ` +
    `omits it. That is the editorial relation contradicting itself in the same block, ` +
    `not a matter of taste:\n`,
  );
  for (const s of linked) console.log(`- \`${s}\``);
}
