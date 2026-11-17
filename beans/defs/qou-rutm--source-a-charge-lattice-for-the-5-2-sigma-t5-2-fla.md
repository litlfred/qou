---
# qou-rutm
title: 'Source a charge lattice for the 5_2 sigma: T[5_2] flavour lattice from 3d-3d (D1-b arrow test)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T07:37:09Z
updated_at: 2026-10-04T15:13:58Z
parent: b9cj
---


## 2026-09-04 opened — three routes closed on the first pass; the gap is now named

Opened on owner instruction ("sourcing a 5₂ charge lattice is worth opening")
after `qou-q9ih` reduced the D1-b arrow question to one labelled hypothesis with
one test:

> **H:** the D1-b quiver has `V = 3` (the three σ) and 3 arrows (the three
> unordered pairs `{12,13,23}`), the two rays being the two orientations.
> **Test:** compute the Dirac pairing `⟨γᵢ,γⱼ⟩` on the 5₂ charge lattice; if it
> is not supported on exactly `{12,13,23}`, H is dead.

`computations/qbeta/d1b_52_charge_lattice_sourcing_probe.py` (6/6, exact
integers) went to source that lattice. **It does not find one**, by three
independent routes — and none of them is a failed numerical search.

**R1 — the paper that produced the datum defines no lattice.** Measured over the
sectioned text of GGM `arXiv:2012.00062v3`: `"charge lattice"` **0**,
`"Dirac pairing"` **0**, `"symplectic"` **2** — both in §7 and both naming
Neumann–Zagier. The σ are labels for asymptotic series; GGM equips them with no
lattice and no pairing. So **H's test has no referent in its own source.**

**R2 — Neumann–Zagier, the paper's own candidate, is Lagrangian exactly where it
would have to matter.** Antisymmetrizing the rect gluing datum,
`J = A·Bᵀ − B·Aᵀ`:

* the **edge block is exactly the zero matrix** — `A·Bᵀ` is symmetric, which *is*
  the NZ symplectic theorem;
* the **entire** nonzero content is the **rank-2 cusp block** `(μ,λ)` carrying
  `±2`, i.e. the 1-cusped relation `A_μ·B_λᵀ − A_λ·B_μᵀ = 2`.

Measured for **both** 4₁ (N=2) and 5₂ (N=3), so it is structural, not an
accident of tetrahedron count. eq (98) is **rank 3**; the NZ antisymmetric
content is **rank 2, always**. So NZ cannot carry an eq-(98)-shaped pairing at
any index set — **scope-(b)**, invariants cited being the NZ symmetry theorem
and the cusp relation. What antisymmetric content NZ *does* have lives on the
**boundary torus**, which is about the cusp, not about saddles.

**R3 — KRSS is the wrong symmetry class.** `arXiv:1707.02991v1` ("BPS states,
knots and quivers") is the one held source assigning a quiver to a knot, and its
quivers are **symmetric** by its own definition — *"the number of arrows from i
to j equals the number of arrows from j to i"*. eq (98) is **antisymmetric**, so
it is not a KRSS quiver matrix before any question of values.

> **Do not merge R3 with the standing refutation.** `qou-q9ih` says *"do NOT
> resurrect the refuted KRSS open-sector route (det(K)=5)"*. That is a
> refutation of a particular **open-sector** construction. R3 is a structural
> remark about the **symmetry class**, applies to the closed sector, and is
> recorded separately so neither is read as evidence for the other.

**What remains, named precisely.** A map

    {σ₁, σ₂, σ₃}  (saddles / asymptotic series, GGM)  ⟶  Γ

where `Γ` carries an antisymmetric integral pairing. It would come from the
**3d-3d correspondence** — the flavour/charge lattice of `T[5₂]` — which is
**not held in `library/`** and is not computable from anything in this repo.

**Consequence, and it is sharper than "blocked".** Until that map exists, **H is
UNSTATED, not merely unconfirmed**: the phrase "the Dirac pairing on the
charges" does not yet denote anything. The honest next step is acquiring a 3d-3d
source (a DGG-lineage paper giving `T[M]`'s flavour lattice for a census knot),
not another probe against what is already held.

## 2026-09-04 CORRECTION — I named one route and called it *the* route

The first pass ended: *"a lattice for the σ would have to come from the 3d-3d
correspondence … not held in `library/`, not computable from anything in this
repo"*, and concluded the next step was **acquiring a paper**. **Both halves
were too strong**, and the trigger was a sibling landing —
[`2026-09-03-colour-cubic-is-a-rank-three-spectral-curve.md`](docs/audits/2026-09-03-colour-cubic-is-a-rank-three-spectral-curve.md),
which merged to `main` while this branch was open.

**Route 2, never named.** For a spectral curve `Σ`, the charge lattice is
`H₁(Σ,ℤ)` with its **intersection form** — a canonical antisymmetric integral
pairing. That is the standard Seiberg–Witten / Hitchin construction and it does
**not** route through `T[5₂]`'s flavour lattice at all. Naming the 3d-3d route as
the only one was an assertion, not a measurement.

**And the repo is not empty of the machinery** (measured):

* **A-polynomial producers, 3** — `aj_figure_eight_operator_construct_verify.py`,
  `aj_trefoil_operator_construct_verify.py`, `borromean_apoly_renormalize.py`.
* **A rank-3 spectral curve worked in-corpus** — the colour cubic
  (`ColorSpectralCubicGeometry`, `bring_cubic_monodromy_probe`). **Wrong curve
  for 5₂, right method.**
* **Intersection-form machinery, 10 files** — including the literal
  `intersection form J = V − Vᵀ`, the Seifert-form antisymmetrization, live in
  the `nastokes_*` probes.

**🛑 My own control caught my own sub-claim.** C7's assertion originally required
**zero** intersection-form files and **FAILED at 10**. So the correction is
*stronger* than its own first draft: the repo has **both** halves of route 2, not
just one. Worth recording because it is the fourth time this session that a
check I wrote to test something else caught a claim I had smuggled past myself.

**What is genuinely absent, and it is narrow:** nothing computes 5₂'s
A-polynomial specifically, and the live intersection forms are on **Seifert
surfaces** rather than on a **spectral curve** — a different lattice, the same
construction.

**So the next step is in-repo work, not an ingest**: extend the existing
A-polynomial machinery to 5₂, then compute `H₁` and its intersection form. That
is a substantially better rung than "acquire a paper", and it is work I can do.

**NOT claimed:** that route 2 succeeds. Whether `H₁(Σ)` is the right lattice for
the σ is exactly as open as route 1 was. Only the *availability* claim is
corrected.

## 2026-09-04 🛑 CORRECTION TO MERGED WORK — "eq (98) is rank 3" is impossible

The first pass merged as **#6599 / `74a927b6af`**, and its headline verdict **C4
is void**. Found while starting the next rung, by asking what rank the target
lattice could have.

**What merged:**

> "eq (98) is a rank-3 antisymmetric integer matrix. The NZ datum's
> antisymmetric content has rank 2, always. ⇒ scope-(b) exclusion."

**eq (98) has rank 2.** I wrote its **size** (3×3) and then used it as a **rank**
in a rank comparison. And rank 3 was never available, for a reason that takes one
line: `det A = det(−Aᵀ) = (−1)ⁿ det A`, so an odd-size antisymmetric matrix is
singular — **an antisymmetric matrix always has even rank**. Measured:
`det(eq 98) = 0`, exact rank over ℚ = **2**.

So the comparison put a *size* against a *rank*, and **both objects are rank 2** —
which makes the NZ cusp block **more** plausible as a carrier, not less. The one
invariant I used to exclude it is the one on which the two agree.

**What actually discriminates them.** A rank-2 antisymmetric integral form is
`[[0,d],[−d,0]] ⊕ 0` up to `GL(ℤ)`, so the elementary divisor `d` is the complete
invariant. By Smith normal form:

| form | SNF | `d` |
|---|---|---|
| eq (98) | `[1, 1]` | **1** |
| NZ cusp | `[2, 2]` | **2** |

**Inequivalent over ℤ, equivalent over ℚ.**

**Re-scoped (b) → (a).** AGENTS.md reserves scope-(b) for exclusions resting on a
*proved invariant*; the invariant cited was a miscomputed rank, so the label was
unearned. The defensible statement is scope-(a): *the NZ cusp form is not on the
nose the eq-(98) form — integral factor 2, and indexed by (μ,λ) rather than by
the three σ.*

**🛑 THE NZ ROUTE IS NOT EXCLUDED.** Charge lattices are routinely defined only
up to normalisation, and the two forms agree over ℚ. Anyone reading the merged C4
as "NZ is dead" is reading a defect.

**Unaffected, because they are measurements rather than inferences:** C1 (GGM
defines no lattice, 0/0), C2 (NZ edge block exactly zero), C3 (antisymmetric
content is the rank-2 cusp at ±2), C5 (KRSS quivers symmetric), C7 (route 2
exists, repo has both halves). Only C4 is void.

Probe: `computations/qbeta/d1b_eq98_rank_correction_probe.py` (5/5). The merged
probe now carries a void banner at the top of its docstring.

**The pattern, fifth instance today and the worst of them.** Every previous one
was caught by a control or a grep before it reached anyone. This one **merged**.
The common shape: a quantity read at the wrong type — a Stokes constant read as
an object count, an antisymmetry read as evidence, a population read as a
singular fact, and now a matrix size read as a rank. Cheapest guard for this
class: when a number enters an argument as an invariant, **compute it** rather
than reading it off the shape of the object.

**Follow-through, same session: the `d=1` vs `d=2` gap is NOT an obstruction
either, and the real difference is a radical.**

The correction above offered `d(eq 98) = 1` vs `d(NZ cusp) = 2` as the surviving
scope-(a) statement. Measured, that too dissolves:

* `NZ cusp / 2 = [[0,1],[−1,0]]`, **integral and unimodular**. So the NZ cusp
  form is `2 ×` a unimodular rank-2 form and eq (98) is already unimodular on its
  support. They differ by an **overall factor 2** — a normalisation convention
  for the NZ symplectic form, not a lattice-theoretic obstruction.

So **even the re-scoped (a) statement is not evidence against the NZ route.**
Three successive verdicts on this comparison have now each been weaker than the
last: scope-(b) exclusion → scope-(a) "not on the nose" → **no obstruction from
the form at all**.

**What genuinely survives is one thing, and it is new.** eq (98) has a
**1-dimensional radical**, spanned by the axis vector `(Ω₂₃, −Ω₁₃, Ω₁₂) =
(−3,−3,4)`; verified `eq(98)·axis = 0`. The NZ cusp form has none. So the
difference is not rank and not the divisor — it is that eq (98) lives on a
**rank-3 lattice with a null direction** while the NZ cusp form lives on a
**rank-2 lattice without one**.

**Guard, because this corpus invites exactly this mistake:** the radical being
built from the `Ω` entries is **forced**, not a coincidence. Any 3×3
antisymmetric matrix is the cross-product matrix of its axis vector, so
`(−3,−3,4)` carries no information beyond the entries themselves. **Read no
numerology into it.**

**Where that leaves the rung.** In Seiberg–Witten terms a null direction of the
Dirac pairing is a **flavour** charge. So the open question for the NZ route is
no longer "why rank 2" — it is **"where is the third, null direction"**. That is
a sharper and more answerable question than the one this bean opened with.

Probe: `d1b_eq98_rank_correction_probe.py`, now 7/7.

## 2026-09-04 ANSWERED — the null direction is MIRROR-SYMMETRIC, and eq (100) forces it

The rung's one surviving question — *where is the third, null direction?* — has an
answer, and it is a derivation rather than an observation.
`d1b_null_direction_is_mirror_symmetric_probe.py` (5/5).

**The derivation.** Every 3×3 antisymmetric matrix is the cross-product matrix of
an axis vector, so writing `M(a,b,c) = [[0,c,−b],[−c,0,a],[b,−a,0]]` the radical
is `span{(a,b,c)}` — asking where the null direction points *is* asking about
`(a,b,c)`. Impose GGM **eq (100)** (`S_ij = −S_{φ(i)φ(j)}`, `φ = (1 2)`)
entrywise:

| entry | condition | yields |
|---|---|---|
| (1,2) | `c = −(−c)` | automatic |
| (1,3) | `−b = −a` | **`a = b`** |
| (2,3) | `a = −(−b)` | `a = b` (same) |

So eq (100) **forces `a = b`** and leaves `c` free. Since `φ = (1 2)` acts on `ℤ³`
with `+1` eigenspace `{(x,x,z)}` (dim 2) and `−1` eigenspace `{(x,−x,0)}` (dim 1),
the radical `(a,a,c)` is **mirror-symmetric for every admissible `M`**, and
anti-symmetric only for `M = 0`.

Confirmed exhaustively over `|entries| ≤ 4`: all **81** solutions have `a = b` —
exactly the `(a,a,c)` family, `(2·4+1)² = 81`.

**eq (98) instantiates it.** Axis `(−3,−3,4)`: `Ω₂₃ = −Ω₁₃ = −3` is the *forced
relation*, `Ω₁₂ = 4` the *free entry*. So that vector is **one constraint plus one
number**, not three independent facts.

**This does not contradict the previous rung's guard.** That guard says the
radical is built from the `Ω` entries *by antisymmetry alone*, hence carries no
information — true, and about 3×3 matrices in general. This is a **second,
independent** constraint, from eq (100), about *this* datum: antisymmetry says
"the radical is the axis vector"; eq (100) says "the axis vector is
mirror-symmetric". Only the latter is informative here.

**What the NZ route must now supply — precise, not a gap.** Embed the rank-2
`(μ,λ)` cusp form in a rank-3 lattice whose adjoined third direction is
**(i)** null for the pairing and **(ii)** fixed by the bar involution.

**OBSERVATION, labelled, NOT a claim.** The earlier rung proved the NZ **edge**
block is exactly zero — Lagrangian — so every edge direction is null and (i) is
abundantly satisfied there. Whether any satisfies **(ii)** is **untested**. It is
recorded as an observation because *"null directions exist over here and I need a
null direction"* is a matching **necessary** condition, and a matching necessary
condition is not evidence — the precise failure shape that has misfired
repeatedly on this object today.

**Disconfirmation, and the next rung:** exhibit the bar involution's action on the
NZ edge lattice and check whether any null direction is fixed. **If none is,
(ii) is the NZ route's real obstruction** — and that would be a genuine
scope-(b), unlike the one I had to retract.

**Same session, testing the labelled observation — and I ran a BROKEN detector
and believed its zero.**

I went to run C5's disconfirmation. First result: a grep pair reporting that
**0** of the files mentioning "bar involution" touch gluing/Neumann/tetrahedra,
from which I wrote *"no bar involution is defined on the NZ lattice anywhere in
this corpus"* and concluded requirement (ii) was **unstatable**.

**That was a false negative from my own check.** Re-run correctly: **35** of them
match. And what is there is directly on this rung:

* [`QOU/QBeta/CuspShapeBarParity.lean`](folio/quantum-observable-universe/lean/QOU/QBeta/CuspShapeBarParity.lean)
  — `barEven`/`barOdd` on the **cusp shape** `ω`, stating in as many words that
  *"the `√−3` that drives the **Neumann–Zagier deformation** `CVol(u) = Vol −
  (τ/4)u² + …` is `barOdd(ω)`"*;
* [`QOU/QBeta/BarParityZeta4Swap.lean`](folio/quantum-observable-universe/lean/QOU/QBeta/BarParityZeta4Swap.lean)
  — the `barEven`/`barOdd` carrier it builds on.

**So bar parity DOES act on NZ-adjacent geometric data**, and my retraction of
the previous claim was itself over-stated. Two caveats keep this from closing
requirement (ii):

* it is **4₁** (both tetrahedra at `ω = e^{iπ/3}`), **not 5₂**;
* it acts on the cusp **shape**, a scalar — not yet on a lattice **direction**,
  which is what (ii) needs.

**The 5₂ analogue of `CuspShapeBarParity` is now the concrete next object** —
much better defined than "acquire a source", and in the same file family.

**Why the false negative happened, since the mechanism matters more than the
number.** The detector returned a zero that *agreed with the shape of the
previous finding* (R1: "GGM defines no lattice"), so it read as confirmation
rather than as a bug. A result that matches what you already believe gets less
scrutiny — which is exactly when a silent tooling failure lands.

**Also recorded: a near-miss caught BEFORE publication.** snappy reports
`Manifold('5_2').is_isometric_to(reverse_orientation())` = **True**, which looks
like "5₂ admits a mirror self-map" and would have handed (ii) its involution for
free. It is **not a fact about 5₂**: mirroring `S³` gives an
orientation-reversing homeomorphism of *any* knot complement onto its mirror's,
so the call returns True for every knot and has no discriminating power. Same
shape as the session's other misreads — a true statement with no power, mistaken
for evidence.

Probe: `d1b_null_direction_is_mirror_symmetric_probe.py`, 7/7.


## (n) 5₂ cusp shapes in bar-parity — MERGED (#6776, superseding #6694), d6b138d8ef

The rung named by #6676. Result is a **negative and that is the substance**:
5₂ has three ideal tetrahedra with `z₁ = z₃ ≠ z₂` (exactly), both shapes cubic
with *different* minimal polynomials `z³−2z²+3z−1` (A) and `z³−2z²+z−1` (B),
both of discriminant −23 and signature (1,1) — one cubic field, two generators.
The (1,1) independently reproduces what `dt_d1b_trace_field_bar_grading_probe`
got by Sturm counting.

Both cubics are irreducible over ℚ, so **neither shape has rational `barEven`**.
4₁'s `barEven ω = 1` IS rational, and that rationality is exactly what makes its
bar-even coordinate the anchor-stable `−Vol(4₁)` part. **So the 4₁ bar-parity
story does not transcribe** — 5₂'s split lands in a cubic field, not in ℚ + √−3.

Recorded but NOT claimed: B's bar-even coordinate is literally `Φ₆(z) = z²−z+1`,
the polynomial whose vanishing defines the 4₁ shape. Two lines from
`z⁻¹ = (z−1)²`. No interpretation attached.

Guard recorded in the probe (C7): the shapes are (A,B,A) and eq (98)'s radical
is (a,a,c) — both "two equal, one different". **Not the same fact.** Different
index sets, no map between them, and the equal pair sits at different positions
({1,3} vs {1,2}). Matching shape is not matching structure.

**Lean caught a false theorem.** `shape52A_not_shape52B` was stated over a
general field and is FALSE in characteristic 2, where both cubics collapse to
`z³+z+1`. It now carries `(2 : R) ≠ 0`, and the collapse is recorded as a
theorem (`shape52_cubics_agree_in_char_two`), not a footnote.

**The verification had to be redone, and this is the reusable part.** The first
`lean`-direct exit 0 was against the restored cache, which is MIXED-AGE: this
file's one dependency olean was dated 2026-08-08 against a source last committed
2026-08-28 — 20 days stale. Same class as the `descartesWtrace` red that landed
on main the same day (`d3b96a29f0`). The merge was withheld and the file
re-verified by rebuilding that dependency from current source into a shadow
placed first on LEAN_PATH. **The mathematics did not move; the evidence did.**

Note for staleness accounting: this file is NEW, so it is in none of the 305
changed-since-snapshot modules `qou-56qy` counts. A new file inheriting a stale
import is invisible to any drift measure keyed on changed sources.


## (o) THE RUNG'S OWN QUESTION, ANSWERED — and the answer is a scope-(b) NO

This bean opened as *"source a charge lattice for the 5₂ flavour"*. Measured:
**it is not sourceable from the held knots-quivers literature, and the exclusion
is structural rather than a search that came up empty.**

**What the corpus holds.** Two documents:
`arxiv-1707.02991v1` (KRSS, the correspondence itself) works **one** explicit
example and it is the trefoil — measured, 8 'trefoil' lines, 0 for 5₂.
`physrevd108106023` (Singh et al., *Knot-quiver correspondence for double twist
knots*, PRD 108 106023) gives explicit quiver matrices for a whole family, and
is **already cited in this corpus** at `conj:stokes-dt-bps-bridge` (beans
`qou-bk77`, `qou-qu53`, `qou-48dw`).

**Why 5₂ is not in that family.** The paper parametrises double twist knots as
`K(p,−m)` and gives their Alexander polynomial in ONE parameter (its eq (5)):

    Δ_{K(p,−m)}(x) = 1 − pm·(1−x)²/x

At `x = −1` that is `Δ(−1) = 1 + 4pm`, so **every member has determinant
≡ 1 (mod 4)**. `det(5₂) = 7 ≡ 3 (mod 4)`. So 5₂ is `K(p,−m)` for **no** positive
integers p, m.

**Scope (b), invariant cited: the knot determinant mod 4.** The argument
excludes the entire two-parameter family, not the finitely many members the
paper tabulates — that is what makes it (b) rather than (a).

**The formula is confirmed by the paper's own knot list**, five for five, from a
formula fitted to none of them: `K(1,−1)=4₁` pm=1→5 ✓, `K(2,−1)=6₁` pm=2→9 ✓,
`K(3,−1)=8₁` pm=3→13 ✓, `K(2,−2)=8₃` pm=4→17 ✓, `K(3,−2)=10₃` pm=6→25 ✓. And
the exclusion predicts the shape of that list: 3₁ (det 3) and 7₂ (det 11) fall
the same way, which is exactly why the paper's worked twist knots are
4₁/6₁/8₁ and never the odd-index ones.

**The guard is the more important half.** Both held sources say **in their own
words** that their quivers are **symmetric** — `physrevd108106023`
intro:33 *"quivers are symmetric quivers. That is, C(K)…"*, KRSS
sec-001:26 *"known for symmetric quivers, i.e. such that…"*. GGM eq (98) is
**antisymmetric**. So a sourced 5₂ quiver would be the **wrong object anyway**:
a symmetric integral form and an antisymmetric one are not two presentations of
one thing. Matching them would be the same category error as reading a matrix's
SIZE as its RANK (#6643, corrected).

**What this does NOT claim:** that no 5₂ quiver exists anywhere. The measured
scope is the two documents this corpus holds. But C7 stands regardless of what
turns up, because anything from this literature is symmetric.

Determinants computed as `|det(V + Vᵀ)|` from exact integer Seifert matrices
(spherogram), determinant by `Fraction` elimination, **calibrated 8/8 against
independently known values before any conclusion rested on it**. No floats.

Probe: `d1b_52_charge_lattice_source_exclusion_probe.py`, 7/7, all four
pre-recorded predictions confirmed.

**Consequence for the arc.** The sourcing rung is closed as a negative. The two
live items it hands on are already-open beans rather than new ones:
`qou-48dw` (cross-check `aomega_bps_sector_nondegeneracy.py`'s 5-node 4₁ count
against the now-legible published 5×5 matrix — the OCR of `C_41` reads cleanly
in sec-005 lines 100-115) and `qou-bk77` (cite the source at the block whose
non-degeneracy table asserts that count).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 59 — PR #8316)
- **Status:** `in-progress` (opened `litlfred/qou#8316`, branch `claude/round59-devacuify-6qbv-b9cj`, HEAD `53b4a670e74a8018b8da97a71f572d818338e732`, C1 `76d4ce5f89f2c26a87c0da074bf6c76b37e0ea03`).
- **Target:** `folio/quantum-observable-universe/lean/QOU/QBeta/BarParityZeta4Swap.lean` + 80-dps witness `computations/probes/round59-devacuify-6qbv-b9cj.witness.json` (`scriptHash = 80c9bce8d43a`, `allPassed = true`, `0` `float64`).
- **Updated at:** `2026-11-17T10:55:34Z`.
