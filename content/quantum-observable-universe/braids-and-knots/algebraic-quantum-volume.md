**Definition.**
*The **algebraic quantum volume** of a braid element
$\beta \in H_n(R, q)$ is the product of traced volumes:*

$$
  \mathrm{Vol}_q(\beta)
  \;=\;
  \prod_{i=0}^{n-2} \hat{V}_i(q)
  \;\in\;
  \mathbb{Z}[q^{1/2}, q^{-1/2}]
$$

*where $\hat{V}_i(q) = z(q) \cdot a_i(q) + b_i(q)$ is the
traced volume of generator $i$, with $a_i(q)$ and $b_i(q)$
the Laurent polynomial entries of the transfer matrix chain
([Markov trace product](#thm:markov-trace-product)).*

*The algebraic quantum volume lives in
$\mathbb{Z}[q^{1/2}, q^{-1/2}]$ — the ring of Laurent
polynomials in $q^{1/2}$.  It is an algebraic object.
Its real-valued archimedean shadow is obtained by
applying the QOU fibre functor*

$$
  \tau \;:\;\mathbf{C}\;\longrightarrow\;\mathbf{Arch},
$$

*restricted to its archimedean component
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
(see [archimedean realization functor](#def:archimedean-realization-functor)
and [Vol(K) factors through $\tau$](#prop:vol-through-tau)). Concretely,*

$$
  \Phi_1(\beta)
  \;:=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\;
  \ln\lvert\mathrm{Vol}_{q_0}(\beta)\rvert
  \;=\;
  \sum_{i=0}^{n-2} \ln\lvert\hat{V}_i(q_0)\rvert,
$$

*where $\tau_{\mathrm{arch}}$ acts on a generator $\hat{V}_i$ by
specializing $q \mapsto q_0$ at the archimedean place and taking
the absolute logarithm. The logarithm is not an extraneous
transcendental operation: it is the canonical map
$|\cdot|_\infty \to \log|\cdot|_\infty$ on the archimedean place
of the [adelic substrate](#def:adelic-substrate), packaged as the
$\tau_{\mathrm{arch}}$-image of the multiplicative quantum-volume
generator. Every archimedean physical observable derived from
$\mathrm{Vol}_q$ is the image of a categorical morphism under
$\tau_{\mathrm{arch}}$ — there is no other archimedean route.*

*The three Wedderburn invariants of the mass formula
([three-invariant mass formula](#thm:wedderburn-mass-formula))
correspond to three algebraic volumes:*

| Invariant | Algebraic volume | Ring |
|:----------|:-----------------|:-----|
| $\Phi_1$ | $\prod \hat{V}_i$ | trace of std rep |
| $\Phi_2$ | $\prod \det(M_i)$ | sym $\times$ alt product |
| $\Phi_3$ | $\prod (\lambda_i^{\mathrm{sym}}/\lambda_i^{\mathrm{alt}})$ | sym/alt ratio |

*Each factor is algebraic in $q$.  The mass formula is the
$\tau_{\mathrm{arch}}$-image of the categorical product, evaluated
on the three Wedderburn channels:*

$$
  \mathcal{M}
  = M_{\mathrm{free}}
  + \alpha \cdot \ln\left\lvert
    \mathrm{Vol}_q^{(1)} \cdot
    \bigl(\mathrm{Vol}_q^{(2)}\bigr)^{-2[3]_q} \cdot
    \bigl(\mathrm{Vol}_q^{(3)}\bigr)^{H_A^2}
  \right\rvert_{q=q_0}
$$

*Every intermediate computation — ground-state ordering, electron
insertion, transfer matrix chain, partition traces — is algebraic
in $q$ and internal to $\mathbf{C}$; the only step that exits is
the final $\tau_{\mathrm{arch}}$, which is the unique boundary at
which categorical data crosses into archimedean geometry.*

*For the Habiro ring: the algebraic volume embeds into
$\widehat{\mathbb{Z}[q]}$ (the cyclotomic completion),
where it coexists with the colored Jones polynomials at all
roots of unity.  The mass at $q_0$ is the evaluation at a
non-root-of-unity point.*
