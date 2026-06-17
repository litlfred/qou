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

## 6. Verdict so far

The B_sym lever is **real but already-identified and stuck**. The honest
contribution here is to (1) formalize the mechanism rigorously and (2)
confirm-or-refute the diagnosed $e_-$ fix — **not** to claim a new win.
Critical-distance note: any "B_sym improved by X%" claim must avoid the
(2,2)/Wigner post-hoc trap — the $e_-$ projection introduces **no free
parameter**, which is what keeps it on the right side of the
three-calibration discipline.
