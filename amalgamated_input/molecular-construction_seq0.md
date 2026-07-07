<!-- FILE_START: molecular-hecke-algebra-intro.md -->
We extend the atomic constructor of Chapter 11 to multi-atom systems. The molecular braid $H_{N_{\mathrm{mol}}}(q)$ (def) joins pre-computed atomic braids inside a single Hecke algebra, and the inter-atomic crossing coefficients (rem) record how strands from different nuclei interact. Two atoms share a single electron trefoil to form a covalent bond as shared electron trefoil (def), and the ILP characterisation of the covalent bond (prop) identifies that shared trefoil as the inverse trefoil $T_{2,3}^{-1}$ — the minimum-crossing knot operator with positive binding energy. With these four objects in hand we can compute any molecule by Hopf-linking atoms.

_(draft.)_
<!-- FILE_END: molecular-hecke-algebra-intro.md -->

<!-- FILE_START: molecular-braid.md -->
**Definition.**
*Let $\mathcal{A}_1, \ldots, \mathcal{A}_k$ be pre-computed
[atomic braids](#def:atomic-braid) with strand counts
$n_i = A_i + Z_i$.  The **molecular braid** is the element*

$$
  \mathcal{M}(A_1, \ldots, A_k; \mathcal{B})
  \;\in\; H_{N_{\mathrm{mol}}}(q),
  \qquad
  N_{\mathrm{mol}} = \sum_{i=1}^{k} n_i
$$

*constructed iteratively as follows:*

1. **Atomic assembly.**  Embed each atomic braid
   $\mathcal{A}_i \in H_{n_i}(q)$ into
   $H_{N_{\mathrm{mol}}}(q)$ using the standard inclusion
   $\iota_i \colon H_{n_i}(q) \hookrightarrow H_{N_{\mathrm{mol}}}(q)$
   that maps $\sigma_j \mapsto \sigma_{j + \sum_{l < i} n_l}$.

2. **Inter-atomic crossings.**  For each pair of atoms
   $(i, j)$ with $i < j$, apply the inter-atomic crossing
   operators determined by the [molecular crossing table](#rem:molecular-crossing-table):
   $$
     C_{\mathrm{mol}}(\mathcal{A}_i, \mathcal{A}_j)
     = \prod_{(s, t) \in \mathrm{pairs}(i,j)} T_{st}
   $$
   where $(s, t)$ ranges over all strand pairs between atoms
   $i$ and $j$.

3. **Shared-electron Hopf linking.**  For each covalent bond
   $b \in \mathcal{B}$ connecting atoms $i$ and $j$ with bond
   order $k_b$, select $k_b$ electron trefoils from atom $i$
   and Hopf-link them to atom $j$:
   $$
     L_b = \prod_{e=1}^{k_b} \sigma_{g_e}^{-1}
   $$
   where $g_e$ is the generator index mediating electron $e$
   between the two nuclei.

4. **Iterative reduction.**  After each assembly step, apply
   [Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)
   to normal form before proceeding to the next step.

*The molecular braid satisfies
$\mathcal{M} = \mathrm{NF}\bigl(\prod_i \iota_i(\mathcal{A}_i) \cdot
\prod_{i<j} C_{\mathrm{mol}} \cdot \prod_b L_b\bigr)$.*

*The binding energy of the molecule relative to its constituent
atoms is*

$$
  \mathfrak{E}_{\mathrm{bind}} = \alpha \left(
    \sum_{i=1}^{k} \Phi_1(\mathcal{A}_i)
    - \Phi_1(\mathcal{M})
  \right)
$$

*where $\alpha = m_e \times 8G$ is the same binding scale as in
the [atomic mass formula](#thm:wedderburn-mass-formula).  Positive
$\mathfrak{E}_{\mathrm{bind}}$ means the molecule is bound.*
<!-- FILE_END: molecular-braid.md -->

<!-- FILE_START: covalent-bond-shared-trefoil.md -->
**Definition.**
*A **covalent bond of order $k$** between atoms $i$ and $j$ is the
Hopf linking of $k$ electron trefoils across the two nuclei.
Specifically, let $e_1, \ldots, e_k$ be electrons from atom $i$
(or shared between $i$ and $j$).  Each electron is a trefoil
$T_{2,3} = \sigma_0\sigma_1\sigma_0$ in its local $H_3(q)$.*

*In the [molecular braid](#def:molecular-braid), the covalent bond
operator for bond $b$ connecting atoms $i$ and $j$ is:*

$$
  L_b = \prod_{e=1}^{k_b}
  \sigma_{g_e(\mathfrak{p}_j)}^{-1} \cdot
  \sigma_{g_e(\mathfrak{p}_i)}^{-1}
$$

*where $g_e(\mathfrak{p}_j)$ is the generator index for the
crossing between shared electron $e$ and proton $\mathfrak{p}_j$
of atom $j$, and $g_e(\mathfrak{p}_i)$ for proton
$\mathfrak{p}_i$ of atom $i$.  Both crossings are $\sigma^{-1}$
(EM attraction), so each shared electron contributes **two
attractive crossings** — one to each nucleus.*
<!-- FILE_END: covalent-bond-shared-trefoil.md -->

<!-- FILE_START: covalent-bond-order-and-lp-selection.md -->
*The key distinction from a lone electron (bound to a single
nucleus):*

| | Lone electron | Shared electron (covalent) |
|:---|:---|:---|
| Crossings | $\sigma^{-1}_{g(\mathfrak{p}_i)}$ (1 attractive) | $\sigma^{-1}_{g(\mathfrak{p}_i)} \cdot \sigma^{-1}_{g(\mathfrak{p}_j)}$ (2 attractive) |
| Transfer matrix | $T_{\mathfrak{p}e}$ (single) | $T_{\mathfrak{p}_ie} \cdot T_{\mathfrak{p}_je}$ (product) |
| $\Phi_1$ contribution | $\ln\lvert V_e\rvert$ | $\ln\lvert V_{e,i}\rvert + \ln\lvert V_{e,j}\rvert$ |

*A bond of order $k$ contributes $2k$ attractive crossings.  The
LP dual finds the optimal assignment of electrons to bonding
positions by minimizing the total $\Phi_1$.*

*Bond orders:*
- *$k = 1$: single bond (H--H, C--H, C--C) — 1 shared pair*
- *$k = 2$: double bond (C=O, C=C) — 2 shared pairs*
- *$k = 3$: triple bond (C$\equiv$O, N$\equiv$N) — 3 shared pairs*
<!-- FILE_END: covalent-bond-order-and-lp-selection.md -->

<!-- FILE_START: ilp-covalent-bond.md -->
**Proposition.**
*The covalent bond operator is selected by the
[universal ILP](#def:universal-ilp-algorithm) — the same LP
that derives confinement ($\mathcal{B}_3$) and the gluon ($2\sigma_0$).*

$$
  \min_{K} \; \mathrm{cr}(K) \quad
  \text{s.t.} \quad K \in \{\text{knots}\}, \quad
  G \cdot \mathrm{NF}(x \cdot K) \geq 0, \quad
  \mathrm{tr}_M(x \cdot K) \leq \mathrm{tr}_M(x)
$$

*For the hydrogen atom ($x = \mathrm{NF}(H)$, Frobenius-stable),
the unknot gives equality ($\mathrm{tr}_M$ unchanged).  The LP
selects the minimum-crossing knot that strictly decreases the
trace:*

| Knot | Crossings | $\mathrm{tr}_M(H \cdot K \cdot H)$ | $\mathfrak{E}_{\mathrm{bind}}$ |
|:-----|:----------|:----------------------------------|:-------------------|
| Unknot | 0 | $0.182$ | $0$ eV |
| **Inverse trefoil** $T_{2,3}^{-1}$ | **3** | **$0.062$** | **$4.48$ eV** |
| Trefoil $T_{2,3}$ | 3 | $0.442$ | $4.71$ eV |
| Figure-eight $4_1$ | 4 | repulsive | — |

*The inverse trefoil $T_{2,3}^{-1} = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$
is the unique LP solution: the minimum-crossing knot satisfying
both Frobenius positivity and non-increasing trace.*

### Knots, not links

*The dual space of the LP is the **knot operator space** — single-component
braid closures.  Links (multi-component closures such as the Hopf link
$(σ_1^{-1})^2$) are excluded because:*

1. *The covalent bond is a single topological structure mediating
   the interaction — not two separate loops.*
2. *The Hopf link gives repulsive or weak binding on the vertex
   volume model ($-0.82$ eV for $H_2$).*
3. *The knot constraint is the molecular analogue of the Borromean
   constraint for quarks: inseparability of the bonded system.*

### Consistency across levels

*The LP that selects the inverse trefoil for molecular binding is
identical to the LP that selects $\mathcal{B}_3$ for quark confinement.
Both solve the same program with the same Gram matrix $G$, the same
Frobenius constraint, and the same trace objective.  The only input
that changes is the state $x$:*

- *Quarks (unstable): $x = \mathrm{NF}(\text{uud})$, $Gx[\gamma] < 0$
  $\Rightarrow$ LP forces non-trivial knot $\Rightarrow$ $\mathcal{B}_3$.*
- *H atom (stable): $x = \mathrm{NF}(H)$, $Gx \geq 0$
  $\Rightarrow$ unknot is feasible but gives zero binding
  $\Rightarrow$ LP selects inverse trefoil.*

### Binding energy

*On the 2-generator vertex volume model with 3-channel Wedderburn
weights $(w_s, w_d, w_a) = (q^2, (q^2+1)^2, q^2)/(q^4+4q^2+1)$:*

$$
  D_0(H_2) = 4.4834 \;\text{eV}
  \qquad (\text{observed: } :val[d0_h2_ev]{precision=4, witness=computations/molecular-experimental-refs.witness.json} \;\text{eV}, \;
  {+}0.1\%)
$$

*On the NF multiplication method:*

$$
  D_0(C\text{-}C) = 3.21 \;\text{eV}
  \qquad (\text{observed: } :val[d0_cc_ev]{precision=3, witness=computations/molecular-experimental-refs.witness.json} \;\text{eV}, \;
  {-}10.9\%)
$$

*Zero fitted parameters.  The binding energy scale
$E_{\mathrm{mol}} = E_{\mathrm{hartree}}/[2]_q^2 = m_e \alpha_{\mathrm{EM}}^2/(q+q^{-1})^2$
is derived from $q_0$ alone.*
<!-- FILE_END: ilp-covalent-bond.md -->

