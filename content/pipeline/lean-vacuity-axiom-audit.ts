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
  | "proof-no-provable-axiom"
  | "proof-no-placeholder-stub"
  | "proof-no-trivial-type-mismatch"
  | "lean-import-after-content"
  // Conjecture-discipline classes (§3b / §3b-cond). A conjecture
  // axiomatised as a Lean `class`/`structure` can be sorry-free,
  // axiom-free, and compile cleanly while asserting *nothing* — an
  // empty marker `Prop`, or a structure whose docstring promises
  // defining properties it never encodes as fields. The proof-anti-
  // pattern detectors above all miss these because there is no proof
  // term to inspect. These four close that gap.
  | "proof-no-empty-prop-carrier"
  | "proof-claims-unencoded"
  | "proof-dependent-conjecture-not-conditional";

const ALL_CATEGORIES: Category[] = [
  "proof-no-trivial-true",
  "proof-no-self-assuming-projection",
  "proof-no-false-premise",
  "proof-no-decide-masking",
  "proof-no-provable-axiom",
  "proof-no-placeholder-stub",
  "proof-no-trivial-type-mismatch",
  "lean-import-after-content",
  "proof-no-empty-prop-carrier",
  "proof-claims-unencoded",
  "proof-dependent-conjecture-not-conditional",
];

const SEVERITY: Record<Category, "critical" | "major" | "minor"> = {
  "proof-no-trivial-true": "critical",
  "proof-no-self-assuming-projection": "critical",
  "proof-no-false-premise": "critical",
  "proof-no-provable-axiom": "critical",
  "proof-no-decide-masking": "major",
  "proof-no-placeholder-stub": "critical",
  // Compile-validity classes (not heuristics — guaranteed errors): a
  // content-block sibling carrying these never compiles. They are the gap
  // the vacuity detectors miss and the basis of the CI `--fail-on` gate.
  "proof-no-trivial-type-mismatch": "critical",
  "lean-import-after-content": "critical",
  // Conjecture-discipline severities. An empty `Prop` carrier and a
  // dependent conjecture that forgot its conditional hypothesis are
  // both unsound-as-stated (a downstream `[C]`-conditional theorem
  // built on either is vacuous), hence critical. The claims-unencoded
  // and unclassified findings are high-recall candidates → major.
  "proof-no-empty-prop-carrier": "critical",
  "proof-claims-unencoded": "major",
  "proof-dependent-conjecture-not-conditional": "critical",
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
  /** Extra human-readable context for the witness/evidence (e.g. which
   * claimed properties went unencoded). */
  detail?: string;
}

// ── Lean source helpers ─────────────────────────────────────────────

/** Recursively collect every `.lean` under `root`. A `root` that is itself a
 * `.lean` file is accepted directly — this enables diff-scoped CI gating
 * (pass the `git diff`-listed changed files, not just directories). */
function collectLean(root: string, out: string[]): void {
  if (!existsSync(root)) return;
  if (statSync(root).isFile()) {
    if (root.endsWith(".lean")) out.push(root);
    return;
  }
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
// Kinds an agent can abuse to DODGE the vacuity audit: re-declaring a
// vacuous `theorem X : True := trivial` as `def X : True := trivial`
// hides it from every `PROVABLE_KINDS`-guarded detector below. A real
// `def`/`abbrev`/`instance` almost never has type `True`, so a
// trivial-bodied `: True` declaration of these kinds is the dodge
// signature and is flagged (see `detectTrivialTrue`).
const DODGE_KINDS = /^(def|abbrev|instance)\b/;
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

/**
 * True when the `.lean`'s content-block sibling `.ts` is a `conjecture`
 * block. Such a block's Lean file may legitimately carry a `def … :
 * True := trivial` placeholder (the conjecture's content is the unproved
 * input per §3b), so it is an acknowledged conjectural representation —
 * NOT an audit dodge. This is the "except conjectures" carve-out.
 */
const conjectureBlockCache = new Map<string, boolean>();
function isConjectureBlock(leanAbs: string): boolean {
  const cached = conjectureBlockCache.get(leanAbs);
  if (cached !== undefined) return cached;
  const ts = leanAbs.replace(/\.lean$/, ".ts");
  let result = false;
  if (existsSync(ts)) {
    try {
      result = /export\s+default\s+conjecture\s*\(/.test(
        readFileSync(ts, "utf-8"),
      );
    } catch {
      result = false;
    }
  }
  conjectureBlockCache.set(leanAbs, result);
  return result;
}

const TRIVIAL_BODY = /^\s*(trivial|by\s+trivial|sorry|by\s+sorry|⟨⟩|by\s+exact\s+trivial)\s*$/;

function detectTrivialTrue(
  d: Decl,
  rawSrc: string,
  fileIsStub: boolean,
  leanAbs: string,
): Hit | undefined {
  const isProvable = PROVABLE_KINDS.test(d.kind);
  // `def`/`abbrev`/`instance` are scanned for the theorem→def audit-dodge:
  // any `: True` conclusion (the body is irrelevant — `True` is trivially
  // inhabited). They are NOT scanned for the reflexive-tautology case (a
  // real def legitimately reduces to a value).
  const isDodge = DODGE_KINDS.test(d.kind);
  if (!isProvable && !isDodge) return undefined;
  const concl = conclusionOf(d.sig);
  const body = d.body.trim();
  let pattern: string | undefined;
  if (/^True\b/.test(concl) || concl === "True") pattern = "conclusion-True";
  else if (/^True(\s*[∧×]\s*True)+$/.test(concl)) pattern = "conclusion-True-conj";
  else {
    // reflexive tautology: `: X = X := rfl` — provable kinds only.
    if (isProvable) {
      const eq = concl.match(/^(.+?)=(.+)$/);
      if (eq && /^\s*(rfl|by\s+rfl|Eq\.refl)\b/.test(body)) {
        const lhs = eq[1].replace(/\s+/g, "");
        const rhs = eq[2].replace(/\s+/g, "");
        if (lhs && lhs === rhs)
          return mk(d, "proof-no-trivial-true", "reflexive-tautology", false);
      }
    }
    return undefined;
  }
  // A `: True := trivial/sorry` is the canonical stub body. Classify
  // shadow (real decl exists elsewhere → exempt) vs placeholder (no
  // real decl → genuine gap, flag).
  const isStubBody = TRIVIAL_BODY.test(body);
  // A `def`/`abbrev`/`instance` concluding `True` is vacuous REGARDLESS of
  // its body — `True` is trivially inhabited, so the body carries no
  // content. Flag every such `def : True` (widened 2026-06-23: the
  // trivial-body-only check let `:= by <tactic>` re-dodge); the shadow-stub
  // and conjecture-block carve-outs below still apply.
  if (isDodge || fileIsStub || isStubBody) {
    const real = findRealDecl(leanAbs, rawSrc, d.name);
    if (real) {
      const h = mk(
        d,
        "proof-no-trivial-true",
        isDodge ? "def-disguised-true-shadow" : pattern,
        true,
      );
      h.exempt_reason = `shadow-stub (real formalisation: ${real})`;
      return h;
    }
    // "except conjectures": a `def : True` inside a `conjecture` content
    // block is the acknowledged §3b placeholder, not a dodge.
    if (isDodge && isConjectureBlock(leanAbs)) {
      const h = mk(d, "proof-no-trivial-true", "def-disguised-true-conjecture", true);
      h.exempt_reason = "conjecture-block Lean placeholder (§3b)";
      return h;
    }
    // genuine placeholder — no resolvable real decl. A `def`-kind hit is
    // the theorem→def dodge (a forbidden audit workaround, AGENTS.md
    // §"No audit-dodging"); honest disposition is to state the real
    // proposition with `sorry` + `-- Ref:`, or demote to `conjecture`.
    return mk(
      d,
      "proof-no-trivial-true",
      isDodge ? "def-disguised-true" : "placeholder-true",
      false,
    );
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

// ── Conjecture-discipline detectors (§3b / §3b-cond) ───────────────────
// A conjecture axiomatised as a Lean `class`/`structure` is the project's
// sanctioned way to carry an open problem (§3b). But the carrier only does
// its job if it actually *asserts* the conjecture's content: an empty
// `Prop` class asserts nothing (any `instance : C := ⟨⟩` discharges it),
// and a structure whose docstring promises "positivity" / "archimedean
// smallness" while encoding only `ε ≠ 𝟙` under-delivers on its own prose.
// A downstream §3b-cond theorem `[C] → …` built on such a carrier is
// vacuous — it proves nothing "modulo the conjecture" because the
// conjecture, as formalised, says nothing. The proof-anti-pattern
// detectors above all miss this: there is no proof term, no `sorry`, no
// `axiom`, and the file compiles. These detectors inspect the *carrier*.

/** Field declarations of a `structure`/`class`, parsed from the
 * comment-free decl text. Returns `{name, type}` per field. An
 * `extends`-only class (no `where`) returns `[]` but is detected as
 * inheriting content via `declExtends`. */
function classFields(d: Decl): { name: string; type: string }[] {
  const whereIdx = d.text.search(/(^|\s)where(\s|$)/);
  if (whereIdx < 0) return [];
  const after = d.text.slice(whereIdx + d.text.slice(whereIdx).indexOf("where") + 5);
  const lines = after.split("\n");
  const fields: { name: string; type: string }[] = [];
  for (const raw of lines) {
    const line = raw.replace(/\s+$/, "");
    if (line.trim() === "") continue;
    // A new field: `name : type` or `(name : type)` at field indent. A
    // continuation of the previous field's type is deeper / has no
    // leading `ident :`, so append it to the last field.
    const m = line.match(/^\s*\(?\s*([a-zA-Z_][\w']*)\s*:\s*(.*)$/);
    if (m && !/^(end|namespace|section|deriving|with)\b/.test(m[1])) {
      fields.push({ name: m[1], type: m[2] });
    } else if (fields.length > 0) {
      fields[fields.length - 1].type += " " + line.trim();
    }
  }
  return fields;
}

function declExtends(d: Decl): boolean {
  return /\bextends\b/.test(d.sig);
}

/** Sort of a `class`/`structure` head: the type after the top-level `:`
 * (`Prop`, `Type`, `Type u`, …). Empty when no explicit sort ascription. */
function declSort(d: Decl): string {
  return conclusionTypeAscription(d.sig);
}

/** Raw (comment-bearing) doc region immediately above a decl: the
 * contiguous run of `--` lines and `/- … -/` / `/-- … -/` / `/-! … -/`
 * blocks directly above `declIdx0` (0-indexed), skipping `@[…]` attribute
 * lines. Markdown and `-- Ref:` / `-- @conjecture` annotations are
 * preserved so the conjecture-discipline heuristics can read them. */
function docBlockAbove(origLines: string[], declIdx0: number): string {
  const collected: string[] = [];
  let j = declIdx0 - 1;
  while (j >= 0 && /^\s*@\[/.test(origLines[j])) j--;
  while (j >= 0) {
    const t = origLines[j].trim();
    if (t === "") break;
    if (t.startsWith("--")) {
      collected.unshift(origLines[j]);
      j--;
      continue;
    }
    if (t.endsWith("-/")) {
      // Prepend lines up to and including the `/-` / `/--` / `/-!` opener.
      while (j >= 0) {
        collected.unshift(origLines[j]);
        const opens = /\/-/.test(origLines[j]);
        j--;
        if (opens) break;
      }
      continue;
    }
    break;
  }
  return collected.join("\n");
}

/** True when the decl is itself a §3b conjecture carrier — a strong
 * signal that the *class* axiomatises a conjecture, not merely that its
 * prose mentions one. We require a `conj:` label/reference or explicit
 * "axiomatis(e)" wording; a bare "conjecture"/"conjectural" word in the
 * prose is NOT enough (it flags definitions that merely discuss a
 * conjecture, e.g. a `def:`-labelled substrate). A `def:`-labelled
 * carrier with no `conj:` self-reference is a definition, not a
 * conjecture, and is excluded. */
function isConjectureCarrier(doc: string): boolean {
  const hasConjRef = /conj:[a-z0-9-]+/i.test(doc) || /\\label\{conj:/i.test(doc);
  const axiomatises = /axiomatis/i.test(doc);
  if (!hasConjRef && !axiomatises) return false;
  // A `def:`-labelled carrier that only *references* a conjecture (no
  // `conj:` self-label, no axiomatisation) is a definition — exclude.
  const ownDefLabel = /\\label\{def:/i.test(doc) || /\bdef:[a-z0-9-]+/i.test(doc);
  const ownConjLabel = /\\label\{conj:/i.test(doc);
  if (ownDefLabel && !ownConjLabel && !axiomatises) return false;
  return true;
}

/** A field type that encodes an actual proposition (quantifier / relation /
 * connective), as opposed to a data field (`obj : C`, `f : A ⟶ B`). A lone
 * `≠` non-triviality counts as the weakest possible Prop content and is
 * tracked separately by the caller. */
function isPropBearingType(type: string): boolean {
  return /[∀∃]|↔|(?<![-=])→|≤|≥|(?<![:<>=!])<|(?<![-:<>=!])>|≠|\b=\b|\bTrue\b|\bFalse\b/.test(
    type,
  );
}

const MARKER_OPT_OUT = /@marker\b|opaque\s+(tag|marker|predicate)/i;

function detectEmptyPropCarrier(
  d: Decl,
  doc: string,
): Hit | undefined {
  if (d.kind !== "class" && d.kind !== "structure") return undefined;
  if (declSort(d) !== "Prop") return undefined; // only Prop carriers
  if (declExtends(d)) return undefined; // inherits content from parent
  if (classFields(d).length > 0) return undefined; // has content
  if (MARKER_OPT_OUT.test(doc)) {
    const h = mk(d, "proof-no-empty-prop-carrier", "annotated-marker", true);
    h.exempt_reason = "explicit @marker opaque-tag opt-out";
    return h;
  }
  const conj = isConjectureCarrier(doc);
  return mk(
    d,
    "proof-no-empty-prop-carrier",
    conj ? "empty-conjecture-class" : "empty-prop-class",
    false,
  );
}

function detectClaimsUnencoded(d: Decl, doc: string): Hit | undefined {
  if (d.kind !== "class" && d.kind !== "structure") return undefined;
  const fields = classFields(d);
  if (fields.length === 0) return undefined; // empty → other detector
  // The doc must *enumerate defining properties* — a "properties / axioms /
  // conditions / laws" framing — to avoid flagging prose that merely uses
  // bold for emphasis.
  if (
    !/\b(propert(y|ies)|axiom|condition|law|must satisfy|pick(s)? out|characteri[sz])/i.test(
      doc,
    )
  )
    return undefined;
  const bullets = [
    ...doc.matchAll(/(?:^|\n)\s*(?:--\s*)?[-*]\s*\*\*([^*]+)\*\*/g),
  ].map((m) => m[1].trim());
  const claimed = bullets.length;
  if (claimed < 2) return undefined;
  // Prop-bearing fields whose content is more than a bare `≠` non-triviality.
  const encoded = fields.filter(
    (f) => isPropBearingType(f.type) && !/^[^=<>≤≥∀∃↔]*≠/.test(f.type),
  ).length;
  if (encoded >= claimed) return undefined;
  const h = mk(d, "proof-claims-unencoded", "docstring-claims-gap", false);
  h.detail = `doc enumerates ${claimed} propert${
    claimed === 1 ? "y" : "ies"
  } (${bullets.join(", ")}); only ${encoded} encoded as Prop field(s)`;
  return h;
}

// ── Derived primary/dependent classification (no hand tags) ────────────
// A dependent conjecture takes its primary as an `[Instance]` (or other
// binder / `extends`) hypothesis — the §3b-cond pattern. That edge is
// already in the Lean type, so the primary-vs-dependent split is a graph
// computation over signatures, not something an author must tag.
// `classifyConjectures` does a global two-pass: (1) collect every
// conjecture carrier (`conj:` label / axiomatises), (2) read instance
// binders to build the dependency graph. Primary = no conjecture
// hypothesis; dependent = ≥1. The only emitted *defect* is the genuine
// unsound case: prose that explicitly claims conditionality on `conj:Y`
// while the type binds no such class.

interface ConjCarrier {
  name: string;
  file: string;
  line: number;
  sig: string;
  doc: string;
  ownLabels: string[];
}

interface ConjGraph {
  total: number;
  primary: string[];
  dependent: { name: string; file: string; line: number; dependsOn: string[] }[];
}

/** conj: labels this carrier *declares* as its own (`\label{conj:X}`). */
function ownConjLabels(doc: string): string[] {
  const out = new Set<string>();
  for (const m of doc.matchAll(/\\label\{conj:([a-z0-9-]+)\}/gi))
    out.add(m[1].toLowerCase());
  return [...out];
}

/** Conjecture-class names referenced in `sig`'s binders — instance `[…]`,
 * implicit `{…}`, strict-implicit `⦃…⦄`, or `extends …` — restricted to
 * the known carrier `names`. */
function bindersReferencing(sig: string, names: Set<string>): string[] {
  const found = new Set<string>();
  for (const m of sig.matchAll(/[[{⦃]([^\]}⦄]*)[\]}⦄]/g))
    for (const w of m[1].split(/[^A-Za-z0-9_'.]+/))
      if (names.has(w)) found.add(w);
  for (const m of sig.matchAll(/\bextends\s+([A-Z][\w'.]*)/g))
    if (names.has(m[1])) found.add(m[1]);
  return [...found];
}

function classifyConjectures(files: string[]): {
  graph: ConjGraph;
  hitsByFile: Map<string, Hit[]>;
} {
  const carriers: ConjCarrier[] = [];
  for (const f of files) {
    let src: string;
    try {
      src = readFileSync(f, "utf-8");
    } catch {
      continue;
    }
    const orig = src.split("\n");
    const code = stripCommentLines(src);
    for (const d of splitDecls(orig, code)) {
      if (d.kind !== "class" && !(d.kind === "structure" && declSort(d) === "Prop"))
        continue;
      const doc = docBlockAbove(orig, d.startLine - 1);
      if (!isConjectureCarrier(doc)) continue;
      carriers.push({
        name: d.name,
        file: relative(REPO_ROOT, f),
        line: d.startLine,
        sig: d.sig,
        doc,
        ownLabels: ownConjLabels(doc),
      });
    }
  }
  const names = new Set(carriers.map((c) => c.name));
  const labelToName = new Map<string, string>();
  for (const c of carriers)
    for (const l of c.ownLabels) if (!labelToName.has(l)) labelToName.set(l, c.name);

  const primary: string[] = [];
  const dependent: ConjGraph["dependent"] = [];
  const hitsByFile = new Map<string, Hit[]>();

  for (const c of carriers) {
    const edges = bindersReferencing(c.sig, names).filter((n) => n !== c.name);
    if (edges.length > 0)
      dependent.push({ name: c.name, file: c.file, line: c.line, dependsOn: edges });
    else primary.push(c.name);

    // Derived defect: the doc *explicitly* claims conditionality on a
    // `conj:Y` (another carrier) yet the type binds no such class. This is
    // the intent-vs-type mismatch — a result that reads as conditional but
    // is stated unconditionally. Plain prose mentions are NOT flagged.
    const claimed = [
      ...c.doc.matchAll(
        /(?:conditional on|assuming|given|depends on|modulo)\s+[[`]?\s*conj:([a-z0-9-]+)/gi,
      ),
    ].map((m) => m[1].toLowerCase());
    const unmet = claimed
      .filter((l) => !c.ownLabels.includes(l))
      .map((l) => labelToName.get(l))
      .filter((n): n is string => !!n && n !== c.name && !edges.includes(n));
    if (unmet.length > 0) {
      const abs = resolve(REPO_ROOT, c.file);
      const hit: Hit = {
        line: c.line,
        category: "proof-dependent-conjecture-not-conditional",
        pattern: "prose-conditional-not-in-type",
        snippet: c.name,
        decl: c.name,
        severity: SEVERITY["proof-dependent-conjecture-not-conditional"],
        detail: `doc claims conditionality on ${unmet
          .map((n) => `\`${n}\``)
          .join(", ")} but the signature takes no binder on it`,
      };
      const arr = hitsByFile.get(abs) ?? [];
      arr.push(hit);
      hitsByFile.set(abs, arr);
    }
  }
  return { graph: { total: carriers.length, primary: primary.sort(), dependent }, hitsByFile };
}

// ── Compile-validity detectors (guaranteed Lean errors, not heuristics) ──
// These catch the gap the vacuity detectors miss: a sibling that does not
// even typecheck. They never compile, so they are never exempt.

/** A term-mode `trivial` body under a non-`True`-typed `def`/`abbrev` is a
 * guaranteed type error — `trivial : True : Prop` cannot inhabit a data type
 * (`ℝ`, `R`, …). This is exactly what bit `conj-rho-k-pair-gen` (`: R := trivial`)
 * and `kashaev-volume-conjecture` (`pieceVolume : ℝ := trivial`). `sorry`
 * (inhabits any type) and `by trivial` (may close a Prop goal) are NOT flagged;
 * a `: True := trivial` is the vacuity case handled by `detectTrivialTrue`. */
const TERM_TRIVIAL = /^trivial$/;
function detectTrivialTypeMismatch(d: Decl): Hit | undefined {
  if (!/^(def|abbrev)\b/.test(d.kind)) return undefined;
  if (!TERM_TRIVIAL.test(d.body.trim())) return undefined;
  const concl = conclusionTypeAscription(d.sig);
  if (!concl || concl === "True" || /^True\b/.test(concl)) return undefined;
  return mk(d, "proof-no-trivial-type-mismatch", "term-trivial-nontrue-type", false);
}

/** Lean 4 requires every `import` to precede all commands (a `/-!` module
 * docstring counts as a command). A `/-!`-before-`import`, or any command
 * before an `import`, is a hard parse error — the file never compiles. Latent
 * in content-block siblings outside the CI-built lake tree (caught: kashaev).
 * Plain `--` / `/- -/` comments and a leading `prelude` legally precede
 * imports and do not count as content. */
const IMPORT_LINE = /^\s*import\b/;
function detectImportOrder(origLines: string[]): Hit | undefined {
  let inBlock = false;
  let sawContent = false;
  for (let i = 0; i < origLines.length; i++) {
    let line = origLines[i];
    if (inBlock) {
      const close = line.indexOf("-/");
      if (close < 0) continue;
      inBlock = false;
      line = line.slice(close + 2);
    }
    const t = line.trim();
    if (t === "") continue;
    if (IMPORT_LINE.test(line)) {
      if (sawContent)
        return {
          line: i + 1,
          category: "lean-import-after-content",
          pattern: "import-after-docstring-or-command",
          snippet: snip(line),
          severity: SEVERITY["lean-import-after-content"],
        };
      continue;
    }
    if (t.startsWith("--") || t === "prelude") continue;
    if (t.startsWith("/-!")) {
      sawContent = true; // module docstring is a command
      if (!line.includes("-/")) inBlock = true;
      continue;
    }
    if (t.startsWith("/-")) {
      if (!line.includes("-/")) inBlock = true; // plain block comment: trivia
      continue;
    }
    // A `/-!` docstring is handled above; any other non-blank, non-comment,
    // non-import token before the imports finish is a command → content.
    sawContent = true;
  }
  return undefined;
}

// ── File-level scan ─────────────────────────────────────────────────

function scanFile(absPath: string, onlyCat: Category | undefined): Hit[] {
  const src = readFileSync(absPath, "utf-8");
  const origLines = src.split("\n");
  const codeLines = stripCommentLines(src);
  const fileIsStub = STUB_MARKERS.test(src);
  const isPlaceholderStub = /# QOU\..* — placeholder stub/.test(src);
  const decls = splitDecls(origLines, codeLines);
  const hits: Hit[] = [];
  const push = (h: Hit | undefined) => {
    if (h && (!onlyCat || h.category === onlyCat)) hits.push(h);
  };

  if (isPlaceholderStub && (!onlyCat || onlyCat === "proof-no-placeholder-stub")) {
    hits.push({
      line: 1,
      category: "proof-no-placeholder-stub",
      pattern: "placeholder-stub-file",
      snippet: "# QOU... — placeholder stub",
      severity: "critical"
    });
  }

  for (const d of decls) {
    push(detectTrivialTrue(d, src, fileIsStub, absPath));
    push(detectSelfAssuming(d));
    push(detectDecideMasking(d));
    push(detectFalsePremise(d));
    push(detectProvableAxiom(d, origLines));
    push(detectTrivialTypeMismatch(d));
    // Conjecture-discipline *content* detectors operate on the
    // `class`/`structure` carrier + its raw doc block. The primary-vs-
    // dependent classification is NOT a per-file check — it is derived
    // globally from instance binders in `classifyConjectures` (the
    // dependency is already in the Lean type; no hand tag is needed).
    const doc = docBlockAbove(origLines, d.startLine - 1);
    push(detectEmptyPropCarrier(d, doc));
    push(detectClaimsUnencoded(d, doc));
  }
  const importHit = detectImportOrder(origLines);
  if (importHit && (!onlyCat || onlyCat === "lean-import-after-content"))
    hits.push(importHit);
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
                    `${relative(REPO_ROOT, leanAbs)}:${h.line} [${h.pattern}] ${h.snippet}${
                      h.detail ? ` — ${h.detail}` : ""
                    }`,
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
  // CI gate: exit 1 if any non-exempt hit lands in one of these categories.
  // Default targets the two guaranteed-error (compile-validity) classes so
  // the gate is low-false-positive; the high-recall vacuity candidates stay
  // warn-only (agent-adjudicated). Pass `--fail-on a,b` to override.
  let failOn: Set<string> | undefined;
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--json") jsonOut = argv[++i];
    else if (a === "--write-sidecars") writeSc = true;
    else if (a === "--quiet") quiet = true;
    else if (a === "--only") onlyCat = argv[++i] as Category;
    else if (a === "--fail-on") {
      // Only consume the next token if it is a comma-list of valid categories;
      // otherwise (a flag, a path, or end-of-args) fall back to the default
      // compile-validity classes WITHOUT advancing the index (Gemini #2753).
      const DEFAULT_FAIL = [
        "proof-no-trivial-type-mismatch",
        "lean-import-after-content",
      ];
      const next = argv[i + 1];
      const explicit =
        next !== undefined &&
        !next.startsWith("-") &&
        next.split(",").every((s) => (ALL_CATEGORIES as string[]).includes(s.trim()));
      const cats = explicit ? (i++, next.split(",")) : DEFAULT_FAIL;
      failOn = new Set(cats.map((s) => s.trim()).filter(Boolean));
    }
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
        console.log(
          `${rel}:${h.line}  ${h.category}  [${tag}]  ${h.snippet}${h.detail ? ` — ${h.detail}` : ""}`,
        );
      }
  }

  // Derived primary/dependent classification — a global graph pass over
  // instance binders. Merge its `not-conditional` defects into the per-
  // file map (respecting `--only`) so they are counted, written, and
  // gated like any other category.
  const { graph, hitsByFile: conjHits } = classifyConjectures(files);
  for (const [abs, hits] of conjHits) {
    const keep = hits.filter((h) => !onlyCat || h.category === onlyCat);
    if (keep.length === 0) continue;
    flaggedByLean.set(abs, [...(flaggedByLean.get(abs) ?? []), ...keep]);
    for (const h of keep) {
      counts[h.category] = (counts[h.category] ?? 0) + 1;
      totalHits++;
      if (!quiet)
        console.log(
          `${relative(REPO_ROOT, abs)}:${h.line}  ${h.category}  [${h.severity.toUpperCase()}]  ${h.snippet}${h.detail ? ` — ${h.detail}` : ""}`,
        );
    }
  }
  if (!quiet)
    console.log(
      `\nconjecture graph: ${graph.total} carrier(s) — ${graph.primary.length} primary, ${graph.dependent.length} dependent (derived from instance binders).`,
    );

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
    conjecture_graph: graph,
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

  if (failOn) {
    const failing: string[] = [];
    for (const [f, hits] of flaggedByLean)
      for (const h of hits)
        if (!h.exempt && failOn.has(h.category))
          failing.push(`${relative(REPO_ROOT, f)}:${h.line} [${h.category}] ${h.snippet}`);
    if (failing.length) {
      console.error(
        `\n✗ CI gate: ${failing.length} guaranteed-error defect(s) in [${[...failOn].join(", ")}]:`,
      );
      for (const l of failing) console.error(`  ${l}`);
      process.exit(1);
    }
    console.log(`\n✓ CI gate clean for [${[...failOn].join(", ")}].`);
  }
}

main();
