# Backlog: ingest uploaded-paper results (citations + per-paper Lean + wrapper-for-overlap)

**Date:** 2026-06-08 · **Requested by:** owner · **Status:** backlog (workflow +
inventory). Seeded by [commit 4183cd9e](https://github.com/litlfred/qou/commit/4183cd9ecb624fc70afdd7644e8ece7e4fb574a3)
(owner uploaded the two DLM papers).

## The task

For every paper in [`library/`](../../library/), **pull in its results** using the
paper-ingestion skills (`local/paper-importer`, `local/document-intake`), with the
**specific relevant citations**, under three organizing principles:

1. **Bib first.** Each ingested result gets a `references.ts` entry (CSL-JSON via
   the `ref()` builder) and is `\cite{}`-d wherever QOU uses it. The `\cite` must
   point at the *specific theorem/section* relied on, not just the paper.
2. **Lean organized by papers.** Formalized results of an external paper live in a
   **per-paper Lake package / namespace** (the existing pattern: `qou`, `ugb`,
   `fred2005`). A newly-ingested paper whose results we formalize gets its own
   package (or a clearly-namespaced module), not scattered into `QOU`.
3. **Wrapper-for-overlap (no duplication).** If a QOU result overlaps an uploaded
   paper's result, QOU's Lean should **import/wrap** the paper's formalization (a
   thin wrapper specialising their statement to the QOU setting), **not re-prove**
   it. Where the paper is not formalized, QOU states it as an `axiom`/`class` with
   a `-- Ref:` to the paper (per the §3b conjectural-class convention) and wraps
   that. This is the same move as the KS algebraic-shortcut remarks
   ([`ks-multiplicativity-via-markov`](../../content/quantum-observable-universe/mass-theory/ks-multiplicativity-via-markov.md))
   — cite the heavy original, give the QOU specialisation.

## Seed (item 1): the DLM papers — just uploaded, already used

- `library/arxiv-gr-qc-0407051v2/0407051v2.pdf` — **Domagała–Lewandowski**, *Black hole entropy from
  quantum geometry* (Class. Quantum Grav. 21 (2004) 5233).
- `library/arxiv-gr-qc-0407052v1/0407052v1.pdf` — **Meissner**, *Black hole entropy in loop quantum
  gravity* (Class. Quantum Grav. 21 (2004) 5245).
- **Relevant results to cite:** the horizon state-count + projection-constraint
  combinatorics (DL); the Immirzi-fixing criticality equation (Meissner). These
  are *already used by name* in
  [`2026-06-08-spin-network-count-q-dimension-partition-function.md`](../audits/2026-06-08-spin-network-count-q-dimension-partition-function.md).
- **Action:** add `domagala-lewandowski-2004` + `meissner2004` to
  `content/schema/references.ts`; switch the spin-network note (and any promoted
  content block) to `\cite{}` them. No QOU Lean overlap yet (the area-operator
  block is not formalized) → no wrapper needed until the spin-network derivation
  is promoted to content.

## Inventory of `library/` (ingestion status — verify each)

| File | Paper (best-known) | Already cited? | Lean overlap? |
|---|---|---|---|
| `0407051`, `0407052` | DLM (LQG BH entropy) | **no → item 1** | none yet |
| `0811.2435` | Kontsevich–Soibelman (DT/WCF) | yes (`kontsevich-soibelman-2008`) | KS shortcut remarks (cite, not wrap) |
| `0409565` | unital Gröbner bases / simpler PBW (UGB) | check (`bokut*`?) | **wrap** — UGB is an in-repo paper (`ugb` package) |
| `1007.1250` | Yekutieli, multiplicative integration | check (`yekutieli2015`) | non-abelian-Stokes (cite) |
| `1203.4538` | Kuhlmann–Matusiński (surreal exp-log) | yes (cited in surreal probe) | none |
| `2111.06645` | Garoufalidis–Zagier (Kashaev/quantum-modularity) | check (`garoufalidis-zagier-2024`) | Kashaev/volume (cite) |
| `0008040` | Marsh (Lusztig cone / canonical basis) | check | KLR/crystal (cite) |
| `0405508` | Geck–Lambropoulou (Markov trace) | check | Markov trace (possible wrap) |
| `0911.4494` | Webster–Williamson (geometry of Markov traces) | yes (`webster-williamson-2014-markov`) | Markov (cite) |
| `9806163` | Orellana (Markov weights) | flagged (Halverson/Orellana key conflation) | Markov (cite) |
| `9909088` | Franecki–Kapranov (microlocal/constructible) | yes (`franecki-kapranov-1999`) | none |
| `bujack-et-al-2022` | non-Riemannian perceptual colour space | check | none (colour/perception) |
| `bach2013` (+`-import-meta.json`) | double-slit (has `bach2013-double-slit` content dir) | check | possible (double-slit content) |
| `centsim`, `HDR`, `6gtx-j455`, `9911033`, `1210.6243`, `2104.06067`, `2605.22763`, `2605.28781` | **UNVERIFIED — identify on ingestion** | ? | ? |
| `mass_1.mas20.txt` | AME mass table (data, not a paper) | data-pin, not a citation | n/a |

## Skill + workflow updates (part of this backlog)

- **`local/paper-importer`** — add a "results-ingestion + citation" step: extract the
  specific cited theorems, mint `references.ts` entries, and decide Lean
  placement (own package vs wrapper) per the overlap rule.
- **`local/document-intake`** — record per-upload ingestion status (cited? Lean
  wrapped?) so `library/intake.json` tracks it.
- **`local/coordinate` / bib audit** — extend `validate-references` (or a new
  `uploads-ingestion-audit`) to flag **uploaded papers with no `references.ts`
  entry** and **QOU results that overlap an uploaded paper but don't wrap/cite
  it**. Add this check to the integration/bib workflow (CI `audit` or
  witness-pipeline).
- **`local/integration-watcher`** — a new axis: "uploaded-paper ingestion" (is
  every `library/*.pdf` either cited or marked not-relevant; is overlap wrapped).

## Order of work (when picked up)

1. DLM refs (item 1) — small, unblocks the spin-network promotion.
2. Verify/identify the UNVERIFIED uploads (one `document-intake` pass).
3. Per-paper: mint citations → place Lean (own package or wrapper) → wire.
4. Skill + bib-audit updates (so this stays enforced, not one-off).

**Note:** this is a multi-session effort. Do not bulk-ingest blindly — one paper
at a time, citation-accurate, with the overlap/wrapper decision explicit per
paper (canonical-watcher + bib-validate gate each).
