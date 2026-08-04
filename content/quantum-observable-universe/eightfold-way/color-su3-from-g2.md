*The color gauge group $\mathrm{SU}(3)_c$ arises as the stabilizer
subgroup of the octonion automorphism group $G_2 = \mathrm{Aut}(\mathbb{O})$.*

The octonion algebra $\mathbb{O}$ is the unique $8$-dimensional real
division algebra.  Its automorphism group $G_2$ is the $14$-dimensional
exceptional simple Lie group.  Fixing an imaginary unit $e \in
\mathrm{Im}(\mathbb{O})$ breaks $G_2$ to the stabilizer
$\mathrm{Stab}_{G_2}(e) \cong \mathrm{SU}(3)$, and the imaginary
octonions decompose under this $\mathrm{SU}(3)$ as
$$
  \mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7
  = \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}},
$$
where the $\mathbf{1}$ is the fixed direction $e$, and the $\mathbf{3},
\bar{\mathbf{3}}$ are complex conjugate representations
(Günaydin--Gürsey \cite{gunaydin1973}).

**The Sym$^2$ gate.**  This $\mathrm{SU}(3)$ passes the discriminator
test that eliminates the corpus's icosahedral colour triple $T_1$:
\begin{itemize}
\item $T_1$: $\mathrm{Sym}^2(T_1) = A \oplus H = \mathbf{1} \oplus
  \mathbf{5}$ --- a singlet is present, so $T_1$ admits an invariant
  symmetric bilinear form and is \emph{self-dual} (orthogonal type).
  It cannot carry $\mathrm{SU}(3)$.
\item $G_2$ route: $\mathrm{Sym}^2(\mathbf{3}) = \mathbf{6}$, irreducible
  --- no singlet, the fundamental is \emph{not self-dual} ($\mathbf{3}
  \not\cong \bar{\mathbf{3}}$).  This is the defining property of
  $\mathrm{SU}(N)$ for $N \geq 3$ (complex type).
\end{itemize}

**Discrete skeleton.**  The associator structure of $\mathbb{O}$ is
invariant under $\mathrm{GL}(3, \mathbb{F}_2) \cong \mathrm{PSL}(2,7)$,
the symmetry group of the Fano plane (7 points, 7 lines, 3 points per
line).  This is the finite shadow of $G_2$: the Fano plane indexes the
multiplication table of the imaginary units $e_1, \ldots, e_7$, and its
automorphism group is the largest finite subgroup of $G_2$ acting
faithfully on $\mathrm{Im}(\mathbb{O})$.  The cyclic determinant
$\det_3$-invariance of the associator has been machine-checked in the
corpus.

**Caveats.** Two honest qualifications:
\begin{enumerate}
\item This $\mathrm{SU}(3)$ is \emph{color}, not flavour.  But color
  $\mathrm{SU}(3)_c$ is precisely the item that
  \texttt{sm-open-problems.md} lists as open (``no construction;
  octonion fragments only''), so closing it is the more valuable target.
\item $\mathrm{PSL}(2,7)$ lives at genus $3$ (Klein quartic), while
  QOU's substrate is genus $4$ (Bring surface, $S_5$, icosahedral).
  Two routes connect them.  First, the $S_4$ bridge: $S_4$ (order $24$)
  is a maximal subgroup of \\emph{both} $S_5$ (point-stabiliser, index
  $5$) and $\mathrm{PSL}(2,7)$ (Fano point-stabiliser, index $7$);
  pinching an $S_4$-invariant $1$-cycle on the genus-$4$ Bring surface
  yields a nodal genus-$3$ curve inheriting $S_4$, which can enhance to
  the Hurwitz-maximal $\mathrm{PSL}(2,7)$ at genus $3$.  Second, the
  McKay correspondence $A_5 \to E_8$ reaches octonionic structure at the
  lattice level.  $\mathrm{PSL}(2,7)$ itself embeds as a finite subgroup
  of $\mathrm{SU}(3)$ (the Blichfeldt group of order $168$), giving a
  direct tie from the Fano-plane symmetry to color gauge structure.
  The continuous $G_2$ completion --- specifically the coset
  $S^6 = G_2/\mathrm{SU}(3)$ --- is a Mathlib gap (no
  \texttt{Octonion}, no $G_2$ Lie group), not a structural obstruction.
\end{enumerate}
