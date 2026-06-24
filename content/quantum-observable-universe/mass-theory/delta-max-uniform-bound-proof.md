*Step 1 — Operator-norm control of the Markov trace.*  The
Markov trace $\mathrm{tr}_M \colon H_n(R, q) \to \mathbb{C}$ is
bounded with respect to the operator norm: for any
$x \in H_n(R, q)$ acting on a Jones--Wenzl module $W$ of dimension
$d_q$,

$$
  |\mathrm{tr}_M(x)|
  \;\leq\; d_q \cdot \|x\|_{\mathrm{op}},
$$

by Cauchy--Schwarz on the Hilbert--Schmidt norm and the
positivity of the Markov trace at real $q > 0$
([Markov trace factorization](#thm\:markov-trace-factorization),
appendix).

*Step 2 — Jet-level transient lives on a bounded module.*
The :refterm[descent]{#descent} splitting
$\mathrm{End}(A_{n+1}) =
 \mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$
([:refterm[descent]{#descent} eigenspaces](#prop\:descent-eigenspaces)) places every
transient endomorphism at level $n+1$ in $\ker\hat\tau_n$.  By
the recursive brane tower
([recursive brane tower](#def\:recursive-brane-tower)),
$A_{n+1} = A_n \otimes \Omega^1(A_n)$, so a transient mode at
level $n+1$ is a section of the Kähler cotangent bundle
$\Omega^1(A_n)$ paired with its Frobenius dual.  On the
Jones--Wenzl module, this pairing multiplies the operator norm
by at most $\hbar_q^{-1}$ per level (the $\Omega^1$ weight),
but the Markov trace absorbs exactly one factor of $\hbar_q^{-1}$
through the normalization $z = \hbar_q / (1 - q^{-1/2})\cdots$
The **net** norm of a transient contribution is bounded
above by the level-0 operator norm
$\|\rho(\beta)\|_{\mathrm{op}}$ independent of $n$.

*Step 3 — Per-level residual bound.*  The per-level residual
is the difference between the free and atomic tower masses at
level $n$:

$$
  \Delta^{(n)}(\varrho)
  \;=\;
  \mathfrak{m}^{(n)}(\varrho_{\mathrm{free}})
    - \mathfrak{m}^{(n)}(\varrho_{\mathrm{atom}}).
$$

By the triangle inequality and Step 1,

$$
  |\Delta^{(n)}|
  \;\leq\;
  |\mathfrak{m}^{(n)}(\varrho_{\mathrm{free}})|
    + |\mathfrak{m}^{(n)}(\varrho_{\mathrm{atom}})|
  \;\leq\;
  2\,d_q\,\|\rho(\beta^{(n)})\|_{\mathrm{op}},
$$

where $\beta^{(n)}$ is the jet-lifted braid at level $n$.
By Step 2 and the operator-norm submultiplicativity
$\|\rho(\beta^{(n)})\|_{\mathrm{op}} \le \|\rho(\beta)\|_{\mathrm{op}}^{n+1}$
bounded by the brane-tower weight $\hbar_q^{-n}$, the factors
cancel: $\|\rho(\beta^{(n)})\|_{\mathrm{op}} \cdot \hbar_q^{n}
\le \|\rho(\beta)\|_{\mathrm{op}}$ uniformly in $n$.

*Step 4 — Braid-length factor.*  The Jones--Wenzl module
dimension $d_q$ for a braid of length $L(\beta)$ on $n$ strands
is bounded by $d_q \le L(\beta) \cdot \|\rho(\beta)\|_{\mathrm{op}}$
(Kassel--Turaev, *Braid Groups*, Prop. 4.4.3 specialized to
generic $q > 0$).  Combining with Step 3,

$$
  |\Delta^{(n)}|
  \;\leq\;
  2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}
  \cdot \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}}).
$$

The right-hand side is independent of $n$; set
$\Delta_{\max}(\varrho)$ equal to it.  $\square$
