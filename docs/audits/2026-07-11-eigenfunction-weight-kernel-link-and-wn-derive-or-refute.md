# Eigenfunction relation → weight kernel: the link is ring-class, and wₙ(K) does not close by fit

**Date:** 2026-07-11
**Branch:** `claude/q-stokes-kernel-eigenfunction-y0pso2`
**PR:** [#3545](https://github.com/litlfred/qou/pull/3545)
**Lean:** [`QOU/Mass/BindingEigenfunctionTwoTier.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingEigenfunctionTwoTier.lean)
**Probes:** [`computations/binding_wn_derive_or_refute.py`](../../computations/binding_wn_derive_or_refute.py)
**Builds on:** [2026-06-27 lever1 cyclotomic kernel](2026-06-27-lever1-qinvolution-cyclotomic-kernel.md),
[2026-06-26 q-involution/q-Hermite id](2026-06-26-binding-period-qinvolution-qhermite-identification.md),
[2026-07-03 θ_λ Reeb/na-Stokes jet filtration](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md)

> **Division of labor with [#3534](https://github.com/litlfred/qou/pull/3534)
> (parallel PR, same steer; owner directive "keep both, trim overlap").** #3534
> owns the **numerical wₙ derive-or-refute** (constant-ratio kernel refutation +
> Coulomb-corrected `B_strong` + witness). This PR (#3545) owns the **Lean
> formalization** of the eigenfunction relation + the **adversarial scoping**
> (the fork, the ring-vs-element distinction). Part 3 below is the *corrected
> cross-check* that reconciles the two — not a competing full derivation.

## The question

Does the na-Stokes binding period's **eigenfunction relation** inform the open
**weight kernel** `wₙ(K)` of `conj:binding-manybody-eq-jet-filtration`
(`B(K) = Σ_{n=2}^{A} mₑ·a_D^(n)·wₙ(K)`, `wₙ` the output of a q-difference
recursion `G(qx;q)=R(q,x)G(x;q)`)? And can `wₙ(K)` be closed now?

The na-Stokes period is `a_D^(n)=S(n)/n`, `S(n)=Σ_{λ⊢n} dim_q(λ)` (q-involution
number; `q→1` → involution/telephone numbers, A000085). Its eigenfunction
relation is the monic three-term recurrence `S(n)=S(n−1)+c_n·S(n−2)`,
`c_n:=(S(n)−S(n−1))/S(n−2)`.

## Part 1 — the two-tier eigenfunction structure (Lean-certified)

Exact symbolic + 50-dps numerics (`c_n/[n−1]_q` at the muon-canonical q₀):

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `c_n/[n−1]_q` | 1.000000 | 1.000000 | 1.005390 | 1.016141 | 1.030051 | 1.049498 | **1.071963** |

- **Tier 1 (seed).** `c₂=[1]_q=1`, **`c₃=[2]_q` exact** (`c3_eq_qbr2`, sorry-free).
  From the q-hook closed forms `S(1)=1, S(2)=2, S(3)=2+[2]_q`.
- **Tier 2 (tail).** First deviation `q²·D(4)=(q−1)²·Φ₃` (`D4_habiro_factor`),
  `D(n):=S(n)−(S(n−1)+[n−1]_q S(n−2))`. Universal `(q−1)²` double root +
  cyclotomic leading factor — the Habiro-ring signature.

### Adversarial re-scoping (STRICT — these are in the Lean docstring)

1. **`[n−1]_q` is 2 points, not a pattern.** `c_n−[n−1]_q` is exactly 0 only at
   `n=2,3`; nonzero from `n=4`. `c₂` is near-trivial, so `c₃=[2]_q` is the single
   nontrivial seed coincidence.
2. **"Habiro" = leading-factor only.** `(q−1)²` universal ✓, leading factors
   cyclotomic (Φ₃/Φ₅/Φ₆/Φ₇), but `D(6),D(7),D(8)` carry **non-cyclotomic**
   cofactors (exact factorizations in the probe). "Habiro-class" is a
   ring-membership claim about leading structure, not a purely-cyclotomic claim.
3. **The fork (decisive).** `S(n)` does **not** obey the clean Rogers–Szegő
   recurrence `μ(n)=μ(n−1)+[n−1]_q μ(n−2)`; it forks from the crossing moment
   `μ_q` — **+0.3 % at n=4 → +7.9 % at n=8**. `q→1` limits agree (both `=I(n)`);
   `q₀`-values do not. The clean q-Hermite / **q-Fourier eigenbasis is `μ_q`'s**,
   not `S(n)`'s, and `μ_q` was owner-dropped 2026-06-26 (collapses past ⁴He).

## Part 2 — how the eigenfunction relation informs the weight kernel: (a) ring-class, not determination

The earlier framing "the na-Stokes recurrence supplies `R(q,x)`'s backbone /
is a consistency condition on `R`" is **overstated**. Corrected scope, matching
the [2026-06-27 audit's own caveat](2026-06-27-lever1-qinvolution-cyclotomic-kernel.md)
("not a claim that the towers are the same element"):

- **(a) scope-limited positive.** The binding deviation `D(m)` and the Q_β `c_k`
  ladder both (i) resist low-order q-holonomic closure and (ii) carry cyclotomic
  Habiro structure — corroboration at the **ring** level (both in the
  cyclotomic-completion / Habiro ring).
- **NOT (b).** They are **different localizations** (binding `D(m)`: real-q `ℤ[q]`;
  Q_β `c_k`: `ζ₄`-fibre / complex, leading `√2·Φ₂`). Same ring, **not** the same
  element. The eigenfunction relation gives `wₙ(K)`/`R(q,x)` a *derived target*
  (the `D(m)` tower) to reproduce — it does **not** determine `R`.

This also answers **"the c_k Habiro w/ recursion rules"**: yes, `kehn`'s Q_β `c_k`
Habiro element is the recursion-rule object — but it is a *different localization*,
and fitting its Φ₂ is the explicitly-forbidden "seventh ansatz". It cannot be
borrowed to close the binding weight by fitting.

## Part 3 — can `wₙ(K)` close now? Derive-or-refute (no fit)

AME2020 anchors D/T/³He/⁴He, `a_D^(n)=S(n)/n`, `mₑ=0.51099895` MeV.

> **CORRECTION (2026-07-11, after coordination with [#3534](https://github.com/litlfred/qou/pull/3534)).**
> An earlier version of this section declared K-independent (body-order) weights
> **structurally excluded (b)** from the *raw* AME split `B(T)=8.48 ≠ B(³He)=7.72`
> (9.9 %). **That was an over-claim** (the exact refuted-discipline trap): the raw
> split is almost entirely **Coulomb**, a separable known effect. #3534
> Coulomb-corrects to the strong binding `B_strong` and finds ³H/³He agree to
> **2.73 %** (charge-symmetry breaking); an independent estimate here
> (`E_C(³He) = ⅗·Z(Z−1)·e²/(4πε₀R) ≈ 0.8–1.0 MeV`) restores the mirror pair to
> within ~1–3 %. **So a K-independent body-order `wₙ` IS admissible.** The (b)
> claim is **re-scoped to (a)** below; the raw numbers stand, only the scope was
> wrong.

**(a) Ad-hoc constant-ratio kernels do not close (scope-a).** On the
Coulomb-corrected `B_strong`, body-order weights `w₂,w₃,w₄` are admissible and
extractable (#3534: `4.353, 9.331, 15.919`, ratios 2.143/1.706, no fit). But no
parameter-free *constant-ratio* kernel `R(q,n)` reproduces them to 5 %: geometric
22.7 %, `[n]_q` 29.4 %, `a_D` self-ratio 37.6 %, `∝n` 30.0 %, `[n]_q²` 6.9 %
(lone near-miss) — #3534 Part (i). A tuned recursion is the banned 7th Δ_λ ansatz.

**Underdetermination of a general K-dependent kernel.** With `wₙ(K)` fully
K-dependent, each isotope contributes `A−1` unknowns (`w₂..w_A`) against **1**
equation `B(K)`. Inverting the anchors for a per-isotope `wₙ` is a **fit** — the
forbidden move (Δ_λ gate, "no seventh fit-based ansatz"). Body-order admissibility
(above) is the *constrained* case (`wₙ` shared across K); even there the closed
form is open.

**Verdict.** `wₙ(K)` does **not** close now. Body-order weights are admissible on
`B_strong`, but no derived constant-ratio kernel reaches 5 % and a tuned one is
banned; closure needs a *derived* `R(q,x)` (the open q-difference kernel /
owner-gated s5-so3 keystone), so any `wₙ` from the anchors is a fit and cannot
honestly improve binding. The **non-fit** routes are (i) expansion in the
**q-Hermite basis** the eigenfunction relation identifies (#3534 Part ii — but see
the fork caveat in Part 1: `S(n)` is not the clean RS moment, so this is the
Habiro-dressed basis, not clean q-Hermite) and (ii) Option-1 of the
[2026-07-03 audit](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md):
`wₙ(K) =` hyperbolic link-volume of the n-body sub-cluster (a topological
invariant) — both untested, both non-fit.

## Part 4 — Frobenius-dual + na-Stokes as `R(q,x)`: refuted (scope-a), with a reason

Owner steer: "the one path that could wire binding is a derived `R(q,x)` — use
Frobenius dual, na-Stokes." The na-Stokes residues are the per-block quantum
dimensions `dim_q(λ)`; the Frobenius pairing is `tr_M(β)=Σ_λ y_λ χ_λ(β)`, `y_λ`
the Jones–Markov weights. Tested (no fit) against the `B_strong` weights
`w=4.353,9.331,15.919` (ratios **2.144, 1.706**, decelerating). Compute:
[`binding_wn_frobenius_dual_probe.py`](../../computations/binding_wn_frobenius_dual_probe.py),
witness `binding-wn-frobenius-dual-refute.witness.json`.

| construction | ratio 3/2 | ratio 4/3 | |
|---|--:|--:|---|
| `a_D` (na-Stokes mean) | 1.337 | 1.894 | accelerating |
| `Σ dim_q²` (self-pairing) | 3.022 | 4.088 | accelerating (~`n!`) |
| `Σ y_λ dim_q = tr_M(𝟙)` | 1.003 | 1.009 | ≡ 1 (Markov normalization) |
| `Σ y_λ dim_q²` (Frobenius self-dual) | 1.574 | 1.573 | constant ratio |
| `Σ y_λ` (total weight) | 0.719 | 0.706 | decreasing < 1 |

**Refuted (scope-a), structural reason.** The canonical `y_λ` are *exactly* the
weights that normalize `tr_M` into a trace, so `Σ y_λ dim_q = tr_M(𝟙) ≡ 1`
identically and self-pairings give **constant** ratios. The Frobenius dual
collapses the block structure into a normalized trace and **cannot** supply the
extensive, *decelerating* weight the anchors need. The na-Stokes residues are the
kernel `a_D`; their Frobenius dual is `tr_M`-normalization, not the weight.
⇒ the weight must be **geometric** (hyperbolic link-volume; volumes grow
sub-exponentially — the decelerating direction), not algebraic-dual. This is the
forward (formalize-first) prune of the steered class; it does not exclude a
geometric `R(q,x)`.

## Part 5 — multi-anchor: the full na-Stokes jet tower summed to A is refuted (scope-a)

Testing the weight *shape* against more anchors (D→¹²C, Coulomb-corrected
`B_strong`; single global scale fit to ⁴He). The low-`n` weights are **quadratic**:
`wₙ/n² = 1.088, 1.037, 0.995` and `wₙ/[n]_q² = 1.077, 1.007, 0.943` (both ~±8 %,
decelerating) — so a *linear* hyperbolic link-volume (ratios ∝n = 1.5, 1.33)
**undershoots** the extracted ratios (2.14, 1.71); the shape is quadratic
(Casimir-class), not linear-volume.

But extrapolated to A≥5 the full-tower form
`B = Σ_{n=2}^{A} mₑ·a_D^(n)·wₙ` **overshoots catastrophically** for *every*
amplifying/quadratic weight
([`binding_wn_multianchor_tower_refute.py`](../../computations/binding_wn_multianchor_tower_refute.py),
witness `binding-wn-multianchor-tower-refute.witness.json`):

| iso | A | `B_strong` | `B_pred` (wₙ=n²) | err |
|---|--:|--:|--:|--:|
| ⁴He | 4 | 29.20 | 29.20 | 0 % (scale anchor) |
| ⁶Li | 6 | 34.37 | 350.65 | **+920 %** |
| ⁷Li | 7 | 41.50 | 1296 | +3023 % |
| ⁹Be | 9 | 62.32 | 21389 | +34222 % |
| ¹²C | 12 | 101.6 | 2.3×10⁶ | +2.3×10⁶ % |

**Refuted (scope-a), precision-independent structural reason.** `a_D^(n)` grows
**super-exponentially** (involution-number growth: `a_D^(12)≈2.5×10⁴`) while
nuclear `B/A → const` (extensive). A bounded-or-amplifying body-order weight
summed to `A` therefore *cannot* be linear in `A`. The light-nucleus amplification
(`wₙ~n²`, needed to lift the 2026-07-03 undershoot 4.87×→12.72×) and the
heavy-nucleus saturation are **incompatible** for one body-order weight × the
super-exp period summed to `A`.

**Redirect.** The binding is **not** the full na-Stokes jet tower summed to the
nucleon count. It must be a **few-body truncation** (fixed small `n_max`, ~2–3
body clusters × an A-multiplicity — matching real nuclear 2-/3-body force
dominance), or a weight decaying faster than `1/a_D^(n)` (i.e. *cancelling* the
period, not "informed by" it). The na-Stokes period remains the correct **light**-
nucleus (A≤4) kernel; it is the wrong object to sum to `A`.

## Part 6 — synthesis: the missing piece is the geometric bond-count, not a weight kernel

Few-body truncation (`n_max=3`, cluster counts `M_n(K)`) tames the Part-5 overshoot
from `~2×10⁶ %` to `~50 %` (chain model, worst-case), confirming the redirect.
The **residual** is a pure **normalization** — the bond-count `M_n(K)`. Anchoring
the per-bond energy on the deuteron (one inter-nucleon bond `= B_strong(D) =
2.22` MeV `= m_e·a_D^(2)·w₂·1`), the *implied* bond count each nucleus needs is:

| iso | A | #bonds needed | #bonds/A (coordination) |
|---|--:|--:|--:|
| D | 2 | 1.00 | 0.50 |
| T / ³He | 3 | ~3.9 | ~1.3 |
| ⁴He | 4 | 13.1 | 3.28 (magic α; needs the n=3 term) |
| ⁶Li | 6 | 15.5 | 2.58 |
| ⁷Li | 7 | 18.7 | 2.67 |
| ⁹Be | 9 | 28.0 | 3.11 |
| ¹²C | 12 | 45.7 | 3.81 |

`#bonds/A` rises from 0.5 (deuteron) and **plateaus at ~2.6–3.8** for A≥6 — the
nuclear **coordination number / saturation curve**. The chain model undershoots
precisely because `M₂=A−1` undercounts bonds in a compact 3-D packing.

**Synthesis (the culmination of Parts 1–5).** Every refutation funnels to one
conclusion: the na-Stokes period `a_D^(n)` supplies the **per-cluster energy**
(deuteron-anchored, `= 2.22` MeV per bond), and the **knot topology** supplies
the **cluster count** `M_n(K)` (the crossing / coordination structure of `𝓑_K`).
The missing piece is **geometric** (a bond-count = the hyperbolic-link / crossing
structure the 2026-07-03 audit Option 1 named), **not** an algebraic weight kernel
`R(q,x)`. The "eigenfunction relation informs the weight kernel" program resolves
as: there is no algebraic weight kernel to derive — the weight is the topological
bond-count of the canonical knot, and the binding is
`B(K) ≈ Σ_{n=2}^{3} m_e·a_D^(n)·M_n(K)` with `M_n(K)` the n-body cluster count of
`𝓑_K` (⁴He the magic-shell outlier). This is the well-posed, tractable next target.

## Part 7 — deriving `M_n(K)`: Reeb-flow → project → Milnor invariants (validated)

The Part-6 synthesis localized the gap to the geometric bond-count `M_n(K)`. The
derivation route ("Reeb flow and project"): the na-Stokes surface integral
`Hol(∂S_c)=∮F`, projected via the Reeb flow to the open-book (Milnor) fiber, has
`n`-fold linking equal to **Milnor's invariant `μ̄(1…n)`**. So the bond-count tower
is the tower of Milnor invariants of the canonical link `𝓑_K`:

- `M_2(K) = ` pairwise linking numbers `lk_ij` (Reeb self-linking / writhe),
- `M_3(K) = ` triple linking `μ̄_ijk` (irreducible 3-body),
- `M_n(K) = ` order-`n` Milnor invariant.

`μ̄` is computed by the standard **Magnus expansion** of the longitudes in the free
group (`μ̄(i_1…i_k) = ` coeff of `X_{i_1}…X_{i_{k-1}}` in the Magnus image of `ℓ_{i_k}`).
Compute + validation:
[`binding_mn_milnor_linking.py`](../../computations/binding_mn_milnor_linking.py),
witness `binding-mn-milnor-linking.witness.json`:

| link | pairwise `lk` (M₂) | `μ̄_123` (M₃) | reading |
|---|--:|--:|---|
| Hopf (one bond) | **1** | — | M₂ unit ✓ |
| Borromean | 0, 0, 0 | **+1** (`μ̄_213=−1`) | irreducible 3-body ✓ |
| 3-chain (Hopf ×2) | 1, 1, 0 | **0** | reducible → pairwise ✓ |

**Milnor cleanly separates the genuine 3-body (Borromean, `μ̄=1`) from a chain of
pairwise bonds (`μ̄=0`)** — exactly the "not reducible to pairwise sums" the
conjecture's `n=3` term requires, and the framework's 3-body knot *is* the
Borromean `𝓑₃`. The bond-count derivation is therefore realized as a working,
validated invariant — not a guess.

**Remaining input (honest).** The per-isotope canonical link `𝓑_K` (which link
represents ⁶Li, ¹²C, …) is the framework **model input** that fixes which link `μ̄`
is evaluated on; `μ̄` gives `M_n` once `𝓑_K` is chosen. `μ̄` of order `n` is
well-defined modulo lower-order invariants — clean integers exactly when the lower
linkings vanish (the Borromean/irreducible case), which is why the `n=3` term is
the tractable one. `M_2` (pairwise `lk`) is already live in the corpus
(`em_linking_invariant_probe.py`, `ch_bond_writhe_lp.py`, Hopf `σ₁²`).

## Consequence for `conj:binding-manybody-eq-jet-filtration`

**Not provable now** (recorded answer). The conjecture's three deep inputs remain
open: (1) the super-exponential `a_D^(n)` magnitude, (2) the na-Stokes identity
`a_D^(n)=lw(n−1)` (owner-gated keystone #1765), and (3) the weight `wₙ(K)`. This
work sharpens (3): body-order weights are *admissible* on the Coulomb-corrected
`B_strong` (#3534), but no derived constant-ratio kernel reaches 5 % and a tuned
one is a banned ansatz — closure needs the derived `R(q,x)`.
`prop:jet-filtration-binding-extensive` (the *qualitative* extensivity) stays the
proved core; the *quantitative* closure is unchanged (open).

## Reproduce

```bash
python3 computations/binding_wn_derive_or_refute.py
```

EXPLORATORY — no production wiring, no fitted constant. Anti-laundering: the Lean
file certifies the two-tier *algebra*; it does not improve any mass/binding number.
