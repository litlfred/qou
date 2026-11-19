#!/usr/bin/env bun
/**
 * Circular-anchor / vacuous-check audit.
 *
 * A probe can be numerically correct, precision-clean, witness-backed and
 * still establish **nothing about the quantity it appears to test**, because
 * its "confirmation" is a round-trip: a value is derived by inverting a
 * relation at a fixed constant, and the constant is then recovered from that
 * value and reported as agreement. Nothing in the existing QA axes catches
 * this — the arithmetic is right, the witness is fresh, the assertions pass.
 * The defect is *epistemic*, not numerical.
 *
 * History (why this exists). `qbeta_t4_stokes3_crux_probe.py` fixes
 * `A_omega = 3`, defines `theta2 = ln2_q0 - S/(A_omega*kappa)` at each anchor,
 * and reports "both anchors yield real theta with correct boost/spin
 * dominance". Recovering `A` from those `theta` returns 3 by construction; the
 * cited "0.6% two-anchor consistency" is rounding in the 8-digit theta values,
 * not independent agreement. Two of its reported checks are worse than weak:
 * `diagonal_crossed` holds for EVERY `A > 0` (proved:
 * `QOU.QBeta.ThetaRealityBound.diagonal_crossed`) and `S_sign_correct` is a
 * hardcoded `True` in the results dict. Full analysis:
 * docs/scope/2026-08-01-t4-anchor-circularity.md.
 *
 * Detectors (deliberately high-recall / agent-confirmed — a `fail` here is a
 * CANDIDATE, not a verdict):
 *
 *   circ-vacuous-check         a results/verdict mapping binds a check-shaped
 *                              key (`*_correct`, `*_ok`, `*_crossed`,
 *                              `*_verified`, `*_holds`, `*_consistent`, ...)
 *                              to a LITERAL True/False instead of a computed
 *                              expression. The "check" cannot fail.
 *
 *   circ-anchor-inverted-roundtrip
 *                              a module-level numeric constant C is used in a
 *                              denominator/inversion to DEFINE a derived
 *                              quantity D, and the file also reports C (or D)
 *                              with confirmation language. Recovering C from D
 *                              is then circular.
 *
 *   circ-derived-used-as-input a hardcoded literal is annotated as derived
 *                              elsewhere (`# T4-inverted`, `back-solved`,
 *                              `derived from`, `inverted`) and is consumed as
 *                              an INPUT without the conditioning being carried.
 *                              Downstream reuse of an assumption-conditioned
 *                              value.
 *
 * Legitimate patterns are NOT flagged (or are exempted on agent review):
 *  - a constant used purely as a scale with no round-trip claim;
 *  - a check literal inside a *test fixture* asserting an expected value;
 *  - a derived value reused WITH explicit conditioning recorded (a comment or
 *    witness field naming the assumption, e.g. "conditional on A=3").
 *
 * Mechanical + agentic, mirroring `lean-vacuity-axiom-audit.ts`: the script
 * finds candidates; an agent adjudicates and records the verdict in a
 * committed ledger, keyed by file sha so a verdict goes stale the moment the
 * file changes.
 *
 *   bun run content/pipeline/circular-anchor-audit.ts \
 *     [root ...]                   # default: computations/
 *     [--json docs/audits/<date>-circular-anchor-audit.json]
 *     [--write-sidecars]           # upsert <block>.qa.json script entries
 *     [--only <criterion>]
 *     [--review-ledger docs/audits/circular-anchor-review-ledger.json]
 *     [--check-ledger  docs/audits/circular-anchor-review-ledger.json]
 *     [--quiet]
 *
 * `--review-ledger` seeds/refreshes the ledger (new or file-changed
 * candidates → `needs-agent`). `--check-ledger` exits 1 unless every
 * non-exempt candidate carries a FRESH agent verdict
 * (`genuine` | `legit` | `advisory`) whose recorded file sha still matches.
 */

import { createHash } from "node:crypto";
import { readFileSync, writeFileSync, existsSync, readdirSync, statSync } from "node:fs";
import { join, relative } from "node:path";

const CRITERIA = [
  "circ-vacuous-check",
  "circ-anchor-inverted-roundtrip",
  "circ-derived-used-as-input",
] as const;
type Criterion = (typeof CRITERIA)[number];

interface Finding {
  file: string;
  criterion: Criterion;
  line: number;
  symbol: string;
  evidence: string;
  severity: "critical" | "major" | "advisory";
}

interface LedgerEntry {
  file: string;
  criterion: string;
  symbol: string;
  line: number;
  verdict: "needs-agent" | "genuine" | "legit" | "advisory";
  file_sha: string;
  reviewer?: string;
  reviewed_at?: string;
  disposition?: string;
  evidence?: string;
}

const shaOfTop = (rel: string) =>
  existsSync(rel) ? sha12(readFileSync(rel, "utf8")) : "";

const sha12 = (s: string) => createHash("sha256").update(s).digest("hex").slice(0, 12);

/** Check-shaped identifiers: a key whose NAME asserts a verified property. */
const CHECK_KEY =
  /^["']?([A-Za-z_][A-Za-z0-9_]*(?:_(?:correct|ok|verified|holds|valid|passes|passed|consistent|confirmed|satisfied)|crossed|_crossed))["']?$/i;

/** Language that claims a result was confirmed rather than merely computed. */
const CONFIRM_WORDS =
  /\b(confirm(?:s|ed|ation)?|consistent|consistency|recover(?:s|ed|y)?|validat(?:e|es|ed|ion)|verif(?:y|ies|ied)|agree(?:s|ment)?|reproduc(?:e|es|ed)|check(?:s|ed)? out|yields?\b.*\bcorrect)\b/i;

/** Annotations marking a literal as having been derived under an assumption. */
const DERIVED_MARK =
  /\b(back[- ]?solved|inverted|T\d-inverted|derived from|solved from|fitted from|obtained by inverting|conditional on)\b/i;

/** Comments that explicitly carry the conditioning — exempts circ-derived. */
const CONDITIONING_CARRIED =
  /\b(conditional on|assumes|assuming|given\s+A|NOT independent|circular|conditioned on|under the assumption)\b/i;

function walk(dir: string, out: string[] = []): string[] {
  if (!existsSync(dir)) return out;
  for (const e of readdirSync(dir)) {
    if (e === "node_modules" || e === ".git" || e === "__pycache__") continue;
    const p = join(dir, e);
    const st = statSync(p);
    if (st.isDirectory()) walk(p, out);
    else if (p.endsWith(".py")) out.push(p);
  }
  return out;
}

/** Strip Python comments/strings crudely for structural scans (keeps line count). */
function codeLines(src: string): string[] {
  return src.split("\n").map((l) => l.replace(/#.*$/, ""));
}

function detect(file: string, src: string): Finding[] {
  const findings: Finding[] = [];
  const raw = src.split("\n");
  const code = codeLines(src);

  // ---- circ-vacuous-check: check-shaped key bound to a literal boolean ----
  raw.forEach((line, i) => {
    // ONLY the dict-literal form:  "diagonal_crossed": True,
    // A bare `ok = True` assignment is the standard accumulator idiom
    // (`ok = True` … `if bad: ok = False`) and is NOT a vacuous check — that
    // shape produced 300+ false positives on the first run and is excluded.
    const m = line.match(/^\s*(["'][A-Za-z_][A-Za-z0-9_]*["'])\s*:\s*(True|False)\s*,?\s*(#.*)?$/);
    if (!m) return;
    const key = m[1];
    if (!CHECK_KEY.test(key)) return;
    // exempt: an explicit expected-value fixture (expected=..., target=...)
    if (/\b(expected|target|reference|golden)\b/i.test(line)) return;
    // exempt: the same key is bound to a COMPUTED expression somewhere else.
    // Parse the value and test it, rather than using a lookahead — a
    // `\\s*(?!True)` lookahead backtracks to zero-width and spuriously
    // matches " True", which silently exempted the motivating T4 case.
    const bare = key.replace(/["']/g, "");
    const valRe = new RegExp(`(?:["']${bare}["']\\s*:|\\b${bare}\\s*=)\\s*([^,\\n]+?)\\s*,?\\s*(?:#.*)?$`);
    const computedElsewhere = raw.some((l, j) => {
      if (j === i) return false;
      const mm = l.match(valRe);
      if (!mm) return false;
      const v = mm[1].trim();
      return v !== "True" && v !== "False";
    });
    if (computedElsewhere) return;
    findings.push({
      file,
      criterion: "circ-vacuous-check",
      line: i + 1,
      symbol: key.replace(/["']/g, ""),
      evidence:
        `check-shaped key bound to the literal ${m[2]}: \`${line.trim()}\` — ` +
        `the reported check cannot fail, so it certifies nothing` +
        (m[2] === "False"
          ? `. NOTE: a literal False is CONSERVATIVE — it cannot manufacture a `
            + `passing claim, and is often a legitimate recording of a negative `
            + `result. Severity is reduced accordingly.`
          : ``),
      // Direction matters. The hazard this criterion exists to catch is a check
      // that always PASSES (the T4 `"diagonal_crossed": True` case). A literal
      // False always fails, so it can never launder a success — it is usually a
      // recorded negative. Measured on the 2026-08-07 ledger drain: 2 of the 5
      // vacuous-check candidates were literal-False recordings of genuine
      // negative results, and both adjudicated `legit`.
      severity: m[2] === "False" ? "advisory" : "critical",
    });
  });

  // ---- circ-anchor-inverted-roundtrip ----
  // module-level numeric constants
  const consts = new Map<string, number>();
  code.forEach((line, i) => {
    const m = line.match(/^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(-?\d+(?:\.\d+)?)\s*$/);
    if (m) consts.set(m[1], i + 1);
  });
  for (const [c, cline] of consts) {
    // a derived variable defined by inverting a relation containing C
    const invRe = new RegExp(
      `^\\s*([A-Za-z_][A-Za-z0-9_]*)\\s*=\\s*.*/\\s*\\(?[^)\\n]*\\b${c}\\b`,
    );
    const invRe2 = new RegExp(
      `^\\s*([A-Za-z_][A-Za-z0-9_]*)\\s*=\\s*.*\\b${c}\\b[^\\n]*\\)?\\s*$`,
    );
    let derived: { name: string; line: number } | null = null;
    for (let i = 0; i < code.length; i++) {
      const m = code[i].match(invRe);
      if (m && m[1] !== c) {
        derived = { name: m[1], line: i + 1 };
        break;
      }
    }
    // also catch `coeff = A_omega * kappa` then `x = ... / coeff`
    if (!derived) {
      for (let i = 0; i < code.length; i++) {
        const m = code[i].match(invRe2);
        if (!m || m[1] === c) continue;
        const alias = m[1];
        const aliasInv = new RegExp(
          `^\\s*([A-Za-z_][A-Za-z0-9_]*)\\s*=\\s*.*/\\s*\\(?[^)\\n]*\\b${alias}\\b`,
        );
        for (let j = i + 1; j < code.length; j++) {
          const m2 = code[j].match(aliasInv);
          if (m2 && m2[1] !== alias) {
            derived = { name: m2[1], line: j + 1 };
            break;
          }
        }
        if (derived) break;
      }
    }
    if (!derived) continue;
    // Confirmation language must come from CODE, not from a docstring or
    // comment. Measured 2026-08-07 (qou-yfsp): scanning `raw` matched prose —
    // an mpmath `DPS` knob was "confirmed" by a formula in the module
    // docstring, a `Q0` by the phrase "the three confirmed atoms". `code` is
    // index-aligned with `raw`, so the quote below still resolves.
    const confirmLine = code.findIndex(
      (l) =>
        CONFIRM_WORDS.test(l) &&
        (new RegExp(`\\b${c}\\b`).test(l) ||
          new RegExp(`\\b${derived!.name}\\b`).test(l) ||
          /\bboth anchors?\b/i.test(l)),
    );
    if (confirmLine < 0) continue;
    findings.push({
      file,
      criterion: "circ-anchor-inverted-roundtrip",
      line: cline,
      symbol: c,
      evidence:
        `constant \`${c}\` (line ${cline}) is USED TO DEFINE \`${derived.name}\` ` +
        `(line ${derived.line}); the file also reports confirmation language at ` +
        `line ${confirmLine + 1}: "${raw[confirmLine].trim().slice(0, 110)}". ` +
        `CANDIDATE ONLY — this is forward dataflow, which is legitimate when ` +
        `\`${c}\` is a tagged calibration input (VOL_41 -> q0 is exactly how q0 ` +
        `is meant to be pinned). It is circular only if \`${derived.name}\` is then ` +
        `presented as EVIDENCE FOR \`${c}\`, which is a semantic judgement this ` +
        `script cannot make. An agent must adjudicate.`,
      // Downgraded from `critical` 2026-08-07 (qou-yfsp). Measured 6 of 6 false
      // positives on the first full drain: the script cannot distinguish a
      // legitimate forward calibration from a circular round-trip, because the
      // difference is whether the derived value is later offered as evidence
      // for the input — semantics, not dataflow. Reporting it as `critical`
      // trained reviewers to skim, which is worse than not reporting it.
      severity: "advisory",
    });
  }

  // ---- circ-derived-used-as-input ----
  raw.forEach((line, i) => {
    const m = line.match(/^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(-?\d+\.\d+|mp\.mpf\(["'][^"']+["']\))/);
    if (!m) return;
    if (!DERIVED_MARK.test(line)) return;
    // exempt when the conditioning is explicitly carried on the same or prior line
    const ctx = (raw[i - 1] ?? "") + " " + line + " " + (raw[i + 1] ?? "");
    if (CONDITIONING_CARRIED.test(ctx) && !/T\d-inverted\s*$/.test(line.trim())) return;
    findings.push({
      file,
      criterion: "circ-derived-used-as-input",
      line: i + 1,
      symbol: m[1],
      evidence:
        `\`${m[1]}\` is a hardcoded literal annotated as derived ` +
        `("${(line.match(DERIVED_MARK) ?? [""])[0]}") and is consumed as an input ` +
        `without the conditioning being carried: \`${line.trim().slice(0, 110)}\``,
      severity: "major",
    });
  });

  return findings;
}

function main() {
  const argv = process.argv.slice(2);
  const roots: string[] = [];
  let jsonOut = "";
  let only = "";
  let reviewLedger = "";
  let checkLedger = "";
  let quiet = false;
  let writeSidecars = false;
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--json") jsonOut = argv[++i];
    else if (a === "--only") only = argv[++i];
    else if (a === "--review-ledger") reviewLedger = argv[++i];
    else if (a === "--check-ledger") checkLedger = argv[++i];
    else if (a === "--quiet") quiet = true;
    else if (a === "--write-sidecars") writeSidecars = true;
    else if (!a.startsWith("--")) roots.push(a);
  }
  if (roots.length === 0) roots.push("computations");

  const files: string[] = [];
  for (const r of roots) walk(r, files);

  const findings: Finding[] = [];
  const shas = new Map<string, string>();
  for (const f of files) {
    const src = readFileSync(f, "utf8");
    shas.set(f, sha12(src));
    for (const fd of detect(relative(process.cwd(), f), src)) {
      if (only && fd.criterion !== only) continue;
      findings.push(fd);
    }
  }

  if (!quiet) {
    console.log(`circular-anchor-audit: ${files.length} python files, ` +
      `${findings.length} candidate(s)`);
    for (const c of CRITERIA) {
      const n = findings.filter((f) => f.criterion === c).length;
      if (n) console.log(`  ${c}: ${n}`);
    }
    for (const f of findings.slice(0, 40)) {
      console.log(`\n  [${f.severity}] ${f.criterion}  ${f.file}:${f.line}  (${f.symbol})`);
      console.log(`      ${f.evidence}`);
    }
    if (findings.length > 40) console.log(`\n  … ${findings.length - 40} more`);
  }

  if (jsonOut) {
    writeFileSync(
      jsonOut,
      JSON.stringify(
        { $schema: "circular-anchor-audit/v1", generated_at: new Date().toISOString(), findings },
        null,
        1,
      ) + "\n",
    );
    if (!quiet) console.log(`\n  json → ${jsonOut}`);
  }

  // ---------- agentic ledger ----------
  const ledgerPath = reviewLedger || checkLedger;
  if (ledgerPath) {
    let ledger: { $schema: string; updated_at: string; entries: LedgerEntry[] } = {
      $schema: "circular-anchor-review/v1",
      updated_at: new Date().toISOString(),
      entries: [],
    };
    if (existsSync(ledgerPath)) ledger = JSON.parse(readFileSync(ledgerPath, "utf8"));

    // Line IS part of the key: the same symbol can be flagged at several lines
    // (e.g. two `S_sign_correct` entries), and a symbol-only key silently drops
    // all but the last via Map(), producing false passes in --check-ledger.
    // Line drift costs nothing extra — any edit that shifts lines also changes
    // file_sha, which already invalidates the verdict.
    const keyOf = (f: { file: string; criterion: string; symbol: string; line: number }) =>
      `${f.file}::${f.criterion}::${f.symbol}::${f.line}`;
    const prev = new Map(ledger.entries.map((e) => [keyOf(e), e]));
    // Single sha source for BOTH paths. The check path previously fell back to
    // "" when the map missed, which made every stored verdict read as stale.
    const shaOf = (rel: string) =>
      shas.get(rel) ?? (existsSync(rel) ? sha12(readFileSync(rel, "utf8")) : "");

    if (reviewLedger) {
      const next: LedgerEntry[] = [];
      for (const f of findings) {
        const sha = shaOf(f.file);
        const p = prev.get(keyOf(f));
        const fresh = p && p.verdict !== "needs-agent" && p.file_sha === sha;
        next.push(
          fresh
            ? { ...p! }
            : {
                file: f.file,
                criterion: f.criterion,
                symbol: f.symbol,
                line: f.line,
                verdict: "needs-agent",
                file_sha: sha,
                evidence: f.evidence,
              },
        );
      }
      ledger.entries = next;
      ledger.updated_at = new Date().toISOString();
      writeFileSync(ledgerPath, JSON.stringify(ledger, null, 1) + "\n");
      const nNeed = next.filter((e) => e.verdict === "needs-agent").length;
      console.log(`\n  ledger → ${ledgerPath} (${next.length} entries, ${nNeed} need agent review)`);
    }

    if (checkLedger) {
      const stale: string[] = [];
      for (const f of findings) {
        const sha = shaOf(f.file);
        const p = prev.get(keyOf(f));
        if (!p || p.verdict === "needs-agent") stale.push(`${keyOf(f)} — no agent verdict`);
        else if (p.file_sha !== sha) stale.push(`${keyOf(f)} — verdict stale (file changed)`);
      }
      if (stale.length) {
        console.error(`\n  ✗ ${stale.length} candidate(s) lack a fresh agent verdict:`);
        for (const s of stale.slice(0, 20)) console.error(`      ${s}`);
        process.exit(1);
      }
      console.log(`\n  ✓ every candidate carries a fresh agent verdict`);
    }
  }

  if (writeSidecars) {
    // Real upsert (was previously a no-op that only printed a note — a flag
    // implying writes that never happened). A probe usually has no block
    // sidecar, so this touches only findings whose file has a sibling
    // <basename>.qa.json; everything else is reported as skipped, loudly.
    let wrote = 0;
    const skipped: string[] = [];
    const byFile = new Map<string, Finding[]>();
    for (const f of findings) {
      const arr = byFile.get(f.file) ?? [];
      arr.push(f);
      byFile.set(f.file, arr);
    }
    for (const [file, fds] of byFile) {
      const sidecar = file.replace(/\.py$/, ".qa.json");
      if (!existsSync(sidecar)) {
        skipped.push(file);
        continue;
      }
      const sc = JSON.parse(readFileSync(sidecar, "utf8"));
      sc.criteria ??= {};
      const scriptSha = sha12(readFileSync("folio/pipeline/circular-anchor-audit.ts", "utf8"));
      for (const f of fds) {
        sc.criteria[f.criterion] ??= [];
        sc.criteria[f.criterion].push({
          field_hash: { py: shaOfTop(file) },
          result: "fail",
          reviewer: {
            kind: "script",
            id: "folio/pipeline/circular-anchor-audit.ts",
            version: "v1",
            script_hash: scriptSha,
          },
          reviewed_at: new Date().toISOString(),
          note: f.evidence,
        });
      }
      writeFileSync(sidecar, JSON.stringify(sc, null, 1) + "\n");
      wrote++;
    }
    console.log(`\n  sidecars: ${wrote} written; ${skipped.length} finding-file(s) ` +
      `have no sibling .qa.json (the ledger is their record)`);
  }
}

main();
