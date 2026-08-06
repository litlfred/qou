*The $q$-deformation lifts the mass degeneracy of the meson octet.
The eight states share the same hexagonal weight pattern but their
masses split through the quantum dimension and crossing-energy
formulas of the Hecke algebra.*

The meson octet decomposition ($\mathbf{3} \otimes \bar{\mathbf{3}} =
\mathbf{8} \oplus \mathbf{1}$) determines \emph{which} states exist.
The mass splitting of these states is a separate, $q$-dependent
phenomenon governed by the Markov trace and the crossing energy.

**$q$-independent structure.**
The weight lattice and the state assignments (which meson sits at
which $(I_3, Y)$) are $q$-independent
(Proposition~\ref{prop:q-deformation-weight-lattice}).
The hexagonal pattern itself --- $\pi^\pm$ at $(\pm 1, 0)$,
$K^\pm$ at $(\pm 1/2, \pm 1)$, $\pi^0$ and $\eta$ at the origin
--- is determined entirely by the Cartan matrix $A_2$, which the
Hecke relation encodes independently of $q$.

**$q$-dependent dynamics.**
Within the hexagonal pattern, the physical masses are governed by
three $q$-dependent ingredients:
\begin{enumerate}
\item \textbf{Quantum dimensions:} $\dim_q(V_\lambda) = \prod_{\alpha > 0}
  [\langle \lambda + \rho, \alpha^\vee \rangle]_q /
  [\langle \rho, \alpha^\vee \rangle]_q$.
  At $q = 1$ these reduce to the classical dimensions (all integer);
  at $q \neq 1$ they split.
\item \textbf{Crossing energy:}
  $\mathfrak{E}_\times(q) = \tfrac{1}{2}(q - q^{-1})$, the
  energy cost per crossing in the Hecke algebra.  This governs
  the mass contribution from each braid crossing in the meson's
  knot representative.
\item \textbf{Markov trace weights:}
  $\tau_q(\beta)$ assigns a $q$-dependent amplitude to each braid
  $\beta$, producing the mass endomorphism via the Frobenius
  integral.
\end{enumerate}

**The Gell-Mann--Okubo mass formula.**
In standard SU(3) flavour physics, the meson masses obey the
Gell-Mann--Okubo relation
$$
  4 m_K^2 = 3 m_\eta^2 + m_\pi^2.
$$
Within QOU this relation is \emph{not} derived.  The conjecture on offer
is that it should follow from the crossing-energy splitting pattern on
the $A_2$ weight lattice, the kaon involving a strange-quark braid word
of different writhe than the pion; but no such derivation exists, and the
one numerical cross-check run so far does not support it.  Measured
against experiment the Gell-Mann--Okubo relation is satisfied to
$\approx 6\%$, whereas the $q$-deformation of the adjoint quantum
dimension at $q_0 \approx 1.11$ is $\approx 3.3\%$
(\texttt{gmo\_meson\_crosscheck.py}).  Same order of magnitude, factor
$\approx 2$ apart, with no mechanism connecting the two numbers.  This is
an unexplained coincidence of scale, recorded as such; it is neither a
derivation nor evidence for one, and it must not be cited as agreement.

**Conditional on $N = 3$ and on $Y$.**
Mass splittings between isospin multiplets (e.g.\ $\pi$ vs.\ $K$)
depend on the hypercharge $Y$, which is open
(\S\ref{sec:flavor-representations}).  Within an isospin multiplet
(e.g.\ $K^+$ vs.\ $K^0$), the splitting is purely electromagnetic
and arises from the writhe difference, which is derived.
