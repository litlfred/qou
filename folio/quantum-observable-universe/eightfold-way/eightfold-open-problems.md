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
| $A_2$ Cartan datum is independent of $q$ under Drinfeld--Jimbo quantisation | **standard** (Lusztig/Kashiwara), cited and *not* proved here | [$q$-deformation](#rem:q-deformation-weight-lattice) |
| Serre exponent; root-angle ratio; the "two $2$s" separation (the Serre coefficient $[2]_q$ *moves* with $q$ while the Cartan datum does not) | proved | [$q$-deformation](#rem:q-deformation-weight-lattice) |
| Root/weight lattices, Weyl group, Kazhdan–Lusztig multiplicities are $q$-independent | standard (Drinfeld–Jimbo), not proved here | [$q$-deformation](#rem:q-deformation-weight-lattice) |
| Quantum Schur–Weyl duality $\mathcal{U}_q(\mathfrak{gl}_N) \leftrightarrow H_n(q)$ | standard \cite{jimbo1986}; the duality itself is not proved here, only its row-cap consequence | [Schur–Weyl](#prop:schur-weyl-eightfold) |
| $\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$; $\dim \mathrm{Sym}^3(W_3^*) = \binom{5}{3} = 10$; quantum $[3]_q^3 = (q^2 + q^{-2})[5]_q + 2[2]_q[4]_q + 1$; weight tables | traceless/scalar vector-space split, polynomial-module dimension $10 \neq 4$, and generic-$q$ quantum dimension balance **proved**; $\mathrm{SU}(3)_{\mathrm{f}}$ equivariance and applicability **conditional on $N = 3$** | [meson octet](#prop:meson-octet-decomposition), [decuplet](#prop:borromean-decuplet) |
| $N = 2$ cannot host the eightfold-way decomposition | **standard**, with a proved *arithmetic* instance: $\dim V_{(1^3)}$ is taken to be $\binom{N}{3}$, and $\binom{N}{3} = 0 \iff N < 3$ is proved. The hook-content formula and the row cap $\ell(\lambda) \le N$ are cited, not proved — same caveat as the $q$-deformation row | [Schur–Weyl](#prop:schur-weyl-eightfold) |
| $\dim V = N = 3$ for the flavour fundamental | **open**: framework supplies $\dim V = 2$; no $q$ raises the row cap. The *obstruction* is proved; the *construction* is missing | item *The $N = 3$ problem* |
| No object of the single-fibre category reaches $\dim W = 3$ through the $\mathrm{Sym}^2$ gate | **proved**, and at *object* level rather than only for irreducible summands: the Frobenius--Schur count forces a passing $W$ to be a sum of pairwise *distinct* even-dimensional irreps, so $\dim W$ is even, and $3$ is odd | item *The $N = 3$ problem* |
| Inequivalent fibre functors of the single-fibre category | **standard** \cite{bichon2003}: they exist at every dimension $n \ge 2$ and are real at $q_0$; and **proved** that none of them supplies a one-dimensional summand of $V^{\otimes 3}$ --- the spin-$0$ object is absent by Clebsch--Gordan parity, so the fusion rules, which every fibre functor preserves, exclude $\mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$ at every $n$ | item *The $N = 3$ problem* |
| Writhe-to-isospin map $w \mapsto I_3$ on the nucleon doublet | derived, scale-free, no fitted parameters, for the writhe of the inter-nucleon arc; the ruled nucleon word has writhe $0$ for both nucleons | [flavour charges](#rem:flavor-charge-assignments) |
| Hypercharge $Y$ and split-bundle $F = V_2 \oplus W_3^*$ coupling | **conditionally coupled** to $N = 3$: single-fibre writhe map falsified ($p$, $n$ share $Y = +1$); on $F = V_2 \oplus W_3^*$ ($z_3 = q^3/[3]_q$), tracelessness $2y_2 + 3y_3 = 0 \iff y_3 = -\tfrac{2}{3}y_2$ is **proved** (fixing doublet $y_2 + y_3 = +\tfrac{1}{3}$, Killing Weinberg ratio $3/8$, and separating $\bar u = -\tfrac{2}{3}$ from $d = -\tfrac{1}{3}$); **open**: categorical construction of $W_3$ | [flavour charges](#rem:flavor-charge-assignments), item *Hypercharge $Y$* |
| Baryon octet weight degeneracy and $H_3(q)$ $S^{(2,1)}$ diquark split | **proved** (exclusion + operator split), **open** (scale): weight-only formulas give $m_\Lambda = m_{\Sigma^0}$ (excluded at $77\;\mathrm{MeV}$), while internal $S^{(2,1)}$ diquark projectors $P_\Lambda, P_{\Sigma^0}$ give $\mathrm{tr}(P_\Lambda V^3) - \mathrm{tr}(P_{\Sigma^0} V^3) = (q - q^{-1})^3(q^2 + q^{-2})[3]_q/[2]_q \neq 0$ ($31.5\;\mathrm{MeV}$ at $q_0$ vs empirical $77.0\;\mathrm{MeV}$) | [baryon octet](#prop:baryon-octet-decomposition) |
| Ordered 3-strand gluon clasp $\beta_{\mathrm{clasp}}(n_1, n_2)$ on neutral mesons | **proved** (invariants), **open** (absolute mass scale): $\mathrm{SL}_2(\mathbb{Z})$ trace $2n_1n_2 + n_1 + n_2 + 3 \ge 27 > 2$ across $\{3,5,7\}^2$, separating $\bar D^0 = (-5,+3)$ from $K^0 = (+3,-5)$ in both $z_2$ and $z_3$ Markov traces | [meson mass splitting](#rem:meson-mass-splitting), [dictionary supplement](#rem:dictionary-flavor-layer) |
| $\mathrm{PSL}(2,7) \cong \mathrm{GL}(3,\mathbb{F}_2)$, order $168$, irreps $\{1,3,\bar 3,6,7,8\}$ | standard; machine-verified numerically | [colour from $G_2$](#prop:color-su3-from-g2) |
| $S_4$ bridge: transitive on local Fano lines | verified numerically | [colour from $G_2$](#prop:color-su3-from-g2) |
| The $S_4$ bridge selects the Klein quartic | **refuted** (verified by exact computation), and not narrowly: the $S_4$-invariant quartics form a pencil, so *infinitely many* pairwise non-isomorphic genus-3 curves admit $S_4$ (Fermat is the member $t = 0$ of the pencil, $t$ being the pencil parameter, not a partition). The datum has essentially no separating power | [colour from $G_2$](#prop:color-su3-from-g2) |
| Bring $\to$ Klein-quartic genus degeneration | **excluded** under its own three premises (scope-(b)): the pinch supplies an $S_4$-stable pair of marked points, and $S_4$ has *no orbit of size $\le 2$* on $\mathbb{P}^2$, since the $3$-dimensional representation and its restriction to $A_4$ are both absolutely irreducible. No smooth plane quartic carries such a pair, and Klein is not hyperelliptic. Rescue requires explicitly dropping one premise: hyperelliptic target, multi-node/separating pinch, or non-faithful $S_4$ | [colour from $G_2$](#prop:color-su3-from-g2) |
| Octonionic $\mathbf{3}$ passes the $\mathrm{Sym}^2$ gate | **proved**: at dimension three, passing the gate forces a complex-type summand, and the Günaydin--Gürsey triple is complex type --- every $J_6$-compatible $\mathfrak{su}(3)$-invariant bilinear form on the colour triplet vanishes, so $\mathrm{Sym}^2(\mathbf{3})$ has no singlet and $\mathbf{3} \not\cong \bar{\mathbf{3}}$ (`OctonionColourTripletComplexType.lean`) | [Schur–Weyl](#prop:schur-weyl-eightfold) |
| The octonion algebra $\mathbb{O}$ and $G_2 = \mathrm{Aut}(\mathbb{O})$ | **established**: [definition](#def:octonion-algebra) in [the colour-algebra section](#sec:color-algebra), with $\mathrm{Der}(\mathbb{O}) = \mathfrak{g}_2$ (\cite{baez2002}) and the Baez-convention multiplication | [definition](#def:octonion-algebra) |
| Continuous $G_2$ completion ($S^6 = G_2/\mathrm{SU}(3)_{\mathrm{c}}$) | Lie-algebra level **proved**: $\dim \mathrm{Der}(\mathbb{O}) = 14$ (`octonion_derivation_dim`) and the stabilizer of a unit imaginary has $\dim = 8$ (`finrank_su3_e1`), so $\dim \mathfrak{g}_2 - \dim \mathfrak{su}(3) = 6 = \dim S^6$. **Open**: the continuous Lie group $G_2$ and the coset $S^6$ themselves — an infrastructure gap, not a structural one | item *Continuous $G_2$ completion* |
| Flavour vs. colour ($\mathrm{SU}(3)_{\mathrm{f}}$ vs. $\mathrm{SU}(3)_{\mathrm{c}}$) | **open**: whether same, different, or groupoid-dual | item *Flavour versus colour separation* |
| Gell-Mann–Okubo has no discriminating power | **proved**: $4m_K^2 - 3m_\eta^2 - m_\pi^2 = 0$ identically for *any* first-order octet breaking | [meson mass splitting](#rem:meson-mass-splitting) |
| Meson mass splitting; the GMO **deviation** | **partially resolved** (sign), **open** (magnitude): rational quantum Casimir gives $(4M_K - 3M_\eta - M_\pi)/(M_\pi - M_\eta) = -((q-1)/(q+1))^2$ (**proved**, matching both meson $+$ and baryon $-$ signs at $q_0$), but accounts for only $1.21\%$ of the $6.43\%$ meson deviation; $\eta$--$\eta'$ mixing remains open | [meson mass splitting](#rem:meson-mass-splitting), item *The Gell-Mann--Okubo deviation* |
| Spin–flavour–colour selection of the Young symmetriser | **open**: decuplet identification currently matches dimensions and weights only | item *Spin--flavour--colour selection rule* |
| Truncation ("freeze-out") mechanism | **open**: heuristic, no derivation | item *Truncation mechanism* |
| Three generations | **open**: not addressed here | item *Three generations* |

The chapter cannot do without **$N = 3$**: the meson octet, the baryon
multiplets, and every quark row of the dictionary are conditional on a
three-dimensional partner, which is unavailable from a single fibre.  As
shown in the Standard Model appendix and in
[the flavour-charges remark](#rem:flavor-charge-assignments),
**hypercharge** is coupled to that same missing partner: on the split
bundle $F = V_2 \oplus W_3^*$ ($z_3 = q^3/[3]_q$), tracelessness forces
$y_3 = -\tfrac{2}{3}y_2$ with no free parameter, whereas without $W_3^*$
the chapter reproduces $I_3$ alone and cannot close the
Gell-Mann--Nishijima relation.

1. **The $N = 3$ problem.**
   Schur--Weyl duality \cite{jimbo1986}
   ([Proposition](#prop:schur-weyl-eightfold))
   requires the fundamental representation to be $3$-dimensional.  The
   single-fibre tower has $\dim V = 2$ (the standard single-fibre
   construction; the Descartes condition $\chi(\mathcal{A}) = -6$ is
   compatible with but does not uniquely force $N = 2$).  That $N = 2$
   *cannot* host the decomposition is now proved
   (the alternating channel
   $\binom{N}{3}$ vanishes iff $N < 3$, and the decuplet dimension forces
   $N = 3$) --- so the obstruction is settled and only the construction is
   missing.  *Open:* construct a
   three-dimensional object $W$ in the multi-fibre groupoid whose
   symmetric square $\mathrm{Sym}^2(W)$ is irreducible (no singlet).
   The octonion $G_2$ route supplies a colour $\mathrm{SU}(3)_{\mathrm{c}}$ candidate
   that **passes** the gate: the singlet count $0$ of
   $\mathrm{Sym}^2(\mathbf{3})$ is proved over $\mathbb{Q}$, together with
   $\mathbf{3} \not\cong \bar{\mathbf{3}}$ (see the ledger).  Whether it yields *flavour*
   $\mathrm{SU}(3)_{\mathrm{f}}$ is untested.

   **What such a construction must supply is now a theorem, and it is one
   property rather than a list.**  Putting the two halves
   together: a three-dimensional object
   passing the gate must contain a complex-type irrep
, and a category all of whose irreps
   are self-dual contains none — which is precisely the single-fibre case,
   since every $\mathrm{SU}(2)$ irrep is self-dual.  So *the property a
   groupoid construction must exhibit is exactly the property one fibre
   lacks*: **non-self-duality**.  This yields a screening test
: a candidate whose three-dimensional
   object is isomorphic to its own dual is dead, and can be discarded
   before its $\mathrm{Sym}^2$ decomposition is computed.  It does not
   construct anything — Route A stays open — but it replaces "more
   structure" with a single checkable condition.

   **The same condition is reachable from the row cap, independently.**
   The Descartes characteristic $\chi_{\mathrm{eu}}(M_0) = -6$ forces $\mathrm{SU}(2)$,
   hence $\dim V = 2$, hence partitions of at most two rows, so the
   $(1^3)$ block drops at $n = 3$ and a three-dimensional object cannot
   be a tensor power of the single fibre.  That argument reaches
   non-self-duality without the $\mathrm{Sym}^2$ gate and without the
   Frobenius--Schur trichotomy, as the gate-and-trichotomy argument
   reaches it without the Euler characteristic and without Schur--Weyl.
   A third route reaches the same negative from a different direction
   again: $N \neq 3$ follows from non-degeneracy of the fibre's volume form
   ($\Lambda^2 V \cong \mathbf{1}$ forces $N = 2$), without the
   $\mathrm{Sym}^2$ gate, the row cap or the Euler characteristic.

   The three are not three votes on one proposition, and the difference
   is what matters here.  The row-cap and volume-form arguments bound the
   **fibre**: they say $N = 2$, so one fibre cannot supply a
   three-dimensional object.  The gate-and-trichotomy argument bounds any
   **candidate**: it says which property a candidate must have, and so
   yields a test that can be applied to an object nobody has built yet.
   The negative is now over-determined; the screen is what is additive.

   *That the search is confined to the groupoid level is now a theorem,
   not an extrapolation.*  The parity criterion
 decides the $\mathrm{Sym}^2$ gate for a single
   **irreducible** summand, and a three-dimensional $W$ need not be
   irreducible --- $W = V_{1/2} \oplus V_0$ has dimension $3$, sits in the
   tensor category generated by the fibre, and is not an irrep, so that
   criterion does not reach it.  The multiplicity form
 closes the case: counting
   singlets by Frobenius--Schur type, a passing $W$ must be a sum of
   pairwise *distinct* even-dimensional irreps, hence $\dim W$ is even.
   Since $3$ is odd, **no** three-dimensional object of the single-fibre
   category passes the gate, reducible or not.  Any $N = 3$ must therefore
   come from genuinely multi-fibre structure --- which is what the route
   above asserts, now with a proved invariant behind it (a scope-(b)
   exclusion, the invariant being the Frobenius--Schur indicator
   $(-1)^{2j}$).  Even dimension is *necessary, not sufficient*:
   $V_{1/2}^{\oplus 2}$ has dimension $4$ and fails the gate too, so the
   parity invariant prunes candidates rather than characterising them.
   The octonionic candidate is no counterexample to this: it is not an
   object of the single-fibre category at all, arising instead from
   $G_2 = \mathrm{Aut}(\mathbb{O})$, which is precisely why the parity
   exclusion leaves it standing.

   The mechanism behind that escape is now proved rather than asserted, and
   it is worth stating because it bounds how far the exclusion reaches.
   The parity argument runs through self-duality: every $\mathrm{SU}(2)$
   irrep satisfies $V^* \cong V$, so the cross terms $V_i \otimes V_j$
   contribute no singlet and the survivors are forced to be distinct
   even-dimensional irreps.  A **complex-type** representation
   ($\mathrm{FS} = 0$, $\mathbf{3} \not\cong \bar{\mathbf{3}}$) pairs to a
   singlet only against its conjugate, so one whose conjugate is *absent*
   from the object passes the gate at any dimension, odd included ---
   and such an object is exhibited at
   dimension exactly $3$.  So the even-dimension exclusion above is a scope-(b)
   exclusion **within the self-dual sector** and is silent, not negative,
   outside it.  This is the same non-self-duality that
   [the colour construction](#prop:color-su3-from-g2) already identifies as
   what the $\mathrm{Sym}^2$ gate consumes.

   **Nor is the fibre functor the missing knob.**  The single-fibre category
   admits fibre functors of every dimension $n \ge 2$ \cite{bichon2003}: for
   $E \in \mathrm{GL}_n$ with $\mathrm{tr}(E^{-1}E^{t}) = -q - q^{-1}$ the
   comodule category of the bilinear-form quantum group $B(E)$ is monoidally
   equivalent to that of $\mathcal{O}_q(\mathrm{SL}_2)$, and such $E$ exist
   over $\mathbb{R}$ at $q_0$ for every $n \ge 3$.  So a three-dimensional
   image of $V$ is available.  It does not help, because a fibre functor is
   monoidal and therefore preserves the Clebsch--Gordan rule: under a
   three-dimensional fibre functor $V^{\otimes 3} \cong V_{3/2} \oplus
   V_{1/2} \oplus V_{1/2}$ has dimensions $21 + 3 + 3$, and under a fibre
   functor of any dimension the spin-$0$ summand the decomposition
   $\mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$
   requires is absent from $V^{\otimes 3}$ by parity
.  Dimension is a
   property of the fibre functor; the multiplet structure is a property of
   the category.  This closes the single-fibre reading of Route A --- the
   question *does the category admit inequivalent fibre functors?* is
   answered affirmatively and turns out not to bear on $N = 3$ --- and
   relocates the missing object to the category itself: an object $W$ with
   $\Lambda^3 W \neq 0$, which the categorical volume constraint
   ([Definition](#def:quantum-observable-universe), condition 5) forbids for
   the fundamental.

2. **Hypercharge $Y$.**
   The writhe-to-isospin map $w \mapsto I_3$ is derived.  The
   hypercharge $Y$ is not: the writhe map is falsified as a $Y$
   assignment (proton and neutron share $Y = +1$ while their writhes
   differ).  *Open:* identify a second crossing invariant
   independent of the writhe.
   Battery (exploratory, not wired): of $10{,}000$ helon-style
   assignments, $4$ survive
 --- but that ratio
   carries *no* corroboration, and is not a $2500\!:\!1$ filter.
   It is proved that the spectrum
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
; scope-(a) for
   that reading only.
   The derivation gap is therefore the entire content: whether the
   twist multisets are forced by the categorical braid words (not
   just consistent with them) is the open content of the hypercharge
   conjecture, and nothing else in the battery constrains anything.
   In the split-bundle framing $F = V_2 \oplus W_3^*$ ($z_3 = q^3/[3]_q$)
   of the Standard Model appendix and
   [the flavour-charges remark](#rem:flavor-charge-assignments),
   tracelessness of $\mathrm{diag}(y_2, y_2, y_3, y_3, y_3)$ forces
   $y_3 = -\tfrac{2}{3}y_2$, pinning the exterior-pair doublet hypercharge
   $y_2 + y_3 = +\tfrac{1}{3}$ at $y_2 = 1$ with Killing Weinberg ratio
   $3/8$, and separating $\bar u$ ($-\tfrac{2}{3}$) from $d$ ($-\tfrac{1}{3}$)
   despite their shared crossing sign $-1$.  Hypercharge is thus reduced
   conditionally to the same missing object as item 1: constructing $W_3$
   in the multi-fibre groupoid.

3. **Continuous $G_2$ completion.**
   The discrete skeleton of $\mathrm{SU}(3)_{\mathrm{c}} \subset G_2 =
   \mathrm{Aut}(\mathbb{O})$ is verified
   ($\mathrm{GL}(3, \mathbb{F}_2) \cong \mathrm{PSL}(2,7)$ Fano
   symmetry of the associator), and so is the Lie-algebra level:
   $\mathrm{Der}(\mathbb{O})$ has dimension $14$ and the stabilizer of
   $e_1$ has dimension $8$, matching $\dim S^6 = 14 - 8$.  The continuous Lie-group completion
   --- specifically the coset $S^6 = G_2/\mathrm{SU}(3)_{\mathrm{c}}$ --- not
   constructed here: the continuous Lie group $G_2$ is not available.
   This is an infrastructure obstruction, not a structural one.

4. **Flavour versus colour separation.**
   The octonionic $\mathrm{SU}(3)_{\mathrm{c}}$ is colour.  The eightfold-way
   classification requires flavour $\mathrm{SU}(3)_{\mathrm{f}}$.  Whether these
   are the same, different, or related by a groupoid-level duality
   is open, and **the $\mathrm{Sym}^2$ gate cannot settle it.**

   In particular the gate does not show that the two *cannot* both
   come from the same construction. That it excludes the icosahedral
   triple $T_1$ while the $G_2$ route passes compares **two different
   objects** and establishes only that those two differ, not that one
   construction cannot supply both roles. (The $T_1$ comparison is in
   [the Schur--Weyl proposition](#prop:schur-weyl-eightfold), where it
   is now stated as a proved pass: the octonionic triple is complex type.)

   The failure is structural, not a repairable gap in the inference.
   It is proved that
   at dimension three, passing the gate is equivalent to carrying a
   complex-type irrep.  Any two three-dimensional objects that both
   pass are therefore both complex type, and the gate has returned the
   same verdict for each --- two distinct such objects are
   exhibited.  A flavour triple and a colour
   triple that each pass are, to this gate, indistinguishable.

   What the gate *does* establish is a class exclusion: no real or
   quaternionic construction reaches dimension three through it, so
   $T_1$'s failure is a consequence of its Frobenius--Schur type and
   not a fact about the icosahedron.  Whatever separates flavour from
   colour lies elsewhere --- as it does for the $\mathbb{Z}/3$ grading,
   which
   is likewise shown to be blind to the identification.

   **The two blindnesses are one blindness.**  Both gates read only
   *object-level* data --- a dimension, a Frobenius--Schur type, a
   triality class --- and on that data the two triples coincide: the
   colour triple is the $\mathbb{C}^3$ of
   $\mathrm{Im}(\mathbb{O}) = \mathbb{R}\oplus\mathbb{C}^3$, of complex
   dimension $(7-1)/2 = 3$; the flavour triple is the fundamental with
   Dynkin label $(1,0)$, of Weyl dimension $2\cdot 1\cdot 3/2 = 3$;
   both are complex type with triality $1$.
   This is a class exclusion, and a proved
   one --- **no** gate reading only object data separates
   them, so there is no third such gate to look for.  This is scope-(b),
   with the invariant named: equal data, equal verdict.

   **Where a discriminator can live is item 7 below, not a further
   invariant of the object.**  The obstruction lifts as soon as a gate
   may also read *which Young-symmetry channel of $V^{\otimes 3}$ carries
   the physical state*: colour occupies the totally antisymmetric channel
   $\lambda = (1^3)$, flavour the symmetric $\lambda = (3)$ for the
   decuplet and the mixed $\lambda = (2,1)$ for the octet.  These are
   distinct $S_3$-irreps, and
   a gate is exhibited that tells them apart.  Item 7 already names this data, in the
   form *"colour antisymmetric and spin symmetric force flavour
   symmetric"*; items 4 and 7 are the same question seen from two sides.

   This locates the discriminator; it does not establish one.  The
   channel assignment is an **input**, and item 7 records that the
   chapter derives neither the spin factor nor the colour antisymmetry
   that would supply it.  What is settled is the negative half --- and
   the negative half is what redirects the search.

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

   **This item is where item 4's discriminator lives.**  Item 4 asks
   what separates flavour from colour and shows that no invariant of
   the *object* can; the Young-symmetry channel named here is data
   about the *role*, and
   a gate is exhibited that reads it and does separate them.  So deriving the
   colour-antisymmetry constraint would settle more than the
   selection rule --- it would supply the one input item 4 is missing.

8. **The Gell-Mann--Okubo deviation.**
   The relation $4m_K^2 = 3m_\eta^2 + m_\pi^2$ is *not* a target
   for derivation: it holds identically for any first-order octet
   breaking, whatever the mechanism, as proved in
   [the meson mass-splitting remark](#rem:meson-mass-splitting).  Reproducing it would therefore
   be no evidence for the framework.  An unconstrained second-order
   polynomial in $(I(I+1), Y)$ surjects onto every scalar residual and
   likewise carries no separating power.  Replacing the classical Casimir
   by the parameter-free rational quantum Casimir
   $d_q(I, Y) = [I]_q[I+1]_q - [Y/2]_q^2$ \cite{kleinkreisler1996} yields
   the $(a,b,c)$-free bar-even ratio
   $(4M_K - 3M_\eta - M_\pi)/(M_\pi - M_\eta) = -((q - 1)/(q + 1))^2$,
   equal to $-2.7168 \times 10^{-3}$ at $q_0$.  This predicts the observed
   signs on *both* the pseudoscalar meson octet ($+$) and the baryon octet
   ($-$) without free parameters, while accounting for only $1.21\%$ of
   the $6.43\%$ isospin-averaged meson deviation and $0.82\%$ of the
   $-0.57\%$ baryon deviation.  *Open:* the remaining $\approx 6.3\%$
   meson residual, dominated by $\eta$--$\eta'$ singlet mixing and
   higher-order $\mathrm{SU}(3)_{\mathrm{f}}$ breaking.  The former $\approx 3.3\%$
   comparison against $\dim_q(\text{adjoint})$ remains withdrawn as a
   category error (a dimension is not a mass splitting).

9. **Ocneanu/Markov trace parameter.**
   The Markov trace $\tau$ on $H_n(q)$ involves a second parameter
   $z$ (the trace parameter).  In QOU, $q$ is the substrate parameter
   (observed at the point of observation as $q_0$, not derived from Bring topology).
   Along the Wenzl family $z_r = q^r/[r]_q$, a fibre of quantum dimension
   $[r]_q$ pins $z = z_r$ with nothing left to choose: $V_2$ fixes
   $z_2 = q^3/(q^2+1)$ and a rank-$3$ partner $W_3^*$ fixes
   $z_3 = q^3/[3]_q = q^5/(q^4+q^2+1)$.  The two parameters satisfy
   $z_2(q) - z_3(q) = q^3 / ((q^2+1)(q^4+q^2+1)) \neq 0$ ($0.1634$ at
   $q_0$) and induce non-proportional Ocneanu weight vectors on $H_3(q)$
   ($w_{(1^3)}(q, z_2) = 0$ whereas $w_{(1^3)}(q, z_3) = [3]_q^{-3} \neq
   0$).  *Open:* constructing the categorical rank-$3$ object $W_3$ that
   instantiates the $r = 3$ level (T3f).
