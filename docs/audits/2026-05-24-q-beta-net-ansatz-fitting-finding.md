# Q_β `net`-ansatz fitting finding (2026-05-24)

**Branch**: `claude/gifted-feynman-U7ckD`  ·  **PR**: [#1127](https://github.com/litlfred/qou/pull/1127)  ·  **Triggered by**: owner directive "I think only 2 CAL is numerical coincidence... no fitting PLEASE"  ·  **Status**: open finding, requires follow-up Path A / Path B (see below)

## Finding (one sentence)

The framework's free-neutron Q-value closed form
$Q_\beta = m_e \cdot |q_0^2 - 2 q_0 - 1| \cdot (q_0+1)/(2 q_0^3) \approx 0.7836$ MeV
**presented as a 2-input prediction** rests on a relation
$Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$
that is **postulated "by construction"**, not derived from the
canonical per-braid mass formula, leaving open whether the +0.17%
match to CODATA is genuine truncation residual or numerical
coincidence (fitting).

## Step-by-step derivation chain audit

| Step | Status | Source / evidence |
|---|---|---|
| **1.** Proton braid word = [u, u, d] in $B_3$ | ✓ **Derived** | Standard Model quark content (forced) |
| **2.** Neutron braid word = [u, d, d] in $B_3$ | ✓ **Derived** | Standard Model quark content (forced) |
| **3.** Typed-crossing operators: $C(\mathfrak{u},\mathfrak{u};\sigma_k) = \sigma_k$, $C(\mathfrak{d},\mathfrak{d};\sigma_k) = \sigma_k - h$, $C(\mathfrak{u},\mathfrak{d};\sigma_k) = \sigma_k - h/2$ | ✓ **Derived** | [`def:typed-crossing-operator`](../../content/quantum-observable-universe/braids-and-knots/typed-crossing-operator.md): up-up = positive orientation, down-down = inverse via Hecke relation, mixed = symmetric midpoint forced by $\mathfrak{u} \leftrightarrow \mathfrak{d}$ swap symmetry |
| **4.** Single-wrap convention: proton ≡ $\sigma_0 \cdot (\sigma_1 - h/2)$, neutron ≡ $(\sigma_0 - h/2)(\sigma_1 - h)$ | ✓ **Derived** as N=0 brane-tower truncation | Minimal braid (one crossing per generator); higher orders = higher tower levels |
| **5.** NF reduction in H_3(q): exact algebra | ✓ **Derived** | Hecke relation $\sigma_i^2 = h \sigma_i + 1$; proton → $L_+ - (h/2)\sigma_0$; neutron → $L_+ - h\sigma_0 - (h/2)\sigma_1 + (h^2/2)\gamma$ |
| **6.** $\Delta(\mathrm{net}) = \mathrm{net}(n) - \mathrm{net}(p) = h(h-2)/2$ where $\mathrm{net} = \sum_i c_i$ over the 6 NF basis elements | ⚠️ **Computation derived; identification of `net` with mass-formula NOT derived** | [`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md) and [`beta-decay-energy-scale.md`](../../content/quantum-observable-universe/archimedean-universe/beta-decay-energy-scale.md) compute the unweighted sum, but DO NOT prove this sum equals the leading-order contribution to $\mathfrak{m}(W)$ |
| **7.** Energy scale $\mathfrak{E}_0 = m_e/(q(q-1))$ (single-tick / N=0 truncation) | ✓ **Derived** | [`energy-scale-planck.md`](../../content/quantum-observable-universe/braids-and-knots/energy-scale-planck.md): Planck-tick energy quantum from cohomological mass formula |
| **8.** $Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$ | ⚠️ **POSTULATED, NOT DERIVED** | [`pre-archimedean-derivation-chain.md`](../../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) line 391: "**so $Q_\beta = \|\Delta(\mathrm{net})\| \times \mathfrak{E}_0$ by construction**". This is the gap. |
| **9.** Closed form $Q_\beta = m_e \cdot \|q^2 - 2q - 1\| \cdot (q+1)/(2q^3)$ | ✓ **Algebraic consequence of (6, 7, 8)** | Pure substitution; valid IF the ansatz (8) is valid |
| **10.** Numerical: 0.7836 MeV vs CODATA 0.7823 MeV (+0.17%) | ✓ **Empirically verified** | Match holds at the substrate $q_0 \approx 1.10998$ |

## Why this matters

The framework's canonical mass formula is the **per-braid mass tower**
[`prop:per-braid-mass-tower`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md):

$$\mathfrak{m}(W) = |\mathrm{tr}_M(W)| + \sum_n \left[\sum_{\xi \in \mathcal{S}^{(n)}_1} \Phi_q(|\mathrm{tr}_M(\xi)|) + z^2 \sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2} \Phi_q(|\mathrm{tr}_M(\xi\xi')|)\right] + R_N$$

This uses the **Markov-trace-weighted** sum: $\mathrm{tr}_M(\gamma) = z$,
$\mathrm{tr}_M(\sigma_i) = z^2$, $\mathrm{tr}_M(L_+) = z^3$, etc.
Different NF basis elements contribute with different weights.

The "net" in the Q_β derivation is the **unweighted** sum $\mathrm{net}(W) = \sum_i c_i$
where $W = \sum_i c_i e_i$ in the NF basis $\{e_i\}$. **This is a different quantity**.

The relation $Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$
**asserts that the unweighted NF sum gives the leading-order
mass difference at first order in $h$** — but this is asserted
"by construction", not proved as an expansion of the per-braid
mass tower.

## Two possibilities for the +0.17% residual

| Possibility | Implication |
|---|---|
| **(a) Genuine truncation residual** | The unweighted `net` formula is the correct leading order; the +0.17% gap is the $O(h^2)$ tower correction, closeable by tower-summation. Q_β IS derivable from CAL-1 + CAL-2 at 1ppb after tower closure. |
| **(b) Numerical coincidence (fitting)** | The unweighted `net` formula happens to match Q_β to 0.17% at the specific substrate $q_0 \approx 1.110$, but is not the correct leading order. No amount of "tower closure" will close the gap because the wrong leading-order operator was identified. Q_β is NOT derivable from CAL-1 + CAL-2; it remains genuinely independent. |

The framework currently assumes (a) implicitly. The +0.17% match is taken as evidence FOR the ansatz. **But there is no independent derivation.**

## Three paths to resolve

| Path | What | Cost | Verifies |
|---|---|---|---|
| **A. Theoretical derivation** | Expand the per-braid mass tower $\mathfrak{m}(W) = \|\mathrm{tr}_M(W)\| + \sum \Phi_q + \dots$ at leading order in $h$. Show $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e = \|\Delta(\mathrm{net})\| \cdot \mathfrak{E}_0 + O(h^3)$. | 1-2 days analytical work | If derivation succeeds: (a). If fails or finds discrepancy: (b). |
| **B. Direct compute** | Compute $\mathfrak{m}(p)$ and $\mathfrak{m}(n)$ DIRECTLY via the per-braid mass tower (Markov-trace-weighted + Φ_q). Compare $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$ to CODATA. | 1-2 hours implementation + run | Whether canonical mass formula even produces correct $Q_\beta$ without the ansatz. |
| **C. Cleanup** | Update all paper content blocks claiming Q_β derivation to honestly label the relation $Q_\beta = \|\Delta(\mathrm{net})\| \cdot \mathfrak{E}_0$ as an **ansatz** pending A or B. | ~1 hour mechanical edits | Honesty in present claims. |
| **D. Hermiticity audit** *(added 2026-05-24 after PR follow-up)* | For each categorical observable ($m_\mu/m_e$, $m_e$, $Q_\beta$, $m_p$, $m_n$, …), classify whether it is structurally `tr_M(Hermitian op)` (forces real by QM), or `\|tr_M(op)\|` (modulus projection), or `Re tr_M(op)` (real-part projection), or unspecified. The "unspecified" rows are exactly where the framework's real-q assumption is unjustified and where Im(q_0) effects could be hiding. Sibling finding to the net-ansatz: addresses **why** the framework defaults to real q (because it never specified the projection rule). | 1 day documentation + analysis | Whether the framework has structurally forced its observables to be real, vs. silently assumed it. Disambiguates between Q3 options (i)-(v) listed below. |

**This finding selects all four paths.** B + C + D are in scope for the current PR; A is queued for a follow-up branch.

## Action items (this branch)

- [x] Revert duplicative `prop:q-beta-substrate-prediction` block (commit `6c317e19`)
- [ ] Cleanup `neutron-qvalue-symbolic.md` — add ansatz banner via `authorNotes`
- [ ] Cleanup `beta-decay-energy-scale.md` — flag `Q_β = |Δ(net)|·E_0` as ansatz
- [ ] Cleanup `pre-archimedean-derivation-chain.md` — clarify "by construction" = ansatz
- [ ] Cleanup `calibration-inputs.md` §"CAL-3 gap" — honestly state dual status
- [ ] Update PR description to surface this finding prominently

## Follow-up branches queued

- `claude/q-beta-direct-per-braid-compute-<utc-ymd>` — Path B: per_braid_q_beta_direct.py
- `claude/q-beta-net-ansatz-leading-order-<utc-ymd>` — Path A: theoretical derivation
- `claude/q-beta-im-q0-coupling-<utc-ymd>` — sequels: connect +0.17% to complex-q exploration, Φ_q under bar/star/skew

## Cross-references

- Authoritative ansatz statement (the gap): [`pre-archimedean-derivation-chain.md:391`](../../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md#L391)
- Canonical mass formula (the right formalism): [`per-braid-mass-tower.md`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md)
- The current "prediction" block (will be updated): [`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md)
- Owner directive flagging this: PR #1127 chat (2026-05-24): *"I think only 2 CAL is numerical coincidence, but I don't know what you are doing exactly. please justify every step. no fitting PLEASE"*
- **Companion**: [`2026-05-24-complex-q-historical-trajectory.md`](2026-05-24-complex-q-historical-trajectory.md) — historical emergence of ℂ in physics (Cardano → Schrödinger → Born → Renou) and the parallel trajectory for `q ∈ ℂ` in QOU; identifies the framework as currently at stage 3 of the trajectory (Born modulus projection) with +0.17% Q_β as the candidate for stage 4 (forced by formula). Empirical test (simultaneous CAL-2 + CAL-3 fit for complex q_0) ~2 hours of work; queued as Path B-extended.

## Path D execution — Hermiticity audit of the categorical mass formula

> **🔄 Reconciliation update (2026-05-24, via PR #1127 coordinate sweep).**
> The structural answer to "what forces real q" is **already in the
> framework** as the `P_avg` / `P_skew` projection in
> [`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md). The framework canonically projects to the
> **bar-symmetric** part (P_avg → `cos, cosh, Li_2^q`) and discards
> the bar-anti-symmetric part (P_skew → `sin, sinh, Φ_q` alone).
> Sibling **PR [#1153](https://github.com/litlfred/qou/pull/1153)** (sinh-bar-antisymmetric-partner-probe) makes the P_skew
> channel EXPLICIT for torus knots: `Q_m / P_m = tanh((2m+1) η_0)`.
>
> What this means for this audit: the "real q" convention is forced
> by the P_avg projection rule (P_avg of real-q observables is real;
> Im(`tr_M`) is in P_skew, discarded). The modulus projection
> finding below is still correct but **subordinate** to the P_avg /
> P_skew framework. The likely closure path for the +0.17% Q_β
> residual is now sharper:
> - Per-braid mass tower uses **Φ_q** which is in **P_skew** (discarded).
> - Canonical P_avg tower function is **Li_2^q** per `bar-involution.md`.
> - Replacing Φ_q with Li_2^q (already conjectured in `calibration-inputs.md:72-84`)
>   gives the proper bar-symmetric tower; the +1.75% wrong-direction
>   tower correction is the signature of using the wrong projection.
> - This makes the closure conjecture **structurally motivated**,
>   not a hand-tuned ansatz — and the framework's "real q" choice IS
>   derivable from the P_avg projection rule.

**Headline (original, retained)**: the framework's mass formula is
**already modulus projection** (option iv). Complex `q` is structurally
admissible without modifying anything; the real-`q` convention is fixed
**by the P_avg projection** (per the reconciliation update above), not by
the modulus alone.

### Evidence

[`prop:categorical-mass-markov`](../../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md#L18-L21) states the categorical mass at single brane level:

$$\mathfrak{m}_{q, \mathcal{K}}\big|_{\text{single level}} = \Big|\!\int_A\! \rho(\beta_\mathcal{K})\Big| = |\mathrm{tr}_M(\rho(\beta_\mathcal{K}))|$$

The `|·|` is the modulus of the Markov trace. This is **option (iv)
modulus-projection** in the Q3 framework above. The full per-braid
mass formula [`prop:per-braid-mass-tower`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md) wraps `|tr_M|` in another `|·|`-stacked sum.

`|·|` is well-defined for any normed field — including `ℂ`. The
formula does NOT force `tr_M(ρ(β)) ∈ ℝ`; only the *measured* mass
(the modulus) is forced real.

### Per-observable classification

| Observable | Formula | Projection | Complex-`q` behaviour |
|---|---|---|---|
| `m(K)` (any particle mass) | `|tr_M(ρ(β_K))|` | **(iv) modulus** | real-valued for any `q ∈ ℂ`; Im(`tr_M`) projected away |
| `m_μ/m_e` (CAL-2 → q_0) | `|tr_M(μ)|/|tr_M(e)| = |Vol(4_1)/ℏ_q²|` | **(iv) modulus** | For `q = u + iv`: `Vol(4_1) · (u² + v²)/((u-1)² + v²)` — ONE real equation for TWO real unknowns |
| `m_e` (CAL-1) | absolute calibration | **fitted to CODATA** | sets the scale (real positive) |
| `Q_β = m_n − m_p − m_e` | difference of three moduli | **iv stacked** | real-valued for any complex `q`; depends nonlinearly on (u, v) |
| Q-values in general | mass differences via `|·|` | **iv stacked** | same |
| `α (fine structure)` | ? — needs separate audit | unspecified | open |
| Other Q-values, half-lives, etc. | derived | inherits (iv) | inherits |

### The 1-parameter family of admissible q_0

`m_μ/m_e ≈ 206.768` gives ONE real equation:

$$\mathrm{Vol}(4_1) \cdot \frac{u^2 + v^2}{(u-1)^2 + v^2} = 206.768$$

This is **one constraint on two real unknowns** (u, v). The
solution set is a curve in the q-plane. The framework's
default choice u = 1.10998, v = 0 (the real-axis intercept) is
**one point** on this curve, fixed by an unstated convention
"`v = 0` unless required otherwise".

**Without an independent measurement constraining `v`, the
framework has one extra free parameter it has silently set to
zero.**

### Implication for Q_β residual

Q_β is a function of `(u, v)` via the stacked modulus projection.
At `v = 0`, Q_β(u=1.10998, 0) ≈ 0.7836 MeV (+0.17% vs CODATA
0.7823 MeV). Solving simultaneously
- m_μ/m_e(u, v) = 206.768
- Q_β(u, v) = 0.7823

gives **two equations for two unknowns (u, v)** — generically a
discrete set of solutions including the real one but possibly
also complex ones with `v ≠ 0` that match CODATA exactly. This
**could resolve the +0.17% residual without invoking tower
closure at all**: it might be an Im(q_0) effect projected away
when we set `v = 0` by default.

This is no longer speculation — given the modulus projection is
the actual formula, the complex-q resolution is structurally
admissible and the open empirical question is "is there a
complex q_0 with Im ≠ 0 that hits both CAL-2 and CAL-3 exactly?"

### What forces real q (currently unstated)

Possibilities, in order of physical plausibility:

1. **Bar-involution invariance**: the mass operator might be
   self-conjugate under the Lusztig bar (`q ↦ q⁻¹`); for the bar
   to be an involution on the OBSERVABLE level, need `q̄ = q⁻¹`,
   i.e., `|q| = 1` — but this conflicts with `q ≈ 1.110`.
2. **Hermitian involution invariance**: `q ↦ q̄⁻¹`; gives `q = q̄⁻¹`
   iff `|q| = 1`. Same issue.
3. **Real Hecke representation**: if all entries of `ρ(σ_i)` are
   real (Hoefsmit basis with rational entries), then `tr_M` is
   automatically real for real `q`, and the modulus is trivial.
   For complex `q`, `tr_M` becomes complex but the operator
   matrix entries are still real-valued functions of `q`. **This
   is the most likely actual reason** the framework uses real `q`:
   the seminormal/Hoefsmit basis gives real-coefficient
   matrices, and complex `q` would require analytic continuation
   of the basis itself.

4. **No structural reason — pure convention.** Most likely
   correct: nobody asked the question.

### Open follow-on questions

- Empirical: solve simultaneously for `(u, v)` from CAL-2 + CAL-3 exactly. ~2 hours implementation given existing per-braid mass infrastructure; queued for Path B.
- Theoretical: are masses `|tr_M(Hermitian op)|` or `|tr_M(generic op)|`? If the former, the categorical observable is real by QM and modulus is degenerate. If the latter, Im(`tr_M`) is genuine info that the modulus projection discards. **The Hoefsmit seminormal basis suggests the matrices are real on the substrate; the operators ARE self-adjoint with real eigenvalues; the modulus is structurally degenerate at real `q` and only becomes a genuine projection at complex `q`.**
- Notation: introduce explicit `q ∈ ℝ` vs `q ∈ ℂ` annotations on every observable formula in the paper, so the projection is unambiguous.

## Open structural questions raised by owner (same chat)

1. **q_0 ∈ ℂ exploration**: if (b) holds, the +0.17% gap is NOT brane-tower truncation. Could it be Im(q_0) effects? **Updated**: my initial answer "no, q_0 real because m_μ/m_e equation is real" was circular — assumes `observable = literal categorical value`. The framework has never specified the projection rule (literal, Re, modulus, Hermitian eigenvalue). Per **Path D** above, the real-q choice is *convention*, not theorem. Five options remain open:
   - (i) **Strict reality**: observables always real by structure; q ∈ ℝ only.
   - (ii) **Hermitian extraction**: complex op, eigenvalues real on *-symmetric ops; q ∈ ℂ with * compatibility.
   - (iii) **Re-projection**: complex observable; we measure `Re(observable)`; q ∈ ℂ.
   - (iv) **Modulus-projection**: complex observable; we measure `|observable|`; q ∈ ℂ.
   - (v) **Phase-pinned**: complex but phase aligned; we measure real component along chosen axis.
2. **Φ_q under bar / star / skew involutions, pre vs post Archimedean**: if the per-braid mass formula has involutive structure that the unweighted `net` formula doesn't reproduce, that's evidence FOR (b). Open analytical work; not yet started.
3. **q_0 = Re(complex observable)?**: see Q1 above. NOT currently formalized; would require either (iii)/(iv) projection rule OR a complex-valued `m_μ/m_e` observable (none in the current framework). Skein-mass-relation does NOT answer this — it states a real equation under the implicit (i) assumption.

The fitting concern (b) is the dominant gap; the structural questions (Q1/Q3 fused) are now addressable via Path D.

## Addendum (2026-08-27) — `net` is fully expressible in derived framework objects; step 8's postulate is narrower than it looks

Bean `qou-xzrj`, PR #5869. Seven tranches, all exact-symbolic over $\mathbb{Q}(q)$
with the Markov parameter $z$ carried as a free symbol.

### What was shown

`net` — the unweighted NF coordinate sum of step 6 — has an **exact
representation** in objects this framework already derives:

$$\mathrm{net}(x) \;=\; \sum_\lambda a_\lambda\,\chi^\lambda(x) \;+\; \mu\,\mathrm{tr}_M(x\,d_C),
\qquad \mu \;=\; \frac{-\dim V_{(2,1)}}{c_{(2,1)}\,y_{(2,1)}(z)}$$

exact on all six basis elements, where $d_C$ is $\Delta$'s commutator part.
Every ingredient is a canonical invariant of one Wedderburn block:

| ingredient | what it is | status |
|---|---|---|
| $\mathrm{net}(x) = \tau(x\,\Omega)$, $\Omega = \sum_w T_w$ | `net` is the symmetrizing trace against the **all-ones** element | derived (rank 6/6, unique) |
| $1/c_{(2,1)}$ | the block's **Schur element**, from $\tau = \sum_\lambda \chi^\lambda/c_\lambda$; $c_{(2,1)} = [3]_q$, the hook formula | derived |
| $\dim V_{(2,1)} = 2$ | the **regular-rep multiplicity**: $\chi_{\mathrm{reg}} = 2\chi^{(2,1)}$ on $[H,H]$ | derived |
| $1/y_{(2,1)}(z)$ | the **pairing normalisation** on the block (Wedderburn) | derived |

Why a *pairing* is needed at all: every trace annihilates $[H,H]$, and 7.67 % of
$\varepsilon_{np}$ lives there. A trace is linear; $\langle x,y\rangle = \mathrm{tr}_M(xy)$
is bilinear and is not. Under convention D the pairing is degenerate on $H_3$
with radical the $(1^3)$ ideal — but $[H,H] = \mathfrak{sl}_2$ sits in the
**two-row** $(2,1)$ block, so the pairing is degenerate exactly where the
remainder is *not*.

A by-product worth recording: $c_{(2,1)}\,y_{(2,1)}(z) = -(z^2 - hz - 1)$ — the
**Hecke quadratic factorises** into the block's Schur element times its Markov
weight.

### Where the last constant comes from — and it is step 3, not a postulate

The one identity the chain rests on is $\mathrm{comm}(\Omega) = -\dim V_{(2,1)}\cdot d_C$
(ratio exactly $-2$). Varying **only** the mixed crossing $t$ in $\Delta$'s
construction:

| $t$ | proportional? | ratio |
|---|---|---|
| $h/2$ (corpus) | **yes** | $-2 = -\dim V_{(2,1)}$ |
| $h/3$ | no | — |
| $h$ | no | — |
| $0$ | no | — |

At any other $t$ the proportionality **fails outright**. So the identity is
contingent on $t = h/2$ — which is **step 3** of the table above, marked
✓ Derived, and its stated justification checks exactly:
$\big(C(\mathfrak{u},\mathfrak{u};\sigma) + C(\mathfrak{d},\mathfrak{d};\sigma)\big)/2
= (\sigma + (\sigma - h))/2 = \sigma - h/2$, the symmetric midpoint forced by
$\mathfrak{u}\leftrightarrow\mathfrak{d}$ swap symmetry.

**So the chain grounds out in derived material, not in an undischarged
assumption.**

### What this does NOT do

It does **not** close step 8. Step 8 postulates that
$Q_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$ — that the unweighted NF sum
*is* the leading-order mass difference. That is a claim about the **physical
identification**, and nothing above touches it: showing `net` is expressible in
derived algebraic objects says what `net` is, not that it is the right
observable. Scope-(a) throughout; nothing is wired, no value is proposed.

Related, and adverse, from the same branch's predecessor (PR #5864): the
complete set of functionals that descend to the convention-D Temperley–Lieb
quotient is **two**, and they bracket CODATA from $+12.470\%$ and $-43.157\%$,
while $\varepsilon_{np}$ — which does *not* descend — gives $+0.168\%$.

### Corrections to earlier statements in this investigation

Recorded because they were published on the branch before being caught:

1. **`t = h/2` is step 3, not step 4.** Step 3 defines the typed-crossing
   operators; step 4 only assembles words from them.
2. **Neither step is "chosen".** Both are marked ✓ Derived here. Bean
   `qou-xzrj` *asks* whether the single-wrap presentation is forced; that is a
   question, not a flag, and I quoted it as one.
3. **The $y_0 \parallel d_C$ alignment was over-read**, across three tranches.
   The set $\{x : \mathrm{comm}(x) \parallel d_C\}$ is a subspace of dimension
   **4 of 6** — two thirds of the algebra. The content was never the
   proportionality, only the ratio.
4. **A mislabel:** $\Omega$'s *commutator part* is not its $(2,1)$-component;
   $\chi^{(2,1)}(\Omega) = 2h \neq 0$.

Probes: `qbeta_trace_invisible_is_pairing_representable_probe.py` (12/12),
`qbeta_riesz_element_is_structurally_forced_probe.py` (9/9),
`qbeta_mu_closed_form_and_delta_alignment_probe.py` (6/6),
`qbeta_mu_normalisation_is_derived_probe.py` (5/5),
`qbeta_mu_is_block_invariants_probe.py` (7/7),
`qbeta_net_is_tau_against_all_ones_probe.py` (8/8),
`qbeta_last_step_is_the_presentation_probe.py` (4/4).
Lean: `QOU/QBeta/PairingSeesCommutator.lean`, 4 declarations, sorry-free.
