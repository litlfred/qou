#!/usr/bin/env bun
/**
 * Census of the two agent-adjudicated sidecar checks, re-run 2026-11-16.
 *
 *   proof-narrative-lean-equiv  on theorem/lemma/proposition/corollary blocks that have Lean
 *   da-non-sequitur             on proof blocks (builder `proof(`)
 *
 * Freshness uses the platform's own rule (`entryIsFresh` + `hashBlockFiles`)
 * and the registry's depends_on / lean_granularity. A verdict counts only if it
 * carries a field_hash. Output: one JSON row per block on stdout.
 *
 *   bun run docs/audits/2026-11-16-sidecar-census-rerun/qa-sidecar-census.ts > rows.json
 */
import { readdirSync, readFileSync, existsSync, statSync } from "node:fs";
import { join, resolve } from "node:path";
import {
  entryIsFresh,
  hashBlockFiles,
  resolveCanonicalLean,
} from "../../../folio-assistant/cat-harness-tools/pipeline/qa-utils.ts";
import { configureLeanPackages } from "../../../folio-assistant/folio-assistant-sci/pipeline/lean-formal-ref";
import { LEAN_PACKAGES } from "../../../schemas/lean-packages";
import { QA_CRITERIA_REGISTRY as QA_CRITERIA } from "../../../folio-assistant/cat-harness-tools/pipeline/qa-criteria-registry.ts";

configureLeanPackages(LEAN_PACKAGES);

const ROOT = resolve(import.meta.dir, "../../..");
const FOLIO = join(ROOT, "folio/quantum-observable-universe");
const STATEMENT = new Set(["theorem", "lemma", "proposition", "corollary"]);

const def = (id: string) => (QA_CRITERIA as any[]).find((c) => c.id === id);

function* walk(d: string): Generator<string> {
  for (const n of readdirSync(d)) {
    const p = join(d, n);
    if (n === "lean" || n.startsWith(".")) continue;
    if (statSync(p).isDirectory()) yield* walk(p);
    else if (n.endsWith(".ts") && existsSync(p.slice(0, -3) + ".md")) yield p;
  }
}

function status(qa: any, crit: string, cur: any) {
  const d = def(crit);
  const list: any[] = qa?.criteria?.[crit] ?? [];
  if (!list.length) return { s: "missing" };
  const hashed = list.filter((e) => e.field_hash && e.reviewer?.kind !== "script");
  if (!hashed.length) return { s: "unhashed" };
  const fresh = hashed.filter((e) => entryIsFresh(e, cur, d.depends_on, undefined, d.lean_granularity));
  if (fresh.length) return { s: "fresh", result: fresh[fresh.length - 1].result };
  return { s: "stale", result: hashed[hashed.length - 1].result };
}

const rows: any[] = [];
for (const ts of walk(FOLIO)) {
  const src = readFileSync(ts, "utf8");
  const m = src.match(/export default (\w+)\(/);
  if (!m) continue;
  const kind = m[1];
  const isStmt = STATEMENT.has(kind);
  if (!isStmt && kind !== "proof") continue;
  const base = ts.slice(0, -3);
  const label = src.match(/label:\s*"([^"]+)"/)?.[1];
  const ref = src.match(/ref:\s*"([^"]+)"/)?.[1];
  const sib = base + ".lean";
  const lean = existsSync(sib) ? sib : ref ? resolveCanonicalLean(ref, ROOT) : undefined;
  if (isStmt && !lean) continue;
  const cur = hashBlockFiles({ md: base + ".md", ts, ...(lean ? { lean } : {}) });
  const qaPath = base + ".qa.json";
  const qa = existsSync(qaPath) ? JSON.parse(readFileSync(qaPath, "utf8")) : undefined;
  const crit = isStmt ? "proof-narrative-lean-equiv" : "da-non-sequitur";
  rows.push({
    block: base.slice(ROOT.length + 1) + ".md",
    chapter: base.slice(FOLIO.length + 1).split("/")[0],
    kind,
    label,
    lean: lean?.slice(ROOT.length + 1),
    criterion: crit,
    ...status(qa, crit, cur),
  });
}
console.log(JSON.stringify(rows, null, 1));
