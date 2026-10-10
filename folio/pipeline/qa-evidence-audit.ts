#!/usr/bin/env bun
/**
 * Report agent QA verdicts that assert a violation without saying what they
 * found.
 *
 *   bun run content/pipeline/qa-evidence-audit.ts [--strict] [--json]
 *     [--root content]
 *
 * `block-qa.schema.json` states the rule on `result` — "fail = violated
 * (evidence must cite file:line + verbatim quote)" — but `evidence` is not in
 * the entry's `required` list, so the corpus accumulated fail/warn entries
 * whose reason is nowhere on record. `qa-agent-entry.ts` now refuses to write
 * new ones; this reports the ones already there.
 *
 * Entries are bucketed by whether they can still be tied to the block they
 * judged, because the three buckets need different remedies:
 *
 *   live      field_hash matches the block's CURRENT .md/.ts. The block is
 *             carrying this failure right now — needs re-adjudication.
 *   stale     field_hash present but superseded by a later block edit. A
 *             historical record; no action.
 *   unhashed  no field_hash at all, so it can never be resolved to a block
 *             version — neither live nor stale, and it does not suppress the
 *             drain queue either (qa-agent-drain-queue.ts gates on
 *             `field_hash?.md === curmd`), so its block is re-reviewed
 *             indefinitely. These come from writers other than
 *             qa-agent-entry.ts, which always emits a field_hash.
 *
 * Only the `live` bucket is a present-tense defect, so only it fails --strict.
 *
 * @module content/pipeline/qa-evidence-audit
 */
import { createHash } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import { Glob } from "bun";
import { basename } from "node:path";
import { FETCH_HINT, listBlockQa, resultsTreePresent } from "./block-qa-io.ts";

const argv = process.argv;
const has = (f: string) => argv.includes(`--${f}`);
const val = (f: string) => {
  const i = argv.indexOf(`--${f}`);
  return i >= 0 ? argv[i + 1] : undefined;
};
const root = val("root") ?? "folio";

const sha12 = (p: string) =>
  createHash("sha256").update(readFileSync(p)).digest("hex").slice(0, 12);

/**
 * Does this entry actually say what it found?
 *
 * Evidence is usually a plain string, but part of the corpus carries it
 * STRUCTURED — `[{ text: "file.md:18-20 '<quote>'" }]` — which is the
 * file:line + verbatim quote the schema asks for, in a richer shape. Treating
 * a non-string as missing would report 35 of the best-evidenced entries in the
 * corpus as evidence-free, so unwrap arrays and objects rather than assuming
 * the string form.
 */
function hasEvidence(ev: unknown): boolean {
  if (typeof ev === "string") return ev.trim() !== "";
  if (Array.isArray(ev)) return ev.some(hasEvidence);
  if (ev && typeof ev === "object") {
    return Object.values(ev as Record<string, unknown>).some(hasEvidence);
  }
  return false;
}

/**
 * Keys other than `evidence` under which a verdict's reasoning is known to be
 * filed. `notes` is schema-blessed for a different purpose ("fix applied / fix
 * proposed / scope note") but the drain writer uses it as the reason field.
 */
const REASON_KEYS = ["notes", "referee_argument", "rationale", "reason"];

type Bucket = "live" | "stale" | "unhashed";
interface Hit {
  block: string;
  qaPath: string;
  criterion: string;
  result: string;
  severity?: string;
  reviewer?: string;
  bucket: Bucket;
  /** `silent` = no reason under any key; `misfiled` = reason present, wrong key. */
  accountability: "silent" | "misfiled";
}

const hits: Hit[] = [];
let totalFailWarn = 0;

// Issue #7642: reports are read where the platform reads them, the results
// tree first and then the legacy sibling (block-qa-io.ts).
if (!resultsTreePresent()) console.error(`qa-evidence-audit: WARNING ${FETCH_HINT}`);
for (const { blockRoot, path: qaPath } of listBlockQa(root)) {
  let doc: any;
  try {
    doc = JSON.parse(readFileSync(qaPath, "utf8"));
  } catch {
    continue; // unparseable sidecars are a different audit's problem
  }
  const stem = blockRoot;

  // The hash set the writer would produce for this block RIGHT NOW.
  const current: Record<string, string> = {};
  for (const ext of ["md", "ts"]) {
    if (existsSync(`${stem}.${ext}`)) current[ext] = sha12(`${stem}.${ext}`);
  }

  for (const [criterion, arr] of Object.entries(doc.criteria ?? {})) {
    if (!Array.isArray(arr)) continue;

    // block-qa/v1: the freshest entry whose field_hash matches the current
    // sources wins. Later entries override earlier ones, so scan forward and
    // keep the last match — anything it supersedes is not a live verdict.
    let winner: any;
    for (const e of arr) {
      if (!e || typeof e !== "object") continue;
      const fh = e.field_hash;
      if (
        fh &&
        Object.keys(current).length > 0 &&
        Object.entries(current).every(([k, v]) => fh[k] === v)
      ) {
        winner = e;
      }
    }

    for (const e of arr) {
      if (!e || typeof e !== "object") continue;
      if (e.reviewer?.kind !== "agent") continue;
      if (e.result !== "fail" && e.result !== "warn") continue;
      totalFailWarn++;
      if (hasEvidence(e.evidence)) continue;

      // The `evidence` key is empty — but that is NOT the same as the verdict
      // being unaccountable. One writer family (reviewer id
      // `local/qa-agent-drain`) files its reasoning under `notes` and
      // `referee_argument` instead, and that prose is substantive: it cites
      // file:line, e.g. "...molecular-braid.lean:22:28: error(...)". Counting
      // those as evidence-free would report a schema-key mismatch as an
      // accountability void, which is a far more serious claim and a false
      // one. Only an entry with no reason under ANY key is truly silent.
      const misfiled = REASON_KEYS.some((k) => hasEvidence((e as any)[k]));

      const bucket: Bucket = !e.field_hash
        ? "unhashed"
        : e === winner
          ? "live"
          : "stale";
      hits.push({
        block: basename(stem),
        qaPath,
        criterion,
        result: e.result,
        severity: e.severity,
        reviewer: e.reviewer?.id,
        bucket,
        accountability: misfiled ? "misfiled" : "silent",
      });
    }
  }
}

const of = (b: Bucket) => hits.filter((h) => h.bucket === b);
const live = of("live");
const silent = hits.filter((h) => h.accountability === "silent");
const liveSilent = live.filter((h) => h.accountability === "silent");

if (has("json")) {
  console.log(
    JSON.stringify(
      {
        $schema: "qa-evidence-audit/v1",
        total_agent_fail_warn: totalFailWarn,
        empty_evidence: hits.length,
        by_bucket: {
          live: live.length,
          stale: of("stale").length,
          unhashed: of("unhashed").length,
        },
        by_accountability: {
          misfiled: hits.length - silent.length,
          silent: silent.length,
        },
        live_silent: liveSilent.length,
        live_blocks: [...new Set(live.map((h) => h.qaPath))].length,
        hits,
      },
      null,
      2,
    ),
  );
} else {
  const tally = (rows: Hit[]) => {
    const c = new Map<string, number>();
    for (const h of rows) c.set(h.criterion, (c.get(h.criterion) ?? 0) + 1);
    return [...c].sort((a, b) => b[1] - a[1]);
  };
  console.log(
    `agent fail/warn entries    : ${totalFailWarn}\n` +
      `  with an empty \`evidence\`: ${hits.length}\n` +
      `    misfiled (reason under notes/referee_argument): ` +
      `${hits.length - silent.length}\n` +
      `    SILENT   (no reason under any key)           : ${silent.length}\n` +
      `\n  by hash bucket:\n` +
      `    live (still applies): ${live.length} ` +
      `across ${new Set(live.map((h) => h.qaPath)).size} blocks ` +
      `(${liveSilent.length} silent)\n` +
      `    stale (superseded)  : ${of("stale").length}\n` +
      `    unhashed (no anchor): ${of("unhashed").length}`,
  );
  if (liveSilent.length) {
    console.log("\nlive AND silent — the actionable set, by criterion:");
    for (const [c, n] of tally(liveSilent)) {
      console.log(`  ${c.padEnd(40)} ${n}`);
    }
  }
}

// The gate is `live AND silent`: a block carrying a failure TODAY whose
// reason is nowhere under any key. A misfiled reason is a schema-conformance
// problem — real, but it is a key migration, not a re-adjudication, and
// failing the gate on it would conflate the two and make the gate unusable.
// Stale and unhashed entries are not present-tense defects either.
if (has("strict") && liveSilent.length > 0) process.exit(1);
