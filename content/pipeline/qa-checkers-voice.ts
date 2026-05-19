/**
 * Automated checkers for `voice-*` / `framework-*` / `wall-*` QA
 * criteria. Each checker returns `result: "pass" | "fail"` plus
 * (on fail) evidence in the form `file:line: <quote>`.
 *
 * Coverage:
 *
 * - Eight voice criteria are now fully automated: status-leak,
 *   emoji-content, first-person-work, time-stamped-notes,
 *   unicode-crash, editorializing, **ai-slop** (heuristic LLM-tell
 *   detection), and **scholarly-default** (second-person address +
 *   lecturer cadence + past-tense narration).
 * - `framework-canonical` and `wall-side-correct` complete the
 *   automated set.
 * - Only `fit-section-chapter` remains agent-only — it requires
 *   semantic block-vs-section reasoning that no lexical heuristic
 *   captures faithfully.
 *
 * The automated checkers are conservative — they prefer
 * false-positive `fail` over false-negative `pass`. Agent entries
 * appended later via `qa-merge-findings.ts` overrule the script
 * entries when the script is being overzealous.
 *
 * @module content/pipeline/qa-checkers-voice
 */

import { readFileSync, existsSync } from "fs";

export interface CheckerHit {
  file: string;
  line: number;
  text: string;
}

export interface CheckerResult {
  result: "pass" | "fail";
  hits: CheckerHit[];
}

function readLines(path: string): string[] {
  return readSource(path).lines;
}

/**
 * Read a file once and return both the whole-file string and the
 * line array. Centralised so every checker uses the same access
 * pattern (avoids duplicate `readFileSync` calls + ambiguous
 * "line vs source" handling). Returns empty when the file is
 * absent so callers can treat missing input as a pass.
 */
function readSource(path: string): { src: string; lines: string[] } {
  if (!existsSync(path)) return { src: "", lines: [] };
  const src = readFileSync(path, "utf-8");
  return { src, lines: src.split("\n") };
}

function scan(
  path: string,
  re: RegExp,
  filter?: (line: string, idx: number, lines: string[]) => boolean,
): CheckerHit[] {
  const lines = readLines(path);
  const hits: CheckerHit[] = [];
  lines.forEach((l, i) => {
    if (re.test(l)) {
      if (filter && !filter(l, i, lines)) return;
      hits.push({ file: path, line: i + 1, text: l.trim().slice(0, 200) });
    }
  });
  return hits;
}

// ── voice-status-leak ───────────────────────────────────────────

const STATUS_LEAK_RE =
  /(\*\*Done\*\*|\*\*Completed\*\*|\*\*Pending\*?\*?|\(TODO\)|\(TBD\)|\bTODO:|\bFIXME:|\bXXX:|\bWIP\b|\bTO-DO\b)/;

export function checkStatusLeak(mdPath: string): CheckerResult {
  const hits = scan(mdPath, STATUS_LEAK_RE);
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── voice-emoji-content ─────────────────────────────────────────

const EMOJI_RE = /[✅❌⚠⏳🔧🚧☑☒✓✗★🎯🚀🔥]/;

export function checkEmojiContent(mdPath: string): CheckerResult {
  // ✓ and ✗ are allowed inside table rows for compact comparison
  // markers. Any OTHER emoji in a table row (or any emoji at all in
  // body prose) is a hit.
  const hits = scan(mdPath, EMOJI_RE, (l) => {
    if (l.trim().startsWith("|")) {
      // In a table row, flag iff at least one non-✓/✗ emoji is present.
      return /[✅❌⚠⏳🔧🚧☑☒★🎯🚀🔥]/.test(l);
    }
    // Body prose: every EMOJI_RE match is a hit.
    return true;
  });
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── voice-first-person-work ─────────────────────────────────────

const FIRST_PERSON_WORK_RE =
  /\b(we'?ll add|I'?ll (?:add|fix|update|do)|let me\b|needs more work|note to self|we should fix|TODO for me|gonna|here'?s what (?:I|we) (?:did|will))/i;

export function checkFirstPersonWork(mdPath: string): CheckerResult {
  const hits = scan(mdPath, FIRST_PERSON_WORK_RE);
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── voice-time-stamped-notes ────────────────────────────────────

const TIME_STAMPED_RE =
  /\b(as of 20\d{2}[- ]\d{2}|after the recent (?:push|merge|fix|rebase)|in the current draft|as currently written|prior to (?:the )?(?:recent )?(?:fix|push))\b/i;

export function checkTimeStampedNotes(mdPath: string): CheckerResult {
  const hits = scan(mdPath, TIME_STAMPED_RE);
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── voice-unicode-crash ─────────────────────────────────────────

// Source of truth: `.claude/skills/local/one-voice-audit.md` §1
// item 5 + §Workflow grep. Each of these characters crashes pdflatex
// unless explicitly mapped in the preamble.
const UNICODE_CRASH_RE = /[↦⁻√─✅❌⚠·²]/;

export function checkUnicodeCrash(mdPath: string): CheckerResult {
  // Allow inside fenced code blocks (```...```) since those don't go through pdflatex.
  const lines = readLines(mdPath);
  let inFence = false;
  const hits: CheckerHit[] = [];
  lines.forEach((l, i) => {
    if (/^```/.test(l.trim())) {
      inFence = !inFence;
      return;
    }
    if (inFence) return;
    if (UNICODE_CRASH_RE.test(l)) {
      hits.push({ file: mdPath, line: i + 1, text: l.trim().slice(0, 200) });
    }
  });
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── voice-editorializing ────────────────────────────────────────

const EDITORIALIZING_RE =
  /\b(surprisingly|remarkably|interestingly|notably|perhaps the most (?:surprising|important|significant)|it is worth noting that|the reader will (?:appreciate|note|see)|it turns out that|one might expect|a beautiful (?:result|theorem|proof)|an elegant proof)\b/i;

export function checkEditorializing(mdPath: string): CheckerResult {
  // Skip lines that are clearly in fenced code (Lean / TeX snippets).
  const lines = readLines(mdPath);
  let inFence = false;
  const hits: CheckerHit[] = [];
  lines.forEach((l, i) => {
    if (/^```/.test(l.trim())) {
      inFence = !inFence;
      return;
    }
    if (inFence) return;
    if (EDITORIALIZING_RE.test(l)) {
      hits.push({ file: mdPath, line: i + 1, text: l.trim().slice(0, 200) });
    }
  });
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── framework-canonical ─────────────────────────────────────────

/**
 * Deprecated notation patterns. Each pattern is a regex that must
 * NOT match outside fenced code blocks. We exempt explicit
 * "deprecated:" callouts so the paper can DISCUSS the old form.
 *
 * Patterns kept conservative — the goal is "flag for review", not
 * "auto-rewrite". The watcher's discharge band escalates to author
 * for any framework hit.
 */
const DEPRECATED_PATTERNS: Array<{ re: RegExp; what: string }> = [
  // 5-tuple — only flag literal "(M, Θ, G, P, E)" or close variants.
  {
    re: /\(M,\s*\\?varTheta,\s*G,\s*P,\s*E\)|\(M,\s*\\?Theta,\s*G,\s*P,\s*E\)/,
    what: "deprecated 5-tuple (M,Θ,G,P,E) — canonical is (𝐂, Θ, G, 𝒮)",
  },
  // ω for fibre functor — canonical is τ.
  {
    re: /\\omega\s*\\colon\s*\\mathbf\{C\}\s*\\to/,
    what: "deprecated $\\omega$ as fibre functor — canonical is $\\tau$",
  },
  // 𝒞 (calligraphic C) for category — canonical is 𝐂 (bold).
  {
    re: /\\mathcal\{C\}(?!_)/, // allow \mathcal{C}_q-style decorated forms
    what: "deprecated $\\mathcal{C}$ for category — canonical is $\\mathbf{C}$",
  },
  // Bare $H_q$ — three distinct objects share H_q; must be disambiguated.
  {
    re: /\$H_q\$/,
    what: "ambiguous $H_q$ — disambiguate as $\\mathcal{H}_q$, $\\hat{H}_q$, or $H_n(q)$",
  },
];

export function checkFrameworkCanonical(mdPath: string): CheckerResult {
  const lines = readLines(mdPath);
  let inFence = false;
  const hits: CheckerHit[] = [];
  lines.forEach((l, i) => {
    if (/^```/.test(l.trim())) {
      inFence = !inFence;
      return;
    }
    if (inFence) return;
    // Skip lines that explicitly call out the deprecated form
    // (e.g. "deprecated:", "old form", "use ... instead").
    if (/\b(deprecated|legacy|use .* instead|never write)\b/i.test(l)) return;
    for (const { re, what } of DEPRECATED_PATTERNS) {
      if (re.test(l)) {
        hits.push({
          file: mdPath,
          line: i + 1,
          text: `${l.trim().slice(0, 160)}  [${what}]`,
        });
      }
    }
  });
  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── wall-side-correct ───────────────────────────────────────────

/**
 * Heuristic archimedean-marker detection in Lean. A block whose
 * `.lean` mentions any of these is on the archimedean side.
 * Cross-checked against the `.md` to flag mixed claims.
 */
const ARCHIMEDEAN_LEAN_RE =
  /\b(Real\.sqrt|Real\.rpow|Real\.log|Real\.exp|Real\.cos|Real\.sin|Real\.pi|linarith|positivity|norm_num|nlinarith|\(ℝ\)|: ℝ\b|: Real\b|LinearOrderedField)\b/;

const ALGEBRAIC_LEAN_RE = /\b(CommRing|Field|GroupWithZero|\{R : Type\*\}|\(R := |variable \{R\b)/;

/**
 * Block is wall-correct iff:
 *   - it has no .lean, OR
 *   - .lean is purely algebraic (no archimedean markers), OR
 *   - .lean is purely archimedean (no generic-R markers in same file),
 *     and the .md does not contradict the placement.
 *
 * Mixed signals (both archimedean AND generic-R markers, or
 * archimedean markers without the .md acknowledging archimedean
 * specialisation) get flagged.
 */
export function checkWallSide(
  mdPath: string | undefined,
  leanPath: string | undefined,
): CheckerResult {
  if (!leanPath || !existsSync(leanPath)) {
    return { result: "pass", hits: [] };
  }
  const leanSrc = readFileSync(leanPath, "utf-8");
  // Strip Lean block comments (/- ... -/) AND line comments (-- ...)
  // to reduce false positives when archimedean markers appear inside
  // narrative comments of an otherwise-algebraic file.
  const stripped = leanSrc.replace(/\/-[\s\S]*?-\/|--.*$/gm, "");
  const isArchimedean = ARCHIMEDEAN_LEAN_RE.test(stripped);
  const isAlgebraic = ALGEBRAIC_LEAN_RE.test(stripped);
  const hits: CheckerHit[] = [];

  if (isArchimedean && isAlgebraic) {
    hits.push({
      file: leanPath,
      line: 1,
      text:
        "Lean file contains both archimedean (ℝ / Real.* / linarith) AND " +
        "generic-R (CommRing / {R : Type*}) markers — split into two files " +
        "per CLAUDE.md §7c.",
    });
  }

  if (isArchimedean && mdPath && existsSync(mdPath)) {
    const md = readFileSync(mdPath, "utf-8");
    // Archimedean is fine if the .md acknowledges the specialisation.
    // Without acknowledgement we flag for review.
    const acknowledged =
      /archimedean|over\s+\\?mathbb\{R\}|over\s+ℝ|specialise|specialize|numerical evaluation|CODATA|experimental/.test(
        md.toLowerCase(),
      );
    if (!acknowledged) {
      hits.push({
        file: leanPath,
        line: 1,
        text:
          "Lean file uses archimedean constructs but .md narrative does " +
          "not acknowledge archimedean specialisation. Add a §7c-style " +
          "banner or move the archimedean evaluation to a sibling block.",
      });
    }
  }

  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── voice-ai-slop ───────────────────────────────────────────────

/**
 * Direct LLM tells — phrases that should NEVER appear in published
 * scholarly prose. These produce zero false-positives in practice;
 * any hit is a real ai-slop violation.
 */
const AI_SLOP_DIRECT_RE =
  /\b(let me (?:think|clarify|explain|address|now|first|see)|here'?s what (?:I|we)(?: did| will| have)?|I'?ll (?:go ahead|now|first|address|explain)|great question|let'?s (?:explore|dive (?:in|into)|unpack|examine)|note that we should|it'?s (?:important|worth) (?:to note|noting) that|delve (?:into|in)|in (?:a )?nutshell)\b/i;

/**
 * Hedging / softener language frequently inserted by LLMs but
 * inappropriate in a precise mathematical paper. Conservative —
 * single-word hits should be a hint, not necessarily a violation.
 * We treat *combinations* (≥ 3 distinct tokens in the same block)
 * as the actual signal — the threshold balances catching real
 * LLM-output concentrations against the false-positive rate on
 * legitimate technical writing that uses one or two of these words
 * naturally.
 */
const AI_SLOP_HEDGE_TOKENS = [
  /\bessentially\b/i,
  /\bcomprehensive(ly)?\b/i,
  /\bleverag(e|ing|es)\b/i,
  /\bstreamlin(e|ing|es)\b/i,
  /\brobust(ly|ness)?\b/i,
  /\boverall(?:,|\s+then)?\b/i,
  /\bin (?:summary|conclusion),/i,
  /\bcrucial(ly)?\b/i,
];

/**
 * Lecturer "First, ... Second, ... Third, ..." cadence used as a
 * structural crutch. Strictly: the same prose block must contain
 * "First," and "Second," (as sentence openers) AND "Third," or
 * "Finally,". Real scholarly use of these words in math context
 * (e.g. "First-order term...") will NOT match the comma-anchored
 * pattern.
 */
const AI_SLOP_FIRST_SECOND_THIRD_RE =
  /\bFirst,\s.*?\bSecond,\s.*?\b(?:Third|Finally),\s/is;

export function checkAiSlop(mdPath: string): CheckerResult {
  const { src, lines } = readSource(mdPath);
  if (!src) return { result: "pass", hits: [] };

  const hits: CheckerHit[] = [];

  // Pass 1 — direct LLM tells (line-by-line so we can cite line).
  let inFence = false;
  lines.forEach((l, i) => {
    if (/^```/.test(l.trim())) {
      inFence = !inFence;
      return;
    }
    if (inFence) return;
    if (AI_SLOP_DIRECT_RE.test(l)) {
      hits.push({ file: mdPath, line: i + 1, text: l.trim().slice(0, 200) });
    }
  });

  // Pass 2 — hedge-token concentration. Strip code fences first;
  // count distinct hedge tokens in the remaining prose. ≥ 3 distinct
  // hedge tokens in one .md file is the signal.
  const proseOnly = src.replace(/```[\s\S]*?```/g, "");
  const distinctHedges = AI_SLOP_HEDGE_TOKENS.filter((re) =>
    re.test(proseOnly),
  );
  if (distinctHedges.length >= 3) {
    hits.push({
      file: mdPath,
      line: 1,
      text: `hedge-token concentration: ${distinctHedges.length} distinct AI-slop softener tokens present (essentially / comprehensive / leverage / streamline / robust / crucial / etc.)`,
    });
  }

  // Pass 3 — First/Second/Third cadence (whole-file scan).
  if (AI_SLOP_FIRST_SECOND_THIRD_RE.test(proseOnly)) {
    // Find the line for the first "First," opener.
    const idx = lines.findIndex((l) => /\bFirst,\s/.test(l));
    hits.push({
      file: mdPath,
      line: idx >= 0 ? idx + 1 : 1,
      text: "First/Second/Third bullet cadence — characteristic LLM structural crutch",
    });
  }

  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── voice-scholarly-default ─────────────────────────────────────

/**
 * Second-person address — the paper addresses the mathematics, not
 * the reader. "you can see", "the reader will note", etc. are
 * non-scholarly.
 */
const SECOND_PERSON_RE =
  /\b(you (?:can|will|note|see|may|might|should|need|have|are|now)|the reader (?:will|can|may|might|should))\b/i;

/**
 * Lecturer cadence — informal sentence openers more at home in a
 * lecture than a paper.
 */
const LECTURER_OPENER_RE =
  /^\s*(?:So (?:what (?:we|I)(?:'re)?(?: going to)?(?: do)?|let'?s|now)|Now (?:we (?:want|need|will|are|have)|let'?s)|Alright|Okay|Well,)/i;

/**
 * Past-tense narration of the paper's own derivation. Paper voice
 * is present-tense for definitions and theorems; past-tense reads
 * as draft narration. Pattern: "we constructed", "we defined",
 * "we showed", "we proved" — limited to first-person plural since
 * generic past tense is fine in proofs ("Hilbert proved ...").
 */
const PAPER_PAST_TENSE_RE =
  /\b(we (?:constructed|defined|showed|proved|established|derived|computed|verified)) (?:above|earlier|before|in the (?:previous|preceding))/i;

export function checkScholarlyDefault(
  mdPath: string,
  leanPath: string | undefined,
): CheckerResult {
  const { lines } = readSource(mdPath);
  if (lines.length === 0) return { result: "pass", hits: [] };

  const hits: CheckerHit[] = [];

  // Scan .md. Fenced code blocks (```) are skipped via `inFence`;
  // HTML-style `<!-- ... -->` and inline comments are intentionally
  // NOT stripped because they render as visible text in the
  // markdown pipeline (and so are part of paper voice).
  let inFence = false;
  lines.forEach((l, i) => {
    if (/^```/.test(l.trim())) {
      inFence = !inFence;
      return;
    }
    if (inFence) return;
    if (SECOND_PERSON_RE.test(l)) {
      hits.push({ file: mdPath, line: i + 1, text: l.trim().slice(0, 200) });
    }
    if (LECTURER_OPENER_RE.test(l)) {
      hits.push({ file: mdPath, line: i + 1, text: l.trim().slice(0, 200) });
    }
    if (PAPER_PAST_TENSE_RE.test(l)) {
      hits.push({ file: mdPath, line: i + 1, text: l.trim().slice(0, 200) });
    }
  });

  // Also scan Lean docstrings — proof bodies share the scholarly
  // standard. Look at /-! ... -/ module docs and /-- ... -/ decl
  // docstrings; line comments (-- ...) are skipped (they're code
  // annotations, not prose).
  if (leanPath && existsSync(leanPath)) {
    const leanSrc = readFileSync(leanPath, "utf-8");
    // Extract docstring spans only; everything else is code.
    const docs = [...leanSrc.matchAll(/\/-!?[\s\S]*?-\//g)].map((m) => m[0]);
    const docsText = docs.join("\n");
    if (SECOND_PERSON_RE.test(docsText)) {
      hits.push({
        file: leanPath,
        line: 1,
        text: "Lean docstring uses second-person address",
      });
    }
    if (LECTURER_OPENER_RE.test(docsText)) {
      hits.push({
        file: leanPath,
        line: 1,
        text: "Lean docstring uses lecturer-cadence opener",
      });
    }
  }

  return { result: hits.length > 0 ? "fail" : "pass", hits };
}

// ── Dispatch table ──────────────────────────────────────────────

export const AUTOMATED_CHECKERS: Record<
  string,
  (paths: { md?: string; ts?: string; lean?: string }) => CheckerResult
> = {
  "voice-status-leak": (p) =>
    p.md ? checkStatusLeak(p.md) : { result: "pass", hits: [] },
  "voice-emoji-content": (p) =>
    p.md ? checkEmojiContent(p.md) : { result: "pass", hits: [] },
  "voice-first-person-work": (p) =>
    p.md ? checkFirstPersonWork(p.md) : { result: "pass", hits: [] },
  "voice-time-stamped-notes": (p) =>
    p.md ? checkTimeStampedNotes(p.md) : { result: "pass", hits: [] },
  "voice-unicode-crash": (p) =>
    p.md ? checkUnicodeCrash(p.md) : { result: "pass", hits: [] },
  "voice-editorializing": (p) =>
    p.md ? checkEditorializing(p.md) : { result: "pass", hits: [] },
  "voice-ai-slop": (p) =>
    p.md ? checkAiSlop(p.md) : { result: "pass", hits: [] },
  "voice-scholarly-default": (p) =>
    p.md ? checkScholarlyDefault(p.md, p.lean) : { result: "pass", hits: [] },
  "framework-canonical": (p) =>
    p.md ? checkFrameworkCanonical(p.md) : { result: "pass", hits: [] },
  "wall-side-correct": (p) => checkWallSide(p.md, p.lean),
};
