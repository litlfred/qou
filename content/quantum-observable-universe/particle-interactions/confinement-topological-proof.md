The eigenvalues of $G$ are (symbolically in $q$):

$$
  \mathrm{spec}(G)
  =
  \{
    \lambda_+(q),\;
    \lambda_+(q),\;
    \lambda_+(q),\;
    \lambda_{\max}(q),\;
    \lambda_0(q),\;
    \lambda_-(q)
  \}
$$

where $\lambda_-(q) < 0$ for all $q > 1$.  At $q_0$:
$\lambda_- \approx -0.855$.

The LP exploits this: the direction $v_-$ (eigenvector of
$\lambda_-$) satisfies $t \cdot v_- < 0$ while $Gv_- \geq 0$
in certain components.  Moving along $v_-$ decreases the
objective without violating Frobenius positivity.
