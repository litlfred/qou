By the [MI--SW abelianisation](#prop:mi-sw-abelianisation), the $n$-th prolonged
Seiberg--Witten differential $\lambda_{\mathrm{SW}}^{(n)}$ is the Cartan
component of the abelianised connection on the exceptional divisor
$\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$. As a connection $1$-form on a
genus-zero curve it is meromorphic, with poles confined to the branch points
$z_c$ (the only points where the prolonged connection degenerates).

$\mathcal{S}_c$ is compact, so $\lambda_{\mathrm{SW}}^{(n)}$ has finitely many
poles $p_1,\dots,p_k$, all at branch points. For a cycle $\gamma$ bounding a
region whose poles are $E \subseteq \{p_1,\dots,p_k\}$, the residue theorem gives

$$
\oint_{\gamma}\lambda_{\mathrm{SW}}^{(n)}
\;=\;
2\pi i \sum_{p_j\,\in\,E}\mathrm{Res}_{p_j}\,\lambda_{\mathrm{SW}}^{(n)},
$$

the right-hand side being a finite sum of local residues. Identifying the
left-hand side with the prolonged period $a_D^{(n)}$ of
[Abelianisation of the MI integral on exceptional divisors](#prop:mi-sw-abelianisation) gives the residue-sum
shape: the period is computed by collecting residues, with no contour
integration — *once $E$ is known*.

**Scope.** The argument cannot run over all $k$ poles, nor appeal to a period
over a generating cycle of $\mathcal{S}_c$. $\mathbb{P}^1(\mathbb{C})$ has
$H_1 = 0$, so there is no generating cycle; and the residue theorem on a compact
Riemann surface states that the residues over *all* poles **sum to zero**, which
would give $a_D^{(n)} = 0$ at every level rather than the positive binding period
the keystone requires. This vanishing is a derived consequence rather than a
claim, and its contrapositive — a nonzero period forces a nonzero total
residue — is what forces $E$ to be a *proper* subset. The companion statement
[The Seiberg–Witten period is an algebraic residue sum](#prop:sw-period-residue-sum) carries the
residue-sum shape as an explicit hypothesis; it does not derive it.
$\qquad\blacksquare$
