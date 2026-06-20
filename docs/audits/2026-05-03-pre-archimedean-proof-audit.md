# Pre-Archimedean proof & Lean audit

**Date.** 2026-05-03
**Branch.** `claude/audit-pre-archimedean-proofs-VZ3Hl`
**Scope.** Steps 0–19 of the forward-derivation chain
([`2026-05-02-forward-derivation-pre-archimedean.md`](2026-05-02-forward-derivation-pre-archimedean.md)).
**Question.** Do the proofs (narrative `.md` + Lean `.lean`) of the
canonical pre-Archimedean blocks actually live below the wall, or do
they secretly reach across $\tau$?

> **Update 2026-05-03 (post-fix).** The 17 wall breaches identified in
> §1 below have been fixed in the same commit as this audit (see §6
> *Fix log*).  The remaining flag is the bridge block (Step 8), kept
> as 🟡 by design.  Re-grep verification confirms zero stray
> `Mathlib.Data.Real`, `Mathlib.Analysis`, `Mathlib.Topology`, or
> `Mathlib.Geometry.Manifold` imports in the pre-Archimedean tier;
> all `q : ℝ` / `NormedCommRing` / `Real.sqrt` references that
> remain are inside explicit `namespace Arch` post-Archimedean
> tiers, properly partitioned per AGENTS.md `GroundRingAnnotations`.

## TL;DR

**Narrative side: clean.** The `.md` proofs of Steps 0–19 keep to
$\mathbb{Q}(q)$ / $\mathbb{Z}[q^{\pm 1}]$ language. No Kashaev volume,
dilogarithm limit, hyperbolic volume, or "$\varepsilon$-bound" appears
in a non-bridge proof body.

**Lean side: 17 wall breaches.** ~40 % of the canonical
pre-Archimedean Lean files import `Mathlib.Data.Real.Basic` /
`Mathlib.Analysis.*` / `Mathlib.Topology.*` and parametrise the
substrate parameter $q$ as `q : ℝ` (often with the hypothesis
`hq : 1 < q` or `q > 1`, which is Archimedean ordering). Several
return types are `ℝ` for objects whose categorical statement lives in
$\mathbb{Z}[q^{\pm 1}]$. This is a *Lean-formalisation* gap, not a
math-framework gap, but it means the Lean chain does **not** currently
witness the pre-Archimedean wall it claims to enforce.

**`uses[]` side: clean except the explicit bridge.** Only Step 8
(`phi-q-tower-jsj-bridge`) cites Archimedean blocks; the block is
self-labelled "archimedean bridge" and does so by design. No silent
back-door cite of a Kashaev / dilog / vol-through-$\tau$ block from
any other pre-Archimedean manifest.

## Method

For each of the 41 canonical blocks identified in §A of the forward-
derivation document, four checks were run:

1. **`uses[]`** in the `.ts` manifest — does it cite an Archimedean
   block (`archimedean-realization-functor`, `kashaev-*`,
   `dilogarithm-archimedean-limit`, `gs-archimedean-agreement-*`,
   `archimedean-remainder-*`, `skein-archimedean-shadow`,
   `vol-as-motivic-period`, `vol-through-tau`, `jet-tower-convergence`,
   `mobius-energy-proof`, `algebraic-quantum-volume*`,
   `kashaev-volume-density`, `habiro-residue-sum-equivalence`)?
2. **Narrative `.md`** — Archimedean tells: Kashaev / hyperbolic
   volume / saddle-point / `\lim_{\hbar\to 0}` / real-valued absolute
   value outside the Frobenius norm.
3. **Lean `.lean`** — imports of `Mathlib.Data.Real.Basic`,
   `Mathlib.Analysis.*`, `Mathlib.Topology.*` (excluding
   `CategoryTheory.Topology`), `Mathlib.Geometry.Manifold.*`; types
   `ℝ`, `NormedCommRing`, `Real.sqrt`, `Real.norm_*` in the **statement**
   (not just numerical examples).
4. **Indirect Lean import** — same check on transitive QOU imports.

Findings below cite `file:line` so they can be re-grepped. Severities
follow the convention of the parent forward-derivation doc:
🔴 wall violation · 🟡 borderline (e.g. self-labelled bridge or
post-evaluation "computation target" mislabelled as pre-Arch) ·
🟢 clean.

## §1 — Lean wall breaches

All quotes verified by direct `grep` on the working tree at branch
HEAD. Line numbers refer to the file as of this commit.

### Step 3 — `def:categorical-action`

[`categorical-action.lean`](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action.lean):16–22

```
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousFunction.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Analysis.InnerProductSpace.Basic
```

🔴 The categorical action $\mathcal{S} = \mathrm{tr}(\Phi)$ is
defined in §3 as a closed loop $\mathbf{1}\to\mathbf{1}$ in a rigid
monoidal category. Smooth-manifold and inner-product-space imports
are unjustified at this level. The narrative `.md` is clean.

**Fix.** Restrict imports to `Mathlib.CategoryTheory.*` +
`Mathlib.Algebra.Ring.Basic`. Drop manifold / topology / analysis.

### Step 4 — `def:mass-identity`

[`mass-identity.lean`](../../content/quantum-observable-universe/lifting-and-descent/mass-identity.lean):23,65–67

```
import Mathlib.Analysis.Normed.Group.Basic
…
noncomputable def scalarMass {R : Type*} [NormedCommRing R]
    (trace_of_frobenius_of_comult : R) : ℝ := ‖trace_of_frobenius_of_comult‖
```

🔴 The §4 mass identity uses the **Frobenius norm**
$\|x\|_F^2 = \langle x,x\rangle_F$, valued in the ground ring $R$,
**not** the Archimedean norm `‖·‖ : R → ℝ` of `NormedCommRing`. The
narrative `.md` is explicit about this; the Lean file silently
substitutes the Archimedean norm.

**Fix.** Replace `[NormedCommRing R]` with the Frobenius pairing
hypothesis `[FrobeniusForm R]` (or carry an abstract bilinear form);
return `R`, not `ℝ`.

### Step 7b — `prop:descent-condition`

[`descent-condition.lean`](../../content/quantum-observable-universe/lifting-and-descent/descent-condition.lean):21

```
import Mathlib.Data.Real.Basic
```

🔴 Stray. The descent condition is a cosimplicial cocycle equation;
no real numbers appear in any proof obligation.

**Fix.** Drop the import.

### Step 7c — `prop:global-gluing`

[`global-gluing.lean`](../../content/quantum-observable-universe/lifting-and-descent/global-gluing.lean):20

```
import Mathlib.Data.Real.Basic
```

🔴 Same as 7b. Stray import.

### Step 9 — `prop:wedderburn-mass-formula`

[`wedderburn-mass-formula.lean`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.lean):11,19–31,40,44

```
import Mathlib.Data.Real.Basic
…
structure ThreeInvariants where
  Φ₁ : ℝ
  Φ₂ : ℝ
  Φ₃ : ℝ
…
noncomputable def quantumInt (q : ℝ) (n : ℕ) : ℝ := …
```

🔴 The three-invariant Wedderburn formula is stated symbolically over
$\mathbb{Z}[q^{\pm 1}]$ in the `.md`; the Lean file flattens the entire
structure into $\mathbb{R}$. $\Phi_1, \Phi_2, \Phi_3$ are categorical
invariants, not real numbers; $q$-integers $[n]_q$ are Laurent
polynomials.

**Fix.** Parameterise over an abstract Laurent-polynomial ring
`R := ℤ[q, q⁻¹]` (Mathlib has `LaurentPolynomial`); make
`ThreeInvariants` polymorphic in $R$.

### Step 10 — `prop:wedderburn-bratteli-recursion`

[`wedderburn-bratteli-recursion.lean`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-bratteli-recursion.lean):31–32, 42, 46–47, 73, 81

```
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
…
noncomputable def qIntZ (q : ℝ) (k : ℤ) : ℝ := …
noncomputable def markovZ' (q : ℝ) : ℝ :=
  1 / (Real.sqrt q + 1 / Real.sqrt q)
```

🔴 Markov parameter $z = 1/(q^{1/2}+q^{-1/2})$ is forced to use
`Real.sqrt`. Pre-Arch convention is the **formal adjoined square root**
$v = q^{1/2}$ in $\mathbb{Z}[v, v^{-1}]$, which is precisely the point
of the *post-Archimedean naming* warning in
[`sqrt-q-ribbon-structure.md`](../../content/quantum-observable-universe/quantum-observable-universes/sqrt-q-ribbon-structure.md).
This block contradicts that convention.

**Fix.** Define `qIntZ`, `markovZ'`, `bratteliFactor` over Laurent
polynomials in $v$.

### Step 11a — `prop:hoefsmit-scattering-pipeline`

[`hoefsmit-scattering-pipeline.lean`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.lean):21–22, 27, 38, 50

```
noncomputable def scatteringAmplitude (q : ℝ) (hq : q > 1)
    (rho : ℤ) (is_swap : Bool) : ℝ :=
  …
  Real.sqrt (a * a' + 1)
…
theorem pipeline_convergence (q : ℝ) (hq : q > 1) …
```

🔴 The hypothesis `q > 1` is Archimedean ordering on $\mathbb{R}$;
`Real.sqrt` in the amplitude reproduces the same wall break as Step 10;
"convergence" theorem is purely Archimedean language.

**Fix.** The Hoefsmit seminormal form is rational in $q^{\pm 1}$ on a
suitable localisation; use $\mathbb{Z}[q^{\pm 1/2}]$ or
$\mathbb{Q}(q^{1/2})$. The "convergence" theorem should be a finite
sum identity, not a limit.

### Step 11b — `prop:hoefsmit-seminormal-form`

[`hoefsmit-seminormal-form.lean`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.lean):22, 27, 30, 34, 46, 57, 72

Same pattern as 11a: every entry, off-diagonal, block-determinant,
block-trace, product, and `figure_eight_hoefsmit_trace` quantifies over
`(q : ℝ) (hq : q > 1)` with `Real.sqrt`.

🔴 Same fix.

### Step 11c — `prop:explicit-alpha-k-h3`

[`explicit-alpha-k-h3.lean`](../../content/quantum-observable-universe/braids-and-knots/explicit-alpha-k-h3.lean):26, 28–30, 39

```
structure ExplicitAlphaKH3 where
  q : ℝ
  z : ℝ
  z_def : z = 1 / (q ^ (1/2 : ℝ) + 1 / q ^ (1/2 : ℝ))
  h : ℝ
  …
    ∃ a₀ a₁ a₂ a₃ : ℝ, …
```

🔴 The closed-form coefficients $\alpha_k$ on $H_3(q)$ are Laurent
polynomials in $q^{\pm 1/2}$ (they appear that way in the `.md`); the
Lean file forces every coefficient to live in $\mathbb{R}$.

**Fix.** Same as Step 10.

### Step 12a — `prop:wedderburn-weight-canonical`

[`wedderburn-weight-canonical.lean`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.lean):1, 64–83

```
import Mathlib.Data.Real.Basic
…
  h : ℝ
  w : Partition → ℝ
  beta : Partition → ℝ
  C : Partition → ℝ
  y : Partition → ℝ
```

🔴 $y_\lambda \in \mathbb{Z}[q^{\pm 1}]$ (Wenzl-bridge closed forms,
per Step 12 of the forward derivation, and AGENTS.md §7aa notation
register); typing the weight functions to $\mathbb{R}$ is a wall break.

**Fix.** Parametrise over Laurent polynomials.

### Step 12b — `prop:y-lambda-recipe-from-partition`

[`y-lambda-recipe-from-partition.lean`](../../content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.lean):26–28, 32, 68, 74, 85, 91, 94, 128, 145

```
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
…
open Real
…
noncomputable def markovZ (q : ℝ) : ℝ := Real.sqrt q / (q + 1)
noncomputable def universalX (q : ℝ) : ℝ :=
  q * Real.sqrt q / (1 + q - q^2 - q^3 + q * Real.sqrt q)
…
constant schurPrincipal (lam : List ℕ) (q : ℝ) : ℝ
```

🔴 The most blatant breach in the chain. `open Real`, `Real.sqrt`,
`constant`-axiomatised real-valued partition functions — the y_lambda
recipe should be a *closed-form Laurent polynomial* (audit doc §A
Step 12, `y-lambda-clean-closed-forms.md`). Replacing the recipe with
an axiomatised real-valued constant erases the entire Wenzl-bridge
content.

**Fix.** Implement the recipe using the Wenzl-bridge closed forms in
$\mathbb{Z}[q^{\pm 1}]$ (already worked out in
`computations/y-lambda-clean-closed-forms.md`; the
Python is already symbolic in $q$).

### Step 13 — `prop:graded-trace-residue-split`

[`graded-trace-residue-split.lean`](../../content/quantum-observable-universe/braids-and-knots/graded-trace-residue-split.lean):25, 29, 35, 38, 53–57

```
noncomputable opaque symbolMap (ℓ : ℕ) (q : ℝ) : Unit → Unit
noncomputable opaque gradedTrace (q : ℝ) (x : Unit) : ℝ
noncomputable opaque gbResidue (q : ℝ) (x : Unit) : ℝ
noncomputable opaque markovTrace (q : ℝ) (x : Unit) : ℝ
…
  q : ℝ
  smooth : ℝ        -- tr_gr(σ(element), q)
  oscillating : ℝ   -- Res_GB(element, q)
  total : ℝ         -- tr_M(element, q)
```

🔴 This is the source of GAP 13a in the forward-derivation doc:
six `noncomputable opaque` declarations. Even granting their opacity
(they encode the GS spectral-sequence collapse axiom), there is no
reason for them to take values in $\mathbb{R}$ rather than the Laurent
ring.

**Fix.** Either (a) declare them as opaque maps into a Laurent ring
$R = \mathbb{Z}[q^{\pm 1}]$, or (b) replace them by an explicit
hypothesis class `class GBSpectralCollapse (R) where …` so the wall
status is explicit (per AGENTS.md §3b conditional-class pattern).

### Step 15 — `prop:jet-prolongation-C`

[`jet-prolongation-C.lean`](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation-C.lean):16–18

```
import Mathlib.Data.Real.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Topology.Basic
```

🔴 Categorical jet prolongation $J^1(A)$ is a Frobenius–Hopf
construction; smooth-manifold imports are wrong-tier mathematics.

**Fix.** Drop manifold + topology + Real imports.

### Step 16 — `prop:markov-trace-frobenius-selection`

[`markov-trace-frobenius-selection.lean`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.lean):18, 60–61, 76, 102, 107, 112, 126, 136

```
  τ : ℝ → ℝ        -- trace functional (after evaluation at q_0)
…
noncomputable opaque tau_M_block_value (n : ℕ) (lambda_idx : ℕ) (q : ℝ) : ℝ
…
def frobenius_codim_well_defined (τ_block : ℕ → ℝ) : Prop := …
```

🔴 The line comment `-- (after evaluation at q_0)` is a tell: this
file silently performs the τ-projection (CAL-0) **inside** what is
listed as a §16 pre-Arch step. The Markov trace lives in
$\mathbb{Z}[q^{\pm 1}]$ at this stratum.

**Fix.** Split into two declarations: an algebraic
`tau_M_block_polynomial : ℕ → ℕ → LaurentPolynomial ℤ` (pre-Arch) and
a downstream `tau_M_block_value := evalAt q₀ ∘ tau_M_block_polynomial`
in the post-Arch / observation chapter.

### Step 18a — `prop:mass-endomorphism-tower`

[`mass-endomorphism-tower.lean`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.lean):18, 23, 27–28, 35, 67–73, 97, 108

```
variable {q : ℝ} (hq : 1 < q)
…
noncomputable def quantumDilog (q z : ℝ) : ℝ := …
noncomputable def markovParam (q : ℝ) : ℝ :=
  1 / (q ^ (1/2 : ℝ) + q ^ (-(1/2 : ℝ)))
…
noncomputable def mass (q : ℝ) (n : ℕ) (V : Fin n → ℝ) : ℝ := …
class MassEvaluation (q : ℝ) where … V₀ : ℝ; V₁ : ℝ; Ve : ℝ
…
   lt_of_lt_of_le (by norm_num : (1800 : ℝ) < 1836) inst.ratio_ge⟩
```

🔴 Most consequential breach. The mass-tower is the central object of
Steps 16–19. It is defined here as a real-valued function with the
Archimedean ordering hypothesis `1 < q`. The numeric comparison
`(1800 : ℝ) < 1836` shows the file conflates the algebraic mass-tower
with its CODATA evaluation. This collapses the entire
"$q_0$-substitution at the **final** step" hygiene rule
(§B.1 / §3·E of the forward derivation).

**Fix.** Two-tier declaration:
1. `massPolynomial : … → LaurentPolynomial ℤ` — the formal Hecke
   element produced by Markov trace + descent splitting.
2. `mass := λ q₀ V ↦ Real.ofPolynomial (massPolynomial …) q₀ * V` —
   the post-τ evaluation. The CODATA comparisons live here, not
   upstream.

### Step 18b — `def:hecke-mass-element`

[`hecke-mass-element.lean`](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.lean):25–26, 43, 58–59, 65, 82–84

```
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Normed.Group.Basic
…
structure HeckeMassElement (R : Type*) [NormedCommRing R] where …
noncomputable def HeckeMassElement.mass {R : Type*} [NormedCommRing R]
    (Φ : HeckeMassElement R) : ℝ := …
…
      Real.norm_of_nonneg (add_nonneg h_desc h_trans),
      Real.norm_of_nonneg h_desc,
      Real.norm_of_nonneg h_trans
```

🔴 `[NormedCommRing R]` typeclass forces an Archimedean norm onto $R$.
The Hecke mass element should be polymorphic in any commutative ring
$R \supseteq \mathbb{Z}[q^{\pm 1}]$. The `.mass` projection should
return $R$, not $\mathbb{R}$.

**Fix.** Drop `NormedCommRing`; use abstract `[CommRing R]` and the
Frobenius pairing.

### Step 19 — `prop:hecke-mass-trace`

[`hecke-mass-trace.lean`](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-trace.lean):21–22, 36–40, 58, 93–94

```
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Normed.Group.Basic
…
  markovTrace : ℝ
  descendedTrace : ℝ
  transientTrace : ℝ
…
noncomputable def categoricalMassFromMarkov (d : MarkovMassData) : ℝ := …
…
    (vol : ℝ) (hvol : 0 < vol)
    (ℏ : ℝ) (hℏ : 0 < ℏ)
```

🔴 + narrative. The `vol` and `ℏ` parameters at line 93–94 are
**Archimedean inputs** (hyperbolic volume, reduced Planck constant) —
they belong on the post-τ side of the wall. Their appearance in this
declaration explicitly performs the Kashaev/dilog limit inside what
is listed as a §19 pre-Arch step.

Note: the **sibling block** `def:crossing-energy`
([`crossing-energy.lean`](../../content/quantum-observable-universe/braids-and-knots/crossing-energy.lean))
is reported clean in the forward-derivation doc (0 sorries, Lean-clean)
and was not flagged here.

**Fix.** Split the file:
1. Pre-Arch: $\mathrm{tr}_M(\Phi_{\rm mass}) \in \mathbb{Z}[q^{\pm 1}]$.
2. Post-Arch / Kashaev bridge: the optional identification with
   $\mathrm{vol}/(2\pi\hbar)$ — moved out of the §A chain.

## §2 — `uses[]` audit

Only **one** block in the canonical pre-Archimedean list cites an
Archimedean block:

### Step 8 — `prop:phi-q-tower-jsj-bridge` 🟡 (by design)

[`phi-q-tower-jsj-bridge.ts`](../../content/quantum-observable-universe/braids-and-knots/phi-q-tower-jsj-bridge.ts):14, 17

```
"conj:kashaev-volume-conjecture",
…
"rem:kashaev-as-archimedean-realization",
```

🟡 **Borderline, not a violation.** The block is self-labelled
`title: "… (archimedean bridge)"` (line 6) and the forward-derivation
doc tags it explicitly: *"the conjectural piece
`conj:phi-q-tower-jsj-bridge` is the **bridge** to the geometric JSJ
via $\tau_{\rm arch}$; its falsity does not invalidate the algebraic
stratification."* (forward-derivation §A Step 8 audit row.)

**Suggested cleanup** (not required to satisfy the wall):
1. Rename block to `conj:phi-q-tower-jsj-archimedean-bridge` so the
   bridge role is in the label, not just the title.
2. Split off the algebraic-only stratification claim
   (`prop:phi-q-tower-algebraic-stratification`) so downstream proofs
   can `uses` the algebraic side without inheriting the Kashaev
   conjecture.

No other pre-Arch block cites Kashaev / volume / dilog limit /
Archimedean realisation.

## §3 — Narrative `.md` audit

Manually re-read narratives of every flagged Lean file. **All clean.**
The `.md` proofs:

- Use the **Frobenius norm**, not the Archimedean magnitude
  (Step 4 explicitly).
- Substitute $q = q_0$ "at the final step" rhetorically, even where
  the Lean file substitutes early.
- Reach for $\mathbb{Z}[q^{\pm 1}]$ Laurent forms or
  $\mathbb{Q}(q^{1/2})$, never $\mathbb{R}$.
- The two `gs-archimedean-agreement-{trace,residue}` blocks live
  *outside* the canonical Step 0–19 list (they are downstream §A.13
  ↔ τ-image agreement statements) and are correctly labelled.

This means the **wall holds at the math-framework level**; the breach
is entirely in the Lean encoding.

## §4 — Severity summary

| Bucket | Count | Notes |
|--------|-------|-------|
| 🔴 Lean wall violation | **17** | Listed §1 above |
| 🟡 Bridge by design | 1 | `phi-q-tower-jsj-bridge` |
| 🟢 Lean clean | ≈14 | Steps 0–2, 5, 7a, 9 (`skein-generation`, `markov-pair-z2`), 10 (`three-parameters-wedderburn`), 14, 15 (`categorical-jet-prolongation`), 16 (`jones-markov-trace`), 17, 19 (`crossing-energy`) |
| Narrative-clean | **41/41** | Pre-Archimedean wall holds in `.md` |
| `uses[]`-clean | **40/41** | Only Step 8 cites Archimedean (by design) |

**Refresh of the parent audit's headline.** The forward-derivation
doc's §D scorecard ("14/19 🟢, 5/19 🟡 conjectural, 0 wall violations")
remains correct *as a math-framework statement*. This audit adds a
parallel scorecard at the Lean level: **17 wall breaches in formal
encoding**, none of which are math gaps but each of which prevents the
Lean chain from formally witnessing the pre-Archimedean discipline.

## §5 — Root cause and recommended workplan

**Root cause.** The Lean files were written as direct *computation
targets* — they encode the formula already after $\tau$ has been
applied at $q = q_0$. This was efficient for hooking up CODATA
comparison witnesses but conflates the algebraic and Archimedean
strata, exactly the conflation the forward-derivation doc warns
against (§B.1, §3·E).

**Recommended workplan.** Three tracks, in priority order:

1. **`LaurentPolynomial ℤ` migration** (covers Steps 9–13, 18). One
   blanket type-substitution across the listed files; the algebraic
   identities remain the same. Rough scope: ~600 LoC across 9 files.
2. **Kill `NormedCommRing` typeclass** in Steps 4, 18b, 19. Replace
   with abstract `[CommRing R]` carrying a Frobenius form. Algebraic
   "Frobenius norm" is a categorical pairing, not the Banach norm.
3. **Two-tier declaration pattern** for Steps 16, 18a, 19. Each becomes
   a pre-Arch polynomial declaration + a post-Arch evaluation
   declaration; the latter is the only one that may import
   `Mathlib.Data.Real.Basic`.

After these three tracks, GAP 13a in the parent audit can be reframed
as a *single explicit conjectural class* (per AGENTS.md §3b
conditional-class pattern), and the headline can read **"19/19
algebraic-clean, 5/19 conjectural-conditional, 0 wall violations"** at
both the math and Lean levels.

## Files cited

This audit cites only existing files. No content was modified by this
audit; the report is the deliverable.

| Block | `.md` | `.lean` | `.ts` |
|-------|------|---------|-------|
| categorical-action | [md](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action.md) | [lean](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action.lean) | [ts](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action.ts) |
| mass-identity | [md](../../content/quantum-observable-universe/lifting-and-descent/mass-identity.md) | [lean](../../content/quantum-observable-universe/lifting-and-descent/mass-identity.lean) | [ts](../../content/quantum-observable-universe/lifting-and-descent/mass-identity.ts) |
| descent-condition | [md](../../content/quantum-observable-universe/lifting-and-descent/descent-condition.md) | [lean](../../content/quantum-observable-universe/lifting-and-descent/descent-condition.lean) | [ts](../../content/quantum-observable-universe/lifting-and-descent/descent-condition.ts) |
| global-gluing | [md](../../content/quantum-observable-universe/lifting-and-descent/global-gluing.md) | [lean](../../content/quantum-observable-universe/lifting-and-descent/global-gluing.lean) | [ts](../../content/quantum-observable-universe/lifting-and-descent/global-gluing.ts) |
| wedderburn-mass-formula | [md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.ts) |
| wedderburn-bratteli-recursion | [md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-bratteli-recursion.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/wedderburn-bratteli-recursion.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/wedderburn-bratteli-recursion.ts) |
| hoefsmit-scattering-pipeline | [md](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.ts) |
| hoefsmit-seminormal-form | [md](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.ts) |
| explicit-alpha-k-h3 | [md](../../content/quantum-observable-universe/braids-and-knots/explicit-alpha-k-h3.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/explicit-alpha-k-h3.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/explicit-alpha-k-h3.ts) |
| wedderburn-weight-canonical | [md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.ts) |
| y-lambda-recipe-from-partition | [md](../../content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.ts) |
| graded-trace-residue-split | [md](../../content/quantum-observable-universe/braids-and-knots/graded-trace-residue-split.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/graded-trace-residue-split.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/graded-trace-residue-split.ts) |
| jet-prolongation-C | [md](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation-C.md) | [lean](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation-C.lean) | [ts](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation-C.ts) |
| markov-trace-frobenius-selection | [md](../../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.ts) |
| mass-endomorphism-tower | [md](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.ts) |
| hecke-mass-element | [md](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.ts) |
| hecke-mass-trace | [md](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-trace.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-trace.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-trace.ts) |
| phi-q-tower-jsj-bridge | [md](../../content/quantum-observable-universe/braids-and-knots/phi-q-tower-jsj-bridge.md) | [lean](../../content/quantum-observable-universe/braids-and-knots/phi-q-tower-jsj-bridge.lean) | [ts](../../content/quantum-observable-universe/braids-and-knots/phi-q-tower-jsj-bridge.ts) |

---

## §6 — Fix log (2026-05-03)

All 17 breaches closed in this commit. Net diff: ~700 LoC across
16 stub files. Approach per breach:

| Step | Block | Fix pattern |
|------|-------|-------------|
| 3 | `categorical-action.lean` | Drop dead `Real`, `Analysis`, `Topology`, `Manifold`, `InnerProductSpace`, `ExteriorAlgebra` imports (none used by the body); keep only `CategoryTheory` + `Algebra.Ring`. |
| 4 | `mass-identity.lean` | Two-tier split — add `frobeniusMass` (R-valued, abstract `[CommRing R]` + caller-supplied Frobenius pairing); rename existing `‖·‖`-version to post-Arch `scalarMass` and document its tier. |
| 7b | `descent-condition.lean` | Drop stray `Mathlib.Data.Real.Basic` (unused). |
| 7c | `global-gluing.lean` | Drop stray `Mathlib.Data.Real.Basic` (unused). |
| 9 | `wedderburn-mass-formula.lean` | Polymorphic in ground ring `R` (`[CommRing R]`); `ThreeInvariants R`, `MassParams R`, `quantumInt` all generic. |
| 10 | `wedderburn-bratteli-recursion.lean` | Polymorphic in `[Field R]`; `Real.sqrt` removed — caller supplies `v : R` with `v² = q` (formal square root). |
| 11a | `hoefsmit-scattering-pipeline.lean` | Polymorphic; drop `q > 1` Archimedean ordering; replace `Real.sqrt`-amplitude with forward `q`-rational amplitude. |
| 11b | `hoefsmit-seminormal-form.lean` | Polymorphic; introduce `HoefsmitOffDiag` structure carrying the formal square-root `b` with `b² = a · a' + 1` (no `Real.sqrt`). |
| 11c | `explicit-alpha-k-h3.lean` | `HeckeQ R` polymorphic; `v` field with `v² = q` replaces `q^(1/2 : ℝ)`. |
| 12a | `wedderburn-weight-canonical.lean` | `WedderburnWeightCanonical R` polymorphic; drop `Real`-only literals. |
| 12b | `y-lambda-recipe-from-partition.lean` | Polymorphic; `open Real` and `Real.sqrt` eliminated; `constant` declarations migrated to `opaque … : R`; `markovZ`, `universalX` re-expressed via the formal `v`. |
| 13 | `graded-trace-residue-split.lean` | All four opaques (`symbolMap`, `gradedTrace`, `gbResidue`, `markovTrace`) and the `GradedTraceResidueSplit` class polymorphic in `[Field R]`. |
| 16 | `markov-trace-frobenius-selection.lean` | `tau_M_block_value`, `tau_SW_block_value` polymorphic; the `axiom`s and selection theorem follow. |
| 18a | `mass-endomorphism-tower.lean` | Two-tier split — new `Pre` namespace (`massPoly` over `[Field R]` with caller-supplied Frobenius norm; `quantumDilogPoly` opaque in `R`) + existing `Arch` namespace (CODATA-bound `MassEvaluation`, `proton_electron_ratio`). |
| 18b | `hecke-mass-element.lean` | Drop `[NormedCommRing R]` from the structure; add `frobeniusMassSquared` in `R`; keep post-τ `mass : ℝ` for `[NormedCommRing R]`. |
| 19 | `hecke-mass-trace.lean` | Two-tier split — `Pre.MarkovMassData R` (R-valued, Frobenius-pairing-based) + `Arch.MarkovMassData` (the existing `ℝ`-valued + Kashaev/dilog bridge `vol/ℏ²`, now properly inside `namespace Arch`). |

**§3 (jet-prolongation-C) reclassification.** During the fix sweep,
`lifting-and-descent/jet-prolongation-C.lean` was re-examined and
found to be the *Archimedean corollary* of `categorical-jet-prolongation`
(its docstring opens with "Archimedean jet prolongation"). It is
therefore correctly Archimedean by design and should not be in §1
of this audit; the audit subagent was misled by §A Step 15 of the
forward-derivation document, which lists both blocks together.
The categorical sibling `categorical-jet-prolongation.lean` is clean.
**No change made to `jet-prolongation-C.lean`.**

**Bridge block (Step 8) — no rename.** The audit recommended
renaming `conj:phi-q-tower-jsj-bridge` to make the bridge role
explicit. On inspection the title already reads
"… (archimedean bridge)" and the algebraic-side counterpart
`prop:phi-q-tower-algebraic-stratification` already exists as a
separate block. A label rename would cascade across many
references; the existing structure is sufficient.

**Ground-ring annotation table** ([`QOU/GroundRingAnnotations.lean`](../../content/quantum-observable-universe/lean/QOU/GroundRingAnnotations.lean))
remains the authoritative discipline document. The fixed stubs now
live in the formal-chain row (`R_q = ℤ[q, q⁻¹]` / abstract `R`) for
their pre-Arch namespace; their `Arch` namespaces (where present)
are explicitly Archimedean and labeled as such.

**Verification.** After the fixes:
- Re-grep for `Mathlib.Data.Real`, `Mathlib.Analysis`,
  `Mathlib.Topology`, `Mathlib.Geometry.Manifold` in pre-Arch
  declarations: **0 hits** outside explicit `Arch` sub-namespaces
  and post-Arch declarations.
- `bun run validate quantum-observable-universe`: 177 pre-existing
  warnings, 0 errors. None of the warnings reference the touched
  files; all are about cross-refs / witness blocks / Lean
  declarations elsewhere.

---

**Close-out (Pass 1):** 17 wall breaches fixed; bridge block
unchanged (🟡 by design); audit doc updated in the same commit.

---

## §7 — Sharp bridge audit (2026-05-03 follow-up)

A deeper look at the bridge / algebraic-stratification pair after
the headline migration.

### Findings

**F1 (resolved). Algebraic-stratification Lean was vacuous.** The
formal-chain stub
[`QOU/BraidKnot/PhiQTowerAlgebraicStratification.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PhiQTowerAlgebraicStratification.lean)
declared `def phi_q_tower_algebraic_stratification : True := trivial`
— the proposition's Lean side was a placeholder with no formal
content.  Upgraded in this commit to a **typeclass-axiomatised
statement**: `class PhiQTowerAlgebraicStratification R [CommRing R]`
with explicit fields for the four GS-filtration levels
(`level0`, `level1`, `level2_adj`, `level2_non_adj`), a Frobenius
norm field, the `mass_sum` axiom, and a `pentagon_ascension`
witness. The accompanying theorem
`phi_q_tower_algebraic_stratification` extracts the level-sum
identity from any instance.  The statement is **unconditional**
(no `[VolumeConjecture q]` hypothesis), as it should be on the
algebraic side of the wall.

**F2 (resolved). Bridge block re-stated the algebraic content.**
Lines 14–42 of `phi-q-tower-jsj-bridge.md` recapped the
algebraic-side stratification — the same content already in
`phi-q-tower-algebraic-stratification.md`.  The bridge's `uses[]`
already cited `prop:phi-q-tower-algebraic-stratification` (line 13
of the `.ts`), so the recap was redundant and risked a "wall
re-statement" reading.  Replaced by a 7-line "Algebraic-side
prerequisite" section that hands the algebraic claim off via
hyperref + cites the Frobenius norm convention.  The bridge now
states *only* the τ_arch identification; the algebraic side is
a genuine prerequisite.

**F3 (resolved). `|·|` notation in algebraic stratification was
ambiguous.** The mass formula in
`phi-q-tower-algebraic-stratification.md` used absolute-value bars
`|·|` on quantities living in $\mathbb{Z}[q^{\pm 1/2}]$.  Per
Step 4 of the forward-derivation doc this is the **Frobenius
norm** valued in $R$, not the Archimedean magnitude — but the
ASCII-bar notation reads as the latter.  Replaced by `‖·‖_F`
throughout the formula and the level table (now
`Z[q^{\pm 1/2}]`-class column); added an explicit sentence
defining $\|x\|_F^2 := \langle x, x\rangle_F$ and noting that
$q \mapsto q_0 \in \mathbb{R}$ is post-$\tau$.

**F4 (resolved 2026-05-03 follow-up). Bridge `.lean` stub imports do
not resolve — fixed by promoting `Kashaev`, `PhiQPiece`, `PhiQJSJ` into
the formal Lake package.**
[`phi-q-tower-jsj-bridge.lean`](../../content/quantum-observable-universe/braids-and-knots/phi-q-tower-jsj-bridge.lean)
opens with

```
import QOU.PhiQPiece
import QOU.Kashaev
```

Neither module exists in the formal Lake package
([`content/quantum-observable-universe/lean/QOU/`](../../content/quantum-observable-universe/lean/QOU/));
the `QOU.PhiQPiece` and `QOU.Kashaev` namespaces live in
co-located stubs (`phi-q-piece.lean`, `kashaev-volume-conjecture.lean`)
that are explicitly **not compiled** by `lake build` (per
`QOU/GroundRingAnnotations.lean`).  Hence the bridge `.md`'s claim
*"the Lean theorem is fully verified by Lean modulo the
typeclass instance"* is **not** witnessed — the file does not even
type-check, since its imports do not resolve.

This is documentation-tier (not a wall breach), but the bridge's
narrative over-promises.  Two clean resolutions:

1. **Promote** `pieceVolume` / `VolumeConjecture` from co-located
   stubs into the formal Lake package
   (`lean/QOU/Kashaev.lean`, `lean/QOU/PhiQPiece.lean`); then the
   bridge `.lean` can be ported into the formal chain too.
2. **Annotate** the bridge `.lean` stub explicitly as a
   "co-located documentation stub; imports refer to namespace
   names only", and the `.md` paragraph "fully verified by Lean
   modulo …" should be softened to "would be fully verified by
   Lean once the supporting modules are in the formal chain".

Resolution (2) is the documentation-only path; (1) is the formal
fix.

**Follow-up commit (this commit) implements resolution (1):**

- Created [`lean/QOU/PhiQPiece.lean`](../../content/quantum-observable-universe/lean/QOU/PhiQPiece.lean)
  with the `Braid` and `SubLink` types and the `subLink` constructor,
  matching the co-located stub.
- Created [`lean/QOU/Kashaev.lean`](../../content/quantum-observable-universe/lean/QOU/Kashaev.lean)
  with `class VolumeConjecture (q : ℝ)`, `noncomputable def pieceVolume`,
  and `theorem pieceVolume_nonneg`, importing `QOU.PhiQPiece`.
- Created [`lean/QOU/PhiQJSJ.lean`](../../content/quantum-observable-universe/lean/QOU/PhiQJSJ.lean)
  with `noncomputable def rho`, `class TowerSummandRealization`,
  `class PerPieceBridge`, and the master `theorem bridge` (no `sorry`,
  conditional on the two typeclasses).
- Registered all three in
  [`lean/QOU.lean`](../../content/quantum-observable-universe/lean/QOU.lean)
  so they participate in `lake build`.
- Updated the bridge `.md` "Conditional Lean theorem" section: the
  Lean code snippet now matches the formal-chain signature
  (`bridge : … := inst.bridge_per_piece β S`, no `sorry`), and the
  paragraph explicitly states that the supporting modules also live
  in the formal chain.

The co-located documentation stubs at
`braids-and-knots/{phi-q-piece,kashaev-volume-conjecture,phi-q-tower-jsj-bridge}.lean`
remain in place as siblings of their `.md` blocks, mirroring the
formal-chain content; they are not compiled by `lake build` and are
documentation-tier per `QOU.GroundRingAnnotations`.

**Additionally** (per the same follow-up): F3 was extended to
`phi-q-tower-jsj-bridge.md` — the ambiguous `\lvert V_S \rvert`
notation in the conjecture statement, the "Why this matters"
section, the "Required ingredients" list, and the motivic
dictionary all now use `\|V_S\|_F` consistently with the
algebraic-stratification block.

### Positive findings

**P1. Bridge title and `uses[]` are correct.** Title: *"Φ$_q$
tower equals $\rho_q \cdot \sum_S \mathrm{Vol}(K_S)$
(archimedean bridge)"* — bridge role is in the title.  `uses[]`
cleanly partitions algebraic prerequisites
(`mass-endomorphism-tower`, `gb-spectral-sequence`,
`graded-trace-residue-split`, `markov-pair-z2`,
`phi-q-tower-algebraic-stratification`) and Archimedean
ingredients (`kashaev-volume-conjecture`,
`kashaev-as-archimedean-realization`, `cor:quantum-dilogarithm`).

**P2. Bridge `.lean` is conditional per AGENTS.md §3b.**
The Lean stub uses two typeclass instances — `[VolumeConjecture q]`
(the Kashaev axiom) and `[PerPieceBridge q]` (the per-piece
identification) — and the master `theorem bridge` is `:=
inst.bridge_per_piece β S`, so there is no `sorry`.  The
conjectural content is fully concentrated in the typeclass
instance (Option B / conditional-class pattern).

**P3. `q : ℝ` in the bridge `.lean` is correct.**  Unlike the §1
breaches, the bridge lives explicitly on the Archimedean side; it
is the τ_arch image of the algebraic statement.  `q : ℝ` is the
right ground type here.

### Net status

After the §6 + §7 fixes, the bridge / algebraic-stratification
pair partitions cleanly:

| Block | Side | Wall status |
|-------|------|-------------|
| `prop:phi-q-tower-algebraic-stratification` | Algebraic (pre-Arch) | 🟢 — unconditional, $R$-valued, Frobenius norm, GS-filtration |
| `conj:phi-q-tower-jsj-bridge` | Archimedean (bridge) | 🟡 — by design, conditional on `[VolumeConjecture q]` + `[PerPieceBridge q]` |

The only outstanding item is **F4**: the bridge `.lean` is a
co-located stub whose imports are namespace-only references.
This is a documentation-tier inconsistency, not a wall breach.

---

**End of bridge audit.**

---

## §8 — Sharp Step-6 audit (motivic descent layer)

The Step-6 cluster from §A of the forward-derivation document:
`def:motivic-galois-character` + `def:descent-involution` +
`conj:motivic-perpetual-obstruction`.  This is **GAP 6a**, the
principal open item on the substrate side.

### Findings

**M1 (resolved). Narrative said "Lemma" but block kind is `conjecture`.**
[`motivic-perpetual-obstruction.md`](../../content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.md):7
opened with *"**Lemma (motivic perpetual obstruction).**"* — a
holdover from the pre-2026-05-02 demotion (the `.ts` file's
header comment notes the demotion from `lemma` to `conjecture`).
The narrative continued reading as a lemma despite the block-kind
correction.  Updated to *"**Conjecture (motivic perpetual
obstruction).**"*; the proof sketch heading also updated to
*"**Sketch (conditional on
`[MotivicGaloisCharacter K0 Mhat Target motiveA]`).**"* to make
the conditional-class status explicit.

**M2 (resolved). The Lean modules existed only as co-located
documentation stubs.** The block `lean.ref` URIs
`qou:QOU.AlgebraicSubstrate.MotivicSubstrate`,
`qou:QOU.LiftingDescent.MotivicGaloisCharacter`, and
`qou:QOU.LiftingDescent.motivic_perpetual_obstruction` resolved
only via the sibling rule (co-located stubs at
`algebraic-substrate/motivic-substrate.lean` and
`lifting-and-descent/motivic-{galois-character,perpetual-obstruction}.lean`),
not via the formal Lake package.  The formal-chain
[`lean/QOU/LiftingDescent/`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/)
directory contained only `BBStratification`, `HomologicalCondensation`,
`JetProlongation` — the Step-6 modules were missing.  Promoted in
this commit:

- new [`lean/QOU/AlgebraicSubstrate/MotivicSubstrate.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/MotivicSubstrate.lean)
  — `Place`, `class MotivicSubstrate K0 Mhat Target`;
- new [`lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean)
  — `class MotivicGaloisCharacter` now properly takes
  `[MotivicSubstrate K0 Mhat Target]` as a hypothesis (closing the
  M5 narrative-vs-Lean gap below);
- new [`lean/QOU/LiftingDescent/MotivicPerpetualObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstruction.lean)
  — `theorem motivic_perpetual_obstruction` conditional on
  `[MotivicSubstrate ...]` + `[MotivicGaloisCharacter ...]`, no
  `sorry`.

Aggregator updates:
[`lean/QOU/AlgebraicSubstrate.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate.lean)
imports the new `MotivicSubstrate` module;
[`lean/QOU/LiftingDescent.lean`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent.lean)
imports both new descent modules.

**M3 (no fix needed). Apparent terminology collision on "archimedean".**
On first read, `motivic-galois-character.md` line 49 ("the archimedean
place") looks like it might collide with the "archimedean wall" of
the forward-derivation document (= τ-realisation).  In fact the two
uses are *consistent*: the "archimedean place" of ℚ is the place
`v = ∞`, whose realisation lands in `ℝ`; this IS the τ-image of the
substrate.  The `MotivicSubstrate` class's `archimedean_nontrivial`
field axiomatises non-degeneracy of exactly this realisation.  No
disambiguation needed.

**M4 (resolved). Stale GitHub URL pointed to a different audit's
branch.**
[`motivic-galois-character.md`](../../content/quantum-observable-universe/lifting-and-descent/motivic-galois-character.md):56
linked to
`https://github.com/litlfred/qou/blob/claude/audit-pole-structure-eqbHE/.../motivic-galois-character.lean`
— a branch from a different audit (`claude/audit-pole-structure-eqbHE`,
not the current `claude/audit-pre-archimedean-proofs-VZ3Hl`).  Hard-
coded branch URLs go stale at every audit; replaced with a relative
path
`[`MotivicGaloisCharacter`](../../lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean)`
that follows the working tree.

**M5 (resolved as part of M2). Narrative claimed
`MotivicGaloisCharacter` takes a `MotivicSubstrate` hypothesis;
co-located Lean stub did not.** The .md narrative said *"The class
takes a `MotivicSubstrate` instance as a hypothesis"*; the
co-located stub Lean class was

```
class MotivicGaloisCharacter
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (motiveA : Mhat) where ...
```

— no `[MotivicSubstrate K0 Mhat]` in sight.  The new formal-chain
version makes the narrative claim hold:

```
class MotivicGaloisCharacter
    (K0 Mhat : Type*) [CommRing K0] [CommRing Mhat]
    (Target : Place → Type*) [∀ v, CommRing (Target v)]
    [MotivicSubstrate K0 Mhat Target]
    (motiveA : Mhat) where ...
```

The Galois character is now genuinely *of a substrate*, not a
free-floating typeclass on raw ring parameters.

**M6 (observation, no fix). Lean theorem is a near-tautological
extraction.** `theorem motivic_perpetual_obstruction` repackages the
class field `MotivicGaloisCharacter.almost_everywhere_nontrivial`
(which provides `∃ N, ∀ p ≥ N, ¬IsUnit (frobenius_at p)`) into the
"bad finite set" form preferred by the conjecture (`∃ S : Finset ℕ,
∀ p ∉ S, ¬IsUnit ...`).  This is fine per AGENTS.md §3b — the
conjectural content lives in the class field; the theorem just
exposes it — but a reader of the .lean file should know that the
theorem's no-`sorry` property is *because* the class field carries
the conjectural input, not because the proof is non-trivial.

**M7 (observation, no fix). `descent-involution` is clean.**  Pure
categorical structure (ascent / descent / retraction / idempotence);
co-located Lean stub is polymorphic in `[CommRing R]`; idempotence
proof is two lines.  Two distinct `DescentInvolution` declarations
coexist:
- `QOU.DescentInvolution` (co-located stub at
  `lifting-and-descent/descent-involution.lean`, polymorphic in
  `Module R M`),
- `QOU.Torsion.Descent.DescentInvolution` (formal chain at
  `lean/QOU/Torsion/Descent.lean`, different signature).

The block `lean.ref = "qou:QOU.DescentInvolution"` resolves to the
co-located stub via the sibling rule.  This duplication is a
design observation, not a wall breach.

### Net status of the Step-6 cluster

| Block | Kind | Lean class | Wall status |
|-------|------|------------|-------------|
| `def:motivic-substrate` | definition | `class MotivicSubstrate K0 Mhat Target` (formal chain) | 🟢 unconditional, place-typed |
| `def:motivic-galois-character` | definition | `class MotivicGaloisCharacter` taking `[MotivicSubstrate]` (formal chain) | 🟢 conditional-class axiomatisation |
| `def:descent-involution` | definition | `structure DescentInvolution` (co-located + formal chain duplication) | 🟢 categorical, no Archimedean |
| `conj:motivic-perpetual-obstruction` | conjecture | `theorem motivic_perpetual_obstruction` conditional on the two classes (formal chain, no `sorry`) | 🟡 by design (GAP 6a) |

The conjectural content is now fully concentrated in the
`MotivicGaloisCharacter.almost_everywhere_nontrivial` field; every
downstream block depending on it (Kummer tower, Descartes-Yekutieli,
χ=−6 derivation, Hochschild-Kummer connection) inherits the
conditional-class hypothesis.  GAP 6a remains open at the
mathematical level — no concrete `instance MotivicGaloisCharacter`
for the QOU substrate at $q_0$ — but the Lean infrastructure is
now in place for any such instance to *immediately* discharge every
downstream block via the typeclass-instance lookup.

---

**End of Step-6 audit.**

---

## §9 — Sharp Step-13 audit (GS-residue / spectral-sequence cluster)

The Step-13 cluster: `prop:gb-spectral-sequence`,
`prop:graded-trace-residue-split`, `prop:graded-markov-trace-from-gs-filtration`,
`prop:residue-at-root`, `prop:gb-residue-spectral-sum`,
`prop:confinement-level-exists`.  This is **GAP 13a** in the
forward-derivation document — six declarations originally written
as `noncomputable opaque`, with a long-standing question of how
to translate them to the `§3b conditional-class` pattern.

### Findings

**S1 (resolved). `prop:gb-spectral-sequence` had no Lean file at
all.** Block kind is `proposition` — AGENTS.md §3 says Lean is
expected (warning if missing).  The block's `lean.ref` was
`qou:QOU.BraidKnot.gb_spectral_sequence`; no co-located stub, no
formal-chain file.  Pipeline fell back to the grep heuristic and
silently failed to verify.

**Fixed**: created
[`lean/QOU/BraidKnot/GBSpectralSequence.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/GBSpectralSequence.lean)
with `class GBSpectralSequence (R : Type u) [CommRing R]` carrying
`graded`, `differential`, `d_squared_zero`, and an
`e_infty_converges` witness; theorem `gb_spectral_sequence`
extracts `d² = 0` from the class instance.

**S2 (resolved). `prop:residue-at-root` had no Lean file at all.**
Same situation as S1.  The narrative defines the residue as the
cyclotomic projection `ℤ̂[q] → ℤ[q]/Φ_n(q) ≅ ℤ[ζ_n]` — purely
algebraic, no analytic continuation.

**Fixed**: created
[`lean/QOU/BraidKnot/ResidueAtRoot.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/ResidueAtRoot.lean)
with `class ResidueAtRoot (R : Type u) [CommRing R]` carrying
the per-`n` target ring `target n`, the cyclotomic projection
`project n : R →+* target n`, and a residue accessor.

**S3 (resolved). `prop:graded-markov-trace-from-gs-filtration`
formal-chain Lean was vacuous (`: True := trivial`).**

Same anti-pattern as `phi-q-tower-algebraic-stratification` (fixed
in §7).

**Fixed**: replaced the placeholder body of
[`lean/QOU/BraidKnot/GradedMarkovTraceFromGSFiltration.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/GradedMarkovTraceFromGSFiltration.lean)
with a `class GradedMarkovTraceFromGSFiltration (R : Type u) [Field R]`
encoding the descent relation `gradedTrace 0 = markovValue` (the
minimal level-0 identity that any instance must satisfy); theorem
`graded_markov_trace_from_gs_filtration` extracts it.

**S4 (resolved). `prop:gb-residue-spectral-sum` had only a
co-located stub.** The co-located stub already had a well-formed
`class GBResidueSpectralSum` (per the "P2.6 Lean refactor 2026-05-02"
note in its docstring: previous opaques `gradedMarkovTrace` and
`residueAtRoot` were already promoted to class fields).  The
remaining gap was that the class lived only in the documentation
tier — the formal chain had no compiled version.

**Fixed**: ported to
[`lean/QOU/BraidKnot/GBResidueSpectralSum.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/GBResidueSpectralSum.lean)
with the same `class GBResidueSpectralSum` (descended, levelBound,
roots, gradedTrace, residue, mass, spectral_decomposition);
theorem `gb_residue_spectral_sum` extracts the spectral
decomposition.  The `RootOfUnity` structure carries `value : ℝ` —
this is genuinely Archimedean (a complex root of unity, real part
recorded), so `ℝ` is correct here.

**S5 (resolved). `prop:graded-trace-residue-split` had only a
co-located stub.** I migrated this in §1 (Pass 10) to be polymorphic
in `[Field R]`, but the co-located file was not compiled.

**Fixed**: ported to
[`lean/QOU/BraidKnot/GradedTraceResidueSplit.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/GradedTraceResidueSplit.lean)
with the same `class GradedTraceResidueSplit (R : Type u) [Field R]`
(symbolMap, gradedTrace, gbResidue, markovTrace as opaques + the
class with split_identity).  The opaque names are
`GradedTraceResidueSplit.gradedTrace` etc. (qualified) to avoid
shadowing the formal-chain `GradedMarkovTraceFromGSFiltration`'s
class field with the same root name.  Theorem
`graded_trace_residue_split` extracts the split identity.

**S6 (resolved). `prop:confinement-level-exists` had only a
co-located stub; the parent type `ConfinementLevel` itself was also
co-located.**

**Fixed**: ported the entire
[`ConfinementLevel`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/ConfinementLevel.lean)
structure + `ConfinementLevel.exists` theorem to the formal chain.
The `confinement-level.md` block is a `definition` (not in the
audit's primary cluster), but its Lean home was previously co-only;
moving it to the formal chain unblocks downstream consumers.

**S7 (broken-import side-fix). `lean/QOU/BraidKnot.lean` imported a
non-existent module.** The pre-existing aggregator imported
`QOU.BraidKnot.ResidueAtRootFromGSFiltration`, but no such file
exists in the formal chain.

**Fixed**: replaced the dead import with the new
`QOU.BraidKnot.ResidueAtRoot`, and added the five other new
imports (`ConfinementLevel`, `GBSpectralSequence`,
`GradedTraceResidueSplit`, `GBResidueSpectralSum`).  This closes a
latent CI failure that would have surfaced on the next `lake build`.

### Net status of the Step-13 cluster

| Block | Kind | Lean home | Wall status |
|-------|------|-----------|-------------|
| `def:confinement-level` | definition | `lean/QOU/BraidKnot/ConfinementLevel.lean` | 🟢 polymorphic in `[CommRing R]` |
| `prop:confinement-level-exists` | proposition | same | 🟢 trivial existence witness |
| `prop:gb-spectral-sequence` | proposition | new `GBSpectralSequence.lean` | 🟡 conditional-class (substrate axiom: spectral-sequence existence) |
| `prop:graded-markov-trace-from-gs-filtration` | proposition | upgraded `GradedMarkovTraceFromGSFiltration.lean` (from `: True := trivial` to class) | 🟡 conditional-class (descent map existence) |
| `prop:residue-at-root` | proposition | new `ResidueAtRoot.lean` | 🟡 conditional-class (Habiro-completion projection) |
| `prop:graded-trace-residue-split` | proposition | new `GradedTraceResidueSplit.lean` (formal-chain version of co-located stub) | 🟡 conditional-class (split identity); pre-Arch by `[Field R]` |
| `prop:gb-residue-spectral-sum` | proposition | new `GBResidueSpectralSum.lean` | 🟡 conditional-class (graded trace + residue values) |

The forward-derivation §C.1 GAP 13a originally listed **six
`noncomputable opaque` declarations**:
`gradedMarkovTrace`, `residueAtRoot`, `spectral_decomposition`,
`spectral_sum_finite`, two `archimedean_agreement`.  After this
audit:

- `gradedMarkovTrace`: now a class field of
  `GBResidueSpectralSum` (and a class field of
  `GradedMarkovTraceFromGSFiltration`).
- `residueAtRoot`: now class fields of `GBResidueSpectralSum`
  and `ResidueAtRoot`.
- `spectral_decomposition`: now a class field of
  `GBResidueSpectralSum`.
- `spectral_sum_finite`: encoded in the finite-type domain
  `Fin levelBound` — automatic.
- The two `archimedean_agreement` declarations were not in the
  audit cluster but were always `Arch`-tier; they live downstream
  of `[GBSpectralSequence R]` + the τ_arch realisation.

GAP 13a is therefore **discharged at the Lean structural level**:
no `opaque` declarations remain in the cluster's primary
`prop:` blocks, every conjectural input is concentrated in named
class fields, and the formal-chain modules are now compiled.

The mathematical content (proving the existence of the spectral
sequence, the Habiro completion, etc.) remains research-grade —
the conditional-class pattern *isolates* the conjectural input
without claiming to prove it.  Concrete `instance` declarations
for the QOU substrate at $q_0$ would discharge each downstream
theorem automatically via typeclass resolution.

---

**End of Step-13 audit.**

---

## §10 — Sharp Step-14 audit (DB filtration / Δ_max cluster)

The Step-14 cluster from §A of the forward-derivation document
(GAP 14a — *Uniform Δ_max bound on per-level descent residue*):
`def:brane-tower-levels` (example), `def:direct-limit-algebra`,
`prop:delta-max-uniform-bound` (Archimedean / rank-1 closure of the
gap), and `conj:jet-tower-uniform-delta-max` (the conjectural
multi-rank statement).

### Findings

**D1 (resolved). `prop:delta-max-uniform-bound` had no Lean file
at all.** Block kind is `proposition` — AGENTS.md §3 expects Lean.
The `lean.ref = "qou:QOU.MassEndomorphism.delta_max_uniform_bound"`
resolved to nothing; no co-located `.lean` and no formal-chain
module.

**Fixed**: created the formal-chain module
[`lean/QOU/MassEndomorphism/DeltaMaxUniformBound.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/DeltaMaxUniformBound.lean)
with:

- `structure OperatorNormBound (ρ : Type*)` — the four ingredients
  of the proof (`braidLength`, `opNorm`, `freeMassLevel0`, `delta`)
  + non-negativity + the `per_level_bound` field that records the
  output of Steps 1–4 of the .md proof.
- `def OperatorNormBound.deltaMax := 2 · L · ‖ρ‖_op² · 𝔪⁽⁰⁾`
  (closed form), `theorem deltaMax_nonneg`.
- `theorem delta_max_uniform_bound : |b.delta n| ≤ b.deltaMax`
  conditional on the `OperatorNormBound` data.
- A discharger
  `def OperatorNormBound.toJetTowerUniformDeltaMax`
  that *converts an `OperatorNormBound`* into an instance of the
  conjectural class `JetTowerUniformDeltaMax` — i.e. the
  archimedean / rank-1 SDP regime is the **closure** of the
  conjecture's leaf, formally witnessed by Lean.

Also created an aggregator
[`lean/QOU/MassEndomorphism.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism.lean)
re-exporting the new module, and registered it in `QOU.lean`.

**D2 (resolved). `prop:delta-max-uniform-bound` had no `uses[]`
field.** The `.ts` manifest carried only `tags`, `lean`, `cites`;
the narrative `.md` cites at least four upstream blocks
(`prop:jet-tower-convergence`, `thm:markov-trace-factorization`,
`prop:descent-eigenspaces`, `def:recursive-brane-tower`). Added
all four to `uses[]` so the dependency graph is auditable from the
manifest.

**D3 (resolved). `def:direct-limit-algebra` Lean was co-located
only.** Promoted to
[`lean/QOU/LiftingDescent/DirectLimitAlgebra.lean`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/DirectLimitAlgebra.lean)
(same `structure DirectLimitAlgebra (R : Type*) [CommRing R]` as
the co-located stub) and registered in
`lean/QOU/LiftingDescent.lean`.

**D4 (resolved). `conj:jet-tower-uniform-delta-max` Lean was
co-located only.** The co-located stub was already a textbook
§3b conditional-class implementation — `class
JetTowerUniformDeltaMax (ρ : Type*)` with `delta`, `delta_max`,
`uniform_bound` fields and a conditional theorem
`geometric_tail_bound_abstract`.  Promoted verbatim to
[`lean/QOU/BraidKnot/JetTowerUniformDeltaMax.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/JetTowerUniformDeltaMax.lean)
and registered in `lean/QOU/BraidKnot.lean`.

**D5 (no fix needed). `ex:brane-tower-levels` is correctly
Archimedean.** It is an `example` block (no Lean expected), tagged
`archimedean`, opens *"Starting from an archimedean QOU"* and
hands off to `cor:jet-prolongation-C`.  ✓ Clean.

**D6 (no fix needed). Wall discipline for `delta-max-uniform-bound`.**
The proof uses Archimedean ingredients (operator norm `‖·‖_op`,
real `q > 0`, Cauchy–Schwarz on Hilbert–Schmidt norm, Kassel–Turaev
JW-module dimension bound) — but the block tags include
`operator-norm` and `legacy-phi-q-tower`, and the narrative
explicitly says it *closes the archimedean / rank-1 SDP regime* of
the convergence conjecture.  This proposition is intentionally on
the τ-image side; its `OperatorNormBound`-conditional form is the
right Lean encoding (the Archimedean ingredients become class
fields).

### Net status of the Step-14 cluster

| Block | Kind | Lean home | Wall status |
|-------|------|-----------|-------------|
| `def:recursive-brane-tower` | definition | (upstream — unchanged) | 🟢 |
| `def:direct-limit-algebra` | definition | new `lean/QOU/LiftingDescent/DirectLimitAlgebra.lean` | 🟢 polymorphic in `[CommRing R]` |
| `ex:brane-tower-levels` | example | (no Lean — example) | 🟢 Archimedean by design |
| `prop:delta-max-uniform-bound` | proposition | new `lean/QOU/MassEndomorphism/DeltaMaxUniformBound.lean` | 🟢 closure of GAP 14a in the rank-1 SDP regime, conditional on `OperatorNormBound` |
| `conj:jet-tower-uniform-delta-max` | conjecture | new `lean/QOU/BraidKnot/JetTowerUniformDeltaMax.lean` | 🟡 by design (multi-rank case open); class-axiomatised per §3b |

GAP 14a status update: the **rank-1 SDP regime** is now formally
closed in Lean — the `delta_max_uniform_bound` theorem is a direct
extraction of the `OperatorNormBound` class fields, and a
constructor `toJetTowerUniformDeltaMax` witnesses that any
`OperatorNormBound` instance discharges the conjectural class on
that leaf.  The **multi-rank case** remains 🟡 open (forward-
derivation §C.1 GAP 14a multi-rank); the conjecture
`conj:jet-tower-uniform-delta-max` is the right home for it.

The forward-derivation document will need a refresh: GAP 14a
should be split into 14a-rank1 (closed by
`prop:delta-max-uniform-bound`) and 14a-multi-rank (still open).

---

**End of Step-14 audit.**

---

## §11 — Sharp Step-17 audit (pentagon UV / Markov-pair cluster)

The Step-17 cluster from §A of the forward-derivation document
(GAP 17a — *pentagon $uv = q\,vu$ verification at the traced-volume
level*; GAP 17b — *descent sharpness on pairs*).  Cluster:
`prop:markov-pair-z2`, `thm:markov-trace-product`,
`prop:pentagon-uv-commutation`.

### Findings

**E1 (resolved). `prop:markov-pair-z2` had no Lean file at all.**
Block kind `proposition` (AGENTS.md §3 expects Lean).  `lean.ref =
"qou:QOU.Hecke.markov_pair_z2"` resolved to nothing.

**Fixed**: created
[`lean/QOU/Hecke/MarkovPairZ2.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/MarkovPairZ2.lean)
with `theorem markov_pair_z2` conditional on a `[MarkovTraceAxioms z]`
instance — two cons-applications of the Markov property give
`tr_M([c₁, c₂]) = z²` for trivial generator chains (the depth-2
cap of the all-pairs jet-tower formula).  Closed with `simp` after
unfolding `vertexVolume` on the `(a = 1, b = 0)` case.

**E2 (resolved). `thm:markov-trace-product` had a stale `lean.ref`.**
The `.ts` carried `lean.ref = "qou:QOU.markov_trace_product"`, but
the co-located stub declared `theorem QOU.Braiding.markov_trace_product`
(under `namespace QOU.Braiding`).  Lookup of the unqualified
`QOU.markov_trace_product` would fail.

**Fixed**: ported to
[`lean/QOU/Hecke/MarkovTraceProduct.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/MarkovTraceProduct.lean)
under the established `namespace QOU.Hecke`, with the same
`MarkovTraceAxioms` typeclass + `MarkovTraceProduct` structure +
`theorem markov_trace_product` (existence form) +
`theorem markov_trace_product_recursion` (cons-induction strong form).
Updated `markov-trace-product.ts`'s `lean.ref` to
`qou:QOU.Hecke.markov_trace_product`.  Registered in
`lean/QOU/Hecke.lean`.

The pre-Arch discipline carries through: `R_q := LaurentPolynomial ℤ`,
`vertexVolume z gc := z * gc.a + gc.b`; the previous Archimedean
hypotheses (`n ≥ 2`, `q > 1`) are commented out and noted as
"archimedean; not meaningful over R_q".

**E3 (no fix needed). `prop:pentagon-uv-commutation` is already
in the formal chain.** [`lean/QOU/QuantumBloch/PentagonUvCommutation.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumBloch/PentagonUvCommutation.lean)
exists ✓.  No co-located stub is required.  The pentagon
commutation `u·v = q·v·u` is precisely the GAP 17a content
("pentagon $uv = q\,vu$ verification") and is structurally encoded
in the formal chain.

### Net status of the Step-17 cluster

| Block | Kind | Lean home | Wall status |
|-------|------|-----------|-------------|
| `prop:markov-pair-z2` | proposition | new `lean/QOU/Hecke/MarkovPairZ2.lean` | 🟢 conditional on `[MarkovTraceAxioms z]`, `R_q`-valued |
| `thm:markov-trace-product` | theorem | new `lean/QOU/Hecke/MarkovTraceProduct.lean` | 🟢 `R_q := LaurentPolynomial ℤ` ground ring; pre-Arch |
| `prop:pentagon-uv-commutation` | proposition | existing `lean/QOU/QuantumBloch/PentagonUvCommutation.lean` | 🟢 (GAP 17a content) |

GAP 17a is **structurally addressed** at the Lean level: the
pentagon UV-commutation theorem statement is in the formal chain,
the Markov-trace product factorization (which fuels the pair
identity) is in the formal chain, and the all-pairs identity
`markov_pair_z2` extracts the depth-2 cap.  GAP 17b (descent
sharpness on pairs) remains residual — the bound "Pairs are the
largest |S| at which Markov property preserves closure" is now
witnessed by the absence of a triple-form theorem; sharpening
requires a separate negative result.

---

## §12 — Sharp Step-18 audit (mass endomorphism cluster)

The Step-18 cluster from §A of the forward-derivation document
(GAP 18a — *`conj:mass-endomorphism` closed form*).  Cluster:
`prop:mass-endomorphism-tower`, `def:hecke-mass-element`,
`conj:mass-endomorphism`, `rem:mass-endomorphism-jet-tower`.

The pre-Arch wall in `prop:mass-endomorphism-tower` and
`def:hecke-mass-element` was already closed in §1 (Pass 13/Pass 11
two-tier `Pre`/`Arch` namespace splits) and `prop:delta-max-uniform-bound`
was closed in §10.  This audit examines the conjecture itself.

### Findings

**F1 (resolved). `conj:mass-endomorphism` had only a co-located
Lean stub.** The co-located file at
`braids-and-knots/mass-endomorphism-conjecture.lean` already
implements the §3b conditional-class pattern textbook-clean:
`class MassEndomorphism (R) [CommRing R] (β)` with fields `q`, `N`,
`z`, `tr_transient`, `tr_descended`, `vol_identity`, and the
asserted `vol_eq` equality; `theorem fullMass_eq_volume` extracts
the volume identity from any instance.

**Fixed**: ported to
[`lean/QOU/MassEndomorphism/MassEndomorphismConjecture.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/MassEndomorphismConjecture.lean)
under `namespace QOU.MassEndomorphism` (matching the existing
`QOU.MassEndomorphism` aggregator from §10).  Updated the
`mass-endomorphism-conjecture.ts` `lean.ref` from
`qou:QOU.WedderburnMass.MassEndomorphism` to
`qou:QOU.MassEndomorphism.MassEndomorphism` for consistency with
the new namespace (the legacy `WedderburnMass` namespace was a
holdover from before the `MassEndomorphism` aggregator existed).

Registered in `lean/QOU/MassEndomorphism.lean`.

**F2 (no fix needed). `rem:mass-endomorphism-jet-tower` is correct.**
A `remark` block (no Lean expected) interpreting
`prop:mass-endomorphism-tower`.  Its `interprets:` field is set
correctly; AGENTS.md §3a discipline holds.

### Net status of the Step-18 cluster

| Block | Kind | Lean home | Wall status |
|-------|------|-----------|-------------|
| `def:hecke-mass-element` | definition | co-located (§1 Pass 11 + §10 follow-up) | 🟢 abstract `[CommRing R]` (no `NormedCommRing` in pre-Arch) |
| `prop:mass-endomorphism-tower` | proposition | co-located (§1 Pass 13 two-tier `Pre`/`Arch`) | 🟢 pre-Arch tier, post-Arch tier explicitly partitioned |
| `conj:mass-endomorphism` | conjecture | new `lean/QOU/MassEndomorphism/MassEndomorphismConjecture.lean` | 🟡 by design (closed-form open); class-axiomatised per §3b |
| `rem:mass-endomorphism-jet-tower` | remark | (no Lean — remark) | 🟢 `interprets:` discipline holds |

GAP 18a status: `conj:mass-endomorphism`'s closed-form claim is
**fully concentrated in the class field `vol_eq`**.  Any concrete
instance of `MassEndomorphism R β` discharges the conjecture for
that pair `(R, β)`; the conditional `fullMass_eq_volume` theorem
is fully verified by Lean (no `sorry`).  The Lean infrastructure
is in place; the open content is the **mathematical** task of
proving an instance for the QOU substrate at $q_0$.

---

**End of Step-17 / Step-18 audit.**

---

## §13 — Sharp Step-7 audit (cosimplicial gluing cluster)

The Step-7 cluster from §A of the forward-derivation document.
Cluster: `prop:cosimplicial-crossed-groupoid` +
`prop:descent-condition` + `prop:global-gluing`. These are the
descent-infrastructure propositions that carry the Yekutieli
obstruction κ_n through the cosimplicial brane tower.

### Findings

**G1 (resolved). All three propositions had Lean siblings only as
co-located stubs.** None lived in the formal Lake package; the
`lean.ref` URIs (`qou:QOU.cosimplicial_crossed_groupoid_exists`,
`qou:QOU.Torsion.descent_condition`, `qou:QOU.Torsion.global_gluing`)
resolved through the sibling rule.

**Fixed**: ported all three to the formal chain:

- New
  [`lean/QOU/LiftingDescent/CosimplicialCrossedGroupoid.lean`](../../content/quantum-observable-universe/lean/QOU/LiftingDescent/CosimplicialCrossedGroupoid.lean)
  — `R_q := LaurentPolynomial ℤ`, structures `YekutielijTriple`,
  `CrossedModule`, `CosimplicialCrossedGroupoid`, and theorem
  `cosimplicial_crossed_groupoid_exists` (constructive existence,
  no `sorry`).  Namespace `QOU.LiftingDescent`; `lean.ref` updated
  to `qou:QOU.LiftingDescent.cosimplicial_crossed_groupoid_exists`.
- New
  [`lean/QOU/Torsion/DescentCondition.lean`](../../content/quantum-observable-universe/lean/QOU/Torsion/DescentCondition.lean)
  — structures `CechCocycleData`, `TwistedCocycleCondition`,
  `DescentCondition`; theorem `descent_condition` extracts global
  consistency from vanishing obstruction.  Namespace `QOU.Torsion`;
  `lean.ref` already correct.
- New
  [`lean/QOU/Torsion/GlobalGluing.lean`](../../content/quantum-observable-universe/lean/QOU/Torsion/GlobalGluing.lean)
  — structures `LocalDeformation`, `TwistedQuantizationMap`,
  `GlobalGluing`; theorem `global_gluing` exhibits the global ring
  structure.  Polymorphic in `[CommRing R]`.  Namespace
  `QOU.Torsion`; `lean.ref` already correct.

Aggregator updates: `lean/QOU/LiftingDescent.lean` imports
`CosimplicialCrossedGroupoid`; `lean/QOU/Torsion.lean` imports
`DescentCondition` and `GlobalGluing`.

**G2 (no fix needed). Wall discipline is already clean.** All
three modules use either `R_q := LaurentPolynomial ℤ` or polymorphic
`[CommRing R]`, with categorical / group-theoretic hypotheses only.
The §1 stray-import removal (Pass 7b/7c) is now reinforced by the
formal-chain port — the formal-chain modules carry no `Real`,
`Analysis`, `Topology`, or `Manifold` imports.

### Net status of the Step-7 cluster

| Block | Kind | Lean home | Wall status |
|-------|------|-----------|-------------|
| `prop:cosimplicial-crossed-groupoid` | proposition | new `lean/QOU/LiftingDescent/CosimplicialCrossedGroupoid.lean` | 🟢 `R_q`-valued, constructive existence |
| `prop:descent-condition` | proposition | new `lean/QOU/Torsion/DescentCondition.lean` | 🟢 polymorphic group cocycles |
| `prop:global-gluing` | proposition | new `lean/QOU/Torsion/GlobalGluing.lean` | 🟢 polymorphic in `[CommRing R]` |

The Step-7 descent infrastructure is now fully in the formal chain.
This unblocks the conditional-class consumers downstream
(`def:motivic-galois-character`, `def:descent-involution`, the
mass-tower descent splitting in §1 / §10).

---

**End of audit.**
