#!/usr/bin/env bun
/**
 * check-references-bib — is the committed `references.bib` what
 * `folio/schema/references.ts` generates? Writes nothing in the tree.
 *
 * C9 story B2 (issue #7528, bean `qou-8tlx`). `references.bib` is DERIVED from
 * the CSL-JSON bibliography by the platform's `export-bibtex.ts`, and a
 * committed copy of derived data drifts silently. This regenerates it into a
 * temp file and compares, ignoring only the `% Generated:` timestamp line,
 * which differs on every run by construction.
 *
 *   bun run scripts/check-references-bib.ts            # exit 0 current, 1 drift, 2 could not run
 *   bun run scripts/check-references-bib.ts --write    # regenerate references.bib in place
 *
 * Both modes call the platform generator (`buildBibtex` from
 * cat-harness-tools/pipeline/export-bibtex.ts) after configuring the registry,
 * so there is one generator and qou only supplies the entries.
 *
 * Until 2026-11-21 this script imported export-bibtex for its side effect and
 * pushed `--out` onto argv. The platform's CLI block runs only under
 * `import.meta.main`, which is false on import, so nothing was ever written and
 * every run ended in "could not regenerate" (exit 2): the drift check could not
 * report drift. It now calls the exported function directly.
 *
 * Like `run-validate-references.ts`, the registry must be configured BEFORE the
 * platform module is imported: `export-bibtex.ts` does its work at module scope.
 */
import { readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { configureReferenceRegistry } from "../folio-assistant/cat-harness-tools/pipeline/references-registry-di";

const ROOT = resolve(import.meta.dir, "..");
const committed = join(ROOT, "references.bib");
const write = process.argv.includes("--write");

let generated: string;
try {
  const bib = await import("../folio/schema/references");
  configureReferenceRegistry({
    references: bib.references,
    referenceMap: bib.referenceMap,
    CSLEntrySchema: bib.CSLEntrySchema,
  });
  const { buildBibtex } = await import("../folio-assistant/cat-harness-tools/pipeline/export-bibtex");
  generated = buildBibtex(bib.references, ROOT);
} catch (e) {
  console.error(`? could not regenerate references.bib: ${(e as Error).message}`);
  process.exit(2);
}

if (write) {
  writeFileSync(committed, generated);
  console.log(`wrote ${committed} (${generated.split("\n").length} lines)`);
  process.exit(0);
}

const strip = (s: string) => s.split("\n").filter((l) => !l.startsWith("% Generated:")).join("\n");
const want = strip(generated);
const have = strip(readFileSync(committed, "utf8"));
if (want === have) {
  console.log("✓ references.bib matches folio/schema/references.ts");
  process.exit(0);
}
const a = have.split("\n");
const b = want.split("\n");
let i = 0;
while (i < a.length && i < b.length && a[i] === b[i]) i++;
console.log(`✗ references.bib has drifted from folio/schema/references.ts (${a.length} vs ${b.length} lines; first difference at line ${i + 1})`);
console.log(`  committed: ${a[i] ?? "<end>"}`);
console.log(`  generated: ${b[i] ?? "<end>"}`);
process.exit(1);
