import { resolveCanonicalLean } from "../folio-assistant/content/pipeline/qa-utils";
import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join } from "node:path";
const ROOT = "/workspace/qou";
const CONTENT = join(ROOT, "content/quantum-observable-universe");
const blocks: {file:string; label:string; ref:string}[] = [];
(function walk(d: string) {
  for (const e of readdirSync(d)) {
    const p = join(d, e);
    if (statSync(p).isDirectory()) { if (!p.includes("/lean/")) walk(p); continue; }
    if (!p.endsWith(".ts")) continue;
    const s = readFileSync(p, "utf-8");
    const lab = s.match(/label:\s*"([^"]+)"/);
    const ref = s.match(/ref:\s*\n?\s*"(qou:[^"]+)"/);
    if (lab && ref) blocks.push({ file: p, label: lab[1], ref: ref[1] });
  }
})(CONTENT);
const dangling: typeof blocks = [];
for (const b of blocks) {
  const sib = b.file.slice(0, -3) + ".lean";
  if (existsSync(sib)) continue;
  let r: string | undefined;
  try { r = resolveCanonicalLean(b.ref, ROOT); } catch { r = undefined; }
  if (r === undefined) dangling.push(b);
}
console.log(`REFS=${blocks.length} DANGLING=${dangling.length}`);
for (const d of dangling) console.log(`${d.label}\t${d.ref}`);
