#!/usr/bin/env bun
/**
 * Copy misfiled verdict reasons into the `evidence` field.
 *
 *   bun run content/pipeline/qa-evidence-migrate.ts [--apply] [--root content]
 *
 * Dry-run by default; `--apply` writes.
 *
 * ## Why this exists
 *
 * `block-qa.schema.json` designates `evidence` as the field carrying a
 * fail/warn verdict's justification — "evidence must cite file:line +
 * verbatim quote". One writer family (reviewer id `local/qa-agent-drain`)
 * files that justification under `notes` and `referee_argument` instead,
 * leaving `evidence` empty on 1302 agent fail/warn entries.
 *
 * The reasons themselves are sound — median 154 characters, citing file:line
 * as asked. So this is a key migration, NOT a re-adjudication: nothing is
 * re-judged and no verdict changes.
 *
 * ## Copy, never move
 *
 * `notes` is read by live consumers in both repos — `qa-flag-preservation-
 * audit.ts` (masking notes), `proof-axis-dashboard.ts`, `qa-sweep.ts`,
 * `qa-merge-findings.ts`, `qa-utils.ts`. Moving the text out would break every
 * one of them to fix a schema-conformance problem, so the source field is left
 * exactly as it is and `evidence` is populated alongside.
 *
 * ## Faithfulness
 *
 * `evidence` is set to text that already existed in the entry, verbatim. This
 * never invents evidence, never upgrades a verdict, and never touches an entry
 * whose `evidence` is already populated — so re-running is a no-op.
 *
 * `field_hash` is a hash of the block's .md/.ts, not of the sidecar, so
 * writing here cannot make any entry look stale.
 *
 * @module content/pipeline/qa-evidence-migrate
 */
import { readFileSync, writeFileSync } from "node:fs";
import { Glob } from "bun";

const argv = process.argv;
const apply = argv.includes("--apply");
const rootIdx = argv.indexOf("--root");
const root = rootIdx >= 0 ? argv[rootIdx + 1] : "content";

/** Preference order: the field most likely to carry file:line comes first. */
const REASON_KEYS = ["notes", "referee_argument", "rationale", "reason"];

const hasEvidence = (ev: unknown): boolean => {
  if (typeof ev === "string") return ev.trim() !== "";
  if (Array.isArray(ev)) return ev.some(hasEvidence);
  if (ev && typeof ev === "object") {
    return Object.values(ev as Record<string, unknown>).some(hasEvidence);
  }
  return false;
};

/**
 * Re-serialize while preserving the SOURCE FILE's own non-ASCII convention.
 *
 * The corpus is mixed: 1357 sidecars store non-ASCII raw (`ö`) and 57 store it
 * escaped (`\u00f6`). `JSON.stringify` always emits raw, so a naive rewrite
 * silently un-escapes the 57 — rewriting `notes` lines on entries this
 * migration has no business touching, and burying the real change in churn.
 * Measured on a first pass: 167 unrelated line rewrites.
 *
 * So each file keeps whatever it already used.
 */
function serialize(doc: unknown, sourceText: string): string {
  const out = JSON.stringify(doc, null, 2);
  const wasEscaped = /\\u[0-9a-fA-F]{4}/.test(sourceText);
  const hasRaw = /[^\x00-\x7F]/.test(sourceText);
  // Escape only for files that escaped and had no raw non-ASCII of their own;
  // a file mixing both conventions is left in the majority (raw) form.
  if (!wasEscaped || hasRaw) return out;
  return out.replace(/[^\x00-\x7F]/g, (c) =>
    "\\u" + c.charCodeAt(0).toString(16).padStart(4, "0"),
  );
}

let migrated = 0;
let filesTouched = 0;
let skippedSilent = 0;
const perKey = new Map<string, number>();

for (const rel of new Glob("**/*.qa.json").scanSync(root)) {
  const path = `${root}/${rel}`;
  let doc: any;
  const raw = readFileSync(path, "utf8");
  try {
    doc = JSON.parse(raw);
  } catch {
    continue;
  }

  let dirty = false;
  for (const arr of Object.values(doc.criteria ?? {})) {
    if (!Array.isArray(arr)) continue;
    for (const e of arr as any[]) {
      if (!e || typeof e !== "object") continue;
      if (e.reviewer?.kind !== "agent") continue;
      if (e.result !== "fail" && e.result !== "warn") continue;
      if (hasEvidence(e.evidence)) continue;

      const key = REASON_KEYS.find(
        (k) => typeof e[k] === "string" && e[k].trim() !== "",
      );
      if (!key) {
        // No reason under any key. There is nothing faithful to copy, and
        // inventing one is the exact failure this whole effort is about.
        skippedSilent++;
        continue;
      }
      e.evidence = e[key];
      perKey.set(key, (perKey.get(key) ?? 0) + 1);
      migrated++;
      dirty = true;
    }
  }

  if (dirty) {
    filesTouched++;
    if (apply) writeFileSync(path, serialize(doc, raw) + "\n");
  }
}

console.log(
  `${apply ? "APPLIED" : "DRY RUN (pass --apply to write)"}\n` +
    `  entries migrated : ${migrated}\n` +
    `  files touched    : ${filesTouched}\n` +
    `  skipped, no reason to copy: ${skippedSilent}`,
);
for (const [k, n] of [...perKey].sort((a, b) => b[1] - a[1])) {
  console.log(`    from \`${k}\`: ${n}`);
}
