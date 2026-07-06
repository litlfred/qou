Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$q$-deformed exterior derivative $d_q$
([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)).  The *$q$-Laplacian*
on $\Omega^k(A)$ is $\Delta_q = d_q\delta_q + \delta_qd_q$.
A **particle** is an element $\alpha \in \Omega^k(A)$ that is
$q$-harmonic:

```tex
\begin{equation}\label{eq:q-harmonic-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^{k-1}(A)
    \ar[r, "d_q"]
  & \Omega^k(A)
    \ar[r, "d_q"]
    \ar[d, "\delta_q"'{near start}, "{\scriptstyle \Delta_q \alpha = 0}"{description, near end}]
  & \Omega^{k+1}(A)
  \\
  & \Omega^{k-1}(A)
\end{tikzcd}
\end{equation}
```

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
