*The discrete color symmetry $\mathrm{PSL}(2,7)$ arises from the octonionic
automorphism group $G_2$ via the Fano plane, whose incidence structure
encodes the octonion multiplication table.  The bridge group
$S_4 \subset S_5 \cap \mathrm{PSL}(2,7)$ carries the local Fano data
from the Bring surface to the Klein quartic.*

**The $S_4$ bridge mechanism.**
The Bring surface $\Sigma_4$ (genus 4) has automorphism group $S_5$.
The Klein quartic $\Sigma_3$ (genus 3) has automorphism group
$\mathrm{PSL}(2,7)$ of order $168 = 84(3-1)$, the Hurwitz bound.
The group $S_4$ is the maximal common subgroup:

\begin{enumerate}
\item $S_4 \subset S_5$ as the stabilizer of one letter (index 5).
\item $S_4 \cong \mathrm{Stab}(\mathrm{pt})$ in $\mathrm{PSL}(2,7)$
  acting on the 7 Fano points (index 7).
\end{enumerate}

The point stabilizer $S_4$ preserves the \emph{local Fano structure}
at the fixed point: the 3 lines through that point, encoding the 3
octonion multiplication triples involving the corresponding imaginary
unit.  Computationally verified
(\texttt{s4\_fano\_action.py}):
\begin{itemize}
\item $S_4$ acts transitively on the 3 lines through the fixed point,
\item $S_4$ acts transitively on the 4 lines not through the fixed point,
\item $S_4$ acts transitively on the 6 remaining Fano points,
\item the 3 local lines partition the 6 remaining points into 3 pairs.
\end{itemize}

**Conjectured genus degeneration.**
The derivation chain from Bring to Fano is:
$$
  \underbrace{\Sigma_4}_{g=4,\; S_5}
  \;\xrightarrow{\text{pinch}}\;
  \underbrace{\Sigma_3^{\mathrm{nod}}}_{g_{\mathrm{arith}}=4,\; S_4}
  \;\xrightarrow{\text{normalize}}\;
  \underbrace{\Sigma_3}_{g=3,\; \mathrm{PSL}(2,7)}
$$
Pinching an $S_4$-invariant 1-cycle on $\Sigma_4$ produces a nodal curve
of arithmetic genus 4 but geometric genus 3.  The $S_4$ symmetry
survives the pinch (it fixes the vanishing cycle).  On the
normalization $\Sigma_3$ of genus 3, the Hurwitz bound forces the
automorphism group to be at most $\mathrm{PSL}(2,7)$, and since $S_4$
embeds in $\mathrm{PSL}(2,7)$ as a point stabilizer, the enhancement
$S_4 \hookrightarrow \mathrm{PSL}(2,7)$ is the unique maximal option.

\textbf{Status:} the $S_4$ bridge mechanism is computationally verified
(\texttt{s4\_bridge\_verification.py}, \texttt{s4\_fano\_action.py}).
The genus degeneration step is a conjecture: whether pinching an
$S_4$-invariant cycle on Bring actually produces the Klein quartic
(rather than some other genus-3 curve) requires an algebraic-geometry
argument not yet provided.

**$\mathrm{PSL}(2,7)$ representation theory.**
Computationally verified (\texttt{psl27\_irrep\_verification.py}):
the group $\mathrm{PSL}(2,7) \cong \mathrm{GL}(3, \mathbb{F}_2)$ has
6 conjugacy classes and 6 irreducible representations of dimensions
\begin{equation}\label{eq:psl27-irreps}
  \{1, 3, \bar{3}, 6, 7, 8\},
  \qquad
  \sum d_i^2 = 1 + 9 + 9 + 36 + 49 + 64 = 168 = |\mathrm{PSL}(2,7)|.
\end{equation}
The physical interpretation:
\begin{center}
\begin{tabular}{c l l}
\hline
$\dim$ & Representation & Physical role \\
\hline
$1$       & trivial         & singlet \\
$3$       & fundamental     & color triplet ($q$) \\
$\bar{3}$ & conjugate       & color antitriplet ($\bar{q}$) \\
$6$       & $\mathrm{Sym}^2(\mathbf{3})$ & no singlet $\Rightarrow$ complex type \\
$7$       & natural on $\mathrm{Im}(\mathbb{O})$ & imaginary octonions \\
$8$       & adjoint of $\mathrm{SU}(3)$ & gluon octet \\
\hline
\end{tabular}
\end{center}
The 3 and $\bar{3}$ are complex conjugate (not self-dual), matching
the Günaydin--Gürsey decomposition
$\mathrm{Im}(\mathbb{O}) \cong \mathbb{R} \oplus \mathbb{C}^3$
under $\mathrm{SU}(3) \subset G_2$.
