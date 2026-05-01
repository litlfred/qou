#!/usr/bin/env bun
/**
 * Conjectural-propagation audit (CLAUDE.md §3b STRICT propagation).
 *
 * Walks every block manifest under
 * content/quantum-observable-universe/, builds the uses[] graph,
 * and reports every `theorem`/`proposition`/`lemma`/`corollary`
 * block whose uses[] cone transitively touches a `conj:` label.
 *
 * Per CLAUDE.md §3b: such blocks must be `conjecture` (or recast as
 * `remark` with `interprets:` if they are interpretations rather
 * than logical claims).
 *
 * Definitions are exempt — they name constructions, not logical
 * claims, and a definition whose well-formedness is conjectural
 * carries an explicit narrative note instead of being demoted.
 */
import { readdir, readFile } from "node:fs/promises";
import { join } from "node:path";

const ROOT = "/home/user/qou/content/quantum-observable-universe";

interface Block {
  label: string;
  kind: string;
  uses: string[];
  file: string;
}

const PROVABLE = new Set(["theorem", "proposition", "lemma", "corollary"]);

async function loadAll(): Promise<Map<string, Block>> {
  const blocks = new Map<string, Block>();
  // Walk every directory under ROOT.
  const dirs = await readdir(ROOT, { withFileTypes: true });
  for (const d of dirs) {
    if (!d.isDirectory()) continue;
    const dirPath = join(ROOT, d.name);
    const files = await readdir(dirPath);
    for (const f of files) {
      if (!f.endsWith(".ts")) continue;
      const path = join(dirPath, f);
      const text = await readFile(path, "utf8");
      // Crude but sufficient parse: find the builder name and the
      // label / uses fields. Avoid running TS — too slow + needs deps.
      const builderMatch = text.match(
        /export default (definition|theorem|proposition|lemma|corollary|conjecture|remark|prose|equation|diagram|example|simulator)\(/,
      );
      if (!builderMatch) continue;
      const kind = builderMatch[1];
      const labelMatch = text.match(/label:\s*"([^"]+)"/);
      if (!labelMatch) continue;
      const label = labelMatch[1];
      // Extract uses[] — find first `uses: [` and read until matching `]`.
      const usesIdx = text.indexOf("uses:");
      let uses: string[] = [];
      if (usesIdx >= 0) {
        const afterUses = text.slice(usesIdx);
        const arrStart = afterUses.indexOf("[");
        const arrEnd = afterUses.indexOf("]", arrStart);
        if (arrStart >= 0 && arrEnd > arrStart) {
          const arr = afterUses.slice(arrStart + 1, arrEnd);
          uses = [...arr.matchAll(/"([^"]+)"/g)].map((m) => m[1]);
        }
      }
      blocks.set(label, { label, kind, uses, file: path });
    }
  }
  return blocks;
}

function transitivelyTouchesConjecture(
  start: string,
  blocks: Map<string, Block>,
  cache: Map<string, Set<string>>,
): Set<string> {
  if (cache.has(start)) return cache.get(start)!;
  const visited = new Set<string>();
  const conjAncestors = new Set<string>();
  const stack = [start];
  while (stack.length) {
    const cur = stack.pop()!;
    if (visited.has(cur)) continue;
    visited.add(cur);
    const block = blocks.get(cur);
    if (!block) continue;
    for (const u of block.uses) {
      // Skip cross-paper / external refs (paper-dir:label or https).
      if (u.includes(":") && !u.startsWith("conj:") && !u.startsWith("def:")
          && !u.startsWith("thm:") && !u.startsWith("prop:")
          && !u.startsWith("lem:") && !u.startsWith("cor:")
          && !u.startsWith("rem:") && !u.startsWith("ex:")
          && !u.startsWith("sim:") && !u.startsWith("eq:")) {
        continue; // qualified cross-paper ref or URL
      }
      if (u.startsWith("conj:")) conjAncestors.add(u);
      if (!visited.has(u)) stack.push(u);
    }
  }
  cache.set(start, conjAncestors);
  return conjAncestors;
}

const blocks = await loadAll();
console.log(`Loaded ${blocks.size} blocks.`);
const cache = new Map<string, Set<string>>();
const violators: { label: string; kind: string; conj: string[]; file: string }[] = [];
for (const [label, block] of blocks) {
  if (!PROVABLE.has(block.kind)) continue;
  const conjAncestors = transitivelyTouchesConjecture(label, blocks, cache);
  if (conjAncestors.size > 0) {
    violators.push({
      label,
      kind: block.kind,
      conj: [...conjAncestors],
      file: block.file.replace("/home/user/qou/", ""),
    });
  }
}

violators.sort((a, b) => a.label.localeCompare(b.label));
console.log(`\nFound ${violators.length} provable blocks transitively touching a conjecture:\n`);
for (const v of violators) {
  console.log(`  ${v.kind.padEnd(11)} ${v.label.padEnd(60)} via {${v.conj.join(", ")}}`);
  console.log(`    ${v.file}`);
}

// Also emit a witness JSON.
await Bun.write(
  "/home/user/qou/folio-assistant/computations/conjectural-propagation-audit.witness.json",
  JSON.stringify(
    {
      audit: "conjectural-propagation (CLAUDE.md §3b STRICT)",
      generated: new Date().toISOString(),
      total_blocks: blocks.size,
      provable_blocks_touching_conjecture: violators.length,
      violators,
    },
    null,
    2,
  ),
);
console.log("\nWitness: folio-assistant/computations/conjectural-propagation-audit.witness.json");
