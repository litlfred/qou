#!/usr/bin/env npx tsx
// Node.js-compatible wrapper for content/pipeline/build.ts
// Works around Bun-specific import.meta.dir/main used in the pipeline.
// Usage: npx tsx scripts/docker-latex-build/run-build.ts [same args as pipeline/build.ts]

import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { existsSync, mkdirSync, writeFileSync } from "node:fs";

const __dirname = dirname(fileURLToPath(import.meta.url));
const contentDir = resolve(__dirname, "../../content");
const pipelineDir = join(contentDir, "pipeline");

// Patch import.meta.dir for modules that use it (Bun-specific)
// @ts-ignore
if (!import.meta.dir) Object.defineProperty(import.meta, "dir", { get: () => pipelineDir });

// Dynamic import of the build modules
const buildMod = await import(join(pipelineDir, "build.ts"));
const { buildPaper } = buildMod;
const mainTexMod = await import(join(pipelineDir, "generate-main-tex.ts"));
const { generateMainTex, generateStandaloneTex } = mainTexMod;

// Parse CLI args (same interface as pipeline/build.ts)
const args = process.argv.slice(2);
const defaultPaper = join(contentDir, "quantum-observable-universe/quantum-observable-universe.ts");
const paperPath = resolve(args[0] || defaultPaper);
const outDirIdx = args.indexOf("--out-dir");
const outDir = resolve(outDirIdx >= 0 ? args[outDirIdx + 1] : join(contentDir, "../chapters"));

const printModeIdx = args.indexOf("--print-mode");
const printMode = (printModeIdx >= 0 ? args[printModeIdx + 1] : "compact") as "formal" | "compact";
const noInlineRefs = args.includes("--no-inline-refs");

console.log(`Building paper: ${paperPath}`);
console.log(`Output dir: ${outDir}`);
console.log(`Print mode: ${printMode}${noInlineRefs ? " (inline refs disabled)" : ""}\n`);

const result = await buildPaper(paperPath, {
  printMode,
  compactInlineRefs: !noInlineRefs,
});

// Print issues
for (const issue of result.issues) {
  const icon = issue.level === "error" ? "✗" : issue.level === "warning" ? "⚠" : "ℹ";
  console.log(`  ${icon} ${issue.message}`);
}

// Write chapter output
if (!existsSync(outDir)) mkdirSync(outDir, { recursive: true });

for (const [num, latex] of result.chapters) {
  const slug = result.chapterSlugs.get(num);
  const filename = slug ? `${slug}.tex` : `chapter-${num}.tex`;
  const outPath = join(outDir, filename);
  writeFileSync(outPath, latex);
  console.log(`  → ${outPath}`);
}

// Generate main.tex from paper manifest + shared preamble
if (args.includes("--generate-main")) {
  const mainOutIdx = args.indexOf("--main-out");
  const mainOutPath = resolve(mainOutIdx >= 0 ? args[mainOutIdx + 1] : "main.tex");
  const preambleIdx = args.indexOf("--preamble");
  const preamblePath = resolve(
    preambleIdx >= 0 ? args[preambleIdx + 1] : join(contentDir, "../latex/preamble.tex"),
  );
  const chaptersDirIdx = args.indexOf("--chapters-dir");
  const chaptersDir = chaptersDirIdx >= 0 ? args[chaptersDirIdx + 1] : "chapters/";

  const paperMod = await import(paperPath);
  const paperData = paperMod.default;

  const excludeChapterIndices = new Set(result.appendixChapters.keys());

  const mainTex = generateMainTex(paperData, {
    preamblePath,
    chaptersDir,
    chapterSlugs: result.chapterSlugs,
    excludeChapterIndices,
    phantomLabels: result.appendixPhantomLabels,
  });
  writeFileSync(mainOutPath, mainTex);
  console.log(`\n  → main.tex: ${mainOutPath}`);

  // Generate standalone .tex files for each appendix chapter
  if (generateStandaloneTex) {
    for (const [idx, latex] of result.appendixChapters) {
      const slug = result.chapterSlugs.get(idx);
      if (!slug) continue;
      const standaloneTex = generateStandaloneTex(paperData, {
        preamblePath,
        chapterSlug: slug,
        chapterLatex: latex,
        chaptersDir,
      });
      const standaloneOut = resolve(join(outDir, `../standalone-${slug}.tex`));
      writeFileSync(standaloneOut, standaloneTex);
      console.log(`  → standalone: ${standaloneOut}`);
    }
  }
}

const errorCount = result.issues.filter((i: any) => i.level === "error").length;
const warnCount = result.issues.filter((i: any) => i.level === "warning").length;
console.log(`\n${errorCount ? "✗" : "✓"} Build complete — ${errorCount} error(s), ${warnCount} warning(s)`);
