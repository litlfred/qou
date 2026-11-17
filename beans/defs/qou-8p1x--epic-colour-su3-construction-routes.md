---
# qou-8p1x
title: Routes to a 3-dimensional fibre / colour SU(3) — assessed and roasted
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-10-10T13:49:31Z
parent: qou-8lxd
---

Umbrella for every proposed route to colour `SU(3)`, old and new, after the
Bring -> Klein bridge was excluded (`qou-8p1b`, scope-(b)).

## The gap, stated once, precisely

**NOT** "why `N = 3`" — that is DONE. `RowCapObstruction.lean` already proves
the Weyl arithmetic (`weylDimAlt N = N.choose 3`, `no_singlet_of_lt_three`,
`singlet_forces_three`). Do **not** re-derive it.
`a2-from-three-strands.md` explicitly disclaims supplying it (its `A_2` is the
Coxeter group on three *strands*, not the `sl_3` acting on the fibre).

The gap is upstream of all of that:

> **The single-fibre construction supplies `dim V = 2`. Colour needs a
> 3-dimensional fibre.**

Every route below is judged on one question: **does it produce that object?**

## Scoreboard

| # | Route | Bean | Produces a 3-dim fibre? | Verdict |
|---|---|---|---|---|
| 1 | Multi-fibre groupoid (T3b) | `qou-8p1i` | count of objects, not a fibre dim | **live, untested** — weakest content, cheapest to state |
| 2 | Bruhat / `GL_n(F_q)` realisation of `H_n(q)` | `qou-8p1h` | group natively; fibre via complex **3** of `PSL(2,7)` | **live, gated** on `qou-8p1j` |
| 3 | char-2 justification (gate for #2) | `qou-8p1j` | — | **the load-bearing unknown** |
| 4 | Octonionic `G_2` (status quo, direction 2) | — | yes, by import | **works, but unearned** — substrate bridge dead, `qou-8fl1` |
| 5 | Tetraplectic / quaternionic (Foth, Foth–Leitner) | `qou-8p1g` | supplies `SU(2)`, already spent on electroweak | **EXCLUDED scope-(b)** — and `m ≥ 2` does not rescue it |
| 6 | "4-form degenerates" -> `Spin(7)` -> `G_2` -> `SU(3)` | `qou-8p1f` | — | **EXCLUDED scope-(b)**, dimension count |
| 7 | `G_2 -> SU(3)` via `S^6 = G_2/SU(3)` | open-problem item 3 | yes, if `G_2` granted | **surviving form-stabilizer link** |

## The roast, route by route

**#1 multi-fibre groupoid.** It is a *name*, not a construction. Nobody has
exhibited the inequivalent fibre objects or shown their interaction space is
three-dimensional. It relocates "why is `dim V = 3`" to "why are there exactly
3 inequivalent fibres" — the same question wearing a hat. Its virtue is that it
is the only route that is both substrate-native and completely untouched by the
Klein exclusion.

**#2 Bruhat.** The strongest *idea*: `H_n(q)` IS the Iwahori–Hecke algebra of
`GL_n(F_q)` by origin, so this is the framework's own core object's defining
realisation, not an import. At `n = 3, q = 2` everything lands
(`21` flags, Fano `= PG(2,F_2)`, `Aut = GL(3,F_2) = PSL(2,7)`, order `168`).
Three things to be honest about: (a) **`q = 2` is the whole ballgame** — the
framework's `q` is a deformation parameter and `q_0` is a *locally observed,
varying* value; jumping to `q = 2` because it yields `168` is textbook
numerology absent a derivation, see `qou-8p1j`; (b) `F_2^3` is **not** a
`C`-fibre, so the fibre still comes from the complex **3** of `PSL(2,7)` —
rep theory you would have had anyway, which weakens the "native" claim;
(c) the Iwahori–Hecke algebra only sees the `B`-bi-invariant part, so
recovering the *group* needs the building, not just `H_3(q)`.

**#4 octonionic `G_2` (status quo).** It works and it is standard mathematics.
The problem is not correctness, it is provenance: `prop:color-su3-from-g2` has
an **empty `uses[]`** and there is no `def:octonion-algebra` in the corpus at
all. After the Klein exclusion this is the section's sole foundation, undefined
and unconstructed (`qou-8fl1`, and see the dependency audit).

**#5 tetraplectic.** In-corpus, owner's own paper, Lean-formalised sorry-free —
and it still does not get to `SU(3)`. Three problems, in increasing severity:
the Bring-cone instantiation is at `m = 1` where the tetraplectic condition is
*vacuous*; its output is `SU(2)`; and that `SU(2)` is already spent on
electroweak. Full detail in `qou-8p1g`.

**UPDATE 2026-08-24 — #5 is now EXCLUDED, not merely "as instantiated".**
`qou-8p1g` left one escape open: go to `m >= 2`, where the tetraplectic
condition has content, and ask whether the `S_3` permuting three quaternionic
lines of `Sp(3)/Sp(1)^3` yields `SU(3)`. It does not. Every Lie-algebra map
`su(3) -> su(2)^k` is zero (simplicity, not dimension — `dim su(2)^3 = 9 > 8`,
so the naive count permits an embedding and is the wrong tool), and `SU(3)` has
no nontrivial real representation below dimension 6, so nothing acts on a
single quaternionic line either. The "three" of the permutation is a
three-element **set** with a **finite** group on it; colour needs a
three-dimensional complex **vector space** with a **connected** one, and a
continuous map from a connected group to a finite one is constant. That is
this bean's own adjoint-vs-fundamental equivocation reappearing one level up.
`computations/quaternionic_flag_su3_exclusion.py`, 23/23.

**#6 "4-form degenerates".** Excluded, and cleanly — `qou-8p1f`. There is
nothing for the 4-form to degenerate *into*.

## Reading of the board

The two live routes are **#1 (native, weak)** and **#2 (strong, gated on
#3)**. If `qou-8p1j` fails to justify characteristic 2 on structural grounds,
#2 collapses into numerology and #1 is all that is left — at which point the
honest position is that colour is an **imported** symmetry and the corpus
should say so plainly.


---

# CORRECTION (2026-08-07, later the same day) — prior work found, gap re-stated

A corpus-grep for `T3b` turned up an **existing programme I had not seen** when
this epic was written: epic **`qou-8lxd`** ("eightfold way / SM derived from
QOU", todo, high priority, 2026-08-03), with `qou-dwsh` (T3b) and `qou-w5fw`
(T3f) both **completed as assessments**, plus five audit docs
(`2026-08-03-flavour-su3-schur-weyl-obstruction`,
`2026-08-04-distinct-fibre-groupoid-assessment`,
`2026-08-04-ocneanu-trace-parameter-audit`,
`2026-08-04-tannakian-gerbe-flavor-assessment`,
`2026-08-04-pgl3-higher-teichmuller-assessment`).

**This epic is a child of `qou-8lxd`, not a rival to it.**

## Correction 1 — the gap statement above is WRONG as written

This epic says: *"the single-fibre construction supplies `dim V = 2`; colour
needs a 3-dimensional fibre."* That conflates two objects the T3f audit
explicitly warns must not be conflated:

| Object | Governs | Constrained by |
|---|---|---|
| **fibre gauge group** `SU(2)`, `dim V = 2` | the braid rep `V^{tensor n}` | Descartes condition `chi(A) = -6` |
| **Ocneanu parameter** `a = q^{N-1}` | *which* `gl_N`-weighted invariant the Markov trace computes | **unknown — a separate DOF** |

So "we need a 3-dimensional fibre" is **not** the only way to reach `N = 3`.
Setting `a = q^2` gives a `gl_3`-weighted invariant **on the same tower at the
same `q`**, with no new fibre and no new construction. `HnMarkovTrace.lean`
types `z` as a free class **field** (only `z_pos`), while its docstring pins the
Jones value — exactly the T3f finding.

## Correction 2 — flavour and colour are different targets

`qou-dwsh` §2a is explicit: the octonionic `G_2` route gives **colour** `SU(3)`,
**not flavour**. This epic grew out of the Klein exclusion, which is a *colour*
route, but the gap statement above was written as if it covered both. It does
not.

* **Flavour `SU(3)`** (the eightfold multiplets, via Schur–Weyl at `N = 3`) —
  the Ocneanu route, `qou-w5fw` / T3f §2c, already flagged there as *"the most
  promising direction: it requires no new construction, only a separation of
  the `N = 2` mass channel from an `N = 3` flavour channel on the same Hecke
  tower."*
* **Colour `SU(3)` / `PSL(2,7)` / Fano** — what this epic's routes address.

## Correction 3 — re-ranking, and `qou-8p1j` is demoted

The Ocneanu route is a **better-formulated version of the instinct behind
`qou-8p1h`** (get `N = 3` from the Hecke tower itself) and it does **not need
characteristic 2 at all** — it needs `a = q^2` at the same `q`.

* `qou-8p1h` (Bruhat) — **subsumed for flavour.** Survives only for the
  distinct *colour* target `PSL(2,7) = GL(3,F_2)`, where the `q = 2` flag
  geometry is genuinely what is wanted.
* `qou-8p1j` (characteristic-2 gate) — **demoted.** Not needed for flavour
  `N = 3`. Relevant only to the colour target above, and therefore much lower
  priority than written.
* `qou-8p1i` (multi-fibre groupoid) — my roast stands and **matches the prior
  audit**: `qou-dwsh` says "No construction exists in the corpus", and its §2b
  asks exactly my questions (what forces exactly 3 fibre types? do the
  inter-fibre morphisms carry the right tensor structure? is the result
  non-self-dual?). Not a duplicate finding — an independent confirmation.

## The actual live blocker, already well-posed by T3f

Not "find a 3-dimensional fibre". It is:

> **Is `N = 2` forced, or is the Ocneanu parameter free?** The mass pipeline is
> structurally tied to `N = 2`: `dim V_{(2,1)}^{gl_2} = 2` but
> `dim V_{(2,1)}^{gl_3} = 8`, so `N = 3` changes the representation dimension
> and the operator structure, not merely the weights. T3f calls this a **soft
> constraint** — "not a theorem, but a structural compatibility".

T3f's own recommendation is the target: **a Lean proof that the mass pipeline
uniquely selects `N = 2`, or that `N = 3` is compatible.** Note the relevant
dimension formula is *already* formalised —
`RowCapObstruction.weylDimMixed N = 2 * (N+1).choose 3 = N(N^2-1)/3`, giving
2 at `N = 2` and 8 at `N = 3`.

That is where the next effort belongs, and it belongs under `qou-8lxd`.


---

## T3f RESOLVED in one direction (2026-08-07)

`ocneanu_N_lockin_probe.py`: the `N = 2` and `N = 3` Ocneanu traces on `H_3(q)`
are **not proportional** (`y_(2,1)/y_(3) = q[2][N-1]/[N+2]`), so the mass
pipeline **cannot** be re-tuned to `N = 3`. T3f's soft constraint is hard.

Consequence for this epic's board: the flavour channel **must** be a separate
trace on the same tower — which is permitted and already typeable
(`HnMarkovTrace.lean` has the parameter as a free class field). The remaining
flavour question is no longer "can we get N = 3" but "**why is the mass channel
the N = 2 one**", which is open and is the honest successor to T3f.

Colour routes are unaffected: still `qou-8p1h`/`qou-8p1j` (Bruhat, gated) and
the unearned octonionic status quo (`qou-8fl1`).


---

## T3f's "Unknown" RESOLVED for the mass channel (2026-08-07)

`computations/ocneanu_parameter_is_fibre_qdim.py`, exact arithmetic, all checks
pass.

T3f's §1 table records the Ocneanu parameter's constraint as **"Unknown"**, on
the grounds that "the Ocneanu trace is defined on `H_n(q)` **abstractly** — it
does not require a specific `V` to exist." That is right for the *abstract*
trace. **The mass pipeline does not use the abstract trace.**

`feynman-eigenbasis.md` defines the mass as the **categorical trace**, summed
"over the finitely many irreducible summands of `V^{tensor n}`", and quotes the
skein relation `q m(L+) - q^{-1} m(L-) = (q^{1/2}-q^{-1/2}) m(L0)` — HOMFLY at
`a = q`, i.e. `a = q^{N-1}` with `N = 2` already baked in.

**The identity that closes it** (dual Cauchy, at the principal specialisation):

    sum_{lambda |- n}  f^lambda * s_lambda(1, q, ..., q^{N-1})  =  [N]_q^n

verified for `n = 1..5`, `N = 2..4`, five rational `q`. The right side is the
categorical trace of the identity on `V^{tensor n}` when `dim_q V = [N]_q`. So
the total Ocneanu weight at parameter `N` **is** the categorical trace of an
`N`-dimensional fibre:

> **`N` is the quantum dimension of the fibre. Choosing `N` IS choosing `V`.**

Descartes fixes `dim V = 2`, hence `N = 2`, hence `a = q` — exactly the skein
the mass block quotes. Not a knob.

## And it collapses the board

An `N = 3` flavour channel cannot be the same trace re-tuned (excluded by
`ocneanu_N_lockin_probe.py`). By this identity it must be the categorical trace
on a **genuinely 3-dimensional object** — which is precisely the missing
3-dimensional fibre `qou-8p1x` identifies as the real gap.

**So the Ocneanu route does not avoid needing a 3-dim fibre; it restates the
need for one. The two open threads are one thread.**

NOT claimed: that the Descartes condition is derived (input here); that no
other trace could serve the mass pipeline (the claim is conditional on the
corpus's own definition of mass as a categorical trace); anything about colour.


---

## LIVE SURFACE COLLAPSED (2026-08-07) — see the synthesis audit

`docs/audits/2026-08-07-eightfold-live-surface-collapse.md`.

Three independent threads now terminate on the **same** requirement:
* the Sym^2-gate result — no summand of any `V^{tensor n}` passes, since all
  SU(2) reps are self-dual, so "inequivalent fibre objects" must mean genuinely
  non-isomorphic fibres;
* the Ocneanu result — an N = 3 channel must be the categorical trace on a
  genuinely 3-dimensional object, since the parameter is the fibre's quantum
  dimension;
* T3g's own question — does the braided category admit inequivalent fibre
  *functors* (a non-neutral Tannakian gerbe)?

**`qou-8p1i` (T3b) and `qou-y7vg` (T3g) are the same question.** Merge their
scope.

**And T3g's stand-down is VOID.** It deferred to the S₄/Fano route ("the Fano/S₄
route subsumes the structural content of this bean") — and that route was
excluded today, scope-(b). T3g is now the *surviving* direction, not the
subsumed one, and should be re-prioritised.


---

## SIZE/PARENTAGE ROAST on this very bean (2026-08-07)

Two failures of my own, recorded rather than quietly fixed:

1. **Parentage was inverted.** This session epic reached **12.5 KB** while
   `qou-8lxd` — the real epic it is a child of — is a **176-byte stub**. Now
   declared `parent: qou-8lxd`.
2. **Beans are not documents.** I appended findings to beans repeatedly instead
   of writing them once to an audit doc and pointing. The result: the beans that
   *closed* things are small (`qou-dwsh` 668 B, `qou-bldy` 723 B) and the open
   ones are bloated (this one 12.5 KB, `qou-8p1i` 5.9 KB, `qou-8p1e` 5.2 KB).
   Size is inversely correlated with usefulness across this whole set. The
   roast table above belongs on `qou-8lxd` or in an audit doc.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.



Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: routes to a 3-dimensional fibre / colour SU(3) — assessed and roasted


---

## 🛑 STALE CLAIM — `prop:color-su3-from-g2` does NOT have an empty `uses[]` (verified 2026-10-10)

This bean asserts the block carries no dependency edge. Measured on this branch at
`folio/.../braids-and-knots/color-su3-from-g2.ts:23`:

    uses: ["def:octonion-algebra"],

and the three comment lines immediately above it record the discharge explicitly:

    // def:octonion-algebra was authored 2026-08-29 (beans qou-7arp / qou-8fl1);
    // the NOTE that used to sit here, recording its absence, is discharged.
    // It sits immediately above this block in sec:color-algebra, so the edge
    // reads backward.

So the gap this bean names was **closed on 2026-08-29**. The same stale claim is
carried by `qou-8p1x`, `qou-8p1e` and `qou-8p1h`, i.e. three beans repeating one
fact that a fourth bean (`qou-8fl1`) had already fixed — the cross-bean staleness
pattern this front's epic (`qou-8lxd`) records: **read the beans a bean cites AND
the beans that cite it before working it.**

**A residual, and it is a different defect:** that comment says the edge *"reads
backward"* — `def:octonion-algebra` sits immediately above the block it is cited
from in `sec:color-algebra`. That is a forward-reference/ordering question for the
detangler arc, not an absent-edge question, and it is NOT what this bean claims.
Recorded, not filed: it changes a block's position, so it is an owner call.

Also verified: `qou-8p1x`'s route sub-beans **`qou-8p1i` and `qou-8p1j` are both
`scrapped`**, so any item here gated on either is gated on an abandoned route.
`qou-8p1h` in particular is blocked on nothing live.

Provenance: cross-session read-only pre-read of the 15 open `8f-colour` beans
(`/mnt/project-files/eightfold/8f-colour-preread.md`), confirmed on this branch at
`37bdbeef6b3` rather than taken on trust — the pre-read states its own path checks
were run partly against `main` at a different commit.

## Round 66 Update (PR #8239)
- Formalized in `WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.lean` and verified via 80-dps `mpmath` witness in PR #8239.
