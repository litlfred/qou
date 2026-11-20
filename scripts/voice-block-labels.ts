import { Glob } from "bun";
const root = process.cwd() + "/folio/quantum-observable-universe";
const out: Record<string, { title?: string; dir: string; file: string; kind?: string }> = {};
const chapters: Record<string, string> = {};
for await (const f of new Glob("*/*.ts").scan(root)) {
  const [dir, base] = f.split("/");
  try {
    const m = (await import(`${root}/${f}`)).default;
    if (!m) continue;
    if (base === dir + ".ts") { if (m.title) chapters[dir] = m.title; continue; }
    if (m.label) out[m.label] = { title: m.title, dir, file: f.replace(/\.ts$/, ".md"), kind: m.kind };
  } catch (e) {}
}
console.log(JSON.stringify({ labels: out, chapters }));
