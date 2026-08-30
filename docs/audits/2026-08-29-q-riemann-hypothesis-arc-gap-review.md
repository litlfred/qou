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

**Four axioms across two files of this arc proved `False`** — two in
`hasse-weil-bound.lean` (`qou-hwax`) and two in `explicit-formula.lean`
(`qou-qexf`, §1 below). With the two already fixed in
`macroscopic-stability-equivalence.lean` (`qou-rhax`, 2026-08-22), that is six
in this arc's recorded history. Every one was found by reading, none by a
checker.

Two axioms in `hasse-weil-bound.lean`, each universally quantified over an
arbitrary `LocalQZetaFunction`, **each proved `False`**. `LocalQZetaFunction`
records the *shape* of a zeta function and never that the shape comes from a
curve; `q := 1, alpha_i := 2` refutes Castelnuovo-Severi and `q := 4, alpha_i := 1`
refutes the functional equation. Machine-checked, `#print axioms` clean on each
`False`. Fixed by the §3b-cond route: the two inputs are now fields of
`class IsWeilZeta`, with `weilZetaExample` witnessing that the class is inhabited.
Full record: bean `qou-hwax`.

**The generalisable lesson, now with three instances.** All three are one shape:
*a claim asserted for every inhabitant of a domain wider than the claim's
subject.*

| instance | the over-wide domain |
|---|---|
| `qou-rhax` | `forall a b, P a <-> Q b` with `P` not constant in `a` |
| `qou-hwax` | a structure that does not carry the theorem's hypotheses |
| `qou-qexf` | two lists quantified independently that must be one geometry's two faces |

The common aggravator is a citation: each made an over-quantified axiom look
load-bearing rather than arbitrary. Worth a detector — the shape is mechanically
recognisable, and a cheap first pass is to construct the smallest inhabitant of
the quantified domain (an empty list, a constant family, a degenerate structure)
and evaluate the claim on it. All four `False` derivations here were found that
way in minutes.

### A fourth instance of the shape, from a sibling — and two lessons off it

Reported on this PR by the q-NS sibling session and **verified here against
`origin/main` rather than taken on trust**: `HasQPlancherelCLT` in
`lean/QOU/MathlibExt/QPlancherel.lean` carried

```lean
bound : ∀ (f : ℕ → ℝ) (f_inf : ℝ) (k : ℕ), k ≥ 4 →
  |f k - f_inf| ≤ Cq / Real.sqrt (k - 3 : ℝ)
```

`Cq` is fixed by the instance while `f_inf` ranged over all of `ℝ`, so
`f := 0`, `f_inf := Cq + 1`, `k := 4` gives `Cq + 1 ≤ Cq`. Same shape as
`qou-hwax`: *an external theorem asserted for every inhabitant of a structure
that does not carry the theorem's hypotheses* — [feray2010] Thm 1.1 is about
the q-Plancherel branching fractions, and the carrier recorded only "a real
sequence and a real limit". Fixed on #6041, now on `main` with `f` and `f_inf`
as class **data**. That makes **five** instances of this one shape and **seven**
`False` axioms in this corpus's history, none of them found by a checker.

Two lessons from that exchange, one theirs and one a sharpening of it.

**1. Show the fix INHABITED, not merely unrefuted.** Theirs, and it is right: a
repair can trade one unusable class for another, and nothing catches it. #6041
proves both directions in one probe — old shape refutable, new shape inhabited.

**But "show it inhabited" can be discharged against the wrong object, and then
it is false comfort.** A structure and a hypothesis class about it are different
things, and the witness for one says nothing about the other. Worked case from
this branch: `reebSpectrumExample` inhabits `ReebSpectrum`, so the *shape* is
satisfiable — and it settles nothing about `HasReebSpectralCoords`, because that
witness has every `spec i = 1`, which would force `αᵢ = q` for all `i`, false
for any `Z` with distinct eigenvalues. The class needed its own result
(`hasReebSpectralCoords_satisfiable`, by diagonalising the exponents from
`exists_spectral_coord`). So the discipline is sharper than "exhibit a witness":
**exhibit a witness of the thing the conditional theorems actually depend on.**
The same applies to `isTannakaKreinDual_refl` — and there the witness is the
identity equivalence, which is a floor rather than evidence, and is labelled so
at the declaration.

**2. The two detectors are complementary and neither subsumes the other.**
Theirs (`scripts/limit-claim-encoding-audit.py`) asks *is the statement weaker
than the prose*; this one (`scripts/lean-overclaim-audit.py`) asks *is the
statement stronger than the truth*. The same field can pass one and fail the
other, and this field did: their detector flagged it and they triaged it a false
positive, correctly for the question it asks — an explicit quantitative bound is
not an unlocalised limit — and blind to whether the bound was **true**. Worth
the taxonomy row: a docstring/statement mismatch has two independent directions,
and a detector for either one is silent on the other.

Run both, and do not read a clean pass from either as a clean bill.

**Measured effect of the Tannaka–Krein fix on this detector**, branch vs
`origin/main`, same tool, same day:

| family | main | branch |
|---|---|---|
| `overclaim-structure` | 80 | 78 |
| `contentless-carrier` | 39 | 39 |
| `empty-carrier` | 9 | 9 |
| `overclaim-independent-binders` | 4 | 3 |
| **`opaque-type-axiom`** | **2** | **0** |
| total | 134 | 129 |

The `opaque-type-axiom` family is **eliminated**, and the attribution is checked
rather than assumed: its two hits on `main` are `RepLoc` and `ComodH` in
`tannaka-krein-isomorphism.lean`, the two axioms that fix removed. The other −3
is the rest of the branch, not that change; do not credit it there.

A fourth axiom, `qLog_tendsto_log_axiom`, is a *different* and simpler failure:
false against a definition three lines above it. No instantiation trick was
needed. That one argues for reading each axiom against its own file before
reaching for any detector.

## Hasse–Weil over the whole tower, added 2026-08-30

The arc had the point-count bound at `r = 1` only — `|∑ αᵢ| ≤ 2g√q` — which is
weaker than the name promises. Hasse–Weil is a statement about **every** finite
extension: Frobenius on `𝔽_{q^r}` acts with eigenvalues `αᵢ^r`, so

```
| |ℬ(𝔽_{q^r})| − (q^r + 1) |  ≤  2g·q^{r/2}
```

Three results, all one or two lines from the magnitude bound already proved, all
`#print axioms` clean:

- `norm_eigenvalue_pow` — `‖αᵢ^r‖ = (q^{1/2})^r`, the magnitude at every level.
- `norm_sum_eigenvalue_pow_le` — the bound itself, `‖∑ αᵢ^r‖ ≤ 8·(q^{1/2})^r`.
- `sum_eigenvalue_pow_isReal` — the power sums are **real** at every level, from
  conjugation-closure. Not decoration: `|ℬ(𝔽_{q^r})|` is an integer, so a power
  sum with nonzero imaginary part would be an inconsistency rather than a loose
  bound. The `r = 1` case was already there as `sum_eigenvalues_isReal`; the
  general one is what a trace formula would need.

**Tightness was checked, not assumed** — `norm_sum_eigenvalue_pow_tight`. A
bound tight at `r = 1` can still be loose in the tower, and the *growth rate* in
`r` is the part of Hasse–Weil that does the work; a loose rate would leave that
part unattested. On the supersingular witness (`q = 4`, all `αᵢ = 2`) the power
sum is `8·2^r` and the bound is `8·(4^{1/2})^r = 8·2^r` — equality at every `r`.

**The `r = 0` degeneracy is stated rather than excluded.** At `r = 0` every
`αᵢ^0 = 1`, the sum is `8`, and the bound reads `8 ≤ 8` — true and tight, and
carrying no arithmetic, since `𝔽_{q^0}` is not a field. The theorems quantify
over all `r : ℕ` because excluding it would buy nothing, but nothing downstream
should read the `r = 0` instance as a point count.

**What this is not.** It is more of the *local* theory, which is the half that
was never in doubt — Hasse–Weil has held unconditionally at every place since
1948. It does not move the arc toward RH; the assembly step still carries the
whole distance. It closes a gap between what the chapter proved and what it
claimed the name of.

## The remaining gaps, ranked by what they cost

### 1. Both axioms in `explicit-formula.lean` prove `False` — CORRECTED 2026-08-29

**This section originally read "`thm:explicit-formula` is assumed, not derived —
and the citation does not cover it", and said the defect was the caption rather
than the axiom. That was an undercall, and it was mine.** Re-measured the same
day: **both** axioms in the file prove `False`, machine-checked, each `#print
axioms` reporting its own axiom plus Lean's three. Bean `qou-qexf`.

`explicit_formula_axiom` quantified over `ideals` and `spectrum`
**independently**. The geometric side is determined by `ideals`, the spectral
side by `spectrum`, and nothing tied them together — so the identity was
asserted for every unrelated pair. With no ideals, no spectrum and
`Ω_q = 1/(2π)`, the left side is `0` and the right side exceeds `2`.

`qLog_tendsto_log_axiom` is false against its own definition three lines above
it: `qLog q x = log x / log q`, and `log q → 0⁺` as `q → 1⁺`, so for `x ≠ 1` it
**diverges**. Multiplying by `log q` forces `log 2 = 0`. The word *renormalised*
in its caption was pointing at the true fact — `qLog q x · log q = log x`, with
no limit — and what genuinely tends to `log x` is the Tsallis q-logarithm
`(x^{1−q} − 1)/(1−q)`, a different function.

Both are withdrawn. The file now has **zero live axioms and zero sorries**:
`qLog_mul_log` (the true identity, proved), `not_qLog_tendsto_log` and
`not_qExplicitFormula_empty` (the two refutations, proved and kept so the false
forms cannot return silently), `QZetaDatum` bundling one geometry's data, and
`QExplicitFormula` as a no-instance §3b conjecture class with `explicit_formula`
conditional on it.

The citation point in the original section still stands and is acted on: Rosen
Thm 5.12 and Weil are the classical explicit formula over `𝔽_q`, which is
theirs; the q-deformation — `[ρ]_q`, `ln_q`, the `Ω_q` term — is the framework's
own, and is now `[manuscript]`.

**Corpus-grep** run on "explicit formula" (all six paths): 7 audit hits (all
mass-theory or the rhax audit), 6 `computations/` hits (λ-scale, h4 drivers,
figure-eight), 3 `library/INDEX.md` hits (Reidemeister torsion, holonomy
R-matrix, Ohtsuki), 5 beans. **None derives it.** The identity remains open; it
is now stated as open rather than assumed.

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

### 4. Eight open conjectures in the chapter — and a sorry count of my own that was wrong

`conj:q-geometric-langlands`, `conj:q-gl-fiber-functor`, `conj:q-gl-classical-limit`,
`conj:q-gl-kummer-filtration`, `conj:q-oper-hecke` (no Lean carrier);
`conj:quantum-langlands-dual`, `conj:mirror-3d-3d-correspondence`,
`conj:modular-s-transform-q-q-tilde` (class carriers). These are Langlands-side,
not RH-side: none is on the four-step spine, and none is what blocks the arc.

**CORRECTION.** An earlier version of this section said
`thm:tannaka-krein-isomorphism` "carries a `sorry`", and the survey table behind
it reported sorries in four chapter files. **All of those were docstring
mentions.** Measured with a comment-stripping counter: the chapter has **6 raw
`sorry` matches and 0 real ones** — every hit is prose of the form *"the class
instance is the conjectural witness (sorry = conjecture)"*, and one is in
docstring text I wrote myself. The chapter is sorry-free.

Two real findings survive that correction:

- **`tannaka-krein-isomorphism.lean` is content-free, and this is already
  known.** `axiom RepLoc : Type` and `axiom ComodH : Type` are unconstrained
  opaque types; `tannaka_krein_isomorphism_axiom : Nonempty (RepLoc ≃ ComodH)`
  then asserts a bijection between two arbitrary types, which is consistent and
  says nothing about representation categories. Per the corpus-grep checklist
  this is **not a new finding**:
  [`2026-07-02-lean-proof-progress-qa-table.md`](2026-07-02-lean-proof-progress-qa-table.md)
  line 729 already flags the block `da-vacuous` alongside
  `da-lean-narrative-divergence`. Recorded here because it is load-bearing —
  `conj:explicit-formula` cites it in `uses[]`.

  > **FIXED 2026-08-30.** A third defect turned up on close reading, and it is
  > the worst of the three: `tannaka_krein_isomorphism` was *its own axiom* —
  > `theorem … := tannaka_krein_isomorphism_axiom`, a proof term that returns
  > the assumption asserting it. Sorry-free, `#print axioms`-dirty, and
  > indistinguishable from a result without reading the proof. That is the shape
  > §"Axiomatization is NOT a Proof" names.
  >
  > Also worth separating from "the types are opaque": **`≃` is `Equiv`, a
  > bijection of types.** The narrative claims an equivalence of *categories*
  > (`≌`). Even with the right types the statement would have forgotten every
  > morphism.
  >
  > Replaced by `IsTannakaKreinDual`, which takes the two categories as
  > **parameters** — nothing opaque — and carries one field:
  >
  > ```lean
  > equiv_over_fibre : ∃ e : RepLoc ≌ ComodH, Nonempty (e.functor ⋙ τC ≅ τR)
  > ```
  >
  > An equivalence of categories *lying over the fibre functors*. The
  > compatibility is the content of Tannaka–Krein, not a decoration:
  > inequivalent Hopf algebras can have equivalent comodule categories, and τ is
  > what separates them. One field rather than two, so the compatibility is
  > asserted of the *same* `e`.
  >
  > `isTannakaKreinDual_refl` witnesses inhabitedness (a category is dual to
  > itself over its own fibre functor). **That witness is the identity, so it
  > establishes a floor and not evidence** — it rules out an unsatisfiable
  > carrier, nothing more. No instance for `Rep_loc(A)` and `Comod(H_ξ)`.
  >
  > The block is demoted `thm:` → `conj:`, matching the disposition chosen for
  > `thm:explicit-formula` earlier in this session. **Cascade: zero.** Of the
  > three `uses[]` consumers, two (`conj:q-birch-swinnerton-dyer`,
  > `conj:explicit-formula`) are already conjectures, and the third
  > (`def:categorical-mordell-weil`) is a definition, which §3b exempts from
  > propagation. Two `axiom` declarations leave the corpus; `#print axioms` on
  > `tannaka_krein_isomorphism` is now `[propext, Classical.choice, Quot.sound]`
  > where it previously named the axiom.

- **Two of the three chapter conjecture carriers assert nothing.**
  `Mirror3d3dCorrespondence` and `QuantumLanglandsDual` each have the single
  field `holds : Prop`, which `⟨True⟩` inhabits, so a `[C]`-conditional theorem
  proves nothing modulo `C` — the `proof-claims-unencoded` / `true-class-field`
  shape. The third, `ModularSTransformQQTilde`, is the model of how it should
  look: a conjectural continuation `F : ℂ → ℂ`, a `nondegenerate` field, and the
  `s_automorphy` law. Three carriers, one chapter, two dispositions.

**Corpus-wide, `holds : Prop` is 23 files — not the 52 a first grep reported.**
A naive grep matches 38 files, of which **15 are prose only**: docstrings
describing a stub that was already replaced. `modular-s-transform-q-q-tilde.lean`
is itself one of those false positives, its docstring recording that it *"replac[ed]
the former `holds : Prop` stub"*. A 39 % false-positive rate, removed entirely by
stripping comments before matching — the same error class as the sorry count
above, in the same session.

Not fixed here. Giving `QuantumLanglandsDual` real content means deciding what
the conjecture claims about `QOU.Hecke.HeckeAlgebra` — a mathematical judgment
about the author's intent, not a mechanical repair, and an encoding restricted to
parameter-level facts about `ℝ` would be *provable*, which would misrepresent an
open conjecture as closed. That is a worse outcome than the stub. Bean `qou-hprp`.

**Why none of them had ever been flagged — bean `qou-vgat`.** Asking why no
`holds : Prop` carrier appears in
[`lean-vacuity-review-ledger.json`](lean-vacuity-review-ledger.json) turned out to
be the more consequential question: **the audit could not see them.**
`isConjectureCarrier` in
[`lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
admitted a declaration only if its docstring carried a `conj:` reference or the
word "axiomatis"; a carrier whose docstring is a bare `**CONJECTURE.** …` fails
both, and that gate runs *before every criterion in the family*. Widening it
moved the conjecture graph from **243 to 309 carriers** — sixty-five had never
been examined, among them every carrier named in this section.

Separately, `proof-dependent-conjecture-not-conditional` — severity **critical** —
returned **0 hits across 244 carriers and 3264 files**, through three compounding
defects (wrong source file, a label map keyed on a spelling used in 15 files
against 113, and a regex one character short of the corpus's own cross-reference
form). Now 0 → 3. Both are fixed on this branch; the `field : Prop` shape still
has **no criterion at all**, which is why widening the gate did not move
`proof-claims-unencoded`, and that remains an owner call.

Cautionary note attached to that work: my first report of the conditionality fix
said 5 hits and attributed three of them to carriers that are in fact well-formed.
A `.md` is the narrative of a whole *block*, and I charged one block-level
sentence to each of the three classes sharing that file. Corrected to 3, scoped
per file. The rule I had already written into the sibling detector's docstring —
sample before quoting — is the one I skipped.

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
4. **The detector exists as of this review** —
   [`scripts/lean-overclaim-audit.py`](../../scripts/lean-overclaim-audit.py),
   with a `--selftest` that includes a negative fixture so a future narrowing
   cannot report a clean tree by reading prose. Its calibration is in its own
   docstring and is worth reading before quoting it: the first run said 172
   candidates, the corrected run 131, and the difference was a bug of mine —
   the binder classifier keyed on the name rather than the type, so `(hq : 1 < q)`
   counted as a data parameter. `contentless-carrier` (39) is the trustworthy
   family; `overclaim-structure` (78) still over-flags on hypothesis-carrying
   structures and its precision is not established.

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
