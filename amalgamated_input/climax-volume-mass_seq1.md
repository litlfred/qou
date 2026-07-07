<!-- FILE_START: crossing-energy-intro.md -->
The previous section converted the $R$-matrix into a global energy for a closed strand. We now localise that energy at the points where strands cross. Each crossing has a sign and a weight, and the weights are forced on us by the Hecke relation rather than chosen by hand; the consequence is a per-crossing decomposition that splits into a strong baseline and an electromagnetic correction.

The section opens with Definition: Crossing energy of a knot composite, which assigns the weights $(q, -q^{-1})$ to positive and negative crossings and traces them back to the eigenvalues of the Hecke generator $T = P \circ R$. The worked Example: Crossing energy and binding in the trefoil carries the definition through a familiar case, and the remark on the Remark: Categorical coordinate of the commutative limit records how $i = \sqrt{\lambda_-}$ appears as the natural complex structure on the antisymmetric eigenspace. The structural pivot is Definition: Coulomb charge of a knot composite, which extracts the antisymmetric half $Q(\mathfrak{H}) = \tfrac{1}{2}(n_+ - n_-)$ of the crossing count and reads off the decomposition $\mathfrak{E}_{\mathrm{cross}} = \text{strong baseline} + Q \cdot (q - q^{-1})$. The two propositions Proposition: Crossing asymmetry and per-crossing Coulomb correction and Proposition: Skein relation $L_+ - L_- = (q - q^{-1})\,L_0$ is bar-antisymmetric then close the loop, showing that the asymmetric piece transforms correctly under the bar involution $q \mapsto q^{-1}$. The next section, **Lagrange Resolvents and $q$-Deformed Kinematics**, takes the Coulomb-charge decomposition as the starting point for the discrete Fourier transform on the cyclic subgroup $C_5$ and reads off the kinematic observables from there.
<!-- FILE_END: crossing-energy-intro.md -->

<!-- FILE_START: crossing-energy.md -->
Let $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a composite
of knots linked by a link $\mathcal{L}$, with braid word
$\beta \in B_n$ representing the linking.  The **crossing energy**
of $\mathfrak{H}$ is

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing } (L_+), \\
    -q^{-1} & \text{negative crossing } (L_-),
  \end{cases}
$$

where $q$ is the substrate parameter
([substrate parameter](#def:substrate-parameter)) and the sign
convention follows the Skein relation

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

The crossing energy measures the net Skein weight of the composite:
positive $\mathfrak{E}_{\mathrm{cross}}$ indicates repulsion dominates,
negative indicates binding dominates.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: crossing-energy.md -->

<!-- FILE_START: crossing-energy-categorical-origin.md -->
**Remark (crossing weights are Hecke eigenvalues, not postulates).**

The per-crossing weights $(q, -q^{-1})$ of the [crossing
energy](#def:crossing-energy) are not chosen as an energetic penalty
laid on top of a topological framework.  They are the **two
eigenvalues of the Hecke generator**
$T = P \circ R \colon V \otimes V \to V \otimes V$ acting on the
symmetric/antisymmetric decomposition, and they are forced by the
rigid monoidal structure:

1. *Rigidity fixes the $R$-matrix determinant.*  Dualisability of
   $V$ together with the categorical volume constraint
   ([volume constraint](#def:quantum-observable-universe)) requires
   the braiding $R = c_{V,V}$ to satisfy
   $\det(R|_{V \otimes V}) = 1$, with eigenvalues $(q, q^{-1})$ on
   $S^{2} V \oplus \Lambda^{2} V$.
2. *The Hecke generator carries the transposition sign.*  The
   Hecke generator is $T = P \circ R$, where $P$ is the swap.
   Since $P|_{\Lambda^{2} V} = -\mathrm{id}$, composition flips the
   sign on the antisymmetric summand, giving $T$-eigenvalues
   $(q, -q^{-1})$ with $\det(T) = -1$ --- exactly the Hecke minimal
   polynomial $(T - q)(T + q^{-1}) = 0$
   ([eigenvalue extraction](#prop:braiding-eigenvalue-extraction)).
3. *Crossing weights are eigenvalues, not postulates.*  Assigning
   a positive crossing $L_{+}$ the weight $q$ and a negative
   crossing $L_{-}$ the weight $-q^{-1}$ is precisely the action
   of $T$ on a symmetric-channel input and $T^{-1}$ on an
   antisymmetric-channel input.  The sum
   $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})$ is therefore a trace
   of $T^{\pm 1}$-eigenvalues along the braid, dictated by the
   categorical structure.
4. *Gröbner--Shirshov resolution.*  When $\mathfrak{H}$ is reduced
   to Gröbner--Shirshov normal form
   ([nuclear normal form](#prop:nuclear-groebner-reduction)), each
   crossing contributes its $T$-eigenvalue exactly once; the net
   $\mathfrak{E}_{\mathrm{cross}}$ is the resulting Laurent
   polynomial in $q$, read off the normal form.  Removing any of
   these weights would violate duality and break the Hecke
   relation.

This quantity is computed entirely from the $R$-matrix braiding
([R-matrix](#rem:r-matrix-braiding)) of
$\mathcal{U}_q(\mathfrak{su}(2))$ acting on the tensor product
of constituent representations.
<!-- FILE_END: crossing-energy-categorical-origin.md -->

<!-- FILE_START: crossing-energy-trefoil.md -->
We evaluate the crossing energy
([crossing energy](#def:crossing-energy)) for the trefoil knot and
then explain how binding arises in hadrons.

**Single crossing energy.**
Each crossing in a knot diagram carries Skein weight $q$ (positive
crossing) or $-q^{-1}$ (negative crossing).  For a positive crossing,
the energy contribution is

$$
  \mathfrak{E}_{\mathrm{cross}}^{(+)} = q,
  \qquad
  \mathfrak{E}_{\mathrm{cross}}^{(-)} = -q^{-1}.
$$

The net energy of a single positive crossing minus a single negative
crossing is $q - q^{-1}$, which is the coefficient appearing in the
Skein relation $T - T^{-1} = q - q^{-1}$.

**Trefoil: three positive crossings.**
The standard diagram of the trefoil $\tau(2,3)$ has three positive
crossings.  Its total crossing energy is

$$
  \mathfrak{E}_{\mathrm{cross}}(\tau(2,3))
  =  3q.
$$

At the substrate parameter $q \approx 1.110$:

$$
  \mathfrak{E}_{\mathrm{cross}}(\tau(2,3))
   \approx  3 \times 1.110
  =  3.330.
$$

This is positive, reflecting the fact that the trefoil is a single
knot (not a composite) — there is no linking to provide negative
binding energy.

**Binding in composites.**
A hadron $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ is a
composite whose linking $\mathcal{L}$ introduces additional crossings
between constituent knots.  Mutual crossings between distinct
components can contribute *negative* energy (from negative crossings
in the linking braid word), so the total crossing energy of a
composite is

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\sum_{i} \mathfrak{E}_{\mathrm{cross}}(K_i)}_{\text{self-crossings (positive)}}
  + 
  \underbrace{\mathfrak{E}_{\mathrm{cross}}(\mathcal{L})}_{\text{mutual crossings (can be negative)}}.
$$

The composite is *bound* when the total is negative:
$\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) < 0$.  This means the mutual linking
energy overcomes the individual knot crossing costs — the composite
is energetically favorable relative to the separated constituents.

**Proton binding.**
The proton ([proton as Borromean hadron](#ex:hadron-proton)) consists
of three quarks linked in a Borromean configuration.  The Borromean
linking contributes enough negative mutual crossing energy to make
$\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$, which is why the
proton is a stable bound state: disassembling it into free quarks
would require adding energy equal to
$|\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p})|$.
<!-- FILE_END: crossing-energy-trefoil.md -->

<!-- FILE_START: commutative-crossing-energy.md -->
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
<!-- FILE_END: commutative-crossing-energy.md -->

<!-- FILE_START: branch-phase-mass-tower-witness.md -->
**Remark (branch-phase localisation and the mass-tower falsifiability witness).**

**Branch-phase localisation on $\mathcal{X}_5$.**  The five finite
branch points $\zeta_5^k$ of the hyperelliptic quintic
([def:hyperelliptic-quintic](#def:hyperelliptic-quintic), with the
sixth branch point at $\infty$) lie on the unit circle and pick out
five preferred phase values $\varphi_k = 2\pi k/5$ on the
$\mathrm{U}(1)$ tube ([rem:u1-phase-tube](#rem:u1-phase-tube)).  At
these phases the commutative crossing weight
([crossing energy](#def:crossing-energy)) takes only two distinct
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

**Caveat (updated).** The structural form of the
per-nucleon scaling between $A = 2$ and $A = 3$ is now categorically
derived: the **Path A pipeline** (commits `f9f25b5f`, `23e447dc`,
[`per_irrep_pole_atom.py`](../../../computations/per_irrep_pole_atom.py))
verifies $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta)) = 18Z + 21N + 1$
via symbolic Hoefsmit pole-order analysis for proton ($Z=1, N=0$)
and deuteron ($Z=N=1$). Predictions then agree with experimental
atomic masses to $\leq 0.30\%$ across $Z = 1$..$20$ via the
single-generator $\rho_K$ formula
([`rho-k-pair-gen-v2-wedderburn.witness.json`](../../../computations/_deprecated/rho-k-pair-gen-v2-wedderburn.witness.json),
the now-deprecated probe witness recording both this single-generator
baseline and the rejected pair-generator extension);
the Wedderburn pair-generator extension was tested and **rejected**
(it worsens the fit to $\sim 4.7\%$ MAE).
The categorical-coordinate identification $i = \sqrt{\lambda_-}$ is
forced by the Hecke structure at $q = 1$ and is independent of this
numerical confirmation.
<!-- FILE_END: branch-phase-mass-tower-witness.md -->

<!-- FILE_START: categorical-coordinate-ring-dedup.md -->
**Remark ($R[i, q^{\pm 1}]$ as the ambient deformation ring).**

**Downstream applications of $R[i, q^{\pm 1}]$.**  Recognising the
categorical-coordinate ring as the ambient deformation ring
([prop:categorical-coordinate-ring](#prop:categorical-coordinate-ring))
deduplicates four ad-hoc complexification patterns elsewhere in the
paper:

1. *This block.*  The substitution $q = e^{i\varTheta}$ used in the
   [commutative-limit remark](#rem:commutative-crossing-energy) is no
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
<!-- FILE_END: categorical-coordinate-ring-dedup.md -->

<!-- FILE_START: coulomb-charge.md -->
Let $\mathfrak{H}$ be a knot composite with braid word $\beta$.  Write
$n_+(\beta)$ and $n_-(\beta)$ for the number of positive and
negative crossings in $\beta$.  The **Coulomb charge** of $\mathfrak{H}$ is

$$
  Q(\mathfrak{H}) =  \tfrac{1}{2}\bigl(n_+(\beta) - n_-(\beta)\bigr).
$$

The crossing energy ([crossing energy](#def:crossing-energy))
decomposes as

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\tfrac{1}{2}(n_+ + n_-)(q + q^{-1})}_{\text{baseline (strong)}}
  + 
  \underbrace{Q(\mathfrak{H}) \cdot (q - q^{-1})}_{\text{Coulomb correction}}.
$$

The first term is symmetric in $q \leftrightarrow q^{-1}$ and
represents the strong binding; the second is antisymmetric and
vanishes at $q = 1$.  The Coulomb charge $Q(\mathfrak{H})$ governs the
magnitude and sign of the electromagnetic correction:

- $Q(\mathfrak{H}) > 0$: net positive crossings, repulsive Coulomb contribution.
- $Q(\mathfrak{H}) = 0$: electromagnetically neutral.
- $Q(\mathfrak{H}) < 0$: net negative crossings, attractive Coulomb contribution.

The ratio of Coulomb to strong contributions is
$\tanh(\ln q) \approx 0.104$ at $q = q_0$.
<!-- FILE_END: coulomb-charge.md -->

<!-- FILE_START: coulomb-strong-ratio-q-rational.md -->
**Proposition (Coulomb/strong ratio as a q-rational).**

*For every real $q > 0$ (the substrate-anchor regime,
$\operatorname{Im}(q) = 0$ at the archimedean place),*

$$
  \tanh(\ln q) \;=\; \frac{q - q^{-1}}{q + q^{-1}} \;=\; \frac{q^2 - 1}{q^2 + 1}.
$$

*In particular, the Coulomb/strong ratio from $\operatorname{def:coulomb-charge}$,
which is the analytic value $\tanh(\ln q_0)$, equals the q-rational
expression $(q_0^2 - 1)/(q_0^2 + 1)$ at the substrate anchor — they are the
SAME object, not two different choices.*

## Significance

`def:coulomb-charge` introduces the Coulomb-to-strong ratio as $\tanh(\ln q)$.
This proposition records that the analytic and the algebraic forms coincide
identically over real $q > 0$, removing any potential ambiguity about whether
the framework uses a "classical-$\tanh$" vs a "$q$-deformed $\tanh_q$"
realization at the substrate anchor.

The forms are equal because $\exp(\ln q) = q$ for $q > 0$, so

$$
  \tanh(\ln q)
  \;=\; \frac{e^{\ln q} - e^{-\ln q}}{e^{\ln q} + e^{-\ln q}}
  \;=\; \frac{q - q^{-1}}{q + q^{-1}}
  \;=\; \frac{q^2 - 1}{q^2 + 1}
  \quad\text{(multiply numerator and denominator by $q$).}
$$
<!-- FILE_END: coulomb-strong-ratio-q-rational.md -->

<!-- FILE_START: skein-crossing-asymmetry-prop.md -->
The Skein relation weights positive crossings by $q$ and negative
crossings by $q^{-1}$:

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

For $q > 1$, the per-crossing repulsive Coulomb correction relative to
a mixed-charge baseline is

$$
  \delta_{\mathrm{Coulomb}}
  =  q -  \tfrac{1}{2}(q + q^{-1})
  =  \tfrac{1}{2}(q - q^{-1})
   >  0,
$$

and the ratio of the antisymmetric (Coulomb) to symmetric (strong)
Skein weights is

$$
  \frac{q - q^{-1}}{q + q^{-1}}
  =  \tanh(\ln q).
$$

At $q = 1$ the asymmetry vanishes; at $q \to \infty$ the ratio
approaches $1$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: skein-crossing-asymmetry-prop.md -->

<!-- FILE_START: skein-crossing-asymmetry.md -->
The $R$-matrix braiding
([R-matrix](#rem:r-matrix-braiding)) introduces a fundamental
asymmetry between positive and negative crossings: the Skein
relation

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0
$$

weights positive crossings by $q$ and negative crossings by
$q^{-1}$.  Since $q > 1$, positive crossings contribute *more*
to the Skein polynomial than negative ones.  This asymmetry is
the topological origin of electromagnetic repulsion.

**Emergent Coulomb repulsion.**
For a hadron $\mathfrak{H}$ with Coulomb charge $Q(\mathfrak{H})$
([Coulomb charge](#def:coulomb-charge)), the crossing energy
([crossing energy](#def:crossing-energy)) decomposes into a
symmetric (strong) baseline and an antisymmetric (Coulomb)
correction.  The per-crossing repulsive correction between
composites of the same charge relative to a mixed-charge
baseline is

$$
  \delta_{\mathrm{Coulomb}}
  =  q -  \tfrac{1}{2}(q + q^{-1})
  =  \tfrac{1}{2}(q - q^{-1})
  > 0.
$$

**Unification of strong and electromagnetic interactions.**
Electromagnetic repulsion is *not* a separate force in the QOU
framework.  It is a **phase asymmetry** in the same Skein
polynomial that encodes the strong binding.  Both interactions
arise from the $R$-matrix braiding of
$\mathcal{U}_q(\mathfrak{su}(2))$, with $q$ controlling the
relative strength:

- The strong binding is proportional to
  $\tfrac{1}{2}(q + q^{-1})$ (the baseline Skein weight).
- The electromagnetic repulsion is proportional to
  $\tfrac{1}{2}(q - q^{-1})$ (the crossing asymmetry).

Their ratio is

$$
  \frac{\text{Coulomb}}{\text{Strong}}
  =  \frac{q - q^{-1}}{q + q^{-1}}
  =  \tanh\!\left(\ln q\right).
$$

At $q = 1$ (classical limit), the asymmetry vanishes and the
electromagnetic interaction disappears.  At $q \to \infty$
(deep-quantum regime), the ratio approaches $1$ and the two
interactions become comparable.

The specific assignment of Coulomb charges to protons and
neutrons — and the consequences for nuclear stability — require
the Descartes universe ($\chi = -6$) and are developed in
Chapter 6.
<!-- FILE_END: skein-crossing-asymmetry.md -->

<!-- FILE_START: skein-bar-antisymmetry.md -->
**Proposition (Bar-antisymmetry of the Skein relation).**
The Hecke--Skein relation

$$
  L_+ - L_-  =  (q - q^{-1})\,L_0
  \tag{S}
$$

in the Iwahori--Hecke algebra $H_n(q)$ is **antisymmetric** under
the bar involution

$$
  \overline{\,\cdot\,} \colon
  (L_+,\,L_-,\,L_0,\,q)
  \;\longmapsto\;
  (L_-,\,L_+,\,L_0,\,q^{-1}).
$$

That is, applying $\overline{\,\cdot\,}$ to both sides of (S) yields
$-1$ times (S):

$$
  \overline{L_+ - L_-}  =  L_- - L_+
   =  -\,(L_+ - L_-),
  \qquad
  \overline{(q - q^{-1})\,L_0}
   =  (q^{-1} - q)\,L_0
   =  -\,(q - q^{-1})\,L_0.
$$
<!-- FILE_END: skein-bar-antisymmetry.md -->

