#!/usr/bin/env bun
/**
 * block-manifest-audit — find content blocks whose `.ts` manifest the pipeline
 * cannot load, so the block silently never enters the paper.
 *
 * ## Why this exists
 *
 * `run-validate` walks the **chapter manifests'** block lists. It never walks
 * the filesystem. So a `<block>.ts` that fails to import, exports nothing under
 * `default`, or carries a label the schema rejects is not a validation error —
 * it is simply invisible. Validation stays green and the block is absent from
 * the rendered paper with no diagnostic anywhere.
 *
 * Measured 2026-08-15 across 3603 blocks with a `.ts` sibling: **five** were in
 * this state, three of them since June/July.
 *
 *   - `mass-theory/atomic-q-reeb-universal-rho`
 *       `import { ContentBlock } from "../../pipeline/content-block"`
 *   - `mass-endomorphism/qbeta-toroidal-harmonics-basis`
 *       `import { Proposition } from "../../ontologist"`
 *   - `nuclear-interactions/audit/wigner-su4-alpha-cluster-probe`
 *       `import { Block } from "../../../../../schema/block-schema"`  (5 levels
 *       up leaves the repository entirely)
 *   - `appendix-mass-binding-algorithms/delta-max-numerical-scale`
 *       `proposition({ label: "audit:…" })` — the schema requires `prop:`
 *   - `unital-groebner-bases-chapter/ugb-main-theorem-proof`
 *       `proof({ label: "proof:…" })` — the schema requires `prf:`
 *
 * **None of the three import targets has ever existed** — `git log --all` on
 * each path returns zero commits. They were authored against invented APIs and
 * never worked for a moment. Each landed in a commit whose message announces
 * the content ("codify universal-rho normalisation and the 1.67% mirror
 * asymmetry prediction", "draft toroidal harmonics basis in paper"), so the
 * history overstates what is in the paper.
 *
 * That is the cost this audit exists to prevent: not a broken build, but a
 * confident commit message for content that never arrived. A block in this
 * state also gets no `.qa.json` criteria refreshed against it, so every
 * per-block checker — one-voice, canonical-watcher, q-usage, devils-advocate —
 * skips it too.
 *
 * ## What counts as an offender
 *
 * A `<block>.md` with a `<block>.ts` sibling where importing the `.ts` throws,
 * or its `default` export is absent or is not a schema block. The three failure
 * shapes seen so far are a nonexistent import target, a label whose prefix does
 * not match the builder's kind, and a manifest that exports only a *named*
 * const (so `default` is `undefined`).
 *
 * `.md` files with no `.ts` sibling are **not** offenders — table-data and
 * fragment files legitimately have none, and they are reported separately.
 *
 * ## Usage
 *
 *   bun run --preload ./scripts/preload-registry.ts \
 *     content/pipeline/block-manifest-audit.ts [--diff <files…>] [--quiet]
 *
 * The `--preload` is required: manifests carrying witnessed `:val` values need
 * `configureValueRegistry()` to have run, and without it every such block
 * throws "Value registry not configured" and is misreported as an offender.
 *
 * Survey mode (default) prints the offenders and exits 0. `--diff <files…>`
 * restricts to the named paths and exits 1 if any of them is an offender —
 * that is the pre-commit gate.
 *
 * ## `--orphans`: the other way content goes missing
 *
 * A manifest that loads perfectly still contributes nothing if no chapter
 * lists the block, or if no paper lists the chapter. Same end state — content
 * on disk, absent from the paper — reached by a different route, so it is
 * reported by the same tool.
 *
 * Inclusion is a two-level walk and BOTH levels are checked, because either
 * can drop content on its own:
 *
 *   paper `<paper>.ts` → `chapters: [chapterRef({dir})]`
 *                      → chapter `<dir>/<dir>.ts` → `sections[].blocks[]`
 *                        (recursing through `subsections`)
 *
 * Measured 2026-08-15 across all five paper directories. QOU is clean at the
 * chapter level (36/36 included) with 10 unlisted blocks, 3 of which are the
 * unloadable manifests above and 6 of which are `fluid-dynamics`.
 * `fred2005-formal-groups`, `bach2013-double-slit` and `visualizer` are clean
 * on both levels. `unital-groebner-bases` carries a whole second generation of
 * itself — 2 of its 3 chapter directories
 * (`introduction`, `buchberger-and-pbw`, 8 blocks) are absent from the paper
 * manifest, and 5 further blocks in the included chapter's directory are not
 * listed by it. Those 13 are internally consistent — the excluded chapters'
 * `uses[]` point at the unlisted blocks — so it reads as a superseded rewrite
 * whose files were never removed, not as damage.
 *
 * Note this is a survey, not a defect list: a block may be parked on disk on
 * purpose. What the tool asserts is only that it is not in the paper.
 */

import { readFileSync, existsSync, readdirSync, statSync } from "fs";
import { execSync } from "child_process";
import { dirname, basename, resolve, join } from "path";

const REPO = resolve(import.meta.dir, "../..");

interface Offender {
  block: string;
  reason: string;
}

async function classify(mdPath: string): Promise<Offender | null> {
  const dir = dirname(mdPath);
  const root = basename(mdPath, ".md");
  const tsPath = `${dir}/${root}.ts`;
  if (!existsSync(tsPath)) return null;

  let mod: Record<string, unknown>;
  try {
    mod = await import(tsPath);
  } catch (e) {
    const msg = String((e as Error).message).replace(/\s+/g, " ").trim();
    return { block: mdPath, reason: `manifest does not import — ${msg.slice(0, 160)}` };
  }

  const block = mod.default as { kind?: unknown } | undefined;
  if (block === undefined) {
    const named = Object.keys(mod).filter((k) => k !== "default");
    return {
      block: mdPath,
      reason:
        `no \`default\` export` +
        (named.length ? ` (only named: ${named.slice(0, 3).join(", ")})` : ""),
    };
  }
  if (typeof block !== "object" || block === null || typeof block.kind !== "string") {
    return { block: mdPath, reason: "`default` export is not a schema block (no `kind`)" };
  }
  return null;
}

function listMarkdown(): string[] {
  return execSync(
    `find ${REPO}/content -name '*.md' -not -path '*/.lake/*' -not -path '*/node_modules/*'`,
    { encoding: "utf8", maxBuffer: 1 << 28 },
  )
    .trim()
    .split("\n")
    .filter(Boolean);
}

const rel = (p: string) => p.replace(`${REPO}/`, "");

/** Every block root-name a chapter lists, recursing through subsections. */
function listedBlocks(section: { blocks?: unknown[]; subsections?: unknown[] }, out: Set<string>) {
  for (const b of section.blocks ?? []) if (typeof b === "string") out.add(b);
  for (const s of section.subsections ?? []) listedBlocks(s as never, out);
}

/** Chapter directories on disk: a subdir `d` holding `d/d.ts`. */
function chapterDirsOnDisk(paperDir: string): string[] {
  return readdirSync(paperDir).filter(
    (d) => statSync(join(paperDir, d)).isDirectory() && existsSync(join(paperDir, d, `${d}.ts`)),
  );
}

/** Block roots on disk under a chapter dir (an `.md` with a `.ts` sibling). */
function blocksOnDisk(chapterDir: string, chapterName: string): string[] {
  const out: string[] = [];
  const walk = (cur: string) => {
    for (const f of readdirSync(cur)) {
      const fp = join(cur, f);
      if (statSync(fp).isDirectory()) { walk(fp); continue; }
      if (!f.endsWith(".md")) continue;
      const root = f.slice(0, -3);
      if (root === chapterName) continue; // the chapter manifest itself
      if (existsSync(join(cur, `${root}.ts`))) out.push(root);
    }
  };
  walk(chapterDir);
  return out;
}

async function orphanSurvey(quiet: boolean): Promise<number> {
  const contentDir = `${REPO}/content`;
  const papers = readdirSync(contentDir).filter(
    (d) => statSync(join(contentDir, d)).isDirectory() && existsSync(join(contentDir, d, `${d}.ts`)),
  );

  for (const paper of papers) {
    const pdir = join(contentDir, paper);
    let manifest: { chapters?: { dir?: string }[] };
    try {
      manifest = (await import(join(pdir, `${paper}.ts`))).default;
    } catch (e) {
      console.log(`\n${paper}: paper manifest failed to load — ${String((e as Error).message).slice(0, 120)}`);
      continue;
    }

    const included = new Set((manifest.chapters ?? []).map((c) => c.dir).filter(Boolean) as string[]);
    const onDisk = chapterDirsOnDisk(pdir);
    const excludedChapters = onDisk.filter((d) => !included.has(d));
    const missingDirs = [...included].filter((d) => !onDisk.includes(d));

    // Blocks listed by the INCLUDED chapters only — a block listed solely by an
    // excluded chapter is still not in the paper.
    const listed = new Set<string>();
    for (const d of onDisk) {
      if (!included.has(d)) continue;
      try {
        const ch = (await import(join(pdir, d, `${d}.ts`))).default as { sections?: unknown[] };
        for (const s of ch.sections ?? []) listedBlocks(s as never, listed);
      } catch (e) {
        console.log(`  !! chapter ${d} failed to load — ${String((e as Error).message).slice(0, 100)}`);
      }
    }

    const unlisted: string[] = [];
    for (const d of onDisk) {
      if (!included.has(d)) continue; // excluded chapters are reported wholesale
      for (const b of blocksOnDisk(join(pdir, d), d)) if (!listed.has(b)) unlisted.push(`${d}/${b}`);
    }

    console.log(
      `\n${paper}: chapters ${included.size}/${onDisk.length} in the paper, ` +
        `${listed.size} blocks listed, ${unlisted.length} on disk but unlisted`,
    );
    if (missingDirs.length) {
      console.log(`  ⚠ paper manifest names chapter dirs that do not exist: ${missingDirs.join(", ")}`);
    }
    if (!quiet) {
      for (const d of excludedChapters) {
        console.log(`  EXCLUDED CHAPTER  ${d}  (${blocksOnDisk(join(pdir, d), d).length} blocks)`);
      }
      for (const b of unlisted.sort()) console.log(`  unlisted block    ${b}`);
    }
  }
  console.log(
    `\n  Survey only — exit 0 regardless. A block may be parked on disk on purpose;\n` +
      `  all this asserts is that it is not in the rendered paper.`,
  );
  return 0;
}

async function main(argv: string[]): Promise<number> {
  const quiet = argv.includes("--quiet");
  if (argv.includes("--orphans")) return orphanSurvey(quiet);
  const di = argv.indexOf("--diff");
  const diffMode = di !== -1;

  let candidates: string[];
  if (diffMode) {
    candidates = argv
      .slice(di + 1)
      .filter((a) => !a.startsWith("--"))
      .map((a) => (a.startsWith("/") ? a : `${REPO}/${a}`))
      // accept either sibling; audit the block either way
      .map((a) => a.replace(/\.(ts|lean|qa\.json)$/, ".md"))
      .filter((a) => a.endsWith(".md") && existsSync(a));
  } else {
    candidates = listMarkdown();
  }

  const offenders: Offender[] = [];
  let withTs = 0;
  for (const md of candidates) {
    const tsPath = `${dirname(md)}/${basename(md, ".md")}.ts`;
    if (!existsSync(tsPath)) continue;
    withTs++;
    const o = await classify(md);
    if (o) offenders.push(o);
  }

  if (diffMode) {
    if (offenders.length) {
      console.error(
        `block-manifest-audit: ${offenders.length} block(s) in this diff have a\n` +
          `manifest the pipeline cannot load. They will be absent from the rendered\n` +
          `paper, and run-validate will NOT tell you — it walks chapter manifests,\n` +
          `not the filesystem.\n`,
      );
      for (const o of offenders) console.error(`  ${rel(o.block)}\n      ${o.reason}`);
      console.error(
        `\nFix: import the builders from \`../../schema/builders\`, export the block\n` +
          `as \`default\`, and give the label the prefix its kind requires (see the\n` +
          `Type system table in AGENTS.md). Re-run to confirm.`,
      );
      return 1;
    }
    if (!quiet) console.log("block-manifest-audit: every manifest in this diff loads.");
    return 0;
  }

  console.log(
    `block-manifest-audit: ${offenders.length} of ${withTs} blocks have a manifest ` +
      `the pipeline cannot load.`,
  );
  if (!quiet) {
    for (const o of offenders) console.log(`\n  ${rel(o.block)}\n      ${o.reason}`);
    console.log(
      `\n  A block listed here is invisible: absent from the paper, and skipped by\n` +
        `  every per-block QA checker. Survey mode exits 0 regardless — use\n` +
        `  --diff <files…> to fail on manifests broken by the change at hand.`,
    );
  }
  return 0;
}

process.exit(await main(process.argv.slice(2)));
