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

## Part 8 — which link is ⁶Li / ¹²C? production says "chain"; and that is the ad-hoc gap

The production canonical braid `mass_at_3A_proper.atom_braid_word_3A` answers
"which link" directly — and it is a **linear chain**. It places one inter-nucleon
generator at gen `3k+2` for `k < A−1` (source), i.e. exactly `A−1` bonds between
consecutive nucleons (verified by run):

| iso | A | production bonds (M₂) | A−1 | M₃ = μ̄₁₂₃ |
|---|--:|--:|--:|--:|
| ⁴He | 4 | 3 | 3 | 0 |
| ⁶Li | 6 | 5 | 5 | 0 |
| ⁷Li | 7 | 6 | 6 | 0 |
| ¹²C | 12 | 11 | 11 | 0 |

Milnor reading (Part 7): a linear chain has `M₂(K)=A−1` (the chain bonds) and
`M₃(K)=μ̄₁₂₃=0` (a chain is reducible to pairwise — no irreducible 3-body). So the
production link *is* the Part-6 chain model, which undershoots (~20–36 %): the
chain undercounts the compact-nucleus coordination (`#bonds/A ≈ 3` vs chain `≈ 1`)
and carries no 3-body term (⁴He's magic binding needs exactly `μ̄₁₂₃≠0`). This is
the already-flagged **open 9b gap** (`binding_canonical.py`: `10A−5 = 5(2A−1)` =
"A nucleons + A−1 bonds", categorical derivation OPEN).

**Critique (owner): `if include_inter and k < A−1` "should not be case by case."**
Correct — the linear chain is an **ad-hoc placeholder**, not a derivation: it
hard-codes a consecutive-neighbour bond rather than letting the bond graph emerge.
The principled derivation is the **confinement / operator-selection SDP**: its dual
active set (`y_star[i] > 0`, the "most receptive sub-braids" of the AGENTS.md
LP/SDP-dual contract) identifies *which* nucleon-pairs actually bond, giving the
compact coordination and the jointly-active triples (the `μ̄₁₂₃` Borromean 3-body
terms) with no hand-coded chain. This is the **right role for the Frobenius/SDP
dual** — it fixes the *link topology* (bond graph), **not** the weight magnitude
(which the Part-4 probe correctly refuted it for). Replacing `k < A−1` with the
SDP-active-set bond graph is the concrete 9b-closure target: compute
`M_n(K) = μ̄`-tower of the SDP-derived link, evaluate `B(K)` against AME.
Compute: [`binding_production_link_milnor.py`](../../computations/binding_production_link_milnor.py).

## Part 9 — can the SDP derive the bond graph? No — it is degenerate

The Part-8 critique said the linear chain should be replaced by an SDP-derived bond
graph (the dual active set = "most receptive sub-braids"). Tested — and it is
**degenerate**, live-confirmed
([`binding_sdp_bondgraph_degenerate.py`](../../computations/binding_sdp_bondgraph_degenerate.py),
witness `binding-sdp-bondgraph-degenerate.witness.json`). The canonical H₃
operator-selection LP-dual (NF basis `{γ,σ₀,σ₁,L₊,L₋,e⁻}`, Frobenius Gram, costs
`t_i=tr_M(b_i)`) returns, at *every* demand:

| n_target | `y0*` | active_set | |
|---|--:|---|---|
| \|tr_M(proton)\|≈0.66 | 0 | {γ} | degenerate |
| identity 1.0 | 0 | {γ} | degenerate |
| Σ t_i | 0 | {γ} | degenerate |

Structural reason (corpus-established — `he3_pairknot_composite_lp_probe.py`, audit
2026-06-18): **a free / single nucleon has `W_free = W_atom`**, so there is no
binding constraint to select against; the active set collapses to the identity, and
the pair (H₆) LP is intractable / also degenerate. So a direct operator-selection
LP-dual does **not** isolate a bond graph at any tractable level.

**Net — both routes fail.** The ad-hoc chain (`k<A−1`, Part 8) undercounts
coordination; the SDP-active-set (this part) is degenerate. Therefore the bond
graph `M_n(K)` — *which* pairs bond, the coordination/topology — is a genuine **open
geometric input**, not derivable from either the chain hack or an LP. It needs a
categorical / geometric coordination construction (the owner-gated s5-so3 keystone
territory). What *is* derivable: the per-bond-**type** strength
`L_pp/L_pn/L_nn = log(tr_M^full/tr_M^atom)` (bond traces, corpus-live) and the
Milnor `M_n` of a **given** graph (Part 7) — not the graph itself. That is the
honest, sharp boundary of the binding-derivation program as it stands.

## Part 10 — the SDP degeneracy is not a dead end: binding is a QUADRATIC Gram form (coordination = cross-terms)

A parallel finding landed on `main` (commit `a44296db`,
`qbeta_c3_barodd_binding_sdp_dual_probe.py`, audit
`2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`) that **independently reproduces
Part 9's LP degeneracy** and explains it — sharpening the coordination route.
Reproduced here ([`binding_ghost_gram_quadratic.py`](../../computations/binding_ghost_gram_quadratic.py),
witness `binding-ghost-gram-quadratic.witness.json`):

The binding / ghost mode `g = ½(L₊−L₋)` (H₃ NF basis) satisfies

- `tr_M(g) = 0` — **traceless**, hence invisible to any linear trace-target LP (⇒ the
  Part-9 degeneracy is structural, not incidental);
- `⟨g⟩²_G = g·G·g = −0.4275 < 0` — **negative Gram norm**;
- `⟨g, mass⟩_G = 0` — binding ⊥ mass (the Gram-signature split).

So **mass is the linear `tr_M` (rest energy); binding is the QUADRATIC Gram/SDP
form** (the mass defect, second order). The LP being blind to binding is *correct* —
binding does not live in the linear/trace layer.

**Coordination-graph consequence (the qou-v0yw keystone, re-sharpened).** The bond
graph `M_n(K)` is neither the ad-hoc chain (Part 8) nor an LP active set (Part 9,
degenerate) — it is the **cross-term structure of the multi-nucleon binding
quadratic form**:

    B(K) ~ ⟨Σ_i g_i⟩²_G = Σ_i ⟨g_i⟩²_G + 2·Σ_{i<j} ⟨g_i, g_j⟩_G

with `g_i` nucleon `i`'s ghost mode. The **pairwise cross-terms `⟨g_i, g_j⟩_G` are
the bonds (M₂)**; jointly-nonzero triples are the irreducible 3-body (M₃, the Milnor
`μ̄₁₂₃` of Part 7). Computing them is a **Gram evaluation on the multi-nucleon
(H₆⁺) basis — not the degenerate LP**, and not a fit. This converts the "open
geometric input" of Part 9 into a concrete, tractable compute target: the deuteron
(H₆) ghost cross-term is the first bond; the coordination is the graph of
significant `⟨g_i, g_j⟩_G`.

## Part 11 — deriving the bond-extensive hypothesis from bond translation-invariance

Siblings #3549/#3551 (`bk_coordination_contact_binding.py`) read the binding
multiplicity as the coordination number `z(A)=A−1` (nucleon) / contact-graph edges
(α-cluster), but flag *"single-link multiplier = coordination number"* as the
**bond-extensive hypothesis — conditional, not derived**. The Part-10 Gram-quadratic
binding form supplies the missing derivation
([`binding_bond_extensive_derivation.py`](../../computations/binding_bond_extensive_derivation.py),
witness `binding-bond-extensive-derivation.witness.json`):

`B(K) ~ ⟨Σ_i g_i⟩²_G = Σ_i ⟨g_i⟩²_G + 2·Σ_{i<j} ⟨g_i, g_j⟩_G`, `g_i = ½(L₊−L₋)_i`.

1. **Unbonded cross-term vanishes.** Two nucleon ghosts on disjoint strands form a
   *split link*; the Markov trace factorizes, `tr_M(g_i⊗g_j)=tr_M(g_i)·tr_M(g_j)`,
   and each ghost is **traceless** (`tr_M(g)=0`). So `⟨g_i,g_j⟩_G = 0` with no bond.
2. **Bonded cross-term is bond-universal.** A single inter-nucleon generator couples
   the pair: `⟨g_i,σ_bond,g_j⟩_G = b* ≠ 0`. For identical nucleons joined by
   identical bonds, every bond is the *same* local ghost-σ-ghost coupling
   (translation-invariant), so every bond contributes the **same** `b*`.

⇒ `B(K) ~ Σ_i⟨g_i⟩²_G + (#bonds)·b* = self + coordination·b*`. **The bond-extensive
form is derived** — the multiplier is constant *because the bonds are structurally
identical couplings*, not by assumption. This upgrades the siblings' conditional
hypothesis to a structural result.

**Boundary (honest).** What remains is the *value* `b*` (one universal per-bond
number) = the H₆ seminormal-Gram build (`markov_trace_combo` is H₃-only;
`gram_matrix_seminormal_h6.py` is the per-block route), overlapping #3548's W_λ
connected transfer matrix (the `tr_M` lens of the same object) — coordinate before
solo. The homogeneity (identical-bond) assumption is the mean-field reading; a
compact non-chain geometry with inequivalent bonds would split `b*` by environment.

## Part 12 — the `b*` bridge: connected `tr_M` == centered Gram-quadratic (exact)

The per-bond `b*` was deferred to an H₆ build (Part 11). It does **not** need a
separate build — #3548's *connected* `tr_M` part and this session's *centered/ghost
Gram-quadratic* norm are the **same object**, proved by an exact identity
([`binding_bstar_bridge.py`](../../computations/binding_bstar_bridge.py),
witness `binding-bstar-bridge.witness.json`). Using the Markov normalization
`tr_M(1)=1`, for any mode `w`:

    C(w)  = tr_M(w²) − tr_M(w)²                      (#3548 connected part)
    ⟨δw⟩²_G = tr_M((w − ⟨w⟩·1)²)
            = tr_M(w²) − 2⟨w⟩tr_M(w) + ⟨w⟩²·tr_M(1)
            = tr_M(w²) − tr_M(w)²  =  C(w).           (#3545 centered Gram norm)

The **connected part IS the Gram-quadratic norm of the centered (traceless) mode** —
the "ghost" `δw = w − ⟨w⟩` is exactly the fluctuation whose connected 2-point #3548
computes. Verified bit-identical on the H₂ `(2,k)` torus bond (#3548's Check 3):
`tr_M(σ)=0.499320`, `tr_M(σ²)=1.104388`, both give `0.8550672621` (`|Δ|=0`).

**Consequences.**
- **`b*` is pinned by whichever lens computes the connected part** — #3548's
  deuteron connected `0.193` **is** this session's per-bond `b* = ⟨g_A,σ_bond,g_B⟩_G`.
  The H₆ seminormal build is #3548's PROBE 2, not a separate #3545 task.
- **Unifies three findings as one object:** main `a44296db` (decay=binding-quadratic),
  #3548 (connected transfer matrix), #3545 (negative-norm ghost Gram-quadratic) —
  binding = quadratic = connected = centered Gram norm.
- **Sign is mode-dependent** (centered modes have indefinite Markov-Gram norm): the
  `σ` mode gives `+0.855`, the bar-odd `L₊−L₋` ghost gives `−0.4275` (binding).

## Part 13 — the edge set: variationally selected (binding-max ⇒ max-contact packing)

The last open piece is the *edge set* — which nucleon pairs bond. It is **not
free**: with `b*` a fixed per-bond constant (Parts 11–12), the physical ground
state **maximizes** binding `B ~ Σ_bonds b*`, hence maximizes the **number of
bonds** subject to 3-D hard-core realizability (unit spheres cannot overlap). ⇒ the
edge set is the **maximum-contact sphere packing** — a pure geometry problem, no fit
([`binding_edge_set_selection.py`](../../computations/binding_edge_set_selection.py),
witness `binding-edge-set-selection.witness.json`).

This **resolves the #2089 open dichotomy** ("chain under-binds, complete
over-binds"): the answer is **neither** — the max-contact graph lies between the
chain (`A−1` edges) and the complete graph (`C(A,2)` edges). For `A≤4` all spheres
mutually touch (simplex) so max-contact `= C(A,2)`; for `A≥5` not all can touch, so
max-contact `< C(A,2)` — exactly the saturation the linear-in-`A` binding requires.

| iso | A | #bonds implied | chain `A−1` | simplex `C(A,2)` |
|---|--:|--:|--:|--:|
| D | 2 | 1.00 | 1 | 1 |
| T/³He | 3 | ~3.8 | 2 | 3 |
| ⁴He | 4 | ~13.1 | 3 | 6 |

The **pairwise** edge set is ≈ the max-contact (simplex) graph; the ⁴He magic
surplus (`~13` vs simplex `6`) is the irreducible **3-body Milnor term `M₃`**
(Part 7), *not* additional pairwise bonds. So max-contact fixes the pairwise edges;
the `μ̄₁₂₃` 3-body term rides on top.

**Boundary (honest).** Max-contact packings for `A≥5` are specific sphere-packing
contact numbers (triangular bipyramid 9, octahedron 12, …) — a known but
case-by-case geometry; and **cluster/halo** nuclei (⁶Li = α+d, ⁹Be) sit *below*
max-contact (loosely bound) — a genuine nuclear-structure deviation the principle
alone does not fix. The principle narrows the edge set to "max-contact modulo
cluster structure"; the residual cluster geometry is the owner-gated s5-so3 input,
and the α-cluster contact-graph level is #3551's scope (Brink deltahedra — the
α-level instance of this same max-contact principle).

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
