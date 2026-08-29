/-
  Fine structure constant — PSLQ-empirical gluon-octet form (CONJECTURE).

  1/α_EM = 45·[3]_q · (1 + δ_CS + 8q·δ_CS²)

  where δ_CS = ℏ_q^4 · [5]_q,  ℏ_q = (q-1)/q.

  STATUS (May 2026 audit): demoted from theorem to conjecture.
  Of the four factors:
    45     = (10 choose 2)        — derivation rigorous (hook-length count)
    [3]_q  — claimed quark-channel weight; q-dim of V_(2,1) in H_3 is
             [2]_q, NOT [3]_q. Identification is unsupported.
    ℏ_q^4 · [5]_q — claimed leading Plancherel-character-product term
             at n=10; the leading-term computation has not been carried
             out, ambient n unspecified.
    8q     — two competing identifications (su(3) gluon octet × q;
             "two-step crossing pattern enumeration"); neither computed.

  At q = q_0 the formula matches CODATA to 6.7e-9. Outside q_0 it
  disagrees with the alternative Chern-Simons-descent form
  (also conjectural) at every q, indicating a single-point fit.

  PSLQ uniqueness at 1000 dps over a 52-element basis is real but does
  not prove canonicity — it shows no SHORTER relation exists in the
  chosen basis.

  See alpha-em-derivation-open-problems.md for the full audit and
  derivation roadmap.
-/

import QOU.Archimedean.EmCouplingProjection
import QOU.Mass.QHookDimensionBalanced

namespace QOU.ArchimedeanUniverse

open QOU.Mass.QHookDimensionBalanced (qIntBal)

/-! ## Which `q`-integer? — resolved by the file's own target (bean `qou-pjfu`)

This file was **red on `main`**: `qInt` was neither defined nor imported
(`Unknown identifier` at the two call sites below). Repair required choosing
between two conventions in the corpus, which the bean correctly declined to
guess:

* the **geometric** `qInt q k = ∑_{j<k} q^j`
  (`FluidDynamics.surreal_enstrophy_finite_modes`, `MathlibExt.QIntegerFactorial`);
* the **balanced** `[k]_q = (q^k − q^{−k})/(q − q^{−1})`, the Hecke convention of
  AGENTS.md §7a (`Mass.QHookDimensionBalanced.qIntBal`, `IwahoriHecke.qBracket`).

It is **decidable rather than a preference**, because `alphaEmInvCorrected`
targets a measured constant. Evaluating both at the substrate anchor:

| convention | `[3]` | `[5]` | `α_EM⁻¹` | vs CODATA `137.035999177` |
|---|---|---|---|---|
| geometric | 3.342031 | 6.2275361 | 150.4821415 | **9.8 % off** |
| **balanced** | 3.0437062 | 5.2204413 | **137.0359995** | **2.6 ppb** |

So the intended object is the **balanced** `[k]_q`, and this file now uses the
existing `qIntBal` rather than adding a sixth `qInt` to the corpus. The argument
order also flips: `qIntBal` is `(q, n)` where the old call sites were `(k, q)`.

**Scope — what this does and does not establish.** It fixes the *identification*
of a symbol, not the physics. The 2.6 ppb agreement carries no evidential weight
for the formula: `κ = 8q` is described in this very file as *empirical*, with
*"no structural derivation linking su(3) gluon dimension to α_EM"*, so the form
was shaped against this target. The number is used here only as a **fingerprint**
to recover which function the author meant — the legitimate use of a known value.
The conjecture below stays a conjecture.

-- Ref: [manuscript] bean `qou-pjfu`
-/

/-- Chern-Simons invariant of a torus knot T_{m,n}. -/
noncomputable def chernSimons (m n : ℕ) : ℝ :=
  Real.pi ^ 2 * ((m ^ 2 - 1) * (n ^ 2 - 1)) / (12 * m * n)

/-- The δ_CS correction in the gluon-octet form: ℏ_q^4 · [5]_q, with `[·]`
the **balanced** quantum integer (see the note above). -/
noncomputable def deltaCS_gluonOctet (q : ℝ) : ℝ :=
  ((1 - 1/q) ^ 4) * qIntBal q 5

/-- The κ coefficient in the gluon-octet form is `8q`.

    **The "8 = dim(su(3)) = gluon octet" reading is post-hoc** — no structural
    derivation links the su(3) gluon dimension to α_EM, and this docstring said
    so, correctly.

    **But the corpus supplies a different and exact reading of the same 8**
    (found 2026-08-28, bean `qou-aemx`). The Borromean rings `L6a4` — the
    nucleon knot of this framework — have hyperbolic volume

        Vol(𝓑₃) = 2 · V_oct = 8G,      G = Catalan's constant,

    since a regular ideal octahedron has `V_oct = 4G`. Verified to 30 digits.
    That identity is already live and load-bearing elsewhere in the corpus —
    the nucleon row of `fundamental-knots-operator-basis`, and the binding
    scale `α = m_e · 8G` in `binding-knots-visual-inventory` — and it is the
    reading `computations/_deprecated/alpha_em_q9_q10_derivation.py` gives:
    `κ = 8q = q · Vol(𝓑₃)/G`.

    So `8` here is not a fitted integer; it is `Vol(𝓑₃)/G`, exactly. The
    su(3)-octet gloss was the wrong gloss on a right number.

    **What is still NOT derived, and must not be read as closed.** Why the
    combination is `q · Vol(𝓑₃)/G` rather than `Vol(𝓑₃)/G` or `q² · Vol(𝓑₃)/G`
    is unaddressed; and why the *nucleon* knot's volume should set a coefficient
    in an *electromagnetic* coupling needs its own argument. Measured, the κ
    window admitting |err| < 100 ppb against CODATA is `[8.474, 9.265]`, which
    also contains the integer 9 — so `8q` is IN RANGE, not FORCED. Bare `κ = 8`
    does miss it (−220 ppb), which is consistent with the `q` belonging to the
    structure rather than being a fudge, but is not a derivation of it. -/
noncomputable def gluonOctetKappa (q : ℝ) : ℝ := 8 * q

/-- The corrected inverse fine structure constant via gluon-octet form. -/
noncomputable def alphaEmInvCorrected (q : ℝ) (hq : q > 1) : ℝ :=
  let prefactor := 45 * qIntBal q 3
  let δ := deltaCS_gluonOctet q
  let κ := gluonOctetKappa q
  prefactor * (1 + δ + κ * δ ^ 2)

/-- The conjectural gluon-octet identity, axiomatised as a class.

    -- Ref: [manuscript]
    Was a `theorem` with `sorry`; demoted to class after audit
    (only `45` of four factors has a structural derivation).
    Downstream results may take this class as an explicit
    `[Instance]` hypothesis to obtain conditional consequences;
    the instance itself is the unproved conjectural input. -/
class AlphaEmGluonOctetConjecture (q : ℝ) (hq : q > 1) : Prop where
  matches_codata :
    |alphaEmInvCorrected q hq - 137.035999177| < 1e-6

/-- The **Chern-Simons-form** conjecture (distinct from the
    PSLQ gluon-octet form above). States the algebraic identity

        1/α = q · [9]_q · [10]_q · (1 + δ_CS/(1 − δ_CS·κ))

    where `κ` is a Gram-determinant ratio from the Chern-Simons
    pairing on Bring's surface. Per `conj:em-coupling-chern-
    simons`, the algebraic content is the existence of such a
    Gram-determinant `κ` making the identity hold.

    **Docstring corrected 2026-08-29** (bean `qou-aemx`). This read
    `(1 + δ_CS + κ · δ_CS²)`, which the block's `.md` names as the form
    it *previously* displayed. The live `.md` gives the resummed form
    above: the tower `Σ_{j≥1} δ_CS^j κ^{j−1}` is geometric with ratio
    `δ_CS·κ ≈ 2.7e-3`, so it sums in closed form and **has no truncation
    order to choose** — which is the point of resumming, since a chosen
    truncation order is a free parameter.

    Re-derived at 50 dps at the proton-pinned `q₀`, with the Witten-1988
    `κ ≈ 1.722`: resummed `137.0359352` (−466.7 ppb vs CODATA-2022),
    truncated `137.0359337` (−477.8 ppb). The truncation costs
    **11.07 ppb**, reproducing the `.md`'s stated `11.06`.

    Only this docstring changed. The `opaque` Prop below is untouched and
    still has **no instance** — what the conjecture asserts, which `κ` it
    asserts it of, and whether the claim is algebraic or numerical are
    author decisions, not a docstring repair. See the note after the class.

    Per `AGENTS.md §3b-cond`, encoded as opaque Prop + class
    field. Algebraic tier only — numerical CODATA match deferred
    to a future Archimedean tier per gemini #721 rule. -/
opaque ChernSimonsGramDeterminantIdentityHolds (q : ℝ) (hq : q > 1) : Prop

/-- **Chern-Simons-correction conjecture** (class-axiomatized
    per §3b-cond). Distinct from `AlphaEmGluonOctetConjecture`. -/
-- Ref: [manuscript] conj:em-coupling-chern-simons
class ChernSimonsCorrectionConjecture (q : ℝ) (hq : q > 1) : Prop where
  identity_holds : ChernSimonsGramDeterminantIdentityHolds q hq

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the field(s) below, which is
-- exactly the open conjecture; supplying one asserts the conjecture.
--
-- History: this file previously carried
--     instance chern_simons_correction_conjecture (q : ℝ) (hq : q > 1) :
--     axiom chern_simons_correction_identity_holds : ∀ (q : ℝ) (hq : q > 1), ChernSimonsGramDeterminan
-- i.e. the conjecture was discharged by `axiom` and installed as a global
-- instance, so every downstream `[ChernSimonsCorrectionConjecture q hq]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  Removed, not completed.
-- Downstream results must take `[ChernSimonsCorrectionConjecture q hq]` as an explicit hypothesis.

/-! ## The resummation, proved

What separates the block's live form from the one its `.md` supersedes is not a
value of `κ` — it is whether the correction tower may be summed in closed form at
all. That question needs no `κ`, no CODATA and no anchor, so it is settled here
rather than deferred with the rest.

The two lemmas below are unconditional, sorry-free, and carry no fitted input.
They do **not** close the conjecture: what stays open is which `κ` the Gram
determinant actually yields, and that is the numerical tier this file's standing
ruling defers. See the note on `ChernSimonsGramDeterminantIdentityHolds`. -/

/-- **The correction tower resums.** For `|δκ| < 1`,

    Σ_{j≥1} δ^j κ^{j-1} = δ / (1 - δκ)

This is the content of the block's live statement `1 + δ_CS/(1 - δ_CS·κ)`: the
closed form is not an approximation of the tower, it **is** the tower, so there
is no truncation order to choose. That matters beyond tidiness — a chosen
truncation order is a free parameter, and the superseded form had one. -/
theorem csTower_resums (δ κ : ℝ) (h : |δ * κ| < 1) :
    ∑' j : ℕ, δ ^ (j + 1) * κ ^ j = δ / (1 - δ * κ) := by
  have hnorm : ‖δ * κ‖ < 1 := by rwa [Real.norm_eq_abs]
  have hterm : ∀ j : ℕ, δ ^ (j + 1) * κ ^ j = δ * (δ * κ) ^ j := by
    intro j; rw [mul_pow, pow_succ]; ring
  rw [tsum_congr hterm, tsum_mul_left, tsum_geometric_of_norm_lt_one hnorm,
    div_eq_mul_inv]

/-- **The superseded form is the tower's second partial sum.** The order-`δ_CS²`
expression `δ + κδ²` is exactly `Σ_{j=1}^{2} δ^j κ^{j-1}`.

Stated so that "its second-order truncation" is a proved identity rather than a
remark. Together with `csTower_resums` this makes the relationship between the
two forms a theorem: same series, one summed and one cut. -/
theorem csTower_partialSum_two (δ κ : ℝ) :
    ∑ j ∈ Finset.range 2, δ ^ (j + 1) * κ ^ j = δ + κ * δ ^ 2 := by
  simp [Finset.sum_range_succ]
  ring

end QOU.ArchimedeanUniverse
