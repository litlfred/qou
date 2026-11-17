---
# qou-mfdq
title: 'The pole-to-cusp bijection: the .md clause is a cardinality mismatch, and the Lean named for it proves no bijection and no cusp'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T15:56:47Z
updated_at: 2026-10-04T15:15:07Z
parent: b9cj
---

Measured 2026-09-14 while running the one cheap check that could open or close
the ideal-triangulation ↔ q-NS link (the arc question). **Nothing here is acted
on** — per AGENTS.md §"ASK THE OWNER BEFORE CHANGING THINGS", both items below
are owner calls in a mathematics file.

## First: I under-described the link, and that correction comes before the finding

I reported earlier this session that the ideal-triangulation ↔ q-NS connection
is carried by **two `prose` blocks with no dependency edge** — `.ts` manifests
that are literally one line, no `uses`, no `lean`, no `computation`, no
`cites`, no `interprets` — and is therefore at "the lowest epistemic tier the
corpus has".

**The `.ts` claim is true. The framing was wrong.** The `.md` body of
`brings-surface/thurston-relaxation.md` carries a markdown cross-reference:

> ([pole-to-cusp bijection](#conj:algebraic-geometric-dilog-equivalence)(1))

That names a real conjecture block with a sibling `.lean` and a `lean.ref`
(`qou:QOU.QPochhammer.algebraic_geometric_equivalence`), **and it names a
clause number**. So the link is carried at the *conjecture* tier, not as
unmoored prose. What is missing is the `uses[]` edge in the manifest — a
manifest defect, not an absence of connection. A `uses[]`-only search (mine,
and the corpus-grepper's) cannot see a `.md`-body cross-reference.

That is the reusable lesson: **`uses[]` is not the corpus's only edge type**,
and an agent measuring dependency structure from manifests alone will
under-report connections that exist in prose with an explicit `#label`.

## Finding 1 — clause (1) is a bijection between an n-set and a 4-set

`mass-theory/algebraic-geometric-dilog-equivalence.md`, clause (1), verbatim:

> *(**Pole-to-cusp bijection.**) The roots $\{x = q^{-k} : k = 0, \dots, n-1\}$
> of the denominator $(x; q)_n$ are in bijection with the ideal vertices of a
> hyperbolic tetrahedron triangulating the $\Phi_q$-piece $K_S$.*

Count both sides:

- **poles:** $\{q^{-k} : k = 0,\dots,n-1\}$ — exactly **$n$**.
- **vertices:** the ideal vertices of **a** hyperbolic tetrahedron — exactly **4**.

A bijection between them forces **$n = 4$**. And $n$ is not pinned to 4: it is
the partial-product order, and clause (2) of the *same conjecture* takes
$n \to \infty$.

**Scope (b), structural exclusion, invariant = cardinality.** This is a
counting argument, not a numerical probe, so it is a (b) under the
"refuted"-discipline and the invariant is cited. It excludes the claim **as
literally written**; it does **not** exclude the intent. Two repairs are
visible from the corpus itself and neither is mine to choose:

- the sibling statement in `thurston-relaxation.md` says *"the ideal vertices
  of the tetrahedral **triangulation**"* (plural) — $T$ tetrahedra give $4T$
  vertices, so the bijection would need $n = 4T$. Better, still not general $n$.
  **The two statements of the same claim already disagree** about whether it is
  one tetrahedron or a triangulation.
- clause (3) sums one $D(z)$ per subset $S \subseteq \{0,\dots,n-2\}$, i.e.
  $2^{n-1}$ tetrahedra — $2^{n+1}$ vertices. Also not $n$.
- the *sane* reading is the one the second bullet of `thurston-relaxation.md`
  already states: the poles **seed the Newton iteration** on the gluing
  equations. Seeding is not a bijection, and needs no cardinality match.

## Finding 2 — `pole_cusp_bijection_proved` proves no bijection and mentions no cusp

`mass-theory/algebraic-geometric-dilog-equivalence.lean:250`:

```lean
theorem pole_cusp_bijection_proved (q : ℝ) (hq : q ≠ 0) (n : ℕ) :
    ∃ z : Fin n → ℝ, (∀ k : Fin n, z k = q ^ (-(k : ℤ)))
      ∧ (∀ k : Fin n, denomPolyLocal q (z k) n = 0)
```

The type says: *there exists a function whose values are $q^{-k}$ and which are
roots of the denominator.* That is pole-vanishing — correct, unconditional,
sorry-free, good algebra. It is **not** a bijection (no `Equiv`, no
injectivity, no `Fintype.card`), and the words **cusp**, **ideal vertex** and
**tetrahedron** appear **nowhere in the statement**. They are in the name and
the docstring only.

**The file's prose is honest about this** — *"the pole side of the matching is
the unconditional theorem `pole_cusp_bijection_proved`"*, and *"Only the cusp
correspondence … remain[s] the open volume conjecture"*. So the defect is
**the name**, which asserts three things the file itself says are not
established: *cusp*, *bijection*, and — worst — *`_proved`*.

Why the name matters more than usual here: an agent running the corpus-grep
checklist to ask *"is the pole-to-cusp bijection proved?"* finds a sorry-free
theorem named `pole_cusp_bijection_proved` and stops. The name is a trap laid
for exactly the discipline AGENTS.md mandates.

**Prior art, checked — this is NOT a re-report.**
`docs/audits/2026-07-11-algebraic-geometric-dilog-provability.md` already
records that the pole half is provable and the cusp half is open (its lines
38/41/46). It refers to the then-current *class field* `pole_cusp_bijection`.
That field has since been removed; the **theorem** now carries the name with
`_proved` appended, which is strictly stronger than what the audit reviewed.

## Finding 3 — the borrowed-name detector is blind to this BY CONSTRUCTION

`scripts/lean-borrowed-name-audit.py` **runs on this very file and flags a
different declaration** (`asymptotic_volume_of_vc:286`, `major`, ledgered
`proof-borrowed-name`). It does not flag `pole_cusp_bijection_proved`, and that
is not a tuning miss — it is structural:

```python
def borrowed_hits(name, doc):
    for nm in EXTERNAL_NAMES: ...      # people / external theorems
    for ab in EXTERNAL_ABBREV: ...
```

and the audit loop does `hits = borrowed_hits(name, doc); if not hits: continue`.

The detector is scoped to **eponymous** borrowing — a declaration named after
an external body (Seifert, Euler, Kashaev) whose result it does not use. Its
own module docstring says so. `pole_cusp_bijection_proved` borrows **no
external name**; it borrows **mathematical content words** — *cusp*,
*bijection*, *proved* — absent from its own type. `borrowed_hits` returns
empty and the declaration never reaches the gate.

**This is a new class for the detector-blindness taxonomy** (currently 45
rows), and it is not any of the seven existing groups: not a spelling, not a
write path, not a data shape, not a naming-heuristic false positive. It is
**the vocabulary the detector borrows from**: it can ask *"is this named after
someone whose theorem it does not use?"* and cannot ask *"is this named after
a mathematical claim it does not make?"*

**Not added to `docs/audits/2026-08-15-detector-blindness-taxonomy.md`** — the
row-count line is contended (PR #7342 was adding a row concurrently, and I
asked them to renumber). Whoever adds it should re-count the table first; that
line has been stale six times.

## The decision for the owner

Three options; the default is the last.

1. **Rename the Lean declaration** to what it proves — e.g.
   `qPochDenom_poles_explicit` or `pole_side_roots_proved`. *Costs:* one
   declaration, and **measured zero external consumers** (`grep` over all
   `.lean` outside the file: 0 references to it). *Risks:* nothing
   mathematical; the proof is unchanged. *Commits to:* nothing — it removes a
   claim the file already disclaims.
2. **Also repair `.md` clause (1)** to the seeding statement the corpus's own
   `thurston-relaxation.md` second bullet already makes, or to an explicit
   $n = 4T$ form. *Costs:* a content-block edit plus its render-QA gate and
   sidecar refresh. *Risks:* it is a conjecture statement — changing what it
   asserts is a mathematical decision, not an editorial one. *Commits to:* a
   particular repair of the bijection, which forecloses the others.
3. **Do nothing.** The conjecture stays as written, the theorem keeps its
   name, and the audit keeps not seeing it. Nothing downstream moves: the
   cusp half is already recorded as open in the 2026-07-11 audit and in the
   file's own prose.

**Agent recommendation (judgement, not a finding): option 1 only.** The rename
is zero-consumer, mathematically inert, and removes a trap aimed squarely at
the corpus-grep discipline. Option 2 asks an agent to pick which of three
inequivalent repairs the conjecture *meant*, and that is the author's call, not
a tidy-up.

## What this settles about the arc question

The ideal-triangulation ↔ q-NS link **is** carried at the conjecture tier, not
merely in prose — that is better than I reported. But the single clause that
connects the algebraic side to the geometric side cannot be literally right,
and the Lean named for it establishes only the algebraic half. So the arc's
joint is **stated, cited, half-proved, and mis-stated at the join** — which is
a more useful answer than either "it's real" or "it's decorative".


---

## 🛑 CORRECTION (2026-09-14, same day): Finding 2 is a RE-REPORT, and this bean said it was not

Finding 2 above asserts, in bold, **"Not a re-report."** That is **false**, and
it merged to `main` in PR #7364 before I caught it.

**`docs/audits/2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md`
already contains the finding, ten days earlier, with the same reasoning and a
proposed name.** Its §"Claim-shape defect" box, verbatim:

> **🛑 Claim-shape defect — the theorem is named for something it does not
> contain.** The wrapper is called **`pole_cusp_bijection_proved`** … **There is
> no cusp in it, and no bijection** — it exhibits `n` roots of a polynomial. The
> *file* is honest about this in prose …, so the defect is the **name**, which
> is what a downstream reader greps. Anyone citing `pole_cusp_bijection_proved`
> as evidence for L2 is citing a polynomial root-finding lemma.

and its §"Two moves, in order, neither of which is research" item 1:

> Also **rename `pole_cusp_bijection_proved`** to say what it proves
> (`qPochDenom_roots_explicit` or similar) — the current name is the sort of
> thing that gets cited as evidence for L2.

So the finding, the argument, the emphasis on *the name being what a reader
greps*, and the remedy were all already on record.

### How I missed it, which is the part worth keeping

**The corpus-grep did not fail. I did.** My path-1 grep
(`pole.*cusp.*bijection\|pole-to-cusp` over `docs/`) **returned this exact file
in its hit list**. I opened `2026-07-11-algebraic-geometric-dilog-provability.md`
from the same list, found it discussed the pole/cusp split, satisfied myself that
it covered a *different* (older, class-field) version, and declared novelty —
**without opening the other hit**.

That is a distinct failure from the ones this repo catalogues. The documented
classes are *the grep missed it* (wrong words, wrong tier, wrong tree). This was
**the grep found it and I did not read it**: a hit list treated as a checklist
item rather than a list of things to open. The discipline says the six paths must
return empty before declaring an item open — mine returned **five hits** on path
1 and I read one.

**Rule for next time, stated so it is checkable:** when a path returns multiple
hits, novelty may be declared only after every hit is opened, or after each
skipped one is named with the reason it was skipped. "I read the most relevant-
looking one" is not a reason.

### What survives, and what does not

- **Finding 2 — WITHDRAWN as novel.** It is a confirmation of the 2026-09-04
  audit, independently reached. Independent confirmation has some value; it is
  not a finding, and this bean claimed it was.
- **Finding 1 (the `n`-set ↔ 4-set cardinality mismatch in `.md` clause (1))** —
  the 2026-09-04 audit discusses *scope* nearby ("L2/L3 are stated for the
  `Φ_q`-piece `K_S`, not for general knots … a reader who takes it as a general
  pole↔cusp statement is over-reading it") but makes **no counting argument**.
  Believed to survive. Flagged as believed rather than established, because this
  correction is precisely about over-claiming novelty.
- **Finding 3 (the borrowed-name detector blind by construction)** — the
  2026-09-04 audit does not mention `lean-borrowed-name-audit.py` at all.
  Believed to survive, same caveat.

### The rename LANDED, and it is now a documented-recommendation execution

Renamed `pole_cusp_bijection_proved` → **`denomPolyLocal_roots_explicit`** (5
occurrences in the `.lean` + 1 in the `.md`). The name follows this file's own
convention — its siblings are `denomPolyLocal_succ` and
`denomPolyLocal_eq_zero_at_pole` — which is within the audit's
"`qPochDenom_roots_explicit` **or similar**" (`qPochDenom` is the generic twin in
`lean/QOU/QBeta/QPochhammerPoles.lean`, not this file's local object).

This also **changes the authorisation basis and strengthens it**: it is no longer
an agent-proposed change awaiting a call, it is the execution of a recommendation
the corpus already recorded — AGENTS.md §"ASK THE OWNER" exemption 2
(*derived from the corpus*, checkable by opening the artifact it cites) — with
the owner's explicit "rename" on top.

**Dated docs deliberately left carrying the old name** (3 files, 4 lines):
`2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`,
`2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md` (×3),
`docs/coordination/2026-07-24-delta-lambda-binding-front-convergence.md`. Same
decision as the `4.66e6` drain (`qou-3nva`): dated audits are records of their
own analysis. Whether to mark the 2026-09-04 recommendation as landed is a
separate, cheap call and is **not** taken here.

---

## EXPLORED 2026-09-14 (PR #7401, issue #7400) — Finding 1's framing was wrong, and Finding 3 has a sharper second half

The owner asked for both open findings to be explored. Both survive; both were
mis-framed here, and in opposite directions.

### Finding 1 — I framed a settled question as an open one

This bean says the repair "means choosing among three inequivalent statements"
and recommends **not** touching it. That treats as a mathematical choice
something **the corpus had already decided in the sibling block this bean never
opened.**

`shared-denominator-cusp-holonomy.md` is named by clause (1) itself as the
carrier of the bijection, and it says **tetrahedra**, twice:

- statement (`:28-32`): `Hol_μk(z_k) = Hol_λk(z_k) = 1` "for some cusp k", `z_k`
  the shape of the ideal tetrahedron at cusp k;
- table row 4 (`:49`): "GB-depth k_star = n | thimble dimension n |
  **n ideal tetrahedra in JSJ piece**".

And the compute agrees: `snappy_cusp_seeding.py:66` sets
`n = M.num_tetrahedra()` and emits **one algebraic seed per tetrahedron** —
**8** for `L6a4`'s 8 tetrahedra, not 3 for its 3 cusps.

So the corpus carries **six** statements with **five** counts (4 vertices / 1
tetrahedron / c cusps / T tetrahedra / 4T vertices), and clause (1) is the sole
outlier. This bean found three of the six and missed the two that decide it.

**For 4_1, measured from the corpus's own witness** (`m004`): vertices of one
tetrahedron **4**, tetrahedra **2**, `4T` **8**, cusps **1** — and the braid
whose closure it is, `(σ₁σ₂⁻¹)²`, lives in `H_3`. Four candidate targets and the
algebraic side matches none, because **`n` is not pinned**: it is the Hecke
index / GB-depth in the carrier's hypothesis, `num_tetrahedra()` in the compute,
a free sweep `MAX_DEPTH = 4` in `q_pochhammer_seed.py`, and `n → ∞` in clause
(2). So this bean's counting argument is sound but **unposable** — you cannot
compare `n` to 4 until someone says what `n` is.

**The part that is not a judgement call at all, and this bean missed it
entirely.** `algebraic-geometric-dilog-equivalence.md` §Witness asserted four
things its own cited witness denies — "the trefoil" (0 occurrences in producer
or witness), "n = 3" (the producer sweeps 1-4), "the SnapPy-solved cusp shape
parameters" (the producer **never imported snappy in any commit**;
`git log -S "import snappy"` is empty — it pairs against the 6 Picard-Lefschetz
discriminant roots of the colour-tube cubic), and "the residual after one Newton
step" (9 of 10 runs, up to 11 iterations). The witness refutes it in its own
`caveats`. The sibling block describes the **same** witness correctly.

**Landed in #7401:** the §Witness rewrite, clause (1) and the Kashaev table row
retargeted to tetrahedra, a scoping note recording that `n` is still unpinned,
and the sixth "depth" sense registered in `notation-collisions.md`. I
recommended deferring the clause (1) repair until `n` is pinned; **the owner
directed it**, and that is recorded in the commit.

**Split out:** the two dead `conj:` labels both producers declare, and the dead
`prop:jet-gb-pl-correspondence` behind `thurston-relaxation`'s "GB-PL
bijection", are `qou-3kni` — including why the producer docstrings were NOT
edited (neither producer can be re-run here: no `snappy`, and local `mpmath`
1.3.0 against the witness's 1.4.1).

### Finding 3 — mechanism confirmed, one claim downgraded, one half added

**Confirmed against the live code**, not asserted:
`borrowed_hits("pole_cusp_bijection_proved", doc)` returns `[]`, so
`if not hits: continue` (line 316) discards it before any other signal runs.

**Added, and it is the sharper half:** `borrowed_hits` reads
`split_camel(name) + " " + doc`, while `overclaim = bool(OVERCLAIM.search(doc))`
(line 338) reads the docstring **alone** — and `OVERCLAIM` matches `'proved'`.
The detector **held the token and never looked where it was written**. Verified
by importing the module: `OVERCLAIM.search(doc)` False,
`OVERCLAIM.search(split_camel(name))` True.

**Downgraded:** measured corpus-wide, that asymmetry costs **10 of 25,810**
provable declarations (7 also eponym-free, so never scored at all), and the 3
that do reach classification look legitimate. So the asymmetry is real but
nearly benign — weaker than this bean implied.

**The class is not benign, and is now measurable.** Guard
`scripts/lean-structure-word-audit.py` (taxonomy **row 46**, added #7401) finds
`pole_cusp_bijection_proved` as the **sole** `bijection` member at `926f2c71ec^`
and zero after the rename, and **13 live members under `iff`** — `qou-bybn`.

🛑 **My first calibration of that probe reported 173 `unique` hits and every one
was Mathlib's uniqueness idiom** (`(a b : T) … : a = b`, no `∃!`). 173 false
positives from one convention I did not know, in the probe written to extend
taxonomy row 45 — whose lesson is that an audit self-certifying its calibration
cannot discover its own blind spot. The `--selftest` now pins the limit as well
as the catch.

### Prior-art, run properly this time

The §CORRECTION above records that I declared novelty after a path returned five
hits and I opened one. This time all six paths were run and every hit opened
(path 0 `corpus_search` was **UNAVAILABLE** — the `paper-assistant` MCP failed
to connect — so both negatives are scope-(a), not scope-(b)).

Result, and it lands on this bean: **Question 1 was ALREADY RECORDED — by
Finding 1 of this bean**, for the vertices-vs-tetrahedra half. The
cusps-vs-tetrahedra half, the `shared-denominator-cusp-holonomy` internal
disagreement, and the producer's 8-seeds-against-3-cusps are on **no** path.
**Question 2 — that `n` carries both the Hecke-index and tetrahedron-count
meanings — is NOT FOUND on all six paths**; the register's own "depth" collision
entry had five senses and none was the tetrahedron count, which is why the sixth
was added.

One more thing worth flagging separately: the corpus-grepper reported that
AGENTS.md's agent-memory figures are stale — it states "195-419 lines for
MEMORY.md and 412-657 for the directory"; measured, `lean-verifier` is **721**
and its directory **2484**, and three of five directories exceed the stated
range. Not fixed here.

## Progress Update (Round 59 — PR #8316)
- **Status:** `in-progress` (opened `litlfred/qou#8316`, branch `claude/round59-devacuify-6qbv-b9cj`, HEAD `53b4a670e74a8018b8da97a71f572d818338e732`, C1 `76d4ce5f89f2c26a87c0da074bf6c76b37e0ea03`).
- **Target:** `folio/quantum-observable-universe/lean/QOU/QBeta/QPochhammerPoles.lean` + 80-dps witness `computations/probes/round59-devacuify-6qbv-b9cj.witness.json` (`scriptHash = 80c9bce8d43a`, `allPassed = true`, `0` `float64`).
- **Updated at:** `2026-11-17T10:55:34Z`.
