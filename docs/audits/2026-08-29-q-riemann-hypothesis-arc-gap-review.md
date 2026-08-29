# The q-Riemann-hypothesis arc: what is proved, what is assumed, what is open

**Date:** 2026-08-29
**Scope:** `content/quantum-observable-universe/q-geometric-langlands/` (52 blocks)
plus the zeta/adelic blocks of `stochastic-mechanics/`.
**Method:** every `.lean` in the cone read and compiled `lean`-direct against the
restored `lake-cache/qou-v4-24-0` oleans; `#print axioms` on the load-bearing
declarations; corpus-grep checklist (all six paths) before anything is called open.

## Summary

The arc's spine is four steps:

```
local q-zeta of Bring's curve  ->  Hasse-Weil bound |alpha_i| = q^{1/2}
   ->  spectral half-line Re(rho_i) = 1/2 at each place
   ->  [adelic assembly]  ->  classical RH
```

Step 2 is now a clean conditional theorem. Step 3 is genuinely proved and is the
best-formalised thing in the chapter. **Step 4 has no carrier at all**, and it is
the whole distance between what the arc proves and what it is aiming at.

## What is actually proved

| declaration | status |
|---|---|
| `spectral_half_line` | **proved**, sorry-free, `#print axioms` clean. Given the spectral coordinate map and the Hasse-Weil bound, `Re(rho_i) = 1/2`. The one genuinely derived theorem of the arc. |
| `eigenvalue_norm_sq` | **proved**. The step turning Castelnuovo-Severi's `<=` into `=`, via the functional-equation partner. `nlinarith`, no axioms. |
| `abs_cpow_ofReal_eq_rpow_re` | **proved**. `|q^rho| = q^{Re rho}` for real `q > 0`. Real content, cleanly done. |
| `hasse_weil_bound` | **proved conditionally** on `[IsWeilZeta Z]` as of this review — see below. |

That is a real result and it should be said plainly: *conditional on the two
classical Weil inputs and on a spectral coordinate map, the framework derives the
critical-line property at each local place.* The derivation is not circular and
not fitted.

## What was inconsistent (fixed here)

Two axioms in `hasse-weil-bound.lean`, each universally quantified over an
arbitrary `LocalQZetaFunction`, **each proved `False`**. `LocalQZetaFunction`
records the *shape* of a zeta function and never that the shape comes from a
curve; `q := 1, alpha_i := 2` refutes Castelnuovo-Severi and `q := 4, alpha_i := 1`
refutes the functional equation. Machine-checked, `#print axioms` clean on each
`False`. Fixed by the §3b-cond route: the two inputs are now fields of
`class IsWeilZeta`, with `weilZetaExample` witnessing that the class is inhabited.
Full record: bean `qou-hwax`.

**The generalisable lesson.** `qou-rhax` was `forall a b, P a <-> Q b` with `P` not
constant in `a`. This is its sibling: *an external theorem asserted for every
inhabitant of a structure that does not carry the theorem's hypotheses.* Both are
instances of one failure — a citation making an over-quantified axiom look
load-bearing rather than arbitrary. Worth a detector: any
`axiom : forall (S : SomeStructure), <classical theorem about S>` where
`SomeStructure` is a shape record.

## The remaining gaps, ranked by what they cost

### 1. `thm:explicit-formula` is assumed, not derived — and the citation does not cover it

`explicit_formula_axiom` asserts the entire identity

```
psi_q(X) = X - sum_{rho} X^rho/[rho]_q - ln_q(2 pi Omega_q) - (1/2) ln_q(1 - X^{-2})
```

and `theorem explicit_formula` is its projection. Nothing is derived. It is
captioned *"External theorem (Rosen 2002 Ch 5 Thm 5.12; Weil 1948;
Reshetikhin-Turaev 1991)"*, but the **q-deformed** explicit formula — with
`[rho]_q`, `ln_q`, and the `Omega_q` term — is the framework's own claim, not
Rosen's or Weil's. This is the caption-provenance defect `qou-rhax` named, in a
milder form: the axiom is not inconsistent, but its attribution overstates what
the literature supplies.

`qLog_tendsto_log_axiom` in the same file is a second assumed analytic fact,
honestly cited to `[manuscript]`.

Corpus-grep run on "explicit formula": 7 audit hits (all mass-theory or the rhax
audit), 6 `computations/` hits (lambda-scale, h4 drivers, figure-eight), 3
`library/INDEX.md` hits (Reidemeister torsion, holonomy R-matrix, Ohtsuki), 5
beans. **None derives it.** The item is open.

### 2. The spectral coordinate map has no carrier

`spectral_half_line` takes `spectral_coord : forall i, alpha_i = q^{rho_i}` as a
hypothesis. Nothing in the corpus constructs that map or shows the `rho_i` are the
Reeb spectrum. Without it the corollary is a statement about *some* complex
exponents, not about the Reeb derivation. This is the cheapest real gap in the arc.

### 3. Adelic assembly — the keystone, and it is not carried anywhere

`classical-riemann-hypothesis.md` states the whole local-to-global step in one
sentence of prose: *"The Riemann hypothesis asserts that this alignment survives
the adelic assembly into the global zeta function."* There is **no** block, no
conjecture, no Lean carrier for it.

Note what is *not* the gap: `stochastic-mechanics/` does carry adelic
infrastructure — `prop:adelic-reeb-restricted-product` (sorry-free),
`def:adelic-substrate`, `rem:adelic-tate-squeeze`,
`rem:classical-limit-adelic-assembly`. But the last is a remark `interprets:
def:classical-limit-functor`, about the archimedean projection of a motivic
realization tower; it says nothing about critical-line persistence. Corpus-grep on
"adelic assembly" and "critical line": zero hits across audits, coordination,
computations and library.

So the honest statement is: *the arc proves a local critical-line property and
asserts, without a carrier, that it globalises.* Since Hasse-Weil holds at every
place unconditionally for curves and RH is nonetheless open, the assembly step is
carrying the entire difficulty. Naming it is the first work.

### 4. Eight open conjectures in the chapter

`conj:q-geometric-langlands`, `conj:q-gl-fiber-functor`, `conj:q-gl-classical-limit`,
`conj:q-gl-kummer-filtration`, `conj:q-oper-hecke` (no Lean carrier);
`conj:quantum-langlands-dual`, `conj:mirror-3d-3d-correspondence`,
`conj:modular-s-transform-q-q-tilde` (content-bearing class carriers, sorry =
conjecture per §3b). `thm:tannaka-krein-isomorphism` carries a `sorry` and two
`axiom`-declared types.

These are Langlands-side, not RH-side: none of them is on the four-step spine
above. They are open in the ordinary sense of being hard open problems, and are
not what is blocking the RH arc.

## What can be chipped away, in order

1. **Give the spectral coordinate map a carrier.** Small, well-defined, and it
   converts `spectral_half_line` from a statement about arbitrary exponents into a
   statement about the Reeb spectrum. Either a definition block constructing
   `rho_i := log_q(alpha_i)` with a branch choice, or a hypothesis class in the
   `IsWeilZeta` style making the assumption explicit and named. The branch choice
   is the real content: `alpha_i = q^{rho_i}` fixes `rho_i` only mod `2 pi i / log q`,
   so `Re(rho_i) = 1/2` is well-defined but the map is not — worth stating.
2. **Split `explicit_formula_axiom` into what the literature gives and what the
   framework claims.** The classical explicit formula for a curve over `F_q` *is*
   Rosen Thm 5.12 and can be cited honestly; the q-deformation of it cannot. Two
   axioms with accurate captions beat one with a caption that overreaches. Same
   disposition the rhax bean required.
3. **Open a block for the assembly step.** Even a `conjecture` block stating
   local-critical-line-at-every-place `=>` classical RH would put the arc's actual
   claim where it can be read and attacked, instead of in a subordinate clause.
   Per §3b it may carry a `sorry`; per §3b-tax it is a *primary* conjecture.
4. **Write the over-quantified-axiom detector.** Two instances found in eight days
   (`qou-rhax`, `qou-hwax`), both in the same chapter cluster, both caught by
   reading rather than by any checker. The shape is mechanically recognisable.

## Verification

`lean`-direct, `LEAN_PATH` over restored `lake-cache/qou-v4-24-0` oleans,
toolchain `lean-v4.24.0`:

- `QOU/AlgebraicSubstrate/LocalQZetaFunction.lean` compiled to olean, exit 0.
- `hasse-weil-bound.lean`, `spectral-half-line.lean`, `explicit-formula.lean` —
  exit 0 (one unused-variable linter warning in the third).
- Both `False` derivations from the old axioms: exit 0, `#print axioms` reporting
  each axiom alone plus Lean's three.
- Post-fix `#print axioms` on `hasse_weil_bound`, `eigenvalue_norm_sq` and the
  `IsWeilZeta` instance: `[propext, Classical.choice, Quot.sound]`.
- Non-vacuity: `example : ||weilZetaExample.eigenvalues 0|| = 2` proved through
  `hasse_weil_bound`.

CI auto-triggers are disabled repo-wide (owner directive 2026-06-30), so the above
is the verification gate, not a supplement to one.
