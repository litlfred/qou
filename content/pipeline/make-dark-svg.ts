/**
 * make-dark-svg — produces a hand-tuned dark-mode SVG sibling
 * (`<stem>.dark.svg`) by transforming the light-mode primary.
 *
 * Use case: figures with multiple distinct accent colours (red /
 * green / blue) where the viewer's automatic CSS
 * `invert(1) hue-rotate(180deg)` filter mangles the colour scheme
 * (red → cyan, green → magenta, blue → yellow).  The dark variant
 * keeps the accents identical but flips the achromatic ground:
 * white background → near-black, black strokes → light grey.
 *
 * Run:
 *   bun run content/pipeline/make-dark-svg.ts <slug-relative-to-rendered/>...
 *
 * Example:
 *   bun run content/pipeline/make-dark-svg.ts \
 *     bring-coral-3-tubes-0  borromean-quarks-0  particle-knot-dictionary-0
 *
 * @module content/pipeline/make-dark-svg
 */

import { readFileSync, writeFileSync, existsSync, readdirSync, statSync } from "fs";
import { join, dirname, basename } from "path";

const REPO_ROOT = join(import.meta.dir, "..", "..");
const CONTENT_ROOT = join(REPO_ROOT, "content", "quantum-observable-universe");

/**
 * Substitution table: light-mode achromatic colour → dark-mode
 * counterpart.  Accent colours (#c0392b red, #27ae60 green,
 * #2980b9 blue, #e67e22 orange, #f1c40f yellow, #8e44ad purple)
 * are explicitly preserved.
 */
const SUBS: Array<[RegExp, string]> = [
  // Backgrounds
  [/fill:\s*#ffffff\b/gi, "fill: #0e0e12"],
  [/fill="#ffffff"/gi, 'fill="#0e0e12"'],
  [/fill:\s*#fafafa\b/gi, "fill: #16161c"],
  [/fill="#fafafa"/gi, 'fill="#16161c"'],
  [/fill:\s*#f5f5f5\b/gi, "fill: #18181e"],
  [/fill:\s*#f6f6f6\b/gi, "fill: #18181e"],
  [/fill:\s*#f0f0f6\b/gi, "fill: #1e1e26"],
  [/fill="#f0f0f6"/gi, 'fill="#1e1e26"'],
  [/fill:\s*#f0e6d2\b/gi, "fill: #2e2818"],
  [/fill:\s*#d2e6f0\b/gi, "fill: #182830"],
  [/fill:\s*#d2f0d2\b/gi, "fill: #182f18"],
  [/fill:\s*#f0d2d2\b/gi, "fill: #2f1818"],
  [/fill:\s*#f0e6f0\b/gi, "fill: #28202e"],
  [/fill:\s*#e6f0e6\b/gi, "fill: #1e2c1e"],
  [/fill:\s*#f0e6e6\b/gi, "fill: #2a1e1e"],

  // Strokes (black → light grey, dark grey → grey)
  [/stroke:\s*#1a1a1a\b/gi, "stroke: #e6e6ea"],
  [/stroke="#1a1a1a"/gi, 'stroke="#e6e6ea"'],
  [/stroke:\s*#888\b/gi, "stroke: #888"],   // mid-grey unchanged
  [/stroke:\s*#b8b8b8\b/gi, "stroke: #555"],
  [/stroke:\s*#c8c8c8\b/gi, "stroke: #555"],
  [/stroke:\s*#ddd\b/gi, "stroke: #444"],

  // Fills for text / glyphs
  [/fill:\s*#1a1a1a\b/gi, "fill: #e6e6ea"],
  [/fill="#1a1a1a"/gi, 'fill="#e6e6ea"'],
  [/fill:\s*#444\b/gi, "fill: #aaa"],
  [/fill="#444"/gi, 'fill="#aaa"'],
  [/fill:\s*#555\b/gi, "fill: #aaa"],
  [/fill="#555"/gi, 'fill="#aaa"'],
  [/fill:\s*#666\b/gi, "fill: #bbb"],
  [/fill="#666"/gi, 'fill="#bbb"'],
  [/fill:\s*#999\b/gi, "fill: #999"],

  // Marker tips  (path d="..." fill="#1a1a1a") — already covered by line above
  // but also catches inline: marker tip arrowheads typically use fill="#1a1a1a"
];

function transform(svg: string): string {
  let out = svg;
  for (const [re, to] of SUBS) out = out.replace(re, to);
  // Replace the SVG <title> if it doesn't already mention dark mode
  out = out.replace(
    /<title>([^<]*)<\/title>/,
    (_m, t) => `<title>${t.trim()} (dark mode)</title>`
  );
  return out;
}

function findSvg(slug: string): string | null {
  // Walk all chapter rendered/ dirs to locate <slug>.svg
  for (const ch of readdirSync(CONTENT_ROOT)) {
    const renderedDir = join(CONTENT_ROOT, ch, "rendered");
    if (!existsSync(renderedDir)) continue;
    const candidate = join(renderedDir, `${slug}.svg`);
    if (existsSync(candidate) && statSync(candidate).isFile()) return candidate;
  }
  return null;
}

function main() {
  const slugs = process.argv.slice(2);
  if (slugs.length === 0) {
    console.error("Usage: bun run make-dark-svg.ts <slug>...");
    process.exit(1);
  }
  let made = 0;
  for (const slug of slugs) {
    const lightPath = findSvg(slug);
    if (!lightPath) {
      console.warn(`  ⚠  ${slug}: not found`);
      continue;
    }
    const darkPath = lightPath.replace(/\.svg$/, ".dark.svg");
    const light = readFileSync(lightPath, "utf-8");
    const dark = transform(light);
    writeFileSync(darkPath, dark);
    console.log(`  ✓  ${basename(darkPath)}  (← ${basename(lightPath)})`);
    made++;
  }
  console.log(`\nMade ${made} dark variant(s).`);
}

main();
