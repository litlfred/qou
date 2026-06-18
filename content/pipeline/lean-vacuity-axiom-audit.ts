#!/usr/bin/env bun
/**
 * Lean vacuity + provable-axiom audit.
 *
 * A Lean declaration can be sorry-free, axiom-clean, and
 * statement-faithful and still prove **nothing** — it assumes its own
 * conclusion, concludes a tautology, rests on an impossible premise,
 * or hides behind the kernel evaluator. `proof-statement-integrity`
 * (signature-stability + axiom sweep) misses all of these because
 * vacuity is a *semantic* property of the proof term. This scanner is
 * the candidate-finder for the agent-checked
 * `lean-proof-vacuity-audit` skill, EXTENDED with a new category:
 * an `axiom` that is a **candidate to prove** (an internal axiom
 * carrying no bibliographic `-- Ref:` justification — it should either
 * be proved or cite an external source).
 *
 * It walks every `.lean` (library trees + content-block siblings),
 * strips comments/docstrings, applies cheap structural heuristics, and
 * EXEMPTS the patterns the skill marks legitimate:
 *  - **sibling-resolution / docstub shadows** — a `: True := trivial`
 *    sibling whose real formalisation exists elsewhere in the Lake
 *    tree (the block's `lean.ref` or a docstring pointer resolves to a
 *    library decl). A `: True` stub with NO resolvable real decl is a
 *    genuine placeholder and IS flagged.
 *  - **field compositions that derive** (`Iff.intro`, `.trans`,
 *    `linarith`, `obtain …`) — not bare projections.
 *
 * Heuristics are deliberately high-recall / agent-confirmed: a `fail`
 * here is a *candidate*, not a verdict. The agent (this skill or
 * `lean-proof-review`) opens the file, applies the legit-vs-anti
 * discriminator, and records the adjudicated `reviewer.kind="agent"`
 * sidecar entry. With `--write-sidecars` the script writes the
 * `reviewer.kind="script"` candidate entry so the gap is trackable.
 *
 *   bun run content/pipeline/lean-vacuity-axiom-audit.ts \
 *     [root ...]                 # default: content/
 *     [--json docs/audits/2026-06-17-lean-vacuity-axiom-audit.json]
 *     [--write-sidecars]         # upsert <block>.qa.json script entries
 *     [--only <category>]        # restrict to one category
 *     [--quiet]
 *
 * Categories (criterion ids):
 *   proof-no-trivial-true            — conclusion is `True` / a tautology
 *   proof-no-self-assuming-projection— body returns a conclusion-typed field verbatim
 *   proof-no-false-premise           — hypothesis is impossible (vacuously true)
 *
 * Fix-guidance for `proof-no-self-assuming-projection` (per the disposition
 * rubric, docs/audits/2026-06-18-self-assuming-disposition-rubric.md) — decide
 * per block, in order:
 *   1. RESTATE-TO-DERIVE — if a genuine upstream input exists from which the
 *      conclusion follows (e.g. an `↔` from its two directions), carry the
 *      *hypotheses* and derive (already exempted when the body uses Iff.intro
 *      etc.). Stays a proved `theorem`.
 *   2. QUEUED-FOR-LEAN — if the conclusion is a clearly-true target not yet
 *      formalised, strip the conclusion-field and use an honest
 *      `:= by sorry` + `-- Ref:` + `-- QUEUED-FOR-LEAN:` (→ derived status
 *      `has_sorry`, NOT a demotion). The scanner already accepts honest sorry.
 *   3. CONJECTURE — only if the truth is genuinely in doubt: demote
 *      `theorem → conjecture` (a claim-change → owner sign-off).
 *   proof-no-decide-masking          — closed by `native_decide` (adds Lean.ofReduceBool)
 *   proof-no-provable-axiom          — internal `axiom` with no `-- Ref:` (prove or cite)
 *
 * @module content/pipeline/lean-vacuity-axiom-audit
 */
import { createHash } from "node:crypto";
import {
  existsSync,
  readFileSync,
  readdirSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { join, relative, resolve } from "node:path";
import { execFileSync } from "node:child_process";

// `block-qa/v1` sidecar types, inlined. The canonical schema lives at
// `folio-assistant/schemas/block-qa.ts`, but `folio-assistant/` is
// gitignored on this branch (the QA pipeline migration), so this
// scanner carries its own copy to stay self-contained and committable.
interface QaFieldHash {
  md?: string;
  ts?: string;
  lean?: string;
}
interface QaReviewer {
  kind: "script" | "agent" | "human";
  id: string;
  version?: string;
  script_hash?: string;
  script_commit_sha?: string;
  deps_hash?: string;
  agent_model?: string;
  agent_date?: string;
  agent_skill?: string;
}
interface QaCriterionEntry {
  field_hash: QaFieldHash;
  result: "pass" | "fail" | "warn" | "n/a";
  severity?: "critical" | "major" | "minor";
  evidence?: string;
  reviewer: QaReviewer;
  reviewed_at: string;
  reviewed_sha: string;
  notes?: string;
}
interface BlockQaReport {
  $schema: "block-qa/v1";
  label: string;
  kind: string;
  paths: { ts: string; md?: string; lean?: string };
  source_hashes: QaFieldHash;
  criteria: Record<string, QaCriterionEntry[]>;
  updated_at: string;
}

// ── Paths / constants ───────────────────────────────────────────────
const REPO_ROOT = resolve(import.meta.dir, "..", "..");
const DEFAULT_ROOTS = ["content"];
const SKIP_DIRS = new Set([
  ".lake",
  "node_modules",
  "build",
  ".git",
  "_deprecated",
]);
const SCRIPT_REL = "content/pipeline/lean-vacuity-axiom-audit.ts";

// Lake package prefix → lakeRoot (inlined to stay free of the migrated
// `folio-assistant/schemas/lean-packages.ts`).
const LAKE_ROOTS: Record<string, string> = {
  qou: "content/quantum-observable-universe/lean",
  ugb: "content/unital-groebner-bases/lean",
  fred2005: "content/fred2005-formal-groups/lean",
};

type Category =
  | "proof-no-trivial-true"
  | "proof-no-self-assuming-projection"
  | "proof-no-false-premise"
  | "proof-no-decide-masking"
  | "proof-no-provable-axiom";

const ALL_CATEGORIES: Category[] = [
  "proof-no-trivial-true",
  "proof-no-self-assuming-projection",
  "proof-no-false-premise",
  "proof-no-decide-masking",
  "proof-no-provable-axiom",
];

const SEVERITY: Record<Category, "critical" | "major" | "minor"> = {
  "proof-no-trivial-true": "major",
  "proof-no-self-assuming-projection": "critical",
  "proof-no-false-premise": "major",
  "proof-no-decide-masking": "major",
  "proof-no-provable-axiom": "major",
};

interface Hit {
  line: number;
  category: Category;
  pattern: string;
  snippet: string;
  decl?: string;
  severity: "critical" | "major" | "minor";
  /** When true the hit is recorded but does NOT count as a defect. */
  exempt?: boolean;
  exempt_reason?: string;
}

// ── Lean source helpers ─────────────────────────────────────────────

/** Recursively collect every `.lean` under `root`. */
function collectLean(root: string, out: string[]): void {
  if (!existsSync(root)) return;
  for (const entry of readdirSync(root)) {
    if (entry.startsWith(".") && entry !== ".") continue;
    if (SKIP_DIRS.has(entry)) continue;
    const full = join(root, entry);
    let st;
    try {
      st = statSync(full);
    } catch {
      continue;
    }
    if (st.isDirectory()) collectLean(full, out);
    else if (entry.endsWith(".lean")) out.push(full);
  }
}

/**
 * Blank out Lean comments while preserving line structure and column
 * positions (so line numbers + original-line snippets stay aligned).
 * Handles nested `/- … -/` block comments (incl. `/-- … -/`
 * docstrings) and `--` line comments. Returns the comment-free code
 * lines; declaration detection + body analysis run on these so a
 * `decide` / `axiom` token inside a comment is never matched.
 */
function stripCommentLines(src: string): string[] {
  const lines = src.split("\n");
  const out: string[] = [];
  let depth = 0;
  let inString = false;
  for (const line of lines) {
    let res = "";
    let i = 0;
    while (i < line.length) {
      if (depth > 0) {
        if (line.startsWith("-/", i)) {
          depth--;
          res += "  ";
          i += 2;
        } else if (line.startsWith("/-", i)) {
          depth++;
          res += "  ";
          i += 2;
        } else {
          res += " ";
          i++;
        }
      } else if (inString) {
        // Inside a string literal: preserve content verbatim so a `--`
        // or `/-` inside the string is NOT mistaken for a comment.
        if (line.startsWith('\\"', i) || line.startsWith("\\\\", i)) {
          res += line.slice(i, i + 2);
          i += 2;
        } else if (line[i] === '"') {
          inString = false;
          res += '"';
          i++;
        } else {
          res += line[i];
          i++;
        }
      } else if (line.startsWith("/-", i)) {
        depth++;
        res += "  ";
        i += 2;
      } else if (line.startsWith("--", i)) {
        res += " ".repeat(line.length - i);
        break;
      } else if (line[i] === '"') {
        inString = true;
        res += '"';
        i++;
      } else {
        res += line[i];
        i++;
      }
    }
    out.push(res);
  }
  return out;
}

const PROVABLE_KINDS = /^(theorem|lemma|proposition|corollary|example)\b/;
const DECL_START =
  /^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|nonrec\s+|scoped\s+|partial\s+|unsafe\s+)*(theorem|lemma|proposition|corollary|example|def|abbrev|instance|axiom|structure|class)\s+([A-Za-z_][\w'.]*)/;

interface Decl {
  kind: string;
  name: string;
  startLine: number; // 1-indexed
  /** Comment-free text from the decl head through the next decl. */
  text: string;
  /** Signature: head through the top-level `:=` (or whole text). */
  sig: string;
  /** Body: after the top-level `:=` (empty for axiom/structure/class). */
  body: string;
  /** Original (comment-bearing) head line, for the witness snippet. */
  headLine: string;
}

/** Split a file into top-level declarations (comment-stripped code). */
function splitDecls(origLines: string[], codeLines: string[]): Decl[] {
  const starts: { i: number; kind: string; name: string }[] = [];
  for (let i = 0; i < codeLines.length; i++) {
    const m = codeLines[i].match(DECL_START);
    if (m && /^\s{0,2}\S/.test(codeLines[i])) {
      starts.push({ i, kind: m[1], name: m[2] });
    }
  }
  const decls: Decl[] = [];
  for (let s = 0; s < starts.length; s++) {
    const { i, kind, name } = starts[s];
    const end = s + 1 < starts.length ? starts[s + 1].i : codeLines.length;
    // The slice runs to the next decl start, which sweeps in any trailing
    // top-level structural lines (a `namespace`/`section` `end` closer,
    // `open`, `variable`, …) that belong to no declaration. Drop them so
    // they do not pollute the body of the last decl before a closer —
    // otherwise a `:= ctx.claim_field` projection body reads as
    // `ctx.claim_field … end QOU.Foo` and the self-assuming / trivial-true
    // body regexes miss it (recall gap, e.g. knot_factor_spectral_derivation:70).
    const declLines = codeLines.slice(i, end);
    while (declLines.length > 1) {
      const last = declLines[declLines.length - 1];
      if (
        /^\s*$/.test(last) ||
        /^\s*(end|namespace|section|open|variable|universe|attribute|set_option)\b/.test(
          last,
        )
      )
        declLines.pop();
      else break;
    }
    const text = declLines.join("\n");
    const asgn = text.indexOf(":=");
    const sig = asgn >= 0 ? text.slice(0, asgn) : text;
    const body = asgn >= 0 ? text.slice(asgn + 2) : "";
    decls.push({
      kind,
      name,
      startLine: i + 1,
      text,
      sig,
      body,
      headLine: origLines[i] ?? "",
    });
  }
  return decls;
}

// Stub-marker phrases (both the "-resolution" and "docstub" wordings,
// plus the standard docstub boilerplate). A file matching any of these
// is a sibling stub whose real formalisation may live elsewhere.
const STUB_MARKERS =
  /Sibling-resolution stub|Sibling docstub|\bdocstub\b|documentation only|compiled formalisation lives|for the import wiring/i;

/** Trim a snippet for the witness (single line, capped). */
function snip(s: string): string {
  return s.replace(/\s+/g, " ").trim().slice(0, 160);
}

/** Conclusion of a signature: the type after the last top-level `:`. */
function conclusionOf(sig: string): string {
  let depth = 0;
  let lastColon = -1;
  for (let i = 0; i < sig.length; i++) {
    const c = sig[i];
    if (c === "(" || c === "[" || c === "{" || c === "⦃") depth++;
    else if (c === ")" || c === "]" || c === "}" || c === "⦄") depth--;
    else if (
      c === ":" &&
      depth === 0 &&
      sig[i + 1] !== "=" &&
      sig[i - 1] !== ":"
    )
      lastColon = i;
  }
  return lastColon >= 0 ? sig.slice(lastColon + 1).trim() : "";
}

/**
 * Resolve the "real" formalisation a stub points at and confirm it
 * declares `declName`. Candidates, in order:
 *   1. the owning content-block `.ts` sibling's `lean.ref`,
 *   2. a `lean/…/X.lean` path mentioned in the file's docstring,
 *   3. a `QOU.A.B.decl` namespace path mentioned in the docstring.
 * Returns the repo-relative real path if found (and it is not the stub
 * itself), else undefined.
 */
function findRealDecl(
  leanAbs: string,
  rawSrc: string,
  declName: string,
): string | undefined {
  const candidates: string[] = [];
  // (1) sibling .ts lean.ref
  const tsSibling = leanAbs.replace(/\.lean$/, ".ts");
  if (existsSync(tsSibling)) {
    const ref = readFileSync(tsSibling, "utf-8").match(
      /ref:\s*["']([^"']+)["']/,
    )?.[1];
    const r = resolveRefLean(ref);
    if (r) candidates.push(r);
  }
  // (2) explicit lean/…/*.lean path in the docstring
  for (const m of rawSrc.matchAll(/\b(lean\/[A-Za-z0-9_/]+\.lean)\b/g)) {
    candidates.push(resolve(REPO_ROOT, "content/quantum-observable-universe", m[1]));
    candidates.push(resolve(REPO_ROOT, m[1]));
  }
  // (3) QOU.A.B namespace → lean/QOU/A/B.lean
  for (const m of rawSrc.matchAll(/\bQOU(?:\.[A-Z][\w]*)+/g)) {
    const parts = m[0].split(".");
    // drop a trailing lowercase decl segment if present
    const modParts = parts.filter((p, idx) => idx === 0 || /^[A-Z]/.test(p));
    const modPath = modParts.join("/");
    candidates.push(
      resolve(REPO_ROOT, "content/quantum-observable-universe/lean", `${modPath}.lean`),
    );
  }
  const declRe = new RegExp(
    `\\b(theorem|lemma|proposition|corollary|def|abbrev|instance|structure|class)\\s+(?:[\\w'.]*\\.)?${declName.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\b`,
  );
  for (const c of candidates) {
    if (!c || resolve(c) === resolve(leanAbs)) continue;
    if (!existsSync(c)) continue;
    try {
      if (declRe.test(readFileSync(c, "utf-8"))) return relative(REPO_ROOT, c);
    } catch {
      /* skip */
    }
  }
  return undefined;
}

// ── Category detectors ──────────────────────────────────────────────

const TRIVIAL_BODY = /^\s*(trivial|by\s+trivial|sorry|by\s+sorry|⟨⟩|by\s+exact\s+trivial)\s*$/;

function detectTrivialTrue(
  d: Decl,
  rawSrc: string,
  fileIsStub: boolean,
  leanAbs: string,
): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  const concl = conclusionOf(d.sig);
  const body = d.body.trim();
  let pattern: string | undefined;
  if (/^True\b/.test(concl) || concl === "True") pattern = "conclusion-True";
  else if (/^True(\s*[∧×]\s*True)+$/.test(concl)) pattern = "conclusion-True-conj";
  else {
    // reflexive tautology: `: X = X := rfl`
    const eq = concl.match(/^(.+?)=(.+)$/);
    if (eq && /^\s*(rfl|by\s+rfl|Eq\.refl)\b/.test(body)) {
      const lhs = eq[1].replace(/\s+/g, "");
      const rhs = eq[2].replace(/\s+/g, "");
      if (lhs && lhs === rhs)
        return mk(d, "proof-no-trivial-true", "reflexive-tautology", false);
    }
    return undefined;
  }
  // A `: True := trivial/sorry` is the canonical stub body. Classify
  // shadow (real decl exists elsewhere → exempt) vs placeholder (no
  // real decl → genuine gap, flag).
  const isStubBody = TRIVIAL_BODY.test(body);
  if (fileIsStub || isStubBody) {
    const real = findRealDecl(leanAbs, rawSrc, d.name);
    if (real) {
      const h = mk(d, "proof-no-trivial-true", pattern, true);
      h.exempt_reason = `shadow-stub (real formalisation: ${real})`;
      return h;
    }
    // genuine placeholder — no resolvable real decl
    return mk(d, "proof-no-trivial-true", "placeholder-true", false);
  }
  // `: True` with a non-trivial body is a genuinely vacuous proof.
  return mk(d, "proof-no-trivial-true", pattern, false);
}

const PROJECTION_BODY = /^([a-z][\w']*)\.([A-Za-z_][\w']*)\s*$/;
const TUPLE_PROJECTION =
  /^⟨\s*([a-z][\w']*)\.[A-Za-z_][\w']*\s*(?:,\s*\1\.[A-Za-z_][\w']*\s*)*⟩\s*$/;
const EXACT_PROJECTION = /^by\s+exact\s+([a-z][\w']*)\.([A-Za-z_][\w']*)\s*$/;
const CONCLUSION_FIELD =
  /^(exists_|claim_|is_|has_|selects_|are_|satisfies_|holds_|equals_)|(_holds|_eq|_iff|_property|_spec|_result)$|^(holds|property|spec|result|main|claim)$/;
const DERIVES =
  /\b(trans|Iff\.intro|linarith|nlinarith|obtain|rcases|calc|rw\b|simp\b|mpr|mp\b|constructor|refine|apply)\b/;

/**
 * The conclusion at the *type-ascription* colon — the FIRST top-level `:`
 * (binders are always bracketed, so the first depth-0 `:` separates them from
 * the conclusion). Unlike `conclusionOf` (last top-level `:`), this is robust
 * to a conclusion that itself contains a binder colon, e.g. `∃ n : ℕ, …` —
 * where last-colon would wrongly slice off everything before the `∃`'s colon.
 */
function conclusionTypeAscription(sig: string): string {
  let depth = 0;
  for (let i = 0; i < sig.length; i++) {
    const c = sig[i];
    if (c === "(" || c === "[" || c === "{" || c === "⦃") depth++;
    else if (c === ")" || c === "]" || c === "}" || c === "⦄") depth--;
    else if (c === ":" && depth === 0 && sig[i + 1] !== "=" && sig[i - 1] !== ":")
      return sig.slice(i + 1).trim();
  }
  return "";
}

/**
 * True when the conclusion's *top-level* connective is `↔`. Balanced
 * parenthesised groups are stripped first, so a `↔` nested inside a conjunct
 * (e.g. `… ∧ (a ↔ b)`) does NOT count — only an iff that is the whole
 * conclusion. A tuple-projection `⟨ctx.fwd, ctx.bwd⟩` of such a conclusion is
 * the *legitimate* `§3b-cond` pattern: it derives the iff from its two
 * direction fields (the anonymous `Iff.intro`), so the class carries the two
 * implications, not the conclusion. The `DERIVES` filter above misses the
 * anonymous constructor, hence this explicit exemption.
 */
function topLevelIff(concl: string): boolean {
  let s = concl;
  let prev = "";
  while (prev !== s) {
    prev = s;
    s = s.replace(/\([^()]*\)/g, "");
  }
  return s.includes("↔") && !s.includes("∧");
}

/** A two-field anonymous tuple `⟨a.x, b.y⟩` — the arity of `Iff.intro`. */
const TWO_FIELD_TUPLE =
  /^⟨\s*[a-z][\w']*\.[A-Za-z_][\w']*\s*,\s*[a-z][\w']*\.[A-Za-z_][\w']*\s*⟩$/;

function detectSelfAssuming(d: Decl): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  const body = d.body.trim();
  if (DERIVES.test(body)) return undefined;
  let field: string | undefined;
  let pat: string | undefined;
  let m = body.match(PROJECTION_BODY);
  if (m) {
    field = m[2];
    pat = "field-projection";
  } else if ((m = body.match(EXACT_PROJECTION))) {
    field = m[2];
    pat = "exact-field-projection";
  } else if (TUPLE_PROJECTION.test(body)) {
    pat = "tuple-projection";
    field = body.match(/\.([A-Za-z_][\w']*)/)?.[1];
  }
  if (!pat) return undefined;
  if (pat !== "tuple-projection" && field && !CONCLUSION_FIELD.test(field))
    return undefined;
  // Precision: exempt a two-field tuple-projection that derives a top-level
  // `↔` from its direction fields — the legitimate conditional-class pattern
  // (`q_bkm_criterion`, `ns_obstruction_tower`), not a self-assuming defect.
  if (
    pat === "tuple-projection" &&
    TWO_FIELD_TUPLE.test(body) &&
    topLevelIff(conclusionTypeAscription(d.sig))
  ) {
    const h = mk(d, "proof-no-self-assuming-projection", pat, true);
    h.exempt_reason = "legitimate iff-from-directions conditional-class";
    return h;
  }
  return mk(d, "proof-no-self-assuming-projection", pat, false);
}

function detectDecideMasking(d: Decl): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  // Only `native_decide` is flagged: it adds `Lean.ofReduceBool` to the
  // axiom set (an integrity concern). Plain `decide` on a small
  // decidable goal is idiomatic and not a defect.
  if (/\bnative_decide\b/.test(d.body)) {
    const h = mk(d, "proof-no-decide-masking", "native_decide", false);
    h.severity = "critical";
    return h;
  }
  return undefined;
}

function detectFalsePremise(d: Decl): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  const body = d.body;
  if (
    /\babsurd\b[\s\S]*?\bby\s+(norm_num|decide|simp|omega)\b/.test(body) ||
    /\bNat\.not_lt_zero\b/.test(body) ||
    /\(by\s+(norm_num|omega)\)\.elim\b/.test(body)
  ) {
    return mk(d, "proof-no-false-premise", "discharged-impossible-hyp", false);
  }
  return undefined;
}

function detectProvableAxiom(d: Decl, rawLines: string[]): Hit | undefined {
  if (d.kind !== "axiom") return undefined;
  // Justification window: the docstring + 8 lines above (raw, so the
  // `-- Ref:` / `[cite]` is visible) plus the decl text.
  const above = rawLines
    .slice(Math.max(0, d.startLine - 1 - 10), d.startLine - 1)
    .join("\n");
  const window = above + "\n" + rawLines[d.startLine - 1];
  const hasRef = /--\s*Ref:/i.test(window);
  const hasCitation =
    /\[[a-zA-Z0-9][\w:+-]*\d{0,4}[a-z]?\]/.test(window) ||
    /doi\.org|arxiv\.org|https?:\/\//i.test(window);
  if (hasRef || hasCitation) return undefined;
  const h = mk(d, "proof-no-provable-axiom", "uncited-axiom", false);
  h.decl = d.name;
  return h;
}

function mk(
  d: Decl,
  category: Category,
  pattern: string,
  exempt: boolean,
): Hit {
  return {
    line: d.startLine,
    category,
    pattern,
    snippet: snip(d.headLine),
    decl: d.name,
    severity: SEVERITY[category],
    ...(exempt ? { exempt: true, exempt_reason: "sibling-resolution-stub" } : {}),
  };
}

// ── File-level scan ─────────────────────────────────────────────────

function scanFile(absPath: string, onlyCat: Category | undefined): Hit[] {
  const src = readFileSync(absPath, "utf-8");
  const origLines = src.split("\n");
  const codeLines = stripCommentLines(src);
  const fileIsStub = STUB_MARKERS.test(src);
  const decls = splitDecls(origLines, codeLines);
  const hits: Hit[] = [];
  const push = (h: Hit | undefined) => {
    if (h && (!onlyCat || h.category === onlyCat)) hits.push(h);
  };
  for (const d of decls) {
    push(detectTrivialTrue(d, src, fileIsStub, absPath));
    push(detectSelfAssuming(d));
    push(detectDecideMasking(d));
    push(detectFalsePremise(d));
    push(detectProvableAxiom(d, origLines));
  }
  return hits;
}

// ── Sidecar wiring ──────────────────────────────────────────────────

function hashFile(p: string): string | undefined {
  if (!existsSync(p)) return undefined;
  return createHash("sha256").update(readFileSync(p)).digest("hex").slice(0, 12);
}
function gitHeadSha(): string {
  try {
    return execFileSync("git", ["rev-parse", "HEAD"], {
      stdio: ["ignore", "pipe", "ignore"],
    })
      .toString()
      .trim();
  } catch {
    return "unknown";
  }
}
function gitFileCommitSha(relPath: string): string {
  try {
    return (
      execFileSync(
        "git",
        ["-C", REPO_ROOT, "log", "-n", "1", "--format=%H", "--", relPath],
        { stdio: ["ignore", "pipe", "ignore"] },
      )
        .toString()
        .trim() || "unknown"
    );
  } catch {
    return "unknown";
  }
}

interface BlockPaths {
  label: string;
  kind: string;
  root: string;
  ts: string;
  md?: string;
  lean?: string;
  qa: string;
}

function readManifest(
  tsPath: string,
): { kind: string; label: string; ref?: string } | undefined {
  const src = readFileSync(tsPath, "utf-8");
  const kindMatch = src.match(
    /export\s+default\s+(definition|theorem|lemma|proposition|corollary|conjecture|example|remark|proof|prose|equation|diagram|simulator)\s*\(/,
  );
  if (!kindMatch) return undefined;
  const labelMatch = src.match(/\blabel\s*:\s*["']([^"']+)["']/);
  if (!labelMatch) return undefined;
  const refMatch = src.match(/ref:\s*["']([^"']+)["']/);
  return { kind: kindMatch[1], label: labelMatch[1], ref: refMatch?.[1] };
}

/** Resolve a `pkg:Module.Decl` lean.ref to an absolute `.lean` path. */
function resolveRefLean(ref: string | undefined): string | undefined {
  if (!ref) return undefined;
  const colon = ref.indexOf(":");
  if (colon < 0) return undefined;
  const pkg = ref.slice(0, colon);
  const decl = ref.slice(colon + 1);
  const lakeRoot = LAKE_ROOTS[pkg];
  if (!lakeRoot) return undefined;
  const modulePath = decl.replace(/\./g, "/");
  const direct = resolve(REPO_ROOT, lakeRoot, `${modulePath}.lean`);
  if (existsSync(direct)) return direct;
  // drop trailing decl segment: pkg:Module.Path.declName → Module/Path.lean
  const segs = decl.split(".");
  if (segs.length > 1) {
    const modOnly = segs.slice(0, -1).join("/");
    const p2 = resolve(REPO_ROOT, lakeRoot, `${modOnly}.lean`);
    if (existsSync(p2)) return p2;
  }
  return undefined;
}

function* walkBlocks(rootDir: string): Generator<BlockPaths> {
  if (!existsSync(rootDir)) return;
  for (const entry of readdirSync(rootDir)) {
    if (entry.startsWith(".") || SKIP_DIRS.has(entry) || entry === "lean")
      continue;
    const full = join(rootDir, entry);
    const st = statSync(full);
    if (st.isDirectory()) {
      yield* walkBlocks(full);
    } else if (entry.endsWith(".ts")) {
      const manifest = readManifest(full);
      if (!manifest) continue;
      const root = full.slice(0, -3);
      const md = root + ".md";
      const lean = root + ".lean";
      const leanResolved = existsSync(lean)
        ? lean
        : resolveRefLean(manifest.ref);
      yield {
        label: manifest.label,
        kind: manifest.kind,
        root,
        ts: full,
        md: existsSync(md) ? md : undefined,
        lean: leanResolved,
        qa: root + ".qa.json",
      };
    }
  }
}

function writeSidecars(
  flaggedByLean: Map<string, Hit[]>,
  scriptHash: string,
  scriptCommitSha: string,
  headSha: string,
  onlyCat: Category | undefined,
): number {
  const blockByLean = new Map<string, BlockPaths>();
  for (const root of DEFAULT_ROOTS)
    for (const b of walkBlocks(resolve(REPO_ROOT, root)))
      if (b.lean) blockByLean.set(resolve(b.lean), b);

  const now = new Date().toISOString();
  const cats = onlyCat ? [onlyCat] : ALL_CATEGORIES;
  let written = 0;

  for (const [leanAbs, hits] of flaggedByLean) {
    const block = blockByLean.get(resolve(leanAbs));
    if (!block) continue; // library file with no owning block — witness only
    const qaPath = block.qa;
    let report: BlockQaReport | undefined;
    if (existsSync(qaPath)) {
      try {
        const raw = JSON.parse(readFileSync(qaPath, "utf-8"));
        if (raw?.$schema === "block-qa/v1") report = raw;
      } catch {
        /* fresh */
      }
    }
    const fieldHash = {
      md: block.md ? hashFile(block.md) : undefined,
      ts: hashFile(block.ts),
      lean: block.lean ? hashFile(block.lean) : undefined,
    };
    if (!report) {
      report = {
        $schema: "block-qa/v1",
        label: block.label,
        kind: block.kind,
        paths: {
          ts: relative(REPO_ROOT, block.ts),
          md: block.md ? relative(REPO_ROOT, block.md) : undefined,
          lean: block.lean ? relative(REPO_ROOT, block.lean) : undefined,
        },
        source_hashes: fieldHash,
        criteria: {},
        updated_at: now,
      };
    }
    report.source_hashes = fieldHash;
    report.updated_at = now;

    for (const cat of cats) {
      const catHits = hits.filter((h) => h.category === cat && !h.exempt);
      const result: QaCriterionEntry["result"] =
        catHits.length > 0 ? "fail" : "pass";
      // Dedup: drop this script's prior entries for the criterion so a
      // re-run REPLACES rather than accumulates them (Gemini, PR #2428).
      if (report.criteria[cat])
        report.criteria[cat] = report.criteria[cat].filter(
          (e) => !(e.reviewer.kind === "script" && e.reviewer.id === SCRIPT_REL),
        );
      // On a full scan, record only real findings (fail). A `pass` is only
      // meaningful as systematic coverage, which a full scan over flagged-
      // only blocks does not give; write passes solely for a targeted
      // `--only` re-audit of a single criterion.
      if (result !== "fail" && !onlyCat) continue;
      const entry: QaCriterionEntry = {
        field_hash: { lean: fieldHash.lean },
        result,
        ...(result === "fail" ? { severity: SEVERITY[cat] } : {}),
        ...(result === "fail"
          ? {
              evidence: catHits
                .map(
                  (h) =>
                    `${relative(REPO_ROOT, leanAbs)}:${h.line} [${h.pattern}] ${h.snippet}`,
                )
                .join(" | "),
            }
          : {}),
        reviewer: {
          kind: "script",
          id: SCRIPT_REL,
          version: "v1",
          script_hash: scriptHash,
          script_commit_sha: scriptCommitSha,
        },
        reviewed_at: now,
        reviewed_sha: headSha,
        notes:
          result === "fail"
            ? "Candidate flagged by heuristic scan — requires agent confirmation per lean-proof-vacuity-audit."
            : undefined,
      };
      report.criteria[cat] = report.criteria[cat] ?? [];
      report.criteria[cat].push(entry);
    }
    writeFileSync(qaPath, JSON.stringify(report, null, 2) + "\n");
    written++;
  }
  return written;
}

// ── Main ────────────────────────────────────────────────────────────

function main() {
  const argv = process.argv.slice(2);
  const roots: string[] = [];
  let jsonOut = "docs/audits/2026-06-17-lean-vacuity-axiom-audit.json";
  let writeSc = false;
  let quiet = false;
  let onlyCat: Category | undefined;
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--json") jsonOut = argv[++i];
    else if (a === "--write-sidecars") writeSc = true;
    else if (a === "--quiet") quiet = true;
    else if (a === "--only") onlyCat = argv[++i] as Category;
    else roots.push(a);
  }
  const scanRoots = roots.length ? roots : DEFAULT_ROOTS;

  const files: string[] = [];
  for (const r of scanRoots) collectLean(resolve(REPO_ROOT, r), files);
  files.sort();

  const flaggedByLean = new Map<string, Hit[]>();
  const counts: Record<string, number> = {};
  let totalHits = 0;
  let exemptHits = 0;
  for (const f of files) {
    const hits = scanFile(f, onlyCat);
    if (hits.length === 0) continue;
    const rel = relative(REPO_ROOT, f);
    flaggedByLean.set(f, hits);
    for (const h of hits) {
      if (h.exempt) {
        exemptHits++;
        continue;
      }
      counts[h.category] = (counts[h.category] ?? 0) + 1;
      totalHits++;
    }
    if (!quiet)
      for (const h of hits) {
        const tag = h.exempt
          ? `EXEMPT(${h.exempt_reason})`
          : h.severity.toUpperCase();
        console.log(`${rel}:${h.line}  ${h.category}  [${tag}]  ${h.snippet}`);
      }
  }

  const flagged: Record<string, Hit[]> = {};
  for (const [f, hits] of flaggedByLean)
    flagged[relative(REPO_ROOT, f)] = hits;
  const witness = {
    audit: "lean-vacuity-axiom-audit",
    generated: new Date().toISOString(),
    script: SCRIPT_REL,
    scanned_files: files.length,
    files_flagged: Object.keys(flagged).length,
    total_defects: totalHits,
    total_exempt: exemptHits,
    categories: counts,
    flagged,
  };
  writeFileSync(resolve(REPO_ROOT, jsonOut), JSON.stringify(witness, null, 2) + "\n");

  if (writeSc) {
    const scriptHash = hashFile(resolve(REPO_ROOT, SCRIPT_REL)) ?? "unknown";
    const scriptCommitSha = gitFileCommitSha(SCRIPT_REL);
    const headSha = gitHeadSha();
    const n = writeSidecars(
      flaggedByLean,
      scriptHash,
      scriptCommitSha,
      headSha,
      onlyCat,
    );
    if (!quiet) console.log(`\nsidecars written/updated: ${n}`);
  }

  console.log(
    `\n${jsonOut} — scanned ${files.length} .lean, ${totalHits} defect candidate(s) across ${Object.keys(flagged).length} file(s) (${exemptHits} exempt).`,
  );
  for (const c of ALL_CATEGORIES)
    if (counts[c]) console.log(`  ${c}: ${counts[c]}`);
}

main();
