By the [MI--SW abelianisation](#prop:mi-sw-abelianisation), the $n$-th prolonged
Seiberg--Witten differential $\lambda_{\mathrm{SW}}^{(n)}$ is the Cartan
component of the abelianised connection on the exceptional divisor
$\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$. As a connection $1$-form on a
genus-zero curve it is meromorphic, with poles confined to the branch points
$z_c$ (the only points where the prolonged connection degenerates).

$\mathcal{S}_c$ is compact, so $\lambda_{\mathrm{SW}}^{(n)}$ has finitely many
poles $p_1,\dots,p_k$, all at branch points. The residue theorem on a compact
Riemann surface gives, for the period over the generating cycle of
$\mathcal{S}_c$,

$$
\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}
\;=\;
2\pi i \sum_{j=1}^{k}\operatorname{Res}_{p_j}\,\lambda_{\mathrm{SW}}^{(n)},
$$

the right-hand side being a finite sum of local residues. Identifying the
left-hand side with the prolonged period $a_D^{(n)}$ of
[`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation) yields the claim: the
period is computed by collecting residues at the branch-point poles, with no
contour integration. The Lean witness
[`QOU.Brings.sw_period_eq_residue_sum`](#prop:sw-period-residue-sum) packages the
meromorphy-with-given-residues data as a hypothesis and extracts the residue-sum
identity. $\qquad\blacksquare$
