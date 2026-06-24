By [prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price),
the BW coefficient of partition $\lambda$ is the LP-dual variable
$u_\lambda^* = C_\lambda \cdot S_\lambda(Z, N, A)$.  The
categorical scale $C_\lambda = m_e \cdot H_q(\lambda)$ (the
$q$-hook product over the Young diagram of $\lambda$) is the
universal constant determined by the partition algebra, with no
nuclear data; the scaling function $S_\lambda(Z, N, A)$ is
realised at each step as $\ln|\mathrm{tr}\,\mathbf{M}_\lambda^{(0..A)}| -
\ln d_\lambda$ via the Young seminormal representation.

For $\lambda = (2,2) \vdash 4$ this recovers the dedicated Wigner
identity ([prop:wigner-np-pairing](#prop:wigner-np-pairing)):
$H_q((2,2)) = [3]_q \cdot [2]_q^2$; for $\lambda = (2,1) \vdash 3$
it reproduces the volume / surface / Coulomb decomposition
through their image under the Wedderburn embedding; for higher
partitions it adds the form-factor, $pn$-correlation, and
${[3,2,1]}$ pn-invisible corrections.

By the Wedderburn-Artin trace identity
$\sum_\lambda \dim_q(\lambda)^2 = [k]_q!$ ($k$ fixed), the dual
shadow prices satisfy a single budget constraint per Hecke
level; by Frobenius reciprocity
([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price),
branching corollary), shadow prices at level $k+1$ are
determined by those at level $k$.  Telescoping per-step log-trace
differences across $k = 1, \ldots, A$ yields the closed-form
$B_\lambda$.

The Kerov $q$-hook walk \cite{kerov1996} gives the iterative
Markov-chain interpretation of $\mathrm{tr}\,\mathbf{M}_\lambda^{(0..k)}$
as a transition kernel on the Young lattice; the
Féray–Méliot $q$-Plancherel CLT \cite{feray-meliot2012}
guarantees the asymptotic convergence of the accumulator at
rate $O(1/\sqrt{A})$ across Hecke levels.

The three legacy mechanisms specialise:
- *deuteron ($A = 2$, dedicated $\alpha_{\mathrm{Borromean}}
  \cdot \hat V_e$):* the $A = 2$ slice of the LP-dual
  accumulator, dominated by the $(2,1)$ and $(2,2)$ shadow
  prices;
- *knot factor ($A = 3, 4$, dedicated $a(N) = 1 - h^2,
  (1 - h^2)^2$):* the $A = 3, 4$ slices of the LP-dual
  accumulator, where the $(2,1)$ and $(3,1)$ contributions
  reproduce the figure-eight and Borromean amphicheiral factors;
- *Wigner energy ($k \geq 5$, dedicated
  $-\Delta_W \cdot T(T+1)/A$):* the $k = 4, 5$ self-conjugate
  shadow prices ($\lambda = (2,2)$ and $(3,1,1)$), which
  vanish on isolated $pn$ crossings (extremal cancellation,
  [prop:confined-knot-binding](#prop:confined-knot-binding))
  but are nonzero on collective $pn$ patterns.
$\qquad\blacksquare$
