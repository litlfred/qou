#!/usr/bin/env bun
/**
 * Prefix-less reference RESOLVER (bean `qou-pfx1`, 2026-09-05).
 *
 * `gen-block-jsonld.ts` ends its run with a line of the shape
 *
 *     35 reference(s) in 34 block(s) name a label with no kind prefix
 *
 * and then lists the *targets*. That line answers "how many", and the one
 * question a reader actually has is "are any of them broken" — which the
 * generator deliberately does not answer, because it cannot: a prefix-less
 * reference resolves through the same helper `mintNodeId` applies to a
 * prefix-less *label*, so referrer and target agree by construction whenever
 * the target exists, and the generator has no cheap way to say whether it
 * does. Its own warning says as much: "a target that does not exist will
 * surface as a dangling edge when the graph is walked."
 *
 * This script walks it. For every bare-label reference it reports the source
 * block, the field, and whether a block with that exact label exists — plus
 * that block's `kind`, which is the fact that decides legitimacy:
 *
 *   - target exists, kind `prose`  -> LEGITIMATE. The Type-system table in
 *     AGENTS.md gives `prose` no required label prefix, so a prose block's
 *     own label is legitimately bare and a reference to it must be bare too.
 *   - target exists, kind anything else -> REPORT IT. Every other kind has a
 *     mandatory prefix, so a bare reference to one is a convention break even
 *     though the edge lands.
 *   - target missing -> the real defect. The edge is emitted, claims an IRI
 *     no node owns, and shows as dangling when the graph is walked.
 *
 * ── Why this exists as a script and not as a number in a doc ─────────────
 *
 * Because the number moves and the verdict does not. Measured 2026-09-05 the
 * answer was 35/35 legitimate, 0 dangling; the moment someone adds a prose
 * block or a table-data sibling that count changes and a reader is back to
 * not knowing whether the new one is fine. An audit doc would be stale on the
 * next commit. Run this instead of trusting a recorded figure.
 *
 * Print-only, like the other qou-side audits — it is a lens, not a gate. It
 * exits 1 only when a bare reference names a target that does not exist,
 * which is unambiguously a content defect rather than a convention nit.
 *
 * Usage:
 *   bun run content/pipeline/prefixless-ref-audit.ts
 *   bun run content/pipeline/prefixless-ref-audit.ts --paper quantum-observable-universe
 *
 * @module content/pipeline/prefixless-ref-audit
 */

import { loadBlocksUnder, reportLoadFailures } from "../../folio-assistant/cat-harness-tools/pipeline/block-module";
import { parseReference } from "../../folio-assistant/cat-harness-tools/schemas/kg/jsonld";

/** The fields `gen-block-jsonld` resolves as references, plus scalar `interprets`. */
const REF_LIST_FIELDS = ["uses", "foreshadows", "proofs", "examples"] as const;

/** Kinds whose label prefix is optional per the AGENTS.md Type-system table. */
const PREFIX_OPTIONAL_KINDS = new Set(["prose", "equation", "diagram"]);

const strList = (v: unknown): string[] =>
  Array.isArray(v) ? v.filter((x): x is string => typeof x === "string") : [];

export interface BareRef {
  src: string;
  srcKind: string;
  field: string;
  ref: string;
}

/**
 * Every prefix-less reference in one block manifest.
 *
 * Split out from {@link auditPaper} so the extraction can be tested without a
 * corpus: on the live tree the interesting branches never fire, and an audit
 * that has only ever returned "clean" has demonstrated nothing about itself.
 */
export function bareRefsOf(label: string, kind: string, block: Record<string, unknown>): BareRef[] {
  const out: BareRef[] = [];
  for (const f of REF_LIST_FIELDS) {
    for (const r of [...new Set(strList(block[f]))]) {
      if (parseReference(r).form === "bare-label")
        out.push({ src: label, srcKind: kind, field: f, ref: r });
    }
  }
  const it = block.interprets;
  if (typeof it === "string" && it && parseReference(it).form === "bare-label")
    out.push({ src: label, srcKind: kind, field: "interprets", ref: it });
  return out;
}

/** The verdict for one bare-label target, given the kind of the block it names. */
export type TargetVerdict = "ok" | "convention" | "dangling";

export function classifyTarget(targetKind: string | undefined): TargetVerdict {
  if (targetKind === undefined) return "dangling";
  return PREFIX_OPTIONAL_KINDS.has(targetKind) ? "ok" : "convention";
}

export async function auditPaper(paperDir: string): Promise<number> {
  const { blocks, failures } = await loadBlocksUnder(paperDir);
  const anyFailure = reportLoadFailures(failures);

  const rows: BareRef[] = [];
  for (const b of blocks.values())
    rows.push(...bareRefsOf(b.label, b.kind, b.block as Record<string, unknown>));

  const srcBlocks = new Set(rows.map((r) => r.src));
  console.log(
    `${rows.length} prefix-less reference(s) in ${srcBlocks.size} block(s), ` +
      `over ${blocks.size} block(s) loaded from ${paperDir}`,
  );

  const targets = [...new Set(rows.map((r) => r.ref))].sort();
  let missing = 0;
  let unexpectedKind = 0;

  console.log(`\n${targets.length} distinct target(s):`);
  for (const t of targets) {
    const hit = blocks.get(t);
    const n = rows.filter((r) => r.ref === t).length;
    switch (classifyTarget(hit?.kind)) {
      case "dangling":
        missing++;
        console.log(`  DANGLING  ${t}  ×${n}  — no block carries this label`);
        break;
      case "convention":
        unexpectedKind++;
        console.log(
          `  CONVENTION  ${t}  ×${n}  — exists, but kind=${hit!.kind} requires a prefix`,
        );
        break;
      default:
        console.log(`  ok  ${t}  ×${n}  — kind=${hit!.kind}, prefix optional for this kind`);
    }
  }

  if (missing || unexpectedKind) {
    console.log("\nReferrers of every non-ok target:");
    for (const r of rows) {
      if (classifyTarget(blocks.get(r.ref)?.kind) !== "ok")
        console.log(`  ${r.ref}  <-  ${r.src} [${r.srcKind}] .${r.field}`);
    }
  }

  console.log(
    `\nverdict: ${rows.length - missing - unexpectedKind} legitimate, ` +
      `${unexpectedKind} convention break(s), ${missing} dangling target(s).`,
  );
  if (!missing && !unexpectedKind)
    console.log(
      "Every prefix-less reference names an existing block whose kind does not\n" +
        "require a prefix. The generator's count is a convention report, not a\n" +
        "defect list — do not 'fix' these to drive the count to zero.",
    );

  return missing > 0 || anyFailure ? 1 : 0;
}

if (import.meta.main) {
  const i = process.argv.indexOf("--paper");
  const paper = i >= 0 ? process.argv[i + 1] : "quantum-observable-universe";
  const root = new URL("../../folio/", import.meta.url).pathname + paper;
  auditPaper(root)
    .then((c) => process.exit(c))
    .catch((e) => {
      console.error(e);
      process.exit(2);
    });
}
