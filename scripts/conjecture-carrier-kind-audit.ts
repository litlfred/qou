/**
 * What DECLARATION KIND does each conjecture's `lean.ref` actually resolve to?
 *
 * AGENTS.md §3b / §3b-tax require a conjecture to be carried by a content-
 * bearing `class` (or `structure`) so that downstream results can take it as
 * an explicit hypothesis.  Two other shapes occur in practice and neither is
 * seen by `content/pipeline/lean-vacuity-axiom-audit.ts`:
 *
 *   * `def X : Prop := True` (or a `match` whose every branch is `True`) —
 *     a content-free carrier that any `⟨⟩` discharges.  MEASURED 2026-09-03
 *     on the pre-fix `conj-im-q-physical-role.lean`: the vacuity audit reports
 *     `0 carrier(s) … 0 defect candidate(s)`.  It does not merely pass the
 *     file — it does not RECOGNISE it as a carrier, so `proof-claims-unencoded`
 *     / `true-class-field` / `proof-no-empty-prop-carrier` cannot fire.  Those
 *     criteria key on class/structure fields; this defect has no class.
 *
 *   * `axiom X : …` — a GLOBAL assumption.  Not vacuous, and often honest
 *     work (see `B1HyperbolicRowsTheorem`, which derives its count from a
 *     per-row axiom), but it pollutes `#print axioms` for every downstream
 *     statement unconditionally where a class would be carried explicitly.
 *
 * This reports the kind for every conjecture block so both shapes are visible.
 * It makes no verdict: an `axiom` carrier can be the right call, and a `def`
 * carrier with a real body is not vacuous.  Read the flagged files.
 *
 * Usage: bun run scripts/conjecture-carrier-kind-audit.ts
 */
import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";

const REPO = "/home/user/qou";
const PAPER = join(REPO, "content/quantum-observable-universe");
const LAKE_ROOTS: Record<string, string> = {
  qou: "content/quantum-observable-universe/lean",
  ugb: "content/unital-groebner-bases/lean",
  fred2005: "content/fred2005-formal-groups/lean",
};
const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

const cache = new Map<string, string[]>();
async function filesUnder(root: string, ext: string): Promise<string[]> {
  const k = root + "|" + ext;
  const hit = cache.get(k);
  if (hit) return hit;
  const out: string[] = [];
  const walk = async (d: string) => {
    let es;
    try { es = await readdir(d, { withFileTypes: true }); } catch { return; }
    for (const e of es) {
      if (e.name === ".lake" || e.name === "build" || e.name === "node_modules") continue;
      const p = join(d, e.name);
      if (e.isDirectory()) await walk(p);
      else if (e.name.endsWith(ext)) out.push(p);
    }
  };
  await walk(root);
  cache.set(k, out);
  return out;
}

const KW = "class|structure|theorem|lemma|def|abbrev|instance|axiom|opaque";

type Row = { label: string; kind: string; file: string; decl: string; body: string };
const rows: Row[] = [];
const noRef: string[] = [];
const unresolved: { label: string; ref: string }[] = [];

for (const ts of await filesUnder(PAPER, ".ts")) {
  const t = await readFile(ts, "utf8").catch(() => "");
  if (!/^\s*export default conjecture\(/m.test(t)) continue;
  const lm = t.match(/label:\s*"([^"]+)"/);
  const label = lm ? lm[1] : ts;
  const rm = t.match(/ref:\s*"([^:"]+):([^"]+)"/);
  if (!rm) { noRef.push(label); continue; }
  const declPath = rm[2];
  const name = declPath.split(".").pop()!;
  const lakeRoot = LAKE_ROOTS[rm[1]];
  if (!lakeRoot) { unresolved.push({ label, ref: declPath }); continue; }
  const re = new RegExp(
    String.raw`^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+|scoped\s+)*` +
    `(${KW})` + String.raw`\s+` + esc(name) + String.raw`\b`, "m");
  const cands = [
    ts.replace(/\.ts$/, ".lean"),
    join(REPO, lakeRoot, declPath.replace(/\./g, "/") + ".lean"),
    ...(await filesUnder(join(REPO, lakeRoot), ".lean")),
  ];
  let found = false;
  for (const f of cands) {
    let text: string;
    try { text = await readFile(f, "utf8"); } catch { continue; }
    const hit = re.exec(text);
    if (!hit) continue;
    const rest = text.slice(hit.index);
    const ends = [rest.indexOf("\n\n"), 2000].filter((n) => n > 0);
    rows.push({
      label, kind: hit[1], file: f.replace(REPO + "/", ""),
      decl: name, body: rest.slice(0, Math.min(...ends)),
    });
    found = true;
    break;
  }
  if (!found) unresolved.push({ label, ref: declPath });
}

const byKind = new Map<string, Row[]>();
for (const r of rows) byKind.set(r.kind, [...(byKind.get(r.kind) ?? []), r]);

console.log(`conjecture blocks with a lean.ref that resolves: ${rows.length}`);
console.log(`  no lean.ref at all:                            ${noRef.length}`);
console.log(`  lean.ref resolves to no declaration:           ${unresolved.length}`);
console.log();
for (const [k, v] of [...byKind].sort((a, b) => b[1].length - a[1].length)) {
  console.log(`  ${k.padEnd(10)} ${String(v.length).padStart(4)}`);
}

// A `def`/`abbrev` carrier whose body is `True`, or a match all of whose
// branches are `True`, asserts nothing.  Reported separately from other
// `def` carriers, which may well have a real body.
const defs = [...(byKind.get("def") ?? []), ...(byKind.get("abbrev") ?? [])];
const contentFree = defs.filter((r) => {
  const rhs = r.body.slice(r.body.indexOf(":=") + 2);
  const branches = [...rhs.matchAll(/=>\s*([A-Za-z_][\w.]*)/g)].map((m) => m[1]);
  if (branches.length) return branches.every((b) => b === "True");
  return /^\s*True\s*$/m.test(rhs.split("\n")[0] ?? "");
});
console.log();
console.log(`\`def\`/\`abbrev\` carriers whose body asserts only \`True\`: ${contentFree.length}`);
for (const r of contentFree) console.log(`  ${r.label}\n     ${r.file}  (${r.decl})`);
console.log();
console.log(`All \`def\`/\`abbrev\` carriers (a class/structure is what §3b-tax asks for):`);
for (const r of defs.sort((a, b) => a.label.localeCompare(b.label))) {
  console.log(`  ${contentFree.includes(r) ? "TRUE-ONLY" : "has body "} ${r.label}`);
}
console.log();
// A conjecture whose ref lands on a `theorem` is not automatically wrong: the
// file may declare the carrier class and the ref merely point at a derived
// consequence.  The propagation audit's `isClassAxiomatised` tests the FILE,
// so those still count.  What matters is a theorem-carrier in a file with NO
// class at all — then nothing in the corpus carries the conjecture.
const thms = byKind.get("theorem") ?? [];
const thmNoClass: Row[] = [];
for (const r of thms) {
  const text = await readFile(join(REPO, r.file), "utf8").catch(() => "");
  if (!/^\s*(?:class|structure)\s+\w+/m.test(text)) thmNoClass.push(r);
}
console.log(`\`theorem\` carriers: ${thms.length}, of which the FILE declares no class/structure: ${thmNoClass.length}`);
for (const r of thmNoClass.sort((a, b) => a.label.localeCompare(b.label))) {
  console.log(`  ${r.label}\n     ${r.file}  (${r.decl})`);
}
console.log();
console.log(`\`axiom\` carriers (global assumption where a class would be local):`);
for (const r of (byKind.get("axiom") ?? []).sort((a, b) => a.label.localeCompare(b.label))) {
  console.log(`  ${r.label}\n     ${r.file}  (${r.decl})`);
}
