# Singlet (e₋) channel and B_sym — Bell/EPR follow-up exploration

**Date:** 2026-06-17
**Branch:** `claude/laughing-hopper-lbo214`
**Context:** Chat exploration starting from "does QOU state locality vs
nonlocality?" → "formulate Bell/EPR in QOU" → "can we use this to improve
m_sym / B_sym?". This doc records the durable findings, the **corpus-grep
prior-art check** (which reframes the question), and the plan.

## 1. Bell/EPR in QOU — outcome

QOU states locality/non-locality in two technical senses (algebraic
Markov-vs-GS, [`trace-locality-meets-gs-nonlocality.md`]; causal
KZ-flatness + Lieb–Robinson, [`q-holonomy-locality-derivation.md`],
[`information-causality.md`]) but **does not** address Bell/EPR
(no Bell/EPR/hidden-variable content in `content/`).

Formulating it: the EPR pair is the **antisymmetric ($-q^{-1}$) eigenstate
of the braiding $\sigma$** — the $q$-singlet $e_- = (q-\sigma)/[2]_q$, which
is exactly the **EM/gauge coupling channel** (`thm:em-spectral-completeness`,
`cor:gauge-coupling-uniqueness`; verified in
`computations/rt_c23_singlet_sign_core.py`). The concurrence of the 2-strand
$q$-singlet is the clean $C = 2/[2]_q$.

**Verdict (Bell/EPR):** the EPR structure is genuinely instantiated (the
deuteron's single $p$–$n$ inter-crossing lives in $e_-$), but there is **no
new Bell observable** — the measured two-body quantity QOU computes is a
*binding energy*, not a correlation function. The "(2,2)/Wigner matches
without fitting" support cited mid-exploration is **post-hoc** (see §4).

## 2. The B_sym connection (the useful lever)

From [`standard-part-functor.md`] + `computations/mass_binding_dashboard.py`:

$$
  B_{\mathrm{sym}} = \alpha\,\ln\!\frac{\mathrm{tr}_M(W_{\mathrm{free}})}{\mathrm{tr}_M(W_{\mathrm{atom}})},
  \qquad \alpha = E_0 = \frac{m_e}{q_0(q_0-1)}.
$$

$W_{\mathrm{free}}$ and $W_{\mathrm{atom}}$ differ **only** by the
inter-nucleon crossings — and those crossings sit in the $e_-$ coupling
channel. So B_sym's binding *is* the $e_-$-channel contribution of the
interface crossing(s). The natural, **parameter-free** refinement: resolve
the interface crossing into $e_\pm$ and keep only the coupling channel.

## 3. Exact 2-strand mechanism (verified by hand)

With $\sigma^2 = h\sigma + 1$, $h = q-q^{-1}$, Bezout projectors
$e_- = (q-\sigma)/[2]_q$, $e_+ = (\sigma+q^{-1})/[2]_q$ (all identities below
are **linear** in $\sigma$ — no quadratic needed):

$$
  e_+ + e_- = 1,\qquad
  \sigma = q\,e_+ - q^{-1}e_-,\qquad
  \boxed{\,1-\sigma = (1-q)\,e_+ + (1+q^{-1})\,e_-\,}.
$$

The binding observable is $\mathrm{tr}_M(1-\sigma) = 1 - z$ (free minus
bound), $z = 1/(q^{1/2}+q^{-1/2})$. Its channel split, with Markov weights
$y_{(2)} = (z+q^{-1})/[2]_q$, $y_{(1,1)} = (q-z)/[2]_q$
(`computations/y-lambda-closed-form-n2.md`):

$$
  1 - z = \underbrace{(1-q)\,y_{(2)}}_{e_+\ \text{(symmetric)}}
        + \underbrace{(1+q^{-1})\,y_{(1,1)}}_{e_-\ \text{(antisymmetric)}}.
$$

At $q_0 \approx 1.10998$: $y_{(2)} = 0.69633$, $y_{(1,1)} = 0.30367$,

| channel | coefficient | contribution to $1-z$ | sign |
|---|---:|---:|:--:|
| $e_+$ symmetric | $1-q = -0.110$ | $-0.0766$ | **anti-binding** |
| $e_-$ antisymmetric | $1+q^{-1} = +1.901$ | $+0.5773$ | **binding** |
| total | | $+0.5007 = 1-z$ | |

The symmetric channel **cancels** ~13% of the antisymmetric binding. Since
B_sym **under-binds** (dashboard error $B_{\mathrm{AME}}/B_{\mathrm{sym}} > 1$),
dropping the $e_+$ cancellation moves the prediction toward AME — a concrete,
parameter-free, directional prediction.

## 4. Prior art (corpus-grep) — this reframes the question

The §3 mechanism is **not novel** and the broad class has **negative
precedents**:

- **Already diagnosed:** [`docs/audits/2026-05-19-weight-factor-audit.md`
  §186] states the antisymmetric channel carries the missing (negative)
  binding and proposes the fix "explicitly projecting onto both $\pm h/2$
  eigenspaces of the averaged crossings." We independently re-derived this.
- **Broad class is NEGATIVE:** [`docs/_archive/orphan-top-level/alpha-fsc-audit.md`
  §206, round 6 (2026-04-28)] — "the atomic combination convention for
  binding energy is **not** any single-channel rearrangement of the nucleon
  $\mathrm{tr}_M$ values" (1.09× improvement only).
- **Nearest execution is POST-HOC:** the self-conjugate **(2,2) Wigner**
  correction ([`wigner-np-pairing.md`], $m_e H_q((2,2))\approx 6.29$ MeV) was
  audited 2026-06-17: the partition/hook-product/prefactor were selected from
  ~10 values bracketing 6.3 MeV (the *classical* hook product gives 6.13 too),
  it *worsens* cal-spread (`per-braid-wigner.witness.json`), its producers are
  in `_deprecated/`, and the Lean sibling is `: True := trivial`.

**Distinction that keeps a narrow question open:** round 6 rearranged the
final *scalar* nucleon traces; the 2026-05-19 fix changes the **$\chi^\lambda$
accumulation itself** (split the interface operator inside the trace). No
witness has *executed and validated* the operator-level $e_-$ projection on
B_sym. That is the open sub-problem.

## 5. Plan (this PR)

1. **Formalize the mechanism** (solid regardless of the numeric outcome):
   a sorry-free `lemma` for the channel split $1-\sigma=(1-q)e_+ +(1+q^{-1})e_-$
   over a generic field, with the $q>1$ sign leg over $\mathbb{R}$
   (symmetric channel anti-binding, antisymmetric binding). This turns the
   2026-05-19 prose diagnosis into proved math.
2. **Settle the open sub-problem** (compute): execute the interface $e_-$
   projection inside `tr_m_atom_zn` for D / T / ³He / ⁴He, compare
   $B_{\mathrm{sym}}^{(e_-)}$ vs $B_{\mathrm{sym}}$ vs AME. Emit a witness.
   Outcome is informative either way — confirm revives the path; refute is a
   formalize-the-refutation candidate (compute-author §3.4).

## 6b. The real gap: Σ_λ does not commute with the archimedean functor τ (observe-last)

The completeness question ("how do we know there aren't more terms? use rep
theory / cohomology") resolves cleanly, and it **retires the additive-sum
framing** (`m_sym + entanglement + h2 + antisymm`) entirely:

1. **Trace-channel completeness is a theorem.** $\sum_{\lambda\vdash n} z_\lambda
   = \mathbf 1$ (resolution of identity; $H_n(q_0)$ split semisimple). So
   $\mathrm{tr}_M = \sum_\lambda y_\lambda\chi^\lambda$ is exhaustive — exactly
   $p(n)$ channels, no more. The complete per-block carrier is the **q-Reeb
   phase** $\theta_\lambda=\arccos(\chi^\lambda/d_\lambda)$ (one per block).
2. **Input completeness is cohomological.** $H^1(\text{Bring})=2W \Rightarrow$ 3
   real calibration DOF (no 4th calibration). Different theorem, different half.
3. **The "extra terms" are early-collapse re-slices, not additions.**
   entanglement (bar-odd), antisymm (e₋), h2 (h-order) are all *gradings of the
   one complete trace*; they overlap → summing double-counts. e₋ in particular
   is the same early-collapse mistake as the scalar trace (project a channel
   *before* observing).
4. **The genuine gap is a non-commutation.** τ (step 9) is K-linear + monoidal,
   so it commutes with $\sum_\lambda$ and $\prod$ — **but** Kashaev
   $\mathrm{tr}_M\sim\exp(\mathrm{Vol})$ makes τ exponential, and
   $\log(\sum_\lambda)\neq\sum_\lambda\log$. Production collapses $\theta_\lambda$
   into the scalar $\mathrm{tr}_M$ at **step 5**, *before* τ at step 9. That is
   exact at A=2 (linearization) and lossy at A≥3. The lost content is the
   documented residual $\Delta_\lambda(K)\approx q_0^{\,10A-5}$ (D exact to 0.01;
   [residual audit](2026-06-09-delta-lambda-canonical-residual.md)).

**Fix = observe-last** (cheat-sheet §9.3): carry the full per-λ $\theta_\lambda$
vector (rotation $\arccos$ + growth $\mathrm{arccosh}$) through the GB/jet tower
and let τ collapse it *last*. The un-collapsed carrier is already emitted by
[`binding_reeb_phase_decomposition.py`](../../computations/binding_reeb_phase_decomposition.py).
The closure is **additive over inter-nucleon bonds**, not a per-block density to
multiply ([intensive-vs-extensive reframing](2026-06-09-delta-lambda-canonical-residual.md)).

**So the answer to "are we missing a factor?":** yes — not a new term, but the
non-linear (exp/log) part of τ acting on the per-block phases that the step-5
scalar collapse truncates. The e₋ probe is superseded by this reframe and was
removed (its algebraic split $1-\sigma=(1-q)e_+ +(1+q^{-1})e_-$ and the
$e_++e_-\equiv\mathrm{atom}$ identity are recorded in §3 above).

## 6c. observe-last probe result — additive phase REFUTED; residual is per-object q₀⁵

[`binding_observe_last.py`](../../computations/binding_observe_last.py) (witness
`binding-observe-last.witness.json`) executes the §6b observe-last collapse and
compares it to production observe-early `B_pred = Q_β·(|tr_free|−|tr_atom|)`
(Q_β = 0.78233 MeV, CAL-3 — **not** E₀ = 4.186). Preflight: reproduces the
residual-audit table to 4e−5, and `e_pred = log_{q0}(B_AME/B_pred)` =
14.99 / 24.93 / 23.60 / 35.27 ≈ 10A−5 ✓ (data + weights + scale validated).

**The additive observe-last `B_late = Q_β·Σ_λ y_λ(θ_λ^free − θ_λ^atom)` is
refuted:** it is small, **negative**, and **shrinks** with A
(−0.067, −0.014, −0.008, −0.0015 MeV for D/T/³He/⁴He; growth-only variant
likewise tiny). The residual it must reproduce is the **opposite** — large,
positive, **growing** (q₀¹⁵ → q₀³⁵, i.e. ×4.8 → ×39 on B_pred). The Jensen gap
of the per-block phase sum is not the residual.

**Formalize-first prune (the real structural reading).** The residual factorises
$$ q_0^{10A-5} = q_0^{5(2A-1)} = \underbrace{(q_0^{5})^{A}}_{\text{nucleons}}\cdot\underbrace{(q_0^{5})^{A-1}}_{\text{interfaces}}, $$
a **per-object multiplicative q₀⁵** (one factor per nucleon + one per inter-
nucleon bond, the §6b "additive over bonds" — but additive *in the exponent*).
An additive phase sum (bounded, O(1)/block, → 0 as the trace concentrates)
**cannot** produce a factor geometric in A. So **any observe-last closure that
recovers the residual must be exponential / per-object-multiplicative**, not an
additive phase sum. The observe-last *infrastructure* (carry per-λ θ to step 9)
is correct; the additive *collapse* is the wrong one. The open step is unchanged
from the 9b workplan H1: derive **q₀⁵ per chain object** from the jet/crossing
bookkeeping of `W_free` vs `W_atom` (12 crossings/nucleon, +1/interface).

## 6d. formalize-first sharpening of the q₀⁵ target — and the STOP

Per-object crossing counts of `atom_braid_word_3A` (compute, this session):
`free_cr = 11A`, `atom_cr = 12A−1 = 11A + (A−1)`, interfaces `= A−1`, intra/nucleon
`= 11` (constant). So the residual exponent factorises **not per-crossing** but
**per chain object**:
$$ 5(2A-1) = \underbrace{5A}_{\text{per nucleon}} + \underbrace{5(A-1)}_{\text{per interface bond}}. $$
Check: D `5·2+5·1=15` ✓, T `5·3+5·2=25` ✓, ⁴He `5·4+5·3=35` ✓; ³He 23.60 vs 25 is
the −1.4 proton-rich deviation ⇒ the per-nucleon factor is **Z-dependent** (p ≠ n).

**Target sharpened:** derive a **q₀⁵ per nucleon** + a **q₀⁵ per interface bond**
(the latter Z-dependent). The exponent "5" is the open quantity.

**Formalize-first STOP (no wide search).** This is not a fresh lever. The
41-commit triage (Q1 verdict,
[`2026-06-17-parked-residual-and-detq-framing.md`]) places the per-nucleon
exactness shortfall as **plausibly the standing CAL-4 VolDensity(𝓑₃)
categorical-exactness gap** (research-grade Subgoal-2; eight structural searches
failed; the coordination ledger declined a substrate q₀-derivation; the Δ_λ gate
forbids a fit ansatz). Confirming that the per-isotope `q₀⁵`-per-object factor IS
the per-nucleon CAL-4 gap is itself open, but either way the "5" derivation sits
behind the gated wall. Honest deliverables this session: the sharpening above +
the observe-last **carrier infra** (§6c, `binding_canonical.binding_observe_last`,
DIAGNOSTIC). The "5" derivation is **held** (option 3) — not faked.

**Explore-4 result (corpus-grep) — closes NEGATIVE.** The trace route is not
merely gated but already **refuted**:
[`2026-06-13-9b-h1-exponent-location-refuted.md`] decomposed
`ord(Δ_λ) = ord(B_AME) − ord(B_pred)` and found the framework trace `ord(B_pred)`
drifts only +1.2…+2.9 per nucleon (decaying to 0), while the **+11.5…+12.8
per-nucleon increment is carried by the experimental curve `ord(B_AME)`**. So the
"5"/10A−5 is **experimental-side**, not trace/crossing-count bookkeeping —
deriving it ≡ deriving `B_AME(A)` itself (Track-A); fitted-adjacent near-match
tier (2 integer params; 3 compliant points + ³He outlier). The `2A−1`
chain-object count IS geometrically real (difference-link cusp count,
[`2026-06-13-difference-knot-jsj-classification.md`]) but the per-object weight is
the **Sage-blocked per-piece JSJ volume**. Consistent with §6c: any *trace*
collapse (early or late) cannot recover the residual, because the A-dependence is
not on the trace side. **No trace-derivable "5"; the q₀⁵ route is closed.**

## 7. Verdict so far

The B_sym lever is **real but already-identified and stuck**. The honest
contribution here is to (1) formalize the mechanism rigorously and (2)
confirm-or-refute the diagnosed $e_-$ fix — **not** to claim a new win.
Critical-distance note: any "B_sym improved by X%" claim must avoid the
(2,2)/Wigner post-hoc trap — the $e_-$ projection introduces **no free
parameter**, which is what keeps it on the right side of the
three-calibration discipline.
