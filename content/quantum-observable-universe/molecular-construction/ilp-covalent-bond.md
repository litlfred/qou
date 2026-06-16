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

### Why knots, not links

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
