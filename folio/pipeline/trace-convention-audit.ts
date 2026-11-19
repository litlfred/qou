#!/usr/bin/env bun
/**
 * `trace-convention` QA axis — is a quoted trace value comparable?
 *
 * The registry rule (`docs/coordination/trace-convention-registry.md`) is one
 * sentence:
 *
 * > Any $\tau$ / $\mathrm{tr}_M$ value quoted below 0.1 % precision, and any
 * > cross-method comparison of trace values, must name its convention id from
 * > this registry with the script or Lean decl cited. **Convention-silent
 * > trace values are not comparable.**
 *
 * Nothing enforced it on the CONTENT layer. `trace_convention_registry_validate.py`
 * checks the registry against `computations/`, `tools/`, `qou-mass/` and the
 * three `doc_claims` rows it happens to list — it does not walk `content/**`,
 * so a `.md` block could quote a convention-C number indefinitely and every
 * gate stayed green. That is exactly how the two defects the registry was
 * opened for survived: a content block naming the full-Hecke Ocneanu trace (C)
 * for a channel whose production code supplies D (195.8 ppm on
 * $\beta_{\mathrm{Bor}}$, −197 ppm on $m_p$), and a $\det G$ comparison that
 * silently mixed the two.
 *
 * This is the content-layer half. One criterion — **`trace-convention`** —
 * with four detectors, all keyed off the registry JSON rather than off
 * constants copied into this file, so a registry edit re-arms the axis
 * automatically (the registry hash is carried as the sidecar `deps_hash`).
 *
 * ── The four detectors ────────────────────────────────────────────────────
 *
 *   `c-value-unlabelled`   (critical)
 *       A convention-**C** fingerprint — $z_C$, a C weight $y_\lambda$, the C
 *       value at $\beta_{\mathrm{Bor}}$, or the C Markov–Gram determinant —
 *       is quoted with no C/excision marker within ±400 characters.
 *       C was excised by the owner ruling of 2026-08-09; a C number that does
 *       not say so reads as production.
 *
 *   `c-formula-unlabelled`   (critical)
 *       `z` is DEFINED by the convention-C formula `1/(q^{1/2}+q^{-1/2})` with
 *       no C/excision marker within ±400 characters. The blind spot the value
 *       detectors cannot see: such a block quotes no number at all, so
 *       `c-value-unlabelled` never fires. It is also the larger surface — 26
 *       content files carry the symbolic form against 1 carrying an unlabelled
 *       C value.
 *
 *       Narrow by design: it matches only `z` BOUND to that reciprocal, never
 *       the expression alone. `q^{1/2} + q^{-1/2}` is `[2]_{√q}`, a legitimate
 *       Temperley–Lieb loop parameter at half-argument (it appears in the Wenzl
 *       positivity condition and in pair-skein formulas). 58 files contain the
 *       expression; flagging those would repeat the loose-grep error that once
 *       reported "70 producers" where the truth was 13.
 *
 *   `convention-silent-value`   (major)
 *       A registry value (either convention) is quoted and the block never
 *       names a convention anywhere — no "convention C/D", no `convention-d`
 *       tag, no link to the registry. This is the registry rule verbatim.
 *
 *   `unqualified-pairing`   (major)
 *       "indefinite" / "Lorentzian" / a $(3,1)$-style signature claim is made
 *       in a Markov–Gram context without naming the pairing. The Lorentzian
 *       reading was retracted in `748ba9b1`: it used the BILINEAR pairing
 *       $\mathrm{tr}_M(b_ib_j)$; the Hecke star is $T_w^{*} = T_{w^{-1}}$ and
 *       under $\mathrm{tr}_M(b_ib_j^{*})$ the form is POSITIVE — $(6,0,0)$
 *       under C, $(5,0,1)$ under D. The registry's own
 *       `blocked_migrations[0].signature_note` says the same thing.
 *
 *   `gram-inverse-unqualified`   (major)
 *       $G^{-1}$ / "invertible" / "non-degenerate" / $\det G \ne 0$ asserted of
 *       the Markov–Gram with no convention named nearby. $\det G = 0$ exactly
 *       under D (the $(1^3)$ block IS the radical), so such a claim is
 *       convention-C arithmetic wearing no label. The $2\times2$
 *       Chern–Simons pairing Gram $G_{\mathrm{CS}}$ is a DIFFERENT matrix and
 *       is not convention-scoped (registry §"Symbol collisions"); a window
 *       naming Chern–Simons is excluded.
 *
 * ── Numeric matching is exact, and it is a ROUNDING test ──────────────────
 *
 * Every decimal literal in the block with ≥ 6 significant digits is compared
 * against every registry value by rounding the 50-dps registry string to the
 * literal's own precision (round-half-up, BigInt digit strings — no float
 * anywhere, per the NO-FLOAT64 directive). So `0.4153958`, `0.41539579536`
 * and `0.41539579536061340131` all match $y^C_{(3)}$, and a number that merely
 * starts with the same two digits does not. Six significant digits is well
 * inside the registry's own 0.1 % (≈ 3 digit) threshold; a value quoted more
 * coarsely than that is out of mechanical scope and is an editorial judgement.
 *
 * ── Scope ─────────────────────────────────────────────────────────────────
 *
 * A block is IN SCOPE when its `.md`/`.ts` text touches the trace surface at
 * all (`tr_M`, Markov trace, Markov–Gram, $y_\lambda$, Ocneanu, the Markov
 * parameter $z$, or a convention id). Everything else is `n/a` — the axis
 * says nothing about a block that quotes no trace.
 *
 * ── Usage ─────────────────────────────────────────────────────────────────
 *
 *   bun run content/pipeline/trace-convention-audit.ts [path ...]
 *       [--write-sidecars]     upsert `trace-convention` into <block>.qa.json
 *       [--blocks-from <file>] newline-separated block paths (.md/.ts/base)
 *       [--json <out>]         machine-readable findings
 *       [--md <out>]           report
 *       [--selftest]           prove the axis can fail AND can clear
 *       [--quiet]
 *
 * Paths may be directories (walked) or individual block files. Default root:
 * `content/`. Exit 1 when any detector fires (so it can gate a pre-commit).
 *
 * `--selftest` is not decoration. A regression check that cannot fail is worse
 * than none, and this branch shipped two of those before this axis existed.
 * The self-test asserts, on in-memory fixtures, that (i) an unlabelled C value
 * FAILS, (ii) the same text with the C value removed PASSES, (iii) a labelled
 * C value passes, (iv) a convention-silent D value fails, (v) an unqualified
 * "Lorentzian" fails and naming the bilinear pairing clears it, and (vi) a
 * $G^{-1}$ claim fails while the Chern–Simons Gram does not. Run it before
 * trusting a green sweep.
 *
 * @module content/pipeline/trace-convention-audit
 */

import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import {
  existsSync,
  readFileSync,
  readdirSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

/** The single criterion id this axis writes into `<block>.qa.json`. */
const CRITERION = "trace-convention";

/** Registry — the sole source of the numeric fingerprints. */
const REGISTRY_JSON = "docs/coordination/trace-convention-registry.json";
const REGISTRY_MD = "docs/coordination/trace-convention-registry.md";

/** Minimum significant digits a literal must carry to be mechanically judged. */
const MIN_SIG_DIGITS = 6;

/** Locality window (characters, each side) for "is the label near the value". */
const WINDOW = 400;

type Severity = "critical" | "major" | "minor";
type Result = "pass" | "fail" | "n/a";

type Detector =
  | "c-value-unlabelled"
  | "c-formula-unlabelled"
  | "convention-silent-value"
  | "unqualified-pairing"
  | "gram-inverse-unqualified"
  | "gram-inverse-under-d";

// ---------------------------------------------------------------------------
// Exact decimal handling — BigInt digit strings, never a float.
// ---------------------------------------------------------------------------

/** value = (neg ? -1 : 1) · 0.<digits> · 10^exp, with digits[0] ≠ "0". */
interface Dec {
  neg: boolean;
  digits: string;
  exp: number;
}

/** Parse a plain decimal literal ("-0.0227449", "137.0359351"). Null if zero. */
export function parseDec(lit: string): Dec | null {
  const m = lit.match(/^([+-]?)(\d*)\.(\d+)$/);
  if (!m) return null;
  const neg = m[1] === "-";
  const all = (m[2] || "") + m[3];
  const intLen = (m[2] || "").length;
  const firstNZ = all.search(/[1-9]/);
  if (firstNZ < 0) return null; // the literal is zero — carries no fingerprint
  return { neg, digits: all.slice(firstNZ), exp: intLen - firstNZ };
}

/** Round a Dec to `n` significant digits, half-up. */
export function roundSig(d: Dec, n: number): Dec {
  if (d.digits.length <= n) {
    return { neg: d.neg, digits: d.digits.padEnd(n, "0"), exp: d.exp };
  }
  const head = d.digits.slice(0, n);
  const roundUp = d.digits.charCodeAt(n) >= 53; // '5'
  if (!roundUp) return { neg: d.neg, digits: head, exp: d.exp };
  const bumped = (BigInt(head) + 1n).toString();
  // 999… → 1000…: one more digit, so the exponent grows and we re-truncate.
  if (bumped.length > n) return { neg: d.neg, digits: bumped.slice(0, n), exp: d.exp + 1 };
  return { neg: d.neg, digits: bumped.padStart(n, "0"), exp: d.exp };
}

/**
 * Does the literal `lit` quote the registry value `val`?
 *
 * True iff rounding `val` to the literal's OWN number of significant digits
 * reproduces the literal exactly. Trailing zeros in the literal are
 * significant ("0.61268803714646525160" is 20 digits, and the registry's
 * 50-dps string does round to it).
 */
export function quotes(lit: Dec, val: Dec): boolean {
  if (lit.neg !== val.neg) return false;
  const r = roundSig(val, lit.digits.length);
  return r.exp === lit.exp && r.digits === lit.digits;
}

// ---------------------------------------------------------------------------
// Registry → fingerprint table
// ---------------------------------------------------------------------------

interface Fingerprint {
  convention: "C" | "D";
  /** human name of the quantity, for the evidence line */
  what: string;
  raw: string;
  dec: Dec;
}

/**
 * Convention-C numbers the JSON twin does not carry as fields.
 *
 * The Markov–Gram determinant lives in the registry MARKDOWN only
 * (§"Symbol collisions" — `det = -0.18920521914403668` under C, `0` exactly
 * under D). It is the single most consequential C fingerprint in the corpus
 * (`prop:frobenius-gram-matrix`, `sec:fine-structure-data`,
 * `confinement-nucleon-unit`), so the axis carries it explicitly rather than
 * waiting for a JSON field. If the JSON twin grows a
 * `symbol_collisions[].value_under_C`, delete this and read it from there.
 */
const EXTRA_C_FINGERPRINTS: { what: string; raw: string }[] = [
  { what: "det of the Markov–Gram under C", raw: "-0.18920521914403668" },
];

export function buildFingerprints(registry: any): Fingerprint[] {
  const out: Fingerprint[] = [];
  const push = (convention: "C" | "D", what: string, raw: unknown) => {
    if (typeof raw !== "string") return;
    const dec = parseDec(raw.trim());
    if (!dec) return; // notably y_(1^3) = "0" under D: zero carries no fingerprint
    out.push({ convention, what, raw: raw.trim(), dec });
  };
  for (const c of registry.conventions ?? []) {
    if (c.id !== "C" && c.id !== "D") continue;
    const id = c.id as "C" | "D";
    push(id, `z(q_0) under ${id}`, c.z_at_q0);
    push(id, `tr_M(beta_Bor) under ${id}`, c.value_at_beta_bor);
    for (const [lam, v] of Object.entries(c.weights_at_q0 ?? {})) {
      push(id, `y_${lam} under ${id}`, v);
    }
  }
  for (const e of EXTRA_C_FINGERPRINTS) push("C", e.what, e.raw);
  return out;
}

// ---------------------------------------------------------------------------
// Text scanning
// ---------------------------------------------------------------------------

/**
 * LaTeX digit-group separators (`\,` `\;` `\!` `~`) between digits are removed
 * so `0.612\,688\,037` is seen as one literal. Offsets shift by a few
 * characters; the ±400 window absorbs that.
 */
export function normalise(text: string): string {
  return text.replace(/(\d)(?:\\[,;!:]|~|\\ )(?=\d)/g, "$1");
}

const NUM_RE = /(?<![\w.])(-?\d*\.\d+)(?![\d])/g;

/**
 * In-scope: the block touches the Markov-trace surface at all.
 *
 * `Markov parameter` / `Markov weight` are here deliberately. Without them a
 * block whose only trace vocabulary is "the Markov parameter $z$" fell out of
 * scope entirely and no detector could fire on it — which is exactly the shape
 * of the blocks `c-formula-unlabelled` exists to catch. The gap was found by a
 * selftest fixture that silently passed for the wrong reason.
 */
const TRACE_SURFACE =
  /\btr\}?_M\b|\btr_M\b|\\mathrm\{tr\}_\{?M|Markov[\s–—-]*trace|Markov[\s–—-]*Gram|Markov[\s–—-]*parameter|Markov[\s–—-]*weight|Frobenius\s+Gram|Gram\s+matrix|Ocneanu|y_\{?\\?lambda|y_\{\(|\bWenzl\b|convention[\s-]*[CD]\b|trace[\s-]convention/i;

/**
 * A convention id attached to a trace symbol: `z_{\mathrm{C}}`, `y^C_{(2,1)}`,
 * `\mathrm{tr}^{D}_M`, `z_D`. Deliberately anchored to the trace symbols
 * (`z`, `y`, `\tau`, `tr`) rather than accepting a bare `_C` anywhere — an
 * unanchored letter subscript is far too common to read as a convention label.
 */
function conventionSubscript(letter: "C" | "D" | "CD"): string {
  const cls = letter === "CD" ? "[CD]" : letter;
  return (
    String.raw`(?:z|y|\\tau|tr|\\mathrm\{tr\})\s*[_^]\s*` +
    String.raw`(?:\{\\mathrm\{${cls}\}\}|\{\\text\{${cls}\}\}|\{\\rm\s*${cls}\}|\{${cls}\}|${cls}(?![A-Za-z0-9]))`
  );
}

/** Any explicit naming of a registry convention id (block-wide check). */
const CONVENTION_NAMED = new RegExp(
  [
    String.raw`convention[\s-]*["'\`]?[CD]\b`,
    String.raw`convention[CD]\b`,
    String.raw`"convention-[cd]"`,
    String.raw`trace-convention-registry`,
    String.raw`conventionD`,
    String.raw`conventionC`,
    String.raw`\bconvention\s+id\b`,
    conventionSubscript("CD"),
  ].join("|"),
);

/**
 * A C value is labelled when the window says C, or says the value is retired.
 *
 * The subscript/superscript forms matter: the corpus writes the side-by-side
 * comparison as `$z_{\mathrm{C}} = 0.4993…$` / `$y^C_{(2,1)}$`, which IS a
 * convention label even though the words "convention C" never appear in the
 * sentence. Missing them turned the deliberate D-vs-C comparison in
 * `prop:convention-d-kills-antisymmetriser` into four false criticals.
 */
const C_LABEL = new RegExp(
  [
    String.raw`convention[\s-]*["'\`]?C\b`,
    String.raw`conventionC`,
    String.raw`convention-c\b`,
    String.raw`\bunder\s+C\b`,
    conventionSubscript("C"),
    // retirement language
    String.raw`\bexcised\b`,
    String.raw`\bwithdrawn\b`,
    String.raw`\bretracted\b`,
    String.raw`\bhistorical\b`,
    String.raw`_HISTORICAL\b`,
    String.raw`\bsuperseded\b`,
    String.raw`\bpre-excision\b`,
    String.raw`\bformer(?:ly)?\b`,
    String.raw`\bold(?:er)?\s+text\b`,
  ].join("|"),
  "i",
);

/** Markov–Gram context (NOT the 2×2 Chern–Simons pairing Gram). */
const MARKOV_GRAM =
  /Markov[\s–—-]*Gram|\\mathrm\{tr\}_M\(\s*b_i\s*b_j|tr_M\(b_i\s*b_j|Frobenius\s+Gram|Gram\s+matrix/i;

/** The Chern–Simons Gram — a different matrix, not convention-scoped. */
const CS_GRAM = /Chern[\s–—-]*Simons|G_\{?\\mathrm\{CS\}|G_\{?\\?mathrm\{cl\}|G\^\{?q\}?_\{?\\mathrm\{CS\}|_\{\\mathrm\{CS\}\}/i;

/** Signature language that the retraction says must name its pairing. */
const SIGNATURE_CLAIM =
  /\bindefinite\b|\bLorentzian\b|signature\s*\$?\\?\(?\s*[0-9]\s*,\s*[0-9]\s*\)?/i;

/** Naming the pairing clears the signature claim. */
const PAIRING_NAMED =
  /\bbilinear\b|\bstar[\s-]*pairing\b|\bstar\s+form\b|b_j\^\{?\\?\*|\\ast|\*-pairing|\bHecke\s+star\b|\bsesquilinear\b|b_ib_j\^|b_i\s*b_j\^/i;

/**
 * The block already acknowledges the degeneracy — it names the radical, the
 * Temperley–Lieb quotient, the corank, or says outright that `det G = 0`. That
 * is the CORRECT end state of the excision for a Gram-inverse claim, so it
 * clears rather than fires. Without this, a block repaired by relocating its
 * claim to `H_n/rad` would keep failing forever and there would be no way to
 * finish the job.
 */
const RADICAL_CAVEAT =
  /\bradical\b|\bTemperley[\s–—-]*Lieb\b|\bTL_\{?[n0-9]|H_\{?[n0-9]\}?\s*\/\s*\\?mathrm\{?rad|\/\s*\\mathrm\{rad\}|\bcorank\b|\bsingular\b|\bdegenerate\b\s*(?:under|over)|\\det\s*G\s*=\s*0|\bquotient\b/i;

/** Claims that the Markov–Gram is invertible / non-degenerate. */
const GRAM_INVERSE =
  /G\^\{-1\}|G\^\{?-1\}?|\bnon-?degenerate\b|\binvertible\b|\bG_\{?\\mathrm\{inv|\bG_INV\b|\\det\s*G\s*(?:<|>|\\ne|\\neq|≠)\s*0/;

/**
 * **`z` defined by the convention-C formula.**
 *
 * The blind spot the value detectors cannot see. `c-value-unlabelled` fires on
 * decimal literals; a block that writes `z = 1/(q^{1/2} + q^{-1/2})` quotes no
 * number at all and sailed straight through. That symbolic form is the larger
 * surface — 26 content files carry it against 1 carrying an unlabelled C value.
 *
 * Matching is deliberately narrow: **only `z` bound to the reciprocal of
 * `q^{1/2} + q^{-1/2}`**, not the expression itself. `q^{1/2} + q^{-1/2}` is
 * `[2]_{√q}`, a perfectly good Temperley–Lieb loop parameter at half-argument —
 * it appears in the Wenzl positivity condition `q^{1/2} + q^{-1/2} > 2` and in
 * pair-skein formulas that have nothing to do with the Markov parameter. 58
 * files contain the expression; flagging those would be the same loose-grep
 * mistake that produced a "70 producers" figure when the truth was 13.
 * `bar-involution-c5-algebraic-identities` states the distinction outright: the
 * half-argument loop parameter "is not a Markov parameter of the Hecke
 * generator".
 */
const C_FORMULA = new RegExp(
  [
    // z := 1/(q^{1/2} + q^{-1/2})   and \frac{1}{...} spellings
    String.raw`z\s*(?::=|=|\\coloneqq)\s*1\s*/\s*\(?\s*q\^\{?1/2\}?\s*\+\s*q\^\{?-1/2\}?`,
    String.raw`z\s*(?::=|=|\\coloneqq)\s*\\d?frac\{1\}\{\s*q\^\{?1/2\}?\s*\+\s*q\^\{?-1/2\}?`,
    // \sqrt{q} spellings
    String.raw`z\s*(?::=|=|\\coloneqq)\s*1\s*/\s*\(?\s*\\sqrt\{q\}\s*\+\s*1\s*/\s*\\sqrt\{q\}`,
    String.raw`z\s*(?::=|=|\\coloneqq)\s*\\d?frac\{1\}\{\s*\\sqrt\{q\}\s*\+`,
    // python/ts producer spellings, so the axis also catches a `.ts` block
    String.raw`z\s*=\s*1\s*/\s*\(\s*q\s*\*\*\s*0\.5\s*\+`,
    String.raw`z\s*=\s*1\s*/\s*\(\s*q_half\s*\+\s*q_half_inv`,
  ].join("|"),
  "i",
);

interface Hit {
  detector: Detector;
  severity: Severity;
  file: string; // "md" | "ts"
  line: number;
  evidence: string;
}

function lineOf(text: string, idx: number): number {
  let n = 1;
  for (let i = 0; i < idx && i < text.length; i++) if (text.charCodeAt(i) === 10) n++;
  return n;
}

function windowAround(text: string, idx: number, len = 0): string {
  return text.slice(Math.max(0, idx - WINDOW), Math.min(text.length, idx + len + WINDOW));
}

function snippet(text: string, idx: number, len: number): string {
  const s = text
    .slice(Math.max(0, idx - 60), Math.min(text.length, idx + len + 60))
    .replace(/\s+/g, " ")
    .trim();
  return s.length > 200 ? s.slice(0, 197) + "…" : s;
}

/**
 * The whole axis, on one block's two source texts.
 *
 * Exported so `--selftest` drives exactly the production code path — a
 * self-test that exercises a parallel copy of the logic proves nothing.
 */
export function scanBlock(
  mdRaw: string,
  tsRaw: string,
  fps: Fingerprint[],
): { inScope: boolean; hits: Hit[] } {
  const md = normalise(mdRaw);
  const ts = normalise(tsRaw);
  const both = md + "\n" + ts;
  const inScope = TRACE_SURFACE.test(both);
  if (!inScope) return { inScope, hits: [] };

  const conventionNamedSomewhere = CONVENTION_NAMED.test(both);
  const hits: Hit[] = [];

  for (const [tag, text] of [
    ["md", md],
    ["ts", ts],
  ] as const) {
    if (!text) continue;

    // ── numeric detectors ──────────────────────────────────────────────
    NUM_RE.lastIndex = 0;
    let m: RegExpExecArray | null;
    while ((m = NUM_RE.exec(text))) {
      const lit = parseDec(m[1]);
      if (!lit || lit.digits.length < MIN_SIG_DIGITS) continue;
      const matched = fps.filter((f) => quotes(lit, f.dec));
      if (!matched.length) continue;
      // A literal can match both conventions only if they agree there; they
      // never do, so `matched` is single-convention in practice. Prefer C:
      // an unlabelled C value is the critical case.
      const c = matched.find((f) => f.convention === "C");
      const win = windowAround(text, m.index, m[1].length);
      if (c) {
        if (!C_LABEL.test(win)) {
          hits.push({
            detector: "c-value-unlabelled",
            severity: "critical",
            file: tag,
            line: lineOf(text, m.index),
            evidence:
              `${m[1]} is ${c.what} (registry ${c.raw}) with no convention-C / ` +
              `excision marker within ${WINDOW} chars: “${snippet(text, m.index, m[1].length)}”`,
          });
          continue;
        }
      }
      if (!conventionNamedSomewhere) {
        const f = matched[0];
        hits.push({
          detector: "convention-silent-value",
          severity: "major",
          file: tag,
          line: lineOf(text, m.index),
          evidence:
            `${m[1]} is ${f.what} (registry ${f.raw}) and the block names no ` +
            `convention id anywhere: “${snippet(text, m.index, m[1].length)}”`,
        });
      }
    }

    // ── symbolic convention-C definition of `z` ────────────────────────
    // Runs per-occurrence rather than once per block: a block may state the C
    // formula in a labelled historical note AND again as a working definition,
    // and only the second is a defect.
    const cf = new RegExp(C_FORMULA.source, "gi");
    let cfm: RegExpExecArray | null;
    while ((cfm = cf.exec(text))) {
      const win = windowAround(text, cfm.index, cfm[0].length);
      if (C_LABEL.test(win)) continue;
      hits.push({
        detector: "c-formula-unlabelled",
        severity: "critical",
        file: tag,
        line: lineOf(text, cfm.index),
        evidence:
          `z is defined by the convention-C formula 1/(q^{1/2}+q^{-1/2}) with no ` +
          `convention-C / excision marker within ${WINDOW} chars. Production is ` +
          `convention D, z = q^3/(q^2+1) = 0.61268803714646525160; the C value is ` +
          `0.49932033418369445241, 22.7% lower. Context: ` +
          `“${snippet(text, cfm.index, cfm[0].length)}”`,
      });
    }

    // ── signature / pairing detector ───────────────────────────────────
    const sig = new RegExp(SIGNATURE_CLAIM.source, "gi");
    let s: RegExpExecArray | null;
    while ((s = sig.exec(text))) {
      const win = windowAround(text, s.index, s[0].length);
      if (!MARKOV_GRAM.test(win)) continue;
      if (CS_GRAM.test(win)) continue;
      if (PAIRING_NAMED.test(win)) continue;
      hits.push({
        detector: "unqualified-pairing",
        severity: "major",
        file: tag,
        line: lineOf(text, s.index),
        evidence:
          `“${s[0]}” said of the Markov–Gram without naming the pairing. The ` +
          `Lorentzian/indefinite reading was retracted (748ba9b1): it is a ` +
          `property of the BILINEAR pairing tr_M(b_i b_j); on the star pairing ` +
          `tr_M(b_i b_j*) the form is positive — (6,0,0) under C, (5,0,1) under D. ` +
          `Context: “${snippet(text, s.index, s[0].length)}”`,
      });
    }

    // ── Gram invertibility detector ────────────────────────────────────
    const gi = new RegExp(GRAM_INVERSE.source, "g");
    let g: RegExpExecArray | null;
    while ((g = gi.exec(text))) {
      const win = windowAround(text, g.index, g[0].length);
      if (!MARKOV_GRAM.test(win)) continue;
      if (CS_GRAM.test(win)) continue;
      // The block already says the form is degenerate / has been moved to the
      // quotient. That is the correct end state, not a defect.
      if (RADICAL_CAVEAT.test(win)) continue;
      // Labelled as convention-C arithmetic: historical, and true under C.
      if (C_LABEL.test(win)) continue;
      if (CONVENTION_NAMED.test(win)) {
        // A convention IS named here and it is not C, so it is D — and under D
        // the claim is FALSE, not merely unqualified. This case used to `continue`,
        // which meant relabelling a wrong claim "convention D" silenced the
        // detector instead of sharpening it. Naming the convention you are wrong
        // under is worse than naming none.
        hits.push({
          detector: "gram-inverse-under-d",
          severity: "critical",
          file: tag,
          line: lineOf(text, g.index),
          evidence:
            `“${g[0]}” asserted of the Markov–Gram with convention D named nearby ` +
            `and no radical/quotient caveat. Under D this is false, not ambiguous: ` +
            `y_(1^3) = 0 exactly, the (1^3) block IS the radical, det G = 0 and ` +
            `G^{-1} does not exist. Move the claim to H_n/rad = TL_n, where the ` +
            `induced pairing IS non-degenerate (QOU/QBeta/MarkovGramDegenerate.lean: ` +
            `gram_det_eq_zero_of_radical_combination, pairing_descends). Context: ` +
            `“${snippet(text, g.index, g[0].length)}”`,
        });
        continue;
      }
      hits.push({
        detector: "gram-inverse-unqualified",
        severity: "major",
        file: tag,
        line: lineOf(text, g.index),
        evidence:
          `“${g[0]}” asserted of the Markov–Gram with no convention named within ` +
          `${WINDOW} chars. det G = 0 exactly under the production convention D ` +
          `(the (1^3) block is the radical) and G^{-1} does not exist; the ` +
          `invertible reading is convention-C arithmetic. Context: ` +
          `“${snippet(text, g.index, g[0].length)}”`,
      });
    }
  }
  return { inScope, hits };
}

// ---------------------------------------------------------------------------
// Block discovery
// ---------------------------------------------------------------------------

const BUILDER_RE =
  /\b(definition|theorem|lemma|proposition|corollary|conjecture|example|remark|proof|prose|equation|diagram|simulator|section|chapter)\s*\(\s*\{/;

interface Block {
  root: string;
  dir: string;
  kind: string;
  label: string;
  mdPath: string;
  tsPath: string;
  md: string;
  ts: string;
}

function parseStringField(ts: string, field: string): string {
  const dq = ts.match(new RegExp(`${field}\\s*:\\s*"((?:[^"\\\\]|\\\\.)*)"`));
  if (dq) return dq[1].replace(/\\(["'\`\\])/g, "$1");
  const sq = ts.match(new RegExp(`${field}\\s*:\\s*'((?:[^'\\\\]|\\\\.)*)'`));
  if (sq) return sq[1].replace(/\\(["'\`\\])/g, "$1");
  const bt = ts.match(new RegExp(`${field}\\s*:\\s*\`([^\`]*)\``));
  if (bt) return bt[1];
  return "";
}

function loadBlock(tsPath: string, repoRoot: string): Block | null {
  if (!existsSync(tsPath)) return null;
  const ts = readFileSync(tsPath, "utf8");
  const km = ts.match(BUILDER_RE);
  if (!km) return null;
  const dir = dirname(tsPath);
  const root = basename(tsPath, ".ts");
  const mdPath = join(dir, `${root}.md`);
  const md = existsSync(mdPath) ? readFileSync(mdPath, "utf8") : "";
  return {
    root,
    dir,
    kind: km[1],
    label: parseStringField(ts, "label"),
    mdPath: relative(repoRoot, mdPath),
    tsPath: relative(repoRoot, tsPath),
    md,
    ts,
  };
}

function* walk(dir: string): Generator<string> {
  let entries: string[];
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const e of entries) {
    if (e === "node_modules" || e === ".git" || e === ".lake") continue;
    if (e === "__pycache__") continue;
    // `content/pipeline/` is tooling, not authored blocks. Skipping it is not
    // cosmetic: this axis carries convention-C fingerprints in its own
    // `--selftest` fixtures, so walking itself makes every sweep fail forever
    // and destroys the exit-1 gate. The axis is tested by `--selftest`, not by
    // being swept as content.
    if (e === "pipeline") continue;
    const full = join(dir, e);
    let st;
    try {
      st = statSync(full);
    } catch {
      continue;
    }
    if (st.isDirectory()) yield* walk(full);
    else if (e.endsWith(".ts") && !e.endsWith(".d.ts")) yield full;
  }
}

/** A path may be a directory, a `.md`, a `.ts`, or a bare block base. */
function expandTargets(p: string): string[] {
  const abs = resolve(p);
  if (existsSync(abs) && statSync(abs).isDirectory()) return [...walk(abs)];
  if (abs.endsWith(".ts")) return [abs];
  if (abs.endsWith(".md")) return [abs.slice(0, -3) + ".ts"];
  if (abs.endsWith(".qa.json")) return [abs.slice(0, -8) + ".ts"];
  return [abs + ".ts"];
}

// ---------------------------------------------------------------------------
// Sidecar upsert — mirrors definition-clarity-audit.ts / lean-vacuity-axiom-audit.ts
// ---------------------------------------------------------------------------

const sha12 = (s: string) => createHash("sha256").update(s).digest("hex").slice(0, 12);

function writeSidecar(
  b: Block,
  result: Result,
  severity: Severity | undefined,
  evidence: string,
  metrics: Record<string, number>,
  prov: { scriptHash: string; scriptSha: string; reviewedSha: string; depsHash: string },
) {
  const qaPath = join(b.dir, `${b.root}.qa.json`);
  let doc: any = {};
  if (existsSync(qaPath)) {
    try {
      doc = JSON.parse(readFileSync(qaPath, "utf8"));
    } catch {
      doc = {};
    }
  }
  doc.$schema ??= "block-qa/v1";
  doc.label ??= b.label;
  doc.kind ??= b.kind;
  doc.paths ??= { ts: b.tsPath, ...(b.md ? { md: b.mdPath } : {}) };
  doc.criteria ??= {};
  const now = new Date().toISOString();
  const entry: any = {
    field_hash: { md: sha12(b.md), ts: sha12(b.ts) },
    result,
    reviewer: {
      kind: "script",
      id: "folio/pipeline/trace-convention-audit.ts",
      version: "v1",
      script_hash: prov.scriptHash,
      script_commit_sha: prov.scriptSha,
      deps_hash: prov.depsHash,
    },
    reviewed_at: now,
    reviewed_sha: prov.reviewedSha,
    metrics,
  };
  if (severity) entry.severity = severity;
  if (evidence) entry.evidence = evidence;
  doc.criteria[CRITERION] = [entry];
  doc.updated_at = now;
  writeFileSync(qaPath, JSON.stringify(doc, null, 2) + "\n");
  return relative(process.cwd(), qaPath);
}

// ---------------------------------------------------------------------------
// Self-test — the axis must be able to fail AND to clear.
// ---------------------------------------------------------------------------

interface Case {
  name: string;
  md: string;
  ts: string;
  expect: Detector | "clean";
  /**
   * Whether the fixture is expected to be IN SCOPE. Defaults to true, and it is
   * checked — without this a `"clean"` case passes whenever the axis decides the
   * block has no trace surface, which is passing for the wrong reason. Three
   * `c-formula-unlabelled` fixtures did exactly that: they "cleared" only
   * because `TRACE_SURFACE` did not yet know the phrase "Markov parameter".
   * A clears-test that clears vacuously is the failure mode this whole selftest
   * exists to prevent, so it is asserted rather than assumed.
   */
  scope?: boolean;
}

const SELFTEST_TS = `proposition({ label: "prop:selftest", title: "t" })`;

function selftest(fps: Fingerprint[]): number {
  // The convention-C weight y_(3), quoted the way the corpus quotes it.
  const C_VALUE = "0.4153958";
  const D_VALUE = "0.5054042";
  const cases: Case[] = [
    {
      name: "C value, no label → fires",
      md: `The three-strand Markov trace weights are $(y_{(3)}, y_{(2,1)}) = (${C_VALUE}, 0.2809296)$ at $q_0$.`,
      ts: SELFTEST_TS,
      expect: "c-value-unlabelled",
    },
    {
      name: "same block, C value removed → clears",
      md: `The three-strand Markov trace weights are $(y_{(3)}, y_{(2,1)}) = ([4]_q/[2]_q^3, 1/[2]_q^2)$ at $q_0$ under convention D.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "C value WITH the excision label → clears",
      md: `Under convention D the Markov trace weight is $y_{(3)} = ${D_VALUE}$; under the excised convention C it was $${C_VALUE}$.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "C value labelled only by a $z_{\\mathrm{C}}$ subscript → clears",
      md: `At $q_0$ the Markov trace gives $z_{\\mathrm{D}} = 0.61268803714646525160$ against $z_{\\mathrm{C}} = 0.49932033418369445241$.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "D value, convention never named → fires",
      md: `The Markov trace weight is $y_{(3)} = ${D_VALUE}$ at $q_0$.`,
      ts: SELFTEST_TS,
      expect: "convention-silent-value",
    },
    {
      name: "z DEFINED by the C formula, no value quoted → fires",
      md: `Write $h = q - q^{-1}$ and $z = 1/(q^{1/2} + q^{-1/2})$ for the Markov parameter.`,
      ts: SELFTEST_TS,
      expect: "c-formula-unlabelled",
    },
    {
      name: "the same C formula in a labelled historical note → clears",
      md: `Earlier versions of this theorem wrote $z = 1/(q^{1/2}+q^{-1/2})$, the excised convention C; production is convention D.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "z defined the D way → clears",
      md: `Write $h = q - q^{-1}$ and $z = q^3/(q^2+1)$ for the Markov parameter (convention D).`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "the half-argument loop parameter is NOT the Markov parameter → clears",
      md: `Let $q > 0$ satisfy the Wenzl positivity condition $q^{1/2} + q^{-1/2} > 2$; the Markov trace $\\mathrm{tr}_M$ is then positive.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "Lorentzian said of the Markov–Gram, pairing unnamed → fires",
      md: `The Markov–Gram matrix $G_{ij}$ carries an indefinite, Lorentzian signature.`,
      ts: SELFTEST_TS,
      expect: "unqualified-pairing",
    },
    {
      name: "same claim with the bilinear pairing named → clears",
      md: `On the bilinear pairing $\\mathrm{tr}_M(b_i b_j)$ the Markov–Gram matrix is indefinite; on the star pairing it is positive.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "G^{-1} asserted of the Markov–Gram, convention unnamed → fires",
      md: `Because the Frobenius Gram matrix is non-degenerate, $G^{-1}$ exists and Term 4 is $\\mathrm{tr}(G^{-1} D)$.`,
      ts: SELFTEST_TS,
      expect: "gram-inverse-unqualified",
    },
    {
      name: "G^{-1} claim RELABELLED 'convention D' → fires HARDER, not clears",
      md: `Write $z = q^3/(q^2+1)$ (**convention D**). The Markov–Gram matrix $G_{ij} = \\mathrm{tr}_M(b_i b_j)$ is non-degenerate, and $G^{-1}$ gives the dual construction.`,
      ts: SELFTEST_TS,
      expect: "gram-inverse-under-d",
    },
    {
      name: "…and moving the claim to the TL quotient clears it",
      md: `Write $z = q^3/(q^2+1)$ (**convention D**). On $H_3$ the Markov–Gram is singular — the $(1^3)$ block is the radical and $\\det G = 0$ — so $G^{-1}$ is read on the quotient $H_3/\\mathrm{rad} \\cong \\mathrm{TL}_3$, where the induced pairing is non-degenerate.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "a G^{-1} claim explicitly labelled convention C stays historical → clears",
      md: `Under the excised **convention C** the Markov–Gram matrix $G_{ij}$ was non-degenerate and $G^{-1}$ existed.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "the Chern–Simons Gram is a different matrix → clears",
      md: `The Chern–Simons pairing Gram matrix $G_{\\mathrm{CS}}$ is non-degenerate and $G^{-1}$ exists; no Markov parameter enters it. The Markov trace is untouched.`,
      ts: SELFTEST_TS,
      expect: "clean",
    },
    {
      name: "a block with no trace surface at all → out of scope",
      md: `The nuclear radius scales as $r_0 A^{1/3}$, an empirical saturation law.`,
      ts: SELFTEST_TS,
      expect: "clean",
      scope: false,
    },
  ];

  let failed = 0;
  for (const c of cases) {
    const { inScope, hits } = scanBlock(c.md, c.ts, fps);
    const got = hits.map((h) => h.detector);
    const wantScope = c.scope ?? true;
    const scopeOk = inScope === wantScope;
    const ok =
      scopeOk &&
      (c.expect === "clean" ? got.length === 0 : got.includes(c.expect as Detector));
    console.log(
      `  ${ok ? "ok  " : "FAIL"}  ${c.name}` +
        (ok
          ? ""
          : !scopeOk
            ? `\n          expected inScope=${wantScope}, got ${inScope}` +
              ` — a "clean" verdict here would be vacuous`
            : `\n          expected ${c.expect}, got [${got.join(", ") || "none"}]`),
    );
    if (!ok) failed++;
  }
  console.log(
    failed === 0
      ? `selftest: ${cases.length}/${cases.length} — the axis fires on a reintroduced convention-C value and clears when it is removed.`
      : `selftest: ${failed} of ${cases.length} case(s) FAILED.`,
  );
  return failed;
}

// ---------------------------------------------------------------------------
// Report
// ---------------------------------------------------------------------------

interface Finding {
  label: string;
  kind: string;
  block: string;
  mdPath: string;
  qaPath: string;
  result: Result;
  severity?: Severity;
  hits: Hit[];
}

function blob(branch: string, path: string): string {
  return `https://github.com/litlfred/qou/blob/${branch}/${path}`;
}

function buildMd(findings: Finding[], branch: string): string {
  const fails = findings.filter((f) => f.result === "fail");
  const L: string[] = [];
  L.push(`# \`trace-convention\` axis — ${new Date().toISOString().slice(0, 10)}`);
  L.push("");
  L.push(
    `Scanner: [\`folio/pipeline/trace-convention-audit.ts\`](${blob(branch, "folio/pipeline/trace-convention-audit.ts")}). ` +
      `Rule + fingerprints: [\`trace-convention-registry\`](${blob(branch, REGISTRY_MD)}).`,
  );
  L.push("");
  L.push(
    "> Any $\\tau$ / $\\mathrm{tr}_M$ value quoted below 0.1 % precision must name its " +
      "convention id. Convention-silent trace values are not comparable.",
  );
  L.push("");
  L.push("| Detector | fails |");
  L.push("|---|--:|");
  const dets: Detector[] = [
    "c-value-unlabelled",
    "c-formula-unlabelled",
    "convention-silent-value",
    "unqualified-pairing",
    "gram-inverse-unqualified",
    "gram-inverse-under-d",
  ];
  for (const d of dets) {
    L.push(`| \`${d}\` | ${fails.reduce((n, f) => n + f.hits.filter((h) => h.detector === d).length, 0)} |`);
  }
  L.push("");
  L.push(
    `Blocks in scope: **${findings.filter((f) => f.result !== "n/a").length}** ` +
      `of ${findings.length} scanned. Blocks failing: **${fails.length}**.`,
  );
  L.push("");
  for (const f of fails) {
    L.push(`## \`${f.label || f.block}\``);
    L.push("");
    L.push(`[\`${f.mdPath}\`](${blob(branch, f.mdPath)})`);
    L.push("");
    for (const h of f.hits) {
      L.push(`- **\`${h.detector}\`** (${h.severity}) — \`${f.block}.${h.file}\`:${h.line} — ${h.evidence}`);
    }
    L.push("");
  }
  return L.join("\n") + "\n";
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  const argv = process.argv.slice(2);
  const targets: string[] = [];
  let jsonOut = "";
  let mdOut = "";
  let writeSidecars = false;
  let quiet = false;
  let doSelftest = false;
  let branch = "";
  let blocksFrom = "";
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--json") jsonOut = argv[++i];
    else if (a === "--md") mdOut = argv[++i];
    else if (a === "--branch") branch = argv[++i];
    else if (a === "--blocks-from") blocksFrom = argv[++i];
    else if (a === "--write-sidecars") writeSidecars = true;
    else if (a === "--selftest") doSelftest = true;
    else if (a === "--quiet") quiet = true;
    else if (!a.startsWith("--")) targets.push(a);
  }

  const repoRoot = execFileSync("git", ["rev-parse", "--show-toplevel"]).toString().trim();
  const registryPath = join(repoRoot, REGISTRY_JSON);
  if (!existsSync(registryPath)) {
    console.error(`trace-convention-audit: registry not found at ${REGISTRY_JSON}`);
    process.exit(2);
  }
  const registryRaw = readFileSync(registryPath, "utf8");
  const fps = buildFingerprints(JSON.parse(registryRaw));
  if (!fps.some((f) => f.convention === "C") || !fps.some((f) => f.convention === "D")) {
    console.error(
      "trace-convention-audit: the registry yielded no C or no D fingerprints — " +
        "the axis would be vacuous. Refusing to run.",
    );
    process.exit(2);
  }

  if (doSelftest) {
    console.log(`trace-convention-audit --selftest (${fps.length} registry fingerprints)`);
    process.exit(selftest(fps) === 0 ? 0 : 1);
  }

  if (blocksFrom) {
    for (const line of readFileSync(blocksFrom, "utf8").split("\n")) {
      const t = line.trim();
      if (t) targets.push(t);
    }
  }
  if (!targets.length) targets.push(join(repoRoot, "folio"));

  const tsPaths = [...new Set(targets.flatMap(expandTargets))].sort();
  const findings: Finding[] = [];
  for (const p of tsPaths) {
    const b = loadBlock(p, repoRoot);
    if (!b) continue;
    const { inScope, hits } = scanBlock(b.md, b.ts, fps);
    const severity: Severity | undefined = hits.some((h) => h.severity === "critical")
      ? "critical"
      : hits.length
        ? "major"
        : undefined;
    findings.push({
      label: b.label,
      kind: b.kind,
      block: b.root,
      mdPath: b.md ? b.mdPath : b.tsPath,
      qaPath: relative(repoRoot, join(b.dir, `${b.root}.qa.json`)),
      result: !inScope ? "n/a" : hits.length ? "fail" : "pass",
      severity,
      hits,
    });
  }

  if (writeSidecars) {
    const selfRel = relative(repoRoot, resolve(__filename));
    const scriptHash = sha12(readFileSync(resolve(__filename), "utf8"));
    let scriptSha = "uncommitted";
    try {
      scriptSha =
        execFileSync("git", ["log", "-1", "--format=%H", "--", selfRel], { cwd: repoRoot })
          .toString()
          .trim() || "uncommitted";
    } catch {
      /* ignore */
    }
    let reviewedSha = "unknown";
    try {
      reviewedSha = execFileSync("git", ["rev-parse", "HEAD"], { cwd: repoRoot })
        .toString()
        .trim();
    } catch {
      /* ignore */
    }
    const depsHash = sha12(registryRaw);
    const prov = { scriptHash, scriptSha, reviewedSha, depsHash };
    let written = 0;
    for (const p of tsPaths) {
      const b = loadBlock(p, repoRoot);
      if (!b) continue;
      const f = findings.find((x) => x.block === b.root && x.qaPath.startsWith(relative(repoRoot, b.dir)));
      if (!f) continue;
      const metrics: Record<string, number> = {
        registry_fingerprints: fps.length,
        c_value_unlabelled: f.hits.filter((h) => h.detector === "c-value-unlabelled").length,
        c_formula_unlabelled: f.hits.filter((h) => h.detector === "c-formula-unlabelled").length,
        convention_silent_value: f.hits.filter((h) => h.detector === "convention-silent-value").length,
        unqualified_pairing: f.hits.filter((h) => h.detector === "unqualified-pairing").length,
        gram_inverse_unqualified: f.hits.filter((h) => h.detector === "gram-inverse-unqualified").length,
        gram_inverse_under_d: f.hits.filter((h) => h.detector === "gram-inverse-under-d").length,
      };
      const evidence =
        f.result === "n/a"
          ? "Block quotes no Markov-trace value and names no trace convention; the axis does not apply."
          : f.result === "pass"
            ? `In scope; every registry-matching value carries a convention id, and no unqualified signature or Gram-inverse claim. Checked against ${fps.length} registry fingerprints (${REGISTRY_JSON}).`
            : f.hits.map((h) => `[${h.detector} @ ${h.file}:${h.line}] ${h.evidence}`).join("  ");
      writeSidecar(b, f.result, f.severity, evidence, metrics, prov);
      written++;
    }
    if (!quiet) console.log(`  sidecars written: ${written}`);
  }

  if (!branch) {
    try {
      branch = execFileSync("git", ["rev-parse", "--abbrev-ref", "HEAD"], { cwd: repoRoot })
        .toString()
        .trim();
    } catch {
      branch = "main";
    }
  }
  if (jsonOut) {
    writeFileSync(
      resolve(jsonOut),
      JSON.stringify(
        {
          generated_at: new Date().toISOString(),
          criterion: CRITERION,
          registry: REGISTRY_JSON,
          registry_fingerprints: fps.map((f) => ({ convention: f.convention, what: f.what, value: f.raw })),
          scanned: findings.length,
          findings,
        },
        null,
        2,
      ) + "\n",
    );
  }
  if (mdOut) writeFileSync(resolve(mdOut), buildMd(findings, branch));

  const fails = findings.filter((f) => f.result === "fail");
  if (!quiet) {
    const inScope = findings.filter((f) => f.result !== "n/a").length;
    console.log(
      `trace-convention-audit: ${findings.length} block(s) scanned, ${inScope} in scope, ` +
        `${fails.length} failing (${fps.length} registry fingerprints)`,
    );
    for (const f of fails) {
      console.log(`  FAIL  ${f.label || f.block}  (${f.mdPath})`);
      for (const h of f.hits) console.log(`        ${h.detector} @ ${h.file}:${h.line}`);
    }
    if (jsonOut) console.log(`  json -> ${jsonOut}`);
    if (mdOut) console.log(`  md   -> ${mdOut}`);
  }
  process.exit(fails.length ? 1 : 0);
}

if (import.meta.main) main();
