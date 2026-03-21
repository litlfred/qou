Let $(M, \theta, G, P, E)$ be an archimedean quantum observable universe
with instanton connection $A$ ([Example](#ex:instanton)) and substrate
parameter $q$ ([Definition](#def:substrate-parameter)).  Let
$\mathbf{E}$ denote the Euler--Lagrange operator of the
$q$-weighted Yang--Mills--Levi functional $S_q$
([Definition](#def:q-yang-mills-levi)), and let $\nabla^A$ denote
parallel transport along $A$.  The following diagram commutes:

```tex
\[
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  J^1E
    \ar[r, "{\mathbf{E}[S_q]}"]
    \ar[d, "\text{jet evaluation}"']
  & \bigl\{ L_\theta : \mathrm{Ric}_{g_\theta} = T^{(q)} \bigr\}
    \ar[d, "{q = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert}"]
  \\
  \Gamma(E_{\mathrm{lin}})
    \ar[r, "\nabla^A"']
  & \bigl\{ \psi : J\hbar_q\,\iota_{\xi_q}D_A\psi = \hat{H}_q\psi \bigr\}
\end{tikzcd}
\]
```

where the top row sends a jet (a first-order perturbation of the gauge field)
to the Einstein-type field equation via the Euler--Lagrange operator; the
left column evaluates a jet at a fibre point to produce a linearised section;
the right column is the coupling through the substrate field $q$; and the
bottom row is the parallel-transport equation whose linearisation is the
Schrödinger equation.

---

**Proof sketch.**
The top row is the variational equation $\delta S_q / \delta L_\theta = 0$,
which involves $q(p)$ through the functional $S_q$.  The bottom row is the
$q$-deformed parallel-transport equation
$J\hbar_q\,\iota_{\xi_q}D_A\psi = \hat{H}_q\psi$,
linearised at a chosen section.
The left column is the jet evaluation map
$j^1_p \sigma \mapsto \sigma(p)$ restricted to $E_{\mathrm{lin}}$.
Commutativity amounts to the statement that solving the variational
equation for $L_\theta$ and then substituting $q(p)$ into the transport
equation gives the same solution set $\psi$ as first evaluating the jet
and then transporting along $A$.  This follows from the chain rule:
$\mathbf{E}[S_q]$ determines $L_\theta$ (and hence $q$), which in turn
determines $\hat{H}_q$ and $\xi_q$ appearing in the transport equation.
