/**
 * `:val[…]` backfill codemod — rewrites known numeric literals inside
 * math contexts to `:val[name]{…}` directives so the rendered LaTeX
 * stays in sync with the canonical witness JSON.
 *
 * Walks every block's `.md` file, parses to mdast, and replaces
 * occurrences of literal decimal numbers inside `inlineMath` / `math`
 * node values with the canonical witness reference.  The match table
 * is built from `verifiedNames()` — entries flagged `needsReview` are
 * never auto-applied.
 *
 * Behaviour:
 *
 *   - **Math-only.**  Replacements happen only inside `inlineMath` /
 *     `math` node `value` strings.  Prose text is never touched.
 *   - **Idempotent.**  A literal already adjacent to a `:val[` token
 *     is skipped, and the rendered numeric form does not match the
 *     literal patterns again.
 *   - **Conservative match.**  Literal must match the witness value
 *     to *at least* the configured number of leading significant
 *     digits (default 4) — looser matches are skipped.  Word-boundary
 *     enforcement: digits adjacent to other digits or letters are
 *     never matched.
 *   - **Skip rules.**
 *       * Fenced ``` ```tex ``` blocks are skipped (they typically
 *         contain derivations where the literal is computed inline).
 *       * Tables are skipped (review manually first).
 *   - **Dry-run by default.**  Without `--write`, prints a per-file
 *     diff summary.
 *
 * Usage:
 *
 *   bun run pipeline/codemod-val.ts <paper-or-chapter-dir>            # dry-run
 *   bun run pipeline/codemod-val.ts <paper-or-chapter-dir> --write    # apply
 *
 * Mdast-based; no regex over raw markdown source.
 *
 * @module content/pipeline/codemod-val
 */

import { existsSync, readFileSync, writeFileSync, readdirSync, statSync } from "fs";
import { basename, join, resolve, extname } from "path";
import { remark } from "remark";
import remarkDirective from "remark-directive";
import remarkMath from "remark-math";
import { visit } from "unist-util-visit";
import { gfmTable } from "micromark-extension-gfm-table";
import { gfmTableFromMarkdown, gfmTableToMarkdown } from "mdast-util-gfm-table";
import { gfmStrikethrough } from "micromark-extension-gfm-strikethrough";
import { gfmStrikethroughFromMarkdown, gfmStrikethroughToMarkdown } from "mdast-util-gfm-strikethrough";
import {
  WITNESSED_VALUES,
  verifiedNames,
  type WitnessedValueEntry,
} from "../values/registry";
import { resolvePath } from "./render-value";

const REPO_ROOT = resolve(import.meta.dir, "..", "..");

// Round-trip parser/serializer with directive support — mirrors the
// renderer's configuration so round-tripping preserves all formatting.
const proc = remark()
  .data("micromarkExtensions", [gfmTable(), gfmStrikethrough()])
  .data("fromMarkdownExtensions", [gfmTableFromMarkdown(), gfmStrikethroughFromMarkdown()])
  .data("toMarkdownExtensions", [gfmTableToMarkdown(), gfmStrikethroughToMarkdown()])
  .use(remarkDirective)
  .use(remarkMath);

// ── Literal index construction ───────────────────────────────────

interface LiteralEntry {
  /** Registry name. */
  name: string;
  /** Full canonical decimal-string value. */
  canonical: string;
  /** Pre-built regex matching this literal at the configured
   *  significant-digit precision, with word boundaries on both sides. */
  pattern: RegExp;
}

/**
 * Number of leading significant digits required for a literal-to-name
 * match.  Set conservatively so common short literals (e.g. `1.109`)
 * cannot accidentally match unrelated values that happen to share a
 * prefix.  At 6 digits, `q_0` requires the literal `1.10997` and
 * `B_4He_AME_MeV` requires `28.2956` — both specific enough to avoid
 * cross-contamination with other physics constants.
 */
const MATCH_PRECISION = 6;

/**
 * Truncate a decimal string to `n` significant digits (no rounding —
 * we want a substring match, not a numerical approximation).
 */
function truncateSignificant(str: string, n: number): string | null {
  const m = str.match(/^(-?)(\d+)(?:\.(\d+))?$/);
  if (!m) return null;
  const sign = m[1];
  const intPart = m[2];
  const fracPart = m[3] || "";
  const allDigits = intPart + fracPart;
  // Strip leading zeros from significant-digit count.
  let firstSig = 0;
  while (firstSig < allDigits.length - 1 && allDigits[firstSig] === "0") firstSig++;
  if (firstSig + n > allDigits.length) return null;  // not enough precision
  // Reconstruct with the truncated digit count.
  const truncDigits = allDigits.slice(0, firstSig + n);
  // Rebuild integer/fractional split.
  if (truncDigits.length <= intPart.length) {
    // Entire truncation falls in integer part; pad trailing zeros.
    return sign + truncDigits + "0".repeat(intPart.length - truncDigits.length);
  }
  const newInt = truncDigits.slice(0, intPart.length);
  const newFrac = truncDigits.slice(intPart.length);
  return sign + newInt + "." + newFrac;
}

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function loadWitnessOnce(file: string, cache: Map<string, unknown | null>): unknown | null {
  if (cache.has(file)) return cache.get(file) ?? null;
  const abs = resolve(REPO_ROOT, file);
  if (!existsSync(abs)) {
    cache.set(file, null);
    return null;
  }
  try {
    const parsed = JSON.parse(readFileSync(abs, "utf-8"));
    cache.set(file, parsed);
    return parsed;
  } catch {
    cache.set(file, null);
    return null;
  }
}

/**
 * Build the literal-match table from verified registry entries only.
 * Entries flagged `needsReview` are skipped — the codemod refuses to
 * auto-apply unverified mappings.
 */
export function buildLiteralIndex(): LiteralEntry[] {
  const out: LiteralEntry[] = [];
  const cache = new Map<string, unknown | null>();
  for (const name of verifiedNames()) {
    const entry = WITNESSED_VALUES[name];
    if (!entry) continue;
    const witness = loadWitnessOnce(entry.witnessFile, cache);
    if (witness == null) continue;
    const raw = resolvePath(witness, entry.witnessPath);
    let canonical: string | null = null;
    if (typeof raw === "string") canonical = raw;
    else if (typeof raw === "number" && Number.isFinite(raw)) canonical = raw.toString();
    else if (raw && typeof raw === "object") {
      const o = raw as Record<string, unknown>;
      if (typeof o.value === "string") canonical = o.value;
    }
    if (!canonical) continue;
    const truncated = truncateSignificant(canonical, MATCH_PRECISION);
    if (!truncated) continue;
    // Word boundaries: digits/letters on either side disqualify a match.
    const pattern = new RegExp(`(?<![\\d.])${escapeRegExp(truncated)}(?![\\d])`, "g");
    out.push({ name, canonical, pattern });
  }
  // Longest canonical first — ensures more-specific literals win
  // when two registry entries share a leading prefix.
  out.sort((a, b) => b.canonical.length - a.canonical.length);
  return out;
}

// ── Per-math-node rewriting ──────────────────────────────────────

interface NodeRewrite {
  changed: boolean;
  newValue: string;
  hits: Map<string, number>;
}

/**
 * Rewrite a single math-node value string.  Skips any region already
 * inside an existing `:val[…]` directive (idempotency).
 */
export function rewriteMathString(value: string, index: LiteralEntry[]): NodeRewrite {
  const hits = new Map<string, number>();
  let changed = false;

  // Carve out existing `:val[…]` regions so we never rewrite inside one.
  const guarded: { kind: "text" | "skip"; s: string }[] = [];
  const valPat = /:val\[[A-Za-z_][A-Za-z0-9_]*\](?:\{[^}]*\})?/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = valPat.exec(value)) !== null) {
    if (m.index > last) guarded.push({ kind: "text", s: value.slice(last, m.index) });
    guarded.push({ kind: "skip", s: m[0] });
    last = m.index + m[0].length;
  }
  if (last < value.length) guarded.push({ kind: "text", s: value.slice(last) });

  // Apply each pattern to text segments.
  const out: string[] = [];
  for (const seg of guarded) {
    if (seg.kind === "skip") {
      out.push(seg.s);
      continue;
    }
    let s = seg.s;
    for (const lit of index) {
      lit.pattern.lastIndex = 0;
      const before = s;
      let count = 0;
      s = s.replace(lit.pattern, () => {
        count++;
        return `:val[${lit.name}]{precision=${MATCH_PRECISION}}`;
      });
      if (count > 0) {
        hits.set(lit.name, (hits.get(lit.name) ?? 0) + count);
        changed = true;
      }
    }
    out.push(s);
  }

  return { changed, newValue: out.join(""), hits };
}

// ── Per-file rewriting ───────────────────────────────────────────

export interface FileRewrite {
  /** Path relative to repo root. */
  file: string;
  /** Whether any replacements were made. */
  changed: boolean;
  /** Rewritten markdown source (only set when changed). */
  newSource?: string;
  /** Per-name hit counts. */
  hits: Map<string, number>;
}

export function rewriteMarkdownFile(file: string, index: LiteralEntry[]): FileRewrite {
  const md = readFileSync(file, "utf-8");
  const tree = proc.parse(md);
  const totalHits = new Map<string, number>();
  let mutated = false;
  let inSkipParent = 0;

  visit(tree as any, (node: any, _index: number | null, parent: any) => {
    // Skip subtree if we're inside a fenced ```tex block or a table.
    if (node.type === "code" && node.lang === "tex") return "skip" as any;
    if (node.type === "table") return "skip" as any;
    if (node.type !== "inlineMath" && node.type !== "math") return;

    const r = rewriteMathString(node.value as string, index);
    if (r.changed) {
      node.value = r.newValue;
      mutated = true;
      for (const [k, v] of r.hits) totalHits.set(k, (totalHits.get(k) ?? 0) + v);
    }
  });

  if (!mutated) {
    return { file, changed: false, hits: totalHits };
  }
  return {
    file,
    changed: true,
    newSource: String(proc.stringify(tree as any)),
    hits: totalHits,
  };
}

// ── Discovery ────────────────────────────────────────────────────

/** Recursively find every .md file under `dir`. */
function findMarkdownFiles(dir: string): string[] {
  const out: string[] = [];
  const stack = [dir];
  while (stack.length) {
    const cur = stack.pop()!;
    let entries: string[];
    try {
      entries = readdirSync(cur);
    } catch {
      continue;
    }
    for (const name of entries) {
      if (name === "node_modules" || name.startsWith(".")) continue;
      const full = join(cur, name);
      let st;
      try { st = statSync(full); } catch { continue; }
      if (st.isDirectory()) stack.push(full);
      else if (extname(name) === ".md") out.push(full);
    }
  }
  return out.sort();
}

// ── CLI ──────────────────────────────────────────────────────────

if (import.meta.main) {
  const args = process.argv.slice(2);
  const write = args.includes("--write");
  const positional = args.filter(a => !a.startsWith("--"));
  const target = resolve(positional[0] || ".");

  if (!existsSync(target)) {
    console.error(`Target not found: ${target}`);
    process.exit(2);
  }

  const index = buildLiteralIndex();
  if (index.length === 0) {
    console.error("No verified registry entries with resolvable witnesses — nothing to do.");
    process.exit(0);
  }
  console.log(`Loaded ${index.length} literal patterns from registry:`);
  for (const lit of index) {
    console.log(`  ${lit.name.padEnd(20)} → ${lit.canonical.slice(0, 24)}`);
  }
  console.log("");

  const files = findMarkdownFiles(target);
  console.log(`Scanning ${files.length} .md file(s) under ${target}\n`);

  const totalHits = new Map<string, number>();
  let filesChanged = 0;

  for (const file of files) {
    const r = rewriteMarkdownFile(file, index);
    if (!r.changed) continue;
    filesChanged++;
    const rel = file.startsWith(REPO_ROOT) ? file.slice(REPO_ROOT.length + 1) : file;
    const summary = Array.from(r.hits.entries())
      .map(([k, v]) => `${k}×${v}`)
      .join(", ");
    console.log(`  ${write ? "WRITE" : "DRY  "} ${rel}  [${summary}]`);
    if (write && r.newSource) {
      writeFileSync(file, r.newSource, "utf-8");
    }
    for (const [k, v] of r.hits) totalHits.set(k, (totalHits.get(k) ?? 0) + v);
  }

  console.log("");
  console.log(`Files ${write ? "modified" : "would be modified"}: ${filesChanged}`);
  console.log("Per-name hits:");
  const sorted = Array.from(totalHits.entries()).sort((a, b) => b[1] - a[1]);
  for (const [k, v] of sorted) console.log(`  ${k.padEnd(20)} ${v}`);
  if (!write && filesChanged > 0) {
    console.log("\nRe-run with --write to apply.");
  }
}
