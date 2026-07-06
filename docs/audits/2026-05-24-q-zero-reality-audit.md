# Audit — is $q_0 \in \mathbb{R}$ derived, or assumed?

**Branch**: `claude/gifted-feynman-U7ckD`.
**Date**: 2026-05-24.
**Companion**: triggered by the 1ppb / L2 precision discussion; the
owner asked *"is there an imaginary component of $q_0$ that the
framework has been silently projecting away?"*

This audit answers two questions:

1. **Does the framework actually prove $q_0 \in \mathbb{R}$, or is it
   an implicit / empirical assumption?**
2. **If $q_0$ were complex with $\mathrm{Re}(q_0) = m_\mu / m_e$, does
   the current L2 residual shape support a non-zero $\mathrm{Im}(q_0)$
   hypothesis?**

## TL;DR

| Question | Answer |
|---|---|
| Does anything *force* $q_0 \in \mathbb{R}$? | **No.** Pre-Archimedean substrate is generic `{R : Type*}`. Reality is implicit engineering + empirical, not a theorem. |
| Is $q_0 \leftrightarrow m_n - m_p$ tautological? | **No.** Substrate-derived $\Delta_{pn}$ at real $q_0$ matches CODATA to **−0.53 %** — non-trivial structural content. |
| Does the L2 residual look "imaginary-shaped"? | **No.** The 2.89 % gap is **bar-symmetric** ($m_p$, $m_n$ shift together); the bar-asymmetric channel $\Delta_{pn}$-via-flavor-split is already correct at 305 ppm. The natural complex-$q_0$ signature points the opposite way. |
| Does the codebase already discuss complex $q$? | **Yes, but only $|q|=1$.** Existing content treats $q = e^{i\Theta}$; $|q|>1$ with $\mathrm{Im}(q) \neq 0$ is uncharted. |

**Verdict**: $q_0 \in \mathbb{R}$ is an *empirical commitment*, not a
theorem. A complex $q_0$ with $|q_0| > 1$ is structurally admissible
in the pre-Archimedean substrate but is *not* the natural explanation
for the dominant 2.89 % L2 gap. The categorical lift is interesting
infrastructure to formalize; the precision payoff is uncertain.

## 1. Where is $q_0 \in \mathbb{R}$ actually pinned?

The reality of $q_0$ shows up in four places. None of them is a
derivation; each is an engineering or empirical commitment that can
be relaxed.

| Site | What it requires | Why |
|---|---|---|
| [`q_parameter.py`](../../computations/substrate/q_parameter.py), `Q_50_DIGIT_STR` | 50-dps real decimal string | Hardcoded; uses `math.sqrt` and `mpmath` (real arbitrary precision). No complex capability. |
| [`markov-trace-factorization.lean`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-factorization.lean):27–47 | `(q : ℝ)` with `hq : 1 < q` | Uses `Real.sqrt`, `Real.rpow`; `linarith` requires ordered field. |
| [`hoefsmit-V21-cos-symmetrization.lean`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-V21-cos-symmetrization.lean) | `Real.sqrt q` for seminormal entries | Orthogonality of Hoefsmit basis requires $q > 0 \in \mathbb{R}$. |
| Archimedean functor (`canonical-derivation-cheat-sheet.md` step 9) | $\tau : \mathbf{C} \to \mathrm{Vec}_\mathbb{R}$ | Codomain $\mathbb{R}$ is **axiomatic** to the functor definition, not derived. |

Conversely, the pre-Archimedean substrate is **already** generic:

| Site | Ring | Note |
|---|---|---|
| [`hq-bi-filtration.lean`](../../content/quantum-observable-universe/braids-and-knots/hq-bi-filtration.lean) | `{R : Type*}`, `{q : R}` | No ordering. |
| [`explicit-central-idempotent.lean`](../../content/quantum-observable-universe/braids-and-knots/explicit-central-idempotent.lean) | `{R : Type*}`, `{q : R}` | Polymorphic. |
| [`categorical-q-lie-bracket.lean`](../../content/quantum-observable-universe/quantum-observable-universes/categorical-q-lie-bracket.lean) | `R_q := LaurentPolynomial ℤ` | Symbolic $q$. |
| [`bar-involution.ts`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.ts) | Hecke algebra over arbitrary CommRing | $q \mapsto q^{-1}$ requires only invertibility. |
| `def:frobenius-hopf-substrate` ([`frobenius-hopf-substrate.md`](../../content/quantum-observable-universe/quantum-observable-universes/frobenius-hopf-substrate.md)) | Non-degenerate bilinear pairing | No Hermitian / $\ast$-structure imposed. |

**Conclusion**: $\S 7\mathrm{c}$ base-ring discipline (`AGENTS.md`) is
**honored** in the substrate. Reality enters only at the Archimedean
realization step, by *definitional choice* of the codomain.

## 2. The $q_0 \leftrightarrow m_n - m_p$ relationship is structural, not tautological

Counter to the owner's worry that the relationship might be a mere
validation check, the substrate-derived identity at *real* $q_0$ is
non-trivial:

$$
m_n - m_p \;=\; M_N \cdot \frac{(q-1)^2 (1 - q^{-4})}{3} \cdot
                \frac{q^{1/2}+q^{-1/2}}{q + q^{-1}}
            \;=\; \frac{M_N}{3} \cdot \hbar_q^2 \cdot h_q \cdot z_{\mathrm{mkv}}^{-1}
            \quad\text{at } q = q_0.
$$

Source: [`flavor-dressed-mass-from-substrate-split.md`](../../content/quantum-observable-universe/braids-and-knots/flavor-dressed-mass-from-substrate-split.md):9–33.

- Evaluated at real $q_0 \approx 1.1098$, this predicts CODATA
  $m_n - m_p$ to **−0.53 % residual** (within the 1 % gate);
  see [`probe_flavor_dressed_mass_split.py`](../../_deprecated/probes/probe_flavor_dressed_mass_split.py):214–225.
- The CODATA value $m_n - m_p$ is **not an input** to this formula
  (line 70–87 of the `.md`); it is a *cross-check*, not a fit.
- A complex $q_0$ would alter $\hbar_q = (q-1)/q$ and $h_q = q - q^{-1}$,
  changing the prediction. But Im($q_0$) is *not* a free parameter
  under the 3-calibration discipline — it would need to be either
  (a) determined by $m_\mu / m_e$ via a function we have not yet
  written, or (b) fixed by another structural constraint.

The "tautological on real part" framing is therefore too pessimistic.
The real-$q_0$ derivation already does structural work; whether a
complex lift improves it depends on *what controls Im($q_0$)*, not
on whether the substrate admits Im($q_0$).

## 3. The 2.89 % L2 gap is bar-symmetric, not bar-asymmetric

Per [`per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json)
and [`m-p-borromean-verification-50dps.witness.json`](../../computations/m-p-borromean-verification-50dps.witness.json):

| Observable | Prediction | CODATA | Relative gap |
|---|---:|---:|---:|
| $m_p$ | 965.384 MeV | 938.272 MeV | **+2.89 %** |
| $m_n$ | 966.715 MeV | 939.565 MeV | **+2.89 %** |
| $\Delta_{pn} / M_N$ (flavor-split) | derived | derived | **−305 ppm** (structurally correct) |

The bar-asymmetric channel (the isospin-breaking flavor split) is
already structurally correct. The unexplained residual lives in the
bar-symmetric **common mode** — both nucleons shift together.

A complex $q_0$ with non-zero $\mathrm{Im}(q_0)$ is the *natural*
candidate to explain bar-*asymmetric* gaps (the bar involution
$q \mapsto q^{-1}$ acts non-trivially on Im part). It is *not* the
natural candidate for a common-mode gap. The natural candidate for
that gap is per-knot refinement of $\mathrm{VolDensity}(\mathcal{B}_3)$
(cheat-sheet §5: Bring color-tube weighted averaging, Yekutieli
per-cell curvature, Reading-A geometrisation).

**This does not kill the complex-$q_0$ hypothesis** — a complex $q_0$
could still affect common-mode quantities via $|q_0|^2$ in partition
norms — but it shifts the burden of proof. The hypothesis is not
*explanatorily required* by the current residual shape.

## 4. Existing complex-$q$ infrastructure (unit-circle only)

The codebase already contains one place where complex $q$ is treated:
the **unit-circle deformation** $q = e^{i\Theta}$ in the commutative
limit. Source: [`commutative-chirality-vanishes.md`](../../content/quantum-observable-universe/braids-and-knots/commutative-chirality-vanishes.md):46–54.

There, the bar involution $q \mapsto q^{-1}$ coincides with complex
conjugation $z \mapsto \bar z$, and the pair $(\Phi_q, \mathrm{Li}_2^q)$
becomes a Hermitian-conjugate pair (cheat-sheet §4). This is a
*radius-zero* deformation: $|q| = 1$, opposite to the owner's $|q| > 1$
hypothesis. But it shows the framework already knows how to think
about complex $q$ — extending to general $|q| > 1$ with
$\mathrm{Im}(q) \neq 0$ is a natural categorical lift.

Open structural question (research-grade):

- For real $q$ with $q > 1$: bar = inverse. The two involutions coincide.
- For unit-circle $q = e^{i\Theta}$: bar = inverse = complex conjugate. All three coincide.
- For general complex $q$ with $|q| > 1$: **the two involutions split**.
  - **Lusztig bar**: $q \mapsto q^{-1}$ (algebra anti-involution).
  - **Hermitian $\ast$**: $q \mapsto \bar q^{-1}$ (Lusztig $\circ$ complex conjugation).

The split is the categorical content of "complex $q_0$ might unlock
something". It is currently uninstantiated.

## 5. Implications for the precision program

| Direction | Status after this audit |
|---|---|
| **Complex $q_0$ as a fix for the 2.89 % $m_p$ / $m_n$ gap** | **De-prioritized.** The gap is bar-symmetric; complex $q_0$ doesn't naturally target it. Pursue cheat-sheet §5 VolDensity refinement instead. |
| **Complex $q_0$ as a categorical lift** | **Promote to research-grade.** Pre-Archimedean substrate already admits it; formalizing the Lusztig vs Hermitian split is independently valuable for the bar-symmetric / bar-asymmetric decomposition machinery (cheat-sheet §4). |
| **$\|q\| > 1$ vs $q > 1$ ordering** | **Replace in substrate.** The pre-Archimedean substrate currently uses `q > 1` only because Hoefsmit (post-$\tau$) needs `Real.sqrt`. The substrate proper should state $\|q\| > 1$; the real specialization happens at $\tau$. |
| **The 1ppb (L1) leg** | **Already met.** Internal cross-method `max_rel_delta = 0.0`. L1 is *not* the blocker; the L2 100× target is. |

## 6. Research-grade follow-up: categorical lift to complex $q$

Queued (chosen by the owner 2026-05-24):

1. **Content block: $q_0$ complex extension**
   [`braids-and-knots/q-zero-complex-extension.md` / `.ts` / `.lean`].
   States that the pre-Archimedean substrate is parametric in
   $q \in R$ for `{R : Type*} [CommRing R]`; the real-axis choice
   $q_0 \in \mathbb{R}$, $q_0 > 1$ is one of many valid
   specializations. Substrate identities (bar involution, Frobenius
   pairing, Markov trace, Hecke quadratic) all lift.

2. **Content block: Lusztig bar vs Hermitian $\ast$**
   [`braids-and-knots/lusztig-vs-hermitian-bar.md` / `.ts` / `.lean`].
   Distinguishes $q \mapsto q^{-1}$ (Lusztig, algebra anti-involution)
   from $q \mapsto \bar q^{-1}$ (Hermitian $\ast$). Proves the two
   involutions coincide on the real axis and on the unit circle; on
   general $|q| > 1$ with $\mathrm{Im}(q) \neq 0$ they split. The
   split is the categorical home for any future Im($q_0$) contribution.

3. **Notation update** ([`notation/notation-collisions.md`](../../content/quantum-observable-universe/notation/notation-collisions.md)):
   add a row clarifying $\|q\| > 1$ (pre-Archimedean) vs $q > 1$
   (Archimedean realization at $\mathrm{Im}(q_0) = 0$).

4. **Lean refactor (deferred, separate PR)**: replace
   `(q : ℝ) (hq : 1 < q)` with `(q : ℂ) (hq : 1 < ‖q‖)` in the ~15
   substrate files; provide a `(q : ℝ).toComplex` adapter so existing
   Archimedean callers don't break. This is a multi-day effort and
   should not block the content-block formalization.

Item 1–3 are the deliverable of this branch. Item 4 is its own follow-up.

## 7. What this audit does *not* claim

- It does **not** assert that $q_0$ is complex.
- It does **not** assert that the L2 residual is due to a missing
  Im part.
- It does **not** propose a 4th calibration input.

It claims only that $q_0 \in \mathbb{R}$ is an **engineering / empirical**
commitment, not a theorem; that the pre-Archimedean substrate already
admits complex $q$; and that formalizing the complex lift is
independently valuable infrastructure regardless of whether any
specific Im($q_0$) hypothesis pans out.

## See also

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) §4 (Φ_q vs Li_2^q bar-conjugate pair), §5 (VolDensity refinement queue)
- [`docs/precision-goals.md`](../precision-goals.md) (L1 vs L2)
- [`content/quantum-observable-universe/braids-and-knots/commutative-chirality-vanishes.md`](../../content/quantum-observable-universe/braids-and-knots/commutative-chirality-vanishes.md) (existing $q = e^{i\Theta}$ unit-circle treatment)
- [`content/quantum-observable-universe/braids-and-knots/bar-involution.ts`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.ts) (bar involution as ring-agnostic)
- [`content/quantum-observable-universe/braids-and-knots/flavor-dressed-mass-from-substrate-split.md`](../../content/quantum-observable-universe/braids-and-knots/flavor-dressed-mass-from-substrate-split.md) (structural Δ_pn derivation)
