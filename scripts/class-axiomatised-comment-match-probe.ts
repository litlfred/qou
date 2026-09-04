/** Does `isClassAxiomatised`'s `/\bclass\s+\w+/` on RAW text match comments? */
import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";
const REPO = "/home/user/qou";
const PAPER = join(REPO, "content/quantum-observable-universe");
const LAKE = join(REPO, "content/quantum-observable-universe/lean");
const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
async function walk(d: string, ext: string, out: string[] = []): Promise<string[]> {
  let es; try { es = await readdir(d, { withFileTypes: true }); } catch { return out; }
  for (const e of es) {
    if (e.name === ".lake" || e.name === "build" || e.name === "node_modules") continue;
    const p = join(d, e.name);
    if (e.isDirectory()) await walk(p, ext, out); else if (e.name.endsWith(ext)) out.push(p);
  }
  return out;
}
function strip(text: string): string {
  let out = "", depth = 0;
  for (let i = 0; i < text.length; i++) {
    if (text[i] === "/" && text[i + 1] === "-") { depth++; i++; continue; }
    if (depth > 0 && text[i] === "-" && text[i + 1] === "/") { depth--; i++; continue; }
    if (depth > 0) { out += text[i] === "\n" ? "\n" : " "; continue; }
    out += text[i];
  }
  return out.split("\n").map((l) => l.replace(/--.*$/, "")).join("\n");
}
const leanFiles = await walk(LAKE, ".lean");
const w = JSON.parse(await readFile(
  join(REPO, "docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json"), "utf8"));
const byLabel = new Map<string, string>();
for (const f of await walk(PAPER, ".ts")) {
  const t = await readFile(f, "utf8").catch(() => "");
  const m = t.match(/label:\s*"([^"]+)"/);
  if (m) byLabel.set(m[1], f);
}
const KW = "class|structure|theorem|lemma|def|abbrev|instance|axiom|opaque";
const commentOnly: string[] = [], real: string[] = [], unres: string[] = [];
for (const lbl of w.class_axiomatised_conjectures as string[]) {
  const ts = byLabel.get(lbl); if (!ts) { unres.push(lbl); continue; }
  const t = await readFile(ts, "utf8").catch(() => "");
  const rm = t.match(/ref:\s*"([^:"]+):([^"]+)"/); if (!rm) { unres.push(lbl); continue; }
  const declPath = rm[2], name = declPath.split(".").pop()!;
  // reproduce the audit's own resolution order
  const cands = [ts.replace(/\.ts$/, ".lean"),
                 join(LAKE, declPath.replace(/\./g, "/") + ".lean")];
  let text: string | null = null;
  for (const c of cands) { try { text = await readFile(c, "utf8"); break; } catch { /* next */ } }
  if (text === null) {
    const re = new RegExp(String.raw`^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+|scoped\s+)*(?:${KW})\s+` + esc(name) + String.raw`\b`, "m");
    for (const f of leanFiles) {
      const x = await readFile(f, "utf8").catch(() => ""); if (re.test(x)) { text = x; break; }
    }
  }
  if (text === null) { unres.push(lbl); continue; }
  const raw = /\bclass\s+\w+/.test(text);          // what the audit tests
  const decl = /^\s*class\s+\w+/m.test(strip(text)); // a real declaration
  if (raw && !decl) commentOnly.push(lbl); else if (decl) real.push(lbl); else unres.push(lbl);
}
console.log(`class_axiomatised as reported:      ${(w.class_axiomatised_conjectures as string[]).length}`);
console.log(`  a real \`class\` declaration:      ${real.length}`);
console.log(`  ONLY the word "class" in a comment:${String(commentOnly.length).padStart(4)}`);
console.log(`  could not resolve to a file:      ${unres.length}`);
console.log();
for (const l of commentOnly.sort()) console.log(`  COMMENT-ONLY  ${l}`);
