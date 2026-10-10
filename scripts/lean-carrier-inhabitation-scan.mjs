#!/usr/bin/env node
/**
 * Carrier inhabitation, done by parsing declarations rather than by regex over
 * flattened text.
 *
 * Two earlier attempts were both wrong, in opposite directions:
 *   1. line-anchored `instance …: C` — missed instances whose type sits on a
 *      continuation line (false "uninhabited": over-reports defects);
 *   2. the same regex over whitespace-collapsed text — bridged from an
 *      `instance` keyword to a *binder* `(d : C R)` in a LATER declaration
 *      (false "inhabited": under-reports defects).
 *
 * The reliable test is the one the scanner already uses for conclusions: split
 * into declarations, then take the conclusion at the FIRST TOP-LEVEL colon,
 * which by construction skips every binder colon. A declaration inhabits `C`
 * iff it is a value-producing kind and its conclusion head is `C`.
 */
import fs from "node:fs";
import path from "node:path";

const ROOT = "folio/quantum-observable-universe";
function walk(d, o = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) { if (e.name !== ".lake" && e.name !== "build") walk(p, o); }
    else if (e.name.endsWith(".lean")) o.push(p);
  }
  return o;
}
function stripComments(src) {
  let out = "", i = 0;
  while (i < src.length) {
    if (src.startsWith("/-", i)) {
      let depth = 1, j = i + 2;
      while (j < src.length && depth > 0) {
        if (src.startsWith("/-", j)) { depth++; j += 2; }
        else if (src.startsWith("-/", j)) { depth--; j += 2; }
        else { if (src[j] === "\n") out += "\n"; j++; }
      }
      i = j;
    } else if (src.startsWith("--", i)) { while (i < src.length && src[i] !== "\n") i++; }
    else out += src[i++];
  }
  return out;
}
function conclusionTypeAscription(sig) {
  let depth = 0;
  for (let i = 0; i < sig.length; i++) {
    const c = sig[i];
    if ("([{⦃".includes(c)) depth++;
    else if (")]}⦄".includes(c)) depth--;
    else if (c === ":" && depth === 0 && sig[i + 1] !== "=" && sig[i - 1] !== ":")
      return sig.slice(i + 1).trim();
  }
  return "";
}
const DECL =
  /^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|partial\s+|unsafe\s+)*(theorem|lemma|def|abbrev|instance|example|structure|class)\s*([A-Za-z_][\w'.]*)?/;
/** Kinds that PRODUCE a value of their stated type (i.e. can inhabit C). */
const VALUE_KINDS = /^(def|abbrev|instance|example)$/;

/** carrier name -> number of declarations inhabiting it */
const inhabits = new Map();
const files = walk(ROOT);
for (const f of files) {
  const code = stripComments(fs.readFileSync(f, "utf8"));
  const lines = code.split("\n");
  const starts = [];
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(DECL);
    if (m && /^\s{0,2}\S/.test(lines[i])) starts.push({ i, kind: m[1] });
  }
  for (let s = 0; s < starts.length; s++) {
    const { i, kind } = starts[s];
    if (!VALUE_KINDS.test(kind)) continue;
    const end = s + 1 < starts.length ? starts[s + 1].i : lines.length;
    const text = lines.slice(i, end).join("\n");
    let depth = 0, cut = -1;
    for (let k = 0; k < text.length - 1; k++) {
      const c = text[k];
      if ("([{⦃".includes(c)) depth++;
      else if (")]}⦄".includes(c)) depth--;
      else if (depth === 0 && c === ":" && text[k + 1] === "=") { cut = k; break; }
      else if (depth === 0 && text.startsWith("where", k) && /\s/.test(text[k - 1] ?? " ")) { cut = k; break; }
    }
    const sig = cut >= 0 ? text.slice(0, cut) : text;
    const concl = conclusionTypeAscription(sig);
    const head = concl.match(/^([A-Z][\w'.]*)/)?.[1];
    if (head) inhabits.set(head, (inhabits.get(head) ?? 0) + 1);
  }
}

const ledger = JSON.parse(fs.readFileSync("docs/audits/lean-vacuity-review-ledger.json", "utf8"));
const rows = [];
for (const key of Object.keys(ledger.entries).filter((k) => k.includes("self-assuming"))) {
  const [rel, decl] = key.split("::");
  const e = ledger.entries[key];
  const lines = fs.readFileSync(rel, "utf8").split("\n");
  const thm = lines.slice((e.line ?? 1) - 1, (e.line ?? 1) + 8).join("\n");
  const proj = thm.match(/[:=]\s*(?:by\s+)?(?:exact\s+)?([a-z][\w']*)\.([A-Za-z_][\w']*)/)
    ?? thm.match(/⟨\s*([a-z][\w']*)\.([A-Za-z_][\w']*)/);
  let carrier = null, field = null;
  if (proj) {
    field = proj[2];
    for (const m of thm.matchAll(/[[(]\s*([a-z][\w']*)\s*:\s*([A-Z][\w'.]*)/g))
      if (m[1] === proj[1]) carrier = m[2];
  }
  const kind = carrier
    ? (fs.readFileSync(rel, "utf8").match(new RegExp(`^(class|structure)\\s+${carrier}\\b`, "m"))?.[1] ?? "?")
    : "?";
  rows.push({ key, rel, decl, carrier, field, carrier_kind: kind, inhabitations: carrier ? (inhabits.get(carrier) ?? 0) : -1 });
}
const un = rows.filter((r) => r.inhabitations === 0);
const inh = rows.filter((r) => r.inhabitations > 0);
console.log(`candidates: ${rows.length}`);
console.log(`  carrier INHABITED (>=1 value decl of that type) : ${inh.length}`);
console.log(`  carrier NEVER inhabited                         : ${un.length}`);
console.log(`  carrier unresolved                              : ${rows.filter((r) => r.inhabitations < 0).length}`);
const byKind = (rs) => rs.reduce((a, r) => ((a[r.carrier_kind] = (a[r.carrier_kind] ?? 0) + 1), a), {});
console.log(`  inhabited by carrier kind   : ${JSON.stringify(byKind(inh))}`);
console.log(`  uninhabited by carrier kind : ${JSON.stringify(byKind(un))}`);
fs.writeFileSync("/tmp/claude-0/-home-user-qou/f1f77005-e63d-54f7-8945-62a1ab40f5c7/scratchpad/inhabited2.json", JSON.stringify(rows, null, 1));
for (const c of ["QIntRatioBoundSmall", "MISWAbelianisation", "LeviFormDefect", "CoreLeviContext", "TrefoilElectronMassConj", "KnotEigenbasisData"])
  console.log(`  check ${c.padEnd(30)} inhabitations=${inhabits.get(c) ?? 0}`);
