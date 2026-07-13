# Alien-calculus / resurgence review for the binding kernel: Gevrey-1/2 pinned (Lean), level-1/2 Borel singularity at ξ = 1/√2, q₀ class change to q-Gevrey

**Date:** 2026-07-12
**Branch:** `claude/alien-calculus-resurgence-nvvezn`
**Bean:** `z2bn` (lever-1 fibre q-difference kernel) — session beans `qou-t4r0/y4ha/y386/7xit`
**Lean:** [`QOU/Mass/BindingGevreyHalf.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingGevreyHalf.lean) (sorry-free, lean-direct exit 0)
**Probes:**
[`computations/lever1_gevrey_order_pin.py`](../../computations/lever1_gevrey_order_pin.py),
[`computations/lever1_borel_half_singularity_probe.py`](../../computations/lever1_borel_half_singularity_probe.py),
[`computations/lever1_habiro_tail_habiro_basis_expansion.py`](../../computations/lever1_habiro_tail_habiro_basis_expansion.py)
**Sibling:** [PR #3686](https://github.com/litlfred/qou/pull/3686) (Habiro cofactors not Salem — the arithmetic side of the same object; this note opens the analytic/growth side)

## 1. What was reviewed

An external AI dialog (owner-pasted, 2026-07-12) proposing an Écalle alien-calculus /
resurgence framing for the lever-1 binding kernel: Borel transform of `a_D^(n)`, alien
derivatives `Δ_ω` at branch-point singularities, a Bridge equation with quantum Stokes
multipliers `A_ω(q) ∝ (q−1)²·Φ_m(q)`, saddle-geodesic spectral networks, per-trajectory
orthogonal polynomials, and a claimed unique rigid reconstruction of a binding kernel
`K_q(x,y)`.

### Verdict per claim (critical-distance license)

| dialog claim | corpus status |
|---|---|
| `D(5)=2(q−1)²Φ₂²Φ₃Φ₆/q`, q-telephone recurrence, Lean q=1 limit | **already derived** ([Habiro-tail closed forms](2026-07-12-lever1-habiro-tail-closed-form.md), `BindingClassicalKernel.lean`) |
| Puiseux ⇒ `a_D^(n) ∝ (1/2)ₙ/Rⁿ` **factorial (Gevrey-1)** ⇒ standard Borel carries `Δ_ω` | **REFUTED (scope-(a), now Lean-backed):** the single-branch factorial rate overshoots ~2.6× at n=8 ([rate-refine audit](2026-07-12-lever1-sw-period-lw-rate-refine.md)); this session proves the class is **Gevrey-1/2** (§2). The level-1 Borel transform of the period is *entire* — no finite singularities, no alien derivatives live in that plane. |
| `K_q(x,y)` "exists uniquely, completely rigid" | **over-claimed:** resurgent reconstruction needs proved endless continuability; the standard theorem base (exact WKB / holonomic modules) does not apply — the tail is **not q-holonomic** at low order (Stages 3–6, 2026-06-28). Hypothesis, not conclusion. |
| saddle-trajectory orthogonal polynomials / Christoffel–Darboux | already pruned as a closure route ([q-involution/q-Hermite id](2026-06-26-binding-period-qinvolution-qhermite-identification.md)); narrative, no new decidable |
| Bridge equation, `A_ω(q)` vanishing at cyclotomic roots | untestable until the singularities are located in the **correct** plane — which this session does (§3); remains open, now with a concrete target |
| "works over ℤ": q-Borel `[n]_q!`, cyclotomic completion (Habiro ring) | **agrees with the queued Stage-6 next step**; executed this session as the `(q;q)_k`-basis expansion (§4) |

## 2. Gevrey order pinned: 1/2 at q=1 (Lean-proved sandwich)

[`BindingGevreyHalf.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingGevreyHalf.lean),
sorry-free, two-step induction from the corpus `involutionNumber` telephone recurrence:

- `factorial_le_four_pow_mul_involution_sq` : `n! ≤ 4ⁿ·I(n)²`
- `involution_sq_le_two_pow_mul_factorial` : `I(n)² ≤ 2ⁿ·n!`

So `√(n!/4ⁿ) ≤ I(n) ≤ √(2ⁿ·n!)` — the classical binding period `a_D^(n) = I(n)/n` is
`(n!)^{1/2}` × (exponentially bounded): **Gevrey-1/2 exactly** (super-exponential, but
strictly below every Gevrey-1 class). Numerics (`lever1_gevrey_order_pin.py`, exit 0):
sandwich asserted to n=60; `ln I(n)` matches the `(n/e)^{n/2}e^{√n−1/4}/√2` asymptote to
+0.035 at n=60; level-1 Borel root test decays as `√(e/n)` (scaled 1.002 ≈ 1 ⇒ B₁ entire).

## 3. The level-1/2 Borel plane: singularity at ξ = 1/√2; q₀ changes class

`lever1_borel_half_singularity_probe.py` (exit 0), coefficients `b_n = a_D^(n)/Γ(n/2+1)`:

- **q=1 (n ≤ 60):** root test → √2 (two-term extrapolation 1.365, 3.5%); Padé [28/28]
  nearest pole `ξ = 0.688` (2.6% from `1/√2 = 0.7071`) on the **positive real axis**
  (Pringsheim, as forced by `b_n > 0`), with **10 real poles accumulating** beyond ρ —
  a **non-polar** (branch/essential) singularity, the `e^{√n}` subexponential signature
  of a mixed-level transseries.
- **q₀ (n ≤ 28):** the level-1/2 root test **rises without plateau** (1.18 → 1.97) —
  the finite-n shadow of radius → 0. Combined with the exact envelope
  `dim_q ≤ [n]_q! ⇒ S_q(n) ≤ p(n)·q^{n(n−1)/2}` and the measured exponent ratio rising
  toward it (0.05 → 0.25, n ≤ 28), the q-deformation **changes the divergence class**:
  classical Gevrey-1/2 → **q-Gevrey** (Jackson q-Borel territory). At q₀ no single
  classical Borel level carries the period; the correct alien-calculus geometry is an
  **Écalle acceleration chain**, not one Borel plane.
- **Geometric comparison (reported only, numerology guard):** the color-cubic branch
  moduli (|z| ≈ 0.943, 1.0, 1.061) live in the z-plane, not the ξ-plane; no
  identification claimed. The measured datum (ρ = 1/√2, positive axis, non-polar) is the
  structural target any derived multi-branch residue kernel must reproduce.

## 4. Habiro-basis expansion of the tail D(n)

`lever1_habiro_tail_habiro_basis_expansion.py` (exact sympy, exit 0): expand
`P_n = q^{v(n)}·D(n) ∈ ℤ[q]` in the Habiro / cyclotomic-completion basis
`{(q;q)_k}` via successive division by `(1−q^{k+1})` (integrality automatic — unit
leading coefficients). Closed forms of the
[Habiro-tail audit](2026-07-12-lever1-habiro-tail-closed-form.md) verified bit-for-bit
(n = 4, 5 + the universal `(q−1)²` root); round-trip exact; `c₀ = 0` universally:

| n | k_max | first k≠0 | height max\|coeff\| |
|--:|--:|--:|--:|
| 4 | 2 | 1 | 1 |
| 5 | 3 | 2 | 4 |
| 6 | 4 | 1 | 38 |
| 7 | 5 | 1 | 308 |
| 8 | 7 | 1 | 2 296 |
| 9 | 8 | 1 | 21 897 |

Depth grows ≈ `n−1` and height ≈ ×8–9 per step — the basis-side face of the
"no finite closed form" Stage 6–9 verdict. One structural curiosity (reported, not
interpreted): n = 5 — the *last all-cyclotomic* tail — is also the only n with
first-nonzero depth k = 2 instead of 1.

## 5. Net (scope + what is now sharper)

- **Derived + Lean-proved:** the classical binding period is Gevrey-1/2 (two-sided
  integer sandwich). This *corrects* the dialog's central technical premise.
- **Measured (scope-(a)):** the canonical (level-1/2) Borel singularity datum at q=1 —
  `ξ = 1/√2`, positive real axis, non-polar — and the q₀ class change to q-Gevrey.
- **The open super-exp kernel question is sharpened:** it now has a concrete analytic
  target (reproduce the `1/√2` datum and the q-Gevrey deformation), complementing the
  concluded algebraic line (Stages 6–9 + [PR #3686](https://github.com/litlfred/qou/pull/3686)'s
  not-Salem classification).
- **Not done, deliberately:** no Bridge-equation / Stokes-multiplier formalism (no proved
  resurgence for a non-q-holonomic series), no orthogonal-polynomial spectral-network
  construction (already pruned), no wiring, no fit, no tier change.

## Addendum (same day) — Stage 3–6 re-verified with a positive control; saddle actions; the exactness (b)-exclusion

**Owner flagged the Stage 3–6 probes may be inaccurate.** Legitimate (Stage 7's first
classifier had a silently-caught bug; Stages 3–6 shipped no positive control), so the
question was re-run independently:
[`lever1_qholonomic_reverify.py`](../../computations/lever1_qholonomic_reverify.py)
(exit 0) — own Laurent-exact `dim_q`/`S(m)` (m ≤ 13, `S(m)|_{q=1}=I(m)` checked), exact
integer nullspaces (no numeric rank), **positive control** (`(q;q)_m`: the engine finds
the known order-1 relation and it survives held-out), sweep widened to **order 4**
(Stages 3–4 stopped at 3): **zero held-out survivors at every configuration** ⇒ the
Stage 3–6 (a)-verdict is **confirmed and strengthened**. Stage-7's D(6…9) invariants
((q−1)² root, published Φ_d lists, cofactor degrees 8/10/14/28, palindromy) also
reproduce bit-for-bit from the independent data.

**Owner-picked follow-ups**
([`lever1_saddle_action_jet_residue_probe.py`](../../computations/lever1_saddle_action_jet_residue_probe.py), exit 0):

- **(A) Per-pair saddle actions.** The exact-WKB dictionary puts Borel singularities at
  saddle **actions** `ω = ∫(X_a−X_b)dz` between branch points — not at branch-point
  *positions* (the dialog conflated the two). The three reciprocal-pair actions of the
  q-free color cubic: `|A| = 0.4294` (unit-modulus pair; colliding sheet-pair differs at
  the two ends — a genuine spectral-network subtlety) and `|A| = 2.4983` (twice, the
  bar-conjugate pair, equal moduli as forced by bar symmetry). Report-only vs the
  measured level-1/2 datum: `|A|/(1/√2) = 0.607, 3.533, 3.533` — **no naive match**;
  any identification would need the correct acceleration-chain normalization (open).
- **(B) The exactness (b)-exclusion.** The classical jet rule makes
  `λ_SW^(n) = X^(n)dz = d(X^(n−1))` an **exact** meromorphic differential for n ≥ 1, so
  **all residues and all closed-cycle periods vanish identically** (invariant:
  Stokes/exactness) — verified exactly at z=∞ (sheet expansions reproduce the Step-1
  n=0 residues `{0, ±5i/16}`, sheet-sum 0; jets n=1…4 have identically zero
  1/z-coefficients on every sheet). Hence the classical-jet reading of
  `a_D^(n) = ∮λ_SW^(n) = lw(n−1) ≠ 0` is excluded on **any** cycle — a second,
  independent (b)-invariant alongside PR #2768's q-freeness exclusion. The q-difference
  prolongation (the live route) and the algebraic `prop:sw-period-residue-sum` identity
  are untouched. Lean target (follow-up, small): `coeff₋₁(f') = 0` for Laurent series —
  the residue-of-exact-form lemma.

## Addendum 2 — the exactness proposition (Lean + paper) and the Bridge-equation alien datum (W5)

**Owner-requested Lean + paper for the exactness result:** new content block
[`prop:sw-classical-jet-exactness`](../../content/quantum-observable-universe/brings-surface/sw-classical-jet-exactness.md)
(+ proof block, registered in `brings-surface.ts`, sited next to
`prop:sw-period-residue-sum`). Lean sibling sorry-free, lean-direct exit 0:
`fresidue_fderiv` (residue of a termwise derivative vanishes — generic `CommRing`,
§7c wall-safe), `classical_jet_period_zero` (composed with the residue-sum shape as an
explicit hypothesis, the L1 pattern), `classical_jet_period_ne_lw` (against the nonzero
`I(m)/m`). Render-QA: pipeline unavailable in this container; manual grep battery +
expository pass run and clean — **not machine-validated**.

**W5 — the Bridge-equation alien datum at ω₀ = 1/√2, closed form + verified**
([`lever1_bridge_alien_datum_probe.py`](../../computations/lever1_bridge_alien_datum_probe.py), exit 0).
Derived *before* measurement from the proved involution asymptotics + the Laguerre
generating identity, the local singular model of the level-1/2 Borel transform is

    B̂(ξ) ~ A_ω·(1−√2ξ)^{3/2}·exp( 1/(4(1−√2ξ)) )  near ξ = 1/√2,

with the four-component **alien datum**: ω₀ = 1/√2 (level-1/2 action), A₂ = 1/4
(second-level action — the `e^{√n}` factor, confirming the acceleration-chain
structure), γ = 3/2 (branch exponent), and Stokes constant **A_ω = 4√2·e^{−3/8}
≈ 3.8884**. Verified against exact `I(n)` to n = 400: K_c to 2×10⁻⁵ rel, √n-coefficient
0.99989, power −1.5016, A_ω to 0.43%. **q-rigidity:** the deformation of the datum is
bar-even (exact under q↔1/q) and O((q−1)²) (measured exponent 1.956) — the alien datum
is *stationary at the classical point*, the derived and testable form of the dialog's
"A_ω(q) carries (q−1)²" claim (the Φ_m root-of-unity part needs |q| = 1 evaluation —
out of real-q scope). **Scope:** at q = 1 the binding EGF `e^{x+x²/2}` is entire, so
there is no equational Stokes phenomenon; the resurgence is **co-equational**
(coefficient-plane), and the literal one-parameter-ODE Bridge form `Δ_ω f = A_ω·df/dz`
does not apply verbatim — A_ω above is the co-equational Stokes constant.

## Addendum 3 — kernel hunt: the binding period IS an involution statistic (exact)

Owner steer: *"try find kernel — corpus grep and lit search based on knowns."* Corpus grep:
the kernel object is `R(q,x)` of
[`prop:binding-genfun-qdifference`](../../content/quantum-observable-universe/mass-theory/binding-genfun-qdifference.md)
(open, must be derived not fitted); the q-Hermite **crossing**-statistic identification was
already pruned (2026-06-26). Web literature backends returned **empty in this container**
(noted); the classical anchors used instead are textbook-solid and are **verified exactly
in-container**: Stanley's q-hook-maj formula (shape-refined, n ≤ 8) and RSK/Schützenberger
descent preservation for involutions.

**The identification (exact, verified n ≤ 8 — 764 involutions at n = 8,**
[`lever1_kernel_maj_involution_identification.py`](../../computations/lever1_kernel_maj_involution_identification.py)**):**

    S^bal(n; q) · q^{n(n−1)/2}  =  Σ_{w ∈ Inv(Sₙ)} q^{2·maj(w) + content(λ(w))}

where `λ(w)` is the RSK shape of the involution and `content(λ) = n(λ′) − n(λ)`. Derivation:
`dim_q^bal(λ) = q^{content(λ) − n(n−1)/2}·f̃^λ(q²)` with `f̃^λ` the fake degree, composed with
`Σ_w q^{maj(w)} = Σ_λ f̃^λ(q)` (the sum of fake degrees). So the binding period is exactly the
generating function of involutions by the mixed statistic **2·maj + content∘RSK** — a
*different* statistic from the pruned crossing/q-Hermite one.

**Kernel consequence (measured, scope-(a)):** splitting `Inv(n)` by the fate of the letter
`n` (fixed point vs 2-cycle), the fixed-point-insertion weight ratio `W_fix(n)/W(n−1)` is
**non-monomial with growing spread** (num terms 2, 4, 6, 10, 15, 22 for n = 3…8) — maj is
not Markovian under RSK insertion. This is the combinatorial face of the Habiro tail `D(n)`
and the structural explanation of the measured non-q-holonomicity: **the kernel is an
insertion recursion at the statistic level, not a finite q-difference operator.** The
productive continuation is therefore a transfer/statistic-level operator (e.g. tracking the
descent-set refinement under insertion), not a larger nullspace search. Follow-up flagged:
promote the identification to a content block (proposition + Lean via a finite `decide`
verification or the classical proofs) once this PR lands.

## Discipline

Formalize-first: the Gevrey sandwich was proved (Lean, sorry-free, lean-direct exit 0)
and the ξ = 1/√2 expectation derived from proved asymptotics *before* the numerical
hunt. Binding `D(n)`/`a_D^(n)` only — **not** the Q_β `c_k` ladder (distinct objects;
the c_k flip-flop discipline is untouched). All exploratory; owner closes (§4a).
