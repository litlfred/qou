# T2/T3 Derivation Chain — what's actually derivable from category / jet / GB / Frobenius / spectral machinery

**Date:** 2026-05-03 (post per-channel + two-avenue probes; user
directive: "keep to what is derivable")

## TL;DR

Per the paper's own propositions, the **derivable** form of T2 and T3
in the canonical 6-term mass formula is:

$$
  r_\ell(T_w; q_0)
  \;=\;
  \frac{\operatorname{Res}_{q = \zeta_\ell}\bigl[\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]}{q_0 - \zeta_\ell},
  \qquad \ell = 1, 2,
$$

where $\mathrm{tr}_{M, \ell}$ is the **induced Markov trace on the
graded piece** $J^\ell(q)/J^{\ell+1}(q)$ of the Gröbner-Shirshov
confinement filtration on $H_n(R, q)$, and $\zeta_\ell$ is the root of
unity at which the $\ell$-th knot-operator energy degenerates
($E_\ell(\zeta_\ell) = 0$).  This residue IS Markov-invariant — both
$\Phi_q$ and the graded Markov trace transform cyclically.

The **literal $\Phi_q(|\hat V_i^{\mathrm{full}}|)$ form currently
implemented in `paper_six_term_isotope_sweep.py` is the archimedean
Kashaev specialisation of the residue** above.  It evaluates $\Phi_q$
on per-generator amplitudes — which is basis-dependent (not a trace).
That's the source of the −737 MeV brane-tower isospin pathology
documented in `brane-tower-isospin-diagnosis.witness.json` (PR #524).

## Derivation chain

| Step | Source | What's derived |
|------|--------|----------------|
| 1 | `prop:gb-spectral-sequence` | GB spectral sequence $(E_r^{\ell, *}, d_r)$ from filtered Hochschild complex over the categorical base ring $R$.  $d \circ d = 0$ from classical Hochschild theory; $E_\infty$ convergence from filtered-spectral-sequence theorems (Weibel §5.5). |
| 2 | `prop:e-infinity-page-identifications` | Page-by-page mapping: $E_\infty^{0,*}$ → T1; $E_\infty^{1,*}$ → T2; $E_\infty^{2,*}$ → T3; full pairing → T4; ribbon self-pairing → T5; $E_\infty^{\ell \geq 3, *}$ → T6. |
| 3 | `prop:gb-residue-spectral-sum` | Symbolic residue formula: $r_\ell(T_w; q_0) = \mathrm{Res}_{\zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\ell}] / (q_0 - \zeta_\ell)$ for each filtration level $\ell$. |
| 4 | `prop:full-pole-structure-mass-trace` | Habiro completion: $\mathrm{tr}_M(T_w) = \sum_m a_m(T_w)(q;q)_m$ with $a_m \in \mathbb{Z}[q^{\pm 1}]$.  The residue spectral sum and the Habiro expansion are equivalent representations modulo the cyclotomic-completion ideal. |
| 5 | `prop:mass-endomorphism-tower` | Kashaev archimedean specialisation: the residue $r_\ell$ specialises to $\Phi_q(|\hat V_i^{\mathrm{full}}|)$ via integrating the q-deformed expansion flow $\ln_q(1+t)/t$ over the resolved defect $E_i \cong \mathbb{P}^1(\mathbb{C})$.  This is **the step where Markov-invariance breaks**, because $|\hat V_i|$ is per-generator. |
| 6 | `prop:jet-prefix-gb-filtration` | Jet-tower interpretation: filtration level $\ell$ corresponds to jet bundle $J^\ell \mathcal{S}$.  Higher levels $(\ell \geq 3)$ ascend to next jet level. |
| 7 | `prop:sw-period-thimble-equivalence` | Picard-Lefschetz periods: the $\mathbb{C}$-side of the $E_\infty$ pairing is a thimble period $\Pi^{(p)}$ on the Descartes elliptic curve $\mathcal{E}_q(\mathbb{C})$. |

## What the derivation says T2/T3 ARE

**T2** is the pairing of the Markov trace cocycle against the
filtration-1 stratum of the Hochschild complex on $H_n(R, q)$,
evaluated via residue extraction at the filtration-1-degenerate root
of unity $\zeta_1$:

$$
  T_2 \;=\; \frac{\operatorname{Res}_{q = \zeta_1}\bigl[\Phi_q \cdot \mathrm{tr}_{M, 1}(T_w)\bigr]}{q_0 - \zeta_1}.
$$

This is rigorous, Markov-invariant, and computable directly from
$\mathrm{tr}_M(T_w; q)$ as a meromorphic function (or its Habiro
expansion).  PR #526's `term6_residues_at_roots.py` does this
extraction for $\ell \geq 2$ (T6); the same machinery extends to
$\ell = 1$ (T2) and $\ell = 2$ (T3) — what's needed is to identify
$\zeta_1, \zeta_2$ explicitly and compute the graded-trace
$\mathrm{tr}_{M, \ell}$ on the appropriate filtration stratum.

**T3** is the analogue at filtration level 2.

## What's NOT the derivation

The currently-implemented $\Phi_q(|\hat V_i^{\mathrm{full}}|)$ form is
**not** the derivation.  It's the closed numerical limit obtained
under a specific Kashaev-style substitution
($\mathrm{Vol}_q^{(S)} \rightsquigarrow \Phi_q(|\hat V_i|)$).  The
substitution loses Markov-invariance because $|\hat V_i|$ depends on
the choice of reduced word for the braid.

**At $q_0 \approx 1.11$**, $\Phi_q(0.99) \approx 6.7 \times 10^5$
amplifies the basis-dependence by $\sim 10^5$, producing the
$-737$ MeV mirror-nucleus pathology.  But this is an artefact of the
specialisation, not of the derivation.

## What probing has shown

- **Per-channel $\Phi_q$**
  (`brane-tower-per-channel-phi-q-probe.witness.json`):
  applying $\Phi_q$ separately to each Wedderburn channel and
  summing with $y_\lambda$ weights flips the sign of the violation
  (legacy −465 MeV → per-channel +516 MeV) but does not resolve.

- **Frobenius-antipode global symmetrization**
  (`brane-tower-two-avenues-probe.witness.json`, Avenue 2):
  $T_2^{\mathrm{sym}} = (T_2(\beta) + T_2(S(\beta)))/2$ reduces by
  ~2× (legacy +465 MeV → symmetrized −232 MeV).  Does not resolve.
  Verified: $S$ does NOT map T's atomic braid to ³He's at the
  per-strand level.

- **Kähler derivative on global** $\mathrm{tr}_M$
  (Avenue 1): the global Markov trace IS Markov-invariant (matches
  the Hoefsmit-Wenzl bridge witness).  Its derivatives
  $\partial^k/\partial q^k \mathrm{tr}_M(T_w)$ are also
  Markov-invariant.  At $q_0$:
  $\mathrm{tr}_M(T) = 0.0281$ vs $\mathrm{tr}_M(^3\mathrm{He}) =
  0.0749$ (factor ~2.7 — the canonical isospin signature, ~0.5 MeV
  at $E_0 \approx 7.95 \times 10^{-4}$, close to CODATA 0.019 MeV).
  Every Kähler derivative preserves this ratio.  This shows the
  trace itself encodes isospin correctly; the brane-tower
  pathology is purely the Kashaev specialisation amplifying the
  trace's natural factor-of-2 by $10^5$.

## Recommended path forward (pick one)

### Path A — Implement the rigorous residue form for T2, T3

Extend `term6_residues_at_roots.py` (PR #526) to filtration levels
$\ell = 1, 2$ — extracting $r_\ell(T_w; q_0)$ directly from the
symbolic Markov trace via `sympy.residue` at $\zeta_\ell$.  Requires:

1. Identifying $\zeta_1, \zeta_2$ explicitly (the roots of unity at
   which $E_1, E_2$ degenerate).  Probably $\zeta_1 = 1$ and
   $\zeta_2 = -1$ but should be derived from the knot-operator
   energy formula in `def:confinement-level`.
2. Computing the graded Markov trace $\mathrm{tr}_{M, \ell}$ on
   $J^\ell / J^{\ell+1}$.
3. Replacing $\sum_i \Phi_q(|\hat V_i|)$ in
   `paper_six_term_isotope_sweep.py` with the residue sum.

This is the principled fix.  Estimated scope: medium (requires
filtered-trace bookkeeping; PR #526's machinery covers most of it).

### Path B — Use Habiro coefficients $a_m(T_w)$ directly

The Habiro expansion $\mathrm{tr}_M(T_w) = \sum_m a_m (q;q)_m$ packages
ALL six terms (T1 + T2 + T3 + T6) into a single symbolic object.  At
$q_0$:

$$
  \mathfrak{m}_{q_0, T_w} \;=\; \sum_{m \geq 0} a_m(T_w; q_0) \cdot (q_0; q_0)_m + T_4 + T_5.
$$

Per `prop:full-pole-structure-mass-trace`, the expansion terminates
at $m_{\max}(T_w)$ (the confinement level).  Each $a_m$ is in
$\mathbb{Z}[q^{\pm 1}]$, hence Markov-invariant by inheritance.  This
collapses T1, T2, T3, T6 into a single sum and avoids the
specialisation.

Probe artefact: `habiro-coefficients-atomic.witness.json` (already on
main, computed via `habiro_coefficients_atomic_fast.py`) gives Habiro
coefficients for proton, neutron, deuteron.  Extending to T, ³He, ⁴He
is computational work bounded by symbolic expression size.

### Path C — Drop $\Phi_q$ specialisation entirely; predict from T1 alone

The "third avenue" surfaced in the two-avenue probe.  If
$\mathrm{tr}_M(T_w)$ alone (with T4 + T5 + T6) is sufficient at
$q_0$, then T2/T3 are unnecessary at the regular substrate point —
they only kick in at roots of unity (Reshetikhin-Turaev evaluations).
This would mean the formula at $q_0$ is

$$
  \mathfrak{m}_{q_0, T_w} \;\approx\; |\mathrm{tr}_M(T_w)| \cdot a_K + T_4 + T_6.
$$

Quick test (worth probing): predict atomic masses from this
simplified formula, compare to AME.  If errors are < 1% it's a
strong candidate.  If they're worse, T2/T3 contribute meaningful
binding even at $q_0$.

## Recommendation

**Path A** is the principled answer per the paper's own derivation.
Path B is a useful intermediate step (Habiro coefficients are
trace-invariant by construction).  Path C is a quick test of whether
T2/T3 even need to be in the $q_0$-evaluated formula at all.

Suggested order: C (1-day probe) → B (1-week extension) → A (multi-week
filtered-trace work).

## References

- `prop:gb-spectral-sequence`
- `prop:e-infinity-page-identifications`
- `prop:gb-residue-spectral-sum`
- `prop:full-pole-structure-mass-trace`
- `prop:mass-endomorphism-tower`
- `prop:jet-prefix-gb-filtration`
- `prop:sw-period-thimble-equivalence`
- PR #524 brane-tower isospin diagnosis
- PR #526 markov-peel followups (T6 residue extraction, kähler_lift)
- PR #534 singular canonical 6-term consolidation (this PR)
- gist (https://gist.github.com/litlfred/b3459bf9143dd03234a9fc55c370f6f4)
