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
 * pointer to future work? — requires reading the citing sentence. The filters
 * below remove work that is already settled; nothing removes the need to read.
 *
 * ## How the manifests are read: by importing them
 *
 * The manifests are IMPORTED, not text-matched. Every content block is a
 * TypeScript module with a default export, so `import()` yields the same
 * object the content pipeline sees — the ground truth, with no grammar to
 * guess at.
 *
 * This matters because the regex approach has three observed failure modes,
 * all of which silently corrupt the graph while `validate` stays green: a
 * quoted string inside a comment becomes a phantom entry; an unanchored field
 * match takes a `uses:` snippet quoted earlier in the file; and a `]` inside a
 * comment truncates the array with no trace at all. See
 * `docs/audits/2026-08-11-manifest-regex-vs-ts-divergence.md`, which names
 * importing the manifest as the fix and the two regex patches as stopgaps.
 *
 * Importing also gets `interprets` for free, which a `uses[]` proposal must
 * not duplicate.
 *
 * ## The filters (see docs/audits/uses-edge-rejections.json)
 *
 *   1. rejection ledger — permanent judgements, recorded because they are
 *      permanent.
 *   2. foreshadows — a target already recorded as a forward POINTER is not a
 *      dependency candidate.
 *   3. interprets — a remark's `interprets` target is already its subject;
 *      proposing it as a dependency adds nothing.
 *   4. transitive reachability — the schema requires immediate neighbours
 *      only, so an already-reachable target is redundant by construction.
 *      COMPUTED, never ledgered: reachability is state-dependent, and a ledger
 *      row would suppress the candidate forever even after the intermediate
 *      edge is removed.
 *   5. direction — a forward-pointing candidate is not a `uses[]` edge at all.
 *
 * Reachability walks `uses[]` alone, matching the graph the detangler
 * checkers build (`loadChapterGraph` reads `uses` and deliberately excludes
 * `cites` / `interprets`).
 *
 * Usage:
 *   bun run scripts/scan-uses-candidates.ts <paper-dir> [--json] [--all]
 *
 * `--all` reports what each filter removed instead of only the survivors.
 */
import { readFileSync, existsSync, readdirSync } from "node:fs";
import { join } from "node:path";

// The CONTENT repo's content/ — an import-relative path lands in
// folio-assistant/content, which holds only pipeline/, and every paper lookup
// would miss while the scan cheerfully reported zero candidates.
const REPO = join(import.meta.dir, "..");
const CONTENT_DIR = join(REPO, "folio");

/**
 * Label tokens as they appear in prose: a known kind prefix, a colon, and a
 * slug. Restricted to the prefixes the corpus actually uses, so ordinary prose
 * punctuation ("note: the following") cannot mint a label. Every hit is
 * intersected with the real label set anyway, which is what makes a loose
 * pattern safe here.
 */
const LABEL_RE =
  /\b(?:def|thm|lem|prop|cor|conj|rem|ex|sec|chap|sim|eq|tbl|alg|fig|prf|obs|note|axm|part|app)[a-z]*:[a-z0-9][a-z0-9-]*/gi;

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

export async function scan(paper: string): Promise<ScanResult> {
  const paperDir = join(CONTENT_DIR, paper);
  const paperTs = join(paperDir, `${paper}.ts`);
  if (!existsSync(paperTs)) throw new Error(`no paper manifest: ${paperTs}`);
  const paperMod = (await import(paperTs)).default;
  const dirs: string[] = (paperMod.chapters ?? []).map((c: { dir: string }) => c.dir);

  const slugToLabel = new Map<string, string>();
  const uses = new Map<string, string[]>();
  const foreshadows = new Map<string, Set<string>>();
  const interprets = new Map<string, string | undefined>();
  const mdRefs = new Map<string, string[]>();
  const chapterOf = new Map<string, string>();
  const fileOf = new Map<string, string>();

  for (const dir of dirs) {
    const chDir = join(paperDir, dir);
    if (!existsSync(chDir)) continue;
    for (const f of readdirSync(chDir)) {
      if (!f.endsWith(".ts") || f === `${dir}.ts`) continue;
      let block: Record<string, unknown>;
      try {
        block = (await import(join(chDir, f))).default;
      } catch {
        continue; // not a block module (helper/data file)
      }
      const label = block?.label as string | undefined;
      if (!label) continue;
      slugToLabel.set(f.slice(0, -3), label);
      uses.set(label, ((block.uses as string[]) ?? []).slice());
      foreshadows.set(label, new Set((block.foreshadows as string[]) ?? []));
      interprets.set(label, block.interprets as string | undefined);
      chapterOf.set(label, dir);
      fileOf.set(label, join(dir, f));
      const md = join(chDir, `${f.slice(0, -3)}.md`);
      if (existsSync(md)) {
        const text = readFileSync(md, "utf-8");
        mdRefs.set(label, [...new Set(text.match(LABEL_RE) ?? [])]);
      }
    }
  }

  // Reading order, from each chapter manifest's ordered sections[].blocks[].
  const pos = new Map<string, number>();
  const STRIDE = 100_000;
  for (const [ci, dir] of dirs.entries()) {
    const mf = join(paperDir, dir, `${dir}.ts`);
    if (!existsSync(mf)) continue;
    const ch = (await import(mf)).default;
    let within = 0;
    for (const sec of ch.sections ?? [])
      for (const slug of sec.blocks ?? []) {
        const lb = slugToLabel.get(slug);
        if (lb && !pos.has(lb)) pos.set(lb, ci * STRIDE + within++);
      }
  }

  // Filter 1: the rejection ledger.
  const rejected = new Set<string>();
  const ledgerPath = join(REPO, "docs/audits/uses-edge-rejections.json");
  if (existsSync(ledgerPath)) {
    const led = JSON.parse(readFileSync(ledgerPath, "utf-8"));
    for (const r of led.rejections ?? []) rejected.add(`${r.source}->${r.target}`);
  }

  // Filter 4: transitive reachability through the declared `uses[]` cone.
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
    interprets: 0,
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
      if (interprets.get(source) === target) { removed.interprets++; continue; }
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
  const r = await scan(paper);
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
