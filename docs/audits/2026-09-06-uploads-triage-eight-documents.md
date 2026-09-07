# Relevance triage — the eight 2026-09-06 uploads

**Skill:** `local/paper-relevance-triage` (one document at a time).
**Ingest commit:** `e5afe5ea7b` (library: eight uploads). **Branch:** `claude/uploads-triage-2026-09-06`.
**Parent bean:** `qou-2akx`. **Ledger:** `content/bib-qa-verifications.json` (eight new rows, one per document).
**Refs created:** `hales-etal2010`, `bezdek-reid2013`, `martelli2016`, `li2026-two-sphere` (in `content/schema/references.ts`).
**Beans created:** `qou-ywbd` (packing citations), `qou-6cu7` (Martelli citations), `qou-2re6` (Li citation).

Verdicts are agent claims (`assessed_by.kind = "agent"`), not settled facts. Every "supplies nothing usable" below is
scope-(a): *this document, as read, supplies nothing usable here* — never a claim that the technique is excluded.

## Summary

| doc-id | what it is | verdict | ref | bean |
|---|---|---|---|---|
| `arxiv-0902.0350v1` | Hales, Harrison, McLaughlin, Nipkow, Obua, Zumkeller — *A revision of the proof of the Kepler conjecture* (DCG 2010; 41 pp) | **supporting** | `hales-etal2010` | `qou-ywbd` |
| `arxiv-1210.5756v1` | Bezdek, Reid — *Contact graphs of unit sphere packings revisited* (J. Geom. 2013; 19 pp) | **supporting** (the strongest of the eight) | `bezdek-reid2013` | `qou-ywbd` |
| `arxiv-1610.02592v3` | Martelli — *An Introduction to Geometric Topology* (arXiv textbook, v3 2022; 494 pp) | **supporting** | `martelli2016` | `qou-6cu7` |
| `arxiv-2305.07425v1` | Abbott, Nguyen, Rasmussen — *Largest hyperbolic actions of 3-manifold groups* (2023; 20 pp) | tangential | — | — |
| `arxiv-2501.00914v2` | Baldwin, Sivek — *L-spaces and knot traces* (2026; 37 pp) | tangential | — | — |
| `arxiv-2601.07906v2` | Belin, Collier, Eberhardt, Liska, Post — *A universal sum over topologies in 3d gravity* (2026; 117 pp) | tangential | — | — |
| `arxiv-2605.20846v1` | Chris Li — *Topological Field Theories and the Algebraic Structures of the Two-Sphere* (2026; 99 pp) | **supporting** | `li2026-two-sphere` | `qou-2re6` |
| `qt2pf5d0mn` | Xingshan Cui — *Higher Categories and Topological Quantum Field Theories* (UCSB PhD thesis, 2016; 106 pp) | tangential | — | — |

Two things the triage changed about the corpus's own record:

1. **The packing shelf is no longer empty.** `docs/audits/2026-09-05-max-contact-sub-affine-negative.md` §5 recorded, correctly at the
   time, that "`references.ts` has no packing entry" and that the Harborth / Bezdek / contact-number forms were "deliberately not
   cited". Two of those sources are now held and registered. **This does not resolve that audit's four objections** to importing
   Euclidean packing geometry (internal derivation demanded by `qou-rav3`; hyperbolic ambient geometry; three-dimensionality
   underived; exponent imported) — it makes the import citable, not derived. `qou-brng` is unchanged.
2. **Martelli is no longer "absent".** `docs/audits/2026-09-06-hyperbolic-surface-law.md` line 144 and bean `qou-j8hp` list it as
   "absent — optional". It is held and registered; the citation actions are queued in `qou-6cu7`. Per the owner's instruction the
   two-bridge layering (`qou-yvyd`) was **not** attempted here.

## Method, briefly

Per document: identify from the document's own front matter (not the filename); check citation status three ways
(`references.ts` entry / `cites[]` or `\cite` site / Lean `-- Ref:`); corpus-grep the topic across `content/`, `docs/audits/`,
`computations/`, `.beans/` and the library; read the abstract, introduction and the statements actually claimed to be usable;
record the verdict, key results with in-source locators, and actions; create the `ref()` **first** when a citation is warranted
(metadata lives only in `references.ts` — the ledger carries no title / author / year); queue non-`no-action` items as beans under
`qou-2akx`, checking each title for an exact match first.

Two mechanical findings while doing that, recorded so the next triage does not repeat them:

- `folio-assistant/content/pipeline/source-ledger-index.ts` seeds rows **only for `uploads/`**, not `library/` (it reads
  `UPLOADS_DIR`, lines 49 / 200–220). Running it `--write` on this tree rewrote all 17,468 lines of the ledger (a whitespace /
  key-order re-serialisation) and added **no** rows for these eight library documents. The rewrite was reverted and the eight
  rows were appended by hand in the file's own `json.dumps(indent=1)` form, which round-trips the committed file byte-for-byte
  (verified before appending).
- Crossref is unreachable from this sandbox (`CONNECT tunnel failed, response 403`), so the journal volume / pages for
  `hales-etal2010` and `bezdek-reid2013` are recalled and flagged as such in their `note` fields, and DOIs are omitted — the same
  convention the existing `frenkel-reshetikhin1998` / `koroteev-zeitlin` entries use.

## Per-document evidence

### 1. `arxiv-0902.0350v1` — Hales et al., Kepler revision — **supporting**

**Identified from:** Introduction (pp. 1–3): "In 2006, *Discrete and Computational Geometry* devoted an issue to the proof of the
Kepler conjecture … This article summarizes the current status of a long-term initiative to reorganize the original proof …
The second part gives errata in the original proof." Sections read: `sec-000` (Introduction), `sec-002` (§2 Blueprint edition),
`sec-006` (§6 Tame graph enumeration: "Theorem 1. Any tame plane graph is isomorphic to a graph in the Archive … at most 2771
tame graphs"), section list for Part 2 (§8 biconnected graphs, §9 errata).

**Corpus status before:** no `ref()`; `references.ts` had no Kepler / packing entry (its only `kissing` match is the surname
Kissinger); `docs/audits` mention fcc / close-packing in the coordination arc (`2026-09-05-coordination-surface-deficit.md`
line 72 "facet (fcc, `k = 12`)"; `2026-07-11-bk-coordination-degree-and-alpha-contact.md` line 71) with no source.

**Usable result (one):** the Kepler theorem *statement* — no packing of congruent balls in $E^3$ exceeds the fcc density
(Introduction p. 2). Targets `rem:bk-coordination-multiplicity` (lines 83–86, "saturates to a geometric close-packing count")
and `prop:coordination-saturation` (Lean docstring: "the close-packing / fcc picture").

**What it does not supply:** any kissing-number or contact-number bound — this paper proves neither; the $k = 12$ bounded degree is
sourced by Bezdek–Reid below (and, underneath, Schütte–van der Waerden 1953). Part 1's HOL Light / Isabelle formalisation is a
methodological precedent for this repo's blueprint-then-formalise discipline, not a mathematical input.

**Actions:** `add-reference` (done: `hales-etal2010`); `cite-in-block` → `qou-ywbd` (combined with Bezdek–Reid, same sentence).

### 2. `arxiv-1210.5756v1` — Bezdek–Reid, contact graphs — **supporting** (bordering core)

**Identified from:** title page and §1 (pp. 1–3). Sections read: `sec-000` (Introduction: Theorems 1–3, Problems 1–2),
`sec-001` (§2 proof of Theorem 1(i): Theorem 4, Theorem 5 "Hales [6]", Lemma 1, Corollary 2, the isoperimetric step and the final
line "$< 6n − 0.926675 n^{2/3} < 6n − 0.926 n^{2/3}$"), `sec-012` (bibliography: [6] Hales, *Dense Sphere Packings — a blueprint
for formal proofs*; [2] Bezdek, *Contact numbers for congruent sphere packings in Euclidean 3-space*; [14] Schütte–van der
Waerden).

**Quoted statements.** Theorem 1: "(i) The number of touching pairs in an arbitrary packing of $n \ge 2$ unit balls in $E^3$ is
always less than $6n − 0.926 n^{2/3}$. (ii) … lattice packing … less than $6n − 3.665\ldots n^{2/3}$." And "for all
$n = (2k^3+k)/3$, $k \ge 2$, there are packings … such that the number of touching pairs is greater than $6n − 7.862\ldots n^{2/3}$."
Theorem 2: touching triplets $\le 25n/3$, quadruples $\le 11n/4$ (lattice: $8n$, $2n$). Theorem 5 (Hales): a 14th ball has centre
distance $\ge 2.52$ from a ball with 12 touching neighbours — the kissing-number-12 rigidity input.

**Why it is the lead that checks out.** `QOU.Mass.CoordinationSaturation` (bean `qou-brng`) proves the dichotomy complete-graph
(unbounded $B/A$) vs bounded-degree $k$ (constant $B/A = \epsilon k/2$), and `2026-09-05-coordination-surface-deficit.md` writes the
bond count as $M = kA/2 − (k − k')A_{\text{surf}}/2$ with $A_{\text{surf}} \propto A^{2/3}$. Theorem 1(i) is exactly that shape
with $k = 12$ and a proved coefficient, and 1(ii) / the fcc lower bound bracket the $n^{2/3}$ coefficient in $[0.926, 7.862]$.
Theorem 2 bounds the 3- and 4-body contact counts a geometric realisation would carry
(`QOU.MassTheory.BodyOrderRecurrenceDepth` says depth $\ge 3$ is forced).

**Why not core.** The corpus already declined to cite exactly these forms on principle (`2026-09-05-max-contact-sub-affine-negative.md`
§5); Bezdek–Reid is Euclidean and settles none of the four objections. A held bound on what a packing model *could* give is a
constraint, not a derivation. Recommended (judgement): cite it where the close-packing count is invoked, and do not read the
citation as progress on `qou-brng`.

**Actions:** `add-reference` (done: `bezdek-reid2013`); `cite-in-block` → `qou-ywbd`. A possible follow-up, not queued: a
`compute-check` of the corpus's fcc-facet surface-deficit coefficients against the $[0.926, 7.862]$ bracket.

### 3. `arxiv-1610.02592v3` — Martelli, geometric topology textbook — **supporting** (citation only)

**Identified from:** title page (`sec-000`: "The aim of this book is to introduce the reader to … geometric topology … an
introduction to surfaces and three-manifolds, and to their geometrisation"), arXiv stamp v3, 5 Apr 2022, 494 pp.
Sections read: `sec-057` (§13.1: Thm 13.1.3 "$\mathrm{Vol}(\Delta) = \Lambda(\alpha) + \Lambda(\beta) + \Lambda(\gamma)$",
Cor 13.1.4 regular ideal tetrahedron maximal), `sec-060` (§14.1: 14.1.1 ideal tetrahedra as one shape $z$, 14.1.2 ideal
triangulations, 14.1.3–14.1.5 consistency + completeness equations, Prop 14.1.7, Prop 14.1.8 "all edges have valence six … the
point $(e^{\pi i/3}, \ldots)$ is a solution", Fig 14.7 + §14.1.7 "SnapPea constructs precisely the ideal triangulation of Figure
14.7 … the complement of the figure-eight knot … decomposes into two ideal regular tetrahedra", Thm 14.1.10 torus / satellite /
hyperbolic), `sec-062` (§15.1: Thm 15.1.1 hyperbolic Dehn filling, Table 15.1 the non-hyperbolic surgeries of $4_1$),
`sec-063` (§15.2: Prop 15.2.1 "$T$ has the same number $n$ of tetrahedra and edges", Cor 15.2.8 "$\mathrm{rk} A = 2n − c$",
Prop 15.2.9 "The rows of $A$ generate a lagrangian subspace", Prop 15.2.11), `sec-046`/`sec-047` (§11.3 Dehn surgery,
§11.4 torus bundles, Prop 11.4.14, "When $|\mathrm{tr} A| > 2$ we say that the monodromy $A$ is Anosov").

**How it lands on `qou-n2cl` / `qou-yvyd`.** `docs/audits/2026-09-06-nz-gluing-data-from-braid-monodromy.md` §2 checks the derived
NZ rows against "exact solution $z_0 = z_1 = \omega$" (= Prop 14.1.8 + Fig 14.7), "NZ symplectic: edges isotropic,
$\omega(\mu,\lambda) = \pm 2$" (= Prop 15.2.9), and reaches the Thurston edge equation (= §14.1.3). Its Lean
`QOU/Mass/FigureEightGluingFromMonodromy.lean` cites only `[manuscript]` and library `arxiv-0808.2716v4`; `prop:hyperbolic-knot-shape-fields`
and `prop:gluing-equations-do-not-detect-hyperbolicity` cite only `thurston1978` + `neumann-zagier1985`. Martelli gives numbered,
held statements for each.

**Not in this book (grep-checked):** the Floyd–Hatcher punctured-torus-bundle layering and Guéritaud's two-bridge layered
triangulations — zero hits for "punctured torus", "Farey", "two-bridge", "layered" outside one figure caption. Keep citing
`arxiv-0808.2716v4` (Futer–Kalfagianni–Purcell) for those. §11.4 treats only closed torus bundles.

**Actions:** `add-reference` (done: `martelli2016`); `cite-in-block` → `qou-6cu7` (three targets: the two content blocks, the
Lean docstring `-- Ref:`, and an appended note in the NZ audit §2). The main session is using Martelli in the foreground; nothing
in the two-bridge work was touched.

### 4. `arxiv-2305.07425v1` — Abbott–Nguyen–Rasmussen — tangential

**Identified from:** title page and §1 (`sec-000`; "Date: May 15, 2023"). Read: abstract, Theorem 1.1 (a non-geometric
3-manifold with a hyperbolic JSJ piece meeting $\partial M$, two hyperbolic pieces glued along a torus, an isolated non-elementary
Seifert piece, or a non-elementary maximal graph-manifold component has H-inaccessible $\pi_1$), Corollary 1.2(a) (connected sums of
cusped hyperbolic 3-manifolds), Theorems 1.3–1.4, Corollary 1.5; section list (§2.1 H-accessibility, §2.3 Croke–Kleiner admissible
groups).

**Corpus-grep:** zero hits in `content/`, `docs/audits/`, `.beans/` for "hyperbolic action", "H-accessib", "acylindrical",
"hierarchically hyperbolic", "Croke-Kleiner". The folio's objects are single hyperbolic knot complements (geometric, so outside
Theorem 1.1's hypothesis); nothing in the Hecke / Markov-trace / NZ pipeline consumes a group action of $\pi_1$ on a hyperbolic
space. Same broad field, no consumable result. No reference created; `no-action`.

### 5. `arxiv-2501.00914v2` — Baldwin–Sivek — tangential

**Identified from:** title page (`sec-000`, arXiv stamp 13 Mar 2026). Read: abstract, §1 Theorems 1.2 ("If $K$ is an L-space knot
then $X_0(K)$ detects $K$"), 1.3, 1.4 ("If $J$ and $K$ are L-space knots such that $S^3_0(J) \cong S^3_0(K)$, then $J = K$",
via Lee–Taubes / Kutluhan–Lee–Taubes), §1.1 Theorems 1.5–1.6 (torus knots, nonzero traces); section list (§2 zero-surgeries on
FFPF knots, §3 traces and large surgeries, §6 Alexander polynomials of L-space knots).

**Corpus-grep:** zero hits for "L-space", "knot trace", "characterizing slope", "Heegaard Floer", "HFK". The folio has no Floer
theory and no 4-manifold layer. **Homonym recorded:** the 4-manifold "knot trace" $X_n(K)$ is unrelated to the folio's Markov
trace $\mathrm{tr}_M$ and trace field, so a corpus-grep on "trace" lands falsely. The FFPF fixed-point-free monodromy criterion
(§2) is a Floer input, not a gluing datum, and does not touch the figure-eight monodromy the NZ chain computes. No reference
created; `no-action`.

### 6. `arxiv-2601.07906v2` — Belin–Collier–Eberhardt–Liska–Post — tangential (lead checked and rejected)

**Identified from:** title page (`sec-000`, header "March 2026", hep-th). Read: Introduction (eq. 1.1
$Z[\Sigma] = \sum_{\partial M = \Sigma} Z_{\text{grav}}[M]$; eq. 1.2 the handlebody sum over $\mathrm{MCG}(\Sigma_g)/H_g$;
Maloney–Witten genus 1), `sec-013` (§4.3 "the gravitational machine is hyperbolic": the surgery moves preserve hyperbolicity by
Thurston's criterion — prime, homotopically atoroidal), `sec-014` heading (§4.4 not all hyperbolic manifolds are generated; the
Discussion says "at least all acylindrical hyperbolic 3-manifolds" are excluded), `sec-017` (§5.3 handlebody knots, the $4_1$ and
$5_2$ handlebody-knots), `sec-018` (Discussion).

**Why the Stokes lead does not hold.** The object is a sum over *distinct compact hyperbolic 3-manifolds with genus-$g$
conformal boundary*, each weighted by an exact Virasoro-TQFT partition function, organised so the boundary CFT$_2$ data form a
consistent statistical ensemble. The folio's Stokes constant (`conj:stokes-dt-bps-bridge`, `ecalle-borel-resurgence-vocabulary`) is a
Borel-plane coefficient of the state integral of *one cusped knot complement*, conjecturally a DT/BPS integer of $T[K]$. A sum over
topologies is not a trans-series over the Borel-plane saddles of a single manifold. Grep of all 31 sections: zero hits for
"Stokes", "resurgen", "Borel", "state integral", "knot complement", "cusped"; "Teichmüller" appears only as boundary moduli and in
the bibliography. Shared background only (Thurston hyperbolisation, already `thurston1978`; handlebody-knot tables). No reference
created; `no-action`. Not excluded: a Virasoro-TQFT-on-knot-complements bridge — it is simply not in this paper.

### 7. `arxiv-2605.20846v1` — Chris Li, TFTs and $S^2$ — **supporting**

**Identified from:** title page (`sec-000`, arXiv stamp 20 May 2026, math.AT; the text calls itself a thesis, no institution on
the extracted pages). Read: Introduction (Def 1.0.1–1.0.2; Thm 1.0.3 $\mathrm{Cob}(2)$ free symmetric monoidal on a commutative
Frobenius object; Thm 1.0.5 "$\mathrm{Cob}(3)_{S^2}$ has a presentation with $G_2$ generators under commutative Frobenius relations
and legs relations"; Thm 1.0.6 the $G_1$ presentation; Thm 1.0.7 Kneser–Milnor; **Thm 1.0.8 "There is a canonical isomorphism
$S : \mathrm{Cob}(2) \xrightarrow{\sim} \mathrm{Cob}(3)_{S^2,\mathrm{CF}}$"** — "the commutative Frobenius part of
$\mathrm{Cob}(S^2)$ is completely determined by $\mathrm{Cob}(2)$"), `sec-013` (§5.1: Def 5.1.1 sketch of P/L-monoids, Lemma 5.1.2
bijection, Prop 5.1.5, Def 5.1.7), `sec-016` (§A.2).

**Where it lands.** `rem:tqft-context` (`quantum-observable-universes/tqft-context.md`) opens: "The Frobenius–Hopf object $A$
carries the 2d cobordism data and the Hopf structure for quantum-group symmetry", citing the general TQFT frame
(`atiyah1988`, `kock2004`, `lurie2009`, `turaev2010`, `freed2010`, `baez1995`, `witten1988`). Thm 1.0.8 is the specific theorem: for
every 3d TFT, $Z(S^2)$ is a commutative Frobenius monoid whose Frobenius data is exactly $\mathrm{Cob}(2)$; Thms 1.0.5–1.0.6 say what
else the $S^2$-sector carries (one unit $\emptyset \to S^2$ per closed oriented irreducible prime 3-manifold, "legs" relations),
which the QOU axioms do not use. Corpus-grep: "Cob(" / "bordism" occur in `content/` only in this block.

**Caveat that keeps it supporting, not core.** Li's monoids are *commutative* Frobenius monoids in a *symmetric* monoidal target;
QOU's $A$ is a Hopf algebra in a *braided* category and is not assumed commutative. The match is at the Frobenius-structure level
only; it does not identify $A$ with $Z(S^2)$ of any TFT and says nothing about the Hopf half. The bean says to state the caveat in
the citing sentence.

**Actions:** `add-reference` (done: `li2026-two-sphere`); `cite-in-block` → `qou-2re6`.

### 8. `qt2pf5d0mn` — Cui, UCSB thesis — tangential

**Identified from:** abstract page (`sec-000`: "Higher Categories and Topological Quantum Field Theories by Xingshan Cui — We give
a construction of Turaev–Viro type (3+1)-TQFT out of a $G$-crossed braided spherical fusion category for $G$ a finite group");
PDF `CreationDate` 2016-06-09. **Note:** `structure.json` records the title as "UC Santa Barbara" — that is the eScholarship banner,
not the document title. Read: abstract, Introduction (`sec-001`, survey of RT / TV / Kuperberg / Hennings / Crane–Yetter), section
list, `sec-016` (§5 open questions: $H^4(G, U(1))$ obstruction; $G$-BSFC $\leftrightarrow$ ribbon fusion categories containing
$\mathrm{Rep}(G)$ by equivariantisation; a (3+1) Kuperberg invariant; Walker–Wang).

**Corpus-grep:** no 4-manifold invariant, Crane–Yetter, $G$-crossed or $G$-graded fusion category anywhere in `content/` or
`docs/audits/`; the single "equivariantiz" hit is `docs/audits/2026-08-25-gerbe-tannakian-intake-triage.md`, which already holds a
primary equivariantisation source (Galindo–Gallego–Morales, `arxiv-2607.10525v1`). The folio's ribbon-category use is (2+1) and
already sourced (`turaev2010`, `bakalovkirillov2001`, `etingof-ostrik2004/2018`); §2.1 adds nothing to those. No reference created;
`no-action`. If a citation is ever wanted, the published version (Cui, *Four dimensional TQFTs from $G$-crossed braided categories*,
Algebr. Geom. Topol. 2019 — recalled, not verified here) is the one to cite, not the thesis.

## Validation

`bun run scripts/run-validate.ts content/quantum-observable-universe` after the four `ref()` additions, against platform
`folio-assistant` `428ca5c` (the pin): `✓ Valid — 9 issue(s)`, "bibliography: 865 entries, parses". The nine are the same nine the
tree reported before this branch (`validate-before.log`: `✓ Valid — 9 issue(s)`): six known pin-`428ca5c` "Unknown field
`authorNotes` / `computation`" drops (AGENTS.md §4d), `lem:piece-a-corner-removal-obligation` no Lean, and the
`def:local-substrate-q` dangling cross-reference. Nothing new. Each new entry was also loaded through `getRef()` under `bun`
before its commit.

## What was deliberately not done

- No content-block, Lean or `computations/` edit — the four citations are queued as beans, not applied.
- No two-bridge / Martelli-foreground work (`qou-yvyd` belongs to the main session).
- No DOIs recorded: Crossref is unreachable from this sandbox; journal locators are marked "recalled" in the `note` fields.
- The ledger indexer was run and its whole-file rewrite reverted (see *Method*); it cannot seed `library/` rows.
- The `assessed_by.model` field, which the schema requires as a bare string, carries a session identifier
  (`coding-agent-session-…`) rather than a model name, per the session instruction not to write model identifiers into files;
  the other 350 triaged rows use a model string, so normalise these eight if the convention is preferred.
