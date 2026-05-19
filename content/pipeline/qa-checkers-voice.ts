/**
 * Automated checkers for `voice-*` / `framework-*` / `wall-*` QA
 * criteria. Each checker returns `result: "pass" | "fail"` plus
 * (on fail) evidence in the form `file:line: <quote>`.
 *
 * Non-automated criteria (scholarly-default, ai-slop, fit-section-
 * chapter) are NOT covered here — they require agent / human
 * adjudication, which the watcher dispatches separately.
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
  if (!existsSync(path)) return [];
  return readFileSync(path, "utf-8").split("\n");
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
  // Allow ✓/✗ inside table rows (pipe-delimited).
  const hits = scan(mdPath, EMOJI_RE, (l) => {
    // Tolerate explicit table rows starting/containing `|`.
    if (l.trim().startsWith("|") && /✓|✗/.test(l) && !/[✅❌⚠⏳🔧🚧]/.test(l))
      return false;
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
  // Strip block comments to reduce false positives on documentation.
  const stripped = leanSrc.replace(/\/-([\s\S]*?)-\//g, "");
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
  "framework-canonical": (p) =>
    p.md ? checkFrameworkCanonical(p.md) : { result: "pass", hits: [] },
  "wall-side-correct": (p) => checkWallSide(p.md, p.lean),
};
