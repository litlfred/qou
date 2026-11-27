Morita defines the Hahn--Exton $q$-Bessel function as
$$
J^{(3)}_\nu(x; q) = \frac{(q^{\nu+1}; q)_\infty}{(q; q)_\infty}\, x^\nu\, {}_1\varphi_1\big(0; q^{\nu+1}; q, q x^2\big)
$$
\cite[\S 1, p. 1]{morita2011}. Working with $0 < |q| < 1$ and $q = p^2$, he uses the $q$-Borel and $q$-Laplace transformations of Zhang to write the solution of the Hahn--Exton equation at infinity as a $\theta_p$-weighted combination of two ${}_1\varphi_1$ series in base $p$, valid for $x \notin [p^{\nu+2}; p]$ \cite[Theorem 1, eq. (4), p. 3]{morita2011}. In the limit $p \to 1^-$ the formula becomes the classical expression of the Hankel function $H^{(2)}_\nu$ through $J_\nu$ and $J_{-\nu}$ \cite[\S 1, p. 3]{morita2011}.

The normalisation agrees with the one used in the [second-order $q$-difference proof](#prf:q-bessel-second-order-qdifference). The coefficient of $(q x^2)^k$ in Morita's ${}_1\varphi_1$ is
$$
\frac{(-1)^k\, q^{k(k-1)/2}}{(q; q)_k\, (q^{\nu+1}; q)_k} = c_k,
$$
so $J^{(3)}_\nu(x; q) = \frac{(q^{\nu+1}; q)_\infty}{(q; q)_\infty}\, x^\nu\, g(q x^2)$, with $g$ the corpus's generating function of the $c_k$. This is the precondition for citing the connection formula alongside the [$c_k$ recursion](#prop:q-beta-c-k-recursion-from-habiro-q-difference): both work with the same series.

What it does not supply: the connection formula is proved for $0 < |q| < 1$, while the corpus evaluates at an aether parameter greater than one, so using it there needs $q$ replaced by $q^{-1}$ and the formula rederived. And the $p \to 1^-$ limit recovers the classical Bessel connection; it says nothing about the $c_k$ beyond the $q$-Bessel series itself.
