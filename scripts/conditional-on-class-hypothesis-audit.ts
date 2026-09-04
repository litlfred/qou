/**
 * §3b-cond item 2 is UNCHECKED by `conjectural-propagation-audit.ts`.
 *
 * That audit splits provable blocks into `violators` and `conditional_on_class`
 * on ONE test: is every conjecture in the block's `uses[]` cone carried by a
 * Lean `class`?  AGENTS.md §3b-cond requires FIVE things, and item 2 —
 *
 *   "**Explicit hypothesis on Lean side.** The downstream block's Lean
 *    declaration has the class as an explicit `[Instance]` hypothesis."
 *
 * — is about the DOWNSTREAM block, which that audit never opens.  So a block
 * reported `conditional_on_class` may state its result unconditionally while
 * the corpus records it as a rigorous conditional result.  This script opens
 * each one and asks whether its declaration binds any class carrying a
 * conjecture in its own cone.
 *
 * BOTH BRACKET STYLES COUNT.  `[C M]` and `(h : C M)` carry the hypothesis in
 * the type identically; the instance bracket is an elaboration convenience,
 * not an epistemic difference, and §3b-cond's "[Instance]" wording must not be
 * read as excluding the explicit form.  An earlier cut of this script tested
 * for `[` alone and would have mis-flagged `prop:boltzmann-constant`, whose
 * theorems take `(sp : ArchimedeanSubstrateField M)` explicitly.
 *
 * THREE successive narrowings of this test each OVERSTATED the failure count,
 * every one caught by hand-checking a named block rather than by the number
 * looking wrong:
 *
 *   1. testing for a bare `[` missed `(sp : ArchimedeanSubstrateField M)`
 *      (`prop:boltzmann-constant`) — explicit binders carry the hypothesis too;
 *   2. requiring a CONE class missed `[ctx : B1Figure8RowContext]`
 *      (`prop:b1-figure-8-row-theorem`) — a locally-minted context class is a
 *      different defect (item 5), not an unconditional statement;
 *   3. matching `class` alone missed `(S : BodyOrderJetGrading)`
 *      (`lem:bond-order-eq-jet-degree`) — a `structure` binds identically;
 *   4. matching same-file declarations only missed `(amphi : Amphicheiral …)`
 *      (`cor:knot-factor-amphicheiral`), whose carrier lives upstream.
 *
 * The pattern is worth stating: every narrowing of a name-shaped detector
 * inflates the count of things it claims to have found.  Hand-check named
 * members of the failure bucket before quoting any figure from here.
 *
 * The test is NECESSARY, not sufficient: binding the class is item 2 only if
 * the proof actually uses it, which no regex can decide.  A block that FAILS
 * here definitively fails item 2; one that passes is merely not-yet-refuted.
 * Report the two numbers separately and never conflate them.
 *
 * Usage: bun run scripts/conditional-on-class-hypothesis-audit.ts [witness.json]
 */
import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";

const REPO = "/home/user/qou";
const LAKE_ROOTS: Record<string, string> = {
  qou: "content/quantum-observable-universe/lean",
  ugb: "content/unital-groebner-bases/lean",
  fred2005: "content/fred2005-formal-groups/lean",
};
const PAPER = join(REPO, "content/quantum-observable-universe");
const witnessPath = process.argv.slice(2).find((a) => !a.startsWith("--")) ??
  join(REPO, "docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json");

const esc = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

const leanCache = new Map<string, string[]>();
async function filesUnder(root: string, ext: string): Promise<string[]> {
  const key = root + "|" + ext;
  const hit = leanCache.get(key);
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
  leanCache.set(key, out);
  return out;
}

const DECL_KW =
  String.raw`(?:class|structure|theorem|lemma|def|abbrev|instance|axiom|opaque)`;

/** Resolve a lean.ref (from a block .ts) to (file, binder region of the decl). */
async function resolveDecl(tsAbs: string): Promise<{ file: string; sig: string } | null> {
  let ts: string;
  try { ts = await readFile(tsAbs, "utf8"); } catch { return null; }
  const m = ts.match(/ref:\s*"([^:"]+):([^"]+)"/);
  if (!m) return null;
  const declPath = m[2];
  const decl = declPath.split(".").pop()!;
  const lakeRoot = LAKE_ROOTS[m[1]];
  if (!lakeRoot) return null;
  const re = new RegExp(
    String.raw`^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+|scoped\s+)*` +
    DECL_KW + String.raw`\s+` + esc(decl) + String.raw`\b`, "m");
  const cands = [
    tsAbs.replace(/\.ts$/, ".lean"),
    join(REPO, lakeRoot, declPath.replace(/\./g, "/") + ".lean"),
    ...(await filesUnder(join(REPO, lakeRoot), ".lean")),
  ];
  for (const f of cands) {
    let text: string;
    try { text = await readFile(f, "utf8"); } catch { continue; }
    const hit = re.exec(text);
    if (!hit) continue;
    const rest = text.slice(hit.index);
    const ends = [rest.indexOf(":="), rest.indexOf("\nwhere"), 4000].filter((n) => n > 0);
    return { file: f.replace(REPO + "/", ""), sig: rest.slice(0, Math.min(...ends)) };
  }
  return null;
}

// label -> .ts path, over the whole paper
const byLabel = new Map<string, string>();
for (const f of await filesUnder(PAPER, ".ts")) {
  const t = await readFile(f, "utf8").catch(() => "");
  const m = t.match(/label:\s*"([^"]+)"/);
  if (m) byLabel.set(m[1], f);
}

/** Every `class` / `structure` name declared anywhere in the Lake tree. */
const ALL_CARRIERS = new Set<string>();
for (const root of Object.values(LAKE_ROOTS)) {
  for (const f of await filesUnder(join(REPO, root), ".lean")) {
    const t = await readFile(f, "utf8").catch(() => "");
    for (const m of t.matchAll(/^\s*(?:class|structure)\s+(\w+)/gm)) ALL_CARRIERS.add(m[1]);
  }
}
// Content-block siblings live outside the Lake globs but are equally real.
for (const f of await filesUnder(PAPER, ".lean")) {
  const t = await readFile(f, "utf8").catch(() => "");
  for (const m of t.matchAll(/^\s*(?:class|structure)\s+(\w+)/gm)) ALL_CARRIERS.add(m[1]);
}

const w = JSON.parse(await readFile(witnessPath, "utf8"));

// conjecture label -> class names its carrier declares
const classNames = new Map<string, string[]>();
for (const lbl of w.class_axiomatised_conjectures as string[]) {
  const ts = byLabel.get(lbl);
  if (!ts) { classNames.set(lbl, []); continue; }
  const d = await resolveDecl(ts);
  let text = "";
  if (d) text = await readFile(join(REPO, d.file), "utf8").catch(() => "");
  else text = await readFile(ts.replace(/\.ts$/, ".lean"), "utf8").catch(() => "");
  classNames.set(lbl, [...text.matchAll(/^\s*class\s+(\w+)/gm)].map((x) => x[1]));
}

const conditional = w.conditional_on_class as
  { label: string; kind: string; file: string; conj: string[] }[];

const carries: string[] = [];
const carriesDetail: { label: string; file: string; cls: string; sig: string }[] = [];
const fails: { label: string; file: string; cone: number }[] = [];
const unresolvedDecl: string[] = [];
const noCone: string[] = [];
const undecided: string[] = [];
const localCtx: string[] = [];

for (const b of conditional) {
  const d = await resolveDecl(join(REPO, b.file));
  if (!d) { unresolvedDecl.push(b.label); continue; }
  const cone = new Set<string>();
  for (const c of b.conj) for (const n of classNames.get(c) ?? []) cone.add(n);
  if (cone.size === 0) { noCone.push(b.label); continue; }
  const binds = (text: string) => [...cone].some((n) =>
    new RegExp(String.raw`[\[(]\s*(?:\w+\s*:\s*)?` + esc(n) + String.raw`\b`).test(text));
  if (binds(d.sig)) {
    carries.push(b.label);
    const hit = [...cone].find((n) =>
      new RegExp(String.raw`[\[(]\s*(?:\w+\s*:\s*)?` + esc(n) + String.raw`\b`).test(d.sig));
    carriesDetail.push({ label: b.label, file: d.file, cls: hit ?? "?", sig: d.sig });
    continue;
  }
  // BLIND SPOT of a signature-only test: Lean's file-level `variable [C M]`
  // never appears in the declaration's own binder region, yet does carry the
  // hypothesis when the statement references it.  Whether it is auto-included
  // is not decidable by regex, so these are reported UNDECIDED, never as
  // failures.  Without this bucket the failure count is overstated.
  const declText = await readFile(join(REPO, d.file), "utf8").catch(() => "");
  const varLines = declText.split("\n").filter((l) => /^\s*variable\b/.test(l)).join("\n");
  if (binds(varLines)) { undecided.push(b.label); continue; }
  // Binds SOME class, but not one from its cone: the block has minted a LOCAL
  // context class re-axiomatising the conjectural inputs rather than taking
  // the conjecture's own class.  That is not "states the result
  // unconditionally" — it is a DIFFERENT question, namely §3b-cond item 5
  // (does the local class carry genuine sub-hypotheses, or the block's own
  // conclusion as a field?), which a regex cannot settle.  Keeping these in
  // the failure bucket overstates it: `prop:b1-figure-8-row-theorem` is
  // `theorem b1_figure_8_row [ctx : B1Figure8RowContext]` and was mis-counted
  // as unconditional by an earlier cut of this script.
  // `structure` counts exactly as `class` does here: `(S : BodyOrderJetGrading)`
  // carries the hypotheses in the type, and instance resolution is a
  // convenience, not epistemics.  Matching `class` alone was the THIRD
  // narrowing of this test to overstate the failure count — see the header.
  void declText;
  // The carrier may be declared in ANY file of the Lake tree, not just this
  // one — `knot_factor_amphicheiral` binds `(amphi : Amphicheiral ...)`, whose
  // structure lives upstream.  Restricting to same-file declarations was the
  // FOURTH narrowing to overstate the count.  Match against every class /
  // structure name in the tree instead.
  const bindsLocal = [...d.sig.matchAll(/[\[(]\s*(?:\w+\s*:\s*)?([A-Z][\w.]*)/g)]
    .some((m) => ALL_CARRIERS.has(m[1].split(".").pop()!));
  if (bindsLocal) { localCtx.push(b.label); continue; }
  fails.push({ label: b.label, file: b.file, cone: cone.size });
}

// ---------------------------------------------------------------------------
// §3b-cond ITEM 5 — this audit is BLIND to it, and `binds_cone_class` is
// therefore an UPPER BOUND in the same way `binds_no_carrier` is a candidate
// set.  Item 2 asks whether the block binds a cone class; item 5 asks whether
// that class carries the block's own CONCLUSION as a field, in which case the
// "conditional theorem" is a projection and proves nothing modulo the class.
//
// A block can sit in `binds_cone_class` and be an item-5 violation.  At least
// one demonstrably was: `prop:reeb-bundle-complement-equals-volume` bound
// `MassVolumeFactorization`, whose three fields were `markov_trace : ℝ`,
// `jsj_volume_sum : ℝ` and `factorization_identity : markov_trace =
// jsj_volume_sum` — both reals chosen by the instance.  Commit `be967ae9f9`
// removed that class for exactly this reason, and the block then left the
// bucket, which reads as a regression and is the opposite (bean `qou-y4v0`).
//
// NO VERDICT IS COMPUTED HERE, deliberately.  Whether a field is a genuine
// sub-hypothesis or the conclusion in disguise is not decidable by regex, and
// this file's header already records four narrowings of a name-shaped test
// that each overstated what it claimed to find.  `--item5` prints the evidence
// — bound class, its field types, the theorem's conclusion — for an agent to
// adjudicate.  The bucket is small enough (single digits) to check every
// member by hand, which is the point.
if (process.argv.includes("--item5")) {
  console.log("§3b-cond item-5 EVIDENCE for the `binds_cone_class` bucket");
  console.log("(evidence for adjudication, NOT a verdict — see the comment above)\n");
  for (const c of carriesDetail.sort((a, b) => a.label.localeCompare(b.label))) {
    console.log(`${c.label}`);
    console.log(`  binds:  ${c.cls}`);
    let where = "", fields: string[] = [];
    for (const root of Object.values(LAKE_ROOTS)) {
      for (const f of await filesUnder(join(REPO, root), ".lean")) {
        const t = await readFile(f, "utf8").catch(() => "");
        const lines = t.split("\n");
        const i = lines.findIndex((l) =>
          new RegExp(String.raw`^\s*(?:class|structure)\s+` + esc(c.cls) + String.raw`\b`).test(l));
        if (i < 0) continue;
        where = f.replace(REPO + "/", "");
        // A class body is the INDENTED block following the declaration line,
        // up to the first non-indented, non-blank line.  Parsing it by a
        // lookahead regex silently produced zero fields for all nine members
        // — a detector reporting only about itself, which is the failure mode
        // this file's header is entirely about.
        for (let j = i + 1; j < lines.length; j++) {
          const l = lines[j];
          if (l.trim() === "") continue;
          if (!/^\s/.test(l)) break;
          const m = /^\s*(\w+)\s*:\s*(.+?)\s*$/.exec(l);
          if (m && !/^--/.test(l.trim())) fields.push(`${m[1]} : ${m[2]}`);
        }
        break;
      }
      if (where) break;
    }
    console.log(`  declared in: ${where || "(not found in Lake tree)"}`);
    if (fields.length) for (const f of fields) console.log(`    field: ${f}`);
    else console.log("    (no fields parsed — inspect by hand)");
    // The conclusion is what follows the LAST top-level ` : ` in the signature.
    const flat = c.sig.replace(/\s+/g, " ").trim();
    const ci = flat.lastIndexOf(" : ");
    console.log(`  conclusion: ${(ci < 0 ? flat : flat.slice(ci + 3)).slice(0, 220)}`);
    console.log();
  }
  console.log("Adjudicate each: does a field carry the block's CONCLUSION, or genuine");
  console.log("sub-hypotheses it composes?  Only the latter satisfies §3b-cond item 5.");
}

console.log(`conditional_on_class blocks:                     ${conditional.length}`);
console.log(`  lean.ref declaration not resolvable:           ${unresolvedDecl.length}`);
console.log(`  no class name found anywhere in cone:          ${noCone.length}`);
console.log(`  BINDS a cone class (item 2 not refuted):       ${carries.length}`);
console.log(`  file-level \`variable\` binds it — UNDECIDED:     ${undecided.length}`);
console.log(`  binds SOME carrier, not the cone's own:    ${localCtx.length}`);
console.log(`  binds NO class at all — UNCONDITIONAL:          ${fails.length}`);
console.log();
console.log("Blocks reported conditional-on-class that bind NO class at all — their");
console.log("Lean states the result unconditionally, so §3b-cond item 2 fails outright:");
for (const f of fails.sort((a, b) => a.label.localeCompare(b.label))) {
  console.log(`  ${f.label}  (${f.cone} candidate classes in cone)`);
}
if (unresolvedDecl.length) {
  console.log("\nlean.ref does not resolve to any declaration (a separate defect):");
  for (const l of unresolvedDecl.sort()) console.log(`  ${l}`);
}
await Bun.write(
  join(REPO, "docs/audits/2026-09-03-conditional-on-class-hypothesis.witness.json"),
  JSON.stringify({
    audit: "conditional-on-class-hypothesis (AGENTS.md §3b-cond item 2)",
    generated: new Date().toISOString(),
    source_witness: witnessPath.replace(REPO + "/", ""),
    note:
      "The propagation audit splits blocks on whether their CONE's conjectures " +
      "are class-axiomatised; it never opens the downstream block, so §3b-cond " +
      "item 2 is unchecked. This measures that. `binds_no_carrier` is a " +
      "CANDIDATE set for hand triage, NOT a violation count: an unconditionally " +
      "true theorem correctly binds nothing (hand-checked: " +
      "lem:frobenius-cocasimir-refuted-deuteron is a numeric refutation, " +
      "prop:alpha-k-derivation-procedure is generic linear algebra).",
    conditional_on_class_total: conditional.length,
    decl_unresolvable: unresolvedDecl.sort(),
    binds_cone_class: carries.sort(),
    binds_other_carrier: localCtx.sort(),
    binds_no_carrier: fails.map((f) => f.label).sort(),
    counts: {
      total: conditional.length,
      decl_unresolvable: unresolvedDecl.length,
      binds_cone_class: carries.length,
      variable_undecided: undecided.length,
      binds_other_carrier: localCtx.length,
      binds_no_carrier: fails.length,
    },
  }, null, 2) + "\n",
);

if (localCtx.length) {
  console.log("\nBinds a LOCALLY-MINTED context class rather than the conjecture's own.");
  console.log("Not unconditional; needs §3b-cond item-5 inspection (genuine");
  console.log("sub-hypotheses, or the conclusion smuggled in as a field?):");
  for (const l of localCtx.sort()) console.log(`  ${l}`);
}
if (undecided.length) {
  console.log("\nUNDECIDED — a file-level `variable` binds a cone class; whether Lean");
  console.log("auto-includes it in this statement is not decidable by regex:");
  for (const l of undecided.sort()) console.log(`  ${l}`);
}
if (noCone.length) {
  console.log("\nCone's conjectures declare no `class` — audit route (c) matched a non-class file:");
  for (const l of noCone.sort()) console.log(`  ${l}`);
}
