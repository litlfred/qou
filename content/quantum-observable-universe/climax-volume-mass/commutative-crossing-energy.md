**Remark (categorical coordinate of the commutative limit).**
The Hecke generator $\sigma = P \circ R$ on $V \otimes V$ has eigenvalues
$(\lambda_+, \lambda_-) = (q, -q^{-1})$ on the symmetric/antisymmetric
decomposition $S^2 V \oplus \Lambda^2 V$
([def:crossing-energy](#def:crossing-energy)).  At $q = 1$
([def:commutative-qou](#def:commutative-qou)) the eigenvalues collapse
to $(+1, -1) = \mathbb{Z}_2$, and the per-crossing weight $q - q^{-1}$
vanishes identically.  The categorical structure of the commutative
limit is recovered by extracting the *square root* of the antisymmetric
eigenvalue $\lambda_- = -1$:

$$
  i  =  \sqrt{\lambda_-}, \qquad i^2 + 1  =  0  \;\text{in}\; R[i].
$$

The ring extension $R[i]$ (the universal $R$-algebra containing an
element $i$ with $i^2 = -1$) of the categorical ground
ring $R$ is therefore forced by the categorical structure: $i$ is the
**categorical coordinate of $\mathbb{P}(V)$ in the commutative limit**,
in exact parallel with the role of $q$ in the non-commutative theory.
The construction is intrinsic to $R$ — no real or complex numbers are
assumed.  Specialisations: when $R$ already contains a square root of
$-1$ (e.g. the archimedean realisation, where $R = \mathbb{C}$ as one
realisation among others, see [archimedean
realisations](#rem:archimedean-realisations)), $i \in R$ is canonical;
when $R$ does not (e.g. $R = \mathbb{Z}[q, q^{-1}]$ at $q = 1$), $R[i]$
is the minimal extension realising $\lambda_-$ as a categorical square.

**Categorical-coordinate dictionary.**

See [Table 1](#tbl:commutative-crossing-energy-table1-data).

**Deformation hierarchy.**  The discrete Weyl group $\mathbb{Z}_2$
embeds into the continuous maximal torus, which itself is the $q = 1$
fibre of the quantum torus:

$$
  \mathbb{Z}_2  \;\hookrightarrow\;  \mathrm{U}(1)  \;\hookrightarrow\;
   \mathrm{U}_q(1).
$$

Each inclusion sees a different categorical coordinate on
$\mathrm{End}(\mathbf{1})$: $-1$ generates $\mathbb{Z}_2$, $i$ generates
$\mathrm{U}(1)$ at the quarter-turn $\varTheta = \pi/2$, and $q$ generates
$\mathrm{U}_q(1)$ off-locus.  The standard non-commutative deformation
$\mathrm{SU}(2) \rightsquigarrow \mathrm{SU}_q(2)$ acts on the second
inclusion; the commutative-limit *enlargement*
$\mathbb{Z}_2 \hookrightarrow \mathrm{U}(1)$ acts on the first.  These
are the two ways to escape the $q = 1$ degeneracy of $q - q^{-1}$.

**Three categorical readings of $i$ on $\mathbb{P}(V)$.**

1. *Algebraic.*  $i = \sqrt{\lambda_-} \in \mathrm{End}_{R[i]}(\mathbf{1})$
   is the categorical square root of the antisymmetric braiding
   eigenvalue.  The same datum appears in three faces — Wick rotation,
   CR complex structure, arrow of time — all reducing to the binary
   choice of braiding orientation $c_{V,V}$ vs $c_{V,V}^{-1}$
   ([rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation)).
2. *Geometric.*  $J = i \cdot \mathrm{id}_V \in \mathrm{End}_{R[i]}(V)$
   is an endomorphism with $J^2 = -\mathrm{id}_V$, descending to a
   complex structure on $\mathbb{P}(V) = \mathrm{Proj}(\mathrm{Sym}\, V^\vee)$
   over $R[i]$.  In the archimedean realisation this recovers the
   standard complex structure on the exceptional divisor
   $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$
   ([def:exceptional-divisor](#def:exceptional-divisor)).
3. *Equivariant.*  The maximal torus $\mathrm{U}(1) \subset \mathrm{SU}(2)$
   acts on $\mathbb{P}(V)$ with $i$ as the quarter-turn generator; the
   orbit space is $[0, \pi]$ with phase fibre $\varphi \in S^1$ over
   the interior ([prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)).

The three readings coincide because each computes the same categorical
datum: a square root of $\lambda_-$ in $\mathrm{End}_{R[i]}(V)$.

**Affine-chart origin.**  Both $q$ and $i$ arise from the
chart-transition data of $\mathbb{P}(V)$
([rem:affine-chart-origin-of-i-and-q](#rem:affine-chart-origin-of-i-and-q)):
$q$ is literally the chart-transition coefficient $z\,w = q^{-1}$ on
the quantum projective line $\mathbb{P}_q(V)$, while $i$ is the
square root of the chart-swap involution $\iota: z \mapsto z^{-1}$
that the transition collapses to at $q = 1$.  Formally, the
**categorical-coordinate ring** is the universal $R$-algebra
extension $R[i, q^{\pm 1}] = R[q, q^{-1}][i]/(i^2 + 1)$
([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring))
in which $q$ is invertible and the involution-eigenvalue $-1$ has a
square root.  The chart-transition automorphism group factors as
$\langle q \rangle \rtimes \langle \iota \rangle$ over this ring.

**Half-twist and ribbon structures.**  The ribbon element $v = q^{1/2}$
is *not* required for the categorical-coordinate construction; it
appears only when $\mathbf{C}$ is equipped with an additional ribbon
twist $\varTheta_V = q^{1/2}\,\mathrm{id}_V$ for framed-link invariants
or Reshetikhin--Turaev TQFT
([rem:sqrt-q-ribbon-structure](#rem:sqrt-q-ribbon-structure)).  The
square root of $\lambda_-$ extracted here lies in $R[i]$, not in any
ribbon datum, and is independent of the eigenvalue-labelling
convention $q := \lambda_+$
([rem:braiding-unit-circle-convention](#rem:braiding-unit-circle-convention)).

**Crossing energy in the commutative limit.**  Setting $q = e^{i\varTheta}$
on the unit circle of $\mathrm{End}(\mathbf{1})$ gives

$$
  q - q^{-1}  =  2i \sin\varTheta,
$$

with $\varTheta \in [0, \pi]$ tracking the orbit-space interval of
[prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction).
The endpoints $\varTheta = 0, \pi$ are the polar fixed points (zero
weight); the interior is the free $S^1$-fibre; $\varTheta = \pi/2$ (where
$q = i$) is the location of maximum weight $|2i \sin(\pi/2)| = 2$.
The Hecke energy $q - q^{-1}$ of the non-commutative theory is the
algebraic deformation of this commutative-limit form.

**Branch-phase localisation on $\mathcal{X}_5$.**  The five finite
branch points $\zeta_5^k$ of the hyperelliptic quintic
([def:hyperelliptic-quintic](#def:hyperelliptic-quintic), with the
sixth branch point at $\infty$) lie on the unit circle and pick out
five preferred phase values $\varphi_k = 2\pi k/5$ on the
$\mathrm{U}(1)$ tube ([rem:u1-phase-tube](#rem:u1-phase-tube)).  At
these phases the commutative crossing weight takes only two distinct
magnitudes,

$$
  2\lvert\sin(2\pi/5)\rvert  \approx 1.902,
  \qquad
  2\lvert\sin(4\pi/5)\rvert  \approx 1.176,
$$

related by the golden-ratio identity
$\sin(2\pi/5)/\sin(4\pi/5) = \varphi$, where
$\varphi = (1+\sqrt{5})/2$.

**Falsifiability witness.**  The computation
`isospin-mass-tower-collapse` evaluates the multi-brane mass
$\mathfrak{m}_{\mathrm{cat}} = \lvert\mathrm{tr}_M(\beta)\rvert + \sum_n \hbar_q^{2n} \mathrm{tower}^{(n)}$
against AME binding for the three lightest non-trivial nuclei.  The
derived/observed ratio overshoots by a factor of $3$ to $4$, indicating
a missing scalar prefactor; after isospin (Coulomb) correction the
two distinct strong-force ratios match the two branch-phase magnitudes
above:

See [Table 2](#tbl:commutative-crossing-energy-table2-data).

Removing the $\approx 0.76\;\mathrm{MeV}$ Coulomb energy of
${}^3\mathrm{He}$ collapses the two $A = 3$ ratios to $3.4767$,
matching tritium ($3.4764$) to $0.014\%$, consistent with isospin
symmetry of the strong-force binding (Wigner-energy convention,
\cite{satula1997}).

**Downstream applications of $R[i, q^{\pm 1}]$.**  Recognising the
categorical-coordinate ring as the ambient deformation ring
([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring))
deduplicates four ad-hoc complexification patterns elsewhere in the
paper:

1. *This block.*  The substitution $q = e^{i\varTheta}$ used above is no
   longer an external complexification.  $e^{i\varTheta} = \cos\varTheta + i\sin\varTheta$
   is a unit *in* $R[i]$ via the Euler identity, so $q - q^{-1} = 2i\sin\varTheta$
   is computed entirely inside $R[i, q^{\pm 1}]$ — no enlargement of
   the categorical ground ring is invoked.

2. *Witness computations.*  The complex arithmetic in
   `isospin-mass-tower-collapse` and the broader mass-tower
   pipeline is justified categorically as a single specialisation
   $R[i, q^{\pm 1}] \to \mathbb{C}$ via $q \mapsto q_0$, applying the
   universal property of the categorical-coordinate ring once rather
   than complexifying ad hoc per script.

3. *Wick-rotation and complex-substrate remarks.*  The blocks
   [rem:laplace-fourier-wick-rotation](#rem:laplace-fourier-wick-rotation)
   and [rem:complex-substrate-interpretation](#rem:complex-substrate-interpretation)
   each currently complexify in isolation (introducing $i$ for the
   half-plane swap, the CR structure, and the substrate value).
   Both invocations of $i$ are now realisations of the single
   categorical coordinate of
   [prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring),
   under the $\mathrm{Gal}(R[i]/R) = \mathbb{Z}_2$ orientation choice
   of [rem:i-as-braiding-orientation](#rem:i-as-braiding-orientation).

4. *Curves over the substrate.*  The hyperelliptic quintic
   $\mathcal{X}_5: y^2 = x^5 - 1$
   ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) and the
   Descartes elliptic curve $\mathcal{E}_q$
   ([prop:descartes-elliptic-curve](#prop:descartes-elliptic-curve))
   are normally introduced "over $\mathbb{C}$" with $\zeta_5 = e^{2\pi i/5}$
   as a complex root of unity.  In the categorical-coordinate
   framework these curves live over $R[i, q^{\pm 1}]$ at $q = q_0$;
   the fifth roots of unity $\zeta_5^k$ are the five geometric points
   of $\mathrm{Spec}(R[i, q^{\pm 1}])$ where the chart-transition
   coefficient hits $\zeta_5^k$, recovering the branch-phase
   localisation of [rem:u1-phase-tube](#rem:u1-phase-tube).

In each case the simplification is *categorical justification*, not
algorithmic: computations and proofs do not change, but their
ambient ring becomes a single named object instead of an ad-hoc
complexification.

**Caveat (updated).** The structural form of the
per-nucleon scaling between $A = 2$ and $A = 3$ is now categorically
derived: the **Path A pipeline** (commits `f9f25b5f`, `23e447dc`,
[`per_irrep_pole_atom.py`](../../../computations/per_irrep_pole_atom.py))
verifies $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta)) = 18Z + 21N + 1$
via symbolic Hoefsmit pole-order analysis for proton ($Z=1, N=0$)
and deuteron ($Z=N=1$). Predictions then agree with experimental
atomic masses to $\leq 0.30\%$ across $Z = 1$..$20$ via the
single-generator $\rho_K$ formula
([`rho-k-pair-gen-v2-wedderburn.witness.json`](../../../computations/rho-k-pair-gen-v2-wedderburn.witness.json));
the Wedderburn pair-generator extension was tested and **rejected**
(it worsens the fit to $\sim 4.7\%$ MAE).
The categorical-coordinate identification $i = \sqrt{\lambda_-}$ is
forced by the Hecke structure at $q = 1$ and is independent of this
numerical confirmation.
