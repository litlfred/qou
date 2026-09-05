# Citation-gap inventory for the hyperbolic-volume / eightfold arc

**Date:** 2026-09-04 · **Branch:** `claude/lean-prove-assertions-2026-09-04` (PR #6584)
**Epic:** `qou-8lxd` · **Agent:** `corpus-grepper` — **read-only.** No content block,
`.ts`, `.lean`, witness or `references.ts` entry was edited by this pass; nothing was
committed or pushed.

memory: MEMORY.md (247 lines, `a79d974beb`) + library-and-staleness-traps.md, resolved-topics.md

**Scope.** The *citation* half of the gap inventory the owner asked for
(*"bean up all gaps and needed lean proofs … start with citations but then do the
infrastructure"*). The Mathlib-infrastructure half is a sibling agent's and is not
touched here.

---

## 0. Method, and the path that is uncovered

**Path 0 — `corpus_search` (MCP): UNAVAILABLE, fourth consecutive session.**
`paper-assistant` fails with `ENOENT: no such file or directory, posix_spawn
'/home/litlfred/folio-assistant/scripts/start-folio-assistant.sh'`; `lean-lsp`,
`openalex-paper-search` and `paper-search-mcp` also failed to connect
(`CONNECT_TIMEOUT`). These are connection failures, not missing capabilities.

**Consequence, stated so it is not read past.** Paths 1–6 are greps and share one
blind spot: they find prior work only if it used *my* words. Path 0 is the step that
survives a change of vocabulary. **Every absence below is therefore lexical**, and
the mitigation was to run many spellings rather than to claim coverage. Spellings
varied here, with measured splits where they mattered:

| spelling pair | library section dirs |
|---|---|
| `hyperbolization` / `hyperbolisation` | **8** / **1** |
| `Riemann-Hurwitz` / `Riemann–Hurwitz` | **7** / **3** |
| `Gauss-Bonnet` / `Gauss–Bonnet` | **12** / **4** |
| `Frobenius-Schur` / `Frobenius–Schur` | **5** / **2** |
| `uniformization` / `uniformisation` | **10** / **1** |
| `Sasakian` / bare `Sasaki` | **0** / 5 (all surnames in bibliographies) |

**Neither member of any pair is a superset of the other.** A `library/` count is
evidence about the string you typed, never about the subject.

**External egress is 403.** `curl` to `api.crossref.org` and `export.arxiv.org`
both return `CONNECT tunnel failed, response 403`; the proxy status endpoint
confirms `connect_rejected — policy denial`. So **no bibliographic metadata was
verified against a publisher record this session**, and the two entries that were
already marked unverified remain so.

**Counts exclude vendored Mathlib.** `content/quantum-observable-universe/lean/.lake/`
inflates naive `content/` counts by ~65 %.

**Baselines re-measured 2026-09-04:** 576 `library/` directories, 552 `INDEX.md`
rows (gap 24 against 23 dirs carrying `duplicate_of` — the index is current, not in
the stale state recorded on 2026-09-03); 828 `references.ts` entries, of which
**394 carry a `library.docId`**; 22 PDFs still queued in `uploads/`.

---

## 1. The inventory

Classes, as the task defines them: **(H)** held and cited correctly ·
**(M)** held but mis-cited or under-cited · **(U)** not held, must be uploaded ·
**(C)** cited-not-proved in Lean.

| # | class | work / claim | what it would source | where it bites | bean |
|---|---|---|---|---|---|
| 1 | **M** | Thurston, *GT3M* (1978) — held as a **33-page Ch. 1–2 excerpt** (22 sections, 54.8 kB) | hyperbolisation; the gluing equations; the figure-eight structure | **113 citers**; `shared-denominator-cusp-holonomy.lean:91` (*"§4.5 (gluing equations)"*), `ManifoldVolumeBridge.lean:112` (*"Ch. 4"*), `ManifoldVolumePositive.lean:30`, `kashaev-volume-conjecture.lean:142`, `figure-8-archimedean-illustration.md:5,97` | `qou-2hc7` |
| 2 | **M** | Riera–Rodríguez 1992 **§2** — held (`pjm-v154-n1-p09-s`), registered, cited for its **period matrix only** | `B = Δ/Γ` genus 4 (**B3**); `[Γ*:Γ]=120` × 2 ⇒ **240** (**B2**); the (2,4,5) triangle group | `EmCouplingBringZeroMode.lean:90,94,195-199`; `em-coupling-bring-zero-mode.md:20` (`.ts` cites the dilogarithm leg only) | `qou-ezne` |
| 3 | **U** | **Murakami & Murakami 2001**, Acta Math. 186, 85–104 | the volume conjecture's founding statement (L5) | **63 citers**, `library.docId` = none, 0 `INDEX.md` rows, absent from `uploads/` | `qou-g71v` |
| 4 | **M** | `library/0803219` = Murakami, *An introduction to the volume conjecture* — **held, unregistered** | the survey-level per-knot KVC locators | `qou-ic22` (*"cite Murakami 3.3 per-knot"*) has **no key to write** | `qou-mzv5` |
| 5 | **U** | CR / contact / Sasakian geometry — **nothing held AND nothing registered** | Darboux, `dim M = 2n+1`, `rank_ℝ H = 2n`; Webster metric; Levi form | `ContactDistributionRank.lean:91`; 34 `content/` files; **10 blocks with no `cites` field at all** | `qou-iryu` |
| 6 | **M** | `[hatcher2002]` — **key does not exist in `references.ts`** | the Gysin sequence of an oriented sphere bundle | `CircleBundleBettiObstruction.lean:63`, where the Gysin count **is the model**, *"cited not derived"* | `qou-josl` |
| 7 | **U + C** | Woronowicz's differential-calculus papers — 4 keys registered, **none held**; the 4D bicovariant classification carries **no `-- Ref:` at all** | `Ω¹(𝒪_q(SU(2)))` free of rank 3; the 4-dimensional bicovariant calculi | `CalculusDimensionObstruction.lean:89-94`, `SelfDualityDegree.lean:89-90` — the premise of the calculus-dimension obstruction | `qou-hfwb` |
| 8 | **M** | Mostow 1968 — registered, `verified-clean`, **not held**; `local_pdf` path in the bib ledger **does not exist** | rigidity ⇒ the topology, and hence the mass, is discrete | `approach-to-exceptional-divisor.md:11` (`.ts`: **no `cites`**); `swampland-island-of-consistency.md:11` (`.ts` cites the swampland papers only); `HyperbolicVolumeFormType.lean:81,152` | `qou-w5oq` |
| 9 | **M** | `[ohtsuki2016-52]` — **key does not exist**; the held `ohtsuki2016` (`104171-qt-83`) is the same DOI | the 5₂ asymptotic expansion | `Archimedean/FiveTwoOhtsukiBridge.lean:161` | `qou-uzzk` |
| 10 | **U** | **Bryant 1987** (Ann. Math. 126) / **Hitchin 2000** (JDG 55) | `G₂` = stabiliser of a generic 3-form on `ℝ⁷`, open orbit | `G2FrameDimensions.lean:46,75,180`; `form_stabilizer_genericity_su3_routes.py:21`. The file's only Ref is `[baez2002]`, which gives `Der(𝕆) ≅ 𝔤₂` and **not** this | `qou-2u6r` |
| 11 | **U** | **Butruille 2005**; Gray 1970; Fernández–Gray 1982 | `S⁶ = G₂/SU(3)` as *the* homogeneous nearly-Kähler 6-sphere | the `S⁶` leg, `qou-uq5x` / `2026-09-04-the-g2-frame.md` | `qou-ctzi` |
| 12 | **M** | Riemann–Hurwitz — **no key anywhere in `references.ts`**; 10 held dirs state it | `R_tot = 14`; the degree/ramification arithmetic | `brings-is-qou-verification.md:15` (`.ts`: **no `cites`**); `CoveringDegreeRamification.lean:73,88-91` (*"a definition encoding … not a proof"*) | `qou-b5ly` |
| 13 | **M** | Gauss–Bonnet for `ℍ²` (**B1**: area = angle defect) — **no key**; 16 held dirs state it | the π/20 triangle area under curvature −1 | `EmCouplingBringZeroMode.lean:88-89`; `em-coupling-bring-zero-mode.md:20` (kind `proposition`) | `qou-aucv` |
| 14 | **C** | **Eight arc Lean files carry zero `-- Ref:` lines** while deferring premises in prose | (per file — see the bean's table) | `ContactDistributionRank`, `HyperbolicVolumeFormType`, `HookContentMarkovParam`, `OcneanuRankFamily`, `SelfDualityDegree`, `VolumeFormDegree`, `CalculusDimensionObstruction`, `CoveringDegreeRamification` | `qou-3o59` |
| 15 | **M** | `bichon2003`, `etingof-ostrik2004` — added 2026-09-03 **UNVERIFIED**, still unverified | the fibre-functor classification for `Rep(SL_q(2))` | `FibreFunctorDimensionNotCategorical.lean`; `fibre_functor_dimension_not_categorical_probe.py`. Neither has a `bib-qa-verifications.json` row | `qou-zx95` |

### (H) — checked and clean, no bean

- **Kashaev 1997** (`arxiv-q-alg-9601025v2`) — held, 73 citers. **Kashaev 1995**
  (`arxiv-q-alg-9504020v1`) — held, 4 citers.
- **Ohtsuki 2016** (`104171-qt-83`) and **Andersen–Hansen 2006**
  (`arxiv-math-0506456v1`) — both held and cited (3 and 5 citers). Task item 3 is
  otherwise answered: the volume-conjecture literature is **extensively** registered
  (Garoufalidis ×20, Murakami ×10, Dimofte ×7, Ohtsuki ×4, …). The one hole is
  MM2001 itself (row 3).
- **Neumann–Zagier 1985** — held **three times** (`1-s20-0040938385900047-main` plus
  two copies carrying `duplicate_of`), registered **with `alternates`**, and cited in
  **63** files. Task item 4 answered: cited, correctly, and the duplication is
  recorded in three places (front-matter `duplicate_of`, `references.ts` `alternates`,
  and the copies get no `INDEX.md` row).
- **Frobenius–Schur / `[fulton-harris1991]`** — task item 8. The book is registered
  with ISBN + DOI, `verified-clean` in the bib ledger, and **not held** — which is
  fine; `references.ts` registers textbooks without PDFs by design. More to the point,
  **the FS type enters Lean as a hypothesis, not an assertion**:
  `Eightfold/Sym2GateFSTrichotomy.lean:103` declares `inductive FSType` and every
  consumer takes `fs : ℕ → FSType` as a **parameter** (`sym2Singlets`, `Passes`,
  `QuaternionicEvenDim`). The trichotomy is cited at four `-- Ref: [fulton-harris1991]`
  sites with §-level locators. Clean.
- **Woronowicz's 3-dimensional left-covariant calculus** — the *source* half of task
  item 5 is clean: `woronowicz1987-twisted-su2` (Publ. RIMS 23) is registered **and
  cited**, at `brings-is-qou-proof.md:11,15` and `connection-su2.ts`. Only the
  *classification* half (row 7) and one sibling block (row 12) are defective.

### Corrections to prior artifacts, owed by this pass

1. **My own 2026-09-04 audit said the Riera–Rodríguez duplicate pair is "absent from
   `library-duplicate-ledger.json`, so the ledger under-counts here."** That is true of
   the file and **misleading as framing**. The ledger is a list of **4 hand-adjudicated
   detector misses**; machine-detected duplicates live in section front-matter (23 dirs
   carry `duplicate_of`) and in `references.ts` `alternates`. The Riera pair is recorded
   in **both**, and the copy correctly gets no `INDEX.md` row. Nothing under-counts.
2. **Two existing beans cite the wrong copy.** `qou-3q4q` and `qou-fkmt` both name
   `library/the-period-matrix-of-bring-s-curve-1hik02mwva/` — the copy carrying
   `duplicate_of: "pjm-v154-n1-p09-s"` — as their source. Retarget to the preferred stem.
   Noted in `qou-ezne` rather than beaned separately.
3. **The arc's Lean is sorry-free.** A naive `grep -c '\bsorry\b'` reports 1–4 in five
   of these files; every match is the string *"sorry-free"* in prose or a commented-out
   instance. I made that error before checking it, and it matters: had it been real, row
   14 would be an AGENTS.md §1 violation rather than a gap that **falls through** §1.

---

## 2. Which uploads would unblock the most — ranked

Ranked by *citers × load-bearingness*, not by how interesting the paper is.

**1. Murakami & Murakami 2001, *The colored Jones polynomials and the simplicial
volume of a knot*** (`math/9905075` / Acta Math. 186). **63 citers, zero holding.**
The most-cited un-held work on the arc and the statement L5 rests on. Its counterpart
`[kashaev1997]` is held and cited 73×, so the pair is half-present. On arXiv ⇒ cheap.

**2. The full Thurston GT3M notes** — replacing the 33-page Ch. 1–2 excerpt.
**113 citers**, several with explicit Ch. 4 / §4.5 locators the held copy cannot
support. Freely distributed by MSRI ⇒ cheap. *Partial substitute already on disk:*
`library/angled-survey` (Futer–Guéritaud) carries `gluing equation` ×10,
`ideal tetrahed` ×9, `Rivin` ×31 — **but it is not registered**, so registering it is
a second, near-free win.

**3. One contact/CR textbook — Blair, *Riemannian Geometry of Contact and Symplectic
Manifolds*.** This unblocks the *live modelling decision*
(`2026-09-04-the-cr-dimension-decision-full-context.md`, blast radius 23 blocks /
90 consumers of `def:substrate-parameter`), and it is the cheapest of the three CR
candidates because the deferred fact is elementary (Darboux, `dim = 2n+1`). A book, so
"upload" may mean *register with ISBN and no PDF* — which is what `fulton-harris1991`
and `ratcliffe` already do, and is sufficient.

**4. Woronowicz, *Twisted SU(2) group*** (Publ. RIMS 23, 117–181). The framework
*declares* the 3-dimensional left-covariant calculus in its defining blocks and holds
nothing behind it — `library/` has **zero** files containing the phrase *"differential
calculus"*. Ingesting this also puts the 4D-bicovariant question on a checkable footing,
though **the attribution for the classification must be settled first** (it may be
Schmüdgen–Schüler 1995, not Woronowicz — flagged, not asserted; egress was 403).

**5. Dragomir & Tomassini, *Differential Geometry and Analysis on CR Manifolds***.
The pseudohermitian / Webster / Levi-form package the corpus uses by name across 34
files. Below Blair only because Blair alone closes the one Lean deferral.

**6. Hitchin, *The geometry of three-forms in six and seven dimensions*** (`math/0010054`)
— on arXiv, closes `G2FrameDimensions.lean:75`, and is the source whose language
(*generic*, *open orbit*) matches what the corpus asserts.

**7. Butruille 2005** (`math/0612655`) — on arXiv, makes `S⁶ = G₂/SU(3)` a
classification rather than an example. Lowest of the seven because the *next* step is
already fenced: `docs/coordination/s5-so3-keystone.md:31,47,51` excludes compact /
finite-dimensional Sasakian arenas for hosting `W_λ`, and
`2026-09-04-the-cr-dimension-decision-full-context.md` §5 shows no resolution of the
dimension question supplies `W`. **An upload here buys citability for the frame, not a
route to the flavour sector.**

**Not an upload, and it outranks items 4–7 on cost/benefit:** rows 4, 6, 9, 12 and 13
are **registry or key edits over material already on disk or already registered** —
register `library/0803219`; add a `hatcher2002` entry; fix `[ohtsuki2016-52]` to
`[ohtsuki2016]`; cite the held `s40879-023-00706-0` (Braden–Disney-Hogg) for
Riemann–Hurwitz; check whether the held Thurston Ch. 2 already covers B1. None needs
egress and none needs a PDF.

---

## 3. Six-path record

| path | run | result |
|---|---|---|
| **0** `corpus_search` (MCP) | attempted | **UNAVAILABLE** — `paper-assistant` `ENOENT`, fourth consecutive session. Every absence here is lexical. |
| **1** `docs/audits/` | ✔ | HIT — the three arc audits; `2026-09-03-cited-not-proved-surface.json` (3529 files, keyed on `sorries`/`axioms`, predates these files); `library-duplicate-ledger.json` (4 entries). |
| **2** `content/` (whole tree, `/.lake/` excluded) | ✔ | HIT — 113 `thurston1978` citers, 63 `murakami-murakami2001`, 63 `neumann-zagier1985`; 10 arc blocks with **no `cites` field**; 4 unresolved `-- Ref:` keys out of 70 distinct. |
| **3** `computations/` | ✔ | HIT — `form_stabilizer_genericity_su3_routes.py:21` asserts the `G₂` 3-form fact; `fibre_functor_dimension_not_categorical_probe.py` consumes `bichon2003`/`etingof-ostrik2004`. |
| **4** `docs/coordination/` | ✔ | HIT — `s5-so3-keystone.md:31,47,51` (the standing `W_λ` exclusion, scope-(a) against a coset route). No ledger on citations. |
| **5** `library/` — INDEX + `summary.json` + `sections/` + **`ocr/`** | ✔ | Mixed. **Saturated** on the hyperbolic-volume layer (Mostow 27 dirs, Riemann–Hurwitz 10, Gauss–Bonnet 16, triangle group 7). **Empty** on CR/contact/Sasakian (0 across all four tiers) and on Woronowicz's own papers (0 `INDEX.md` rows; 0 files containing *"differential calculus"*). |
| **6** `.beans/` (4726 beans; titles + bodies) | ✔ | HIT — 62 `Cite [key] at …` beans exist, two on Riera–Rodríguez for **other** sections; `qou-ic22` wants a key that does not exist. **EMPTY** for `Boyer`, `Galicki`, `Dragomir`, `Bryant`, `Butruille`, `bicovariant`, `triangle group`, `uniformis`, `Gauss-Bonnet`, `hyperbolization`. Zero titles begin `CITE:` — no duplicates minted. |

**Exact-title existence check** was run against all 4726 bean titles before every
`beans create`; zero matches and zero near-matches on any of the fifteen subjects.

---

## 4. What I could not verify

1. **Every bibliographic detail.** Egress to `api.crossref.org` and
   `export.arxiv.org` is **403 (policy denial)**. Volumes, issues, pages and DOIs
   quoted here and in the beans are taken from `references.ts` or from memory of the
   literature and are **not** publisher-confirmed. This is why row 15 is a bean rather
   than a fix.
2. **Whether the 4D bicovariant classification is Woronowicz's or
   Schmüdgen–Schüler's.** The corpus says *"Woronowicz's classification"*; I flagged
   the alternative and did not adjudicate.
3. **Whether `library/thurston` Ch. 2 contains B1** (hyperbolic triangle area = angle
   defect). Its sections cover hyperbolic trigonometry and `cosh d(x,y)`; I did not
   read them closely enough to say. Noted inside `qou-aucv` because it could make row
   13 a no-op.
4. **A systematic `library/<docId>` ↔ `references.ts library.docId` reconciliation.**
   `0803219` was found incidentally. 828 entries, 394 with a `docId`, 576 directories,
   23 of them duplicates — the residual is **not** simply 182 and was not measured.
   That sweep would likely find more of row 4's class and is worth its own bean if
   anyone wants it.
5. **`uploads/`.** 22 PDFs sit there, invisible to path 5. I listed them and matched
   none to this arc, but I did not open any.
6. **Whether the four `Woronowicz`-adjacent keys are each cited for the right paper.**
   `woronowicz1987` (*Compact matrix pseudogroups*) is cited at
   `qou-exists-axiom-1-proof.md:4` for *"Woronowicz's reconstruction theorem"*, which
   is plausible; I did not check every one of the ~15 sites.

## Cross-references

- Arc audits: [`2026-09-04-the-cr-dimension-decision-full-context.md`](2026-09-04-the-cr-dimension-decision-full-context.md) ·
  [`2026-09-04-contact-distribution-complex-rank-and-dimension-seven.md`](2026-09-04-contact-distribution-complex-rank-and-dimension-seven.md) ·
  [`2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md`](2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md)
- Prior surface scan: [`2026-09-03-cited-not-proved-surface.json`](2026-09-03-cited-not-proved-surface.json)
- Duplicates: [`library-duplicate-ledger.json`](library-duplicate-ledger.json)
- Beans minted here: `qou-2hc7` `qou-ezne` `qou-g71v` `qou-mzv5` `qou-iryu` `qou-josl`
  `qou-hfwb` `qou-w5oq` `qou-uzzk` `qou-2u6r` `qou-ctzi` `qou-b5ly` `qou-aucv`
  `qou-3o59` `qou-zx95` — all `--parent qou-8lxd`.
