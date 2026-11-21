#!/usr/bin/env bun
/**
 * Voice-leak ratchet — the draining gate over `voice-leak-audit.ts`
 * (epic `qou-d4kh`, step 5; owner ruling 2026-11-20, #8526 comment
 * 7041693067: "5 (gate as a draining ratchet)").
 *
 * The audit itself exits 1 while any failing hit exists, which on the
 * current corpus is every run. This wrapper turns it into a gate a PR can
 * pass: it compares the live failing-hit counts, per file and per leak
 * sub-kind, against a committed baseline
 * (`folio/pipeline/voice-leak-baseline.json`).
 *
 *   check (default)  exit 1 if any (file, class, sub-kind) count is ABOVE
 *                    its baseline, or a file absent from the baseline has
 *                    any failing hit. Counts below baseline pass, and are
 *                    reported as "drained, run --shrink".
 *   --shrink         rewrite the baseline to min(baseline, live) for every
 *                    entry. It can only lower counts and drop entries; it
 *                    never adds an entry and never raises one. This is the
 *                    only supported way to edit the baseline.
 *   --init           write the baseline from the live counts. Refuses if a
 *                    baseline already exists (use --shrink).
 *
 * Counts are keyed by file, not by line, so an edit that moves a leak
 * without adding one passes. Advisory hits are not counted.
 *
 * Never make a red run green by raising a number in the baseline. Fix
 * the leak (restate the sentence; move Lean names to the block's .ts
 * `lean` / `authorNotes`), or ask the owner.
 *
 *   bun run folio/pipeline/voice-leak-ratchet.ts [--shrink|--init] [--json]
 */
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { audit, type LeakClass } from "./voice-leak-audit";

export const BASELINE = "folio/pipeline/voice-leak-baseline.json";
const PAPER = "folio/quantum-observable-universe";

export type Counts = Record<string, Record<string, number>>; // file -> "L2:block-id" -> n

export async function liveCounts(paperDir = PAPER): Promise<Counts> {
  const { reports } = await audit(paperDir, new Set<LeakClass>(["L1", "L2", "L3", "L4"]));
  const out: Counts = {};
  for (const r of reports)
    for (const h of r.hits) {
      if (h.advisory) continue;
      const k = `${h.cls}:${h.sub}`;
      (out[r.file] ??= {})[k] = (out[r.file]![k] ?? 0) + 1;
    }
  return out;
}

export interface Verdict { grown: string[]; drained: string[]; total: { baseline: number; live: number } }

export function compare(base: Counts, live: Counts): Verdict {
  const grown: string[] = [];
  const drained: string[] = [];
  let tb = 0, tl = 0;
  for (const f of Object.keys(base)) for (const n of Object.values(base[f]!)) tb += n;
  for (const [f, ks] of Object.entries(live))
    for (const [k, n] of Object.entries(ks)) {
      tl += n;
      const b = base[f]?.[k] ?? 0;
      if (n > b) grown.push(`${f}  ${k}: ${b} -> ${n}`);
    }
  for (const [f, ks] of Object.entries(base))
    for (const [k, b] of Object.entries(ks)) {
      const n = live[f]?.[k] ?? 0;
      if (n < b) drained.push(`${f}  ${k}: ${b} -> ${n}`);
    }
  return { grown, drained, total: { baseline: tb, live: tl } };
}

export function shrink(base: Counts, live: Counts): Counts {
  const out: Counts = {};
  for (const f of Object.keys(base).sort())
    for (const k of Object.keys(base[f]!).sort()) {
      const n = Math.min(base[f]![k]!, live[f]?.[k] ?? 0);
      if (n > 0) (out[f] ??= {})[k] = n;
    }
  return out;
}

function sorted(c: Counts): Counts {
  const out: Counts = {};
  for (const f of Object.keys(c).sort()) {
    out[f] = {};
    for (const k of Object.keys(c[f]!).sort()) out[f]![k] = c[f]![k]!;
  }
  return out;
}

function write(c: Counts) {
  writeFileSync(BASELINE, JSON.stringify({ schema: "voice-leak-baseline/v1", note: "Draining ratchet: counts may only go down. Edit only with `voice-leak-ratchet.ts --shrink`.", counts: sorted(c) }, null, 1) + "\n");
}

if (import.meta.main) {
  const args = process.argv.slice(2);
  const live = await liveCounts();
  if (args.includes("--init")) {
    if (existsSync(BASELINE)) { console.error(`voice-leak-ratchet: ${BASELINE} exists; use --shrink`); process.exit(2); }
    write(live);
    console.log(`voice-leak-ratchet: baseline written`);
    process.exit(0);
  }
  if (!existsSync(BASELINE)) { console.error(`voice-leak-ratchet: no baseline at ${BASELINE}`); process.exit(2); }
  const base: Counts = JSON.parse(readFileSync(BASELINE, "utf8")).counts;
  const v = compare(base, live);
  if (args.includes("--shrink")) {
    write(shrink(base, live));
    console.log(`voice-leak-ratchet: baseline shrunk by ${v.drained.length} entr${v.drained.length === 1 ? "y" : "ies"}`);
  }
  if (args.includes("--json")) console.log(JSON.stringify(v, null, 2));
  else {
    for (const g of v.grown) console.log(`NEW  ${g}`);
    console.log(`voice-leak-ratchet: ${v.grown.length} new leak count(s); ${v.drained.length} drained entr${v.drained.length === 1 ? "y" : "ies"}; failing hits baseline ${v.total.baseline}, live ${v.total.live}`);
    if (v.drained.length && !args.includes("--shrink")) console.log(`voice-leak-ratchet: counts fell below baseline; run with --shrink to lock the drain in`);
  }
  process.exit(v.grown.length ? 1 : 0);
}
