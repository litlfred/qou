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
 *   proof-no-trivial-true            — conclusion is `True` / a tautology.
 *       Tautology patterns: `: True`, `def`-disguised-`True`, reflexive
 *       equality `X = X` (any body — incl. `1 = 1 := sorry`), `∃ …, True`,
 *       and a top-level `… ∨ True`. All assert nothing regardless of proof.
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
// `folio-assistant/cat-harness/schemas/block-qa.ts`, but `folio-assistant/` is
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
const DEFAULT_ROOTS = ["folio"];
const SKIP_DIRS = new Set([
  ".lake",
  "node_modules",
  "build",
  ".git",
  "_deprecated",
]);
const SCRIPT_REL = "content/pipeline/lean-vacuity-axiom-audit.ts";

// Lake package prefix → lakeRoot (inlined to stay free of the migrated
// `folio-assistant/cat-harness/schemas/lean-packages.ts`).
const LAKE_ROOTS: Record<string, string> = {
  qou: "folio/quantum-observable-universe/lean",
  ugb: "folio/unital-groebner-bases/lean",
  fred2005: "folio/fred2005-formal-groups/lean",
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
  | "proof-dependent-conjecture-not-conditional"
  // A `rfl`-proved statement binding an explicit hypothesis it cannot use.
  // `rfl` consults no hypothesis, so the claim holds for every value of it.
  // Not reachable by the projection detector (the body is not `ctx.field`).
  | "proof-no-unused-hypothesis-rfl"
  // The docstring says the body is a `sorry`; the body has none.
  //
  // Why this is worth its own criterion rather than folding into the
  // projection detector: `detectSelfAssuming` gates on the projected FIELD
  // NAME (`CONCLUSION_FIELD` — `claim_`, `_holds`, `_eq`, …), so a class field
  // named outside that convention is invisible to it no matter how blatantly
  // it posits the conclusion. Two live cases were found by hand on 2026-08-08,
  // both missed for exactly that reason and both named `*_ident`:
  // `confinement_categorical` (`exact ctx.confinement_ident`) and
  // `nucleon_ordering_factorization` (`exact ctx.factorization_ident`).
  //
  // This detector keys on nothing but the docstring and the body, so no
  // naming convention can dodge it. It is also the *cheapest* signal for the
  // defect: an author who writes "the body is therefore `sorry`" and then
  // discharges by projection has left the contradiction in plain text. When
  // the prose and `#print axioms` disagree about whether a proof exists, one
  // of them is wrong and the class is usually positing its own conclusion.
  | "proof-docstring-sorry-mismatch"
  // A `Prop` carrier that Lean PROVED inhabitable with no hypotheses.
  //
  // Every other category on this list is decided by reading source. This one
  // cannot be: the defect is that the carrier's fields, whatever shape they
  // have, assert nothing — and shape is exactly what a static scan sees. The
  // corpus's own exemplar makes the point. AGENTS.md §3b-tax cites
  // `ConditionalClasses.lean` as the model of a carrier "in the *shape* of the
  // claim", which it is; each field is a parameter-quantified inequality. Every
  // one is also discharged by zero, and that file raises **0** lines here.
  //
  // So the evidence comes from OUTSIDE this scanner:
  // `scripts/vacuous-prop-carrier-probe.py` emits a Lean file re-declaring each
  // self-contained carrier and attempts to inhabit it, and records what Lean
  // said in `docs/audits/vacuous-prop-carrier-baseline.json`. This audit reads
  // that record. See `seedProbeInhabitedCandidates` for the asymmetry that
  // governs which of its verdicts may be used.
  | "proof-carrier-inhabited-by-probe";

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
  "proof-no-unused-hypothesis-rfl",
  "proof-docstring-sorry-mismatch",
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
  // High-recall candidate, agent-confirmed like the conjecture-discipline
  // classes: a `rfl` proof with a decorative hypothesis is usually a
  // definitional restatement (should be a `def`), occasionally a real signal
  // that the underlying definition ignores an argument. Major, not critical.
  "proof-no-unused-hypothesis-rfl": "major",
  // Critical: the docstring is not merely stale, it is *load-bearing
  // misinformation*. An audit reading the prose records an honest queued gap;
  // an audit reading `#print axioms` records a proof. Both are wrong, and they
  // disagree — so neither review path can catch it unaided.
  "proof-docstring-sorry-mismatch": "critical",
  // Major, not critical, and deliberately so. Lean proving the carrier
  // inhabitable is a hard fact, but "asserts nothing" is not the same as
  // "should not exist": a carrier can be provably inhabitable-by-zero and
  // still be the right disposition — the three `FMap*` carriers are typed
  // `: True` behind a sanctioned `@marker` opt-out. The probe settles
  // inhabitability; the agent still settles disposition.
  "proof-carrier-inhabited-by-probe": "major",
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
  /** Set when a `triage pending` exemption was lifted because the review
   * ledger already carries an agent verdict of `genuine` for this key. Carries
   * the exemption that was superseded, so the promotion stays auditable. */
  promoted_from_exempt?: string;
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
    candidates.push(resolve(REPO_ROOT, "folio/quantum-observable-universe", m[1]));
    candidates.push(resolve(REPO_ROOT, m[1]));
  }
  // (3) QOU.A.B namespace → lean/QOU/A/B.lean
  for (const m of rawSrc.matchAll(/\bQOU(?:\.[A-Z][\w]*)+/g)) {
    const parts = m[0].split(".");
    // drop a trailing lowercase decl segment if present
    const modParts = parts.filter((p, idx) => idx === 0 || /^[A-Z]/.test(p));
    const modPath = modParts.join("/");
    candidates.push(
      resolve(REPO_ROOT, "folio/quantum-observable-universe/lean", `${modPath}.lean`),
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

/** Split on top-level `∧`, ignoring any nested inside brackets. */
function splitTopLevelAnd(s: string): string[] {
  const parts: string[] = [];
  let depth = 0;
  let cur = "";
  for (const c of s) {
    if ("([{⟨⦃".includes(c)) depth++;
    else if (")]}⟩⦄".includes(c)) depth--;
    if (c === "∧" && depth === 0) {
      parts.push(cur);
      cur = "";
      continue;
    }
    cur += c;
  }
  parts.push(cur);
  return parts.map((p) => p.trim()).filter((p) => p.length > 0);
}

/**
 * Is this single proposition a tautology on its face — `True`, a reflexive
 * `X = X`, or a reflexive equality hidden behind an ascribed numeric literal
 * (`(0 : ℝ) = 0`)? Returns the shape, or `null` if it asserts something.
 */
function reflexiveKind(s: string): "plain" | "ascribed" | "true" | null {
  const t = s.trim();
  if (/^True$/.test(t)) return "true";
  const eq = t.match(/^([^=]+?)=([^=].*)$/);
  if (!eq) return null;
  const lhs = eq[1].replace(/\s+/g, "");
  const rhs = eq[2].replace(/\s+/g, "");
  if (lhs && lhs === rhs) return "plain";
  const unascribeLit = (x: string) => {
    const m = x.match(/^\((-?\d+(?:\.\d+)?)\s*:[^():]*\)$/);
    return m ? m[1] : x;
  };
  const nl = unascribeLit(lhs);
  const nr = unascribeLit(rhs);
  if (nl && nl === nr && (nl !== lhs || nr !== rhs)) return "ascribed";
  return null;
}

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
  // `axiom X : True` was invisible here until 2026-08-08: `axiom` is neither
  // a PROVABLE_KIND nor a DODGE_KIND, so the guard below dropped it before any
  // pattern ran. It is the purest form of the anti-pattern — an axiom whose
  // conclusion is `True` asserts nothing, has no body to inspect, and (unlike
  // a `theorem`) is not even *provable*-looking, so no reader thinks to check
  // it. Live instance that motivated this: `QOU.Eightfold.Sym2Gate`'s
  // `su3_sym2_irreducible`, an `axiom … : True` standing in for "the SU(3)
  // fundamental has irreducible Sym²" (drain: bean `qou-8fl1` item 3).
  const isAxiom = /^axiom\b/.test(d.kind);
  if (!isProvable && !isDodge && !isAxiom) return undefined;
  // Strip `--` line comments from the conclusion before pattern-matching.
  // A commented-out explanation sitting between the `:` and the actual
  // conclusion hides the conclusion from every test below — which is exactly
  // how `su3_sym2_irreducible` evaded this detector even after `axiom` was
  // admitted above:
  //
  //     axiom su3_sym2_irreducible :
  //       -- "For V = the SU(3) fundamental (dim 3), Sym²(V) is irreducible."
  //       True
  //
  // The prose is where the real claim lives; `True` is what is asserted.
  const concl = conclusionOf(d.sig)
    .replace(/--[^\n]*/g, " ")
    .replace(/\s+/g, " ")
    .trim();
  const body = d.body.trim();
  let pattern: string | undefined;
  if (/^True\b/.test(concl) || concl === "True")
    pattern = isAxiom ? "axiom-true" : "conclusion-True";
  else if (/^True(\s*[∧×]\s*True)+$/.test(concl))
    pattern = isAxiom ? "axiom-true" : "conclusion-True-conj";
  else {
    // Tautological conclusions — provable kinds only. The STATEMENT asserts
    // nothing, so the body is irrelevant (rfl, sorry, simp, decide all
    // "prove" it).
    if (isProvable) {
      // Use the type-ascription conclusion (FIRST top-level `:`), robust to
      // an existential's binder colon (`∃ v : Nat, True`) that the
      // last-colon `conclusionOf` would mis-slice.
      const conclTA = conclusionTypeAscription(d.sig) || concl;
      // (a) reflexive equality `: X = X` — vacuous REGARDLESS of body.
      // Widened 2026-06-29: the prior check required an rfl-like body, so
      // `1 = 1 := sorry` (the lr-tensor dodge) and `a = a := by simp`
      // slipped through. Match is syntactic (lhs === rhs after stripping
      // whitespace), so `a + b = b + a` is NOT a false positive.
      // Strip leading ∀-binders and → antecedents before the reflexive test.
      // A tautology is no less tautological for being quantified: the body of
      // `∀ N : ℕ, 2 ≤ N → f N = f N` is still `X = X`, and matching the WHOLE
      // conclusion compares `∀ N : ℕ, 2 ≤ N → f N` against `f N` and misses it.
      // That is how `orbit_sum_general` shipped
      // `∀ N, 2 ≤ N → cl3OrbitSumPredicted N zeta3 = cl3OrbitSumPredicted N zeta3`.
      // Only the matched prefix is dropped — the two SIDES are still compared
      // verbatim, so `∀ n, f n = g n` is untouched.
      let refBody = conclTA;
      for (;;) {
        const before = refBody;
        refBody = refBody.replace(/^\s*(?:∀|Π)\s*[^,]*,\s*/, "");
        // Drop a leading antecedent only when it carries no `=` of its own,
        // so an equational hypothesis is never mistaken for the conclusion.
        refBody = refBody.replace(/^\s*([^=→↔]+?)→\s*/, "");
        if (refBody === before) break;
      }
      const eq = (refBody.match(/^([^=]+?)=([^=].*)$/) ?? conclTA.match(/^([^=]+?)=([^=].*)$/)) as
        | RegExpMatchArray
        | null;
      if (eq) {
        const lhs = eq[1].replace(/\s+/g, "");
        const rhs = eq[2].replace(/\s+/g, "");
        if (lhs && lhs === rhs)
          return mk(d, "proof-no-trivial-true", "reflexive-tautology", false);
        // Whitespace-only normalisation misses an ascribed NUMERIC LITERAL:
        // `(0 : ℝ) = 0` compares `(0:ℝ)` against `0` and slips through. That
        // is how `yangBaxter_energy_zero` / `farComm_energy_zero` shipped a
        // literal `(0 : ℝ) = 0` as the claim "a Yang-Baxter step has zero
        // energy" — banned by §Strict Lean Discipline item 5, and reachable
        // here only because those two also carry an unused hypothesis.
        //
        // Deliberately narrow: ONLY a bare numeric literal under a single
        // ascription is stripped. Stripping ascriptions in general would make
        // genuine coercion lemmas look vacuous — `((n : ℕ) : ℤ) = n` is
        // `Nat.cast` content, not a tautology, and its inner side is not a
        // bare literal, so it is left alone.
        const unascribeLit = (s: string) => {
          const m = s.match(/^\((-?\d+(?:\.\d+)?)\s*:[^():]*\)$/);
          return m ? m[1] : s;
        };
        const nl = unascribeLit(lhs), nr = unascribeLit(rhs);
        if (nl && nl === nr && (nl !== lhs || nr !== rhs))
          return mk(d, "proof-no-trivial-true", "reflexive-tautology-ascribed-literal", false);
      }
      // (b) existential-over-True `: ∃ …, True` (e.g. `∃ v, True := sorry`,
      // the vol-through-tau dodge) and (c) a top-level `… ∨ True` / `True ∨ …`
      // disjunction (e.g. `hA.holds ∨ True`, the crystal-r-matrix dodge) —
      // both are tautologies asserting nothing. Paren-stripped so a `∨ True`
      // nested inside a real conjunct is not a false positive.
      if (/^∃.*\bTrue\s*$/.test(conclTA)) {
        return mk(d, "proof-no-trivial-true", "exists-true-tautology", false);
      }
      let bare = conclTA, prev = "";
      while (prev !== bare) { prev = bare; bare = bare.replace(/\([^()]*\)/g, ""); }
      if (/∨\s*True\b/.test(bare) || /\bTrue\s*∨/.test(bare)) {
        return mk(d, "proof-no-trivial-true", "or-true-tautology", false);
      }
      // (d) a CONJUNCTION of tautologies. The reflexive tests above read the
      // conclusion as a single proposition, so `(6 : ℕ) = 6 ∧ (0 : ℕ) = 0`
      // parses as lhs `(6:ℕ)` against rhs `6∧(0:ℕ)=0`, matches nothing, and
      // escapes every check — which is how `octonion_3_passes_sym2_gate`
      // shipped two tautologies as a representation-theoretic gate result
      // (found by reading, not by this scanner, 2026-08-09). Flag only when
      // EVERY conjunct is vacuous: one real conjunct makes the statement
      // assert something, and `1 + 5 = 6 ∧ 1 > 0` is arithmetic, not a
      // tautology, so its sibling `corpus_T1_fails_sym2_gate` stays unflagged.
      const conjuncts = splitTopLevelAnd(conclTA);
      if (conjuncts.length >= 2 && conjuncts.every((c) => reflexiveKind(c) !== null)) {
        return mk(d, "proof-no-trivial-true", "conjunction-of-tautologies", false);
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
// An *applied* SINGLE field, `ctx.classical_limit s t hst` — the one-field
// analogue of `APPLIED_TUPLE_PROJECTION` below, and blind for the same reason
// its comment gives: `PROJECTION_BODY` ends at the field name, so any argument
// after it kills the match. `detectSelfAssuming` then leaves `pat` undefined
// and RETURNS BEFORE reaching `projectionTypeMatchesConclusion`, the structural
// fallback that exists precisely to catch a projection whose field name escapes
// `CONCLUSION_FIELD`. The strongest check the detector has was unreachable for
// this shape.
//
// This is the subclass that matters, not a corner case: a class field carrying
// a conclusion is almost always `∀ … → …`, so the theorem MUST apply it to the
// binders to produce the conclusion. A self-assuming projection whose
// conclusion is universally quantified was therefore invisible BY
// CONSTRUCTION — and a universally quantified conclusion is the normal case.
//
// Measured on the QOU Lean tree (2871 .lean) when this was added:
// `proof-no-self-assuming-projection` 26 -> 42, i.e. 16 bodies the four earlier
// patterns could not see, every one of them passing the `CONCLUSION_FIELD` name
// gate. Found by fixing an instance the audit never reported —
// `QOU/BraidsKnots/mobius_frobenius_kernel.lean`, body
// `ctx.classical_limit s t hst`, whose class docstring read "All fields are
// inputs; none is the conclusion" while the conclusion was field three of
// three. Bean `qou-metc`; issue #7329.
//
// Deliberately conservative: each argument must be an identifier-ish token, so
// `ctx.foo (h.bar) x` does not match. Under-matching is the safe direction for
// a criterion at `critical` severity.
const APPLIED_PROJECTION =
  /^(?:by\s+exact\s+)?([a-z][\w']*)\.([A-Za-z_][\w']*)(?:\s+[A-Za-z_][\w'.]*)+\s*$/;
// An *applied*-field tuple `⟨ctx.impl_x ctx.active, ctx.impl_y ctx.active⟩`:
// each component is a field `word.field` optionally APPLIED to further
// `word[.field]` arguments. The `TUPLE_PROJECTION` regex above rejects the
// trailing argument, so these placeholder-canonical projections escaped the
// detector entirely (measured 2026-07-05: 0/99 corpus hits). Distinct name so
// they are tracked separately and never disturb the existing verbatim-tuple
// classification.
// Tight by design (per Copilot #3370): every `applied-tuple-projection` hit is
// auto-`exempt`, so an over-broad regex could silently downgrade an unrelated
// conjunction proof to tracked. Enforce BOTH (a) a single captured tuple prefix
// `\1` (e.g. `ctx`) shared across all components, and (b) ≥1 applied argument
// per component (`)+`). This matches exactly the placeholder pattern
// `⟨ctx.impl_x ctx.active, ctx.impl_y ctx.active, …⟩` and nothing looser — a
// fully-bare `⟨ctx.a, ctx.b⟩` is left to the verbatim `TUPLE_PROJECTION`
// branch. (Supersedes the looser symmetric-`*` suggestion — that would
// over-match.)
const APPLIED_TUPLE_PROJECTION =
  /^⟨\s*([a-z][\w']*)\.[A-Za-z_][\w']*(?:\s+[a-z][\w']*(?:\.[A-Za-z_][\w']*)?)+\s*(?:,\s*\1\.[A-Za-z_][\w']*(?:\s+[a-z][\w']*(?:\.[A-Za-z_][\w']*)?)+\s*)*⟩\s*$/;
// A `def`-kind declaration counts as a disguised provable claim when its
// conclusion type carries a logical connective / relation (i.e. it is a proof
// of a Prop, not a data definition). `detectSelfAssuming` skips `def` by
// default (`PROVABLE_KINDS`); this opts the Prop-valued ones in.
const PROP_CONCLUSION = /[∧↔∨∀∃≤≥¬≠]|=/;
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

/**
 * Binder variable → carrier type name, for every `[v : C …]` / `(v : C …)`
 * binder in a signature. This is what lets the type-match test below resolve
 * `ctx.foo` to the field `foo` of the class `C` that `ctx` inhabits.
 */
function binderCarriers(sig: string): Map<string, string> {
  const out = new Map<string, string>();
  for (const m of sig.matchAll(
    /[[(]\s*([a-z][\w']*)\s*:\s*([A-Z][\w'.]*)[^)\]]*[\])]/g,
  ))
    out.set(m[1], m[2]);
  return out;
}

/**
 * The structural discriminator the name gate approximates: does the projected
 * field's DECLARED TYPE match the theorem's CONCLUSION?
 *
 * `CONCLUSION_FIELD` is a *naming-convention* proxy for "this field is the
 * conclusion". It is high-precision but leaks badly: any field named outside
 * the convention is invisible however plainly it posits the conclusion (the
 * `confinement_ident` / `factorization_ident` escape in
 * `lean-proof-vacuity-audit.md` §8; measured at 84 corpus-wide in
 * `docs/audits/2026-08-09-self-assuming-projection-reanalysis.md`). This test
 * asks the question directly instead of guessing from the name.
 *
 * Comparison is character-exact after stripping the binder prefix (field types
 * are written bare inside the carrier; the conclusion writes them `ctx.foo`)
 * and collapsing whitespace. That is deliberately conservative — anything
 * needing real unification is NOT reported, so this under-counts rather than
 * over-counts.
 */
/**
 * Head-symbol aliases introduced by a file-local eta-expanded `abbrev`.
 *
 * `abbrev qIntSym (q : ℝ) (m : ℤ) : ℝ := QOU.QInteger.qIntBalZ q m` makes
 * `qIntSym q m` and `QOU.QInteger.qIntBalZ q m` the SAME term — an `abbrev` is
 * reducible, so a projection whose field type spells the qualified head still
 * typechecks against a conclusion that spells the alias. The character-exact
 * comparison below then reports no match, and a verbatim self-assuming
 * projection escapes.
 *
 * Measured instance: `QOU.BraidKnot.volume_perturbation` is
 * `:= ctx.perturbation_formula` — one field, returned verbatim — and was the
 * one member of bean `qou-octr`'s eight that this detector did not report,
 * solely because the class field says `QOU.QInteger.qIntBalZ` where the
 * theorem says `qIntSym`.
 *
 * Deliberately narrow: only an `abbrev` whose body is a dotted head applied to
 * its own binders, in order, is an alias. Anything else needs real unification
 * and stays out, per this detector's under-count-rather-than-over-count rule.
 */
function fileHeadAliases(decls: Decl[]): Map<string, string> {
  const out = new Map<string, string>();
  for (const d of decls) {
    if (!/^(noncomputable\s+)?abbrev\b/.test(d.kind)) continue;
    const binders: string[] = [];
    for (const m of d.sig.matchAll(/\(([^():]+):[^()]*\)/g)) {
      for (const n of m[1].trim().split(/\s+/)) if (n) binders.push(n);
    }
    if (binders.length === 0) continue;
    const body = d.body.trim().replace(/\s+/g, " ");
    const head = "([A-Za-z_][\\w'\\.]*)";
    const re = new RegExp(
      "^" + head + "\\s+" + binders.map((b) => b.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("\\s+") + "$",
    );
    const m = body.match(re);
    if (!m) continue;
    if (!m[1].includes(".")) continue; // an unqualified head is not an alias worth normalising
    out.set(m[1], d.name);
  }
  return out;
}

function projectionTypeMatchesConclusion(
  d: Decl,
  carriers: Map<string, Decl>,
  variable: string,
  fields: string[],
  aliases: Map<string, string>,
): boolean {
  const carrierName = binderCarriers(d.sig).get(variable);
  if (!carrierName) return false;
  const carrier = carriers.get(carrierName);
  if (!carrier) return false; // declared in another file — stay conservative
  // First declaration wins, and `name := value` assignment lines are dropped.
  // `DECL_START` requires a name after the keyword, so an ANONYMOUS
  // `instance : C where` (very common right below the class it instantiates)
  // starts no new decl — the class's `text` swallows the instance body, and
  // `classFields` then reads each `field := value` line as a re-declaration
  // whose "type" is `= value`. Last-wins would silently replace the real field
  // type with that, and the comparison below would miss a genuine projection.
  const table = new Map<string, string>();
  for (const f of classFields(carrier)) {
    if (/^=/.test(f.type.trim())) continue; // `field := value` from an instance body
    if (!table.has(f.name)) table.set(f.name, f.type);
  }
  const types = fields.map((f) => table.get(f));
  if (types.some((t) => t === undefined)) return false;
  const ws = (s: string) => {
    let t = s.replace(/\s+/g, " ").trim();
    // Normalise reducible `abbrev` aliases so a field spelling the qualified
    // head matches a conclusion spelling the alias (see `fileHeadAliases`).
    for (const [head, alias] of aliases) {
      t = t.split(head).join(alias);
    }
    return t;
  };
  const concl = conclusionTypeAscription(d.sig);
  if (!concl) return false;
  const nc = ws(concl.replace(new RegExp(`\\b${variable}\\.`, "g"), ""));
  if (types.length === 1) return ws(types[0]!) === nc;
  // A tuple splits a conjunction across one field per conjunct.
  const bare = ws(types.join(" ∧ "));
  return (
    bare === nc ||
    ws(types.map((t) => `(${t})`).join(" ∧ ")) === nc ||
    ws(bare.replace(/[()]/g, "")) === ws(nc.replace(/[()]/g, ""))
  );
}

function detectSelfAssuming(
  d: Decl,
  carriers: Map<string, Decl>,
  aliases: Map<string, string> = new Map(),
): Hit | undefined {
  const provable = PROVABLE_KINDS.test(d.kind);
  // A Prop-valued `def` is a disguised provable claim (§1a def-disguised); it
  // escaped detection because `detectSelfAssuming` only scanned the provable
  // kinds. Opt those in — a data `def` (no connective in its conclusion) stays
  // out. This is the primary corpus gap: 36/99 placeholder-canonical
  // projections are `def`-kind.
  const isDefProof =
    /^def\b/.test(d.kind) &&
    PROP_CONCLUSION.test(conclusionTypeAscription(d.sig) ?? "");
  if (!provable && !isDefProof) return undefined;
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
  } else if ((m = body.match(APPLIED_PROJECTION))) {
    field = m[2];
    pat = "applied-field-projection";
  } else if (TUPLE_PROJECTION.test(body)) {
    pat = "tuple-projection";
    field = body.match(/\.([A-Za-z_][\w']*)/)?.[1];
  } else if (APPLIED_TUPLE_PROJECTION.test(body)) {
    pat = "applied-tuple-projection";
    field = body.match(/\.([A-Za-z_][\w']*)/)?.[1];
  }
  if (!pat) return undefined;
  if (
    pat !== "tuple-projection" &&
    pat !== "applied-tuple-projection" &&
    field &&
    !CONCLUSION_FIELD.test(field)
  ) {
    // The field name escapes the convention — but the name was only ever a
    // proxy. Ask the structural question before dropping it: if the field's
    // declared type IS the conclusion, this is a self-assuming projection no
    // matter what it is called.
    //
    // Emitted EXEMPT (tracked-not-counted) on landing, mirroring the §3b
    // placeholder carve-out below: closing a 84-candidate blindspot must not
    // turn the vacuity CI gate red in the same commit that discovers it. The
    // point of tracking them is that EXEMPT hits still enter the review
    // ledger, so `--check-ledger` now demands an agent verdict on each.
    // Promoting these to hard failures is a deliberate follow-up.
    const projVar = body.match(/([a-z][\w']*)\.[A-Za-z_][\w']*/)?.[1];
    if (
      projVar &&
      projectionTypeMatchesConclusion(d, carriers, projVar, [field], aliases)
    ) {
      const h = mk(d, "proof-no-self-assuming-projection", pat, true);
      h.exempt_reason =
        "type-matched projection (field name escapes CONCLUSION_FIELD; tracked, triage pending)";
      h.detail =
        `the projected field \`${projVar}.${field}\` has a declared type ` +
        "character-identical to the conclusion — the theorem returns its own " +
        "claim. Named outside `CONCLUSION_FIELD`, so the name gate misses it.";
      return h;
    }
    return undefined;
  }
  // Newly-covered patterns (the def-disguised projections + applied-field
  // tuples) are the acknowledged §3b placeholder-canonical projections whose
  // docstrings honestly state the content is carried by the context-class
  // axioms with derivation pending (post-PR #3363). Emit them EXEMPT
  // (tracked-not-counted) so the coverage blindspot is closed WITHOUT turning
  // the vacuity CI gate red on ~99 files. Promoting these to a hard failure —
  // once the honest-placeholder vs. dishonest-dodge line is codified — is a
  // deliberate follow-up, not a silent side effect of closing the blindspot.
  //
  // NARROWED 2026-08-09: `isDefProof` no longer overrides a `CONCLUSION_FIELD`
  // name-gate match. The gate above runs FIRST but only *diverts* candidates
  // whose field name escapes the convention; a `def` whose field name the gate
  // MATCHES — `ctx.claim_yang_baxter`, `ctx.claim_pslq_independence` — fell
  // straight through to here and was exempted anyway. So the §3b carve-out was
  // swallowing the strongest signal the detector has: the author named the
  // field `claim_*`. A matched name means the projection is self-assuming on
  // the detector's own primary criterion, and the §3b deferral does not apply.
  // Recommendation 4 of `docs/audits/2026-08-09-honest-placeholder-criterion.md`.
  const nameGateMatched = !!field && CONCLUSION_FIELD.test(field);
  // NOTE the asymmetry between the two arms below: the first disjunct of the
  // second arm respects `nameGateMatched`, and `applied-field-projection` does
  // not. That is deliberate but narrow — the exemption is a LANDING
  // concession, not a judgement, and ALL 21 hits it covers match
  // `CONCLUSION_FIELD` (measured, not estimated — `claim_*` × 12, `*_holds`
  // × 6, `exists_*`, `*_iff`, `*_eq`). Not 14, which is what this comment said
  // before the names were run through the regex.
  // Exempting them therefore swallows the detector's strongest signal, which is
  // exactly what the 2026-08-09 narrowing above removed from the §3b carve-out.
  // What makes it safe rather than a re-introduction is the ledger: they are
  // seeded as `needs-agent`, and a `genuine` verdict promotes each one back to
  // a counted defect. If that ledger route is ever removed, remove this
  // exemption with it.
  if (pat === "applied-field-projection") {
    // EXEMPT on landing (#7332) so closing a coverage blindspot does not turn a
    // `critical` gate red in the commit that discovers it — but the wording is
    // load-bearing and #7332 got it wrong. `LEDGER_TRACKED_EXEMPT` keys on the
    // literal "triage pending"; the shared reason string USED TO say
    // "derivation pending", so every hit taking that arm was dropped at the
    // ledger-seeding site and never reached an agent. #7332's own comment
    // asserted the opposite — "the 16 it newly reaches still enter the review
    // ledger" — and measured, 0 of them did, and the population is 21 rather
    // than 16. Fixed for this arm in #7341 and for the arm below in the
    // follow-up (bean `qou-vh1o`); both now emit "triage pending".
    // "triage pending" here puts them in the ledger as `needs-agent`; an agent
    // `genuine` verdict then promotes that ONE candidate to a counted defect
    // (the `adjudicatedGenuine` path), which is the designed per-candidate
    // route rather than a blanket promotion.
    const h = mk(d, "proof-no-self-assuming-projection", pat, true);
    h.exempt_reason =
      "canonical §3b placeholder projection (tracked; triage pending)";
    return h;
  }
  if ((isDefProof && !nameGateMatched) || pat === "applied-tuple-projection") {
    // The last arm on the "derivation pending" wording, CLOSED here (bean
    // `qou-vh1o`, follow-up to #7341). Both arms now emit "triage pending", so
    // `LEDGER_TRACKED_EXEMPT` reaches every exempted self-assuming candidate
    // and none is exempted into silence. The 13 this seeds — 6
    // `applied-tuple-projection` and 7 `tuple-projection` arriving as `def`
    // proofs — were adjudicated before the wording moved, so the seeding turns
    // up no unadjudicated queue: 6 genuine, 6 advisory, 1 legit.
    //
    // They are NOT the applied-field tranche's defect class. Four shapes:
    // an ANTECEDENT-ASSERTING context (a free `Prop` field, a field asserting
    // it, and `impl_* : P -> conclusion`, with the theorem doing modus ponens
    // — the class supplies both premises); a conjunction of the class's own
    // fields; an accessor on an EXPLICIT structure argument, which is ordinary
    // mathematics and not a projection defect; and one instance of the correct
    // §3b-cond pattern.
    const h = mk(d, "proof-no-self-assuming-projection", pat, true);
    h.exempt_reason =
      "canonical §3b placeholder projection (tracked; triage pending)";
    return h;
  }
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

/**
 * The docstring asserts the body is a `sorry`. The body has none.
 *
 * Deliberately keyed on nothing but the doc block and the body — no field
 * name, no naming convention, so nothing an author calls a field can dodge it.
 * That is the point: `detectSelfAssuming` gates on `CONCLUSION_FIELD`, and
 * both live cases found on 2026-08-08 were named `*_ident` and slipped past.
 *
 * Present tense only. A docstring narrating history ("previously carried a
 * `sorry`", "the `sorry` is removed", "sorry-free") is describing the past or
 * the absence, not claiming the body has one, and must not fire.
 */
const DOC_CLAIMS_SORRY =
  /(?:body|proof|it)\s+is\s+(?:therefore\s+|thus\s+|an?\s+)*`?sorry`?|discharged\s+by\s+(?:an?\s+)?`?sorry`?|stated\s+(?:[^.\n]{0,60}?)\bwith\s+(?:an?\s+)?`?sorry`?|honest\s+`?sorry`?|carries\s+(?:an?\s+)?`?sorry`?/i;

/**
 * Phrases that make a `sorry` mention historical, negated, or hypothetical.
 * Checked on the SAME sentence as the match, not the whole doc block — a file
 * may legitimately say "sorry-free" about one declaration and claim a `sorry`
 * for another in the next paragraph.
 *
 * The second line is ATTRIBUTION TO SUPERSEDED TEXT, added 2026-09-03. This
 * corpus's house style, when a docstring is corrected, is to QUOTE the wording
 * it replaced — "the paragraph that stood here said …", "Until 2026-08-08 this
 * docstring said …", "the previous wording called this …". The quoted sentence
 * still contains a present-tense `sorry` claim, so without these the detector
 * fires on the correction itself and keeps firing forever.
 *
 * Measured on `main` b8d883189d: of the 5 findings then live, **4** were this
 * shape and only 1 (`shell_filling_rule`) was anything else. Note `previously`
 * was already here but `previous` was not, so "the previous wording" slipped
 * through on a suffix.
 *
 * The risk is over-suppression — a real claim in a sentence that happens to
 * mention an old one. `--selftest-docstring-sorry` guards it: the eight genuine
 * claims drained in PR #6471 must all still fire.
 */
const SORRY_MENTION_IS_HISTORICAL =
  /sorry-free|no\s+longer|previously|formerly|used\s+to|was\s+`?sorry`?|removed|not\s+a\s+`?sorry`?|no\s+`?sorry`?|instead\s+of|rather\s+than|modulo/i;

/**
 * Attribution to text this docstring has replaced — see the note above.
 * Kept separate from `SORRY_MENTION_IS_HISTORICAL` so the two can be measured
 * apart; `docstringSorryIsHistorical` is the only consumer of both.
 */
const SORRY_MENTION_QUOTES_SUPERSEDED =
  /previous\s+(?:wording|version|revision|encoding|paragraph|sentence|docstring)|(?:stood|read)\s+here|(?:docstring|wording|sentence|paragraph|header|note)\s+(?:said|read|called|claimed)|earlier\s+revision|until\s+\d{4}-\d{2}-\d{2}/i;

/** A `sorry` mention that does not assert this body is currently a `sorry`. */
function docstringSorryIsHistorical(sentence: string): boolean {
  return (
    SORRY_MENTION_IS_HISTORICAL.test(sentence) ||
    SORRY_MENTION_QUOTES_SUPERSEDED.test(sentence)
  );
}

/**
 * Wording that attributes the `sorry` to some OTHER declaration rather than to
 * this body — a sub-theorem, an inherited lemma, an upstream brick.
 *
 * This is NOT sufficient to exempt on its own. The first drain (2026-08-09)
 * found five declarations that delegated in exactly this language while the
 * delegated-to declaration had no `sorry` either — delegation is precisely
 * where an unproved claim goes unchecked. So the wording only *permits* an
 * exemption; `fileHasSorry` below has to supply the evidence.
 */
const DOC_DELEGATES_SORRY =
  /sub-?(theorem|lemma)|inherit|bricks?['’]?\s+own|named\s+sub|upstream|its\s+(own\s+)?cores?\b/i;

function detectDocstringSorryMismatch(
  d: Decl,
  doc: string,
  fileHasSorry: boolean,
): Hit | undefined {
  // Only declarations that *can* carry a proof body.
  const provable = PROVABLE_KINDS.test(d.kind);
  const isDefProof =
    /^def\b/.test(d.kind) &&
    PROP_CONCLUSION.test(conclusionTypeAscription(d.sig) ?? "");
  if (!provable && !isDefProof) return undefined;

  // The claim only bites if the body genuinely has no `sorry`.
  if (/\bsorry\b/.test(d.body)) return undefined;
  if (d.body.trim() === "") return undefined; // axiom/structure — nothing to check

  // Find a sentence that claims a `sorry` in the present tense.
  const sentences = doc.split(/(?<=[.!?])\s+|\n{2,}/);
  const claim = sentences.find(
    (s) => DOC_CLAIMS_SORRY.test(s) && !docstringSorryIsHistorical(s),
  );
  if (!claim) return undefined;

  // Evidence-gated delegation exemption. The claim points at another
  // declaration AND this file genuinely contains a `sorry` — so the prose is
  // plausibly true and the call is a judgement, not a defect. Tracked, not
  // counted. Without the `fileHasSorry` half this would be a wording exemption,
  // which the first drain proved unsafe.
  if (DOC_DELEGATES_SORRY.test(claim) && fileHasSorry) {
    const h = mk(d, "proof-docstring-sorry-mismatch", "doc-delegates-sorry", true);
    h.exempt_reason =
      "docstring attributes the `sorry` to another declaration and this file has one";
    return h;
  }

  const h = mk(d, "proof-docstring-sorry-mismatch", "doc-claims-sorry-body-has-none", false);
  h.detail =
    "docstring states the body is `sorry` but the body contains none — the prose and " +
    "`#print axioms` disagree about whether a proof exists. Check whether a class field " +
    "is being projected: this is how a self-assuming projection reads when the field name " +
    "escapes `CONCLUSION_FIELD`";
  return h;
}

/**
 * A `rfl`-proved statement carrying an explicit hypothesis it cannot use.
 *
 * `rfl` consults NO hypothesis — it proves the conclusion by definitional
 * unfolding alone. So a provable declaration whose body reduces to `rfl`,
 * and which binds an explicit `(h : …)` that does not occur in its own
 * conclusion, proves that conclusion for EVERY value of that hypothesis. The
 * hypothesis is decoration, and the statement is definitionally true rather
 * than a theorem (§Strict Lean Discipline item 8: it should be a `def`).
 *
 * The sharper consequence is about the DEFINITION, not the theorem: if
 * `f a = f b := rfl` holds with the relating hypothesis unused, then `f`
 * does not depend on that argument at all.
 *
 * Worked instance — `LevelSufficiency`
 * (`knots-particles-confinement/level-sufficiency.lean:72`): both hypotheses
 * are `_`-prefixed and the body is `rfl`, so `markovTrace P q = markovTrace
 * P' q` holds for ANY two particles and the covering condition is decoration.
 *
 * Why the existing detectors structurally miss it: there is no `sorry`, no
 * `axiom`, no `True` conclusion, and the body is not a `ctx.field`
 * projection, so `proof-no-self-assuming-projection` cannot match it however
 * its regexes are tuned.
 *
 * PRECISION (this is a high-recall candidate class, agent-confirmed like the
 * others, hence `major` rather than `critical`):
 *  - Only EXPLICIT `( … : … )` binders count. Instance `[…]`, implicit `{…}`
 *    and strict-implicit `⦃…⦄` binders can be load-bearing for elaboration
 *    even when the proof is `rfl`.
 *  - A binder whose name OCCURS IN THE CONCLUSION is used by the statement
 *    (e.g. `(h : P) : Q h = …`), so it is not decoration — skipped.
 *  - Binders that look like DATA rather than hypotheses (`(n : ℕ)`,
 *    `(q : ℝ)`) are skipped; a `rfl` over data is ordinary computation. Only
 *    Prop-shaped types (carrying a relation/connective) count.
 */
// Tactic separators in Lean 4 are `;` OR a newline, so both must be accepted:
// `strangelet_double_beta` writes `by\n  unfold double_beta_rate\n  rfl` and was
// missed by a `;`-only pattern.
const RFL_BODY =
  /^(?:rfl|by\s+rfl|by\s+(?:unfold|delta|show|simp\s+only|with_unfolding_all|intros?)\b[^;\n]*[;\n]\s*rfl)\s*$/;
/**
 * The same blindness, wearing an existential.
 *
 * `∃ a, a = e` proved `⟨_, rfl⟩` consults no hypothesis either — the witness
 * is handed over and `rfl` closes the equation. `RFL_BODY` never matched it
 * because the body is an anonymous constructor rather than the token `rfl`,
 * so a statement could bind any number of decorative hypotheses and stay
 * invisible to this detector. Ten such declarations sat in
 * `docs/audits/2026-08-07-lean-vacuous-existential-audit.json` — found by the
 * standalone `scripts/lean-vacuous-existential-audit.py`, flagged by nothing
 * that gates.
 *
 * Whitespace is collapsed before matching, so the `by`-block form
 * (`by\n  exact ⟨.borromean, rfl⟩`) is covered by the same pattern.
 */
const ANON_RFL_BODY = /^(?:by\s+exact\s+)?⟨[^⟨⟩]*,\s*rfl⟩$/;
/** A binder type that looks like a proposition rather than data. */
const PROP_SHAPED = /[=≤<≥>≠∈∣]|↔|→|∧|∨|¬|Odd\b|Even\b|Prime\b/;

const BINDER_OPEN: Record<string, string> = {
  "(": ")",
  "{": "}",
  "[": "]",
  "⦃": "⦄",
};

interface Binder {
  names: string[];
  type: string;
  /** `(…)` — the only kind whose non-use is evidence of decoration. */
  explicit: boolean;
}

/**
 * Every binder in a signature head, at any nesting depth.
 *
 * Replaces a regex that admitted exactly ONE level of parentheses inside a
 * binder's type:
 *
 *     /\(\s*([^():]+?)\s*:\s*([^()]*(?:\([^()]*\)[^()]*)*)\)/g
 *
 * A hypothesis nesting two deep did not match, so the binder was **dropped
 * silently** — indistinguishable, in the output, from a signature that binds
 * nothing. `knot_factor_amphicheiral` (`QOU/BraidKnot/KnotFactorAmphicheiral.lean`)
 * is the case that exposed it: its `_off_block_norm` hypothesis is
 *
 *     (β.partitions.toList.filter (· ≠ altPartition)).foldl
 *       (fun acc μ => acc + β.weight μ * (β.c μ / β.trivial μ) ^ 2) 0
 *     = 1 - β.weight altPartition
 *
 * — `(β.c μ / β.trivial μ)` inside `(fun acc μ => …)` is two deep. The binder
 * was invisible, so `proof-no-unused-hypothesis-rfl` reported nothing on a
 * declaration proved `⟨_, rfl⟩` with an underscored unused hypothesis: the
 * exact shape it exists to catch.
 *
 * The bias is not neutral. It ran against the most elaborate statements,
 * which are the ones most likely to be hiding a tautology behind
 * decoration. `scripts/lean-self-assuming-audit.py` carried the identical
 * defect and was fixed the same way (bean `qou/q407`, 2026-08-21); the two
 * implementations reached it independently, which is the argument for
 * balanced scanning over regex here rather than a wider regex.
 */
function parseBinders(head: string): Binder[] {
  const out: Binder[] = [];
  let i = 0;
  while (i < head.length) {
    const close = BINDER_OPEN[head[i]];
    if (!close) {
      i++;
      continue;
    }
    // Scan to the matching closer, counting every delimiter kind.
    const open = head[i];
    let depth = 0;
    let j = i;
    for (; j < head.length; j++) {
      const c = head[j];
      if (BINDER_OPEN[c]) depth++;
      else if (c === ")" || c === "}" || c === "]" || c === "⦄") {
        depth--;
        if (depth === 0) break;
      }
    }
    if (j >= head.length) break; // unbalanced — stop rather than guess
    const inner = head.slice(i + 1, j);
    i = j + 1;
    // Split at the FIRST `:` outside any nested group; `:=` and `::` are not it.
    let d2 = 0;
    let colon = -1;
    for (let k = 0; k < inner.length; k++) {
      const c = inner[k];
      if (BINDER_OPEN[c]) d2++;
      else if (c === ")" || c === "}" || c === "]" || c === "⦄") d2--;
      else if (c === ":" && d2 === 0 && inner[k + 1] !== "=" && inner[k - 1] !== ":") {
        colon = k;
        break;
      }
    }
    if (colon < 0) continue; // `[Field R]`-style anonymous instance binder
    const names = inner
      .slice(0, colon)
      .trim()
      .split(/\s+/)
      .filter((n) => /^_?[a-zA-Z_][\w']*$/.test(n) || n === "_");
    if (names.length === 0) continue;
    out.push({
      names,
      type: inner.slice(colon + 1).replace(/\s+/g, " ").trim(),
      explicit: open === "(",
    });
  }
  return out;
}

/**
 * `-- vacuous-by-design: <reason>` immediately above a declaration.
 *
 * Some vacuous statements are deliberate and the vacuity IS the content —
 * `qou_standardPart_image_exists` (`QOU/AppendixSurreals/Conjectures.lean`)
 * records that a conjunct of the original `VacuumEpsilon` conjecture was
 * provable for every `SQ`, so the surviving conjecture asserts only what is
 * irreducibly open, and it is *used* to rebuild the wider statement.
 *
 * Such a hit is emitted EXEMPT — tracked, in the ledger, never dropped. A
 * check that silently excuses cases is indistinguishable from one that never
 * ran, which is the defect class this whole scanner is for. The marker must
 * carry a reason; a bare mute is not honoured.
 *
 * Only the contiguous run of `--` lines, attributes and blanks directly above
 * the declaration is searched, so a marker cannot drift onto a neighbour.
 * Kept byte-identical in meaning to the `VACUOUS_OK` marker in
 * `scripts/lean-self-assuming-audit.py` so the two agree on the corpus.
 */
function vacuousByDesign(origLines: string[], startLine: number): string | undefined {
  for (let i = startLine - 2; i >= 0; i--) {
    const t = (origLines[i] ?? "").trim();
    if (t === "" || t.startsWith("@[")) continue;
    if (!t.startsWith("--")) return undefined;
    const m = t.match(/--\s*vacuous-by-design:\s*(\S.*?)\s*$/);
    if (m) return m[1];
  }
  return undefined;
}

function detectUnusedHypothesisRfl(d: Decl): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  const body = d.body.trim();
  const collapsed = body.replace(/\s+/g, " ").trim();
  const anon = ANON_RFL_BODY.test(collapsed);
  if (!RFL_BODY.test(body) && !anon) return undefined;
  const concl = conclusionTypeAscription(d.sig);
  if (!concl) return undefined;

  // Explicit binders only, from the head up to the conclusion `:`.
  const head = d.sig.slice(0, d.sig.length - concl.length);
  const unused: string[] = [];
  for (const b of parseBinders(head)) {
    if (!b.explicit) continue; // `[…]` / `{…}` / `⦃…⦄` can be load-bearing
    const names = b.names;
    const ty = b.type;
    if (!PROP_SHAPED.test(ty)) continue; // data binder, not a hypothesis
    for (const n of names) {
      if (!/^_?[a-zA-Z_][\w']*$/.test(n)) continue;
      // Used by the statement itself? then it is not decoration.
      if (n !== "_" && new RegExp(`(^|[^\\w'])${n}([^\\w']|$)`).test(concl)) continue;
      // Used by the PROOF? A bare `rfl` mentions nothing, but an anonymous
      // constructor supplies a witness that can be built from a hypothesis
      // (`⟨h.choose, rfl⟩`), and then the binder is load-bearing. Checking
      // the body is a no-op for the `rfl` shapes and required for this one.
      if (n !== "_" && new RegExp(`(^|[^\\w'])${n}([^\\w']|$)`).test(body)) continue;
      unused.push(n);
    }
  }
  if (unused.length === 0) return undefined;
  // `_`-prefixed names are the author explicitly recording non-use — the
  // strongest form of the signal, and worth distinguishing in the witness.
  const pat = anon
    ? unused.every((n) => n.startsWith("_"))
      ? "rfl-witness-with-underscored-hypothesis"
      : "rfl-witness-with-unused-hypothesis"
    : unused.every((n) => n.startsWith("_"))
      ? "rfl-with-underscored-hypothesis"
      : "rfl-with-unused-hypothesis";
  const h = mk(d, "proof-no-unused-hypothesis-rfl", pat, false);
  h.detail =
    `proof is \`${body}\`, which uses no hypothesis, yet the statement binds ` +
    `${unused.map((n) => `\`${n}\``).join(", ")} — absent from the conclusion, so ` +
    `the claim holds for every value of ${unused.length > 1 ? "them" : "it"}`;
  return h;
}

/**
 * Split a proposition into its `∀`-telescope, its arrow hypotheses, and the
 * final conclusion.
 *
 * `detectUnusedHypothesisRfl` above scans only *parenthesised binders before
 * the colon* (`theorem foo (h : P) : C`). A statement can carry exactly the
 * same decoration inside its type instead —
 *
 *     theorem foo : ∀ (p : ℕ), Odd p → ∀ (s : R_q), s ≠ 0 → C p
 *
 * — and then `head` is empty, nothing is scanned, and no hit is possible.
 * That is the shape this splitter exists to expose.
 *
 * Scanning is bracket-aware, so an arrow inside `(a → b)` or a comma inside
 * `(x : Fin (n, m))` does not terminate a segment. The iteration bound is a
 * guard against pathological input, not a semantic limit.
 */
function telescopeParts(ty: string): {
  bound: string[];
  hyps: string[];
  concl: string;
} {
  const OPEN = "([{⦃";
  const CLOSE = ")]}⦄";
  const bound: string[] = [];
  const hyps: string[] = [];
  let rest = ty.trim();
  for (let guard = 0; guard < 64; guard++) {
    rest = rest.trim();
    if (rest.startsWith("∀")) {
      let depth = 0;
      let i = 1;
      for (; i < rest.length; i++) {
        const c = rest[i];
        if (OPEN.includes(c)) depth++;
        else if (CLOSE.includes(c)) depth--;
        else if (c === "," && depth === 0) break;
      }
      const binderText = rest.slice(1, i);
      // Grouped binders `(x y : T)` / `{x : T}` / `[inst]`.
      for (const m of binderText.matchAll(
        /[({[⦃]\s*([^:()[\]{}⦃⦄]+?)\s*:[^)}\]⦄]*[)}\]⦄]/g,
      )) {
        for (const n of m[1].trim().split(/\s+/)) {
          if (/^_?[a-zA-Z_][\w']*$/.test(n)) bound.push(n);
        }
      }
      // Bare binders `∀ n, …` (no parentheses, no ascription).
      const bare = binderText.replace(/[({[⦃][^)}\]⦄]*[)}\]⦄]/g, " ");
      for (const n of bare.trim().split(/\s+/)) {
        if (n && /^_?[a-zA-Z_][\w']*$/.test(n)) bound.push(n);
      }
      rest = rest.slice(i + 1);
      continue;
    }
    let depth = 0;
    let arrow = -1;
    for (let i = 0; i < rest.length; i++) {
      const c = rest[i];
      if (OPEN.includes(c)) depth++;
      else if (CLOSE.includes(c)) depth--;
      else if (c === "→" && depth === 0) {
        arrow = i;
        break;
      }
    }
    if (arrow >= 0) {
      hyps.push(rest.slice(0, arrow).trim());
      rest = rest.slice(arrow + 1);
      continue;
    }
    break;
  }
  return { bound, hyps, concl: rest.trim() };
}

/**
 * The telescope twin of `detectUnusedHypothesisRfl`.
 *
 * A `rfl`-closed theorem consults no hypothesis, so anything its *type*
 * quantifies over is decoration: the claim holds for every value of it. When
 * the decoration sits in a `∀`-telescope rather than in named binders, the
 * older detector cannot see it.
 *
 * Worked instance (bean `qou-wcff`), which every checker missed:
 *
 *     theorem chebyshev_degree_eq_genus :
 *         ∀ (p : ℕ), Odd p → 2 ≤ p → ∀ (s : R_q), s ≠ 0 →
 *         seifertGenus_T2p p = (p - 1) / 2 := by
 *       intros; rfl
 *
 * `s` and all three hypotheses are absent from the conclusion, which unfolds
 * to `(p-1)/2 = (p-1)/2`. It escaped on two counts: `RFL_BODY` did not list
 * `intros`, and the binders were not where the scan looked. Both are fixed
 * here — this is a recall gap, not a one-off.
 */
function detectTelescopeVacuousRfl(d: Decl): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  const body = d.body.trim();
  const collapsed = body.replace(/\s+/g, " ").trim();
  if (!RFL_BODY.test(collapsed)) return undefined;
  const ty = conclusionTypeAscription(d.sig);
  if (!ty || !/∀|→/.test(ty)) return undefined;
  const { bound, hyps, concl } = telescopeParts(ty);
  if (!concl) return undefined;
  const occurs = (n: string, s: string) =>
    new RegExp(
      `(^|[^\\w'])${n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}([^\\w']|$)`,
    ).test(s);
  const unused = bound.filter(
    (n) => n !== "_" && !occurs(n, concl) && !occurs(n, body),
  );
  // A `rfl` body discharges no hypothesis, so a surviving arrow hypothesis is
  // as much decoration as an unused ∀-binder. Either alone is a candidate.
  if (unused.length === 0 && hyps.length === 0) return undefined;
  const pat =
    unused.length > 0
      ? "rfl-with-unused-telescope-binder"
      : "rfl-with-discarded-telescope-hypothesis";
  const h = mk(d, "proof-no-unused-hypothesis-rfl", pat, false);
  const parts: string[] = [];
  if (unused.length > 0) {
    parts.push(
      `quantifies over ${unused.map((n) => `\`${n}\``).join(", ")}, absent from the conclusion`,
    );
  }
  if (hyps.length > 0) {
    parts.push(
      `assumes ${hyps.length} hypothes${hyps.length > 1 ? "es" : "is"} ` +
        `(${hyps.map((x) => `\`${x}\``).join(", ")})`,
    );
  }
  h.detail =
    `proof is \`${collapsed}\`, which consults no hypothesis, yet the type ` +
    `${parts.join(" and ")} — so the claim reduces to \`${concl}\` and holds ` +
    `regardless`;
  return h;
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

/**
 * Tactics that introduce a hypothesis or open a case. Their presence means a
 * contradiction below them is *local* — an eliminated branch, or a negation
 * being assumed in order to be refuted — and so says nothing about whether the
 * statement's own premises are satisfiable.
 */
const LOCAL_CONTEXT_TACTIC =
  /(^|[^\w'])(intro|rintro|rcases|obtain|cases|match|by_contra|induction|interval_cases|fin_cases|refine|constructor|exfalso|suffices|rsuffices|subst|letI|fun)\b|(^|\n)\s*[·|]/;

/** A conclusion that *is* a negation: proving it means deriving a contradiction. */
const NEGATIVE_CONCLUSION = /¬|≠|\bFalse\b/;

/**
 * The *whole body* is the contradiction — nothing else is proved. A nested
 * `absurd` (inside a `letI`, a `fun … =>` argument, a `have`) is a sub-proof
 * discharging some side condition, not the goal.
 */
const WHOLE_BODY_DISCHARGE =
  /^(?:by\s+)?(?:exact\s+)?(?:absurd\b|Nat\.not_lt_zero\b|\(.*\bby\s+(?:norm_num|omega)\b.*\)\.elim\b)/;

function detectFalsePremise(d: Decl): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  const body = d.body;
  const discharges =
    /\babsurd\b[\s\S]*?\bby\s+(norm_num|decide|simp|omega)\b/.test(body) ||
    /\bNat\.not_lt_zero\b/.test(body) ||
    // Tolerates a type ascription inside the parens — `(by norm_num : ¬P).elim h`
    // is the same discharge as `(by norm_num).elim h`, and the tighter original
    // spelling silently missed it.
    /\(.*\bby\s+(?:norm_num|omega)\b.*\)\.elim\b/.test(body);
  if (!discharges) return undefined;

  // A contradiction *inside a proof* is not the defect this criterion names.
  // The defect is a VACUOUS STATEMENT — the theorem's own binders are
  // unsatisfiable, so the goal falls straight out of `absurd` with nothing
  // else to do:  `theorem foo (h : 0 = 1) : P := absurd h (by norm_num)`.
  //
  // Deriving a contradiction is also how one proves a negation, and how one
  // kills an impossible branch of a case split. Both are idiomatic and carry
  // the real content of the proof. Flagging them on the bare `absurd` made
  // this criterion 0-for-56 across the corpus (agent adjudication 2026-08-09:
  // every candidate `legit` — negation goals, `interval_cases` branches,
  // empty-`Finset` arguments, and `letI` discharges of `i ≠ j` from
  // `M i j = 3` against `M i i = 1`). The three conditions below are what the
  // vacuity claim actually requires.
  if (!WHOLE_BODY_DISCHARGE.test(body.trim().replace(/\s+/g, " "))) return undefined;
  if (LOCAL_CONTEXT_TACTIC.test(body)) return undefined;
  const concl = conclusionTypeAscription(d.sig);
  if (NEGATIVE_CONCLUSION.test(concl)) return undefined;

  // The discharged term must be one of the statement's own hypotheses — a
  // contradiction built from locally-derived facts is a proof step, not a
  // property of the premises.
  const head = d.sig.slice(0, d.sig.length - concl.length);
  const binders: string[] = [];
  for (const m of head.matchAll(
    /[({\[⦃]\s*([^(){}\[\]:]+?)\s*:\s*([^(){}]*(?:\([^()]*\)[^(){}]*)*)[)}\]⦄]/g,
  )) {
    if (!PROP_SHAPED.test(m[2])) continue; // data binder, not a hypothesis
    for (const n of m[1].trim().split(/\s+/)) {
      if (/^_?[a-zA-Z_][\w']*$/.test(n)) binders.push(n);
    }
  }
  // The body *is* the discharge (checked above), so any hypothesis it names is
  // what the contradiction is built from — whether as `absurd h …`, `h.elim`,
  // or the argument in `(…).elim h`.
  const dischargedBinder = binders.find((n) =>
    new RegExp(`(?:^|[^\\w'])${n}(?:[^\\w']|$)`).test(body),
  );
  if (!dischargedBinder) return undefined;

  const h = mk(d, "proof-no-false-premise", "discharged-impossible-hyp", false);
  h.detail =
    `the entire goal is discharged by contradiction from the statement's own ` +
    `hypothesis \`${dischargedBinder}\`, with no \`intro\` and no case split — so the ` +
    `premises are unsatisfiable and the claim holds vacuously`;
  return h;
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

/**
 * Exemption reasons that still owe an agent verdict. An exemption normally
 * *is* the verdict, so exempt hits sit outside the `--check-ledger`
 * agent-inspection gate; these ones explicitly defer the call instead of
 * making it, so they must remain inside it.
 */
const LEDGER_TRACKED_EXEMPT = /triage pending/;

/** Default location of the agent-inspection review ledger. */
const DEFAULT_REVIEW_LEDGER = "docs/audits/lean-vacuity-review-ledger.json";

/**
 * Keys the review ledger has already adjudicated `genuine`.
 *
 * A `triage pending` exemption is a promise, not a verdict: it says a human
 * call is still owed (see `LEDGER_TRACKED_EXEMPT` and the emit sites, which
 * describe promotion to a hard failure as "a deliberate follow-up"). Once an
 * agent has recorded `genuine` for that key, the promise has been kept and the
 * heuristic is superseded — so the hit must count.
 *
 * Without this, an adjudicated defect stays suppressed from `total_defects`
 * forever, and the committed artifact reads as a smaller backlog than the
 * ledger records. Measured on 2026-08-22: `total_defects` 53 against 123
 * ledger-`genuine`, because **76** confirmed defects were still exempt under
 * the single reason "type-matched projection (field name escapes
 * CONCLUSION_FIELD; tracked, triage pending)". Bean `qou-v4ht`.
 *
 * Only `genuine` promotes. `legit` and `advisory` are verdicts that the hit is
 * NOT a defect, so they leave the exemption in place.
 */
function loadAdjudicatedGenuine(ledgerRel: string): Set<string> {
  const out = new Set<string>();
  const p = resolve(REPO_ROOT, ledgerRel);
  if (!existsSync(p)) return out;
  try {
    const r = JSON.parse(readFileSync(p, "utf-8"));
    for (const [key, e] of Object.entries(
      (r?.entries ?? {}) as Record<string, { verdict?: string }>,
    ))
      if (e?.verdict === "genuine") out.add(key);
  } catch {
    /* unreadable ledger: promote nothing, behave exactly as before */
  }
  return out;
}

// ── Statement-shape vacuity: the two shapes the standalone Python sweep
//    finds and nothing in this pipeline gated on (bean `qou/q407`).
//
//    `proof-no-unused-hypothesis-rfl` above needs an *unused explicit
//    Prop-shaped binder*. That is a good tell, but it is a property of the
//    decoration, not of the claim. A statement with no hypotheses at all —
//    `knot_factor_spectral_form`, `habiro_integral`, `q_0_well_defined` —
//    can be a pure tautology and bind nothing, and then there is no unused
//    binder to notice. Measured 2026-08-21: over the six pre-fix files
//    holding eleven such declarations this scanner reported **zero**.

/** `⟨e, rfl⟩` or `⟨_, rfl⟩`, optionally behind `by exact`. */
const ANON_REFL_WITNESS = /^(?:by\s+)?(?:exact\s+)?⟨\s*(.+?)\s*,\s*rfl\s*⟩$/;
/** `∃ x, body` / `∃ x : T, body` — a single leading binder. */
const EXISTS_HEAD = /^∃\s*([A-Za-z_][\w']*)\s*(?::([^,]*))?,\s*([\s\S]+)$/;

/** `(lhs, rhs)` of the first `=` outside every bracket group, or undefined. */
function splitTopLevelEq(body: string): [string, string] | undefined {
  let depth = 0;
  for (let i = 0; i < body.length; i++) {
    const c = body[i];
    if (BINDER_OPEN[c] || c === "⟨") depth++;
    else if (c === ")" || c === "}" || c === "]" || c === "⦄" || c === "⟩") depth--;
    else if (c === "=" && depth === 0) {
      if (":<>!=".includes(body[i - 1] ?? "") || body[i + 1] === "=") continue;
      return [body.slice(0, i).trim(), body.slice(i + 1).trim()];
    }
  }
  return undefined;
}

/**
 * `∃ x, e = x := ⟨e, rfl⟩` — true for every `e`, so it asserts nothing.
 *
 * "Well-defined" is not a theorem in a total type theory: naming the value of
 * a total expression is a property of the ambient type being inhabited. The
 * corpus carried sixteen of these, six of them `lean.ref` targets, all
 * sorry-free and axiom-clean.
 *
 * `⟨_, rfl⟩` counts and is the stronger tell — the author did not name the
 * witness at all; the elaborator recovered it by unifying `rfl`. Requiring a
 * spelled-out witness is what kept `knot_factor_amphicheiral` out of the
 * standalone sweep while its unreferenced sibling thirteen lines below was
 * reported.
 */
function detectTrivialExistential(
  d: Decl,
  origLines: string[],
): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  const m = d.body.trim().replace(/\s+/g, " ").match(ANON_REFL_WITNESS);
  if (!m) return undefined;
  const em = conclusionTypeAscription(d.sig).replace(/\s+/g, " ").trim().match(EXISTS_HEAD);
  if (!em) return undefined;
  const wit = m[1].trim();
  const [v, body] = [em[1], em[3].trim()];
  let witness: string | undefined;
  if (body === `${wit} = ${v}` || body === `${v} = ${wit}`) witness = wit;
  else if (wit === "_") {
    const sides = splitTopLevelEq(body);
    if (!sides) return undefined;
    const [lhs, rhs] = sides;
    const mentions = (s: string) =>
      new RegExp(`(^|[^\\w'])${v}([^\\w']|$)`).test(s);
    if (lhs === v && !mentions(rhs)) witness = rhs;
    else if (rhs === v && !mentions(lhs)) witness = lhs;
  }
  if (witness === undefined) return undefined;
  const why = vacuousByDesign(origLines, d.startLine);
  const h = mk(d, "proof-no-trivial-true", "trivial-existential", !!why);
  if (why) h.exempt_reason = `vacuous-by-design: ${why}`;
  h.detail =
    `concludes \`∃ ${v}, … = ${v}\` and proves it \`⟨${wit}, rfl⟩\` — the ` +
    `witness IS the expression, so the statement holds for every value of ` +
    `\`${snip(witness)}\` and says nothing about it`;
  return h;
}

/** A proof term that is a bare hypothesis reference. */
const BARE_IDENT = /^[A-Za-z_][\w'.!?]*$/;
const EXACT_IDENT = /^by\s+exact\s+([A-Za-z_][\w'.!?]*)$/;
const BY_ASSUMPTION = /^by\s+assumption$/;

/**
 * `theorem name … (h : P) … : P := h` — the hypothesis IS the conclusion.
 *
 * Distinct from `detectSelfAssuming`, which matches a projection out of a
 * *class field* (`ctx.claim_foo`). Here the conclusion is echoed straight
 * back from a binder, so there is no field name for `CONCLUSION_FIELD` to
 * gate on and no carrier to resolve. `by exact h` and `by assumption` are the
 * same term wearing a tactic block.
 *
 * The comparison is on whitespace-normalised text, which is conservative in
 * the right direction: a genuine re-statement that differs by so much as a
 * parenthesis is not reported.
 */
function detectBinderEcho(d: Decl, origLines: string[]): Hit | undefined {
  if (!PROVABLE_KINDS.test(d.kind)) return undefined;
  const proof = d.body.trim().replace(/\s+/g, " ").trim();
  if (!proof || proof.length > 200) return undefined;
  const concl = conclusionTypeAscription(d.sig).replace(/\s+/g, " ").trim();
  if (!concl) return undefined;
  const head = d.sig.slice(0, d.sig.length - conclusionTypeAscription(d.sig).length);
  const binders = parseBinders(head);
  let hyp: string | undefined;
  const named = proof.match(EXACT_IDENT)?.[1] ?? (BARE_IDENT.test(proof) ? proof : undefined);
  if (named) {
    for (const b of binders)
      if (b.names.includes(named) && b.type === concl) hyp = named;
  } else if (BY_ASSUMPTION.test(proof)) {
    for (const b of binders)
      if (b.type === concl) hyp = b.names[0];
  }
  if (!hyp) return undefined;
  const why = vacuousByDesign(origLines, d.startLine);
  const h = mk(d, "proof-no-self-assuming-projection", "binder-echo", !!why);
  if (why) h.exempt_reason = `vacuous-by-design: ${why}`;
  h.detail =
    `binds \`(${hyp} : ${snip(concl)})\` and concludes the same proposition, ` +
    `returning it verbatim — the statement stays true if every definition it ` +
    `mentions is swapped`;
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
  // A docstring that simply *announces* itself as a conjecture is a carrier.
  //
  // Measured 2026-08-29: without this clause the gate rejected every carrier
  // whose docstring is a bare `**CONJECTURE.** …` with no `conj:` label and no
  // "axiomatis" wording -- among them `QuantumLanglandsDual`,
  // `Mirror3d3dCorrespondence`, `LusztigCanonicalBasisQEq1`, `SpinFromSo3Fiber`
  // and `PoincareLefschetzBorromean`, all five of which carry the content-free
  // `holds : Prop`. Because the gate runs before every criterion in this
  // family, those carriers were invisible to `proof-claims-unencoded`,
  // `proof-no-empty-prop-carrier` AND
  // `proof-dependent-conjecture-not-conditional` alike, and none had ever
  // reached the review ledger. The audit could not see the carriers most
  // likely to be defective.
  const announcesConjecture = /\*\*\s*conjecture\b|^\s*conjecture[.:]/im.test(doc);
  const hasConjRef = /conj:[a-z0-9-]+/i.test(doc) || /\\label\{conj:/i.test(doc);
  const axiomatises = /axiomatis/i.test(doc) || announcesConjecture;
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
  // 🛑 The equality alternative was `\b=\b`, which CANNOT MATCH A LEAN
  // EQUATION.  `=` is not a word character, so `\b` on either side of it
  // requires an adjacent word character — i.e. it matches `a=b` and nothing
  // else.  Every equation written the way Lean is actually written,
  // `hh0 = 0`, read as NOT Prop-bearing.
  //
  // Measured 2026-09-13: all four live `docstring-claims-gap` hits were
  // FALSE POSITIVES caused by this.  `QOUCohomology` was reported "only 0
  // encoded" against `observability : hh0 = 0` and `frobeniusHopf_duality :
  // hh2 = 1` — both of its enumerated properties, both properly encoded.
  // `CategoricalReebDerivation` likewise, against `reeb_normalizes : reeb ≫
  // contact = contact` and `reeb_periodic : reeb ^ period = 1`, which its
  // docstring explicitly says are "encoded as fields below".
  //
  // An equation is the commonest way to encode a property in this corpus, so
  // the criterion was blind to the majority of the evidence it exists to
  // weigh — and it told agents to "encode" carriers that already had.
  //
  // The replacement matches `=` as a RELATION: not `:=` (a default value),
  // not `==`, not `=>`, and not the tail of `≠` (which the caller filters
  // separately).  Verified against the alternatives it does not touch: of a
  // 23-case corpus sample only 7 verdicts change, all of them equations, and
  // no non-proposition flips.  `ℕ → ℝ` and `Prop := True` match here for
  // unrelated reasons (`→`, `True`) and did so before this change too.
  return /[∀∃]|↔|(?<![-=])→|≤|≥|(?<![:<>=!])<|(?<![-:<>=!])>|≠|(?<![:!<>=≠])=(?![=>])|\bTrue\b|\bFalse\b/
    .test(type);
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
  //
  // A `class`/`structure` ascribed `: Prop` can only have Prop fields — Lean's
  // elaborator enforces it — so on such a carrier EVERY field is a
  // proposition and the syntactic sniff below is both unnecessary and wrong.
  //
  // 🛑 Measured 2026-09-13, this was the second of two blind spots that made
  // every live `docstring-claims-gap` hit a false positive.  A field whose
  // type is a NAMED PREDICATE applied to arguments carries no relational
  // operator, so `isPropBearingType` cannot see it:
  //
  //   FaddeevPhiPhysical    instStripGrowth : FaddeevPhiStripGrowth (substrateB t) Φ
  //                         hNF             : MeromorphicNFOn Φ Set.univ
  //   HasCategoricalIrreducibility
  //                         form_mono       : CategoryTheory.Mono (ι ≫ ∫_A)
  //
  // All three are genuine propositions, properly encoding exactly the
  // properties their docstrings enumerate; the first carrier was reported
  // "only 0 encoded" against two such fields.  Nothing distinguishes
  // `Mono f` from `Option R` by shape alone without elaborating it, so the
  // sort of the carrier is the sound discriminator rather than a heuristic.
  //
  // The count comparison still bites on a `: Prop` carrier: a docstring
  // naming two properties over a one-field class still fires.  What no
  // longer happens is a correctly-encoded carrier being told to encode.
  //
  // LIMITATION, stated rather than papered over: on a carrier that is NOT
  // `: Prop` — a `Type`-valued class — a named-predicate field remains
  // invisible to `isPropBearingType`, so this criterion can still
  // under-count there.  Fixing that needs elaboration, not regex.
  // `declSort` returns everything after the head's top-level `:`, which for a
  // `… : Prop where` carrier is `"Prop where\n"` followed by the entire field
  // block — so a bare `=== "Prop"` never matches one.  Cut at `where` (or the
  // end of the line) to get the sort itself.
  const allFieldsAreProps =
    declSort(d).split(/\bwhere\b|\n/)[0].trim() === "Prop";
  const encoded = fields.filter(
    (f) =>
      (allFieldsAreProps || isPropBearingType(f.type)) &&
      !/^[^=<>≤≥∀∃↔]*≠/.test(f.type),
  ).length;
  if (encoded >= claimed) return undefined;
  const h = mk(d, "proof-claims-unencoded", "docstring-claims-gap", false);
  h.detail = `doc enumerates ${claimed} propert${
    claimed === 1 ? "y" : "ies"
  } (${bullets.join(", ")}); only ${encoded} encoded as Prop field(s)`;
  return h;
}

/** A `class`/`structure` field whose type is literally `True` (or a
 * conjunction of `True`s, or a `Prop`/`… := True` default) carries **zero**
 * content — any instance satisfies it, so a downstream consumer that uses the
 * field as a hypothesis assumes nothing. This is the field-level analogue of a
 * `: True` conclusion and is the gap the empty-prop-carrier (zero-field) and
 * claims-unencoded (≥2 enumerated bullets) detectors both structurally miss —
 * a *single* `: True` field on an otherwise-populated carrier. Exemplar:
 * `mass-theory/confinement-categorical.lean` `hh_vanish : True`. Honest fix:
 * encode the real property as the field type, or demote per §3b-tax. */
const TRUE_FIELD_TYPE = /^True(\s*[∧×]\s*True)*$/;
function detectTrueClassField(d: Decl, doc: string): Hit | undefined {
  if (d.kind !== "class" && d.kind !== "structure") return undefined;
  const trueFields = classFields(d).filter((f) => {
    const t = f.type.replace(/--.*$/, "").replace(/\s+/g, " ").trim();
    return (
      TRUE_FIELD_TYPE.test(t) ||
      /(^|\s):=\s*True$/.test(t) ||
      /^Prop\s*:=\s*True$/.test(t)
    );
  });
  if (trueFields.length === 0) return undefined;
  const names = trueFields.map((f) => f.name).join(", ");
  // Honest opaque-marker carve-out (consistent with empty-prop-carrier): a
  // field explicitly framed as an opaque/marker placeholder for genuinely-open
  // infrastructure is recorded but not counted. An *un-annotated* `: True`
  // field — especially one a trivial `instance` then "closes" — is the
  // §3b-tax violation (fabricating a content-free conjecture instance).
  if (MARKER_OPT_OUT.test(doc)) {
    const h = mk(d, "proof-claims-unencoded", "true-class-field", true);
    h.exempt_reason = "explicit @marker / opaque-tag opt-out";
    h.detail = `opaque-marker field(s) \`: True\` (${names}) — honestly framed; tracked not counted`;
    return h;
  }
  const h = mk(d, "proof-claims-unencoded", "true-class-field", false);
  h.detail = `carrier field(s) typed \`: True\` carry no content (${names}) — encode the real property as the field type, or demote per §3b-tax`;
  return h;
}

/** A field typed with the **universe** `Prop` and consumed by nothing:
 * `holds : Prop`, standing alone. This is the fourth shape in the
 * carrier-vacuity family, and all three existing detectors structurally miss
 * it — `proof-no-empty-prop-carrier` requires **zero** fields and returns early
 * on one; `true-class-field` tests for a literal `True` (it catches the
 * *defaulted* `Prop := True`, not the bare universe); and `tautological-field`
 * is deliberately narrow to bounded-function shapes, which `Prop` is not.
 *
 * A field of type `Prop` asks the instance to supply *a proposition of its
 * choosing*, so an unconsumed one leaves the carrier satisfied by `⟨True⟩` and
 * every `[C]`-conditional downstream result unconditional. §3b-tax: *"Class
 * fields must carry the conjecture's **content** … never a bare `True` or an
 * empty body."* An unconsumed universe-typed field is an empty body wearing a
 * field name.
 *
 * **A `Prop`-typed field is NOT vacuous on its own, and the naive rule
 * over-reports 6x.** Declaring an abstract predicate as a field and then
 * *consuming* it in a sibling is the correct §3b-cond pattern. Worked
 * counter-example: `QOU.Torsion.BraneBoundaryContext`, whose five `Prop` fields
 * are all consumed — `boundary_active : brane_boundary_regular` asserts one and
 * `impl_brane_boundary_structure : brane_boundary_regular → Codim_at_least_2 ∧
 * ExceptionalKernel ∧ InvolutionSymmetric ∧ ChiralityInterface` relates the
 * rest. That carrier states a real implication and must stay silent. Firing on
 * *any* `Prop` field reported **101** carriers; firing only on **unconsumed**
 * ones isolates the genuine shape.
 *
 * So the criterion is: a `Prop`-typed field whose name appears in **no other
 * field's type** in the same carrier — nothing asserts it, nothing implies from
 * it, so it has no role. Honest fix: encode the property as the field's type,
 * consume it in a sibling field, or demote per §3b-tax.
 *
 * Exemplars — all three dualities of the spin/isospin cluster:
 * `IsospinFromCanonicalBowtie` (D9), `SpinFromSo3Fiber` (D10) and
 * `WignerSu4FromSpinIsospin` (D11) each declare exactly `holds : Prop` and
 * nothing else, while their `.md` siblings state real content (D9's is a
 * mass-split formula quoted at 305 ppm). The material for a contentful class
 * exists and simply is not in the Lean. */
const PROP_UNIVERSE_TYPE = /^Prop$/;
function detectPropUniverseField(d: Decl, doc: string): Hit | undefined {
  if (d.kind !== "class" && d.kind !== "structure") return undefined;
  const fields = classFields(d);
  const clean = (s: string) =>
    s.replace(/--.*$/, "").replace(/\s+/g, " ").trim();
  const universeFields = fields.filter((f) =>
    PROP_UNIVERSE_TYPE.test(clean(f.type)),
  );
  if (universeFields.length === 0) return undefined;
  // A universe-typed field earns its place if a SIBLING field's type mentions
  // it — asserting it, or relating it in an implication. Only unconsumed ones
  // are decoration.
  const unconsumed = universeFields.filter((f) => {
    const word = new RegExp(`(^|[^\\w.])${f.name}([^\\w]|$)`);
    return !fields.some((g) => g.name !== f.name && word.test(clean(g.type)));
  });
  if (unconsumed.length === 0) return undefined;
  const names = unconsumed.map((f) => f.name).join(", ");
  if (MARKER_OPT_OUT.test(doc)) {
    const h = mk(d, "proof-claims-unencoded", "prop-universe-field", true);
    h.exempt_reason = "explicit @marker / opaque-tag opt-out";
    h.detail = `unconsumed universe-typed field(s) \`: Prop\` (${names}) — honestly framed; tracked not counted`;
    return h;
  }
  const h = mk(d, "proof-claims-unencoded", "prop-universe-field", false);
  h.detail =
    `field(s) typed with the universe \`Prop\` rather than a proposition, and ` +
    `consumed by no sibling field (${names}) — the instance chooses the ` +
    `proposition, so \`⟨True⟩\` inhabits the carrier and any ` +
    `[${d.name}]-conditional result is unconditional. Encode the real property ` +
    `as the field type, consume it in a sibling, or demote per §3b-tax`;
  return h;
}

/** A `Prop`-universe field whose **only** sibling consumption is a field that
 * asserts it and nothing else — `p : Prop` sitting beside `p_holds : p`.
 *
 * This is the fifth shape in the carrier-vacuity family, and it exists in the
 * blind spot that `detectPropUniverseField` deliberately creates. That detector
 * fires only on an *unconsumed* `Prop` field, because firing on any `Prop` field
 * over-reported 6x — declaring an abstract predicate and then consuming it in a
 * sibling is the correct §3b-cond pattern. Correct, but the exemption is
 * satisfied by a consumer that adds nothing: if the only sibling mentioning `p`
 * has type *literally `p`*, the instance still chooses the proposition, and
 * `⟨True, True.intro⟩` inhabits both fields together. The pair asserts exactly
 * what a bare `p : Prop` asserts, which is nothing, while looking twice as
 * populated.
 *
 * Exemplar, and it comes with its own proof: `QOU.Mathlib.HeckeAlgebra`'s
 * `WedderburnDecomposition` declares
 *
 *     blocks_sum_to_one : Prop      blocks_sum_holds : blocks_sum_to_one
 *     blocks_orthogonal : Prop      blocks_orthogonal_holds : blocks_orthogonal
 *
 * under docstrings promising `Σ_λ p_λ = 1` and `p_λ · p_μ = 0`, and the SAME
 * FILE then discharges them at `triv_wedderburn` with `:= True` / `:= True.intro`.
 * The class asserts nothing about the block projections, so every
 * `[WedderburnDecomposition]`-conditional result downstream is unconditional.
 *
 * Deliberately NARROWER than "has a bare-assertion consumer": a field with a
 * bare assertion *and* a relating sibling keeps its content and stays silent.
 * That is what preserves `QOU.Torsion.BraneBoundaryContext`, the counter-example
 * `detectPropUniverseField` is calibrated against — its `brane_boundary_regular`
 * carries both `boundary_active : brane_boundary_regular` and an implication
 * field, so `every` fails and this detector does not fire. This criterion
 * therefore refines that exemption without overturning its calibration.
 *
 * Honest fix: encode the real proposition as the field's type (dropping the
 * `_holds` field, which then becomes the field itself), or demote per §3b-tax.
 *
 * Raised on PR #6097 / #6093 and tracked as bean `qou-qcy6`. */
function detectSelfDischargedPropField(d: Decl, doc: string): Hit | undefined {
  if (d.kind !== "class" && d.kind !== "structure") return undefined;
  const fields = classFields(d);
  const clean = (s: string) =>
    s.replace(/--.*$/, "").replace(/\s+/g, " ").trim();
  const universeFields = fields.filter((f) =>
    PROP_UNIVERSE_TYPE.test(clean(f.type)),
  );
  if (universeFields.length === 0) return undefined;
  const pairs: { prop: string; holds: string }[] = [];
  for (const f of universeFields) {
    const word = new RegExp(`(^|[^\\w.])${f.name}([^\\w]|$)`);
    const consumers = fields.filter(
      (g) => g.name !== f.name && word.test(clean(g.type)),
    );
    // Unconsumed is `detectPropUniverseField`'s territory, not this one.
    if (consumers.length === 0) continue;
    // Every consumer is a bare assertion `g : f` — nothing relates `f` to
    // anything else, so the pair adds no content over the bare field.
    if (!consumers.every((g) => clean(g.type) === f.name)) continue;
    pairs.push({ prop: f.name, holds: consumers.map((g) => g.name).join("/") });
  }
  if (pairs.length === 0) return undefined;
  const names = pairs.map((p) => `${p.prop} + ${p.holds}`).join(", ");
  if (MARKER_OPT_OUT.test(doc)) {
    const h = mk(d, "proof-claims-unencoded", "prop-field-self-discharged", true);
    h.exempt_reason = "explicit @marker / opaque-tag opt-out";
    h.detail = `self-discharged \`Prop\` field pair(s) (${names}) — honestly framed; tracked not counted`;
    return h;
  }
  const h = mk(d, "proof-claims-unencoded", "prop-field-self-discharged", false);
  h.detail =
    `\`Prop\`-universe field(s) whose only consumer asserts them and nothing ` +
    `else (${names}) — the instance chooses the proposition, so ` +
    `\`⟨True, True.intro⟩\` inhabits the pair and any [${d.name}]-conditional ` +
    `result is unconditional. Encode the real proposition as the field's type, ` +
    `or demote per §3b-tax`;
  return h;
}

/** A class/structure field whose Prop is a **tautology about the subject** —
 * neither empty (`proof-no-empty-prop-carrier`) nor literally `: True`
 * (`true-class-field`), but provable for an *arbitrary* substitution of the
 * subject term, so it constrains nothing.
 *
 * This is the third shape in the carrier-vacuity family and the one both
 * existing detectors structurally miss: the carrier *looks* populated (it has
 * real-looking Prop fields, and the docstring's claim count does not exceed the
 * field count), yet every field is a Mathlib theorem for any argument.
 *
 * Exemplar — `QOU.Interactions.TransferMatrixEigenphase`, documented as
 * axiomatising "`M_β` has spectrum `{e^{+iα}, e^{−iα}}` on `V_(2,1)`", whose
 * two fields are `-2 ≤ 2 cos(α) ∧ 2 cos(α) ≤ 2` and `cos(α) = cos(−α)`. Both
 * hold for every real. Proved vacuous in
 * `QOU.QBeta.EigenphaseCarrier.carrier_is_trivial` (`… ↔ True`).
 *
 * Deliberately NARROW: it matches only a small library of shapes that are
 * unconditionally true of the *function applied*, never of the subject —
 * bounds on a bounded function, and even/odd symmetry identities. Deciding
 * tautology in general needs the compiler; per this audit's design these are
 * high-recall candidates for an agent verdict, not verdicts. */
const BOUNDED_FN = String.raw`(?:Real\.)?(?:cos|sin)`;
/** `c ≤ k·f(x)` / `f(x) ≤ c` … with `f` bounded and `c` outside its range: the
 * bound holds for every argument. Matches a chain or a single comparison. */
const TAUT_BOUND = new RegExp(
  String.raw`^\s*-?\s*\d+(?:\.\d+)?\s*[≤<]\s*(?:\d+\s*\*\s*)?${BOUNDED_FN}\b[^∧]*` +
    String.raw`(?:∧\s*(?:\d+\s*\*\s*)?${BOUNDED_FN}\b[^≤<]*[≤<]\s*-?\s*\d+(?:\.\d+)?\s*)?$`,
);
/** `f x = f (-x)` (or the reverse): the evenness of `cos`, true for every `x`. */
const TAUT_EVEN = new RegExp(
  String.raw`${BOUNDED_FN}\s*\(?\s*([^)=]+?)\s*\)?\s*=\s*${BOUNDED_FN}\s*\(\s*-\s*\1\s*\)` +
    String.raw`|${BOUNDED_FN}\s*\(\s*-\s*([^)=]+?)\s*\)\s*=\s*${BOUNDED_FN}\s*\(?\s*\2\s*\)?`,
);
function detectTautologicalField(d: Decl, doc: string): Hit | undefined {
  if (d.kind !== "class" && d.kind !== "structure") return undefined;
  const fields = classFields(d);
  if (fields.length === 0) return undefined; // empty-carrier detector owns this
  const taut = fields.filter((f) => {
    const t = f.type.replace(/--.*$/, "").replace(/\s+/g, " ").trim();
    return TAUT_BOUND.test(t) || TAUT_EVEN.test(t);
  });
  // Only fire when EVERY field is tautological: a carrier with one real field
  // still constrains something, and flagging it would over-report.
  if (taut.length !== fields.length) return undefined;
  const names = taut.map((f) => f.name).join(", ");
  if (MARKER_OPT_OUT.test(doc)) {
    const h = mk(d, "proof-claims-unencoded", "tautological-field", true);
    h.exempt_reason = "explicit @marker / opaque-tag opt-out";
    h.detail = `all field(s) tautological (${names}) — honestly framed; tracked not counted`;
    return h;
  }
  const h = mk(d, "proof-claims-unencoded", "tautological-field", false);
  h.detail =
    `every field is a tautology about the subject (${names}) — each holds for an ` +
    `arbitrary substitution, so the carrier is equivalent to True and any ` +
    `[${d.name}]-conditional result is unconditional. Encode the real property, ` +
    `or demote per §3b-tax`;
  return h;
}

/** Theorem-assertion language in a docstring: a bold or leading
 * **Theorem/Lemma/Proposition/Corollary** header. Signals the block claims a
 * *provable* result — so a `: True` conclusion underneath it is the
 * `q_gl_obstruction_calc` failure mode (a real claim hidden behind a
 * tautology), NOT an honest open conjecture. */
const DOC_ASSERTS_PROVABLE =
  /\*\*\s*(Theorem|Lemma|Proposition|Corollary)\b|(^|\n)\s*(--\s*)?(Theorem|Lemma|Proposition|Corollary)\b/i;

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
  /** The `.md` sibling's prose, scanned alongside the docstring. */
  narrative: string;
}

interface ConjGraph {
  total: number;
  // {name, file, line} objects (same shape as `dependent`): short carrier
  // names are not unique across namespaces/files, so a bare string list
  // would be ambiguous for consumers treating `primary` as a set.
  primary: { name: string; file: string; line: number }[];
  dependent: { name: string; file: string; line: number; dependsOn: string[] }[];
}

/** conj: labels this carrier *declares* as its own (`\label{conj:X}`). */
function ownConjLabels(doc: string): string[] {
  const out = new Set<string>();
  for (const m of doc.matchAll(/\\label\{conj:([a-z0-9-]+)\}/gi))
    out.add(m[1].toLowerCase());
  return [...out];
}

/** The content block's own label, read from the authoritative `.ts` sibling.
 *
 * `ownConjLabels` keys on `\label{conj:…}`, which appears in **15** `.lean`
 * files corpus-wide against **113** using the markdown-link form. Since
 * `labelToName` is built from own-labels, that alone left the map nearly empty
 * and `proof-dependent-conjecture-not-conditional` unable to resolve any
 * claimed dependency to a carrier — measured, the criterion returned **0 hits
 * across 244 carriers and 3264 files** while at least four carriers declare
 * conditionality in prose and bind nothing. The `.ts` `label:` field is the
 * block's identity and does not depend on how a docstring was written. */
function siblingBlockLabel(leanFile: string): string | undefined {
  const ts = leanFile.replace(/\.lean$/, ".ts");
  if (!existsSync(ts)) return undefined;
  try {
    const m = /label:\s*"(conj:[a-z0-9-]+)"/i.exec(readFileSync(ts, "utf8"));
    return m ? m[1].slice("conj:".length).toLowerCase() : undefined;
  } catch {
    return undefined;
  }
}

/** The content block's own label of ANY kind (`prop:…`, `thm:…`, `conj:…`).
 *
 * `siblingBlockLabel` above deliberately returns only `conj:` labels, because
 * it feeds `labelToName`, which maps a label to the carrier CLASS that
 * axiomatises it — and only conjectures have one. The `uses[]`-reachability
 * check below needs something different: the node this block occupies in the
 * dependency graph, whatever its kind. A `prop:`-labelled block has no `conj:`
 * label at all, so without this it has no start node and cannot be checked. */
function siblingBlockLabelAny(leanFile: string): string | undefined {
  const ts = leanFile.replace(/\.lean$/, ".ts");
  if (!existsSync(ts)) return undefined;
  try {
    const m = /label:\s*"([a-z]+:[a-z0-9-]+)"/i.exec(readFileSync(ts, "utf8"));
    return m ? m[1].toLowerCase() : undefined;
  } catch {
    return undefined;
  }
}

/** `label -> uses[]` over every content block, built once and cached.
 *
 * This is the EDITORIAL dependency graph the `.md` banners are checked
 * against. Parsed from the `.ts` manifests rather than from any derived
 * artifact, so it cannot go stale relative to the blocks themselves. */
let _usesGraph: Map<string, string[]> | undefined;
function usesGraph(): Map<string, string[]> {
  if (_usesGraph) return _usesGraph;
  const g = new Map<string, string[]>();
  const root = resolve(REPO_ROOT, "folio");
  const walk = (dir: string): void => {
    let ents: ReturnType<typeof readdirSync<{ withFileTypes: true }>>;
    try {
      ents = readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const e of ents) {
      const p = join(dir, e.name);
      if (e.isDirectory()) walk(p);
      else if (e.name.endsWith(".ts")) {
        let t: string;
        try {
          t = readFileSync(p, "utf8");
        } catch {
          continue;
        }
        const lm = /label:\s*"([a-z]+:[a-z0-9-]+)"/i.exec(t);
        if (!lm) continue;
        // Comments are stripped BEFORE the array is matched. `uses: [ … ]` is
        // matched non-greedily to the first `]`, so a single `]` anywhere in an
        // explanatory comment inside the array truncates the capture and the
        // block silently reads as having NO dependencies. Found the hard way:
        // the comment added to `magic-A-binding-formula.ts` contains the string
        // `uses[]`, which zeroed out that block's edges and made the very
        // dependency the comment was documenting look unrecorded.
        const noComments = t
          .replace(/\/\*[\s\S]*?\*\//g, "")
          .replace(/(^|[^:])\/\/[^\n]*/g, "$1");
        const um = /uses:\s*\[([\s\S]*?)\]/.exec(noComments);
        g.set(
          lm[1].toLowerCase(),
          um ? [...um[1].matchAll(/"([^"]+)"/g)].map((m) => m[1].toLowerCase()) : [],
        );
      }
    }
  };
  if (existsSync(root)) walk(root);
  _usesGraph = g;
  return g;
}

/** Is `target` reachable from `from` by walking `uses[]` edges? UNBOUNDED.
 *
 * **It was bounded at 5, and that bound manufactured a false positive within
 * the hour** (bean `qou-s3zd`). `prop:root-of-unity-truncation` reaches
 * `conj:regularity-breakdown` at depth **6** — one hop past the cutoff — so
 * the block was reported as claiming a dependency it does not record, and the
 * verdict written against it said "unreachable at any depth" on the strength
 * of a search that had only looked five deep. An absence measured under a
 * bound is not an absence.
 *
 * The bound was there on the theory that an unbounded walk over a large graph
 * would eventually connect almost anything to anything. **Measured, that is
 * false here**: 3606 blocks joined by 4912 edges — barely more than one edge
 * per block — and the transitive closures of the four blocks in question are
 * 164, 110, 11 and 1. A `uses[]` graph is a reading order, not a mesh.
 *
 * Unbounded is also the semantics that matters. The question this answers is
 * "would a direct edge here be redundant?", and `prune-transitive-deps.ts`
 * strips a redundant edge at ANY depth, so any bound makes the checker
 * disagree with the tool whose rule it is enforcing. Termination comes from
 * `seen`, not from a depth counter. */
function reachableInUses(from: string, target: string): boolean {
  const g = usesGraph();
  if (!g.has(from)) return false;
  const seen = new Set([from]);
  const queue = [from];
  while (queue.length > 0) {
    const n = queue.shift() as string;
    for (const c of g.get(n) ?? []) {
      if (c === target) return true;
      if (!seen.has(c)) {
        seen.add(c);
        queue.push(c);
      }
    }
  }
  return false;
}

/** The `.md` sibling's prose, where a content block actually declares its
 * conditionality. The Lean docstring is a summary; the narrative is where
 * "conditional on [`conj:X`]" is written. Scanning only the docstring was the
 * second half of the blind spot above. */
function siblingNarrative(leanFile: string): string {
  const md = leanFile.replace(/\.lean$/, ".md");
  if (!existsSync(md)) return "";
  try {
    return readFileSync(md, "utf8");
  } catch {
    return "";
  }
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
      const ownFromTs = siblingBlockLabel(f);
      carriers.push({
        name: d.name,
        file: relative(REPO_ROOT, f),
        line: d.startLine,
        sig: d.sig,
        doc,
        narrative: siblingNarrative(f),
        ownLabels: ownFromTs
          ? [...new Set([...ownConjLabels(doc), ownFromTs])]
          : ownConjLabels(doc),
      });
    }
  }
  const names = new Set(carriers.map((c) => c.name));
  const labelToName = new Map<string, string>();
  for (const c of carriers)
    for (const l of c.ownLabels) if (!labelToName.has(l)) labelToName.set(l, c.name);

  const primary: ConjGraph["primary"] = [];
  const dependent: ConjGraph["dependent"] = [];
  const hitsByFile = new Map<string, Hit[]>();
  /** `.md`-sourced claims already reported for a file — see `scan` below. */
  const narrativeReported = new Map<string, Set<string>>();

  for (const c of carriers) {
    const edges = bindersReferencing(c.sig, names).filter((n) => n !== c.name);
    if (edges.length > 0)
      dependent.push({ name: c.name, file: c.file, line: c.line, dependsOn: edges });
    else primary.push({ name: c.name, file: c.file, line: c.line });

    // Derived defect: the doc *explicitly* claims conditionality on a
    // `conj:Y` (another carrier) yet the type binds no such class. This is
    // the intent-vs-type mismatch — a result that reads as conditional but
    // is stated unconditionally. Plain prose mentions are NOT flagged.
    // Sourced separately, because they have different SCOPE. A Lean docstring
    // belongs to one declaration; the `.md` is the narrative of the whole
    // content block, which may define several carriers. Charging a block-level
    // sentence to each carrier in the file manufactures duplicates: measured,
    // one line of `phi-q-aj-machinery-identification.md` became three "hits"
    // across the three classes that share it, and all three were spurious --
    // those classes are well-formed §3b-cond carriers binding
    // `[QuantumAPolynomial …]`, not the conjecture the prose names.
    // `[[`]?` allowed exactly ONE bracket-or-backtick, but the corpus's
    // canonical cross-reference is ``[`conj:X`]`` -- bracket AND backtick.
    // That single `?` was the third reason this criterion never fired.
    //
    // The label KIND is captured as well as the stem. The pattern was
    // `conj:` only, which made a second missing dependency in the SAME banner
    // structurally invisible: `magic-A-binding-formula.md` declares itself
    // conditional on `conj:magic-numbers-bring` AND
    // `prop:gravity-spectral-prefactor`, both were absent from `uses[]` and
    // unreachable, and only the first was ever reported (bean `qou-s3zd`).
    // ALL labels in the banner clause, not just the first. A trigger phrase is
    // located, then every `kind:stem` in the clause it opens is taken, because
    // a banner routinely names several: `magic-A-binding-formula.md` reads
    // "conditional on [`conj:magic-numbers-bring`](…) and
    // [`prop:gravity-spectral-prefactor`](…)", and one-label-per-trigger saw
    // only the first — the second is preceded by "and", not by a trigger.
    //
    // The clause ends at the next `**` (banners are bold-delimited) or after
    // 300 characters, whichever comes first, so the scan cannot run on into
    // unrelated prose. Markdown link targets in the window are not at risk of
    // matching: a path (`../…/magic-numbers-bring.md`) and a URL scheme
    // (`https://`) both fail `[a-z]+:[a-z0-9-]+`, the first for want of a
    // colon and the second because `//` is not `[a-z0-9-]`.
    const scan = (text: string): string[] => {
      const out: string[] = [];
      const trigger =
        /(?:conditional on|assuming|given|depends on|modulo)\s+(?=[[`\s]*[a-z]+:[a-z0-9-]+)/gi;
      for (const t of text.matchAll(trigger)) {
        const from = (t.index ?? 0) + t[0].length;
        const rest = text.slice(from, from + 300);
        const end = rest.indexOf("**");
        const clause = end === -1 ? rest : rest.slice(0, end);
        for (const m of clause.matchAll(/([a-z]+):([a-z0-9-]+)/gi))
          out.push(`${m[1].toLowerCase()}:${m[2].toLowerCase()}`);
      }
      return [...new Set(out)];
    };

    // A DOC claim and a BLOCK claim are checked against different things, and
    // conflating them produced two of the three hits in the 2026-08-30 sweep.
    //
    // A Lean docstring belongs to ONE DECLARATION, so "conditional on conj:Y"
    // there is a statement about this type and is checked against the type:
    // does the signature bind Y's carrier class? That is unambiguous.
    //
    // The `.md` is the narrative of the WHOLE BLOCK, and its banner routinely
    // names an upstream result the block is conditional on *editorially* --
    // what a reader must have read -- while the Lean's own conditionality sits
    // on a proximate context class. Checking that against the binder is a
    // category error, and it is what flagged `root-of-unity-truncation` and
    // `phi-q-aj-machinery-identification`, both of which are well-formed
    // §3b-cond blocks. What a block-level claim SHOULD match is the block's
    // dependency record, so it is checked against `uses[]` reachability.
    const fromDoc = scan(c.doc);
    const narrativeSeen = narrativeReported.get(c.file) ?? new Set<string>();
    const fromNarrative = scan(c.narrative).filter((l) => !narrativeSeen.has(l));
    for (const l of fromNarrative) narrativeSeen.add(l);
    narrativeReported.set(c.file, narrativeSeen);

    const mkHit = (pattern: string, detail: string): void => {
      const abs = resolve(REPO_ROOT, c.file);
      const arr = hitsByFile.get(abs) ?? [];
      arr.push({
        line: c.line,
        category: "proof-dependent-conjecture-not-conditional",
        pattern,
        snippet: c.name,
        decl: c.name,
        severity: SEVERITY["proof-dependent-conjecture-not-conditional"],
        detail,
      });
      hitsByFile.set(abs, arr);
    };

    // (1) Doc-level: intent-vs-type. `conj:` only, because `labelToName` maps
    // a label to the carrier CLASS axiomatising it and only conjectures have
    // one -- a `prop:` has nothing to bind, so widening here would flag the
    // absence of a binder that could not exist.
    const unmetDoc = fromDoc
      .filter((l) => l.startsWith("conj:"))
      .map((l) => l.slice("conj:".length))
      .filter((l) => !c.ownLabels.includes(l))
      .map((l) => labelToName.get(l))
      .filter((n): n is string => !!n && n !== c.name && !edges.includes(n));
    if (unmetDoc.length > 0)
      mkHit(
        "prose-conditional-not-in-type",
        `doc claims conditionality on ${unmetDoc
          .map((n) => `\`${n}\``)
          .join(", ")} but the signature takes no binder on it`,
      );

    // (2) Block-level: is the declared dependency RECORDED anywhere? Any label
    // kind. Unreachable in `uses[]` means it exists in one prose sentence and
    // nowhere a reader or a tool can follow -- the §3b-cond item 4 gap.
    const own = siblingBlockLabelAny(resolve(REPO_ROOT, c.file));
    if (own) {
      const unrecorded = fromNarrative.filter(
        (l) => l !== own && usesGraph().has(l) && !reachableInUses(own, l),
      );
      if (unrecorded.length > 0)
        mkHit(
          "prose-conditional-unrecorded-dependency",
          `the block's .md declares \`${own}\` conditional on ${unrecorded
            .map((l) => `\`${l}\``)
            .join(", ")}, which is absent from uses[] and unreachable from it ` +
            `at any depth — the dependency is claimed in prose only`,
        );
    }
  }
  return {
    graph: {
      total: carriers.length,
      primary: primary.sort(
        (a, b) => a.name.localeCompare(b.name) || a.file.localeCompare(b.file),
      ),
      dependent,
    },
    hitsByFile,
  };
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

  // Does ANY declaration in this file carry a real `sorry` in code? This is the
  // evidence half of the delegation exemption in `detectDocstringSorryMismatch`
  // — a docstring that hands its `sorry` to a sub-theorem is believable only if
  // a `sorry` actually exists nearby. `Decl.body` is comment-free, so prose
  // mentions of the word do not count.
  const fileHasSorryCode = decls.some((x) => /\bsorry\b/.test(x.body));

  // Carrier lookup for the self-assuming type-match test: it resolves a
  // projection `ctx.foo` to the field `foo` of the class `ctx` inhabits, so it
  // needs the file's `class`/`structure` declarations by name. Same-file only —
  // a carrier declared elsewhere yields no match, which keeps the test
  // conservative rather than guessing.
  // Reducible `abbrev` head aliases, so the self-assuming type-match test is
  // not defeated by a field and a conclusion spelling the same term two ways.
  const headAliases = fileHeadAliases(decls);

  const carrierDecls = new Map<string, Decl>(
    decls
      .filter((x) => /^(class|structure)\b/.test(x.kind))
      .map((x) => [x.name, x] as const),
  );

  for (let di = 0; di < decls.length; di++) {
    const d = decls[di];
    // The doc block is computed once up front so the trivial-true detector
    // can be escalated when the prose asserts a *provable* claim (the
    // `q_gl_obstruction_calc` failure mode) and the conjecture-discipline
    // content detectors can read it.
    const doc = docBlockAbove(origLines, d.startLine - 1);
    // Raw (comment-bearing) span of this decl through the next, so the
    // true-field opaque-marker opt-out can see a *field-level* `opaque marker`
    // annotation (which lives inside the class body, not in the block above).
    const spanEnd =
      di + 1 < decls.length ? decls[di + 1].startLine - 1 : origLines.length;
    const rawSpan = origLines.slice(d.startLine - 1, spanEnd).join("\n");
    const tt = detectTrivialTrue(d, src, fileIsStub, absPath);
    if (
      tt &&
      !tt.exempt &&
      /placeholder-true|def-disguised-true/.test(tt.pattern) &&
      DOC_ASSERTS_PROVABLE.test(doc) &&
      !isConjectureCarrier(doc)
    ) {
      tt.detail =
        (tt.detail ? tt.detail + "; " : "") +
        "docstring asserts a provable claim (Theorem/Lemma/Proposition) while the Lean concludes `True` — a genuine vacuity defect, not an honest open conjecture";
    }
    push(tt);
    push(detectSelfAssuming(d, carrierDecls, headAliases));
    push(detectBinderEcho(d, origLines));
    push(detectTrivialExistential(d, origLines));
    push(detectDocstringSorryMismatch(d, doc, fileHasSorryCode));
    push(detectUnusedHypothesisRfl(d));
    push(detectTelescopeVacuousRfl(d));
    push(detectDecideMasking(d));
    push(detectFalsePremise(d));
    push(detectProvableAxiom(d, origLines));
    push(detectTrivialTypeMismatch(d));
    // Conjecture-discipline *content* detectors operate on the
    // `class`/`structure` carrier + its raw doc block. The primary-vs-
    // dependent classification is NOT a per-file check — it is derived
    // globally from instance binders in `classifyConjectures` (the
    // dependency is already in the Lean type; no hand tag is needed).
    push(detectEmptyPropCarrier(d, doc));
    push(detectClaimsUnencoded(d, doc));
    push(detectTrueClassField(d, doc + "\n" + rawSpan));
    push(detectPropUniverseField(d, doc + "\n" + rawSpan));
    push(detectSelfDischargedPropField(d, doc + "\n" + rawSpan));
    push(detectTautologicalField(d, doc + "\n" + rawSpan));
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

/** Where the inhabitation probe records what Lean actually said. */
const PROBE_BASELINE = "docs/audits/vacuous-prop-carrier-baseline.json";

/**
 * Seed `proof-carrier-inhabited-by-probe` candidates from the probe baseline.
 *
 * THE ASYMMETRY, which is the whole reason this is a separate function rather
 * than three lines inline: **a probe SUCCESS is evidence and a probe FAILURE
 * is not.** Lean inhabiting a carrier with no hypotheses settles that the
 * carrier asserts nothing. Lean failing to means the tactic list found no
 * witness — nothing more. This is not a hypothetical distinction; measured on
 * this corpus, the generic list misses `QAubinLions`, `BlowupYekutieli` and
 * `RegularityBreakdown`, all three of which are provable and two of which the
 * corpus itself proves in its own instance bundle.
 *
 * So this reads exactly one verdict, `proved-vacuous`, and every other value
 * — `uninhabitable-by-design`, `undecided`, anything added later — emits
 * nothing. A carrier is never flagged because a probe *failed* to settle it,
 * and the enum cannot drift into flagging one: the check is an allowlist of
 * one, not a denylist.
 *
 * The baseline is optional. It is produced by a script that needs a working
 * Lean toolchain, which a bare container does not have, and an audit that
 * hard-failed on its absence would be unrunnable exactly where Lean is
 * unavailable. Absent baseline → no candidates, no error.
 *
 * Staleness is delegated to the ledger's existing `file_sha` logic, keyed on
 * the CARRIER's file rather than on the baseline. That is deliberate and is a
 * strict improvement on the baseline alone, which stores no hash at all: edit
 * a carrier and its ledger verdict goes `needs-agent` on the next
 * `--review-ledger`, whether or not anyone re-runs the probe.
 */
function seedProbeInhabitedCandidates(
  shaCache: Map<string, string | undefined>,
): {
  key: string;
  rel: string;
  line: number;
  decl: string;
  category: string;
  pattern: string;
  file_sha?: string;
}[] {
  const p = resolve(REPO_ROOT, PROBE_BASELINE);
  if (!existsSync(p)) return [];
  let entries: Record<string, { verdict?: string }> = {};
  try {
    entries = JSON.parse(readFileSync(p, "utf-8"))?.entries ?? {};
  } catch {
    return [];
  }

  const out = [];
  for (const [k, v] of Object.entries(entries)) {
    if (v?.verdict !== "proved-vacuous") continue;
    const sep = k.lastIndexOf("::");
    if (sep < 0) continue;
    const rel = k.slice(0, sep);
    const decl = k.slice(sep + 2);
    const abs = resolve(REPO_ROOT, rel);
    if (!existsSync(abs)) continue; // carrier's file moved or was deleted
    if (!shaCache.has(abs)) shaCache.set(abs, hashFile(abs));

    // Locate the declaration. The baseline stores the fully-qualified name;
    // the source writes the last component, so match on that at a
    // `class`/`structure` head.
    const leaf = decl.slice(decl.lastIndexOf(".") + 1);
    const lines = readFileSync(abs, "utf-8").split("\n");
    const at = lines.findIndex((l) =>
      new RegExp(`^\\s*(?:@\\[[^\\]]*\\]\\s*)?(?:class|structure)\\s+${leaf}\\b`).test(l),
    );

    // A MISS MEANS THE DECLARATION IS GONE, AND THE CANDIDATE IS NOT REAL.
    // This used to fall through to line 1 on the reasoning that "the candidate
    // is still real, so fall back rather than dropping it" — but `existsSync`
    // above tests the FILE, not the DECLARATION, so a carrier deleted from a
    // file that still exists sailed through. Measured 2026-08-30: five
    // carriers removed from `core-levi-form.lean` were still being seeded,
    // each pointing at line 1, and each had collected a `genuine` ledger
    // verdict for something that was not there — 5 of 19 baseline entries,
    // and 5 of the 14 candidates in this category. Skipping is correct: the
    // baseline records what Lean said about a declaration, and there is no
    // declaration left for it to have said it about. Bean `qou-s3zd`.
    if (at === -1) continue;

    out.push({
      key: `${rel}::${decl}::proof-carrier-inhabited-by-probe`,
      rel,
      line: at + 1, // `at === -1` is impossible here — skipped above.
      decl,
      category: "proof-carrier-inhabited-by-probe",
      pattern: "lean-inhabited-no-hypotheses",
      file_sha: shaCache.get(abs),
    });
  }
  return out;
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

/**
 * Guard for `docstringSorryIsHistorical`, added with the superseded-text
 * patterns on 2026-09-03.
 *
 * The risk of those patterns is OVER-suppression: a sentence that mentions old
 * wording *and* makes a live claim would go silent. So the fixtures are the
 * eight genuine mismatches drained in PR #6471 (which must all still fire) and
 * the four attribution-to-superseded-text sentences that were firing on `main`
 * b8d883189d and must not (three of them predate that PR; one is its own
 * correction). Every fixture is real text from the corpus, not invented.
 */
function selftestDocstringSorry(): number {
  const suppress: Array<[string, string]> = [
    ["identityB_general",
     '**Corrected 2026-08-23.** The sentence that stood here said "the only ' +
     "residual inputs are the bricks' own honest `sorry`s\"."],
    ["nucleon_ordering_factorization",
     "**Honest `sorry` — and now actually one.** Until 2026-08-08 this docstring " +
     "said \"honest `sorry`\" while the body read `exact ctx.factorization_ident`."],
    ["whitehead_volume_conjecture",
     '⚠ The previous wording called this "the one honest `sorry` here".'],
    ["confinement_categorical",
     'The paragraph that stood here said the body was "an honest `sorry` + ' +
     '`-- Ref:`", that "no class field posits this conclusion".'],
  ];
  const mustFire: Array<[string, string]> = [
    ["kappa_commutes_bar",
     "It is a non-false, non-trivial claim that is NOT derivable from the diagonal " +
     "structure alone, so it is left as an honest `sorry`."],
    ["mobius_frobenius_kernel",
     "neither of which is yet formalised; the body is a `sorry` carrying the " +
     "manuscript citation per AGENTS.md §1."],
    ["markovTrace_branching",
     "that cannot be added as a simple class field, so the body is `sorry` with " +
     "the manuscript citation."],
    ["four_term_pair_nucleon",
     "Honest `sorry`: the polarization-independence is proved as a mechanism."],
    ["descended_trace_is_base_trace",
     "Needs the descent / Frobenius-trace infrastructure (not formalised); body is `sorry`."],
    ["base_mass_is_norm_of_base_trace",
     "the base level (not formalised); body is `sorry`."],
    ["ConfinementSDP",
     "The conic-duality step itself is not in Mathlib, so it is discharged by " +
     "`sorry` here — the hypothesis is the genuine analytic input."],
    ["confinement_categorical (pre-fix)",
     "neither of which is in Mathlib. The body is therefore an honest `sorry` + `-- Ref:`."],
  ];
  const fires = (s: string) =>
    DOC_CLAIMS_SORRY.test(s) && !docstringSorryIsHistorical(s);

  let bad = 0;
  for (const [name, s] of suppress) {
    if (fires(s)) {
      console.log(`SELFTEST FAIL: still fires on superseded-text quote: ${name}`);
      bad++;
    }
  }
  for (const [name, s] of mustFire) {
    if (!fires(s)) {
      console.log(`SELFTEST FAIL: genuine claim no longer fires (over-suppressed): ${name}`);
      bad++;
    }
  }
  if (bad === 0) {
    console.log(
      "selftest ok: 4 attribution-to-superseded-text sentences suppressed, " +
      "8 genuine sorry-claims still flagged",
    );
  }
  return bad === 0 ? 0 : 1;
}

function main() {
  const argv = process.argv.slice(2);
  const roots: string[] = [];
  let jsonOut = "docs/audits/2026-06-17-lean-vacuity-axiom-audit.json";
  // Whether `--json` was passed. A caller who names an output path has chosen
  // where the report goes and may write whatever they scanned; a caller who did
  // not is aiming at the committed corpus record by default, which a partial
  // scan must not overwrite. See the guard above `writeFileSync`.
  let jsonExplicit = false;
  let writeSc = false;
  let quiet = false;
  let onlyCat: Category | undefined;
  // CI gate: exit 1 if any non-exempt hit lands in one of these categories.
  // Default targets the two guaranteed-error (compile-validity) classes so
  // the gate is low-false-positive; the high-recall vacuity candidates stay
  // warn-only (agent-adjudicated). Pass `--fail-on a,b` to override.
  let failOn: Set<string> | undefined;
  // Agent-inspection ledger (the durable "not just machine" layer). A
  // standalone library `.lean` has no `<block>.qa.json` sidecar, so an agent
  // verdict has nowhere to live and detection stays purely heuristic. The
  // ledger is a committed JSON keyed by `<relpath>::<decl>::<category>` that
  // records the AGENT verdict (genuine / legit / advisory) + the `.lean` sha
  // at review time. `--review-ledger` seeds/refreshes it (new + file-changed
  // candidates → `needs-agent`); `--check-ledger` fails if any non-exempt
  // candidate lacks a FRESH agent verdict — making agent inspection mandatory.
  let reviewLedger: string | undefined;
  let checkLedger: string | undefined;
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--selftest-docstring-sorry") {
      process.exit(selftestDocstringSorry());
    }
    else if (a === "--json") {
      jsonOut = argv[++i];
      jsonExplicit = true;
    }
    else if (a === "--write-sidecars") writeSc = true;
    else if (a === "--quiet") quiet = true;
    else if (a === "--only") onlyCat = argv[++i] as Category;
    else if (a === "--review-ledger") reviewLedger = argv[++i];
    else if (a === "--check-ledger") checkLedger = argv[++i];
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
    // An unrecognised FLAG is a mistake, not a scan root. Falling through to
    // `roots.push()` made `--help` a path that matches no `.lean`, and the
    // witness below then wrote 0 findings over the committed audit — turning a
    // typo into "the corpus is clean". Same for `--jsonn`, `-h`, etc.
    else if (a.startsWith("-")) {
      console.error(`lean-vacuity-axiom-audit: unknown option '${a}'\n`);
      console.error(
        "usage: bun run content/pipeline/lean-vacuity-axiom-audit.ts [root ...]\n" +
          "  --json FILE          witness output (default docs/audits/2026-06-17-lean-vacuity-axiom-audit.json)\n" +
          "  --write-sidecars     upsert <block>.qa.json script entries\n" +
          "  --only CATEGORY      restrict to one category\n" +
          "  --review-ledger F    seed/refresh the agent-verdict ledger\n" +
          "  --check-ledger F     fail unless every candidate has a fresh verdict\n" +
          "  --fail-on A,B        exit non-zero on these categories\n" +
          "  --selftest-docstring-sorry  guard for the superseded-text patterns\n" +
          "  --quiet\n",
      );
      process.exit(2);
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
  // An adjudicated `genuine` verdict outranks a `triage pending` exemption:
  // the exemption said a verdict was owed, and one has since been given.
  const adjudicatedGenuine = loadAdjudicatedGenuine(
    reviewLedger ?? checkLedger ?? DEFAULT_REVIEW_LEDGER,
  );
  let promotedHits = 0;
  for (const f of files) {
    const hits = scanFile(f, onlyCat);
    if (hits.length === 0) continue;
    const rel = relative(REPO_ROOT, f);
    flaggedByLean.set(f, hits);
    for (const h of hits) {
      if (
        h.exempt &&
        LEDGER_TRACKED_EXEMPT.test(h.exempt_reason ?? "") &&
        adjudicatedGenuine.has(`${rel}::${h.decl ?? "file"}::${h.category}`)
      ) {
        h.promoted_from_exempt = h.exempt_reason;
        h.exempt = false;
        h.exempt_reason = undefined;
        promotedHits++;
      }
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
    /** Of `total_defects`, how many were counted only because the review
     * ledger already adjudicated them `genuine`, lifting a `triage pending`
     * exemption. Reported so the artifact cannot silently disagree with the
     * ledger about the size of the backlog (bean `qou-v4ht`). */
    total_promoted_from_exempt: promotedHits,
    categories: counts,
    conjecture_graph: graph,
    flagged,
  };
  // Safety net for the same failure the unknown-option check above prevents at
  // the source: a run that scanned NOTHING must not overwrite a real audit.
  // The witness is a committed file, and zeros in it read as "the corpus is
  // clean" — the most misleading possible artifact. Observed: a stray `--help`
  // replaced a 1961-file / 44-defect / 105-flagged-file audit with all zeros.
  // A genuinely empty scan is always a mistake (a bad root, a typo); there is
  // no legitimate run of this script over zero `.lean` files.
  if (files.length === 0) {
    console.error(
      `lean-vacuity-axiom-audit: scanned 0 .lean files under ${scanRoots.join(", ")} — refusing to write ${jsonOut}.`,
    );
    console.error(
      "  Writing would replace the committed audit with zeros, which reads as a clean corpus.",
    );
    console.error("  Check the scan root(s); pass a directory that contains .lean files.");
    process.exit(2);
  }
  // …and the SAME reasoning one step further out: a PARTIAL scan must not
  // overwrite the corpus record either.  The zero-file guard above was added
  // after a stray `--help` replaced a real audit with zeros; it stops that case
  // and nothing else.  The documented CI invocation
  //
  //     bun run … lean-vacuity-axiom-audit.ts <changed .lean files> --quiet --fail-on …
  //
  // passes explicit paths, scans a handful of files, and sailed straight past
  // it.  Measured 2026-08-15 (bean `qou-c7jp`): a 12-file diff run replaced a
  // 2765-file / 169-flagged / 94-defect audit with `scanned 12, flagged 0,
  // defects 0` — a 3,736-line deletion that reads as a CLEAN CORPUS over 94
  // real defects.  CI never commits the file, so this only ever arrives from a
  // local run plus `git add -A`, surfacing as an unrelated diff in an unrelated
  // PR.
  //
  // A caller who passes `--json` has chosen where the report goes and may write
  // whatever they scanned; the default path is the committed record and is
  // reserved for a corpus-wide scan.
  if (roots.length > 0 && !jsonExplicit) {
    if (!quiet) {
      console.error(
        `lean-vacuity-axiom-audit: partial scan (${files.length} file(s) from explicit path(s)) — NOT writing ${jsonOut}.`,
      );
      console.error(
        "  That file is the corpus-wide record; a partial scan would overwrite it with a",
      );
      console.error(
        "  smaller count that reads as a clean corpus. Gate results below are unaffected.",
      );
      console.error(
        "  To write a partial report anyway, name an output: --json <path>.",
      );
    }
  } else {
    writeFileSync(resolve(REPO_ROOT, jsonOut), JSON.stringify(witness, null, 2) + "\n");
  }

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

  // ── Agent-inspection ledger ──────────────────────────────────────
  // The set of non-exempt candidates this scan would defer to an agent.
  // `flaggedByLean` already has the derived conjecture hits merged in.
  let ledgerFail = 0;
  if (reviewLedger || checkLedger) {
    const nowIso = new Date().toISOString();
    const candidates: {
      key: string;
      rel: string;
      line: number;
      decl: string;
      category: string;
      pattern: string;
      file_sha?: string;
    }[] = [];
    const shaCache = new Map<string, string | undefined>();
    for (const [f, hits] of flaggedByLean) {
      const rel = relative(REPO_ROOT, f);
      if (!shaCache.has(f)) shaCache.set(f, hashFile(f));
      const sha = shaCache.get(f);
      for (const h of hits) {
        // Exempt hits are normally out of scope for the agent-inspection gate:
        // the exemption IS the verdict (a shadow stub, an `@marker` opt-out, a
        // legitimate iff-from-directions derive). But an exemption that says
        // "tracked, triage pending" asserts the opposite — that a human call is
        // still owed. Blanket-skipping those would make EXEMPT a way to bury a
        // candidate rather than queue it, which is the failure mode this whole
        // audit exists to catch. So they stay in the ledger.
        if (h.exempt && !LEDGER_TRACKED_EXEMPT.test(h.exempt_reason ?? ""))
          continue;
        const decl = h.decl ?? "file";
        candidates.push({
          key: `${rel}::${decl}::${h.category}`,
          rel,
          line: h.line,
          decl,
          category: h.category,
          pattern: h.pattern,
          file_sha: sha,
        });
      }
    }

    // Candidates this scanner cannot see, because deciding them needs Lean
    // rather than a reading of the source. Evidence comes from the probe
    // baseline; only carriers Lean PROVED inhabitable are admitted.
    candidates.push(...seedProbeInhabitedCandidates(shaCache));

    if (reviewLedger) {
      const p = resolve(REPO_ROOT, reviewLedger);
      let led: {
        $schema: string;
        updated_at: string;
        entries: Record<string, Record<string, unknown>>;
      } = { $schema: "lean-vacuity-review/v1", updated_at: nowIso, entries: {} };
      if (existsSync(p)) {
        try {
          const r = JSON.parse(readFileSync(p, "utf-8"));
          if (r?.entries) led = r;
        } catch {
          /* fresh */
        }
      }
      const seen = new Set<string>();
      let added = 0,
        kept = 0,
        stale = 0;
      for (const c of candidates) {
        seen.add(c.key);
        const prev = led.entries[c.key];
        const hasVerdict =
          prev && prev.verdict && prev.verdict !== "needs-agent";
        if (hasVerdict && prev.file_sha === c.file_sha) {
          led.entries[c.key] = { ...prev, line: c.line, pattern: c.pattern };
          kept++;
        } else if (hasVerdict) {
          // file changed since the verdict → re-review required.
          led.entries[c.key] = {
            ...prev,
            verdict: "needs-agent",
            stale_prev_verdict: prev.verdict,
            line: c.line,
            pattern: c.pattern,
            file_sha: c.file_sha,
          };
          stale++;
        } else {
          led.entries[c.key] = {
            category: c.category,
            pattern: c.pattern,
            line: c.line,
            verdict: "needs-agent",
            file_sha: c.file_sha,
          };
          added++;
        }
      }
      // Drop entries whose candidate no longer flags (resolved/fixed) — but
      // ONLY in categories this audit actually produces.
      //
      // The ledger is SHARED. Other tools and hand adjudications write into it
      // under categories this scanner has never heard of, and to this loop an
      // entry it cannot produce is indistinguishable from one that has been
      // fixed. Measured on `main` 2026-08-30, before this guard: a single
      // `--review-ledger` run deleted **116 of 268 entries** — 104
      // `proof-borrowed-name`, 7 `proof-zero-placeholder`, and one each of
      // `name-overload`, `proof-docstring-body-mismatch`,
      // `proof-vacuous-hypotheses` — carrying **38 `genuine`, 56 `legit` and
      // 22 `advisory` agent verdicts** with them.
      //
      // Those verdicts are not recoverable by re-running anything: none of the
      // five categories is emitted by any script in the tree. Deleting them
      // discards the one thing the ledger exists to hold, and does it silently,
      // in a run whose printed summary says only "N candidate(s)".
      //
      // `OWNED` is derived from SEVERITY rather than hardcoded, so a category
      // added to this audit is covered automatically and one belonging to
      // another tool is left alone by default — the safe direction.
      const OWNED = new Set(Object.keys(SEVERITY));

      // SECOND AXIS of the same defect, measured 2026-09-13 (bean `qou-metc`).
      //
      // The `foreign` guard below distinguishes "fixed" from "not produced by
      // this scanner". It does NOT distinguish "fixed" from "NOT SCANNED", and
      // this loop cannot tell those apart either: an entry whose file the run
      // never visited looks exactly like one whose candidate stopped flagging.
      //
      // Measured cost, on this ledger: a `--review-ledger` run scoped to
      // `folio/quantum-observable-universe/lean` rewrote the file −863/+67,
      // destroying **106 of 329 entries** — every one of them in a category
      // this audit DOES produce, so `foreign` preserved none of them. The
      // ledger spans 22 roots across two papers and only 223 entries live under
      // that subtree.
      //
      // The `--json` path three hundred lines up already states this principle
      // for itself — *"a partial scan would overwrite it with a smaller count
      // that reads as a clean corpus"* — and refuses. The ledger path is the
      // other write path of the same API and never got the rule; that is
      // taxonomy row 33 (`qou-3ral`), a guard installed on one of several write
      // paths.
      //
      // Scoping the deletion is better than refusing: a partial scan stays
      // useful (it still resolves stale entries INSIDE what it looked at) and
      // can no longer touch what it did not look at.
      const scannedRel = new Set(files.map((f) => relative(REPO_ROOT, f)));
      let foreign = 0;
      let unscanned = 0;
      let missingOnDisk = 0;
      for (const k of Object.keys(led.entries)) {
        if (seen.has(k)) continue;
        const cat = k.slice(k.lastIndexOf("::") + 2);
        if (!OWNED.has(cat)) {
          foreign++;
          continue; // another tool's entry — not ours to resolve or delete
        }
        if (!scannedRel.has(k.slice(0, k.indexOf("::")))) {
          unscanned++;
          // A key naming a file that no longer exists is kept too: it cannot
          // be told apart from a rename (the content/ -> folio/ move left all
          // 325 keys pointing at missing paths, and deleting them would have
          // destroyed their verdicts). Count it so a human can re-key or
          // retire it; this loop never deletes it.
          if (!existsSync(resolve(REPO_ROOT, k.slice(0, k.indexOf("::")))))
            missingOnDisk++;
          continue; // this run never opened that file — absence is not evidence
        }
        delete led.entries[k];
      }
      if (foreign && !quiet)
        console.log(
          `  (preserved ${foreign} entr(ies) in categories this audit does not produce)`,
        );
      if (unscanned && !quiet)
        console.log(
          `  (preserved ${unscanned} entr(ies) in files this run did not scan)`,
        );
      if (missingOnDisk && !quiet)
        console.log(
          `  (${missingOnDisk} of those name a file that does not exist: renamed or deleted — re-key or retire by hand)`,
        );
      led.updated_at = nowIso;
      writeFileSync(p, JSON.stringify(led, null, 2) + "\n");
      if (!quiet)
        console.log(
          `\nreview ledger: ${candidates.length} candidate(s) — ${added} new, ${kept} confirmed, ${stale} stale (file changed); ${reviewLedger}`,
        );
    }

    if (checkLedger) {
      const p = resolve(REPO_ROOT, checkLedger);
      let led: { entries?: Record<string, Record<string, unknown>> } = {};
      if (existsSync(p)) {
        try {
          led = JSON.parse(readFileSync(p, "utf-8"));
        } catch {
          /* missing → all fail */
        }
      }
      const missing: string[] = [];
      for (const c of candidates) {
        const e = led.entries?.[c.key];
        if (
          !e ||
          !e.verdict ||
          e.verdict === "needs-agent" ||
          e.file_sha !== c.file_sha
        )
          missing.push(
            `${c.rel}:${c.line} [${c.category}/${c.pattern}] ${c.decl}`,
          );
      }
      if (missing.length) {
        console.error(
          `\n✗ agent-inspection gate: ${missing.length} candidate(s) lack a fresh agent verdict in ${checkLedger}:`,
        );
        for (const l of missing) console.error(`  ${l}`);
        ledgerFail = missing.length;
      } else {
        console.log(
          `\n✓ agent-inspection gate: all ${candidates.length} candidate(s) carry a fresh agent verdict.`,
        );
      }
    }
  }

  // Name the report only when one was actually written. Printing `jsonOut`
  // unconditionally made a partial scan look like it had just produced that
  // file's contents — which is the very confusion the write guard above exists
  // to prevent, restated in the summary line.
  const wroteReport = !(roots.length > 0 && !jsonExplicit);
  console.log(
    `\n${wroteReport ? jsonOut : "(partial scan — no report written)"} — scanned ${files.length} .lean, ${totalHits} defect candidate(s) across ${Object.keys(flagged).length} file(s) (${exemptHits} exempt${promotedHits ? `, ${promotedHits} promoted from a triage-pending exemption by a ledger \`genuine\` verdict` : ""}).`,
  );
  for (const c of ALL_CATEGORIES)
    if (counts[c]) console.log(`  ${c}: ${counts[c]}`);

  if (checkLedger && ledgerFail) process.exit(1);

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
