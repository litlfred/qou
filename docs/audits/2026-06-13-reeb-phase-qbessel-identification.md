# The Reeb-phase objects are q-special functions in disguise (2026-06-13)

## Status: owner-requested exposition + structural identification

This note answers "where do Bessel / Bessel-like functions play a role?"
and makes explicit a claim that has been implicit across the Q_β `c_3`
residue-A program: **the framework's home-grown Reeb-phase / Markov-trace
objects are, term for term, the standard q-special functions of the
quantum group $\mathrm{SU}_q(2)$ — Chebyshev / little-q-Jacobi matrix
coefficients in the bounded (rotation) regime, and Hahn–Exton q-Bessel
functions in the contraction (brane-tower) limit.**

Nothing here is wired to production, nothing is fitted, and no `c_3`
closure is claimed. The value is (a) a citation trail to the q-special-
function literature the corpus was missing, (b) a *structural* (derive-or-
refute) reframing of two stuck items — the f-map refutation and the #1839
"no low-order C-finite recurrence" finding — as the *generic* behaviour of
q-Bessel coefficients rather than dead ends. Discipline gates (three-
calibration; no 7th fit; report TIERED; Im(q)/regime explicit) are
respected throughout.

Companion compute + Lean (this PR):

- `computations/qbeta/qbeta_reeb_tower_jacobi_anger.py`
  — verifies the bar-graded Jacobi–Anger identity and runs the falsifiable
  tower test.
- `computations/qbeta/qbeta_qbessel_contiguity_cfinite.py`
  — constructs the Hahn–Exton q-Bessel, verifies its q-difference
  equation + three-term contiguity + the `q → 1` limit, and derives the
  `c_k` coefficient recurrence from contiguity.
- `QOU/QBeta/ReebTowerJacobiAnger.lean` — the bar-graded three-term
  recurrence and the rotation/growth = `J_ν`/`I_ν` unification (Bessel-
  free, sorry-free).
- `QOU/QBeta/QBesselContiguityRecurrence.lean` — q-Bessel three-term
  contiguity ⟹ order-2 coefficient recurrence; the C-finite case as its
  constant-coefficient degeneration.

---

## 1. The two literal "Bessel" mentions, made precise

Before this PR the string "Bessel" appeared in exactly two places, both as
an informal analogy in the `c_3` residue-A work:

1. `docs/scope/2026-06-05-qbeta-perblock-collapse-order-scope.md` calls the
   observe-last sum `Σ_λ y_λ |sinh(k_λ η)|` **"(Bessel-like)"** — "a weighted
   sum of different-order sinhs whose effective order is η-dependent … with
   no single ℓ to anchor-lock."
2. `qbeta_reeb_sinh_fmap_brane_tower_probe.py` floats **"Bessel-style
   profiles"** as a way the refuted f-map family could be broadened.

Both intuitions are exactly right, and the precise statement is the
**hyperbolic Jacobi–Anger expansion**. Writing `q = e^η`, `η = log q₀`,
and using the ordinary-Bessel generating function
`e^{(x/2)(t − 1/t)} = Σ_n J_n(x) t^n` at `t = e^η`:

$$
e^{x\,\sinh\eta} \;=\; \sum_{n=-\infty}^{\infty} J_n(x)\,e^{n\eta}
\;=\; J_0(x) + 2\!\sum_{m\ge1} J_{2m}(x)\cosh(2m\eta)
            + 2\!\sum_{m\ge0} J_{2m+1}(x)\sinh\big((2m{+}1)\eta\big).
$$

Splitting into bar-parity sectors (`η ↦ −η`; `cosh` even, `sinh` odd):

$$
\boxed{\;\cosh(x\,\sinh\eta) = J_0(x) + 2\!\sum_{m\ge1} J_{2m}(x)\,\cosh(2m\eta)\;}
\qquad\text{(bar-EVEN — the } c_2 \text{ sector)}
$$
$$
\boxed{\;\sinh(x\,\sinh\eta) = 2\!\sum_{m\ge0} J_{2m+1}(x)\,\sinh\big((2m{+}1)\eta\big)\;}
\qquad\text{(bar-ODD — the } c_3 \text{ sector)}
$$

This is the exact content of "Bessel-like": the bar-odd generating
function `sinh(x sinh η)` expands in **odd-order** `sinh((2m+1)η)` only,
with weights the **ordinary Bessel** values `J_{2m+1}(x)` — precisely the
"effective order is η-dependent, no single ℓ" structure the scope doc
described, and exactly matching `QBeta.CoherentCollapseSinhCosh`
(`χ^(2,1)(σ_1) = 2 sinh η` is pure bar-odd; `c_3` lives in the odd-sinh
sector).

**Honest caveat (the discipline-critical point).** A single `λ ⊢ n` trace
is a *finite* sum of a few `sinh(k_λ η)` terms — it is **not** a Bessel
function. The Bessel object is the **infinite brane-tower / contraction
limit**. So the correct claim is not "the trace is Bessel" but:

> The f-map refutation — "no single integer level `ℓ` reproduces `c_3` at
> both anchors" (`qbeta_reeb_sinh_fmap_brane_tower_probe.py`, NEGATIVE) —
> is the **signature of a full `J_n` superposition**, in which no single
> term dominates, rather than evidence that the brane-tower idea is wrong.

That reframes a numerical dead end as a structural prediction with a
sharp, falsifiable test (§4).

---

## 2. The standard quantum role: Hahn–Exton q-Bessel = $E_q(2)$ matrix coefficients

The deepest connection is not an analogy at all. The framework's substrate
category is $\mathbf{Rep}(\mathrm{SU}_q(2))$, and the harmonic analysis of
$\mathrm{SU}_q(2)$ and its contraction $E_q(2)$ **is** the theory of
q-Bessel functions. The classical template and its q-deformation:

| | Classical | Quantum |
|---|---|---|
| Compact group | $\mathrm{SU}(2)\cong S^3$ | $\mathrm{SU}_q(2)$ |
| Matrix coefficients | Jacobi polynomials $P_n^{(\alpha,\beta)}$ | **little q-Jacobi** polynomials |
| Motion group (contraction) | $E(2)=\mathbb{R}^2\rtimes\mathrm{SO}(2)$ | **$E_q(2)$** (quantum plane motions) |
| Its matrix coefficients | **Bessel** $J_\nu$ (Vilenkin) | **Hahn–Exton q-Bessel** $J_\nu^{(3)}(\cdot\,;q)$ |
| Contraction limit | $\mathrm{SU}(2)\to E(2)$: Jacobi → Bessel (Mehler–Heine) | $\mathrm{SU}_q(2)\to E_q(2)$: little-q-Jacobi → q-Bessel |

The quantum statement is a theorem:

> **(Vaksman–Korogodsky 1989; Koelink 1994.)** The matrix coefficients of
> the irreducible unitary representations of the quantum group of plane
> motions $E_q(2)$ are Hahn–Exton q-Bessel functions $J_\nu^{(3)}(x;q)$
> (Jackson's "third" q-Bessel). Equivalently, the q-Bessel functions are
> the $\mathrm{SU}_q(2)\to E_q(2)$ contraction limit of the little
> q-Jacobi polynomials, mirroring Vilenkin's classical
> $J_\nu = $ matrix-coefficient-of-$E(2)$.

The Hahn–Exton q-Bessel function is, in the Gasper–Rahman normalisation,

$$
J_\nu(x;q) \;=\; x^{\nu}\,\frac{(q^{\nu+1};q)_\infty}{(q;q)_\infty}\;
{}_1\phi_1\!\big(0;\,q^{\nu+1};\,q,\,q x^{2}\big)
\;=\; x^{\nu}\,\frac{(q^{\nu+1};q)_\infty}{(q;q)_\infty}
\sum_{k=0}^{\infty}\frac{(-1)^k\,q^{k(k-1)/2}}{(q;q)_k\,(q^{\nu+1};q)_k}\,
\big(q x^{2}\big)^{k},
$$

it satisfies a **second-order q-difference equation** (the q-Bessel
equation) and the q-analogue of Bessel's **three-term contiguity**
$J_{\nu-1}+J_{\nu+1}=\tfrac{2\nu}{x}J_\nu$, and Koelink–Swarttouw (1994)
built the **q-Hankel transform** from the orthogonality of its zeros.
As `q → 1⁻`, `J_ν(x;q) → J_ν(x)` (ordinary Bessel).

---

## 3. The dictionary: home-grown object ↔ q-special function

Every "home-grown" object the corpus computes with has a name in the
q-special-function literature. This is the table the corpus was missing.

| QOU home-grown object (where) | q-special-function identity | Classical (`q→1`) shadow |
|---|---|---|
| Reeb phase `η = log q₀`; generators `h = q−q⁻¹ = 2 sinh η`, `[2]_q = q+q⁻¹ = 2 cosh η` (`CoherentCollapseSinhCosh.lean`) | the `q = e^η` uniformiser of `U_q(𝔰𝔩₂)`; q-integer `[n]_q = sinh(nη)/sinh η` | `[n]_q → n` |
| Wedderburn character `χ^λ`, **rotation** regime `|χ^λ/dim_λ| ≤ 1`, `θ_λ = arccos` (`binding_reeb_phase_decomposition.py`) | little-q-Jacobi / q-Krawtchouk matrix coefficient; Chebyshev `U_{n−1}(cos θ)` | `SU(2)` character `sin(nθ)/sin θ` |
| Wedderburn character, **growth** regime `|χ^λ/dim_λ| > 1`, `θ_λ = arccosh` (same) | `SU_q(1,1)` / `E_q(2)` regime; Chebyshev `U_{n−1}(cosh η)` | modified-Bessel `I_ν` regime |
| brane-tower level sum `Σ_ℓ w_ℓ sinh(ℓη)` ("Bessel-like", scope §9.2) | Jacobi–Anger `sinh(x sinh η) = 2 Σ_m J_{2m+1}(x) sinh((2m+1)η)`; contraction limit = Hahn–Exton q-Bessel matrix coeff of `E_q(2)` | Fourier–Bessel `J_ν` |
| `c_k` ladder q-difference kernel `R`, `F(qξ)=R·F(ξ)` (#1839, #1880; `RationalCoeffRecurrence.lean`) | the q-Bessel **second-order q-difference operator**; its contiguity = the coefficient recurrence | Bessel ODE + contiguity |
| rotation/growth dichotomy `arccos`/`arccosh` (`binding_reeb_phase_decomposition.py`) | `J_ν` vs `I_ν` via `I_ν(x) = i^{−ν} J_ν(ix)` | same |
| Markov parameter `z = √q/(1+q)` (`qbeta_utils.markov_parameter`) | `√q` half-integer uniformiser of the q-line | `z → 1/2` |

Reading the table top to bottom: the **rotation channels are the `J_ν`
(bounded, oscillatory, `cos`) world**, the **growth channels are the
`I_ν` (unbounded, exponential, `cosh`) world**, and the **two are one
object** — `I_ν(x) = i^{−ν}J_ν(ix)` is exactly the analytic continuation
`η ↦ iη` that swaps `arccosh ↔ arccos`. The binding probe's
rotation/growth split (`binding_reeb_phase_decomposition.py:109`,
`acos` vs `acosh`) is literally the `J/I` split.

---

## 4. Structural payoff (derive-or-refute, nothing wired)

### 4a. The falsifiable tower test (compute #1)

The bar-odd character data at `λ ⊢ 3` gives a finite set of
`{(k_λ, weight_λ)}`. The Jacobi–Anger boxed identity predicts that, **if**
the bar-odd sector is the brane-tower / contraction object, the weights
are the Bessel values `2 J_{2m+1}(x)` at a **single substrate-fixed**
`x = x(q₀)`, with orders `2m+1`. The test (run in
`qbeta_reeb_tower_jacobi_anger.py`):

- Solve for `x` from the leading (`m = 0`) term at the proton anchor.
- **Cross-anchor gate** (identical in spirit to the f-map's "same integer
  `ℓ` at both anchors"): does that *same* `x(q₀)` reproduce the bar-odd
  data — and the `c_3` cross-anchor swing — at the muon anchor, with **no
  per-anchor refit**?
- PASS ⟹ first structural identification of the bar-odd tower as the
  Hahn–Exton q-Bessel matrix coefficient. FAIL ⟹ a clean refutation, on
  the same footing as the f-map, with the mismatch quantified.

Either branch is a structural result, not a curve fit. Reported TIERED;
`c_3` stays cal-anchored regardless.

### 4b. q-Bessel contiguity explains the #1839 recurrence finding (compute + Lean)

PR #1839 found: the canonical `c_2..c_10` admit **no constant-coefficient
linear recurrence of order ≤ 4**, yet the tail dominant root equals
`1/u_substrate ≈ 117.4` (the pole). `RationalCoeffRecurrence.lean`
formalised the load-bearing fact (pole ⟹ reciprocal is a characteristic
root) under the hypothesis that the fibre object `F` is **rational** (⟹ the
`c_k` are C-finite).

The q-Bessel identification supplies the missing structure:

> The q-Bessel function satisfies a **second-order q-difference equation**;
> its power-series coefficients therefore satisfy an **order-2 linear
> recurrence whose coefficients depend on `q^k`** — they are
> **q-holonomic**, not absolutely constant. A constant-coefficient
> (C-finite) recurrence is the special **degeneration** that occurs only
> when the q-shift is trivial (`q → 1`) or `F` is rational.

So #1839's "no low-order constant recurrence" is exactly what a genuine
q-Bessel kernel predicts: the kernel `R` is the **q-Bessel q-difference
operator** (q-shift-dependent coefficients), and the search for an
*absolutely* constant recurrence was bound to fail while the pole /
dominant-root structure (the leading q-difference singularity) survives.
This is a derivation of the observed phenomenology, not a fit:
`qbeta_qbessel_contiguity_cfinite.py` exhibits the q-difference equation,
the three-term contiguity, the `q → 1` collapse to the constant-coefficient
Chebyshev recurrence, and confirms the dominant-root/pole match.

`QBesselContiguityRecurrence.lean` formalises the algebraic skeleton:
the three-term contiguity (taken as a hypothesis, cited to
Koelink–Swarttouw / Gasper–Rahman) ⟹ the order-2 coefficient recurrence,
with the C-finite case recovered as its constant-coefficient degeneration,
linking back to `pole_reciprocal_is_char_root`.

### 4c. The Lean backbone (proof #3 + #4)

`ReebTowerJacobiAnger.lean` proves the `q → 1` / real backbone that all of
the above rests on, **without** needing a Bessel library in Mathlib:

- the **three-term tower recurrence**
  `sinh((k+1)η) = 2 cosh η · sinh(kη) − sinh((k−1)η)` (and the `cosh`
  analogue), which is simultaneously the Chebyshev-`U` recurrence, the
  `q → 1` Bessel contiguity, and the constant-coefficient kernel of §4b;
- the **rotation/growth = `J`/`I` unification**: the *same* recurrence
  `p_{k+1} = 2t·p_k − p_{k−1}` is solved by `sin(kθ)/sin θ` at `t = cos θ`
  (`|t| ≤ 1`, the `J_ν`/rotation regime) **and** by `sinh(kη)/sinh η` at
  `t = cosh η` (`t ≥ 1`, the `I_ν`/growth regime) — one operator, two
  regimes by `|t| ⋚ 1`.

---

## 5. Discipline gates (standing)

- **Three-calibration; no 7th fit.** The tower test (§4a) is derive-or-
  refute with a cross-anchor gate; a per-anchor refit is a refutation,
  not a result.
- **Im(q) / regime explicit.** Rotation = real `η` (`J_ν`, `arccos`),
  growth = imaginary `η` (`I_ν`, `arccosh`); never silently `.real`.
  `I_ν(x)=i^{−ν}J_ν(ix)` is the bridge, kept explicit.
- **Report TIERED** (proved / near-match / fitted). The Jacobi–Anger
  identity and the q-Bessel q-difference/contiguity are *proved* (math
  facts). Any `c_3` reproduction is at best *near-match* until the
  cross-anchor gate is passed with a substrate-fixed `x`. Nothing wired.

## References

- L.L. Vaksman, L.I. Korogodsky, *An algebra of bounded functions on the
  quantum group of the motions of the plane, and q-analogues of Bessel
  functions*, Soviet Math. Dokl. **39** (1989) 173–177.
- H.T. Koelink, *The quantum group of plane motions and the Hahn–Exton
  q-Bessel function*, Duke Math. J. **76** (1994) 483–508.
  doi:10.1215/S0012-7094-94-07617-0
- H.T. Koelink, R.F. Swarttouw, *On the zeros of the Hahn–Exton q-Bessel
  function and associated q-Lommel polynomials*, J. Math. Anal. Appl.
  **186** (1994) 690–710. doi:10.1006/jmaa.1994.1330
- T.H. Koornwinder, *Orthogonal polynomials in connection with quantum
  groups*, in: Orthogonal Polynomials (P. Nevai, ed.), NATO ASI Ser. C
  **294**, Kluwer, 1990, 257–292.
- G. Gasper, M. Rahman, *Basic Hypergeometric Series*, 2nd ed.,
  Encyclopedia of Mathematics and its Applications **96**, Cambridge
  Univ. Press, 2004. doi:10.1017/CBO9780511526251
