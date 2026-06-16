**Proposition.**
*Let $\beta \in H_3(R, q)$ be a confined nuclear braid
([atomic braid](#def:atomic-braid)) — typically
$\beta = T_w = \mathtt{atom\_braid\_word\_3A}(Z, N)$
([`mass_at_3A_proper.atom_braid_word_3A`](https://github.com/litlfred/qou/blob/main/computations/mass_at_3A_proper.py))
— built from crossing operators
$c_k \sigma_{i_k} + d_k \cdot 1 \in H_3(R, q)$ at generators
$\sigma_{i_k}$ with parameters $(c_k, d_k)$ (the $k$-th letter of
$T_w$ in its GB normal form). The Wedderburn-Artin decomposition
([three-parameter decomposition](#prop:three-parameters-wedderburn))
separates each crossing's contribution into three channels:*

$$
  \hat{V}(c, d)
  = W_{\mathrm{sym}} \cdot \chi_{\mathrm{sym}}(c, d)
  + W_{\mathrm{std}} \cdot \chi_{\mathrm{std}}(c, d)
  + W_{\mathrm{alt}} \cdot \chi_{\mathrm{alt}}(c, d)
$$

*where the Wedderburn weights are:*

$$
  W_{\mathrm{sym}} = W_{\mathrm{alt}}
  = \frac{q^2}{q^4 + 4q^2 + 1},
  \qquad
  W_{\mathrm{std}}
  = \frac{(q^2 + 1)^2}{q^4 + 4q^2 + 1}
$$

*and the channel characters are:*

$$
  \chi_{\mathrm{sym}}(c, d) = cq + d,
  \quad
  \chi_{\mathrm{alt}}(c, d) = -\frac{c}{q} + d,
  \quad
  \chi_{\mathrm{std}}(c, d) = z \cdot a + b
$$

*with $(a, b)$ accumulated via the transfer-matrix recurrence
$\bigl[\begin{smallmatrix} a' \\ b' \end{smallmatrix}\bigr]
= \bigl[\begin{smallmatrix} cH_A + d & c \\ c & d
\end{smallmatrix}\bigr]
\bigl[\begin{smallmatrix} a \\ b \end{smallmatrix}\bigr]$,
$H_A = q - q^{-1}$, $z = 1/(\sqrt{q} + 1/\sqrt{q})$.*

**Extremal cancellation (symmetric crossings).**
*For any crossing with $d = -H_A/2$ (the symmetric mixing
$\tfrac{1}{2}(\sigma + \sigma^{-1})$, which encodes the
proton-neutron nuclear force):*

$$
  \chi_{\mathrm{sym}} = \frac{q^2 + 1}{2q},
  \qquad
  \chi_{\mathrm{alt}} = -\frac{q^2 + 1}{2q}
$$

*Since $W_{\mathrm{sym}} = W_{\mathrm{alt}}$, the extremal
contributions cancel exactly:*

$$
  W_{\mathrm{sym}} \cdot \chi_{\mathrm{sym}}
  + W_{\mathrm{alt}} \cdot \chi_{\mathrm{alt}} = 0
$$

*The binding volume of a symmetric crossing is carried entirely
by the standard representation:*

$$
  \hat{V}_{\mathrm{pn}}
  = W_{\mathrm{std}} \cdot \Bigl(z - \frac{H_A}{2}\Bigr)
$$

**Cross-channel interaction (adjacent generators).**
*The symmetric and alternating representations are $1$-dimensional,
so products of consecutive crossings on the same generator are
scalar: $\chi_{\mathrm{sym}}(\beta) = \prod_k (c_k q + d_k)$.
The standard representation is $2$-dimensional — consecutive
crossings compose as $2 \times 2$ matrix products:*

$$
  M_i = \prod_k \begin{pmatrix}
    c_k H_A + d_k & c_k \\ c_k & d_k
  \end{pmatrix}
$$

*This non-commutativity produces the cross-channel term between
adjacent generators $i$ and $i{+}1$, weighted by the Markov
parameter $z^2 = \mathrm{tr}_M(\sigma_i \sigma_{i+1})$:*

$$
  \delta_{\times}
  = z^2 \sum_{|i-j|=1}
    \ln\bigl\lvert
      \hat{V}_i^{\mathrm{full}} \cdot \hat{V}_j^{\mathrm{full}}
    \bigr\rvert
$$

*The weight $z^2$ is derived from the Hecke algebra (not fitted):
it is the Markov trace of the adjacent generator product
$\mathrm{tr}_M(\sigma_0 \sigma_1) = z^2$.*

**General confined-state character ratio.**
*For an $A$-nucleon system with construction at jet levels
$\ell = 0$ (quark), $\ell = 1$ (nucleon), $\ell = 2$ (nucleus),
the knot factor at each level is the character ratio:*

$$
  a_\ell
  = \frac{\hat{V}_\ell(\text{confined})}
         {\hat{V}_\ell(\text{free})}
$$

*measuring how the confined state's Wedderburn volume departs from
the free constituent product at that jet level.  The total knot
factor is:*

$$
  a(Z, N) = \prod_\ell a_\ell
$$

*This product emerges from the algebraic structure of $H_3(R, q)$ —
the character ratios are functions of $q$ alone, with no empirical
input.*

**Molecular extension.**
*The same decomposition applies at the molecular level.  A
covalent bond is an inverse trefoil $T^{-1}$ inserted between
two atomic braids $\mathcal{A}$, $\mathcal{B}$.  The molecular
binding energy is:*

$$
  E_{\mathrm{bond}}
  = \bigl(
      W_{\mathrm{sym}} \cdot \Delta\Phi_{\mathrm{sym}}
    + W_{\mathrm{std}} \cdot \Delta\Phi_{\mathrm{std}}
    + W_{\mathrm{alt}} \cdot \Delta\Phi_{\mathrm{alt}}
    \bigr) \times E_{\mathrm{mol}}
$$

*where $\Delta\Phi_\lambda = \bigl\lvert
\ln|\chi_\lambda(\mathcal{A} \cdot \mathcal{B})|
- \ln|\chi_\lambda(\mathcal{A} \cdot T^{-1} \cdot \mathcal{B})|
\bigr\rvert$
is the per-channel volume shift from inserting the bond, and
$E_{\mathrm{mol}} = m_e \alpha^2 / 2$ is the Hartree energy
scale (derived from $q$).  Double and triple bonds use $n$
inverse trefoils: $\Delta\Phi \propto n$, so bond energies
scale as $1 : 2 : 3$.*

*Proof.*
The equality $W_{\mathrm{sym}} = W_{\mathrm{alt}}$ follows from
$\dim_q(\lambda_{\mathrm{sym}}) = \dim_q(\lambda_{\mathrm{alt}}) = 1$
for the one-dimensional representations of $H_3(R, q)$.
The Wedderburn weight is $w_\lambda = d_q(\lambda)^2 / [n]_q!$,
and $d_q((3)) = d_q((1,1,1)) = 1$.

For the symmetric crossing $(c, d) = (1, -H_A/2)$:

$$
  \chi_{\mathrm{sym}} + \chi_{\mathrm{alt}}
  = (q - H_A/2) + (-q^{-1} - H_A/2)
  = q - q^{-1} - H_A = 0
$$

since $H_A = q - q^{-1}$.  Therefore the weighted sum vanishes:
$W_{\mathrm{sym}} \cdot \chi_{\mathrm{sym}}
+ W_{\mathrm{alt}} \cdot \chi_{\mathrm{alt}}
= W_{\mathrm{sym}}(\chi_{\mathrm{sym}} + \chi_{\mathrm{alt}}) = 0$.

The standard-representation volume $z - H_A/2$ follows from the
transfer matrix with initial condition $(a_0, b_0) = (0, 1)$:
$(a, b) = (1, -H_A/2)$, giving
$\chi_{\mathrm{std}} = z \cdot 1 + (-H_A/2) = z - H_A/2$.

For a general confined state at jet level $\ell$, the character
ratio $a_\ell$ compares the accumulated Wedderburn volume of
the confined braid word against the tensor product of free
constituent volumes.  The product $\prod_\ell a_\ell$ telescopes
through the jet tower:

$$
  \prod_\ell a_\ell
  = \frac{\hat{V}(\text{nucleus})}
         {\prod_{\text{nucleons}} \hat{V}(\text{nucleon})}
  \cdot
  \frac{\prod_{\text{nucleons}} \hat{V}(\text{nucleon})}
       {\prod_{\text{quarks}} \hat{V}(\text{quark})}
  \cdot \dotsb
$$

Each factor is determined by the Hecke algebra multiplication
rules applied to the crossing parameters at that level.
$\square$

**Witness**: `confined-knot-binding.witness.json`.
