---
# qou-j377
title: 'SW-6 (=R2b): semisimplicity of H_n(q) at generic q (Tits deformation / ρ_λ separate points)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-09-03T15:05:35Z
parent: qou-59vq
blocked_by:
    - qou-u86i
    - qou-jfr8
---

H_n(q) is split semisimple for q generic (not a root of unity). Route: the ρ_λ separate points + dim count Σ d_λ²=n! ⇒ the map to ⊕M_{d_λ} is injective on a n!-dim algebra ⇒ iso. Or Tits deformation from K[S_n]. Uses SW-3. Ref: [wenzl1988], [kassel1995].

## Refine (recon): no Tits deformation in Mathlib. K[S_n] semisimple is free (Maschke `instIsSemisimpleRingAddMonoidAlgebra`). Generic-q transfer must be hand-done (discriminant / Gram-determinant nonvanishing of the bilinear form). Substantial.

## ⏩ Concrete Burnside-surjectivity half PROVED (2026-08-10) — sorry-free

[`QOU/SchurWeyl/BurnsideSpan.lean`](https://github.com/litlfred/qou/blob/claude/schur-weyl-sw5-irreducibility-2026-08-10/content/quantum-observable-universe/lean/QOU/SchurWeyl/BurnsideSpan.lean):
`seminormal21_no_linear_relation` (q≠0) — `{1, S0, S1, S0·S1}` admit no nontrivial
linear relation over ℝ ⇒ linearly independent ⇒ (dim M₂=4) span M₂(ℝ) ⇒ the (2,1)
seminormal rep is SURJECTIVE onto M₂(ℝ) (Burnside). Entry-computation proof, no
density theorem. Axiom-clean; lean-direct exit 0; wired into QOU.lean; on PR #4942.

**Still open for full SW-6 (semisimplicity of H_3(q)):** needs `dim H_3(q) = 6`
(the Iwahori–Hecke basis theorem {T_w : w∈S_3}) to turn the surjective block maps
(two 1-dim reps + this M₂ factor, 1+1+4=6) into the iso H_3(q) ≅ ℝ×ℝ×M₂. That
basis/dimension theorem is the real blocker → feeds SW-7 (qou-0h5k); tracking it here.


## Measured 2026-08-19 — blocked, and the blocker is now SW-5 not the reps

State on main: `BurnsideSpan.seminormal21_no_linear_relation` (concrete (2,1),
sorry-free) is the only content. General semisimplicity needs the rho_lambda to be
irreducible and pairwise inequivalent (SW-5, `qou-jfr8`) plus the dimension
anchor sum d_lambda^2 = n! (SW-3, `qou-wtny`). Both are now the live blockers;
the representations themselves are no longer missing (#5279).

Route note kept: no Tits deformation in Mathlib; generic-q transfer from k[S_n]
would have to be hand-done via Gram-determinant nonvanishing. The
separate-points route through SW-5 is the cheaper one now that Ram 4.1 (#5290)
supplies the diagonalisation.


## 2026-09-03 — the blocker list above is STALE, and the real open half is named

The 2026-08-19 note says SW-5 (`qou-jfr8`) and SW-3 (`qou-wtny`) are "the live
blockers".  **Both landed.**  `QOU.SchurWeyl.heckeWedderburn` (SW-7) and
`sum_dLambda_sq` are on `main`; I built against them this session and used the
Wedderburn iso to transport `IsSemisimpleRing` to the `T_w` carrier
(`QOU/SchurWeyl/HeckeCarrierEquiv.lean`, PR #6437).  So `H_n(q)` **is** proved
split semisimple at every rank — **over `ℝ`**.

This bean's own headline says *"for `q` generic (not a root of unity)"*, and that
phrasing turns out to be exactly the open half: the corpus has the theorem over
`ℝ` and the general field is what remains.

### Why it is `ℝ`, measured rather than assumed

On `heckeWedderburn`'s **103-module in-repo import cone**:

* **`Real.sqrt` does not occur in it at all.**  The seminormal form as built here
  needs no square roots — so the usual reason a Hoefsmit construction wants `ℝ`
  is not the reason here.  I expected to find it and did not.
* **Exactly two modules** use anything `Real.*` in code — `SeminormalRep` and
  `SeminormalInequivalence` — and both use only the **`Real.log` family**, in one
  idiom.

That idiom is `SeminormalRep.zpow_ne_one : q ≠ 0 → q² ≠ 1 → ∀ m ≠ 0, qᵐ ≠ 1`,
whose own docstring already says it is *sharp over `ℝ`*.  So **over `ℝ` the
two-line hypothesis IS "q is not a root of unity"**, and over a general field it
is not — a primitive cube root of unity satisfies both hypotheses and has
`q³ = 1`.

**The `ℝ` is load-bearing, but only as a cheap proof of one hypothesis.**  The
generalisation is therefore not "swap `ℝ` for `K`"; it is "carry the classical
criterion this bean already names".

### Landed toward it

`QOU/SchurWeyl/GenericParameter.lean` (sorry-free, axioms clean) — the hypothesis
over an arbitrary field plus the two consequences the two `Real.log` proofs
actually extract, and the bridge showing the `ℝ` form implies it:

    NotRootOfUnity q          ∀ m > 0, qᵐ ≠ 1
    pow_left_injective        the powers of q are pairwise distinct
    zpow_ne_one               no nonzero INTEGER power is 1
    poly_eq_zero_of_eval_pow  a polynomial vanishing at every qᵐ is zero
    ofSqNeOne                 over ℝ, q ≠ 0 ∧ q² ≠ 1 give it

`ofSqNeOne` is what makes this a **weakening**: every `ℝ` statement in the cone is
the specialisation of a `NotRootOfUnity` statement, so generalising those files
strengthens no hypothesis and invalidates no downstream use.

`zpow_ne_one` here needs **no** `q ≠ 0` — `0ᵐ ≠ 1` either way.  The `ℝ` original
carries it only because `Real.log` does.

### Cost of the remaining tranche, measured

**13 files, 248 occurrences of `ℝ`** in the cone, led by `QJucysMurphyEigen` (49),
`SeminormalInequivalence` (40), `SeminormalRep` (30), `HoefsmitRep` (26),
`HeckeWedderburnGeneral` (26).  A tranche, not a step — which is why only the
must-exist part landed.  Route note kept: still no Tits deformation in Mathlib,
but the separate-points route no longer needs one.


## 2026-09-03 — the `Real.*` surface in the cone is now ZERO (PR #6486)

`GenericParameter` (landed in #6437) is now applied at both sites, so the two `Real.log`
idioms are gone:

    SeminormalRep.zpow_ne_one                        Real.log_zpow  ->  GenericParameter.zpow_ne_one
                                                                       (GenericParameter.ofSqNeOne hq0 hq2)
    SeminormalInequivalence
      .pow_right_injective_of_pos_of_ne_one          Real.log_pow   ->  GenericParameter.pow_left_injective

**Measured on the 105-module cone, comments AND import lines stripped: `Real.*` function
uses = 0.**  Strip the import lines or you measure your own `import Mathlib.Data.Real.Basic`
as a use — it reports 1 otherwise, and that 1 is a path, not a call.

### What this bought, and what it did not

Both sites **fused two claims that are not the same claim**: *"`q ≠ 0 ∧ q² ≠ 1` implies `q`
is not a root of unity"* (TRUE over `ℝ`, FALSE over a general field — the only place `ℝ`
does real work here) and *"not a root of unity implies no nonzero power is `1`"* (true over
any field).  `Real.log` proved the conjunction in one step, so the `ℝ`-specific half was
invisible, buried in a log identity three files below the theorem that needs it.  It is now
`GenericParameter.ofSqNeOne` — named, one lemma, in a file whose name says archimedean.

**This does NOT make anything general-field.**  It removes the disguise, not the
restriction.  `heckeWedderburn` is still `ℝ`-only and its statement is unchanged.

**No signature changed**, deliberately: `zpow_ne_one` keeps `{q : ℝ} (hq0) (hq2)`, so all
~40 call sites are untouched.  The point of this step is to make the next one mechanical.

### The remaining obstacle is ORDER, and it is a different (smaller) number

Still `ℝ`: **14 files, 244 occurrences** (was 13/248 — the extra file is
`GenericParameterReal`).  Every one is now a base ring with no `Real` function applied.
What is left is (a) threading `NotRootOfUnity` in place of `q ≠ 0 ∧ q² ≠ 1`, and (b) the
order uses, measured separately as **24** (`linarith` / `nlinarith` / `positivity` / `abs` /
`sq_nonneg`) across **9** files:

    5  OffDiagNonvanishing      5  SeminormalInequivalence   5  SeminormalParam
    3  CauchyBinet              2  QJucysMurphyEigen         1  JucysMurphy
    1  SpechtStandardBasisCore  1  HoefsmitRep               1  SeminormalRep

Those work over any **ordered** field, so they are a weaker obstacle than `ℝ` — but they are
not zero, and `[LinearOrderedField K]` is not `[Field K]`.  Do not report the cone as
"general-field ready" on the strength of the `Real.* = 0` figure alone.

### Also landed: a §7c split that predates this work

`check-sidecars.sh` flagged `SeminormalInequivalence` MIXED once my edit put it in the
changed-file set.  **I did not cause it** — the checker's own `GEN` regex gives identical
hits on `main`'s version and mine, both at `def MatRepEquiv {R A ι κ : Type*} [CommRing R]`.
66 generic lines moved to `QOU/SchurWeyl/MatRepEquiv.lean`; **zero** consumers outside the
original file, 16 inside, namespace unchanged.  It also helps this tranche: a block that
never needed `ℝ` was sitting in the file with the largest `ℝ` surface in the cone (39).

### Chain scoping, for whoever takes the tranche

All 13 files are genuinely on the chain — each is referenced by something downstream,
ending at `HeckeWedderburnGeneral`.  Nothing is incidental, so the tranche cannot be
shortened by dropping a file.  Dependency order (deps within the set, then `ℝ` count):

    0  HoefsmitRep 26 | 1  QJucysMurphy 6, SeminormalParam 13 | 2  SeminormalRep 26
    3  HoefsmitRepGeneral 14, OffDiagNonvanishing 5 | 5  QJucysMurphyEigen 49
    6  SeminormalInequivalence 39, SeminormalSimpleSpectrum 7 | 7  SeminormalRange 13
    9  SeminormalRangeTop 7 | 11 HeckeProductSurjective 12 | 12 HeckeWedderburnGeneral 26

One measurement NOT to repeat: I checked whether `HoefsmitRep`'s `ℝ` block is a free island
by grepping its declaration names corpus-wide.  `S0` and `S1` reported 17 and 13 users —
**meaningless**, they are two-character names and the grep cannot tell this file's `S0` from
any other file's.  The reliable signal is `seminormalRep21`, used by 4 files including
`QJucysMurphy`, which IS in the chain.  So `HoefsmitRep` is not free.


## 2026-09-03 — the tranche does NOT need an ordered field (formalize-first prune)

The `Real.* = 0` result above left an open question I flagged rather than answered: the
cone still has **24 order uses** across 9 files, and `[LinearOrderedField K]` is not
`[Field K]`.  If even one were essential, the migration would land on an ordered field and
most of its value would be gone.

Read all 24 before spending the refactor.  **The recurring hard one is a single
statement:**

    (q ^ 2 + 1) ≠ 0

- `HoefsmitRep.sq_add_one_ne` — `by positivity`.
- `SeminormalParam` twice: inside `hne4 : 1 - q^4 ≠ 0`, which case-splits
  `(q²−1)(q²+1) = 0` and kills the second branch with `nlinarith [sq_nonneg q]`; and inside
  `hden : q³ + q ≠ 0`, which factors to `q·(q²+1)` and closes with `positivity`.

Over a general field the statement is **false** — a primitive fourth root of unity has
`q² + 1 = 0` — so it reads as a second, independent obstruction to leaving `ℝ`.

**It is not.**  `q² + 1 = 0` forces `q⁴ = 1`, which `NotRootOfUnity` already forbids.  The
one hypothesis introduced for the `Real.log` sites covers the order sites too.  Proved
rather than argued: `GenericParameter.sq_add_one_ne_zero` over any field, plus `ne_one` and
`sq_ne_one` for the call-site shapes.

**In one place the hypothesis does better than replace the argument — it deletes it.**
Under `NotRootOfUnity`, `1 - q⁴ ≠ 0` is immediate from `hq 4`; the case split and both
`nlinarith` calls go away.

### The conclusion, and how far it is verified

**The tranche needs `[Field K]` + `NotRootOfUnity`, not `[LinearOrderedField K]`.**

Scope that honestly: the two `SeminormalParam` sites are **verified against the source**,
because the conclusion turns on them.  The other 22 I classified **by inspection** as
convenience tactics over linear/ring facts — `sub_ne_zero` shapes (`A ≠ 1 → 1 - A ≠ 0`), a
cast equality, a `zpow` identity, and `0 < q²` feeding the old
`pow_right_injective_of_pos_of_ne_one` signature, which the generic lemma has already
displaced.  That is a reading, not a machine check; a site that resists is a finding, not a
refutation of this note.

### Proof note worth keeping

`sq_add_one_ne_zero` keeps `GenericParameter`'s single Mathlib import:
`q⁴ = (q²+1)(q²−1) + 1` by `ring`, then rewrite by the hypothesis.  The obvious
`linear_combination` route **fails here as "unknown tactic"** — `Mathlib.Tactic.LinearCombination`
is not imported and deliberately should not be, to keep this file's cone minimal.


## 2026-09-03 — CORRECTION to my own entry above: the tranche is 11 modules / 59 declarations, not 13 files

The entry two sections up says *"all 13 files are genuinely on the chain — each is
referenced by something downstream, ending at `HeckeWedderburnGeneral`.  Nothing is
incidental, so the tranche cannot be shortened by dropping a file."*  **That is wrong, and
the reason is the same coarse-detector error this bean already documents twice.**

It was measured at **file** level — does module A reference any declaration of module B.
Re-measured at **declaration** level, walking references from `heckeWedderburn` itself
(`scripts/lean-general-field-tranche-scope.py`):

     ℝ-decls  reachable  module
          19         12  QJucysMurphyEigen
          16         10  SeminormalRep
          14          9  SeminormalInequivalence
          12          0  HoefsmitRep            <-- OFF the general path
           6          6  HeckeWedderburnGeneral
           6          5  SeminormalParam
           6          6  HeckeProductSurjective
           3          3  SeminormalSimpleSpectrum / SeminormalRangeTop / SeminormalRange
           1          1  OffDiagNonvanishing
           1          0  QJucysMurphy           <-- OFF the general path
           1          0  HoefsmitRepGeneral     <-- OFF the general path
           1          1  GenericParameterReal

**TRANCHE: 59 ℝ-carrying declarations across 11 modules**, of 92 across 14 in the cone.

### Why `HoefsmitRep` is off the path

Its `ℝ` block is the concrete `S0` / `S1` / `seminormalRep21` / `seminormalRep22`
development.  It reaches the chain through exactly one bridge —
`QJucysMurphy.qJM_seminormalRep21_one`, a rank-2 sanity check on the q-Jucys–Murphy element
— and **that theorem has zero consumers corpus-wide**.  `seminormalRep21`'s other four
users (`HeckeWedderburn3`, `HeckeDim3Indep`, `HeckeMarkov3`, and the dead lemma) are **not
in `heckeWedderburn`'s cone at all**; they are the separate concrete rank-3 development.
`QJucysMurphy` carries exactly one `ℝ` declaration — that same dead lemma — so it comes off
the tranche entirely too.

### And "244 occurrences" was the wrong unit

`ℝ` is a character.  A theorem mentioning it six times is one declaration of work.  Quote
**59 declarations across 11 modules**; do not quote 244.

### The check that makes the OFF verdict safe

Reachability here is **name-based** and excludes names of ≤ 3 characters, because a bare
`S0` matches too much prose to follow.  That is precisely how a file gets *wrongly* called
off-path — the closure cannot see the very names `HoefsmitRep` exports.  So the script
carries `--check-short`, which asks directly whether any **reachable** body mentions `S0`
or `S1`.  Answer: **NONE**.  Run it before believing any OFF verdict.

Recorded because the earlier over-count and this correction come from the same place: a
detector one granularity too coarse, trusted because it was specific.


## 2026-09-03 — first tranche file done, and the remaining threading is now sized

**`SeminormalParam` is generic, and it needed NO new hypothesis.**  Its five declarations
on the general path moved to `{K : Type*} [Field K]` carrying the *same* `q ≠ 0`,
`q ^ 2 ≠ 1` they already had.  No `NotRootOfUnity` threading, no order, no proof changed —
`sub_ne_zero` + `field_simp` + `ring` never needed `ℝ`.  **The `ℝ` in that file was not
load-bearing at all; it was inherited from a `variable (q : ℝ)` line.**

Its sixth declaration `S1_eq_seminormalParam` genuinely cannot be generic (it identifies
`HoefsmitRep`'s `ℝ`-valued `S1`, and proves `1 - q⁴ ≠ 0` via `nlinarith [sq_nonneg q]`), so
per §7c it moved to `SeminormalParamAnchorReal.lean`.  It is **off the general path**
anyway.  Tranche: **59 → 54 declarations, 11 → 10 modules.**

### How NOT to do this edit

My first attempt blanket-replaced `(1 : ℝ) → (1 : K)` across the file.  It hit the private
helper `add_inv_aux`, whose binders are separate, and it inserted the section boundary
*between a docstring and its theorem* (`unexpected token 'end'; expected 'lemma'`).
Reverted; redone with explicit line anchors plus an assertion that no `ℝ` survives in the
generic section.

### The remaining threading, measured

`SeminormalRep` is next in dependency order and is where the real work is — not because of
`ℝ` in its types (those are base-ring shaped) but because `zpow_ne_one` is consumed **36
times inside it**, each as `zpow_ne_one hq0 hq2`, and generalising means those become
`NotRootOfUnity`.

    module                        decls  sig-hq2  zpow sites
    SeminormalRep                    40       15          36
    OffDiagNonvanishing               2        2           3
    QJucysMurphyEigen                21        8           1
    SeminormalSimpleSpectrum          3        3           1
    SeminormalInequivalence          26        7           0
    SeminormalRange                   3        3           0
    SeminormalRangeTop                3        3           0
    HeckeProductSurjective            7        6           0
    HeckeWedderburnGeneral            7        3           0

**THREADING: 50 signatures carrying `q ^ 2 ≠ 1`, 41 `zpow_ne_one` call sites, over 112
declarations.**  Mechanical, bounded, but not a single sitting — `SeminormalRep` alone is
1810 lines with a >2-minute build loop.

**Do not quote a "0 signatures" figure.**  My first attempt at this measurement reported
exactly that, from a regex that took everything between the declaration name and the first
`:` as the binder list — and every binder contains a `:`.  The corrected version splits the
declaration at `:=` and searches the header.

### Order of attack, if resuming

`OffDiagNonvanishing` cannot go before `SeminormalRep`: it consumes `offDiag`, which is
defined there.  So the order is `SeminormalRep` → `OffDiagNonvanishing` /
`QJucysMurphyEigen` → the three `Seminormal*` leaves → `HeckeProductSurjective` →
`HeckeWedderburnGeneral`.


## 2026-09-03 — TRANCHE COMPLETE: `heckeWedderburn` is general-field, 0 `ℝ` on the path

    isSemisimpleRing_hecke_generic {K} [Field K] [CharZero K] (q : K)
        (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
      IsSemisimpleRing (Hecke K q q⁻¹ n)

`scripts/lean-general-field-tranche-scope.py` reports **`TRANCHE: 0 ℝ-carrying
declarations across 0 modules`** — from 54/10 at the start of this arc.

Nine modules retyped in the forced order: `SeminormalRep` → `OffDiagNonvanishing` /
`QJucysMurphyEigen` → `SeminormalSimpleSpectrum` / `SeminormalRange` /
`SeminormalRangeTop` → `SeminormalInequivalence` → `HeckeProductSurjective` →
`HeckeWedderburnGeneral`.

### The design choice that made 41 call sites into 5

**`zpow_ne_one` keeps its hypothesis NAMED `hq2` while its TYPE moves** from `q ^ 2 ≠ 1`
to `NotRootOfUnity q`.  So `zpow_ne_one hq0 hq2` → `zpow_ne_one hq2` mechanically (the
`hq0` is genuinely unnecessary — `0 ^ m ≠ 1` either way), and the `seminormalParam_*`
lemmas, which still want `q ^ 2 ≠ 1`, take `GenericParameter.sq_ne_one hq2`.

### TWO CHARACTERISTIC HYPOTHESES — the only places this was not a retyping

1. **`barSymJMSum_block_eigenvalue_zero_false` needs `(2 : K) ≠ 0`.**  Over `ℝ` the
   contradiction is `1 + 1 = 0` in the block algebra, closed by `simp` on a diagonal
   entry.  In characteristic two that equation **holds**, so the statement is **false**
   there.
2. **The power-sum cone needs `[CharZero K]`** (7 signatures, from
   `contentCount_eq_of_contentPowSum_eq`).  `exact_mod_cast` on `(card : K) = (card : K)`
   is valid only in characteristic zero.  *"Equal power sums force equal exponent
   multisets"* is a characteristic-zero fact and now says so.

Both are recorded at the declaration, not only in the commit.

### The complete list of proof repairs, across ~3300 lines

One `linarith` → `linear_combination` (`SeminormalRep`); three `sub_ne_zero` shapes
(`OffDiagNonvanishing`); one `simp only [seminormalGen]` → `unfold` (the extra universe
from `K` broke the equation lemma); one `rfl` → `norm_cast`; two explicit `(K := K)`
where `finrank` could not infer it.  **That is all of it** — confirming what
`SeminormalParam` suggested: most of the `ℝ` was inherited from `variable` lines.

### Added

`GenericParameter.pow_notRootOfUnity` — a positive power of a non-root-of-unity is one;
needed wherever the development passes to `q ^ 2`.

### §7c splits

`HeckeSemisimpleReal.lean` (the substrate-shaped `isSemisimpleRing_hecke` + the three
`1 < q` forms) and `SeminormalParamAnchorReal.lean`.  The `ℝ` corollary is **derived**
from the generic theorem via `ofSqNeOne`, so nothing downstream changed shape.
`isSemisimpleRing_blocks` and `coshSum_transpose` turned out to need no work at all —
`inferInstance` and a zpow identity respectively.

### NOT done — do not over-read this

`isSemisimpleRing_iwahoriHecke` (the `T_w` / `twGram` carrier) is **still `ℝ`**: it uses
`Real.sqrt` to name the `q` with `q ^ 2 = Q`.  That is a separate, smaller step, not part
of this tranche.

Verified after rebasing onto main (78 commits): `lean`-direct exit 0 on all 15 modules;
`#print axioms` unchanged; `check-sidecars` zero action lines.


## 2026-09-03 — the arc is closed: the Iwahori carrier is general-field too (PR #6517)

#6486 merged (`c491117b54`) with one `ℝ` named as outstanding —
`isSemisimpleRing_iwahoriHecke`, the `T_w` / `twGram` carrier, which used `Real.sqrt` to
name the `q` with `q² = Q`.  Closed:

    isSemisimpleRing_iwahoriHecke_sq {K} [Field K] [CharZero K] (q : K)
        (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
      IsSemisimpleRing (QOU.Hecke.IwahoriHecke K (q ^ 2) n)

    isSemisimpleRing_iwahoriHecke_of_sq   -- the same at Q, given Q = q ^ 2

### The finding, which is a narrowing rather than a weakness

**The general statement has to be parameterised by the square root.**
`skeinIwahoriEquiv` relates the skein algebra at `q` to the Iwahori algebra at `q²`.  Over
`ℝ` the caller produces its own `q` as `Real.sqrt Q`, because every `Q > 1` is a square.
A general field cannot — `ℚ` has no `√2` — so the honest general form takes the root as the
parameter: *"the Iwahori algebra at a square is semisimple"*.

**So the whole residue of the `ℝ` on this arc was the EXISTENCE OF A SQUARE ROOT, never any
algebra.**  Worth recording because #6486's scope note ("still `ℝ`") invited the reading
that something mathematical was missing here, and nothing was.

### The `ℝ` theorem now derives from the generic one

It exhibits `Real.sqrt Q`, gets `NotRootOfUnity` from `GenericParameter.ofSqNeOne`, and
calls `isSemisimpleRing_iwahoriHecke_of_sq`.  The `ℝ`-specific content of that proof is now
**exactly one step — naming the root** — instead of being tangled with the transport.

### Mechanics

Generic result in a new file per §7c (`QOU/SchurWeyl/HeckeCarrierSemisimple.lean`), leaving
`HeckeCarrierSemisimpleReal.lean` as the archimedean specialisation.  **No import cycle** —
verified that `HeckeCarrierEquiv` is not in `HeckeSemisimpleGeneral`'s cone before adding
the import, rather than assuming it.

`lean`-direct exit 0 on both; axioms `[propext, Classical.choice, Quot.sound]` on all three;
check-sidecars 0 action lines.

### What is left on qou-j377

Nothing on the semisimplicity arc.  `qou-kwoa`'s last item — `det(twGram)` at rank ≥ 2 — is
untouched and unaffected: it is still Mathlib-scale and now wanted only for the determinant
**value**, since #6437 took semisimplicity off its critical path.
