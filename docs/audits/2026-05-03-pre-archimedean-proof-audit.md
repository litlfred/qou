# Pre-Archimedean proof & Lean audit

**Date.** 2026-05-03
**Branch.** `claude/audit-pre-archimedean-proofs-VZ3Hl`
**Scope.** Steps 0–19 of the forward-derivation chain
([`2026-05-02-forward-derivation-pre-archimedean.md`](2026-05-02-forward-derivation-pre-archimedean.md)).
**Question.** Do the proofs (narrative `.md` + Lean `.lean`) of the
canonical pre-Archimedean blocks actually live below the wall, or do
they secretly reach across $\tau$?

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
per Step 12 of the forward derivation, and CLAUDE.md §7aa notation
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
`folio-assistant/computations/y-lambda-clean-closed-forms.md`; the
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
status is explicit (per CLAUDE.md §3b conditional-class pattern).

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
as a *single explicit conjectural class* (per CLAUDE.md §3b
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

**End of audit.** No code was modified. Closing the 17 Lean breaches
above is a follow-up workpiece (estimated: ~600 LoC across 14 files,
plus 3 two-tier splits).
