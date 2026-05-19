/**
 * bib-verification.ts — per-paper verification status for the QOU
 * bibliography, complementing `references.ts` (which is pure CSL-JSON
 * metadata).
 *
 * Each entry records whether the corresponding ref in `references.ts`
 * has been verified against a local PDF (in `uploads/`) — when, by
 * whom, how many citation sites were checked, and how many corrections
 * were committed. Consumers:
 *
 *   - `content/pipeline/bib-qa.ts` reads this to emit the
 *     `verification_status` QA tag (added 2026-05-19; see
 *     `.claude/skills/local/bib-qa.md §"QA Tags"`).
 *   - The standalone dashboard at `folio-assistant/ui/bib-qa.html`
 *     displays it in the per-reference detail panel.
 *   - The `local/bib-qa` skill walks this list to identify entries
 *     still in `pending` status when grinding through backlog.
 *
 * Schema is intentionally minimal — it's a status sidecar, not a
 * full audit trail (that lives in `docs/coordination/<date>-bib-
 * verification-ledger.md`).
 *
 * Authoring note: every entry should have a corresponding
 * `references.ts` entry with the same `id`. The
 * `validate-references.ts` validator checks this cross-reference;
 * orphan verification entries (id not in references.ts) are flagged.
 */

export type VerificationStatus =
  /** Not yet examined. */
  | "pending"
  /** Every citation site checked; descriptions match paper content;
   *  no fix needed. */
  | "verified-clean"
  /** Some citations verified + fixed; others still need work. */
  | "partial"
  /** Misattributions resolved; entry is correctness-clean. */
  | "fixed"
  /** Paper is in references.ts but has zero `-- Ref:` / `\cite`
   *  consumer in content/ — awaits author decision (keep / remove
   *  / find use). */
  | "uncited"
  /** The local PDF does not match the metadata in `references.ts`
   *  (it's a different work) — escalate to user. */
  | "paper-mismatch"
  /** Paper not in `uploads/`; cannot verify against local copy.
   *  May become `verified-clean` later if intake succeeds. */
  | "unfetchable";

export interface BibVerification {
  /** Must match a `ref({ id })` in content/schema/references.ts. */
  id: string;
  /** Current status; updated by verifying agents. */
  status: VerificationStatus;
  /** Count of `-- Ref: [<id>]` lines in `.lean` files. */
  lean_sites: number;
  /** Count of `\cite{<id>}` / `[@<id>]` occurrences in `.md`. */
  md_sites: number;
  /** Path to the local copy under `uploads/` (if present). */
  local_pdf?: string;
  /** ISO 8601 timestamp of the most recent verification action. */
  verified_at?: string;
  /** Free-text identifier of the verifier ("Claude (claude-opus-4-7)",
   *  "litlfred", or a GitHub username). */
  verified_by?: string;
  /** Number of bib-metadata corrections committed during verification. */
  fixes_applied: number;
  /** Git commit SHA where the most recent fix was applied (12-char
   *  prefix is sufficient; full SHA also OK). */
  fix_commit?: string;
  /** Optional free-text note (≤ 200 chars; longer notes go in the
   *  markdown ledger). */
  note?: string;
}

/**
 * Initial verification status for the 22-paper intake batch landed
 * on `claude/upload-bib-papers-2026-05-19`. Most entries are
 * `pending`; `boyd-vandenberghe-2004` is `partial` after 4
 * misattribution fixes committed in `66b3caf7f`.
 */
export const bibVerifications: BibVerification[] = [
  {
    id: "boyd-vandenberghe-2004",
    status: "partial",
    lean_sites: 11,
    md_sites: 0,
    local_pdf: "uploads/boyd-vandenberghe-2004-convex-optimization.pdf",
    verified_at: "2026-05-19T05:50:00Z",
    verified_by: "Claude (claude-opus-4-7)",
    fixes_applied: 4,
    fix_commit: "66b3caf7f",
    note: "§5.5.3→§5.5.2, §5.5.4→§5.5.2+alizadeh, Thm 5.5→§5.2.3+§5.3, §A.5.3→§A.5.5. 9 generic Refs still need §-specific updates.",
  },
  { id: "codata2022", status: "pending", lean_sites: 5, md_sites: 0,
    local_pdf: "uploads/codata-2022-constants.txt", fixes_applied: 0 },
  { id: "leitnerpawloski2004", status: "pending", lean_sites: 3, md_sites: 4,
    local_pdf: "uploads/leitnerpawloski2004.pdf", fixes_applied: 0 },
  { id: "yekutieli2008", status: "pending", lean_sites: 2, md_sites: 2,
    local_pdf: "uploads/yekutieli2008.pdf", fixes_applied: 0 },
  { id: "zink2002", status: "pending", lean_sites: 1, md_sites: 1,
    local_pdf: "uploads/zink2002.pdf", fixes_applied: 0 },
  { id: "freed2010", status: "pending", lean_sites: 1, md_sites: 1,
    local_pdf: "uploads/freed2010.pdf", fixes_applied: 0 },
  { id: "berarducci2018", status: "pending", lean_sites: 1, md_sites: 0,
    local_pdf: "uploads/berarducci-mantova-2018-surreal-derivations.pdf", fixes_applied: 0 },
  { id: "faddeev_kashaev1994", status: "pending", lean_sites: 1, md_sites: 0,
    local_pdf: "uploads/faddeev-kashaev-1994-quantum-dilogarithm.pdf", fixes_applied: 0 },
  { id: "baez2004", status: "pending", lean_sites: 1, md_sites: 0,
    local_pdf: "uploads/baez2004.pdf", fixes_applied: 0 },
  { id: "hu-mathas2012graded", status: "pending", lean_sites: 1, md_sites: 0,
    local_pdf: "uploads/hu-mathas2012graded.pdf", fixes_applied: 0 },
  { id: "klein1888", status: "pending", lean_sites: 1, md_sites: 1,
    local_pdf: "uploads/klein1888.pdf", fixes_applied: 0,
    note: "17 MB book scan; verify pp. citing Klein's icosahedron / Bring's surface only." },
  { id: "pham1965", status: "pending", lean_sites: 1, md_sites: 0,
    local_pdf: "uploads/pham1965.pdf", fixes_applied: 0 },
  { id: "oeis-A006752", status: "pending", lean_sites: 1, md_sites: 0,
    local_pdf: "uploads/oeis-A006752.txt", fixes_applied: 0,
    note: "Numeric data — verify Catalan's constant value match." },
  { id: "mostow1968", status: "pending", lean_sites: 0, md_sites: 2,
    local_pdf: "uploads/mostow1968.pdf", fixes_applied: 0 },
  { id: "bufetov2020", status: "pending", lean_sites: 0, md_sites: 1,
    local_pdf: "uploads/bufetov2020.pdf", fixes_applied: 0 },
  // Uncited (in references.ts but no -- Ref: / \cite consumer anywhere)
  { id: "gromov1982", status: "uncited", lean_sites: 0, md_sites: 0,
    local_pdf: "uploads/gromov1982.pdf", fixes_applied: 0,
    note: "Bib orphan; decision pending (keep / remove / find use)." },
  { id: "bilsonthompson2005", status: "uncited", lean_sites: 0, md_sites: 0,
    local_pdf: "uploads/bilsonthompson2005.pdf", fixes_applied: 0,
    note: "Bib orphan; decision pending." },
  { id: "finster2021", status: "uncited", lean_sites: 0, md_sites: 0,
    local_pdf: "uploads/finster2021.pdf", fixes_applied: 0,
    note: "Bib orphan (causal fermion systems — wave functions); decision pending." },
  { id: "finster2022", status: "uncited", lean_sites: 0, md_sites: 0,
    local_pdf: "uploads/finster2022.pdf", fixes_applied: 0,
    note: "Bib orphan (causal fermion systems — baryogenesis); decision pending." },
  { id: "finster2024", status: "uncited", lean_sites: 0, md_sites: 0,
    local_pdf: "uploads/finster2024.pdf", fixes_applied: 0,
    note: "Bib orphan (causal fermion systems — collapse theory); decision pending." },
  { id: "dappiaggi2024", status: "uncited", lean_sites: 0, md_sites: 0,
    local_pdf: "uploads/dappiaggi2024.pdf", fixes_applied: 0,
    note: "Bib orphan (holographic mixing in causal fermion systems); decision pending." },
  { id: "blitvic2012", status: "uncited", lean_sites: 0, md_sites: 0,
    local_pdf: "uploads/blitvic2012.pdf", fixes_applied: 0,
    note: "Bib orphan ((q,t)-Gaussian process); decision pending." },
];

/** Lookup map for O(1) verification status by id. */
export const bibVerificationMap = new Map(
  bibVerifications.map((v) => [v.id, v])
);

/** Get verification status for a given ref id. */
export function getBibVerification(id: string): BibVerification | undefined {
  return bibVerificationMap.get(id);
}

/** All ref ids that have a verification entry. */
export function allVerifiedRefIds(): string[] {
  return bibVerifications.map((v) => v.id);
}
