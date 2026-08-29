# Two axioms proving `False`, and the 73 content-block Lean files nothing compiles

**Date:** 2026-08-22
**Bean:** `qou-rhax` (high)
**Branch/PR:** `claude/q-ns-classical-gaps-9l9mj9` / #5467
**Scope:** `content/quantum-observable-universe/stochastic-mechanics/macroscopic-stability-equivalence.{lean,md,ts}`, plus a corpus-wide measurement of which content-block `.lean` siblings compile.

---

## 1. The defect

`macroscopic-stability-equivalence.lean` carried two axioms:

```lean
axiom macroscopic_iff_rh_axiom :
    ∀ (ψ : R_q → R_q) (ζ : ℂ → ℂ), MacroscopicStability ψ ↔ RiemannHypothesis ζ

axiom rh_iff_persistence_axiom :
    ∀ (ζ : ℂ → ℂ) (spectral_limit : ℕ → Fin 8 → R_q),
      RiemannHypothesis ζ ↔ SpectralPersistence spectral_limit
```

**Both prove `False`, and for one shared structural reason.** An
`∀ a b, P a ↔ Q b` quantifies its two sides **independently**, which forces
`P` to be constant in `a`: fix any `b` and the right-hand side stops varying,
so all values of `P a` agree with each other.

`RiemannHypothesis` is not constant in `ζ`:

- `RiemannHypothesis (fun _ => 1)` holds **vacuously** — the constant 1 is
  never zero, so the implication's hypothesis `ζ s = 0` is never met.
- `RiemannHypothesis (fun _ => 0)` **fails** — every point of the strip is a
  zero, so `s = 1/4` would have to satisfy `1/4 = 1/2`.

Feed both into either axiom with the other argument fixed, and `False`
follows in four lines.

**Machine-checked** (Lean v4.24.0, `lean`-direct against the restored
Mathlib oleans). A standalone file restating the second axiom derives
`False` from it, and `#print axioms` reports the derivation depends on
nothing but that axiom plus `propext`, `Classical.choice`, `Quot.sound` —
no `sorryAx`, no other input.

The argument uses only `RiemannHypothesis`. It needs neither
`SpectralPersistence`'s content nor `LaurentPolynomial`, so it survives any
repair to those.

### The independently-reported route

`agent:p01` found this on the stochastic-mechanics trap-drain by a different
argument: `SpectralPersistence f`, as written, was

```lean
(∀ (n : ℕ) (i : Fin 8), spectral_limit n i = 1/2) →
  ∀ (i : Fin 8), spectral_limit 0 i = 1/2
```

— *"if every level is ½ then level 0 is ½"*, which is instantiation and is
inhabited by `fun h i => h 0 i`. So the axiom equated `RiemannHypothesis ζ`
with a **tautology**, for every `ζ`. Either route suffices; the
quantifier-shape route is the more general statement, since it also condemns
the first axiom.

---

## 2. Three further defects in the same file

**It had never compiled.** `lean`-direct reports **22 errors**: the two
imports never provided `LaurentPolynomial`; two docstrings sat back to back
before `macroscopic_iff_rh_axiom` (`unexpected token '/--'`); and the
`noncomputable section` was never closed, so the final `end
QOU.AlgebraicSubstrate` failed against an unnamed scope.

This is the real reason the blast radius was contained. The bean recorded
that nothing imports the file — true, but the stronger fact is that **there
was nothing to import**: no declaration in it ever entered any environment.

**`1/2 : R_q` does not elaborate.** `R_q = LaurentPolynomial ℤ` has no `Div`
instance, so `HDiv ℕ ℕ R_q` fails to synthesize. Both `SpectralPersistence`
and `MacroscopicStability` were **ill-typed as written** — the critical-line
condition and the `X ^ (1/2 + ε)` error bound are archimedean statements that
cannot live over a Laurent-polynomial ring. Restated over `ℝ`/`ℂ`, which is
what §7c requires here: the ordering, `|·|` and `rpow` are genuinely
archimedean, so this belongs on the archimedean side of the wall.

**The Weil attribution was wrong.** The second axiom was headed *"External
axiom (Weil 1948 explicit formula): RH ↔ spectral persistence"*. Weil's
explicit formula is a duality between zeros and prime powers. No formulation
of it makes RH equivalent to a proposition in which `ζ` does not occur — and
the removed axiom's right-hand side does not mention `ζ` at all. **The
citation is what made an arbitrary axiom look load-bearing.** It is
withdrawn; the `weil1948` cite is dropped from the block manifest. The von
Koch attribution on the first axiom is accurate for the direction it names
and is retained in prose.

---

## 3. The fix

Both axioms removed. Replaced by a single content-bearing **primary
conjecture class** (§3b, §3b-tax) over **one datum**:

```lean
structure SubstrateSpectralDatum where
  zeta : ℂ → ℂ
  psi  : ℝ → ℝ
  rho  : ℕ → Fin 8 → ℂ

class MacroscopicStabilityEquivalence (D : SubstrateSpectralDatum) : Prop where
  stability_iff_rh     : MacroscopicStability D.psi ↔ RiemannHypothesis D.zeta
  rh_iff_critical_line : RiemannHypothesis D.zeta ↔ CriticalLineSpectrum D.rho
```

Binding `ζ`, `ψ` and `ρ` into one structure **is** the fix. Both fields
quantify over the same `D`, so neither forces either side to be constant in
its argument — which is what the informal statement always meant. This is
the §"Grep the claim SHAPE" item-3 distinction (shared type vs shared
instance) applied as a repair rather than as a review finding.

There is deliberately **no instance**. The honest state of "RH ↔ our
spectral condition" is *open*, not axiomatised (§"Axiomatization is NOT a
Proof"). `CriticalLineSpectrum ρ := ∀ n i, (ρ n i).re = 1/2` constrains the
whole family, so unlike its predecessor it has content.

The one theorem is conditional on the class and derives the equivalence the
class does **not** carry — `(1) ↔ (3)` — by `Iff.trans`. That is a derivation
from the hypotheses, not a projection of a field (§3b-cond item 5, the
failure mode the old `macroscopic_stability_equivalence` exhibited by
returning `⟨axiom₁, axiom₂⟩`).

Two small theorems are kept in the file so the inconsistency argument is
checkable *there* rather than only in commentary:
`riemannHypothesis_const_one` and `not_riemannHypothesis_const_zero`.

**The block is demoted `theorem` → `conjecture`** (`thm:` → `conj:`), with
the three live references retargeted. Both downstream consumers are
`remark`s, which may freely interpret a conjecture (§3a), so no propagation
violation arises.

### Verification

- `lean`-direct on the rewritten file: **exit 0, silent, 2.4 s** — the first
  time this file has ever compiled.
- `#print axioms` on all three declarations: `[propext, Classical.choice,
  Quot.sound]`. No `sorryAx`, no custom axiom.
- Note this file has no build target (see §4), so this agent verification is
  the only gate.

  **CORRECTED 2026-08-28.** This read *"not covered by
  `lean-content-siblings.yml`"*, which is wrong about the mechanism and
  under-states the problem. That workflow's `content-sibling-compile` job
  **does** cover content-block siblings — it runs `lean`-direct on the `.lean`
  files a PR changes, which on that PR would have included this one. It did not
  run for **two** independent reasons, and only naming the second is what makes
  the finding durable:

  1. **It is `workflow_dispatch:` only** — "CI auto-triggers disabled (owner
     directive 2026-06-30): Actions billing". So it never fires on a push or a
     PR, and nothing enqueues it.
  2. **It is diff-scoped by design**, and deliberately so: a whole-tree gate
     would block every PR on the pre-existing backlog. So even with triggers
     restored it would gate *new* drift and never reach the 73 already there.

  Reason 2 is the one that survives billing being fixed, and it is the reason
  §4's remedy has to be a widened gate rather than a re-enabled one.

---

## 4. Why it survived: 73 content-block Lean files nothing compiles

Content-block `.lean` siblings live at `content/<paper>/<chapter>/<block>.lean`
— **outside** `content/<paper>/lean/`, and therefore outside the `qou`
package's `globs = ["QOU", "QOU.+"]`. `lake build QOU` never touches them.

Measured with `lean`-direct across all **958** such files, at 6-way
parallelism:

| | count | share |
|---|---:|---:|
| exit 0 | **885** | 92.4 % |
| non-zero | **73** | 7.6 % |

**The first pass of this measurement said 297 (31 %), and that was wrong.**
`LEAN_PATH` held only `.lake/packages/*`, so every file importing `QOU.*`
failed on an unresolvable module. Adding the three paper build directories
moved 224 of the 297 to exit 0. Quoting 31 % would have overstated the
problem by a factor of four — the number is 7.6 %.

By chapter, the 73 concentrate in `mass-theory` (27) and `predicted-spectra`
(10); the rest are scattered ≤ 8 per chapter.

This is the population that lets a file with 22 errors and an inconsistent
axiom sit in the tree indefinitely. The lakefile already records an earlier
widening (bean `qou-rc7b`, `QOU.lean` root → `QOU`/`QOU.+` globs) that
recovered 785 unbuilt modules **inside** `lean/`; the 958 siblings are a
separate population that widening did not reach.

### Triage of the 73

Per-file first-error and error-count data:
[`2026-08-22-unbuilt-lean-siblings-triage.tsv`](2026-08-22-unbuilt-lean-siblings-triage.tsv)
(columns: error count, path, first error).

| first-error class | files |
|---|---:|
| `RESOLVE` — unknown identifier or constant | 30 |
| `INSTANCE` — failed to synthesize / bad binder | 13 |
| `PARSE` — unexpected token, unterminated comment | 9 |
| `PROOF` — unsolved goals, unknown tactic, no goals | 6 |
| `TYPE` — function expected, type mismatch, not a field | 5 |
| `ENV` — **not a file defect** (see below) | 4 |
| `DUPLICATE` — name already declared | 3 |
| `NONCOMPUTABLE` — needs `noncomputable` | 2 |
| `OTHER` | 1 |

**Four of the 73 are environment artifacts, not defects.** They fail with
`object file '…/QOU/MassEndomorphism/JetTower.olean' … does not exist` —
an imported *library* module has no built olean in this container. Whether
those four files are sound is **undetermined** here. So the confirmed
file-defect count is **69 of 958 (7.2 %)**, not 73.

**66 of the 73 back a block that declares a `lean:` ref** — 25
propositions, 21 definitions, 5 lemmas, 5 corollaries, 4 theorems, 4
conjectures, 7 remarks. Sibling resolution takes precedence over the
library path (§0a), so for those blocks the paper's claimed formalisation
*is* the non-compiling file. The 21 definitions matter most: a
`definition` block requires a Lean sibling at type level.

**The error counts are a LOWER BOUND, and reading them as repair cost is a
mistake I made and then measured.** Lean halts at the first parse error and
never reports what is behind it, so a file counted as "1 error" can need
several sequential repairs. 339 errors across 73 files, median 2 per file,
30 files with exactly one error — treat all three as floors.

Measured on the first five repaired (§4a): **two** were a genuine one-line
fix; **three** needed two or three rounds, and one of those hid a structure
that does not exist anywhere in the corpus.

The class distribution still says *drift*, not unfinished work — renamed
Mathlib lemmas dominate (`RESOLVE`, 41 %). Confirmed renames found so far:
`abs_add` → `abs_add_le`, `div_lt_iff` → `div_lt_iff₀`, `div_lt_div_iff` →
`div_lt_div_iff₀`. One file appeared to dominate the total
(`frobenius-codim-universal.lean`, "101 errors"). **Both halves of that
sentence were wrong**, and the file is worked through in §4b.

### 4a. First five repaired (this branch)

| file | rounds | what it actually took |
|---|---:|---|
| `climax-volume-mass/q-momentum` | 1 | `abs_add` → `abs_add_le` |
| `predicted-spectra/hadron-half-life` | 1 | `div_lt_iff` → `div_lt_iff₀` |
| `glossary/glossary-s3-group` | 2 | missing `Fintype` import; then the *first* import tried (`GroupTheory.Perm.Fintype`) has no olean in this container — `Data.Fintype.Perm` does |
| `predicted-spectra/q-value-transition` | 3 | `div_lt_div_iff` → `div_lt_div_iff₀`; then `push_cast` had to precede the rewrite (goal carries `↑(A+1)`, not `↑A + 1`); then an `nlinarith` hint stated over `ℤ` against an `ℝ` goal |
| `predicted-spectra/gauge-coupling-uniqueness` | 3 | unterminated docstring; behind it `∃ λ :` (reserved token); behind *that* `GaugeCouplingUniquenessData` **undefined corpus-wide**, auto-bound to a metavariable |

The last is the instructive one. Its declaration body was `d.exists_lambda`
— the "corollary" was to be the projection of a field of its own hypothesis
structure, which under §3b-cond item 5 derives nothing. Restoring the
missing structure with an `exists_lambda` field would have made the file
compile **while proving nothing**. It was instead rewritten so the structure
carries genuine hypotheses (linearity of both couplings, non-degeneracy of
the reference) and the theorem derives the conclusion, with the witness
`lam = phi 1 · (psi 1)⁻¹`. `#print axioms` → `[propext]`.

That is the warning for the rest of the tranche: **a file that compiles is
not thereby a file that proves anything**, and this population has had no
reviewer at all.

By chapter: `mass-theory` 27, `predicted-spectra` 10,
`quantum-observable-universes` 8, then ≤ 3 each.

**Not fixed here.** Repairing the 69, or bringing the population under a
build target, is its own tranche and is not in scope for this branch — the
measurement and triage are recorded so the next agent starts from a number
rather than from a guess. Bean `qou-lsib`. The
`macroscopic-stability-equivalence.lean` fix removes one of them.

---

## 5. The sibling that got this right

`ClassicalRiemannHypothesis.lean`, flagged clean in the same trap-drain
batch, is the model: a content-bearing class, **no instance**, and a removed
axiom recorded in its docstring. Two files, one chapter, opposite
dispositions — which is what an unbuilt population looks like from the
inside.

### 4b. `frobenius-codim-universal.lean` — the outlier, worked through

Two claims I made about this file were wrong.

**"101 errors" was never a count.** Lean stops at `maximum number of errors
(100; from option maxErrors)` — the figure is the cap plus the cap message.
Every "error count" in the triage table is bounded above by 101 for the same
reason, so the total of 339 is a floor, not a measurement.

**"44 of them are `λ` used as a binder" was wrong.** `λ` *is* reserved in
Lean 4 and the file did use it as a binder in 43 code lines (73 further
occurrences are prose in comments, where it is correct notation for a
partition and must be left alone). But renaming all 43 to `lam` changed the
error count by **zero**: the parse failures were masking an equal number of
elaboration failures behind them. Fixing the visible errors revealed the
real ones rather than reducing the count.

What actually cut the file down, in order:

| step | errors after |
|---|---:|
| baseline | 100 (capped) |
| rename the 43 `λ` code binders → `lam` | 100 (capped) |
| **add `import Mathlib.Data.Real.Basic`** | **34** |
| convert 2 orphan docstrings to `/-! … -/` | 32 |
| **`set_option maxHeartbeats 1000000` on `heckeH8DimQ`** | **8** |

The two large drops are the interesting ones.

**`ℝ` was not `Real`.** The file imported `Algebra.Basic`,
`BigOperators.Fin` and `RepresentationTheory.FDRep` — none of which supplies
`Mathlib.Data.Real.Basic` — and did not set `autoImplicit false`. So every
`ℝ` in the file was **auto-bound as a free type variable**, and 85 errors
read `failed to synthesize OfNat ℝ 0`. One import line fixed all 85.

**I then tested whether that generalises, and it does not — see §4c.**

**A 22-case `match` exceeded the elaborator's heartbeat budget.**
`heckeH8DimQ` (the q-hook-length dimensions of the 22 partitions of 8) timed
out at `whnf`, so the *definition* failed and the name was auto-bound to a
metavariable at all 22 use sites — reported as 22 separate
`Function expected at heckeH8DimQ` errors, which look like 22 problems and
are one. Note `set_option … in` must precede the **docstring**, not sit
between docstring and declaration; placing it wrongly costs another parse
error.

**Still 8 errors, and they are real.** Three `unsolved goals`, three
`typeclass instance problem is stuck`, one `simp` failure, one `rewrite`
failure. That is formalisation work, not drift, and it is **not** done here.
The file remains in the failing set.

### 4c. The `ℝ`-is-not-`Real` root cause does NOT generalise (measured)

§4b's one-import fix was dramatic enough that I expected it to be the
population's dominant root cause, and wrote as much. Tested, it is not.

**31** of the 73 failing files use `ℝ` without importing
`Mathlib.Data.Real` directly. Each was given the import, re-run, and the
import kept **only** if the error count actually dropped
([`2026-08-22-real-import-experiment.tsv`](2026-08-22-real-import-experiment.tsv)):

| outcome | files |
|---|---:|
| improved | **2** |
| no change | 29 |

So the hypothesis is **refuted as a general rule: 2 of 31, about 6 %**. Most
of those files reach `Real` transitively through some `Mathlib.Analysis.*`
import, so their `ℝ` is genuinely Mathlib's and their errors are elsewhere.
`frobenius-codim-universal` was unusual in importing only
`Algebra.Basic` / `BigOperators.Fin` / `RepresentationTheory.FDRep`, none of
which pulls `Real` in.

The two that improved are kept:

| file | errors | note |
|---|---|---|
| `mass-theory/knot-factor-borromean-composite` | 6 → **0** | now compiles |
| `mass-theory/reeb-bundle` | 3 → 1 → **0** | the import exposed `Real.exp` and `Real.pi` as unknown; adding `SpecialFunctions.Exp` and `Trigonometric.Basic` closed it |

`reeb-bundle` is the pattern in miniature and the reason the *empirical*
form of this test matters: the first import does not fix the file, it
changes which error is visible. A sweep that added the import everywhere on
the strength of §4b would have touched 29 files for no benefit while
claiming a root-cause fix.

### 4d. Full re-triage on the rebased tree (authoritative)

The §4 classification was taken before any repairs and is stale in a way
worth naming: parse errors mask what is behind them, and one file's count
was the error **cap**. Everything was re-measured after rebasing onto `main`
at `e9fd81a63`. The TSV linked above is this run, not the original.

| | count |
|---|---:|
| population | **955** (958 − the 3 deleted stubs) |
| pass | **899** |
| **fail** | **56** (5.9 %) |
| error-capped | **0** |

**The counts are now real counts, not floors.** Nothing hits the 100-error
cap any more, so unlike the original 339 the new total of **221 errors
across 56 files** can be read as written. **16** files carry exactly one
error.

**Reconciliation — 73 → 56, and every one of the 17 is accounted for:**

| | files |
|---|---:|
| repaired on this branch | 13 |
| deleted as shadowing stubs | 3 |
| **fixed on `main` by a sibling agent** | **1** |

The last is `predicted-spectra/spectral-decomposition-qvalue.lean`, closed by
`2f453c89e` (*"discharge two inactive branches of the Rosso–Jones per-shell
cancellation"*) among the 83 commits that landed while this branch was open.
**Zero files newly failing** — nothing regressed.

**First-error class, re-measured:**

| class | files |
|---|---:|
| `RESOLVE` — unknown identifier/constant | 22 |
| `INSTANCE` — failed to synthesize / bad binder | 11 |
| `PROOF/TACTIC` | 6 |
| `PARSE` | 6 |
| `TYPE` | 5 |
| `ENV` — dependency olean missing, **not a defect** | 4 |
| `OTHER` | 2 |

By chapter: `mass-theory` 19, `quantum-observable-universes` 8,
`predicted-spectra` 6, then ≤ 3 each. Excluding the 4 `ENV` cases, the
confirmed defect count is **52**.

**`RESOLVE` at 39 % is the obvious next batch, but it is two populations
that this classification does not separate**: Mathlib renames (cheap and
mechanical — `abs_add` → `abs_add_le`, `div_lt_iff` → `div_lt_iff₀`,
`div_lt_div_iff` → `div_lt_div_iff₀`, `one_rpow` → `Real.one_rpow` are the
four confirmed so far) versus unknown *project* constants, which are
formalisation gaps and not cheap at all — `GaugeCouplingUniquenessData` and
`heckeH8DimQ` both presented as `RESOLVE`-class and neither was a rename.
Split that before estimating the batch.

### 4e. The `RESOLVE` split, and the `Foo.mk.field` batch

§4d flagged that `RESOLVE` (22 files, 39 %) is two populations. Splitting
them by hand on the unknown name:

- **Mathlib-side** (renames or missing imports — cheap): `Complex.abs`,
  `Real.sqrt` ×2, `MonoidalFunctor`, `div_le_div_iff`,
  `Nat.pos_of_lt_of_le`, `intervalIntegrable_log'`,
  `CategoryTheory.Preadditive`,
  `CategoryTheory.MonoidalCategory.whiskerRight_comp`,
  `Real.tendsto_log_mul_rpow_nhdsGT_zero`, `Algebra`.
- **Project-side** (formalisation gaps — not cheap): `q_param`,
  `zPochhammer`, `hoefsmit_v21_b_sq_rational`, `R`,
  `QOU.BraidKnot.ConfinementLevel.exists`,
  `QOU.BraidKnot.ResidueAtRoot.residue`, and **five**
  `QOU.Archimedean.<Particle>.mk.<field>`.

**The five are one bug, not five.** `up-quark`, `electron-knot`,
`neutrino-knot`, `antineutrino-knot` and `positron-knot` all write
`Foo.mk.field` — projecting a field off the *constructor*. Every field of
these structures has a default, which is presumably what made the form look
plausible, but `Foo.mk` is still a function and Lean reports the whole thing
as an unknown constant. The idiom is `({} : Foo).field`, which fills the
defaults. 20 sites rewritten; four of the five now compile.

**`positron-knot` is blocked on something structural** (6 → 2 errors). Its
two genuine cross-particle theorems — charge opposite, orientation reversed —
reference `Electron`, which is declared in `electron-knot.lean`. That is a
*sibling* content-block file, not a library module, so it cannot be
imported. Both files sit in namespace `QOU.Archimedean` and would see each
other inside a Lake library; standalone they cannot. Two honest options:

1. **Move the particle structures into `content/<paper>/lean/QOU/Archimedean/`**
   so siblings can import them. Correct architecture, and it is what
   `lean.ref` candidate-2 resolution assumes — but a refactor across several
   blocks.
2. Leave the two theorems failing and say so.

**Not option 3: duplicating `Electron` into `positron-knot.lean`.** That
manufactures exactly the defect three stubs were deleted for earlier on this
branch — and the corpus already has an instance of it: **`structure UpQuark`
is declared twice**, in `up-quark.lean:40` and `down-quark.lean:48`. Latent
today because nothing compiles both at once; a live duplicate the moment
anything does.

**Standing count: 56 → 52 failing.**

### 4f. The Mathlib-side batch — and an invalid experiment, discarded

Four more compile (`maximal-ideal-defect`, `q-reeb-lattice-vibration`,
`knot-particle-generation`, `categorical-q-ext-deriv`), all by adding an
import that was simply missing. Confirmed targets:

| unknown name | supplying import |
|---|---|
| `Algebra` | `Mathlib.Algebra.Algebra.Defs` |
| `RingHom.ker` | `Mathlib.RingTheory.Ideal.Maps` |
| `Real.sqrt` | `Mathlib.Analysis.SpecialFunctions.Sqrt` |
| `CategoryTheory.Preadditive` | `Mathlib.CategoryTheory.Preadditive.Basic` |
| `CategoryTheory.Linear` | `Mathlib.CategoryTheory.Linear.Basic` |

Confirmed renames extend the list from §4b:
`div_le_div_iff` → `div_le_div_iff₀`.

**An experiment that produced a clean-looking false result.** To split the
`RESOLVE` files into *missing-import* versus *renamed-away* cheaply, each
was re-run with `import Mathlib` prepended: if the error count dropped, the
name exists somewhere and the file just needs the right import. It returned
a tidy **6 IMPORT / 2 RENAME**.

**It measured nothing.** `Mathlib.olean` — the top-level aggregator module —
is **not in the restored olean cache**, so `import Mathlib` fails with
exactly one error and leaves every declaration below it unelaborated. Every
file therefore lands on `after = 1`, and the "verdict" was just sorting
files by whether they started with more than one error. The two "RENAME"
files were the two that happened to start with exactly one.

The tell was the *uniformity*: `after = 1` for all six, from starting counts
of 2, 2, 2, 3, 5 and 9. A real signal does not converge on one value.
Recorded because the artifact is specific to a **restored** olean tree and
will reappear for anyone probing this population the same way — and because
a blanket `import Mathlib` is a plausible-looking move that cannot work here
at all.

The valid probe is per-name: `import <candidate>` + `#check @<name>`, both
of which need real oleans, and which is what produced the table above.

**Two files improved but not closed**, and neither residual is a rename:

- `c5-involution-leibniz-decomposition` (3 → 1): behind `div_le_div_iff` sat
  `eq_inv_iff_mul_eq_one₀`, which does **not** exist while
  `eq_inv_iff_mul_eq_one` does — an `₀` added where the family does not have
  one, the opposite of the `div` case. Dropping it resolves the name and
  then fails the `rewrite`, because the two lemmas have different shapes and
  the `h_ne` argument has nowhere to go. Goal-state work; reverted.
- `spectral-half-line`: `Complex.abs` is **gone** from Mathlib in favour of
  `‖·‖`. Both `Complex.abs z` and `Complex.abs_exp` need rewriting — a real
  edit, not a substitution.

`classical-limit-functor` is the same class: `MonoidalFunctor` as a *type*
no longer exists; the modern form is a plain functor plus a `[F.Monoidal]`
instance, which changes the field's signature.

**Standing count: 52 → 48 failing.**

### 4g. The cross-sibling blocker is a class, not a one-off — and a revert

`positron-knot` was recorded in §4e as blocked because it references
`Electron`, declared in a sibling content-block file that cannot be
imported. **`spectral-half-line` has the identical blocker**: it references
`LocalQZetaFunction`, declared in `local-q-zeta-function.lean`, a sibling.
A third file, `hasse-weil-bound.lean`, references the same structure.

So this is a **class**. Content-block siblings in one chapter routinely
refer to each other's structures — which works inside a Lake library and
cannot work for standalone files. The architectural fix named in §4e (move
shared structures into `content/<paper>/lean/QOU/…`) is worth more than the
per-file repairs, because it closes several files at once and stops the
pattern recurring. It is not attempted here: it reshapes the tree and is an
owner decision.

**A migration begun and reverted.** `spectral-half-line` also needs a real
Mathlib migration — `Complex.abs` is **gone** in favour of `‖·‖`:

| old | new |
|---|---|
| `Complex.abs z` | `‖z‖` |
| `Complex.abs_exp` | `Complex.norm_exp` |
| `Complex.abs_ofReal` | `Complex.norm_real` (to a **real** norm, not to `|·|`) |

The last is the trap: `Complex.norm_real : ‖(r : ℂ)‖ = ‖r‖` lands on
`Real.norm_eq_abs`, so a proof that previously went straight to
`abs_of_pos` now needs both lemmas in sequence. Two attempts at that chain
still failed on goal shape.

**The whole edit was reverted rather than landed**, because the file cannot
compile either way while `LocalQZetaFunction` is unreachable — so a partial,
unverifiable migration would sit in the tree looking like progress and
misleading the next reader. The table above is recorded so the discovery
does not have to be repeated; the migration should land together with
whatever resolves the structural blocker.

### 4h. The structural fix, and a baseline that had silently expired

The owner authorised the §4e/§4g architectural move. Two library modules now
hold the structures that content-block siblings were re-declaring or failing
to reach:

- `QOU/Archimedean/ParticleKnots.lean` — Electron, Positron, Neutrino,
  Antineutrino, UpQuark, DownQuark
- `QOU/AlgebraicSubstrate/LocalQZetaFunction.lean`

| file | before | after |
|---|---:|---|
| `positron-knot` | 6 | **exit 0** |
| `up-quark` / `electron-knot` | 4 / 4 | **exit 0** |
| `neutrino-knot` / `antineutrino-knot` | 3 / 3 | **exit 0** |
| `local-q-zeta-function` | — | **deleted** (contained only what moved) |
| `spectral-half-line` | 4 | 6 |
| `hasse-weil-bound` | 22 | 24 |

**Not a dedup — the duplicates disagreed.** `down-quark.lean` carried
*stripped-down* copies of `Neutrino` and `UpQuark`. The fuller declarations
are canonical; field-level identity was checked against all six originals
before switching.

**The two that rose are not regressions.** Removing the blocker lets those
files reach proof errors it was hiding.

**The `Complex.abs` migration reverted in §4g was re-applied**, because the
blocker's removal made it verifiable. It clears its class outright: two
`Unknown constant Complex.abs` → **zero**.

#### A baseline that expired without saying so

§4d's validation baseline — "✗ Invalid, 5 issue(s), identical on clean HEAD"
— was measured at `c37d5eda9`, **before this branch was rebased onto
`e9fd81a63`**. The rebase brought in main's commits, one of which
(`1d3988bc3`) broke `motivic-perpetual-obstruction`. The count became 21, and
the 5 stopped being a comparison the moment the base moved. It was carried
forward across that boundary anyway, and briefly read as evidence that this
branch had introduced 16 issues.

**Re-measured properly**, by validating `origin/main` in a worktree and
diffing the issue lists: **21 on main, 21 on the branch, byte-identical apart
from the worktree path in one error string.** The branch adds nothing.

The rule this earns: *a validation baseline is valid only against a fixed
base, and a rebase silently invalidates it.* Re-measure the base, do not
carry the number.

#### A live breakage on `main`, not fixed here

17 of the 21 stem from one commit. `1d3988bc3` changed
`motivic-perpetual-obstruction.ts` from `conjecture()` to `theorem()` while
leaving its label `conj:…`. A `theorem` block requires a `thm:` label, so the
block fails Zod, never loads, and 16 references to it dangle across
`kummer-tower-motivic-galois`, `chi-minus-six-chain`,
`perpetual-obstruction-depth-omega`, `ns-obstruction-tower`,
`substrate-gm-torsion`, `motivic-galois-character`,
`yekutieli-transcendence-shadow`, `geom-yekutieli-alignment`,
`brings-is-qou-verification`, `definition-index` and the two
`qou-motivic-galois-instance` blocks.

Left alone deliberately: the fix direction — relabel and retarget 16
references, or revert the kind — depends on the author's intent, and the
commit is recent.

**Standing count: 47 → 42.**


---

## 5. Follow-on, 2026-08-28: a third inconsistent axiom, and the other half of the structural fix

Written after #5467 and #5505 merged and `main` moved 26,632 commits. Two of
the findings below are corrections to this document.

### 5a. The structural fix put the modules in the tree, not the build

§4h reported the cross-sibling move as the architectural fix. It was half of
one. Nothing inside `QOU.lean`'s import closure imported either new module, so
`lake build QOU` never compiled them and both sat in the `qou-orph` orphan
population; the only thing that had ever type-checked them was the `lean`-direct
run in that PR. Measured with `scripts/lean-orphan-modules.sh`: 986 → 984 NOT
BUILT after wiring them into the root, and `--list` no longer names either.

### 5b. The sibling gate exists — see the correction in §3

The claim that `lean-content-siblings.yml` "does not gate" this population was
wrong about the mechanism. Corrected in place above; the durable half is that
the gate is **diff-scoped by design**, so widening it — not re-enabling it — is
what §4's remedy requires.

### 5c. All four named residuals are closed, and one was not closed by me

| file | was | now | by |
|---|---:|---|---|
| `c5-involution-leibniz-decomposition` | 1 | **exit 0** | this tranche |
| `spectral-half-line` | 6 | **exit 0** | this tranche |
| `hasse-weil-bound` | 24 | **exit 0** | this tranche |
| `frobenius-codim-universal` | 8 | **exit 0** | a sibling agent, `d16f2b6273` on `main` |

`frobenius-codim-universal` was carried in §4f as the one file that improved but
would not close. It closed while this branch was away, sorry-free, 100 errors to
0 — credited here because the standing count would otherwise read as this
tranche's work.

### 5d. The q-zeta structure's `q` was formal where it had to be real

Four of `spectral-half-line`'s six errors and most of `hasse-weil-bound`'s were
a single type error, and it was in the structure rather than in either consumer.
`LocalQZetaFunction.q` was `R_q = LaurentPolynomial ℤ` while `eigenvalues` and
`charPoly` were already `ℂ`-valued, and the block's own `.md` defines the object
as the classical Weil zeta function of Bring's curve over a finite field. `R_q`
carries no order and no norm, so `Z.q > 1`, `(Z.q : ℂ)` and `q ^ ρ` were not
unproved but **unstatable** — neither file could have compiled whatever was done
to its proofs.

Corroboration that this was a known wall: the pre-migration structure carried
`q_pos` **commented out**, annotated `-- (archimedean; not meaningful over
R_q)`. An author wanted exactly that hypothesis and could not state it.

### 5e. A third axiom that proves `False` (the class from §3 is not closed)

`hasse-weil-bound.lean` declared three axioms. Two are properly cited external
results (Weil 1948 §IV–V; Rosen 2002 Ch 5). The third was not:

```lean
axiom eigenvalue_norm_sq_axiom :
    ∀ Z i (_h_cs : ‖Z.eigenvalues i‖^2 ≤ Z.q)
          (_h_fe : ∃ j, Z.eigenvalues j = ↑Z.q / Z.eigenvalues i),
      ‖Z.eigenvalues i‖^2 = Z.q
```

It omits `αᵢ ≠ 0`. The all-zeros datum satisfies every field of the structure
and both hypotheses — `‖0‖² = 0 ≤ q`, and `(q : ℂ)/0 = 0` in Lean, so the
functional equation holds with `j = i` — and the conclusion then reads `0 = q`,
against `q_pos`.

Machine-checked and preserved as a self-contained artifact:
[`artifacts/2026-08-28-eigenvalue-norm-sq-axiom-refutation.lean`](artifacts/2026-08-28-eigenvalue-norm-sq-axiom-refutation.lean)
— exit 0, with `#print axioms axiom_is_false` naming that axiom and the three
standard ones. It carries its own copy of the pre-fix structure on purpose: the
live one now has `eigenvalues_ne_zero`, which makes the witness inadmissible.

Its own comment records the provenance — *"since `lake build` is prohibited for
this task, the exact mathlib lemma names ... cannot be safely verified.
Retaining the axiom fallback"* — which is the general shape to watch for: an
axiom introduced because verification was unavailable, in a file that could not
be verified either.

**Discharged, not deleted.** The paired eigenvalue has norm `q/‖αᵢ‖`, so
Castelnuovo–Severi applied to it gives `q ≤ ‖αᵢ‖²`; with the forward bound that
is equality. Axiom surface 3 → 2, both cited.

### 5f. Two lessons about the measurement, not the corpus

**A silent stop is not a result.** The first whole-population re-sweep died at
100 of 944 with no completion line and was left looking like a partial answer
for an hour. The repo's own long-compute discipline says to assume a crash and
relaunch with logging; that is what it is for.

**Do not grep a tool's prose for its verdict.** The second sweep reported *zero*
failures over 270 files because it classified a run as a skip whenever the
output contained "neutral" — and `lean-verify-siblings.sh` ends **every** run,
pass or fail, with `pass=N neutral-skip=N fail=N`. Two known-genuine failures
were labelled SKIP. Parse the tool's own counters. Caught only because a file
already known to fail was checked against the classifier before the numbers were
believed.

### 5g. Whole-population re-sweep: 73 → 34

Re-measured on this branch (= `main` at `cdbdc84af1` plus this tranche), all
944 content-block siblings, `scripts/lean-verify-siblings.sh` at 6-way
parallelism. Per-file data:
[`2026-08-28-unbuilt-lean-siblings-resweep.tsv`](2026-08-28-unbuilt-lean-siblings-resweep.tsv).

| | count | share |
|---|---:|---:|
| PASS | 907 | 96.1 % |
| FAIL | **34** | 3.6 % |
| NEUTRAL-SKIP (cache-cone, not a defect) | 3 | 0.3 % |

**73 → 34, and most of it was not this arc.** Three closed here
(`c5-involution-leibniz-decomposition`, `spectral-half-line`,
`hasse-weil-bound`), one by a sibling on `main`
(`frobenius-codim-universal`), 22 in #5505, and the remainder across main's
26,632 intervening commits by agents who never saw this bean. The population
also shrank 958 → 944.

**The §4h figure of 42 was never wrong, but it has expired** — it was measured
against a base that has since moved by 26k commits, which is precisely the rule
§4h itself records. Quote 34, with its date and its base.

**One verdict shape worth knowing before reading the TSV.**
`delta-max-uniform-bound` is `FAIL` with **zero** `: error` lines. That is
correct, not a classifier artifact: it is the STALE IMPORT class — it imports
`QOU.MassEndomorphism.JetTower`, which does not exist in the source tree — and
the script detects that instead of running Lean at all. Do not filter the TSV
by error count.

The 34 are not triaged here. Shape of the tail: 11 files at a single error, 11
at two, and 8 at five, so the distribution is still mostly small — but §4's
warning stands that these counts are floors, since Lean halts at the first
parse error and reports nothing behind it.
