#!/usr/bin/env node
/**
 * Adjudicate the inhabited self-assuming candidates.
 *
 * Inhabitation is necessary but not sufficient. Reading the instance bodies
 * shows three kinds, and only one of them carries content:
 *
 *  - `Fact`-wrapper:  `instance … [hf : Fact P] : C … := ⟨hf.out⟩`
 *    Supplies nothing. It relabels the assumption `P` as an instance of `C`;
 *    whoever must discharge `Fact P` is exactly where the gap already was.
 *  - degenerate slice: `instance …_refl … : C k hk f f …` — inhabits only the
 *    diagonal (`f_k = f_inf`), where the bound reads `0 ≤ …` and closes by
 *    `positivity`. The projected theorem quantifies over ARBITRARY arguments,
 *    so the general claim is untouched.
 *  - substantive: instances with real proofs covering the class's parameter
 *    domain — e.g. QIntRatioBoundSmall's four instances discharge
 *    `m = 1,2,3,4` from `qInt_ratio_bound_m1..m4`, and the class itself binds
 *    `_hm4 : m ≤ 4`, so they EXHAUST it.
 *
 * Verdict: substantive coverage ⇒ `legit` (accessor idiom, content lives in
 * the instances). Only Fact-wrappers and/or degenerate slices ⇒ `genuine`.
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
const files = walk(ROOT);
const rows = JSON.parse(fs.readFileSync("/tmp/claude-0/-home-user-qou/f1f77005-e63d-54f7-8945-62a1ab40f5c7/scratchpad/inhabited2.json", "utf8"));

/**
 * A "substantive" instance must actually invoke something. An instance that
 * stipulates a constant and closes by `norm_num`/`rfl` proves only that the
 * constant it just chose has the property — it discharges the class without
 * supplying the content the class was standing in for. Two live examples,
 * both read by hand: `Term7ShellCorrectionClass`'s instance picks
 * `alpha5_value = -1` (its own docstring: "sign witness only", "placeholder"),
 * and `ZHabiroConvergenceClass`'s picks the constant bound `fun _ => 1`.
 *
 * Test: after removing tactic keywords, structural syntax and numerals, does
 * any external identifier remain (something with an `_` or a dotted name that
 * is not a local hypothesis)? Plus an explicit docstring check for
 * self-declared placeholders.
 */
// `unfold`/`show`/`change`/`dsimp` are definitional: they rewrite by a
// definition the author already wrote, so an instance closing with them has
// still supplied no mathematical content. ZHabiroConvergenceClass's instance
// is exactly this shape — `use fun _ => 1; use 1; … unfold brane_tower_pole;
// norm_num` — a constant witness that reads as substantive only because
// `unfold` names an identifier.
const TRIVIAL_TACTICS =
  /\b(by|refine|exact|use|intro|intros|constructor|norm_num|rfl|simp|simpa|positivity|omega|decide|trivial|ring|linarith|fun|And|Or|Iff|True|this|unfold|show|change|dsimp)\b/g;
function isTrivialWitness(body, lines, declLine) {
  const doc = lines.slice(Math.max(0, declLine - 12), declLine).join("\n");
  if (/placeholder|sign witness only|stipulat/i.test(doc)) return true;
  const rest = body
    .replace(TRIVIAL_TACTICS, " ")
    .replace(/[⟨⟩(),;:=<>≤≥∀∃∧∨¬→←↦·\[\]{}?_|+\-*/^]/g, " ")
    .replace(/\b\d+\b/g, " ")
    .replace(/\bh[\w']*\b/g, " ") // local hypotheses h, hq, hC, hz …
    .trim();
  const idents = rest.split(/\s+/).filter((t) => /[A-Za-z]/.test(t) && t.length > 2);
  return idents.length === 0;
}

function classifyInstances(carrier) {
  const kinds = [];
  for (const f of files) {
    const src = fs.readFileSync(f, "utf8");
    if (!src.includes(carrier)) continue;
    const lines = src.split("\n");
    for (let i = 0; i < lines.length; i++) {
      if (!/^\s*(?:noncomputable\s+)?(?:instance|def|abbrev)\b/.test(lines[i])) continue;
      const win = lines.slice(i, i + 16).join("\n");
      const head = win.split(/:=|(?<=\s)where(?=\s|$)/)[0];
      if (!new RegExp(`:\\s*${carrier}\\b`).test(head)) continue;
      const body = win.split(/:=|(?<=\s)where(?=\s)/).slice(1).join(":=");
      const name = lines[i].match(/(?:instance|def|abbrev)\s+([\w'.]+)/)?.[1] ?? "";
      if (/\bFact\b/.test(head) && /⟨\s*\w+\.out\s*⟩/.test(body)) kinds.push({ name, kind: "fact-wrapper" });
      else if (/_refl\b/.test(name) || /_of_eq\b/.test(name)) kinds.push({ name, kind: "degenerate-slice" });
      else if (isTrivialWitness(body, lines, i)) kinds.push({ name, kind: "trivial-witness" });
      else kinds.push({ name, kind: "substantive" });
    }
  }
  return kinds;
}

const NOW = "2026-08-09T21:10:00Z";
const LEDGER = "docs/audits/lean-vacuity-review-ledger.json";
const led = JSON.parse(fs.readFileSync(LEDGER, "utf8"));
const cache = new Map();
let legit = 0, genuine = 0, skipped = 0;

for (const r of rows) {
  if (r.inhabitations <= 0) continue;
  const e = led.entries[r.key];
  if (!e) continue;
  if (!cache.has(r.carrier)) cache.set(r.carrier, classifyInstances(r.carrier));
  const ks = cache.get(r.carrier);
  const sub = ks.filter((k) => k.kind === "substantive");
  const desc = ks.map((k) => `${k.name}(${k.kind})`).join(", ") || "none found";
  // A wrong `legit` is the dangerous direction: it closes the agent-inspection
  // gate on a real defect, whereas a wrong `genuine` only creates work. So
  // `legit` is written ONLY for carriers whose instances were read by hand in
  // this session. Everything else that merely LOOKS substantive stays
  // `needs-agent` with the classification recorded for the next reviewer.
  // Hand verdicts take precedence over the shape test — reading beats
  // heuristics, and where they disagreed the reading was right every time
  // (ZHabiroConvergenceClass's `use fun _ => 1` reads as substantive to the
  // test only because `unfold brane_tower_pole` names an identifier).
  const HAND_VERDICT = {
    QIntRatioBoundSmall: ["legit", "four instances discharge m = 1,2,3,4 from qInt_ratio_bound_m1..m4 with real analytic work; the class binds `_hm4 : m ≤ 4`, so they EXHAUST its domain"],
    QFactRatioBound: ["legit", "same shape as QIntRatioBoundSmall — four proved instances exhausting the bounded parameter domain"],
    GBResidueSpectralSum: ["legit", "`fromCrystalData` is a general builder constructing the structure from arbitrary crystal data, so accessors on it are the ordinary idiom"],
    BranchingConverges: ["genuine", "inhabited only by a Fact-wrapper (`⟨hf.out⟩`, relabels the assumption) and `branchingConverges_refl` (the diagonal f_k = f_inf, where the bound is 0 ≤ … and closes by positivity); the theorem quantifies over arbitrary f_k, f_inf"],
    Term7ShellCorrectionClass: ["genuine", "single instance stipulates alpha5_value = -1 and closes by norm_num/rfl; its own docstring calls it a placeholder / 'sign witness only'"],
    ZHabiroConvergenceClass: ["genuine", "single instance picks the constant bound `fun _ => 1` and closes by norm_num after `unfold brane_tower_pole`; the file's own prose says the substantive content 'remains' open"],
    SkeinMultisetInvariant: ["genuine", "only `skeinMultisetInvariant_refl config config … := ⟨rfl⟩` — the diagonal; the theorem takes two arbitrary configs, and is itself named `…_axiom`"],
    ConvergenceBound: ["genuine", "only `convergenceBound_refl … f f` — the diagonal, closed by simp/positivity"],
    KnotInvariantConvergence: ["genuine", "Fact-wrapper plus `…_refl` diagonal; no instance supplies the general bound"],
    NobleGasMultiOperator: ["genuine", "sole instance is a Fact-wrapper `⟨hf.out⟩` from `[hf : Fact (bindingMultiplicity S q ≥ 2)]` — it relabels the assumption and supplies nothing"],
    ConvergenceRate: ["genuine", "Fact-wrapper plus diagonal, same shape as BranchingConverges"],
    ShellClosureMonotone: ["genuine", "inhabited only at the degenerate slice"],
  };
  const hand = HAND_VERDICT[r.carrier];
  if (hand) {
    const [v, why] = hand;
    if (v === "legit") legit++; else genuine++;
    e.verdict = v;
    e.reviewer = "agent";
    e.reviewed_at = NOW;
    e.disposition = v === "legit" ? "no-fix" : "restate-to-derive-or-demote";
    e.evidence =
      (v === "legit"
        ? `Accessor idiom, not a defect. `
        : `Self-assuming projection: \`.${r.field}\` has the conclusion's type and is returned verbatim, and though \`${r.carrier}\` is inhabited, nothing that inhabits it supplies content. `) +
      `Instances read by hand: ${why}. (Automated shape test saw: ${desc}.)`;
    continue;
  }
  if (sub.length > 0) {
    skipped++;
    e.verdict = "needs-agent";
    e.reviewer = "agent";
    e.reviewed_at = NOW;
    e.evidence =
      `Type-matched projection of \`${r.carrier}.${r.field}\`. Carrier is inhabited and the instances ` +
      `(${desc}) look substantive under the automated shape test — no Fact-wrapper, no \`_refl\` ` +
      `diagonal, no constant-witness-closed-by-norm_num. NOT yet read by hand, and a wrong \`legit\` ` +
      `closes this gate on a real defect, so left open deliberately. To close: confirm the instances ` +
      `prove the property across the class's parameter domain (as QIntRatioBoundSmall's four do for ` +
      `\`m ≤ 4\`) rather than at a convenient slice.`;
    continue;
  }
  if (sub.length > 0) {
    legit++;
    e.verdict = "legit";
    e.disposition = "no-fix";
    e.evidence =
      `Accessor idiom, not a defect. \`${r.carrier}\` is genuinely inhabited by substantive ` +
      `instance(s): ${desc}. The projected field \`.${r.field}\` does equal the conclusion, but the ` +
      `mathematical content lives in those instances' proofs, so \`${r.decl}\` is the ordinary ` +
      `per-instance accessor (Mathlib's \`IsCompact.foo\` pattern), not a conclusion smuggled into a ` +
      `carrier nobody builds.`;
  } else {
    genuine++;
    e.verdict = "genuine";
    e.disposition = "restate-to-derive-or-demote";
    e.evidence =
      `Self-assuming projection: \`.${r.field}\` has the conclusion's type and is returned verbatim. ` +
      `\`${r.carrier}\` IS inhabited, but by nothing that supplies content: ${desc}. A ` +
      `\`Fact\`-wrapper instance (\`⟨hf.out⟩\` from \`[hf : Fact P]\`) merely relabels the assumption — ` +
      `whoever must discharge \`Fact P\` is exactly where the gap already was. A \`_refl\` instance ` +
      `inhabits only the diagonal (e.g. \`f_k = f_inf\`, where the bound reads \`0 ≤ …\` and closes by ` +
      `\`positivity\`), while \`${r.decl}\` quantifies over arbitrary arguments, so the general claim is ` +
      `untouched. Fix: restate so the class carries genuine sub-hypotheses the theorem composes, or ` +
      `demote (claim change, owner sign-off).`;
  }
  e.reviewer = "agent";
  e.reviewed_at = NOW;
}
led.updated_at = NOW;
fs.writeFileSync(LEDGER, JSON.stringify(led, null, 1) + "\n");
console.log(`legit   : ${legit}`);
console.log(`genuine : ${genuine}`);
console.log(`skipped : ${skipped}`);
console.log("\nper-carrier instance classification:");
for (const [c, ks] of cache)
  console.log(`  ${ks.some((k) => k.kind === "substantive") ? "LEGIT  " : "GENUINE"} ${c.padEnd(36)} ${ks.map((k) => k.kind).join(", ")}`);
