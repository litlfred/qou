/**
 * Registry of QA criteria the per-block sweep recognises.
 *
 * Each criterion is one independently-trackable audit dimension.
 * The sweep walker iterates the registry and, per block, decides
 * whether to run the automated checker or queue an agent / human
 * adjudication request.
 *
 * Domain buckets (current):
 *
 * - `voice` — scholarly voice + status-leak greps (extends
 *   `.claude/skills/local/one-voice-audit.md` with four new
 *   axes: scholarly-default, ai-slop, fit-section-chapter,
 *   framework-canonical, wall-side-correct).
 * - `fit` — does the block belong in its declared sub-section /
 *   section / chapter.
 * - `framework` — uses current canonical math (not deprecated
 *   notation, e.g. old 5-tuple, $\omega$ for fibre functor).
 * - `wall` — archimedean vs algebraic placement, per CLAUDE.md
 *   §7c base-ring convention.
 *
 * Future watchers (proof, canonical, compute, detangler) extend
 * the registry with their own criteria.
 *
 * @module content/pipeline/qa-criteria-registry
 */

import type { QaCriterionDefinition } from "../../folio-assistant/schemas/block-qa";

// ── Domain: voice ───────────────────────────────────────────────

const VOICE: QaCriterionDefinition[] = [
  {
    id: "voice-status-leak",
    domain: "voice",
    description:
      "No status markers in body prose (✅ Done, (TODO), (TBD), **Pending.**). " +
      "Work-tracker speech belongs in todos/, not in the paper.",
    default_severity: "critical",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-emoji-content",
    domain: "voice",
    description:
      "No emoji used as content (✅, ❌, ⚠, 🔧, 🚧) outside tables. In " +
      "tables, only compact comparison markers (✓ matches / ✗ diverges).",
    default_severity: "major",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-first-person-work",
    domain: "voice",
    description:
      "No first-person work tone: 'we'll add X', 'let me', 'needs more " +
      "work', 'I'll fix this'. These signal draft state, not paper authority.",
    default_severity: "major",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-time-stamped-notes",
    domain: "voice",
    description:
      "No time-stamped notes ('as of 2026-…', 'after the recent push', " +
      "'in the current draft'). The paper does not narrate its own draft history.",
    default_severity: "major",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-unicode-crash",
    domain: "voice",
    description:
      "No Unicode characters that crash pdflatex (↦, ⁻, √, ─, ✅, ·, ²) " +
      "outside preamble-mapped sets. Use LaTeX equivalents in math.",
    default_severity: "critical",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-editorializing",
    domain: "voice",
    description:
      "No editorialising phrases ('surprisingly', 'remarkably', " +
      "'interestingly', 'it is worth noting that', 'a beautiful result'). " +
      "Results speak for themselves.",
    default_severity: "minor",
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-scholarly-default",
    domain: "voice",
    description:
      "Block uses scholarly third-person voice by default. Applies to " +
      "both narrative .md AND proof bodies (Lean docstrings, expository " +
      "comments inside .lean). Exceptions require explicit author markers. " +
      "Heuristic-automated: second-person address, lecturer-cadence openers, " +
      "paper-past-tense narration. Borderline cases are confirmed / overruled " +
      "by an agent reviewer entry on the same sidecar.",
    default_severity: "major",
    // Applies to narrative prose independently of proofs; relaxed
    // to `["md"]` so prose-only blocks (no `.lean` sibling) still
    // run through the scholarly check.  Lean-docstring scanning is
    // dispatched per-block when the `.lean` is present (see the
    // dispatcher in `qa-checkers-voice.ts`).
    depends_on: ["md"],
    automated: true,
  },
  {
    id: "voice-ai-slop",
    domain: "voice",
    description:
      "No AI / status-update tells: 'Let me think about this', 'Here's " +
      "what I did', 'I'll go ahead and', 'Note that we should', 'Great " +
      "question', repeated First/Second/Third bullet cadence, over-use of " +
      "'essentially' / 'comprehensive' / 'leverage' / 'streamline' / 'robust'. " +
      "Heuristic-automated: direct LLM tells (zero false-positives in practice), " +
      "≥ 3 distinct hedge tokens in one .md (concentration signal), and " +
      "First/Second/Third comma-anchored sentence cadence. Borderline cases " +
      "are confirmed / overruled by an agent reviewer entry.",
    default_severity: "critical",
    depends_on: ["md"],
    automated: true,
  },
];

// ── Domain: fit ─────────────────────────────────────────────────

const FIT: QaCriterionDefinition[] = [
  {
    id: "fit-section-chapter",
    domain: "fit",
    description:
      "Block topic + kind fit the declared sub-section / section / " +
      "chapter context. Stranger-than-fiction blocks (off-topic, wrong " +
      "register, redundant with siblings) should move or be promoted / demoted.",
    default_severity: "major",
    depends_on: ["md", "ts"],
    automated: false,
  },
];

// ── Domain: framework ───────────────────────────────────────────

const FRAMEWORK: QaCriterionDefinition[] = [
  {
    id: "framework-canonical",
    domain: "framework",
    description:
      "Uses current canonical math framework, not deprecated notation. " +
      "Examples of deprecated forms: 5-tuple (M, Θ, G, P, E) instead of " +
      "(C, Θ, G, S); $\\omega$ for fibre functor (canonical: $\\tau$); " +
      "$\\mathcal{C}$ for category (canonical: $\\mathbf{C}$); $E$ alone for " +
      "exceptional divisor or state bundle; bare $H_q$ (now $\\mathcal{H}_q$, " +
      "$\\hat{H}_q$, or $H_n(q)$ depending on meaning).",
    default_severity: "major",
    // The automated checker only scans the .md body for deprecated
    // notation. The .ts manifest carries metadata, not prose; including
    // it here would over-stale on label-only edits.
    depends_on: ["md"],
    automated: true,
  },
];

// ── Domain: wall ────────────────────────────────────────────────

const WALL: QaCriterionDefinition[] = [
  {
    id: "wall-side-correct",
    domain: "wall",
    description:
      "Block is on the correct side of the substrate-to-archimedean " +
      "wall (CLAUDE.md §7c). Algebraic claims must NOT mention `ℝ`, " +
      "`Real.sqrt`, `Real.rpow`, `Real.log`, `Real.exp`, `linarith`, " +
      "`0 < q`, or other archimedean-specific constructs. Archimedean " +
      "blocks must declare `ℝ` (or LinearOrderedField) explicitly. " +
      "Each block belongs in either the algebraic substrate or the " +
      "archimedean specialisation, never both.",
    default_severity: "critical",
    // The automated checker scans .lean imports and the .md narrative
    // for an archimedean acknowledgement banner. The .ts manifest is
    // not read — kept out of depends_on to avoid spurious staleness.
    depends_on: ["md", "lean"],
    automated: true,
  },
];

// ── Exported registry ───────────────────────────────────────────

export const QA_CRITERIA_REGISTRY: QaCriterionDefinition[] = [
  ...VOICE,
  ...FIT,
  ...FRAMEWORK,
  ...WALL,
];

export const QA_CRITERIA_BY_ID: Record<string, QaCriterionDefinition> =
  Object.fromEntries(QA_CRITERIA_REGISTRY.map((c) => [c.id, c]));

export const QA_CRITERIA_BY_DOMAIN: Record<string, QaCriterionDefinition[]> =
  QA_CRITERIA_REGISTRY.reduce(
    (acc, c) => {
      (acc[c.domain] ??= []).push(c);
      return acc;
    },
    {} as Record<string, QaCriterionDefinition[]>,
  );

/**
 * The set of criteria the `one-voice-integration-watcher` is
 * responsible for. Other watchers register their own subsets.
 */
export const ONE_VOICE_WATCHER_CRITERIA: string[] = [
  ...VOICE.map((c) => c.id),
  ...FIT.map((c) => c.id),
  ...FRAMEWORK.map((c) => c.id),
  ...WALL.map((c) => c.id),
];
