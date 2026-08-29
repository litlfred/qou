/**
 * Blocks whose `.md` announces that it superseded an earlier form — do their
 * Lean siblings still state the old one?
 *
 * Two confirmed cases motivated this, and both were found by hand:
 * `em-coupling-chern-simons` (PR #5931) and `centered-hecke-variance-positive`
 * (PR #5936). In each, the `.md` names a formula it "previously displayed" while
 * the Lean still displayed it — the second for nineteen days, carrying a figure
 * the `.md` had explicitly withdrawn.
 *
 * WHAT THIS IS NOT.  It is not a content comparison. It cannot tell whether a
 * block's Lean agrees with its `.md`; it only finds the blocks where the `.md`
 * *says* it moved, which is where disagreement is most likely and cheapest to
 * check. The verdict is an agent's, not this script's.
 *
 * WHY IT IS A LOWER BOUND, stated up front so the count is not over-read: a
 * block corrected *silently* — no "previously read" sentence — will not match.
 * The true population is unknown and is at least the number reported here.
 *
 * A REFUTED ALTERNATIVE, recorded so it is not re-attempted (bean `qou-mdlv`).
 * The obvious cheaper detector is "`.md` committed after its `.lean`". Measured
 * over all 931 blocks with a sibling `.lean`: 100 show that skew and **neither
 * known positive is among them**. Commit order measures who was edited last, not
 * whether the two agree — any unrelated touch to a stale `.lean` resets its
 * timestamp, so the signal is anti-correlated with the defect.
 *
 * RESOLVING THE LEAN.  Per AGENTS.md §0a a block's `lean.ref` resolves to a
 * sibling `.lean` OR to a library file under the package's Lake root. Half the
 * known positives are the library shape, so a sibling-only scan misses them.
 * That is the one thing this script must get right.
 *
 * @module content/pipeline/superseded-block-lean-audit
 */
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { join, dirname, basename } from "node:path";

/** Prose that announces the block moved on from an earlier form. */
const SUPERSESSION =
  /previously displayed|previously stated|previously read|superseded (form|version)|earlier form of this|this (proposition|theorem|lemma|definition|conjecture) previously/i;

interface Finding {
  block: string;
  sentence: string;
  lean: string | null;
  leanKind: "sibling" | "library" | "none";
}

function* walk(dir: string): Generator<string> {
  for (const e of readdirSync(dir)) {
    if (e === "node_modules" || e.startsWith(".")) continue;
    const p = join(dir, e);
    if (statSync(p).isDirectory()) yield* walk(p);
    else if (p.endsWith(".md")) yield p;
  }
}

/** Resolve a block's Lean: sibling first, then the `lean.ref` library path. */
function resolveLean(md: string): { path: string | null; kind: Finding["leanKind"] } {
  const sibling = md.replace(/\.md$/, ".lean");
  if (existsSync(sibling)) return { path: sibling, kind: "sibling" };

  const ts = md.replace(/\.md$/, ".ts");
  if (!existsSync(ts)) return { path: null, kind: "none" };
  const ref = readFileSync(ts, "utf8").match(/ref:\s*"([^"]+)"/)?.[1];
  if (!ref) return { path: null, kind: "none" };

  // "qou:QOU.Observations.foo" -> content/<paper>/lean/QOU/Observations/foo.lean
  const decl = ref.includes(":") ? ref.split(":")[1] : ref;
  const parts = md.split("/");
  const paperRoot = parts.slice(0, 2).join("/"); // content/<paper>
  const candidate = join(paperRoot, "lean", decl.replace(/\./g, "/") + ".lean");
  if (existsSync(candidate)) return { path: candidate, kind: "library" };

  // Decl name and file name may differ; fall back to the containing directory.
  const dir = join(paperRoot, "lean", decl.split(".").slice(0, -1).join("/"));
  if (existsSync(dir)) {
    const leaf = decl.split(".").pop()!;
    for (const f of readdirSync(dir)) {
      if (f.endsWith(".lean") && basename(f, ".lean") === leaf)
        return { path: join(dir, f), kind: "library" };
    }
  }
  return { path: null, kind: "none" };
}

const root = process.argv[2] ?? "content";
const findings: Finding[] = [];

for (const md of walk(root)) {
  if (md.endsWith(".qa.json")) continue;
  const text = readFileSync(md, "utf8");
  const line = text.split("\n").find((l) => SUPERSESSION.test(l));
  if (!line) continue;
  const { path, kind } = resolveLean(md);
  findings.push({ block: md, sentence: line.trim().slice(0, 150), lean: path, leanKind: kind });
}

const withLean = findings.filter((f) => f.leanKind !== "none");
console.log(`  blocks announcing a supersession : ${findings.length}`);
console.log(`  ...of which have Lean            : ${withLean.length}` +
  `  (sibling ${withLean.filter((f) => f.leanKind === "sibling").length},` +
  ` library ${withLean.filter((f) => f.leanKind === "library").length})`);
console.log(`  ...no Lean, nothing to diverge   : ${findings.length - withLean.length}`);
console.log();
console.log("  NEEDS AN AGENT VERDICT — does the Lean still state the superseded form?");
for (const f of withLean) {
  console.log(`\n    ${f.block}`);
  console.log(`      lean (${f.leanKind}): ${f.lean}`);
  console.log(`      says: ${f.sentence}`);
}
console.log(
  "\n  This is a LOWER BOUND: a silently-corrected block carries no such sentence.",
);
