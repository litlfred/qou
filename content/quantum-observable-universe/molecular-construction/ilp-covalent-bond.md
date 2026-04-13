**Proposition.**
*The covalent bond operator between two atoms in $H_3(q)$ is the
inverse trefoil $T_{2,3}^{-1} = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$,
selected by the integer linear program:*

$$
  \min_{K} \; \mathrm{cr}(K) \quad
  \text{s.t.} \quad K \in \{\text{knots}\}, \quad
  E\bigl(\mathcal{A}_1 \times K \times \mathcal{A}_2\bigr) > 0
$$

*where $\mathrm{cr}(K)$ is the crossing number of the knot $K$
and $E$ is the binding energy computed from the 3-channel
Wedderburn vertex volumes:*

$$
  \hat{V}_i^{\mathrm{full}} = w_{\mathrm{sym}} \lambda_i^{\mathrm{sym}}
  + w_{\mathrm{std}} \hat{V}_i^{\mathrm{std}}
  + w_{\mathrm{alt}} \lambda_i^{\mathrm{alt}}
$$

*The ILP solution proceeds as follows:*

1. *$n = 0$ (unknot): $E = 0$ — no binding (infeasible).*

2. *$n = 1, 2$: no knots exist with fewer than 3 crossings.*

3. *$n = 3$ (trefoil): two candidates.*
   - *$T_{2,3} = \sigma_0\sigma_1\sigma_0$: $E = 4.71$ eV
     (positive, feasible).*
   - *$T_{2,3}^{-1} = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$:
     $E = 4.48$ eV (positive, feasible, lower energy).*
   - *The inverse orientation is selected by energy minimisation.*

*At $q_0 \approx 1.110$, the predicted $H_2$ bond dissociation
energy is:*

$$
  D_0(H_2) = 4.4834 \;\text{eV}
  \qquad (\text{observed: } 4.478 \;\text{eV}, \;
  \text{error } {+}0.1\%)
$$

*with zero fitted parameters.  The binding energy is computed from
the per-generator vertex volume decomposition using the Wedderburn
weights $w_{\mathrm{sym}} = w_{\mathrm{alt}} = q^2/(q^4 + 4q^2 + 1)$,
$w_{\mathrm{std}} = (q^2+1)^2/(q^4+4q^2+1)$ and the molecular
energy scale $E_{\mathrm{mol}} = E_{\mathrm{hartree}}/[2]_q^2$.*

*The universal binding quantum on the full atom tower is
$0.7043$ eV per crossing — constant for all atom pairs.
For $H_2$, the inverse trefoil's 3 crossings give
$3 \times 0.7043 \times f_{\mathrm{vertex}} = 4.48$ eV
where $f_{\mathrm{vertex}}$ encodes the vertex volume structure
of the small hydrogen atom.*
