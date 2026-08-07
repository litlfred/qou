This section collects the open problems identified during the
construction of this chapter, each stated with a falsifiable test.

**Consolidated ledger.**
Every structural ingredient the chapter uses, with its tier
(\S\ref{sec:a2-root-system}).  Items marked *open* name the missing
object precisely.

| Ingredient | Status | Where |
|---|---|---|
| $H_3(q)$ has Coxeter type $A_2$; $W(A_2) \cong S_3$ | standard, and true by construction ($B_n$ has type $A_{n-1}$) | [$A_2$ from three strands](#prop:a2-from-three-strands) |
| $A_2$ Cartan matrix is fixed integer data, independent of $q$; Serre exponent; root-angle ratio; the "two $2$s" separation | proved (Lean, sorry-free) | `WeylInvarianceQDeformation.lean` |
| Root/weight lattices, Weyl group, Kazhdan–Lusztig multiplicities are $q$-independent | standard (Drinfeld–Jimbo), not formalised here | [$q$-deformation](#rem:q-deformation-weight-lattice) |
| Quantum Schur–Weyl duality $\mathcal{U}_q(\mathfrak{gl}_N) \leftrightarrow H_n(q)$ | standard \cite{jimbo1986}; the duality itself is not formalised, only its row-cap consequence | [Schur–Weyl](#prop:schur-weyl-eightfold) |
| $\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$; decuplet dimension $\binom{5}{3} = 10$; weight tables | standard $\mathrm{SU}(3)$ representation theory, **conditional on $N = 3$** | [meson octet](#prop:meson-octet-decomposition), [decuplet](#prop:borromean-decuplet) |
| $N = 2$ cannot host the eightfold-way decomposition | **proved** (Lean, sorry-free): $\dim V_{(1^3)} = \binom{N}{3} = 0 \iff N < 3$; decuplet dimension forces $N = 3$ | `RowCapObstruction.lean` |
| $\dim V = N = 3$ for the flavour fundamental | **open**: framework supplies $\dim V = 2$; no $q$ raises the row cap. The *obstruction* is proved; the *construction* is missing | item 1 below |
| Writhe-to-isospin map $w \mapsto I_3$ on the nucleon doublet | derived, scale-free, no fitted parameters | [flavour charges](#rem:flavor-charge-assignments) |
| Hypercharge $Y$ | **open**: writhe map falsified ($p$, $n$ share $Y = +1$, writhes differ); missing a second crossing invariant | item 2 below |
| $\mathrm{PSL}(2,7) \cong \mathrm{GL}(3,\mathbb{F}_2)$, order $168$, irreps $\{1,3,\bar 3,6,7,8\}$ | standard; machine-verified numerically (`psl27_irrep_verification.py`) | [colour from $G_2$](#prop:color-su3-from-g2) |
| $S_4$ bridge: transitive on local Fano lines | verified numerically (`s4_fano_action.py`) | [colour from $G_2$](#prop:color-su3-from-g2) |
| The $S_4$ bridge selects the Klein quartic | **refuted** (machine-verified), and not narrowly: the $S_4$-invariant quartics form a pencil, so *infinitely many* pairwise non-isomorphic genus-3 curves admit $S_4$ (Fermat is the member $t = 0$ of the pencil, $t$ being the pencil parameter, not a partition). The datum has essentially no separating power | `s4_genus3_competitor_fermat.py`, `s4_genus3_pencil_infinite_family.py` |
| Bring $\to$ Klein-quartic genus degeneration | **excluded** under its own three premises (scope-(b)): the pinch supplies an $S_4$-stable pair of marked points, and $S_4$ has *no orbit of size $\le 2$* on $\mathbb{P}^2$, since the $3$-dimensional representation and its restriction to $A_4$ are both absolutely irreducible. No smooth plane quartic carries such a pair, and Klein is not hyperelliptic. Rescue requires explicitly dropping one premise: hyperelliptic target, multi-node/separating pinch, or non-faithful $S_4$ | `s4_marked_pair_obstruction.py`; beans `qou-8p1b`, `qou-8p1c` |
| Octonionic $\mathbf{3}$ not excluded by the $\mathrm{Sym}^2$ gate | literature decomposition; the Lean file proves only arithmetic ($6=6 \wedge 0=0$) | `Sym2Gate.lean`, bean `qou-sym2` |
| The octonion algebra $\mathbb{O}$ and $G_2 = \mathrm{Aut}(\mathbb{O})$ | **open**: used throughout \S\ref{sec:color-algebra} but **never defined as a content block** — there is no `def:octonion-algebra` in the corpus | bean `qou-8fl1` |
| Continuous $G_2$ completion ($S^6 = G_2/\mathrm{SU}(3)$) | **open**: Mathlib gap (no `Octonion` type, no $G_2$ Lie group) — infrastructure, not structural | item 3 below |
| Flavour vs. colour $\mathrm{SU}(3)$ | **open**: whether same, different, or groupoid-dual | item 4 below |
| Gell-Mann–Okubo has no discriminating power | **proved** (Lean, sorry-free): $4m_K^2 - 3m_\eta^2 - m_\pi^2 = 0$ identically for *any* first-order octet breaking | `GellMannOkuboIdentity.lean` |
| Meson mass splitting; the GMO **deviation** | **open**: the $\approx 6\%$ deviation is the only testable content; no second-order term derived, so the framework predicts $0$ | item 6 below |
| Spin–flavour–colour selection of the Young symmetriser | **open**: decuplet identification currently matches dimensions and weights only | item 5 below |
| Truncation ("freeze-out") mechanism | **open**: heuristic, no derivation | item 7 below |
| Three generations | **open**: not addressed here | item 9 below |

Two of these deserve emphasis, because the chapter cannot do without
them.  **$N = 3$** gates every flavour statement below --- the meson
octet, the baryon multiplets, and every quark row of the dictionary are
conditional on it, and it is not available from a single fibre.
**Hypercharge** gates the $\mathrm{U}(1)$ factor: without a second
crossing invariant the chapter reproduces $I_3$ but not $Y$, and the
Gell-Mann--Nishijima relation cannot be closed.

\begin{enumerate}

\item \textbf{The $N = 3$ problem.}
  Schur--Weyl duality \cite{jimbo1986}
  (Proposition~\ref{prop:schur-weyl-eightfold})
  requires the fundamental representation to be $3$-dimensional.  The
  single-fibre tower has $\dim V = 2$ (the standard single-fibre
  construction; the Descartes condition $\chi(\mathcal{A}) = -6$ is
  compatible with but does not uniquely force $N = 2$).  That $N = 2$
  \emph{cannot} host the decomposition is now proved sorry-free
  (\texttt{RowCapObstruction.lean}: the alternating channel
  $\binom{N}{3}$ vanishes iff $N < 3$, and the decuplet dimension forces
  $N = 3$) --- so the obstruction is settled and only the construction is
  missing.  \emph{Open:} construct a
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

\item \textbf{Spin--flavour--colour selection rule.}
  The identification $\lambda = (3) \leftrightarrow$ decuplet,
  $\lambda = (2,1) \leftrightarrow$ octet
  (Proposition~\ref{prop:borromean-decuplet}) currently matches
  dimensions and weights only.  What physically forces the symmetric
  flavour channel for the spin-$3/2$ decuplet is antisymmetry of the
  total wavefunction once colour is included --- colour antisymmetric
  and spin symmetric force flavour symmetric.  This chapter derives
  neither the spin factor nor the colour antisymmetry.  \emph{Open:}
  produce the spin degree of freedom and the colour-antisymmetry
  constraint from the braid structure, and show that together they
  determine the Young symmetriser.  Compatibility with it is what the
  chapter currently establishes.

\item \textbf{The Gell-Mann--Okubo deviation.}
  The relation $4m_K^2 = 3m_\eta^2 + m_\pi^2$ is \emph{not} a target
  for derivation: it holds identically for any first-order octet
  breaking, whatever the mechanism, proved sorry-free in
  \texttt{GellMannOkuboIdentity.lean}.  Reproducing it would therefore
  be no evidence for the framework.  \emph{Open:} the $\approx 6\%$
  \emph{deviation}, which measures the failure of first-order breaking
  (second-order terms plus $\eta$--$\eta'$ singlet mixing).  The
  framework has derived no second-order term and so predicts deviation
  $0$; a derivation that produced $\approx 6\%$ would be a genuine
  prediction, and one that produced a different value would falsify the
  mechanism.  The former $\approx 3.3\%$ comparison against
  $\dim_q(\text{adjoint})$ is withdrawn as a category error
  (a dimension is not a mass splitting).

\item \textbf{Ocneanu/Markov trace parameter.}
  The Markov trace $\tau$ on $H_n(q)$ involves a second parameter
  $z$ (the trace parameter).  In QOU, $q$ is the substrate parameter
  (observed at our location as $q_0$, not derived from Bring topology).
  Whether $z$ is similarly extracted from categorical data or must be
  chosen is open (T3f).

\end{enumerate}
