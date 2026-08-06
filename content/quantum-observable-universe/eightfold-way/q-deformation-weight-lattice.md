A persistent confusion in the literature and in early drafts of this
framework conflates two occurrences of the number $2$ in the $A_2$
Serre relation.  Resolving this confusion is essential for
understanding what the substrate parameter $q_0$ does and does not do
to the eightfold-way classification.

**The two $2$s.**
The classical Serre relation for $A_2$ reads
$$
  e_i^2 e_j - 2\, e_i e_j e_i + e_j e_i^2 = 0,
$$
where the coefficient $2$ is the binomial coefficient
$\binom{2}{1} = \binom{1 - a_{ij}}{1}$, with $a_{ij} = -1$ the
off-diagonal Cartan entry.  Meanwhile, the diagonal Cartan entry is
$a_{ii} = 2$, which appears in the root angle formula
$\cos\theta = a_{ij}/a_{ii} = -1/2$, giving $\theta = 120°$.

The Drinfeld--Jimbo quantization replaces the binomial $2$ by the
Gaussian binomial $[2]_q = q + q^{-1}$:
$$
  e_i^2 e_j - [2]_q\, e_i e_j e_i + e_j e_i^2 = 0.
$$
The Cartan entry $a_{ii} = 2$ is \emph{untouched}.  The angle
$\cos\theta = -1/2$ does not become $\cos\theta_q = -(q + q^{-1})/2$.
These are two different mathematical objects that coincide numerically
at $q = 1$: one is a binomial coefficient, the other is a normalization
constant.

**What is $q$-independent — machine-checked.**
The following are proved sorry-free in
\texttt{QOU/Eightfold/WeylInvarianceQDeformation.lean}:
\begin{itemize}
\item The Cartan matrix $a_{ij}$ is fixed integer data, independent of
  $q$ (\texttt{cartanMatrix\_A2\_q\_independent}, quantified over two
  arbitrary $q_1, q_2$ in any commutative ring).
\item The off-diagonal entry $a_{12} = -1$ and the Serre exponent
  $1 - a_{12} = 2$ (\texttt{cartan\_A2\_offdiag},
  \texttt{serre\_exponent\_A2}).
\item The $q$-Serre coefficient $[2]_q$ and the Cartan diagonal
  $a_{ii} = 2$ are distinct objects, agreeing only at $q = 1$
  (\texttt{qSerre\_neq\_cartan\_diag},
  \texttt{qSerre\_eq\_cartan\_at\_classical}) --- the ``two $2$s''
  separation above.
\item The root-angle ratio $\cos\theta = a_{ij}/a_{ii} = -1/2$
  (\texttt{root\_angle\_ratio\_A2}).
\end{itemize}

**What is $q$-independent — standard, but not formalised here.**
These follow from the Drinfeld--Jimbo construction and are cited, not
machine-checked in this corpus:
\begin{itemize}
\item The root lattice $\Lambda_R = \mathbb{Z}\alpha_1 \oplus
  \mathbb{Z}\alpha_2$ and the weight lattice $\Lambda_W =
  \mathbb{Z}\omega_1 \oplus \mathbb{Z}\omega_2$.
\item The Weyl group $W(A_2) \cong S_3$.
\item Weight multiplicities: for generic $q$ the representation category
  $\mathrm{Rep}\,\mathcal{U}_q(\mathfrak{g})$ is tensor-equivalent to
  $\mathrm{Rep}\,\mathfrak{g}$.  Crystal bases exist precisely because
  the weight combinatorics is $q$-independent (the $q \to 0$ limit
  retains the same lattice).
\end{itemize}

**What $q$ does deform.**
\begin{itemize}
\item The braiding: the $R$-matrix of $\mathcal{U}_q(\mathfrak{sl}_3)$
  depends on $q$ and governs the braid group action on tensor products.
\item The quantum dimensions: $\dim_q(V_\lambda) = \prod_{\alpha > 0}
  [\langle \lambda + \rho, \alpha^\vee \rangle]_q /
  [\langle \rho, \alpha^\vee \rangle]_q$.
\item The Markov trace: $\tau_q(\beta)$ on $H_n(q)$ varies with $q$,
  producing $q$-dependent link invariants (Jones polynomial, HOMFLY-PT).
\item The crossing energy: $\mathfrak{E}_\times(q) =
  \tfrac{1}{2}(q - q^{-1})$, which governs mass splittings in the
  framework.
\end{itemize}

**Consequence for the eightfold way.**
The hexagonal weight lattice of $A_2$ is rigid under $q$-deformation.
The octet and decuplet patterns do not ``bend'' or become hyperbolic
at $q = q_0$.  What changes is the \emph{dynamics on} the lattice:
transition amplitudes, mass splittings, and mixing angles all depend
on $q_0$ through the Hecke algebra representations, while the
classification pattern itself --- which states go where on the
hexagon --- is $q$-independent.

This separation is a feature: the classification is universal (it holds
for any $q$), while the quantitative predictions (mass ratios, decay
rates) are specific to $q = q_0$.
