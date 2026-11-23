**Proposition (torus-knot $\alpha_{\mathrm{shift}}$).**
*Let $p \geq 1$, $k \geq 1$ with $\gcd(p, k) = 1$, and let
$T_{p,k}$ be the $(p, k)$-torus knot, presented as the closure
of the braid $\beta_{p,k} = (\sigma_1 \sigma_2 \cdots
\sigma_{p-1})^k \in B_p$. Define the **shift exponent** of the braid $\beta_{p,k}$*

$$
  \alpha_{\mathrm{shift}}(\beta_{p,k})
  \;:=\;
  \max_{\lambda \,\vdash\, p}\;
  \mathrm{ord}_{q=0}^{(-)}\; \chi_\lambda(\beta_{p,k})
$$

*where $\chi_\lambda$ is the seminormal Hecke character on
$V_\lambda$ ([$q$-dimension decoration $\delta_q$](#def:delta-q-decoration))
and $\mathrm{ord}_{q=0}^{(-)}$ denotes the pole order at $q = 0$
(i.e. the negative of the Laurent valuation). Then:*

1. *The channel $V_{(1^p)}$ has pole order exactly $k(p-1)$.*
2. *For $(p, k) \in \{(2,3), (2,5), (2,9), (3,4), (3,5), (3,7)\}$ this channel is the maximizer, so $\alpha_{\mathrm{shift}}(\beta_{p,k}) = k(p - 1)$ for those pairs. For general $(p, k)$ maximality is conjectural.*

*$\alpha_{\mathrm{shift}}$ is an invariant of the braid $\beta_{p,k}$, not of the knot $T_{p,k}$: since $T_{p,k} \cong T_{k,p}$, the two braid presentations give $k(p-1)$ and $p(k-1)$, which differ when $p \neq k$ (for the trefoil, $3$ from $\beta_{2,3}$ and $4$ from $\beta_{3,2}$). We keep the notation $\alpha_{\mathrm{shift}}(T_{p,k})$ elsewhere only as shorthand for $\alpha_{\mathrm{shift}}(\beta_{p,k})$ with $p$ the braid index.*
### Witness summary

The canonical evidence
records the full per-irrep symbolic $\chi_\lambda \in \mathbb{Q}(q)$
together with the pole order at $q = 0$ for every test pair, summarised
in
[Table: $\alpha_{\mathrm{shift}}(T_{p,k})$ for 6 test pairs](#tbl:alpha-shift-torus-knot-table-data).
All $14$ assertions in the witness pass.

