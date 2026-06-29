**Theorem (Frobenius antipode unifies chirality and the neutron-tower closure).**
*$H_n(R, q)$ is a self-dual Frobenius algebra
([Frobenius universal](#thm:frobenius-codim-universal)) with
canonical antipode*

$$
  S(\sigma_i) \;=\; \sigma_i^{-1}, \qquad
  S(ab) \;=\; S(b) S(a) \quad (\text{anti-homomorphism}),
$$

*equivalently in $(c, d)$-pair notation
([proton/neutron Hecke crossings](#def:atomic-braid))*

$$
  S \colon (1, 0) \;\leftrightarrow\; (1, -h),
  \qquad
  S \colon (1, -h/2) \;\mapsto\; (1, -h/2),
$$

*so $S$ swaps positive and negative Hecke generators while fixing the
averaged $ud$-pair $(1, -h/2) = \tfrac{1}{2}(\sigma + \sigma^{-1})$.
The same antipode $S$ is the common primitive of two derivations:*

1. *the **Term-5 chirality factor**
   ([chirality dual-space](#prop:chirality-dual-space-derivation)),
   which is the symmetric-channel antipode-asymmetry
   $\tau_{\mathrm{sym}}(\sigma) - \tau_{\mathrm{sym}}(S(\sigma)) = q - q^{-1} = h$,
   giving the per-pn-crossing factor $(1 + \mathrm{sign}\cdot h)$; and*
2. *the **neutron-tower closure**, which is the Frobenius
   symmetrization $\hat V_0^{\mathrm{Frob}} := \tfrac{1}{2}(\hat V_0 + \hat V_0\circ S)$
   of the per-generator brane-tower volumes.*
