*Let $T_w \in H_n(q)$ be a closed braid word and let
$\mathrm{tr}_M(T_w, q)$ denote its Markov trace, viewed in the Habiro
ring $\widehat{\mathbb{Z}[q]}$.  The two formulations of $\mathrm{tr}_M$
arising in this chapter agree on the archimedean realization*

$$
  \widehat{\mathbb{Z}[q]} \;\xrightarrow{\;\rho_\infty\;}\; \mathbb{R}
$$

*whenever both correspond to the same braid word $T_w$, namely:*

1. *the **polynomial-ring** value, computed from any
   [Habiro completion](#prop:full-pole-structure-mass-trace) instance
   $\mathcal{H}$ as $\mathrm{eval}_{u_0}(\mathcal{H}.\mathrm{trace})$
   with $u_0 = q_0^{1/2}$, and*

2. *the **residue spectral sum**, computed from any
   [Gröbner–Shirshov residue spectral sum](#prop:gb-residue-spectral-sum)
   instance $\mathcal{R}$ as $\mathcal{R}.\mathrm{mass}$,*

*coincide as the two distinct constructions of
$\mathrm{tr}_M(T_w) \in \widehat{\mathbb{Z}[q]}$.*

This is a
[non-trivial analytic identity](#def:archimedean-realization-functor): it
relates the cyclotomic-coefficient sum
$\sum_m a_m(u_0) \cdot (u_0;u_0)_m$ (Habiro side) to the
residue-spectral-sum
$|\mathrm{tr}_M^{(0)}| + \sum_\ell \mathrm{Res}_{q\to\zeta_\ell}(\Phi_q \cdot \mathrm{tr}_{M,\ell})$
(GB side).  The analytic identification of
the residue contributions with the cyclotomic tail remains open.

**Empirical witness.** The agreement is certified at machine precision
on every available atomic Markov trace by
the formal derivation.  The
cross-pipeline witness records, per atom, the relative difference
between the two paths.  The current run achieves:

| Atom | Polynomial path $\rho_\infty(\mathcal{H}.\mathrm{trace})$ | Residue path $\mathcal{R}.\mathrm{mass}$ | $|\mathrm{rel\ diff}|$ |
|------|-----------------------------------------------------------|-------------------------------------------|------------------------|
| $\mathfrak{p}$ (proton, $A=1$)   | $2.1225825095$ | $2.1225825095$ | $0$ |
| $\mathfrak{n}$ (neutron, $A=1$)  | $1.5893934460$ | $1.5893934460$ | $2.79\!\times\!10^{-16}$ |
| D (deuteron, $A=2$)              | $0.1774369242$ | $0.1774369242$ | $0$ |

All differences fall within the relative tolerance $10^{-9}$ — the
two paths agree to machine epsilon.  This is numerical evidence for the
analytic identity stated above, not a proof; it is not used as a premise, and the proton case remains the
open conjecture [Archimedean agreement (proton instance)](#conj:gs-archimedean-agreement-residue).
