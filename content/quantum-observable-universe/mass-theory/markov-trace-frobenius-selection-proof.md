**Proof sketch.**  Non-degeneracy is required by the Frobenius
co-Casimir construction (Step 3).  $\tau_M$ is non-degenerate
(Jones \cite{jones1987} Theorem 6.1; Wenzl \cite{wenzl1988} Lemma
2.4).  Any other non-degenerate trace on $H_n(R, q)$ satisfying
the Markov-peel + cyclic axioms equals $\tau_M$ by Wenzl's
uniqueness corollary to Lemma 2.4 (equivalently Jones' Markov
trace uniqueness).  Hence $\tau_M$ is the unique such trace. ∎

## Computational consequence

The QOU production stack computes $\tau_M$ on the
**11-crossing canonical proton / neutron braid** via four
independent paths — Hoefsmit seminormal matrices
(`atomic_tr_m_mpfr_50dps.py`), `markov_peel`, the $\chi$-cache
combiner (`canonical_tr_m_via_chi_cache.py`), and the Habiro
integer-$a_m$ expansion — which agree to $\leq 2 \times 10^{-15}$
at the proton-pinned $q_0$:

| atom | $\tau_M(\beta_{\rm atom}, q_0)$ | error vs 4-way |
|---|---:|---:|
| proton | $1.0653061442544499$ | $\leq 2.57\times 10^{-16}$ |
| neutron | $0.9232332299116371$ | $\leq 2.03\times 10^{-16}$ |
| deuteron | $0.3882864240747888$ | $\leq 8.16\times 10^{-16}$ |

> **Pedagogical alternative (deprecated for production).** The
> `from_scratch/` pipeline computes $\tau_M$ via the Markov axioms on
> a **different braid choice** (single-component free-proton braid,
> not the 11-crossing canonical recipe), yielding $\tau_M(p_{\rm free},
> q_0) \approx 1.7339$ — a legitimate Jones–Markov value on its
> *own* braid, not a competing convention for the 11-crossing braid
> above.  An earlier escalation framed this as a "$\tau_M$ /
> $\tau_{\mathrm{SW}}$ conflation" but the audit doc itself records the
> different-braid framing (line 248-251); decision A' purges
> $\tau_{\mathrm{SW}}$ and reads the from-scratch as a different
> braid's $\tau_M$, not a competing form.
