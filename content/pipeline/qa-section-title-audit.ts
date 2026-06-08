/**
 * Title coherence + conciseness audit (chapter-scoped).
 *
 * A title is the reader's table-of-contents view of the story. The
 * ownership hierarchy is: the **paper** is responsible for its
 * **chapter** titles, each **chapter** for its **section** titles, and
 * each **section** for its **subsection** titles. Every title should be
 * (a) **short and concise** and (b) **coherent read against its
 * responsible parent** — meaningful without hunting for context.
 *
 * Two failure classes are audited:
 *
 *  1. **Mechanical / conciseness defects** (flagged automatically):
 *     - `split-artifact`  — trailing ` : <tag>` left by the
 *       chapter-restructure auto-split (e.g. "Confinement operator
 *       selection : vs", "… genus completeness : characterisation").
 *       Meaningless out of context. **Hard defect** (exit 1).
 *     - `trailing-colon`  — title ends in a bare `:`. **Hard.**
 *     - `empty`           — blank title. **Hard.**
 *     - `too-long`        — over the length budget. **Soft warn.**
 *     - `compound`        — three-plus comma-joined concepts
 *       ("A, B, C, and D"); not concise. **Soft warn.**
 *     - `duplicate` / `sibling-echo` — same title twice / "X : tag"
 *       beside a sibling "X". **Soft warn.**
 *
 *  2. **Voice / story coherence** (needs an agent): does each title,
 *     read against its responsible parent, follow the narrative and
 *     stand on its own? Emitted as a per-chapter worklist
 *     (`todos/section-title-audit.json`, gitignored) carrying the
 *     parent chain so an agent can adjudicate. Criterion id:
 *     `voice-section-title-coherence` (chapter-scoped; see the note in
 *     `qa-criteria-registry.ts`). This audit is NOT a per-block sweep
 *     criterion — titles live in chapter manifests, not blocks.
 *
 * Math (`$…$`) is stripped before colon/length checks so signature
 * titles ("… $\mathrm{st} : \mathbf{No} \to \mathbb{R}$") and
 * legitimate subtitles ("Mass predictions: per-particle …") are not
 * mis-flagged — only the trailing ` : <tag>` artifact / bare trailing
 * colon are hard defects.
 *
 * Usage:
 *   bun run content/pipeline/qa-section-title-audit.ts             # all papers
 *   bun run content/pipeline/qa-section-title-audit.ts <paper>     # one paper
 *   bun run content/pipeline/qa-section-title-audit.ts --report-only   # never exit 1
 *   bun run content/pipeline/qa-section-title-audit.ts --max-len 64    # length budget
 *
 * @module content/pipeline/qa-section-title-audit
 */
import { readdirSync, existsSync, mkdirSync, writeFileSync, statSync } from "node:fs";
import { resolve, dirname, join } from "node:path";
import { pathToFileURL } from "node:url";

process.chdir(resolve(import.meta.dir, "..", ".."));

const args = process.argv.slice(2);
const reportOnly = args.includes("--report-only");
const maxLenIdx = args.indexOf("--max-len");
const MAX_LEN = maxLenIdx >= 0 ? Number(args[maxLenIdx + 1]) : 72;
const paperArg = args.find((a) => !a.startsWith("--") && a !== String(MAX_LEN));

// Trailing ` : <one lowercase word>` is the auto-split artifact. The
// observed tag vocabulary; any single lowercase trailing word matches.
const SPLIT_TAGS = new Set([
  "vs", "generation", "characterisation", "characterization",
  "comparison", "construction", "unique", "foundations", "continued",
]);

type FlagKind =
  | "split-artifact" | "trailing-colon" | "empty"            // hard
  | "too-long" | "compound" | "duplicate" | "sibling-echo";  // soft
const HARD: ReadonlySet<FlagKind> = new Set(["split-artifact", "trailing-colon", "empty"]);

interface TitleNode {
  paper: string;
  chapterDir: string;
  /** depth 0 = chapter title, 1 = section, 2+ = subsection. */
  depth: number;
  title: string;
  label?: string;
  /** Title of the responsible parent (paper title for a chapter,
   *  chapter title for a section, section title for a subsection). */
  parent: string;
}
interface Flag { node: TitleNode; kind: FlagKind; detail: string }

function stripMath(t: string): string {
  return t.replace(/\$\$[\s\S]*?\$\$/g, "§").replace(/\$[^$]*\$/g, "§");
}

function findChapterManifests(paperFilter?: string): string[] {
  const out: string[] = [];
  const contentDir = resolve("content");
  for (const paper of readdirSync(contentDir)) {
    if (paperFilter && paper !== paperFilter) continue;
    // Skip tooling / dependency dirs — only paper dirs hold chapters.
    if (paper === "node_modules" || paper === "schema" || paper === "pipeline" || paper.startsWith(".")) continue;
    const paperPath = join(contentDir, paper);
    try { if (!statSync(paperPath).isDirectory()) continue; } catch { continue; }
    let dirs: string[];
    try { dirs = readdirSync(paperPath); } catch { continue; }
    for (const ch of dirs) {
      const chPath = join(paperPath, ch);
      let isDir = false;
      try { isDir = statSync(chPath).isDirectory(); } catch { /* */ }
      if (!isDir) continue;
      const manifest = join(chPath, `${ch}.ts`);
      if (existsSync(manifest)) out.push(manifest);
    }
  }
  return out;
}

function walkSections(
  sections: unknown,
  ctx: { paper: string; chapterDir: string },
  depth: number,
  parent: string,
  acc: TitleNode[],
): void {
  if (!Array.isArray(sections)) return;
  for (const s of sections as Array<Record<string, unknown>>) {
    if (s && typeof s.title === "string") {
      acc.push({ ...ctx, depth, title: s.title, label: typeof s.label === "string" ? s.label : undefined, parent });
      if (Array.isArray(s.subsections)) walkSections(s.subsections, ctx, depth + 1, s.title, acc);
    }
    // SectionRef (no inline title) — its title lives in a referenced
    // file and is audited when present as an inline section.
  }
}

function flagNode(n: TitleNode): Flag[] {
  const flags: Flag[] = [];
  const bare = stripMath(n.title).trim();
  if (bare === "") { flags.push({ node: n, kind: "empty", detail: "blank title" }); return flags; }
  const split = bare.match(/\s:\s+([a-z][a-z-]*)$/);
  if (split) {
    const known = SPLIT_TAGS.has(split[1]) ? " (known auto-split tag)" : "";
    flags.push({ node: n, kind: "split-artifact", detail: `trailing " : ${split[1]}"${known} — meaningless out of context` });
  } else if (/:$/.test(bare)) {
    flags.push({ node: n, kind: "trailing-colon", detail: 'title ends in ":"' });
  }
  if (bare.length > MAX_LEN) flags.push({ node: n, kind: "too-long", detail: `${bare.length} chars > ${MAX_LEN}` });
  const commas = (bare.match(/,/g) ?? []).length;
  if (commas >= 2) flags.push({ node: n, kind: "compound", detail: `${commas + 1} comma-joined concepts — not concise` });
  return flags;
}

async function main(): Promise<void> {
  const manifests = findChapterManifests(paperArg);
  const allNodes: TitleNode[] = [];
  const importErrors: string[] = [];
  // Cache paper titles for the chapter-title parent context.
  const paperTitle = new Map<string, string>();

  for (const m of manifests) {
    const chapterDir = dirname(m).split("/").pop() ?? "?";
    const paper = dirname(dirname(m)).split("/").pop() ?? "?";
    if (!paperTitle.has(paper)) {
      const pm = resolve("content", paper, `${paper}.ts`);
      try {
        const pmod = (await import(pathToFileURL(pm).href)) as { default?: { title?: string } };
        paperTitle.set(paper, pmod.default?.title ?? paper);
      } catch { paperTitle.set(paper, paper); }
    }
    let mod: { default?: Record<string, unknown> };
    try { mod = (await import(pathToFileURL(resolve(m)).href)) as { default?: Record<string, unknown> }; }
    catch (e) { importErrors.push(`${chapterDir}: ${(e as Error).message.split("\n")[0]}`); continue; }
    const ch = mod.default;
    if (!ch || typeof ch.title !== "string") continue;
    // depth 0: the chapter title (paper is responsible).
    allNodes.push({ paper, chapterDir, depth: 0, title: ch.title, label: typeof ch.label === "string" ? ch.label : undefined, parent: paperTitle.get(paper)! });
    walkSections(ch.sections, { paper, chapterDir }, 1, ch.title, allNodes);
  }

  const flags: Flag[] = [];
  for (const n of allNodes) flags.push(...flagNode(n));

  // Duplicate + sibling-echo, scoped within a chapter's own sections.
  const byChapter = new Map<string, TitleNode[]>();
  for (const n of allNodes) {
    const key = `${n.paper}/${n.chapterDir}`;
    const arr = byChapter.get(key) ?? (byChapter.set(key, []), byChapter.get(key)!);
    arr.push(n);
  }
  for (const [, nodes] of byChapter) {
    const counts = new Map<string, number>();
    for (const n of nodes) { if (n.depth === 0) continue; const b = stripMath(n.title).trim(); counts.set(b, (counts.get(b) ?? 0) + 1); }
    for (const n of nodes) {
      if (n.depth === 0) continue;
      const b = stripMath(n.title).trim();
      if ((counts.get(b) ?? 0) > 1) flags.push({ node: n, kind: "duplicate", detail: `appears ${counts.get(b)}× in chapter` });
      const sp = b.match(/^(.*\S)\s:\s+[a-z][a-z-]*$/);
      if (sp && counts.has(sp[1])) flags.push({ node: n, kind: "sibling-echo", detail: `"${sp[1]}" is itself a sibling section — confirmed auto-split pair` });
    }
  }

  // ── Report ────────────────────────────────────────────────────
  const hard = flags.filter((f) => HARD.has(f.kind));
  const soft = flags.filter((f) => !HARD.has(f.kind));
  console.log(`section-title audit: ${allNodes.length} titles across ${byChapter.size} chapters (max-len ${MAX_LEN})`);
  if (importErrors.length) console.log(`  (${importErrors.length} manifest(s) un-importable — skipped)`);

  const show = (label: string, fs: Flag[]) => {
    if (!fs.length) { console.log(`  ✓ no ${label}`); return; }
    console.log(`\n  ${fs.length} ${label}:`);
    for (const f of fs) {
      const d = f.node.depth === 0 ? "chapter" : f.node.depth === 1 ? "section" : "subsection";
      console.log(`   [${f.kind}] ${f.node.paper}/${f.node.chapterDir} (${d}${f.node.label ? " " + f.node.label : ""})\n      "${f.node.title}"  — ${f.detail}\n        ↳ parent: "${f.node.parent}"`);
    }
  };
  show("HARD defect(s)", hard);
  show("conciseness/duplicate warning(s)", soft);

  // ── Agent worklist (ordered titles + parent chain per chapter) ─
  mkdirSync("todos", { recursive: true });
  const worklist = [...byChapter.entries()].map(([key, nodes]) => ({
    chapter: key,
    chapterTitle: nodes.find((n) => n.depth === 0)?.title ?? "",
    titles: nodes.map((n) => ({
      depth: n.depth,
      kind: n.depth === 0 ? "chapter" : n.depth === 1 ? "section" : "subsection",
      title: n.title,
      label: n.label,
      parent: n.parent,
      flags: flags.filter((f) => f.node === n).map((f) => f.kind),
    })),
  }));
  writeFileSync("todos/section-title-audit.json", JSON.stringify(
    { generated: new Date().toISOString(), max_len: MAX_LEN, total_titles: allNodes.length, hard_defects: hard.length, soft_warnings: soft.length, chapters: worklist }, null, 2));
  console.log(`\n  worklist → todos/section-title-audit.json (review each title for conciseness + coherence against its parent)`);

  if (hard.length > 0 && !reportOnly) process.exit(1);
}

main();
