#!/usr/bin/env bun
/**
 * refresh-authors-note.ts — keep the author-note's Lean-coverage numbers live.
 *
 * The introduction's author-note advertises how much of the paper is
 * Lean-formalised: how many provable claims are sorry-free, and how many
 * of the paper's own (primary) open conjectures are class-axiomatised.
 * Those numbers drift every time a proof lands or a conjecture is added,
 * so they must never be hand-typed. This script recomputes them from the
 * live content tree (via the folio-assistant `lean-coverage` tool) and
 * rewrites the numeric spans in `authors-note.md`.
 *
 *   bun run scripts/refresh-authors-note.ts          # rewrite the note in place
 *   bun run scripts/refresh-authors-note.ts --check   # CI: exit 1 if stale
 *
 * The `--check` mode is the drift gate: it recomputes the numbers and
 * fails if the committed note disagrees, without writing. Wire it into
 * validate/CI so a landed proof that isn't reflected in the note is caught.
 *
 * Definition of the advertised numbers (see lean-coverage.ts):
 *   - provable sorry-free / total: theorem+lemma+proposition+corollary
 *     blocks whose resolved .lean (sibling or lean.ref library file) is
 *     sorry-free, over all such blocks.
 *   - primary open conjectures: the paper's OWN root conjectures — QOU
 *     conjectures excluding famous external problems (tag `tier:famous`)
 *     and excluding those conditional on another conjecture (dependent,
 *     per CLAUDE.md §3b-tax). Class-axiomatised = carries a Lean `class`.
 */

import { readFileSync, writeFileSync } from "fs";
import { join, resolve } from "path";
// The platform (content pipeline + this tool) lives in the sibling
// folio-assistant repo, wired in via the in-repo `folio-assistant/` symlink
// (scripts/setup-folio-assistant.sh). Run that once if this import fails.
import { computeStats } from "../folio-assistant/folio-assistant-sci/scripts/lean-coverage";

const REPO_ROOT = resolve(import.meta.dir, "..");
const PAPER = "quantum-observable-universe";
const CONTENT_ROOT = join(REPO_ROOT, "folio");
const NOTE = join(CONTENT_ROOT, PAPER, "introduction", "authors-note.md");
const WITNESS = join(CONTENT_ROOT, PAPER, "introduction", "lean-coverage.json");

/** Each rule locates a numeric span in the note and supplies its live value. */
interface Rule {
  name: string;
  re: RegExp;
  make: (s: ReturnType<typeof computeStats>) => string;
}

const RULES: Rule[] = [
  {
    name: "provable-sorry-free",
    re: /\*\*[\d,]+ of [\d,]+ \([\d.]+%\) provable claims\*\*/,
    make: (s) =>
      `**${s.provable.sorry_free} of ${s.provable.total} ` +
      `(${s.provable.percent_sorry_free}%) provable claims**`,
  },
  {
    name: "primary-conjectures",
    re: /\*\*\d+ primary open conjectures\*\*/,
    make: (s) => `**${s.conjectures.primary} primary open conjectures**`,
  },
  {
    name: "primary-class-axiomatised",
    re: /\*\*\d+ \([\d.]+%\) are class-axiomatised in Lean\*\*/,
    make: (s) =>
      `**${s.conjectures.primary_class_axiomatized} ` +
      `(${s.conjectures.percent_primary_class_axiomatized}%) ` +
      `are class-axiomatised in Lean**`,
  },
];

function main() {
  const check = process.argv.includes("--check");
  const stats = computeStats(PAPER, CONTENT_ROOT);
  const before = readFileSync(NOTE, "utf-8");

  let after = before;
  const problems: string[] = [];
  // A rule whose span is MISSING is not drift: the note's structure changed,
  // so that number is no longer maintained. Write mode used to report success
  // anyway; it now refuses, as --check always did (T11 audit, bean qou-aq9i).
  const missing: string[] = [];
  for (const rule of RULES) {
    const want = rule.make(stats);
    const m = after.match(rule.re);
    if (!m) {
      const line = `  ✗ ${rule.name}: no span matching ${rule.re} found in the note`;
      problems.push(line);
      missing.push(line);
      continue;
    }
    if (m[0] !== want) {
      problems.push(`  ✗ ${rule.name}: note says "${m[0]}" but live is "${want}"`);
    }
    // Function replacer: returns `want` verbatim, with no `$`/`$&`/`$1`
    // special-pattern expansion (a string replacement would treat `$` in a
    // future rule's value specially and corrupt the note).
    after = after.replace(rule.re, () => want);
  }

  // Witness: numeric snapshot for CI diffing (timestamp-free so it is stable).
  const { generated_at, ...stable } = stats;
  const witness = JSON.stringify(stable, null, 2) + "\n";

  if (check) {
    if (problems.length) {
      console.error("author-note Lean-coverage stats are STALE:");
      console.error(problems.join("\n"));
      console.error("\nRun: bun run scripts/refresh-authors-note.ts");
      process.exit(1);
    }
    console.log("author-note Lean-coverage stats are current.");
    return;
  }

  if (missing.length) {
    console.error("author-note: cannot refresh, rule span(s) missing from the note:");
    console.error(missing.join("\n"));
    process.exit(1);
  }
  if (after !== before) writeFileSync(NOTE, after);
  writeFileSync(WITNESS, witness);
  console.log(
    `author-note refreshed: ${stats.provable.sorry_free}/${stats.provable.total} ` +
    `provable sorry-free (${stats.provable.percent_sorry_free}%); ` +
    `${stats.conjectures.primary} primary conjectures, ` +
    `${stats.conjectures.primary_class_axiomatized} class-axiomatised ` +
    `(${stats.conjectures.percent_primary_class_axiomatized}%).`,
  );
  if (after !== before) console.log(`  wrote ${NOTE}`);
  console.log(`  wrote ${WITNESS}`);
}

main();
