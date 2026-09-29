#!/usr/bin/env node
/**
 * Name-independent self-assuming-projection detector.
 *
 * The in-repo scanner (`folio/pipeline/lean-vacuity-axiom-audit.ts`,
 * `detectSelfAssuming`) gates a field-projection on the projected field's
 * NAME matching `CONCLUSION_FIELD` (`claim_`, `_holds`, `_eq`, …). Any class
 * field named outside that convention is invisible no matter how plainly it
 * posits the conclusion — the escape documented in `lean-proof-vacuity-audit.md`
 * §8 (`confinement_ident`, `factorization_ident`).
 *
 * This pass replaces the name gate with the structural test the skill doc names
 * as the real discriminator: does the projected field's DECLARED TYPE unify with
 * the theorem's CONCLUSION? Comparison is syntactic-after-normalisation
 * (strip the instance binder prefix `ctx.`, collapse whitespace), so it is
 * conservative: it reports only exact matches and will under- rather than
 * over-count.
 */
import fs from "node:fs";
import path from "node:path";

const ROOT = process.argv[2] ?? "folio/quantum-observable-universe";

/* ---------- file walk ---------- */
function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (e.name === ".lake" || e.name === "build") continue;
      walk(p, out);
    } else if (e.name.endsWith(".lean")) out.push(p);
  }
  return out;
}

/** Strip block comments (incl. `/-- … -/` docstrings) and `--` line comments. */
function stripComments(src) {
  let out = "";
  let i = 0;
  while (i < src.length) {
    if (src.startsWith("/-", i)) {
      let depth = 1;
      let j = i + 2;
      while (j < src.length && depth > 0) {
        if (src.startsWith("/-", j)) { depth++; j += 2; }
        else if (src.startsWith("-/", j)) { depth--; j += 2; }
        else { if (src[j] === "\n") out += "\n"; j++; }
      }
      i = j;
    } else if (src.startsWith("--", i)) {
      while (i < src.length && src[i] !== "\n") i++;
    } else {
      out += src[i++];
    }
  }
  return out;
}

const norm = (s) => s.replace(/\s+/g, " ").trim();

/* ---------- class/structure field tables ---------- */
/** name -> Map(field -> type) */
function collectCarriers(src) {
  const carriers = new Map();
  const lines = src.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/^(class|structure)\s+([A-Za-z_][\w'.]*)\b(.*)$/);
    if (!m) continue;
    // header may span lines until a line ending in `where`
    let hdr = m[3];
    let j = i;
    while (!/\bwhere\s*$/.test(lines[j]) && j < i + 12 && j + 1 < lines.length) {
      j++;
      hdr += " " + lines[j];
    }
    if (!/\bwhere\s*$/.test(lines[j])) continue;
    const fields = new Map();
    let k = j + 1;
    let cur = null;
    for (; k < lines.length; k++) {
      const L = lines[k];
      if (L.trim() === "") continue;
      if (!/^\s/.test(L)) break; // dedent ends the body
      const fm = L.match(/^\s+([A-Za-z_][\w']*)\s*:\s*(.*)$/);
      if (fm && !/^\s{6,}/.test(L)) {
        cur = fm[1];
        fields.set(cur, fm[2]);
      } else if (cur) {
        fields.set(cur, fields.get(cur) + " " + L.trim());
      }
    }
    carriers.set(m[2], fields);
    i = k - 1;
  }
  return carriers;
}

/* ---------- declaration parse ---------- */
const DECL =
  /^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+|scoped\s+)*(theorem|lemma|def|abbrev|instance|example)\s+([A-Za-z_][\w'.]*)/;

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

/** split a decl chunk into signature (before top-level `:=`) and body. */
function splitBody(chunk) {
  let depth = 0;
  for (let i = 0; i < chunk.length - 1; i++) {
    const c = chunk[i];
    if ("([{⦃".includes(c)) depth++;
    else if (")]}⦄".includes(c)) depth--;
    else if (c === ":" && chunk[i + 1] === "=" && depth === 0)
      return [chunk.slice(0, i), chunk.slice(i + 2)];
  }
  return null;
}

const DERIVES =
  /\b(trans|Iff\.intro|And\.intro|linarith|nlinarith|obtain|rcases|calc|rw|simp|mpr|mp|constructor|refine|apply|induction|cases|omega|ring|field_simp|norm_num|unfold|intro|fun)\b/;

const results = [];
const files = walk(ROOT);

for (const file of files) {
  const raw = fs.readFileSync(file, "utf8");
  const src = stripComments(raw);
  const carriers = collectCarriers(src);
  const lines = src.split("\n");

  for (let i = 0; i < lines.length; i++) {
    const dm = lines[i].match(DECL);
    if (!dm) continue;
    // gather the decl chunk until the next top-level decl / end / namespace
    let chunk = lines[i];
    let j = i + 1;
    for (; j < lines.length; j++) {
      if (
        /^(theorem|lemma|def|abbrev|instance|example|end|namespace|section|class|structure|open|@\[|noncomputable|private|protected|scoped)\b/.test(
          lines[j],
        )
      )
        break;
      chunk += "\n" + lines[j];
      if (chunk.length > 8000) break;
    }
    const parts = splitBody(chunk);
    if (!parts) { i = j - 1; continue; }
    const [sig, bodyRaw] = parts;
    const body = bodyRaw.trim();
    if (/\bsorry\b/.test(body)) { i = j - 1; continue; }

    // instance-binder: `[ctx : SomeCtx …]`  or `(ctx : SomeCtx …)` / `(d : D …)`
    const binders = [
      ...sig.matchAll(/[[(]\s*([a-z][\w']*)\s*:\s*([A-Z][\w'.]*)[^)\]]*[\])]/g),
    ];
    if (!binders.length) { i = j - 1; continue; }

    // body must be a bare projection or a tuple of them (no derivation)
    let projFields = null;
    let variable = null;
    let pattern = null;
    const single = body.match(
      /^(?:by\s+)?(?:exact\s+)?([a-z][\w']*)\.([A-Za-z_][\w']*)\s*$/,
    );
    if (single) {
      variable = single[1];
      projFields = [single[2]];
      pattern = "field-projection";
    } else if (/^⟨[\s\S]*⟩$/.test(body) && !DERIVES.test(body)) {
      const inner = body.slice(1, -1);
      const vars = [...inner.matchAll(/\b([a-z][\w']*)\.([A-Za-z_][\w']*)/g)];
      // every element must be a projection of the SAME variable, and there must
      // be no free-standing lemma application
      const stripped = inner.replace(/\b[a-z][\w']*\.[A-Za-z_][\w']*/g, "").replace(/[\s,⟨⟩]/g, "");
      if (vars.length >= 2 && stripped === "" && new Set(vars.map((v) => v[1])).size === 1) {
        variable = vars[0][1];
        projFields = vars.map((v) => v[2]);
        pattern = "tuple-projection";
      }
    }
    if (!projFields) { i = j - 1; continue; }

    const binder = binders.find((b) => b[1] === variable);
    if (!binder) { i = j - 1; continue; }
    const carrier = carriers.get(binder[2]);
    if (!carrier) { i = j - 1; continue; }

    const concl = conclusionTypeAscription(sig);
    if (!concl) { i = j - 1; continue; }
    // strip the binder prefix so field types (written bare inside the class)
    // are comparable with the conclusion (written `ctx.foo`)
    const nc = norm(concl.replace(new RegExp(`\\b${variable}\\.`, "g"), ""));

    let match = false;
    let detail = "";
    if (pattern === "field-projection") {
      const ft = carrier.get(projFields[0]);
      if (ft && norm(ft) === nc) { match = true; detail = norm(ft).slice(0, 160); }
    } else {
      const types = projFields.map((f) => carrier.get(f)).filter(Boolean);
      if (types.length === projFields.length) {
        const joinAnd = norm(types.map((t) => `(${t})`).join(" ∧ "));
        const bare = norm(types.join(" ∧ "));
        const nc2 = norm(concl.replace(new RegExp(`\\b${variable}\\.`, "g"), "").replace(/[()]/g, ""));
        if (bare === nc || joinAnd === nc || norm(bare.replace(/[()]/g, "")) === nc2) {
          match = true;
          detail = bare.slice(0, 160);
        }
      }
    }

    const CF =
      /^(exists_|claim_|is_|has_|selects_|are_|satisfies_|holds_|equals_)|(_holds|_eq|_iff|_property|_spec|_result)$|^(holds|property|spec|result|main|claim)$/;
    if (match) {
      results.push({
        file,
        line: i + 1,
        kind: dm[1],
        decl: dm[2],
        carrier: binder[2],
        pattern,
        fields: projFields,
        caught_by_name_gate: projFields.some((f) => CF.test(f)),
        conclusion: nc.slice(0, 200),
        field_type: detail,
      });
    }
    i = j - 1;
  }
}

const leaked = results.filter((r) => !r.caught_by_name_gate);
console.log(`scanned ${files.length} .lean under ${ROOT}`);
console.log(`type-matched self-assuming projections: ${results.length}`);
console.log(`  caught by the name gate (CONCLUSION_FIELD): ${results.length - leaked.length}`);
console.log(`  LEAKED past the name gate:                  ${leaked.length}`);
fs.writeFileSync(
  process.argv[3] ?? "/tmp/type-match-projections.json",
  JSON.stringify({ total: results.length, leaked: leaked.length, results }, null, 1),
);
console.log("\n=== LEAKED (field type ≡ conclusion, but name escapes the gate) ===");
for (const r of leaked) {
  console.log(`- ${r.file}:${r.line}`);
  console.log(`    ${r.kind} ${r.decl}  [${r.carrier}.${r.fields.join(", .")}]  (${r.pattern})`);
}
