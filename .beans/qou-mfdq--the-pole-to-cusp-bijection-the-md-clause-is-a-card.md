---
# qou-mfdq
title: 'The pole-to-cusp bijection: the .md clause is a cardinality mismatch, and the Lean named for it proves no bijection and no cusp'
status: todo
type: task
priority: high
created_at: 2026-09-14T15:56:47Z
updated_at: 2026-09-14T15:56:47Z
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
