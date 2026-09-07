# Upload triage — eight q-difference / Stokes documents (2026-09-07)

**Skill:** `local/paper-relevance-triage`, one document at a time. **Bean:**
`qou-2akx` (session milestone; the five action beans hang under it).
**Branch:** `claude/qdiff-stokes-triage-2026-09-07`. **Assessor:** agent
(`claude-opus-5`) — every verdict below is an agent claim awaiting
adjudication, per the ledger's `assessed_by` discipline.

**Why these eight.** The owner uploaded them for the framework's Stokes /
`A_ω` arc — the off-diagonal Stokes constant `A_ω = 3` (`conj:stokes-dt-bps-bridge`,
bean `qou-arc1`, the `A_ω → S` negative `qou-q3np`), the q-difference side of the
fibre-level objects (Habiro / KZ / q-holonomic), the `qbeta` Habiro element and the
convention-C `c_k` ladder (`qou-cds1`). The triage's first finding is about that
framing: **none of the eight touches `A_ω`, the DT/BPS bridge, or the `c_k`
ladder.** They are q-difference *Galois / Stokes-sheaf / q-Borel* literature, and
their consumers in this corpus are the q-difference-module files of the C1 arc —
`QOU/Mathlib/QAlienBridgeEquation.lean` (`qou-vkg5`),
`QOU/MathlibExt/QBorelKernel*.lean`, `QOU/MathlibExt/RSZIsoformalInterface.lean`,
bean `qou-wgnx` — plus one mass-theory Lean file with a wrong library pointer.
`A_omega` / `A_ω` grep 6 + 47 content files and 44 + 19 `computations/qbeta` files,
and not one of them names Ramis, Sauloy, van der Put, Morita, Dreyfus or
Chatzidakis.

## Verdict table

| # | document (`library/…`) | ref id | verdict | key results (in-source locators) | actions | beans |
|---|---|---|---|---|---|---|
| 1 | `arxiv-math-0409393v1` | `sauloy2004` (new) | **supporting** | Prop 4.1 (Stokes sheaf = vector bundle of `End^{>0}(M0)` over `E_q`; one slope ⇒ trivial); Thm 3.7 (canonical resummation along a divisor direction `D`); Thm 3.18 (`F(M0) ≅ H¹(E_q, Λ_I(M0))`, algebraic proof) | add-reference (done); cite-in-block `RSZIsoformalInterface.lean` | `qou-vsho` |
| 2 | `arxiv-math-0611521v1` | `ramis-sauloy2006` (new) | **core** | Prop 2.5 + eq. (6) (Stokes operator = ambiguity between two q-directions `c, d ∈ E_q`); Thm 3.3 (`S_{c0,c} ∈ St(A)`); **Thm 3.5** (q-alien derivations = residues of `log S`, in `st(A)`, level-graded eq. 16); Thm 3.6 (Lie-like ⊗-endomorphisms); Thm 3.8 / 3.9 (level-δ q-Borel invariants complete; ↔ alien-derivation invariants by a theta power); §4 item 1 (Écalle programme, open) | add-reference (done); cite-in-block `QAlienBridgeEquation.lean`; cite-in-block `QBorelKernel.lean` | `qou-at59`, `qou-x0aa` |
| 3 | `arxiv-math-0612592v1` | `vanderput2006` (new) | **supporting** | Thm 3.4 / 3.5 (`E(cz^{t/n})` pure irreducible slope `t/n`; every irreducible is one; indecomposables `E ⊗ U_m`); §5 (1), (5) + Remarks 5.1 (Galois group: torus of characters × `G_a`; `1 → U_ξ → Gal(M) → Gal(gr M) → 1`, semi-direct; `Gal^o` solvable; algorithmic) | add-reference (done); cite-in-block `BindingScalarKernelParityExclusion.lean` **and fix the `crmath-2011` mis-pointer** | `qou-86p5` |
| 4 | `arxiv-0705.2975v1` | — | **tangential** | (none consumed) Thm 2.9, Thm 3.1: the Picard–Vessiot, weak-PV-field, tannakian and model-theoretic Galois groups agree over the algebraic closure of the constants | no-action | — |
| 5 | `arxiv-0903.0853v3` | `ramis-sauloy-zhang2013` (exists) | **core** (row unchanged, current) | row's §1.3.2 / §2.2 / §2.3.2 / Thm 3.3.5 locators re-verified in the ledger's own rationale; `source_sha d4295d4b18b2` re-measured = current | none new; the row's "8 citation sites" is now low — 12 `-- Ref:` sites on this tree | — |
| 6 | `arxiv-1205.1453v2` | `morita2012b` (new) | **supporting** | Thm 1 (§3.2) + Cor 1 (first-kind q-Borel–Laplace of bilateral `₁ψ₀` in direction `λ` = theta-quotient product; connection coefficient q-elliptic); eq. (19)–(20) (the degenerate first-order equation `₁ψ₀` solves); Thm 2 (`q → 1` gives `₁H₀`) | add-reference (done); cite-in-block `QBorelKernel.lean` | `qou-89w7` |
| 7 | `arxiv-1404.2541v1` | `morita2014` (exists) | **supporting** (row **corrected**) | Thm 3.1 / 7.1 (Ramanujan-equation connection formulae), Thm 8.3 / 9.3 (level `r−1` extension) — unchanged from the 2026-08-08 assessment | add-reference marked **done** (`qou-zdty` completed); cite-in-block still open | `qou-hnuw` (existing, todo) |
| 8 | `arxiv-2208.13448v2` | — | **tangential** | (none consumed) §6.4 algorithm for order-3 difference Galois groups (Case Q included); Thm 6.13 (Zudilin's Rogers–Ramanujan double sum: `GL_3`); Thm 7.1 (∂-transcendence criterion, order 3) | no-action | — |

Refs created (`content/schema/references.ts`, commit `15519eba39`):
`ramis-sauloy2006`, `sauloy2004`, `vanderput2006`, `morita2012b`. All four carry
`library:` blocks (`stage: "sections"`) and notes that say which venue placements
are recalled rather than verified. No ref for #4 and #8 (tangential ⇒ none, per
the skill).

## Per-document notes — what each would actually be consumed by

**#2 Ramis–Sauloy (core).** `QAlienBridgeEquation.lean` builds a `QBridgeSystem`
(dilation `σ`, alien derivations `Δ_ω`, multiplicative weight, unipotent
correction) and says in its docstring that the adjoint action *is* "the Levi
decomposition of the local q-difference Galois group — a torus of characters `qⁿ`
extended by a unipotent part that the q-logarithm generates". Its `-- Ref:` header
cites only RSZ. The q-alien derivations are *defined* in this paper (Thm 3.5, as
residues in the summation direction `c ∈ E_q` of `log` of the Stokes operator of
Prop 2.5), proved Lie-like ⊗-endomorphisms (Thm 3.6), and tied to the level-δ
q-Borel transform of `QBorelKernel*.lean` (Thm 3.8 / 3.9). Corpus-grep before
calling this a gap: "wild fundamental group" has **zero** hits in `content/`,
`docs/`, `computations/`, `.beans/`; bean `qou-vkg5`'s open item 2 ("the q-native
form … additive or multiplicative … not settled") and the file's own "Not claimed"
paragraph name exactly what Thm 3.5 supplies the *object* for. Scope: it supplies
the object and the kernel's reading; it does **not** show `QBridgeSystem.bridge`
holds for `Δ̇_c` with any weight — no `aid-proof` proposed. The RSZ-route caveat
stands (§2.3 "one level" is a two-integral-slope setting; C1 at `∞` is pure
isoclinic — `2026-08-08-rsz-c1-infinity-route-closed.md`), so nothing here
supplies C1 Stokes data.

**#1 Sauloy 2004 (supporting).** Cited by #2 as its [28]. The corpus argues
"pure isoclinic ⇒ no local Stokes data" from RSZ Thm 3.3.5 (formalised as
`rszIsoformalDim_one`) and RSZ §4.4; Prop 4.1 here is the one-line algebraic
version (the Stokes sheaf is the bundle of `End^{>0}(M0) = ⊕_{μ_i>μ_j} Hom(P_j,P_i)`,
empty sum for one slope). Not core: every conclusion it supports is already
sourced.

**#3 van der Put 2006 (supporting) — and a mis-pointer.**
`QOU/Mass/BindingScalarKernelParityExclusion.lean:43-46` reads "…the van der
Put–Reversat structure theorem … `E(r,d,b)`, which is irreducible — held in this
corpus at `library/crmath-2011-349-19-20-1037-0/`". That directory is **Bugeaud
2011** (`bugeaud2011`, the CRAS note on non-integral slopes), not van der
Put–Reversat (`library/afst-2007-6-16-3-665-0/`, `vanderput-reversat2007`). No
bean tracked it (`grep -rl crmath-2011 .beans/` hits only `qou-37mj`, which is
the correct Bugeaud citation at `RSZIsoformalInterface.lean`). The same sentence
recurs without the pointer in `mass-theory/binding-genfun-qdifference.md` (~l.71)
and `mass-theory/qdifference-kernel-prolongation-symbol.md` (~l.76). Thm 3.4/3.5
of this survey is the English statement of the result; §5 is the
torus-extended-by-unipotent Galois-group shape `QAlienBridgeEquation.lean`
asserts. Bean `qou-86p5` covers both.

**#6 Morita 2012b (supporting).** The bilateral `₁ψ₀` is the divergent formal
solution of the degenerate first-order equation (19); Thm 1 resums it in
direction `λ` and the whole `λ`-dependence is a theta quotient (Cor 1: q-elliptic).
Bean `qou-wgnx` records that theta-normalising C1's `∞`-side solutions moved the
Stokes data into "the choice of theta" and that its route (a) is to resum in two
directions without normalising — this is the simplest worked instance, one order
below `morita2014`'s. Not a compute-check: the corpus evaluates no `₁ψ₀`; the
"θ-kernel bilateral Laplace" in `qbeta_g3_5two_qborel_theta_laplace.py` is a
different object (the Masbaum bar-side series).

**#4 Chatzidakis–Hardouin–Singer (tangential).** Definition-comparison of
difference Galois groups (PV ring / weak PV field / tannakian / model-theoretic).
The corpus names "the local q-difference Galois group" in two Lean docstrings
and never depends on which definition; "Chatzidakis" / "Hardouin" have zero hits.
Scope-(a): nothing consumed as read.

**#8 Dreyfus–Poulet (tangential).** Order-3 difference Galois groups, Case Q
included. The corpus has exactly two order-3 q-difference objects: the `4₁`
strong-AJ operator (`figure_eight_aj_operator.py`, cited to `nguyen-tran-2021`,
Galois group never asked for) and the W1 rank-3 base q-connection, which
`ColorCubicIrreducible.lean` + `2026-09-04-w1-route1-base-qshift-rationality-prune.md`
**prove does not exist** as a rational system. No block wants an order-3 Galois
group or a ∂-transcendence statement. Recorded for a future reader: §6.4 is the
algorithm and Thm 7.1 the criterion, should the `4₁` AJ operator's Galois group
ever be wanted.

**#5 RSZ (row current).** `source_sha` re-measured `d4295d4b18b2`; verdict `core`
stands; the rationale's "eight citation sites" is now 12 `-- Ref:` sites
(`QBorelKernelLevel`, `RSZIsoformalInterface`, `QBorelKernel`,
`OhtsukiKappaDependence`, `DominationTowers`, `QGevreyOrder`, `QAlienBridgeEquation`,
`RamifiedShiftCalculus`, `C1FormalSolutionGrowth`, `ThetaSlopeArithmetic`,
`DoorVParityNoIdentity`, `RamificationParityMonodromy`). Not edited — a count in
a rationale, not a wrong judgement.

**#7 Morita 2014 (row corrected).** The id was backfilled to `morita2014` on
2026-09-03 but the rationale still opened "WRONG JOIN — LOUD … no ref() entry
exists" and the `add-reference` action was still open although `qou-zdty` is
completed — so a reader saw an unregistered orphan while `references.ts` held the
entry. Rationale rewritten with the history kept, `add-reference` marked done,
`cite-in-block` (`qou-hnuw`, todo) untouched, `source_sha` re-measured unchanged.

## Method

- Identification from each document's own title page (section front-matter for
  the seven sectioned documents; `pypdf` text for #4, which has no sections).
- Citation status three ways per refid (`references.ts` entry / `.md` cite /
  Lean `-- Ref:`); corpus-grep over `content/`, `docs/audits/`,
  `docs/coordination/`, `computations/qbeta/`, `computations/probes/`, `.beans/`
  for the 19 terms the caller listed plus "van der Put", "Chatzidakis",
  "Hardouin", "Poulet", "bilateral". Discriminating counts: `wild fundamental
  group` 0/0/0/0/0/0; `Dreyfus` 0; `Chatzidakis` 0; `difference Galois` 3/1/0/0/0/0;
  `Stokes sheaf` 1/2/0/0/0/1; `Ramis` 18/21/2/8/7/8 (all RSZ or DRSZ);
  `Morita` 8/2/0/0/1/5 (the physics Morita and `morita2011`'s theta inversion).
- `source_sha` = `sha256sum <pdf> | cut -c1-12`, measured on the `library/` copy
  in the main checkout and on the byte-identical `uploads/` copy in this worktree.
- Ledger edited programmatically after verifying `json.dumps(indent=1,
  ensure_ascii=True)` reproduces the committed file byte-for-byte; the diff
  removes exactly four lines, all in the `morita2014` row.
- Validator: `bun run scripts/run-validate.ts content/quantum-observable-universe`
  against the **pinned** platform `428ca5c` (`.folio-assistant-pin`; symlink to
  the sibling clone `/home/user/folio-assistant`). Pre-edit **9 issue(s)**,
  post-edit **9 issue(s)** — unchanged; bibliography 865 → 869 entries, parses.

## What I could not settle

1. **Ingestion state is not in this branch.** The six new `library/` directories
   exist only in the main checkout, uncommitted there; this worktree holds the
   PDFs under `uploads/` (byte-identical, so the `source_sha` values are right)
   but not the `sections/`, `summary.json` or `INDEX.md` rows. The ledger rows
   point at `library/<doc-id>/<file>.pdf` as the skill prescribes; they resolve
   once the main session commits its ingestion.
2. **#4 is un-sectioned** *(resolved by the main session on the same PR: sectioned with
   `pdf-structure`, 8 sections, INDEX row added — it was one of the 22 bare-PDF orphans)*.
   At triage time `library/arxiv-0705.2975v1/` held only the PDF — no
   `structure.json`, no `sections/`, no `INDEX.md` row — so corpus-grep path 5
   is blind to it. Its verdict is from a `pypdf` read of the front matter and
   the theorem statements; nothing I found makes me expect a different verdict
   after ingestion, but that is an expectation, not a measurement.
3. **The ledger was not reseeded.** The skill's first step runs
   `source-ledger-index.ts --write`, which would add rows for *every*
   un-indexed library directory, not just these eight — out of scope for a
   cherry-pick. The six rows were hand-written in the indexer's shape and keyed
   by `source.file`, so a later reseed (idempotent, never overwrites `relevance`)
   should find them.
4. **Venues.** Sauloy 2004's Astérisque placement (vol. 296) and Ramis–Sauloy's
   published venue are recalled, not verified in-sandbox (arXiv egress only);
   the `note` fields say so. The R–S title is taken from the document's own
   header, which omits the "(I)" that the arXiv listing carries.
5. **Whether `QBridgeSystem` matches Ramis–Sauloy's `Δ̇_c`.** I verified that
   Thm 3.5 defines the object the Lean file is named after; I did *not* verify
   that the file's `bridge` relation (σ-conjugation = weight · Δ + unipotent)
   holds for those derivations, which is bean `qou-vkg5`'s open item. Hence
   `cite-in-block`, not `aid-proof`.
6. **Existing ledger rows carry titles in `note`** (e.g. the 2026-09-06 rows
   for `arxiv-2601.07906v2`, `arxiv-2605.20846v1`), contrary to the skill's
   "no title in the ledger" rule. Not touched here; flagged for whoever owns
   ledger hygiene.

## Commits on `claude/qdiff-stokes-triage-2026-09-07`

| sha | content |
|---|---|
| `15519eba39` | `references.ts`: four `ref()` entries |
| `e1ed3e1b26` | five beans under `qou-2akx` |
| `e418e8aaff` | ledger: six rows + `morita2014` correction |
| (this doc) | audit |
