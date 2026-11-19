The Hecke mass element
$\Phi_{\mathrm{mass}}(\beta) \in H_3(R, q)$
([Hecke mass element](#def:hecke-mass-element)) has a
specific normal form structure determined by the **word
length filtration** on the NF basis.

## Statement

**Proposition (conditional on [mass-endomorphism conjecture](#conj:mass-endomorphism)).**
*For any particle with braid representative $\beta$ in
$H_3(R, q)$, the Hecke mass element has the NF decomposition:*

$$
  \Phi_{\mathrm{mass}}(\beta)
  =
  a_1(\beta)\,(\sigma_0 + \sigma_1)
  +
  a_3(\beta)\,(L_+ + L_-)
  +
  a_5(\beta)\, e^-
$$

*with $a_0 = 0$ ($\gamma$ coefficient vanishes).  The
coefficients $a_1, a_3, a_5 > 0$ depend on the specific
particle through its brane tower weights.*

## Vanishing of $\gamma$ (photon masslessness)

The :refterm[descent]{#descent} involution $\hat\tau_n$ at the first brane level
projects onto the $H_1(q)$ content of $H_3(R, q)$.  Since
$H_1(q) = \mathrm{span}\{\gamma\}$ (the identity is the
only degree-0 element), the descended component at level
0 is $\gamma$.  The **transient** component at level 0
therefore has zero $\gamma$ coefficient — it lives in
$\ker(\hat\tau_0) = \mathrm{span}\{\sigma_0, \sigma_1, L_+, L_-, e^-\}$.

Since all brane levels $n \geq 1$ contribute to
$\ker(\hat\tau_{n-1})$, and the accumulated mass element is
the sum over all levels, the total $\Phi_{\mathrm{mass}}$
inherits $a_0 = 0$ from the first-level filtration.

This is the **NF statement that the photon is massless**:
the mass endomorphism has zero projection onto $\gamma$.

## Degree filtration and cycling

The NF basis has word lengths (degrees):

| Degree |    Basis elements    |      Tower levels     |
| :----: | :------------------: | :-------------------: |
|   $0$  |       $\gamma$       |   Descended (killed)  |
|   $1$  | $\sigma_0, \sigma_1$ | $n = 1, 4, 7, \ldots$ |
|   $2$  |      $L_+, L_-$      | $n = 2, 5, 8, \ldots$ |
|   $3$  |         $e^-$        | $n = 3, 6, 9, \ldots$ |

The :refterm[descent]{#descent} involution at level $n$ kills elements of degree
$\leq (n-1) \bmod 3$, so the transient contribution at level
$n$ lives in degree $(n \bmod 3)$ elements.  The tower cycles
through degrees $1 \to 2 \to 3 \to 1 \to 2 \to 3 \to \cdots$,
accumulating contributions to $\sigma_i$, then $L_\pm$, then
$e^-$, repeating.

## Explicit NF for the electron

For the electron (trefoil, $\mathrm{Li}_2(q^{-2})/\hbar_q^2$
mass formula), grouping the $\mathrm{Li}_2$ series by
$n \bmod 3$:

$$
  S_k = \sum_{\substack{n \geq 1 \\ n \equiv k \pmod{3}}}
  \frac{q^{-2n}}{n^2},
  \qquad k \in \{1, 2, 0\}
$$

gives:

|             Group             |    Contributes to    | Fraction of $\mathrm{Li}_2$ |   NF coefficient   |
| :---------------------------: | :------------------: | :-------------------------: | :----------------: |
| $S_1$ ($n = 1, 4, 7, \ldots$) | $\sigma_0, \sigma_1$ |           $76.9\%$          | $a_1 \approx 86.2$ |
| $S_2$ ($n = 2, 5, 8, \ldots$) |      $L_+, L_-$      |           $16.7\%$          | $a_3 \approx 37.4$ |
| $S_0$ ($n = 3, 6, 9, \ldots$) |         $e^-$        |           $6.4\%$           | $a_5 \approx 13.4$ |

The electron mass is mostly carried by the **crossing
channels** ($\sigma_0, \sigma_1$), not by the trefoil
channel itself.  The $e^-$ coefficient ($\approx 13.4$
including the descended part) is only $12\%$ of the total
mass element norm.

**Witness**: computed from $\mathrm{Li}_2(q^{-2})$ grouping
at $q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps).
