#!/usr/bin/env bun
/**
 * qa-flag-preservation-audit.ts
 *
 * Guard against the "distrust-clear" anti-pattern in `<block>.qa.json`
 * sidecars: a real flag (`fail` / `warn`) on a QA criterion is silently
 * discarded by appending a later `n/a` entry whose only justification is
 * that the *verdict was distrusted* (e.g. "batch had ~83% false-positive
 * rate, invalidated as unreliable").
 *
 * `n/a` in the block-qa schema means **the criterion does not apply to
 * this block** — such entries are excluded from the findings roll-up and
 * read as clean. Using `n/a` to mean "we no longer trust this verdict"
 * therefore *throws the flag away*: a genuinely-failing block goes green.
 *
 * The correct disposition for a distrusted verdict is **re-audit**, not
 * silent clearing. A verdict may only be superseded by
 *   - a fresh verdict from a trusted reviewer (pass / warn / fail), or
 *   - an `n/a` that is genuinely "criterion does not apply" (the block
 *     kind / content changed so the criterion is out of scope).
 * It may NOT be superseded by an `n/a` that merely distrusts the prior
 * reviewer while leaving the block unchanged.
 *
 * Modes
 *   (default) / --check   Scan every sidecar; report each criterion whose
 *                         LATEST entry is a distrust-`n/a` masking a prior
 *                         `fail`/`warn`. Exit 1 if any are found (CI gate).
 *   --fix                 Reinstate each masked flag: append a fresh
 *                         `local/qa-flag-reinstate` entry restoring the
 *                         prior `fail`/`warn` result (with the source hash
 *                         it was computed against, so ordinary staleness
 *                         re-queues it for a legitimate re-audit). The
 *                         distrust-`n/a` stays in history for the trail.
 *   --json                Emit the findings as JSON (with --check).
 *
 * Usage:
 *   bun run content/pipeline/qa-flag-preservation-audit.ts [root] [--fix] [--check] [--json]
 *   # root defaults to content/
 */

import { readFileSync, writeFileSync } from "node:fs";
import { globSync } from "node:fs";
import { FETCH_HINT, listBlockQa, resultsTreePresent, saveBlockQa } from "./block-qa-io.ts";

type Result = "pass" | "warn" | "fail" | "n/a" | string;
interface Entry {
  result?: Result;
  notes?: string;
  field_hash?: Record<string, string>;
  reviewed_at?: string;
  reviewed_sha?: string;
  reviewer?: Record<string, unknown>;
}
type Criteria = Record<string, Entry[] | Entry>;
interface Sidecar {
  criteria?: Criteria;
  [k: string]: unknown;
}

/** Signatures that mark an entry as a *distrust* clear (not a genuine
 *  scope change). Matched case-insensitively against the entry `notes`. */
const DISTRUST_SIGNATURES =
  /invalidat|unreliable|false[- ]?positive|distrust|not\s+re-?checkable|no\s+deterministic\s+re-?check/i;

const FLAG_RESULTS = new Set(["fail", "warn"]);

function asArray(v: Entry[] | Entry | undefined): Entry[] {
  if (v == null) return [];
  return Array.isArray(v) ? v : [v];
}

interface Finding {
  file: string;
  criterion: string;
  maskedResult: string;
  maskingNote: string;
  priorEntryIndex: number;
}

/**
 * The verdict the tail distrust-`n/a` actually superseded: the most recent
 * non-`n/a` entry before the tail. We return it only if it is a real flag
 * (`fail`/`warn`). Walking past a more-recent `pass` (e.g. history
 * `[fail, pass, distrust-n/a]`) would reinstate the wrong historical flag,
 * so we stop at the first non-`n/a` entry rather than hunting for any flag.
 */
function supersededFlag(entries: Entry[]): { entry: Entry; index: number } | null {
  for (let i = entries.length - 1; i >= 0; i--) {
    if (entries[i].result === "n/a") continue; // skip the tail + any earlier n/a
    return FLAG_RESULTS.has(entries[i].result ?? "") ? { entry: entries[i], index: i } : null;
  }
  return null;
}

function scan(files: string[]): { findings: Finding[]; sidecars: Map<string, Sidecar> } {
  const findings: Finding[] = [];
  const sidecars = new Map<string, Sidecar>();
  for (const f of files) {
    let d: Sidecar;
    try {
      const parsed = JSON.parse(readFileSync(f, "utf8"));
      if (parsed === null || typeof parsed !== "object") continue;
      d = parsed as Sidecar;
    } catch {
      continue;
    }
    sidecars.set(f, d);
    const criteria = d.criteria ?? {};
    for (const [cid, raw] of Object.entries(criteria)) {
      const entries = asArray(raw);
      if (entries.length < 2) continue;
      const tail = entries[entries.length - 1];
      if (tail.result !== "n/a") continue;
      if (!DISTRUST_SIGNATURES.test(tail.notes ?? "")) continue;
      // The tail is a distrust-n/a. Did it supersede a real flag?
      const prior = supersededFlag(entries);
      if (!prior) continue;
      findings.push({
        file: f,
        criterion: cid,
        maskedResult: prior.entry.result as string,
        maskingNote: (tail.notes ?? "").slice(0, 160),
        priorEntryIndex: prior.index,
      });
    }
  }
  return { findings, sidecars };
}

function reinstate(d: Sidecar, cid: string, prior: Entry): void {
  const entries = asArray(d.criteria![cid]);
  const tail = entries[entries.length - 1];
  const reinstated: Entry = {
    // Restore the source hash + sha the flag was computed against so ordinary
    // staleness (source has since drifted) re-queues a legitimate re-audit
    // instead of trusting this reinstated verdict verbatim. field_hash is
    // required by the block-qa schema, so always emit it (empty ⇒ stale).
    field_hash: prior.field_hash ?? {},
    ...(prior.reviewed_sha ? { reviewed_sha: prior.reviewed_sha } : {}),
    result: prior.result,
    notes:
      `Reinstated by qa-flag-preservation-audit: the ` +
      `${tail.reviewed_at ?? "prior"} distrusted n/a entry cleared a prior ` +
      `'${prior.result}' without a fresh verdict. A distrusted verdict must be ` +
      `re-audited, not silently cleared to n/a. Original flag note: ` +
      `${prior.notes ?? "(none)"}`,
    reviewed_at: new Date().toISOString(),
    reviewer: { kind: "script", id: "local/qa-flag-reinstate", version: "v1" },
  };
  entries.push(reinstated);
  d.criteria![cid] = entries;
}

function main() {
  const argv = process.argv.slice(2);
  const fix = argv.includes("--fix");
  const json = argv.includes("--json");
  const root = argv.find((a) => !a.startsWith("--")) ?? "folio";

  // Issue #7642: the results tree first, then the legacy sibling (block-qa-io.ts).
  if (!resultsTreePresent()) console.error(`qa-flag-preservation-audit: WARNING ${FETCH_HINT}`);
  const reports = listBlockQa(root);
  const rootOf = new Map(reports.map((r) => [r.path, r.blockRoot]));
  const files = reports.map((r) => r.path);
  const { findings, sidecars } = scan(files);

  if (fix) {
    const touched = new Map<string, Sidecar>();
    for (const fnd of findings) {
      const d = sidecars.get(fnd.file)!;
      const prior = asArray(d.criteria![fnd.criterion])[fnd.priorEntryIndex];
      reinstate(d, fnd.criterion, prior);
      touched.set(fnd.file, d);
    }
    const now = new Date().toISOString();
    for (const [f, d] of touched) {
      d.updated_at = now; // keep staleness tooling in sync, like sibling QA writers
      // A reinstated flag is a judgement: it goes to the attestation store
      // and the derived report is recomposed from it (issue #7642).
      const saved = saveBlockQa(rootOf.get(f)!, d, "attesting");
      if (!saved.ok) throw new Error(saved.reason);
    }
    console.log(
      `qa-flag-preservation-audit --fix: reinstated ${findings.length} masked flag(s) across ${touched.size} sidecar(s).`,
    );
    for (const fnd of findings) {
      console.log(`  reinstated ${fnd.maskedResult.toUpperCase()}  ${fnd.criterion}  ${fnd.file}`);
    }
    return;
  }

  if (json) {
    console.log(JSON.stringify({ count: findings.length, findings }, null, 2));
  } else if (findings.length === 0) {
    console.log(`qa-flag-preservation-audit: clean (${files.length} sidecars scanned).`);
  } else {
    console.error(
      `qa-flag-preservation-audit: ${findings.length} masked flag(s) — a distrust-n/a is hiding a real fail/warn.\n` +
        `A distrusted verdict must be re-audited, not cleared to n/a. Run with --fix to reinstate.\n`,
    );
    for (const fnd of findings) {
      console.error(`  ${fnd.maskedResult.toUpperCase()}  ${fnd.criterion}\n      ${fnd.file}\n      masked by: ${fnd.maskingNote}`);
    }
  }
  process.exit(findings.length === 0 ? 0 : 1);
}

main();
