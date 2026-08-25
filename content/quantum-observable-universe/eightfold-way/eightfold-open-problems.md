This section collects the open problems identified during the
construction of this chapter, each stated with a falsifiable test.

**Consolidated ledger.**
Every structural ingredient the chapter uses, with its tier
([the root-system section](#sec:a2-root-system)).  Items marked *open*
name the missing object precisely.  The "Where" column points to the
numbered items below by *name* rather than by number, so that reordering
the list cannot silently break the pointers.

| Ingredient | Status | Where |
|---|---|---|
| $H_3(q)$ has Coxeter type $A_2$; $W(A_2) \cong S_3$ | standard, and true by construction ($B_n$ has type $A_{n-1}$) | [$A_2$ from three strands](#prop:a2-from-three-strands) |
| $A_2$ Cartan datum is independent of $q$ under Drinfeld--Jimbo quantisation | **standard** (Lusztig/Kashiwara), cited and *not* formalised here | [$q$-deformation](#rem:q-deformation-weight-lattice) |
| Serre exponent; root-angle ratio; the "two $2$s" separation (the Serre coefficient $[2]_q$ *moves* with $q$ while the Cartan datum does not) | proved (Lean, sorry-free) | `WeylInvarianceQDeformation.lean` |
| Root/weight lattices, Weyl group, Kazhdan–Lusztig multiplicities are $q$-independent | standard (Drinfeld–Jimbo), not formalised here | [$q$-deformation](#rem:q-deformation-weight-lattice) |
| Quantum Schur–Weyl duality $\mathcal{U}_q(\mathfrak{gl}_N) \leftrightarrow H_n(q)$ | standard \cite{jimbo1986}; the duality itself is not formalised, only its row-cap consequence | [Schur–Weyl](#prop:schur-weyl-eightfold) |
| $\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$; decuplet dimension $\binom{5}{3} = 10$; weight tables | standard $\mathrm{SU}(3)$ representation theory, **conditional on $N = 3$** | [meson octet](#prop:meson-octet-decomposition), [decuplet](#prop:borromean-decuplet) |
| $N = 2$ cannot host the eightfold-way decomposition | **standard**, with a sorry-free machine-checked *arithmetic* instance: the Lean defines $\dim V_{(1^3)} := \binom{N}{3}$ and proves $\binom{N}{3} = 0 \iff N < 3$. The hook-content formula and the row cap $\ell(\lambda) \le N$ are cited, not formalised — same caveat as `Sym2Gate` and `WeylInvariance` | `RowCapObstruction.lean` |
| $\dim V = N = 3$ for the flavour fundamental | **open**: framework supplies $\dim V = 2$; no $q$ raises the row cap. The *obstruction* is proved; the *construction* is missing | item *The $N = 3$ problem* |
| Writhe-to-isospin map $w \mapsto I_3$ on the nucleon doublet | derived, scale-free, no fitted parameters | [flavour charges](#rem:flavor-charge-assignments) |
| Hypercharge $Y$ | **open**: writhe map falsified ($p$, $n$ share $Y = +1$, writhes differ); missing a second crossing invariant | item *Hypercharge $Y$* |
| The baryon octet's weight map is non-injective | **proved** (Lean, sorry-free): $\Lambda$ and $\Sigma^0$ share $(2I_3, Y) = (0,0)$, so a weight-only mass formula predicts $m_\Lambda = m_{\Sigma^0}$ and is excluded at $\approx 7\%$ | [baryon octet](#prop:baryon-octet-decomposition) |
| $\mathrm{PSL}(2,7) \cong \mathrm{GL}(3,\mathbb{F}_2)$, order $168$, irreps $\{1,3,\bar 3,6,7,8\}$ | standard; machine-verified numerically (`psl27_irrep_verification.py`) | [colour from $G_2$](#prop:color-su3-from-g2) |
| $S_4$ bridge: transitive on local Fano lines | verified numerically (`s4_fano_action.py`) | [colour from $G_2$](#prop:color-su3-from-g2) |
| The $S_4$ bridge selects the Klein quartic | **refuted** (machine-verified), and not narrowly: the $S_4$-invariant quartics form a pencil, so *infinitely many* pairwise non-isomorphic genus-3 curves admit $S_4$ (Fermat is the member $t = 0$ of the pencil, $t$ being the pencil parameter, not a partition). The datum has essentially no separating power | `s4_genus3_competitor_fermat.py`, `s4_genus3_pencil_infinite_family.py` |
| Bring $\to$ Klein-quartic genus degeneration | **excluded** under its own three premises (scope-(b)): the pinch supplies an $S_4$-stable pair of marked points, and $S_4$ has *no orbit of size $\le 2$* on $\mathbb{P}^2$, since the $3$-dimensional representation and its restriction to $A_4$ are both absolutely irreducible. No smooth plane quartic carries such a pair, and Klein is not hyperelliptic. Rescue requires explicitly dropping one premise: hyperelliptic target, multi-node/separating pinch, or non-faithful $S_4$ | `s4_marked_pair_obstruction.py` |
| Octonionic $\mathbf{3}$ not excluded by the $\mathrm{Sym}^2$ gate | literature decomposition; the Lean file proves only arithmetic ($6=6 \wedge 0=0$) | `Sym2Gate.lean` |
| The octonion algebra $\mathbb{O}$ and $G_2 = \mathrm{Aut}(\mathbb{O})$ | **open**: used throughout [the colour-algebra section](#sec:color-algebra) but never defined — this paper has no definition of $\mathbb{O}$ to point at | — |
| Continuous $G_2$ completion ($S^6 = G_2/\mathrm{SU}(3)$) | **open**: Mathlib gap (no `Octonion` type, no $G_2$ Lie group) — infrastructure, not structural | item *Continuous $G_2$ completion* |
| Flavour vs. colour $\mathrm{SU}(3)$ | **open**: whether same, different, or groupoid-dual | item *Flavour versus colour separation* |
| Gell-Mann–Okubo has no discriminating power | **proved** (Lean, sorry-free): $4m_K^2 - 3m_\eta^2 - m_\pi^2 = 0$ identically for *any* first-order octet breaking | `GellMannOkuboIdentity.lean` |
| Meson mass splitting; the GMO **deviation** | **open**: the $\approx 6\%$ deviation is the only testable content; no second-order term derived, so the framework predicts $0$ | item *The Gell-Mann--Okubo deviation* |
| Spin–flavour–colour selection of the Young symmetriser | **open**: decuplet identification currently matches dimensions and weights only | item *Spin--flavour--colour selection rule* |
| Truncation ("freeze-out") mechanism | **open**: heuristic, no derivation | item *Truncation mechanism* |
| Three generations | **open**: not addressed here | item *Three generations* |

The chapter cannot do without two of these.  **$N = 3$** gates every flavour statement below --- the meson
octet, the baryon multiplets, and every quark row of the dictionary are
conditional on it, and it is not available from a single fibre.
**Hypercharge** gates the $\mathrm{U}(1)$ factor: without a second
crossing invariant the chapter reproduces $I_3$ but not $Y$, and the
Gell-Mann--Nishijima relation cannot be closed.

1. **The $N = 3$ problem.**
   Schur--Weyl duality \cite{jimbo1986}
   ([Proposition](#prop:schur-weyl-eightfold))
   requires the fundamental representation to be $3$-dimensional.  The
   single-fibre tower has $\dim V = 2$ (the standard single-fibre
   construction; the Descartes condition $\chi(\mathcal{A}) = -6$ is
   compatible with but does not uniquely force $N = 2$).  That $N = 2$
   *cannot* host the decomposition is now proved sorry-free
   (`RowCapObstruction.lean`: the alternating channel
   $\binom{N}{3}$ vanishes iff $N < 3$, and the decuplet dimension forces
   $N = 3$) --- so the obstruction is settled and only the construction is
   missing.  *Open:* construct a
   three-dimensional object $W$ in the multi-fibre groupoid whose
   symmetric square $\mathrm{Sym}^2(W)$ is irreducible (no singlet).
   The octonion $G_2$ route provides a colour $\mathrm{SU}(3)$ candidate
   that passes this test; whether it yields *flavour*
   $\mathrm{SU}(3)$ is untested.

2. **Hypercharge $Y$.**
   The writhe-to-isospin map $w \mapsto I_3$ is derived.  The
   hypercharge $Y$ is not: the writhe map is falsified as a $Y$
   assignment (proton and neutron share $Y = +1$ while their writhes
   differ).  *Open:* identify a second crossing invariant
   independent of the writhe.  Candidate: ribbon-framing twist
   ([Definition](#def:strand-twist-datum)).
   Battery (exploratory, not wired): of $10{,}000$ helon-style
   assignments, $4$ survive
   (`strand-twist-y-battery.witness.json`) --- but that ratio
   carries *no* corroboration, and is not a $2500\!:\!1$ filter.
   Proved sorry-free in
   `QOU/StandardModel/TwistBatteryVacuity.lean`: the spectrum
   battery is exactly $T = 3Q$ (the $-2I_3$ common to candidate and
   target cancels, leaving the defining equation of
   $Q_{\mathrm{twist}}$, not a test of it); the nucleon check is
   entailed by charge additivity and states one condition twice; and
   the $\mathbb{Z}_6$ condition never sees the assignment, so it
   filters nothing.  Each flavour is thus filtered independently by
   one linear equation, and $4 = 1 \times 2 \times 2 \times 1$ counts
   multisets with totals $3Q = (2,-1,0,-3)$ --- the "uniquely
   determined" $u$ and electron multisets being the two totals that
   admit a single multiset.
   A parameter-free repair using the *canonical* ribbon twist
   ($Q = c(\lambda)/3$, $c$ the content sum) was tested and fails: at
   $n = 3$ it gives the integer charges $\{+1,0,-1\}$, and no
   $n \le 8$ yields both quark charges
   (`ribbon_twist_charge_quantum_probe.py`); scope-(a) for
   that reading only.
   The derivation gap is therefore the entire content: whether the
   twist multisets are forced by the categorical braid words (not
   just consistent with them) is the open content of the hypercharge
   conjecture, and nothing else in the battery constrains anything.

3. **Continuous $G_2$ completion.**
   The discrete skeleton of $\mathrm{SU}(3) \subset G_2 =
   \mathrm{Aut}(\mathbb{O})$ is machine-checked
   ($\mathrm{GL}(3, \mathbb{F}_2) \cong \mathrm{PSL}(2,7)$ Fano
   symmetry of the associator).  The continuous Lie-group completion
   --- specifically the coset $S^6 = G_2/\mathrm{SU}(3)$ --- is a
   Mathlib gap (no `Octonion` type, no $G_2$ Lie group).  This
   is an infrastructure obstruction, not a structural one.

4. **Flavour versus colour separation.**
   The octonionic $\mathrm{SU}(3)$ is colour.  The eightfold-way
   classification requires flavour $\mathrm{SU}(3)$.  Whether these
   are the same, different, or related by a groupoid-level duality
   is open.  The obstruction audit
   ([the colour-algebra section](#sec:color-algebra)) shows
   that they *cannot* both come from the same construction: the
   $\mathrm{Sym}^2$ gate excludes the icosahedral colour triple $T_1$,
   while the $G_2$ route passes it.

5. **Truncation mechanism.**
   Why does the observable-scale symmetry reduce to a finite-dimensional
   Lie group rather than the full groupoid symmetry?  Root-of-unity
   truncation is a candidate (T4), but no derivation of the specific
   root of unity from QOU axioms exists.

6. **Three generations.**
   The $A_2$ root system and eightfold-way classification are
   generation-independent.  Why there are exactly three generations
   of fermions is a separate open problem (T6), not addressed here.

7. **Spin--flavour--colour selection rule.**
   The identification $\lambda = (3) \leftrightarrow$ decuplet,
   $\lambda = (2,1) \leftrightarrow$ octet
   ([Proposition](#prop:borromean-decuplet)) currently matches
   dimensions and weights only.  What physically forces the symmetric
   flavour channel for the spin-$3/2$ decuplet is antisymmetry of the
   total wavefunction once colour is included --- colour antisymmetric
   and spin symmetric force flavour symmetric.  This chapter derives
   neither the spin factor nor the colour antisymmetry.  *Open:*
   produce the spin degree of freedom and the colour-antisymmetry
   constraint from the braid structure, and show that together they
   determine the Young symmetriser.  Compatibility with it is what the
   chapter currently establishes.

8. **The Gell-Mann--Okubo deviation.**
   The relation $4m_K^2 = 3m_\eta^2 + m_\pi^2$ is *not* a target
   for derivation: it holds identically for any first-order octet
   breaking, whatever the mechanism, proved sorry-free in
   `GellMannOkuboIdentity.lean`.  Reproducing it would therefore
   be no evidence for the framework.  *Open:* the $\approx 6\%$
   *deviation*, which measures the failure of first-order breaking
   (second-order terms plus $\eta$--$\eta'$ singlet mixing).  The
   framework has derived no second-order term and so predicts deviation
   $0$; a derivation that produced $\approx 6\%$ would be a genuine
   prediction, and one that produced a different value would falsify the
   mechanism.  The former $\approx 3.3\%$ comparison against
   $\dim_q(\text{adjoint})$ is withdrawn as a category error
   (a dimension is not a mass splitting).

9. **Ocneanu/Markov trace parameter.**
   The Markov trace $\tau$ on $H_n(q)$ involves a second parameter
   $z$ (the trace parameter).  In QOU, $q$ is the substrate parameter
   (observed at our location as $q_0$, not derived from Bring topology).
   Whether $z$ is similarly extracted from categorical data or must be
   chosen is open (T3f).
