# arg(tr_M) is U(1) (Chern–Simons / framing), NOT C₅ color — structural verdict

**Date:** 2026-06-16
**Type:** Structural investigation (read + numerical probe). No paper content edited.
**Probe:** `/tmp/phase_probe.py` (log `/tmp/phase_probe.log`).

## Question

QOU mass is the *modulus* of the categorical Markov trace,
`𝔪 = |tr_M(ρ(β))|`
([`mass-endomorphism-conjecture.md`](../../content/quantum-observable-universe/mass-endomorphism/mass-endomorphism-conjecture.md) L34-41, L83-90).
The modulus presupposes a complex trace, so the discarded degree of
freedom is the **phase** `arg(tr_M(ρ(β)))`. Does that phase carry:

- **(U1)** a continuous U(1) phase — the Chern–Simons / framing-anomaly,
  the Im channel of the complex volume 𝔙, EM-like; or
- **(C5)** the discrete C₅ Galois character `χ_ζ` (ζ = e^{2πi/5}) of the
  Bring "color" tubes — a color quantum number?

## Verdict: **U(1) (Chern–Simons / framing / Im 𝔙).** C5 is a *separate* object.

`arg(tr_M)` is a **continuous** U(1) phase living on the **same** Hecke
object whose modulus is mass; it is the framing/Chern–Simons channel that
the corpus already names `Im 𝔙 = CS(K)`. The C₅ character `χ_ζ` is a
discrete Galois grading on a **different** object — the Bring quintic
resolvents (geometry), not the Markov trace. A "color = phase of the mass
trace" conjecture would therefore be **FALSE and must not be written.**

## Structural reasons (the load-bearing argument; numerics only corroborate)

1. **The phase is the framing/CS channel, by the corpus's own construction.**
   - The trace transforms under the antipode/bar involution `q ↦ q⁻¹` as a
     *Laurent polynomial in q* (the Jones polynomial), with an
     **anti-self-reciprocal** numerator carrying only a single overall
     ± sign — a *parity*, not a C₅ phase:
     `tr_M(𝓑_p)(1/q) = −tr_M(𝓑_p)(q)`
     ([`markov-trace-antipode-polynomial-symmetry.md`](../../content/quantum-observable-universe/mass-endomorphism/markov-trace-antipode-polynomial-symmetry.md) L21-29, L73-78).
   - The framing dependence is the **ribbon twist** `Θ·v_λ = q^{2c(λ)}v_λ`,
     giving the framed Jones `J = q^{2w·c(λ)}·V` with writhe `w`
     ([`chirality-writhe-ribbon-derivation.md`](../../content/quantum-observable-universe/mass-theory/chirality-writhe-ribbon-derivation.md) L20-43).
     On `q = e^{iθ}` this is `e^{2i·w·c(λ)·θ}` — a **continuous U(1) phase
     linear in θ and in the writhe**. That is exactly the Chern–Simons /
     framing-anomaly winding.
   - The corpus already classifies this: the phase / Im channel is the
     **bar-odd** projection (`sinh`, `Φ_q`, discarded by `P_avg`)
     ([`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md) L32-37),
     identified as `Im 𝔙 = CS(K)`, the Tate-twisted imaginary period
     ([`chirality-period-pairing.md`](../../content/quantum-observable-universe/mass-endomorphism/chirality-period-pairing.md) L20, L54-62;
     [`bar-parity-split.md`](../../content/quantum-observable-universe/mass-theory/bar-parity-split.md) L30-39;
     [`complex-volume-intro.md`](../../content/quantum-observable-universe/mass-endomorphism/complex-volume-intro.md) L1, L11-21).
     CS(3₁) = ±π²/6 — a *real continuous number*, not a C₅ lattice value.
   - `arg(tr_M) ≠ 0 ⟺ root-of-unity (bar-odd / CS) evaluation` is
     **confirmed**: at real `q`, the Markov trace is a real Laurent value
     (real Jones), phase 0 or π only; nonzero continuous phase appears only
     when `q` rotates onto the unit circle (`cosh λ → cos θ`,
     `sinh λ → i sin θ`), i.e. the analytic-continuation / root-of-unity
     channel. This is the `λ ↦ iθ` continuation of `bar-parity-split.md`.

2. **C₅ acts on a different object — the Bring resolvents, not the trace.**
   The `χ_ζ = ζ⁻¹σ + ζ⁻²c_r + ζ⁻³c_g + ζ⁻⁴c_b` character
   ([`aggregate-color-quantities.md`](../../content/quantum-observable-universe/brings-surface/aggregate-color-quantities.md) L12)
   and the cyclic action `w_k ↦ ζ⁻ᵏ w_k`
   ([`c5-color-tube.md`](../../content/quantum-observable-universe/brings-surface/c5-color-tube.md) L1-14)
   are applied to the **Lagrange resolvents / color-tube coordinates** of
   the Bring quintic — the geometric `(σ, c_r, c_g, c_b)` of
   `ℙ¹(ℂ) × 𝔸³` ([`color-tube-interpretation.md`](../../content/quantum-observable-universe/brings-surface/color-tube-interpretation.md) L4-24).
   The C₅ ζ-action is **never applied to the Markov trace / Jones
   polynomial** anywhere in the corpus. Color is a grading on the *Bring
   geometry*; mass-modulus is on the *Hecke Markov trace*. Different objects
   ⇒ the phase of one cannot be the character of the other.
   The `U(1)` longitudinal "σ-backbone" in
   [`spectral-dynamics.md`](../../content/quantum-observable-universe/brings-surface/spectral-dynamics.md) L7
   / [`color-tube-interpretation.md`](../../content/quantum-observable-universe/brings-surface/color-tube-interpretation.md) L20-24
   is the space-like resolvent mode, again a Bring-geometry U(1), distinct
   from the trace-phase U(1) — but both are continuous, neither is C₅.

## Numerical corroboration (`/tmp/phase_probe.py`, mpmath 50 dps)

Jones convention `J = tr_M(ρ(β))`, variable `t = q`,
`J_{3₁} = −t⁻⁴+t⁻³+t⁻¹`, `J_{4₁} = t⁻²−t⁻¹+1−t+t²`, on `q = e^{iθ}`.
`distC5` = distance of arg to nearest `{2πk/5}`.

| test | result |
|---|---|
| **(a) smoothness** | arg(J_{3₁}) sweeps **continuously** (−0.021, −0.135, −0.347, −0.628, −0.955, −1.32, … wraps at −π, returns). `distC5` is generic everywhere (0.02–0.63), never pinned to 0. → continuous U(1), not discrete. 4_1 amphichiral: arg ∈ {0, π} (real Jones). |
| **(b) at ζ₅ʲ** | arg(J_{3₁}) = ∓2.1226, ∓1.4265 for j=1..4. `2π/5 = 1.2566`; distances 0.39, 0.17 — **NOT** on the C₅ lattice. |
| **(c) Galois j→2j** | the action permutes eval points; arg follows the values at permuted points, which are continuous, **not** χ_ζ-character outputs. |
| **(d) framing (−q³)⁻ʷ** | phase shifts by **exactly w·(linear-in-θ)**: at θ/π=0.2, w=0→−0.628, w=1→+0.628, w=3→−π. Dominated by a `w·(continuous θ)` term = the **U(1) framing phase**. Decisive. |

## Consequence for authoring (do NOT write a "color = phase" conjecture)

- The discarded phase `arg(tr_M)` **is** the EM/Im-of-𝔙 / Chern–Simons /
  framing channel (bar-odd, `Q_β`/`sinh`/weak). It is already correctly
  homed in `complex-volume-intro`, `bar-parity-split`,
  `chirality-period-pairing`, `em-coupling-chern-simons`.
- "Color" is a genuinely separate **C₅ Galois** object on the Bring
  resolvents. A conjecture equating the two would be false; the
  formalize-first invariant that kills it is: *the trace-phase is a
  continuous function of θ (winding number ≠ 0, framing-linear), whereas a
  C₅ character takes values only in the discrete group μ₅* — probe (d) shows
  the phase is framing-linear, so it cannot factor through μ₅.

## Provable Lean gate (if anyone re-pitches color = phase)

The refuting lemma is a **discreteness/continuity contradiction**, not a
numerics fit: a C₅-character-valued invariant `c: Knots → μ₅ ⊂ U(1)` is
locally constant under continuous deformation of the evaluation point `θ`,
while the framed-trace phase satisfies
`arg J(e^{iθ}; framing w) = 2 w c(λ) θ + arg V(e^{iθ})` with
`d/dθ ≠ 0` (probe (d)). A formal statement: *no group hom
`μ₅ → U(1)` reproduces a θ-linear (winding) phase* — `μ₅` is finite, its
image in `U(1)` is the 5th-roots subgroup, which contains no nonconstant
continuous path. This is the Lean gate that should be cited to decline any
future "color = arg(tr_M)" conjecture.

## Refinement (owner, S₃→S₅): color IS on the trace algebra — but as a discrete grading, not the phase

The verdict above (phase = U(1), **not** color) **stands**. But claim #2's
phrasing — "C₅ acts on a *different object*, never the trace" — is too strong,
and the owner's S₃→S₅ observation pins down why.

**Color lives in the Hecke trace algebra after all.** A "photon with color
content `(φ₀,φ₁,φ₀₁)`" is literally an element
`γ = 𝟏 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁ ∈ H₃(q)`
([`knot-basis-color-content.md`](../../content/quantum-observable-universe/brings-surface/knot-basis-color-content.md) L1-22),
with σ₀,σ₁ the **color axes** and the σ₀σ₁ term the *cross-color* Hopf
dressing. That is the *same* Hecke algebra family the Markov trace acts on.

**The bridge is 2 + 3 = 5.** The embeddable strand counts give
`H₂(q) ⊕ H₃(q)` with `2 + 3 = 5` total irreps — the Bring fivefold
([`cohomological-embedding.md`](../../content/quantum-observable-universe/brings-surface/cohomological-embedding.md) L125-132),
and the Markov trace decomposes `V = Σ_{λ⊢r} d_λ χ_λ` over them.

**The coordinate split.** Bring's 5 coordinates split
`(x₀,x₁)=spacetime | (x₂,x₃,x₄)=color`
([`brings-qou-4tuple.md`](../../content/quantum-observable-universe/brings-surface/brings-qou-4tuple.md) L4-10),
the **S₃ permutes the three color sheets while fixing spacetime**
(`:31` → SO(3) holonomy), and there are **three copies of S₃ ⊂ S₅**
([`color-sector-coords.md`](../../content/quantum-observable-universe/brings-surface/color-sector-coords.md) L34-37),
ℤ/3-permuted (r→g→b, ψ+2πk/3), each a trefoil-group quotient ⟨x,y|x²=y³⟩
permuted by the remaining S₅ generators
([`chirality-trefoil.md`](../../content/quantum-observable-universe/brings-surface/chirality-trefoil.md) L5-11).

**Synthesis (one inferential step flagged).** Read `H₂'s S₂ ↔ spacetime`,
`H₃'s S₃ ↔ color`, so `S₂ × S₃ ⊂ S₅` is the Bring Galois group. Then on the
*one* trace object `H₂ ⊕ H₃`:

| quantity | reads | sector | character |
|---|---|---|---|
| **mass** | `\|tr_M\|` (modulus) | both | — |
| **EM** | `arg tr_M` (U(1) framing/CS) | spacetime / `S₂` | continuous |
| **color** | `S₃` irrep grading (φ₀,φ₁,φ₀₁) | color / `S₃` | discrete |

**"Recover color from within U(1)/EM"?** Because the **S₃ fixes spacetime**,
color and EM are *orthogonal at the S₂×S₃ level* — the discrete color label is
**not** extractable from the single continuous U(1) phase (the phase verdict is
unaffected). They are unified **one level up**: the S₅ generators *outside*
S₂×S₃ rotate spacetime indices into color indices. So color↔EM is real, but it
is an **S₅** statement, not a U(1) statement.

**Provable Lean targets (this is "does it come together").**
1. `S₂ × S₃ ↪ S₅` injective, via `Equiv.Perm.sumCongrHom (Fin 2) (Fin 3)`
   transported along `finSumFinEquiv`; the `S₃` factor (color) fixes the
   `Fin 2` (spacetime) block pointwise — formalizes "S₃ keeps spacetime
   invariant". The `2+3=5` index split is `Fintype.card (Fin 2 ⊕ Fin 3) = 5`.
2. Polar/Cartesian decomposition `tr = |tr|·exp(i·arg tr)`
   (`Complex.abs_mul_exp_arg_mul_I`) — mass = modulus, EM = phase, on one
   object; complements `complex_volume_unification` (Re + i·Im = 𝔙).
3. The refuting gate (color ≠ phase): no group hom `μ₅ → U(1)` carries a
   θ-linear winding phase (finite image ⇒ locally constant).

These are recorded/attempted in
`content/quantum-observable-universe/mass-endomorphism/color-spacetime-s5-factorization.lean`
(investigation Lean; see commit log).

## Note: residual ambiguity (minor, does not change verdict)

At root-of-unity `q = ζ_N` the colored-Jones / WRT story does involve `N`
and cyclotomic projections (`mass-endomorphism-conjecture.md` L153-220),
and the C₅ resolvents are *also* a μ₅ structure — so there is a shared
"5-ness" in the Bring substrate. But the *phase of the mass trace* is the
**continuous winding** channel (framing/CS), and the *C₅ color* is the
**discrete grading on the resolvents**; the corpus keeps them on distinct
objects and the numerics show the trace phase is not μ₅-valued. The only
probe that could surface a genuine coupling would be checking whether the
*writhe / self-linking* `w(β)` of a Bring-embeddable braid is itself
C₅-graded — but that would be a property of `w`, not of `arg(tr_M)`, and
still would not make the phase a color character.
