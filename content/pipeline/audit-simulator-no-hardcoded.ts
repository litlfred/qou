#!/usr/bin/env bun
/**
 * audit-simulator-no-hardcoded.ts — refuse PRs that bake QOU values
 * into a simulator HTML.
 *
 * The Recursive Knot-Atlas Viewer (and any sibling simulator) must
 * read every QOU-flavoured value from its companion witness JSON at
 * runtime.  This audit scans the simulator HTML for numeric literals
 * that appear next to QOU-flavoured identifiers (q0, vol_4_1,
 * m_e_MeV, q_pinned, q_substrate, …) and fails the build if any are
 * found inside `<script>` blocks (excluding documented constants
 * inside comments and pure-projection chart math).
 *
 * Usage:
 *   bun run pipeline/audit-simulator-no-hardcoded.ts
 *   bun run pipeline/audit-simulator-no-hardcoded.ts --strict
 */
import { readFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";

const STRICT = process.argv.includes("--strict");
const ROOT = join(import.meta.dir, "..", "..", "folio-assistant", "simulators");

// QOU-flavoured identifiers that must not have a numeric literal pinned
// to them inside a simulator HTML script block.
const QOU_IDENTIFIER_RE = new RegExp(
  [
    "q0", "q_0", "q_pinned", "q_substrate",
    "vol_4_1", "vol_41", "Vol\\(4_1\\)",
    "m_e_MeV", "m_mu_over_m_e", "muon_electron_ratio",
  ].map((s) => `\\b${s}\\b`).join("|"),
  "i",
);

// Numeric literal next to a QOU-identifier on the same line.
// Matches floats, scientific notation, AND plain integers (e.g. `q0 = 1`).
const HARDCODED_RE = /(\b[A-Za-z_][A-Za-z0-9_]*\b)\s*[:=]\s*(-?\d+\.\d+|-?\d+e[+-]?\d+|-?\d+\b)/i;

interface Finding {
  file: string;
  line: number;
  text: string;
  identifier: string;
}

function* simulatorFiles(dir: string): Generator<string> {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) yield* simulatorFiles(full);
    else if (entry.endsWith(".html")) yield full;
  }
}

function inScriptBlock(html: string): { line: number; text: string }[] {
  // Strip everything outside <script>…</script> blocks; keep line numbers.
  const lines = html.split("\n");
  const out: { line: number; text: string }[] = [];
  let inside = false;
  for (let i = 0; i < lines.length; i++) {
    const ln = lines[i];
    if (/<script(\s|>)/i.test(ln)) inside = true;
    if (inside) {
      // Strip line comments and block-comment-only lines.
      const stripped = ln.replace(/\/\/.*$/, "").trim();
      if (stripped && !/^\/\*|\*\/$|^\*/.test(stripped)) {
        out.push({ line: i + 1, text: ln });
      }
    }
    if (/<\/script>/i.test(ln)) inside = false;
  }
  return out;
}

function audit(file: string): Finding[] {
  const html = readFileSync(file, "utf8");
  const findings: Finding[] = [];
  for (const { line, text } of inScriptBlock(html)) {
    const m = HARDCODED_RE.exec(text);
    if (!m) continue;
    const ident = m[1];
    if (QOU_IDENTIFIER_RE.test(ident)) {
      findings.push({ file, line, text: text.trim(), identifier: ident });
    }
  }
  return findings;
}

let totalFindings = 0;
const checked: string[] = [];

for (const file of simulatorFiles(ROOT)) {
  checked.push(file);
  const findings = audit(file);
  if (findings.length === 0) continue;
  totalFindings += findings.length;
  const rel = file.replace(join(ROOT, "..", ".."), ".");
  console.error(`✗ ${rel} — ${findings.length} hardcoded QOU value(s):`);
  for (const f of findings) {
    console.error(`    L${f.line}: ${f.identifier} ← ${f.text}`);
  }
}

console.log(`\nScanned ${checked.length} simulator HTML file(s).`);
if (totalFindings === 0) {
  console.log("✓ No hardcoded QOU values found — every simulator reads from witness JSON.");
  process.exit(0);
}
console.error(`\n✗ ${totalFindings} hardcoded value(s) detected.`);
console.error(`  Move these into the simulator's witness JSON and read them at runtime.`);
if (STRICT) process.exit(1);
console.error(`  (warn-only; pass --strict to fail CI)`);
process.exit(0);
