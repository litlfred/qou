---
# qou-j377
title: 'SW-6 (=R2b): semisimplicity of H_n(q) at generic q (Tits deformation / ρ_λ separate points)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-09-03T08:44:21Z
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
