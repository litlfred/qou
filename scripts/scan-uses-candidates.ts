#!/usr/bin/env bun
/**
 * Surface `uses[]` restoration candidates: labels a block's own prose names
 * that its manifest does not declare.
 *
 * ## What it is for
 *
 * Two bulk transitive prunes removed 783 dependencies no surviving path
 * replaces (bean `prn1`). The strongest restoration candidates are the ones a
 * second, independent record still attests to — the block's own narrative. If
 * A's `.md` names B by label and A's `uses[]` does not reach B, two unrelated
 * sources disagree, and one of them is wrong.
 *
 * This is a "declares some, names more" scan, so unlike the completeness scan
 * (`fwr10`, which selects blocks with an EMPTY `uses[]`) it also reaches
 * blocks that lost edges without being emptied — the `rem:millennium-unification`
 * case `prn1` flagged as undetectable.
 *
 * ## It proposes; it does not decide
 *
 * Every row is a CANDIDATE. The judgement — is this a prerequisite a reader
 * must have read, or merely a comparison, an aside, a generalisation, a
 * pointer to future work? — requires reading the citing sentence. Four filters
 * below remove work that is already settled; nothing removes the need to read.
 *
 * ## The four filters (see docs/audits/uses-edge-rejections.json)
 *
 *   1. rejection ledger — permanent judgements, recorded because they are
 *      permanent.
 *   2. foreshadows — a target already recorded as a forward POINTER is not a
 *      dependency candidate.
 *   3. transitive reachability — the schema requires immediate neighbours
 *      only, so an already-reachable target is redundant by construction.
 *      COMPUTED, never ledgered: reachability is state-dependent, and a ledger
 *      row would suppress the candidate forever even after the intermediate
 *      edge is removed.
 *   4. direction — a forward-pointing candidate is not a `uses[]` edge at all.
 *
 * Usage:
 *   bun run scripts/scan-uses-candidates.ts <paper-dir> [--json] [--all]
 *
 * `--all` reports what each filter removed instead of only the survivors.
 */
import { readFileSync, existsSync, readdirSync } from "node:fs";
import { join } from "node:path";
import {
  parseForeshadows,
  parseMdBlockRefs,
  parseManifestStringArray,
} from "../folio-assistant/content/pipeline/qa-checkers-extended";

// The CONTENT repo's content/ — an import-relative path lands in
// folio-assistant/content, which holds only pipeline/, and every paper lookup
// would miss while the scan cheerfully reported zero candidates.
const REPO = join(import.meta.dir, "..");
const CONTENT_DIR = join(REPO, "content");

interface Candidate {
  source: string;
  target: string;
  sourceChapter: string;
  targetChapter: string;
  sourceFile: string;
}

interface ScanResult {
  candidates: Candidate[];
  removed: Record<string, number>;
  totals: { blocks: number; raw: number; surviving: number };
}

export function scan(paper: string): ScanResult {
  const paperDir = join(CONTENT_DIR, paper);
  const paperTs = join(paperDir, `${paper}.ts`);
  if (!existsSync(paperTs)) throw new Error(`no paper manifest: ${paperTs}`);
  const dirs = [...readFileSync(paperTs, "utf-8").matchAll(/dir:\s*"([^"]+)"/g)].map(
    (m) => m[1],
  );

  const slugToLabel = new Map<string, string>();
  const uses = new Map<string, string[]>();
  const foreshadows = new Map<string, Set<string>>();
  const mdRefs = new Map<string, string[]>();
  const chapterOf = new Map<string, string>();
  const fileOf = new Map<string, string>();

  for (const dir of dirs) {
    const chDir = join(paperDir, dir);
    if (!existsSync(chDir)) continue;
    for (const f of readdirSync(chDir)) {
      if (!f.endsWith(".ts") || f === `${dir}.ts`) continue;
      const src = readFileSync(join(chDir, f), "utf-8");
      const m = src.match(/label:\s*"([^"]+)"/);
      if (!m) continue;
      const label = m[1];
      slugToLabel.set(f.slice(0, -3), label);
      // The SHIPPED parser, never a local regex. A hand-rolled one reads
      // commented-out entries and prose inside comments as real array members;
      // see docs/audits/2026-08-11-manifest-regex-vs-ts-divergence.md.
      uses.set(label, parseManifestStringArray(src, "uses"));
      foreshadows.set(label, new Set(parseForeshadows(src)));
      chapterOf.set(label, dir);
      fileOf.set(label, join(dir, f));
      const md = join(chDir, `${f.slice(0, -3)}.md`);
      if (existsSync(md)) mdRefs.set(label, parseMdBlockRefs(readFileSync(md, "utf-8")));
    }
  }

  // Reading order, from each chapter manifest's ordered sections[].blocks[].
  const pos = new Map<string, number>();
  const STRIDE = 100_000;
  dirs.forEach((dir, ci) => {
    const mf = join(paperDir, dir, `${dir}.ts`);
    if (!existsSync(mf)) return;
    let within = 0;
    for (const bm of readFileSync(mf, "utf-8").matchAll(/blocks\s*:\s*\[([\s\S]*?)\]/g))
      for (const sm of bm[1].matchAll(/"([^"]+)"/g)) {
        const lb = slugToLabel.get(sm[1]);
        if (lb && !pos.has(lb)) pos.set(lb, ci * STRIDE + within++);
      }
  });

  // Filter 1: the rejection ledger.
  const rejected = new Set<string>();
  const ledgerPath = join(REPO, "docs/audits/uses-edge-rejections.json");
  if (existsSync(ledgerPath)) {
    const led = JSON.parse(readFileSync(ledgerPath, "utf-8"));
    for (const r of led.rejections ?? []) rejected.add(`${r.source}->${r.target}`);
  }

  // Filter 3: transitive reachability through the declared cone.
  const reaches = (from: string, to: string): boolean => {
    const seen = new Set<string>([from]);
    const stack = [...(uses.get(from) ?? [])];
    while (stack.length) {
      const cur = stack.pop()!;
      if (cur === to) return true;
      if (seen.has(cur)) continue;
      seen.add(cur);
      for (const n of uses.get(cur) ?? []) stack.push(n);
    }
    return false;
  };

  const removed: Record<string, number> = {
    unknown_label: 0,
    already_declared: 0,
    rejection_ledger: 0,
    foreshadows: 0,
    transitively_reachable: 0,
    forward: 0,
    unpositioned: 0,
  };
  const candidates: Candidate[] = [];
  let raw = 0;

  for (const [source, refs] of mdRefs) {
    const declared = new Set(uses.get(source) ?? []);
    const myPos = pos.get(source);
    for (const target of refs) {
      if (target === source) continue;
      raw++;
      if (!chapterOf.has(target)) { removed.unknown_label++; continue; }
      if (declared.has(target)) { removed.already_declared++; continue; }
      if (rejected.has(`${source}->${target}`)) { removed.rejection_ledger++; continue; }
      if (foreshadows.get(source)?.has(target)) { removed.foreshadows++; continue; }
      if (reaches(source, target)) { removed.transitively_reachable++; continue; }
      const tPos = pos.get(target);
      if (myPos === undefined || tPos === undefined) { removed.unpositioned++; continue; }
      if (tPos > myPos) { removed.forward++; continue; }
      candidates.push({
        source,
        target,
        sourceChapter: chapterOf.get(source)!,
        targetChapter: chapterOf.get(target)!,
        sourceFile: fileOf.get(source)!,
      });
    }
  }

  candidates.sort((a, b) =>
    a.sourceChapter === b.sourceChapter
      ? a.source.localeCompare(b.source) || a.target.localeCompare(b.target)
      : a.sourceChapter.localeCompare(b.sourceChapter),
  );

  return {
    candidates,
    removed,
    totals: { blocks: mdRefs.size, raw, surviving: candidates.length },
  };
}

if (import.meta.main) {
  const args = process.argv.slice(2);
  const paper = args.find((a) => !a.startsWith("--"));
  if (!paper) {
    console.error("usage: scan-uses-candidates.ts <paper-dir> [--json] [--all]");
    process.exit(2);
  }
  const r = scan(paper);
  if (args.includes("--json")) {
    console.log(JSON.stringify(r, null, 2));
  } else {
    if (args.includes("--all")) {
      console.log("removed by filter:");
      for (const [k, v] of Object.entries(r.removed)) console.log(`  ${k}: ${v}`);
      console.log("");
    }
    let cur = "";
    for (const c of r.candidates) {
      if (c.source !== cur) {
        cur = c.source;
        console.log(`\n${c.source}  [${c.sourceChapter}]`);
      }
      const x = c.sourceChapter === c.targetChapter ? " " : "X";
      console.log(`  ${x} -> ${c.target}  [${c.targetChapter}]`);
    }
    console.log(
      `\n${r.totals.surviving} candidates from ${r.totals.raw} raw prose refs across ${r.totals.blocks} blocks`,
    );
  }
}
