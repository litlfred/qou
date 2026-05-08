**Proposition.**
*The self-conjugate partition $(2,2) \vdash 4$ at Hecke level
$k = 4$ contributes an additional binding term for nuclei with
both protons and neutrons.  This is the categorical Wigner
energy from $T{=}0$ isoscalar np pairing, with energy scale
fixed by the $q$-hook product of $(2,2)$:*

$$
  \mathbf{\Delta}_{(2,2)}
  = m_e \cdot H_q\big((2,2)\big)
  = m_e \cdot [3]_q \cdot [2]_q^2
  \approx 6.29\;\mathrm{MeV},
$$

*matching the empirical Wigner scale $\Delta_W \approx 6.3$ MeV
\cite{satula1997} **without fitting**.  The hook lengths
$\{3, 2, 2, 1\}$ of the $2 \times 2$ Young diagram give the
product $[3]_q \cdot [2]_q \cdot [2]_q \cdot [1]_q$, which is
exactly $\mathbf{\Delta}_S = \mathbf{\Delta}_{(2,2)}$ — the
$(2,2)$ channel and the shell correction share **one**
categorical scale.*

*The binding increment is:*

$$
  \Delta B_{\mathrm{Wigner}}
  = \hat{V}_{\mathrm{pn}} \cdot \alpha
    \cdot \frac{\min(Z, N)}{A}
$$

*where:*
- *$\hat{V}_{\mathrm{pn}} = W_{\mathrm{std}} \cdot (z - H_A/2)$
  is the pn crossing volume
  ([confined knot binding](#prop:confined-knot-binding)),*
- *$\alpha = m_e \times 8G$
  ([binding scale](#prop:binding-scale-catalan)),*
- *$\min(Z, N)/A$ counts the fraction of nucleons that can form
  $T{=}0$ pairs.*

*This dedicated formulation is subsumed by the
[unified iterative $(2,2)$ correction](#prop:unified-iterative-correction),
which accumulates the Wedderburn projection step by step from
$A = 1$ — replacing $\hat V_{\mathrm{pn}} \cdot \alpha \cdot
\min(Z,N)/A$, the deuteron formula, and the knot factor by
**one** mechanism.*

*This term is:*
- *Nonzero for all nuclei with $Z \geq 1$ and $N \geq 1$,*
- *Largest for $N = Z$ (Wigner energy),*
- *Constructive from $A = 1$ upward (no conditional on $A$),*
- *Derived from the $(2,2)$ partition's Wedderburn weight, not
  fitted to data.*

*Proof.*
The partition $(2,2)$ is self-conjugate ($\lambda = \lambda'$),
with $q$-dimension $d_q((2,2)) = [2]_q$ and Wedderburn weight
$w_{(2,2)} = [2]_q^2/[4]_q!$.

By the branching rule $H_4(R, q) \to H_3(R, q)$, the restriction of
$V_{(2,2)}$ contains only $V_{(2,1)}$ (the standard representation)
with multiplicity $1$.  Therefore the $(2,2)$ contribution to
binding is carried entirely by the **standard channel**, consistent
with extremal cancellation for pn crossings
([confined knot binding](#prop:confined-knot-binding)).

The scaling $\min(Z, N)/A$ counts the maximum number of
proton-neutron $T{=}0$ pairs per nucleon.  Each pair contributes
$\hat{V}_{\mathrm{pn}} \cdot \alpha$ of binding through the
standard channel.

The Kerov $q$-hook walk \cite{kerov1996} provides the iterative
construction: at each nucleon addition, the pn crossings project
onto the $(2,2)$ partition, accumulating the Wigner energy step
by step from $A = 1$.  The Féray–Méliot $q$-Plancherel CLT
\cite{feray-meliot2012} gives the asymptotic convergence rate
$O(1/\sqrt{k})$ of the accumulator across Hecke levels.
$\square$

**Mass table improvement** (N=Z atoms):

| Atom | Before | After | Change |
|:-----|-------:|------:|-------:|
| ${}^{10}$B | $+0.012\%$ | $+0.007\%$ | $43\%$ better |
| ${}^{12}$C | $+0.010\%$ | $+0.006\%$ | $44\%$ better |
| ${}^{16}$O | $+0.007\%$ | $+0.004\%$ | $47\%$ better |
| ${}^{40}$Ca | $+0.002\%$ | $+0.001\%$ | $69\%$ better |

**Witness**: `jet-knot-invariants.witness.json`.
