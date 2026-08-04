This section collects the open problems identified during the
construction of this chapter, each stated with a falsifiable test.

\begin{enumerate}

\item \textbf{The $N = 3$ problem.}
  Schur--Weyl duality (Proposition~\ref{prop:schur-weyl-eightfold})
  requires the fundamental representation to be $3$-dimensional.  The
  single-fibre tower has $\dim V = 2$ (the standard single-fibre
  construction; the Descartes condition $\chi(\mathcal{A}) = -6$ is
  compatible with but does not uniquely force $N = 2$).  \emph{Open:} construct a
  three-dimensional object $W$ in the multi-fibre groupoid whose
  symmetric square $\mathrm{Sym}^2(W)$ is irreducible (no singlet).
  The octonion $G_2$ route provides a colour $\mathrm{SU}(3)$ candidate
  that passes this test; whether it yields \emph{flavour}
  $\mathrm{SU}(3)$ is untested.

\item \textbf{Hypercharge $Y$.}
  The writhe-to-isospin map $w \mapsto I_3$ is derived.  The
  hypercharge $Y$ is not: the writhe map is falsified as a $Y$
  assignment (proton and neutron share $Y = +1$ while their writhes
  differ).  \emph{Open:} identify a second crossing invariant
  independent of the writhe.  Candidate: ribbon-framing twist
  (Definition~\ref{def:strand-twist-datum}).
  Battery (exploratory, not wired): of $10{,}000$ helon-style
  assignments, only $4$ survive the spectrum + nucleon-GMN battery;
  the $u$-quark twist multiset $\{0,1,1\}$ and the electron twist
  $\{-1,-1,-1\}$ are uniquely determined
  (\texttt{strand-twist-y-battery.witness.json}).
  The derivation gap: whether these twist multisets are forced by
  the categorical braid words (not just consistent with them) is
  the open content of the hypercharge conjecture.

\item \textbf{Continuous $G_2$ completion.}
  The discrete skeleton of $\mathrm{SU}(3) \subset G_2 =
  \mathrm{Aut}(\mathbb{O})$ is machine-checked
  ($\mathrm{GL}(3, \mathbb{F}_2) \cong \mathrm{PSL}(2,7)$ Fano
  symmetry of the associator).  The continuous Lie-group completion
  --- specifically the coset $S^6 = G_2/\mathrm{SU}(3)$ --- is a
  Mathlib gap (no \texttt{Octonion} type, no $G_2$ Lie group).  This
  is an infrastructure obstruction, not a structural one.

\item \textbf{Flavour vs.\ colour separation.}
  The octonionic $\mathrm{SU}(3)$ is colour.  The eightfold-way
  classification requires flavour $\mathrm{SU}(3)$.  Whether these
  are the same, different, or related by a groupoid-level duality
  is open.  The obstruction audit (\S\ref{sec:color-algebra}) shows
  that they \emph{cannot} both come from the same construction: the
  $\mathrm{Sym}^2$ gate excludes the icosahedral colour triple $T_1$,
  while the $G_2$ route passes it.

\item \textbf{Truncation mechanism.}
  Why does the observable-scale symmetry reduce to a finite-dimensional
  Lie group rather than the full groupoid symmetry?  Root-of-unity
  truncation is a candidate (T4), but no derivation of the specific
  root of unity from QOU axioms exists.

\item \textbf{Three generations.}
  The $A_2$ root system and eightfold-way classification are
  generation-independent.  Why there are exactly three generations
  of fermions is a separate open problem (T6), not addressed here.

\item \textbf{Ocneanu/Markov trace parameter.}
  The Markov trace $\tau$ on $H_n(q)$ involves a second parameter
  $z$ (the trace parameter).  In QOU, $q$ is the substrate parameter
  (observed at our location as $q_0$, not derived from Bring topology).
  Whether $z$ is similarly extracted from categorical data or must be
  chosen is open (T3f).

\end{enumerate}
