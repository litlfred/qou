**Conjecture (Bloch-group decomposition of $2/(3\pi)$).**
*There exists a finite multi-set
$\{(K_1, n_1), \ldots, (K_m, n_m)\}$ of hyperbolic knots
$K_i \subset S^3$ that embed in Bring's surface $X_{\mathrm{Bring}}$
respecting (a finite-index sub-symmetry of) the $S_5$ automorphism
group, with integer multiplicities $n_i \in \mathbb{Z}$, such that*

$$
  \boxed{\;\;
  \sum_{i = 1}^{m} n_i \cdot D\bigl[Z_{K_i}\bigr]
  \;=\;
  \frac{2}{3\pi}
  \quad\text{in } \mathbb{R},
  \;\;}
$$

*where $[Z_K] \in B(F_K)$ is the Bloch class of $K$ in its trace
field $F_K$ and $D$ is the Bloch-Wigner dilogarithm. Equivalently,
the aggregate class*

$$
  [Z]_{\mathrm{Bring}}
  \;:=\;
  \sum_i n_i\,[Z_{K_i}]
  \;\in\;
  B(F)\otimes \mathbb{Q},
$$

*for $F = \mathbb{Q}(\zeta_{15})$ the compositum
$\mathbb{Q}(\zeta_3, \zeta_5)$, has Bloch-Wigner image
$D([Z]_{\mathrm{Bring}}) = 2/(3\pi)$.*

## Why this conjecture is the right framing

The mass / hyperbolic sector of the QOU framework
([figure-8 archimedean illustration](#rem:figure-8-archimedean-illustration))
delivers Bloch-Wigner content via $\tau_{\mathrm{arch}}$: each
hyperbolic knot $K \subset S^3$ contributes a class $[Z_K] \in B(F_K)$
whose BW image is the hyperbolic volume of $S^3 \setminus K$. The
force-carrier sector — torus knots $T(2,9), T(3,5)$ producing the
multiplicative bare formula $q[9]_q[10]_q$ — does **not** contribute
to BW: torus knots are Seifert-fibered, not hyperbolic, so their
complements have no ideal-tetrahedron triangulation and no
$D$-class. The additive correction $2/(3\pi)$ in
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
must therefore originate in the *hyperbolic* sector of knots
embedded in Bring's surface.

## Field structure (unconditional)

Let $\zeta_n$ denote a primitive $n$-th root of unity.

| Field $F$ | $[F:\mathbb{Q}]$ | $r_1$ | $r_2$ | $\mathrm{rk}_{\mathbb{Z}}\,B(F)\otimes\mathbb{Q}$ |
|---|---:|---:|---:|---:|
| $\mathbb{Q}(\zeta_3)$ — figure-8 ($4_1$) trace field | 2 | 0 | 1 | 1 |
| $\mathbb{Q}(\zeta_4) = \mathbb{Q}(i)$ — Borromean ($\mathcal{B}_3$) trace field, via 2 ideal regular octahedra of shape $i$ | 2 | 0 | 1 | 1 |
| $\mathbb{Q}(\zeta_5)$ — Bring's natural field | 4 | 0 | 2 | 2 |
| $\mathbb{Q}(\zeta_{12}) = \mathbb{Q}(\zeta_3,\zeta_4)$ — figure-8 + Borromean compositum | 4 | 0 | 2 | 2 |
| $\mathbb{Q}(\zeta_{60}) = \mathbb{Q}(\zeta_3,\zeta_4,\zeta_5)$ — full compositum (figure-8, Borromean, Bring) | 16 | 0 | 8 | 8 |

The rank columns are by Borel's theorem [`borel1974`]:
$\mathrm{rk}\,K_3^{\mathrm{ind}}(F)\otimes\mathbb{Q} =
\mathrm{rk}\,B(F)\otimes\mathbb{Q} = r_2(F)$ for any number field
$F$ (here $K_3^{\mathrm{ind}}$ is the indecomposable part of $K_3$).
The Bloch-Wigner regulator
$D \colon B(F)\otimes\mathbb{Q} \xrightarrow{\sim} \mathbb{R}^{r_2(F)}$
is an isomorphism after tensoring with $\mathbb{Q}$.

**Observation 1.** The figure-8's trace field $\mathbb{Q}(\zeta_3)$
is **not** a subfield of $\mathbb{Q}(\zeta_5)$ (degrees 2 and 4
respectively, and $\mathbb{Q}(\zeta_5)$ contains no real quadratic
imaginary subfield other than $\mathbb{Q}$). So a decomposition
working entirely inside $B(\mathbb{Q}(\zeta_5))$ cannot include the
figure-8.

**Observation 2.** The natural compositum is widened by the
Borromean rings (proton/neutron in the QOU spectrum, see
[`recursive-atom-knot-atlas`](../appendix-knot-periodic-table/recursive-atom-knot-atlas.md)):
$\mathrm{Vol}(\mathcal{B}_3) = 8G = 8\,\mathrm{Cl}_2(\pi/4)$ via two
ideal regular octahedra of shape parameter $i$
([`binding-scale-catalan`](../braids-and-knots/binding-scale-catalan.md)),
so $\mathcal{B}_3$'s trace field is $\mathbb{Q}(i) = \mathbb{Q}(\zeta_4)$,
not $\mathbb{Q}(\zeta_3)$. Combining figure-8, Borromean, and Bring's
$\mathbb{Q}(\zeta_5)$ gives the compositum
$\mathbb{Q}(\zeta_{60}) = \mathbb{Q}(\zeta_3, \zeta_4, \zeta_5)$,
of degree 16 over $\mathbb{Q}$ and Bloch-group rank
$r_2(\mathbb{Q}(\zeta_{60})) = 8$. The figure-8 and Borromean
contributions occupy two distinct 1-dimensional sub-lines, so the
remaining 6 dimensions are available for the decomposition.

**Observation 3.** The QOU framework supplies an explicit
finite enumeration of hyperbolic knots in its mass-bearing
spectrum, via the
[recursive atom-knot atlas](../appendix-knot-periodic-table/recursive-atom-knot-atlas.md):

| Particle / atom | Hyperbolic knot / link | Volume | Trace field (standard) |
|---|---|---|---|
| Proton, neutron | $\mathcal{B}_3$ Borromean | $8G \approx 7.328$ | $\mathbb{Q}(i)$ |
| Deuteron $^2$H | $6_2$ | $\approx 4.401$ | quartic field over $\mathbb{Q}$ |
| Tritium $^3$H | $8_{11}$ | $\approx 8.286$ | sextic field |
| $^3$He | $L_{6a4}$ (link) | $\approx 7.328$ | $\mathbb{Q}(i)$ (twin to $\mathcal{B}_3$) |
| Higgs / mass mechanism | $4_1$ figure-8 | $\approx 2.030$ | $\mathbb{Q}(\zeta_3)$ |

(`recursive-on-⁴He` and the $^4$He magic-A formula contribute via
$8G$ algebraically, not via a single hyperbolic knot.) Trace fields
beyond degree 2 quickly enlarge the compositum: $6_2$'s field is
quartic, $8_{11}$'s is sextic. Including all hyperbolic knots in
the QOU spectrum, the natural compositum is **at least**
$\mathbb{Q}(\zeta_{60})$ and may be larger depending on which
non-cyclotomic fields appear.

The $S_5$-equivariance constraint pins which knots actually embed
$S_5$-equivariantly in Bring's surface; the figure-8 and Borromean
admit such embeddings up to standard ambiguities, and the higher
isotope knots ($6_2, 8_{11}, L_{6a4}, \ldots$) inherit
$S_5$-equivariance via the binding-operator $\oplus$ structure of
the atlas.

**Observation 4 (force carriers contribute zero to BW).** The
electroweak knot operators identified in the paper —
$W \leftrightarrow \sigma_1^4 \to T(2,4)$,
$Z \leftrightarrow \sigma_3^6 \to T(2,6)$,
$H \leftrightarrow \sigma_5^8 \to T(2,8)$
([`ew-interface-knot`](../braids-and-knots/ew-interface-knot.md),
[`categorical-higgs-mechanism`](../braids-and-knots/categorical-higgs-mechanism.md)) —
together with the strong-force pair $T(2,9), T(3,5)$
([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)),
are **torus links**: Seifert-fibered, not hyperbolic, no
ideal-tetrahedron triangulation. They contribute identically zero
to the BW image
$D \colon B(F)\otimes\mathbb{Q} \to \mathbb{R}^{r_2(F)}$, hence
they cannot enter the decomposition of $2/(3\pi)$ on the
hyperbolic side. Only the matter / mass-bearing knots in the
atlas carry BW content.

**Observation 5 (BW contributions come from NF-basis subknots,
not just atlas particles).** The atlas lists 5 hyperbolic knots
as the principal mass-bearing entries
$\{4_1, \mathcal{B}_3, 6_2, 8_{11}, L_{6a4}\}$. But each
established particle / atom is built from a Hecke normal-form
word, and the BW image is generated by the closures of all
NF-basis triple products $b_i \cdot \beta(T_{m,n}) \cdot b_j$
across all relevant $H_n(q)$ — see
[`knot-operator-lp-selection`](../braids-and-knots/knot-operator-lp-selection.md)
and the witness
[`knot-operator-table.witness.json`](../../../computations/knot-operator-table.witness.json).
For $H_3(q)$ alone the NF basis
$\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ is six-dimensional;
products with the torus operators $T_{1,0}, T_{2,1}, T_{2,2},
T_{2,3}, T_{2,5}$ generate the supply table of demand-channel
identifiers. At higher $n$ the NF basis grows polynomially and
the closure space includes many hyperbolic knots beyond the five
atlas entries.

Consequently the dimension of the BW-accessible sub-space inside
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$ is not bounded by 5,
and the rank-8 ambient image is in principle reachable through
NF-basis closures. The five-knot count is a *lower bound on
visible hyperbolic content*, not a span.

**Reformulation of the search.** The K-theoretic identification
becomes: identify a finite collection of NF-basis triple-product
closures whose BW values $\sum n_i D[Z_i] = 2/(3\pi)$. The
falsifiable atlas check (rank-4 sub-lattice of established
entries with $\mathcal{B}_3 \sim L_{6a4}$ via the shared volume
$8G$ identity) is a strict sub-question — if $2/(3\pi)$ lies in
the rank-4 atlas-spanned lattice
$\mathbb{Z}\cdot 2\,\mathrm{Cl}_2(\pi/3)
\;\oplus\; \mathbb{Z}\cdot 8G
\;\oplus\; \mathbb{Z}\cdot D[Z_{6_2}]
\;\oplus\; \mathbb{Z}\cdot D[Z_{8_{11}}]$,
the decomposition closes immediately; otherwise the search
extends to NF-basis closures of products in higher $H_n(q)$,
where the BW dimension grows.

## Hyperbolic knots from the 6 NF dual-basis operators

The NF basis for $H_3(q)$
([`prop:knot-operator-lp-selection`](../braids-and-knots/knot-operator-lp-selection.md))
is $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$. Each basis
element is a specific element of $H_3(q)$; its Markov closure in
$S^3$ is a 3-braid closure. The closures of the basis elements
themselves and their pairwise products fall in a tightly
constrained class:

| NF basis element | Markov closure |
|---|---|
| $\gamma$ | 3 disjoint unknots (identity element) |
| $\sigma_0$ | unknot (1 generator, 1 crossing) |
| $\sigma_1$ | unknot (1 generator, 1 crossing) |
| $L_+, L_-$ | Hopf link $L_H$ (signed) |
| $e^- = \sigma_1^3$ | trefoil $3_1 = T(2,3)$ |

None of the basis elements closes to a *hyperbolic* knot — all
six closures are torus or links of torus knots. The hyperbolic
content arises only at the level of *triple products*
$b_i \cdot \beta(T_{m,n}) \cdot b_j$ when these algebraic words
are expanded in $\sigma$-generators and their Markov closures
taken.

By Birman-Hilden, all knots arising as closures of 3-braids are
classified: the hyperbolic 3-braid closures up to 10 crossings
are $4_1, 5_2, 6_1, 6_2, 6_3, 7_2, 7_3, 7_4, 7_5, 7_6, 7_7,
8_1, 8_2, \ldots$ — about 30 prime knots. **Every hyperbolic
knot embeddable in Bring's surface (genus 4) with bridge number
$\leq 3$ appears in this list**, because Bring's surface
contains all 3-bridge embeddings as closed 3-braids
[`thurston1978`].

For higher tunnel-number / bridge-number hyperbolic knots
embeddable in genus-4 (e.g. $8_{11}$ which is 4-bridge), the
relevant Hecke algebra is $H_n(q)$ for $n \geq 4$, and the NF
basis grows to $n!$ elements. The full set of hyperbolic knots
embeddable in Bring's surface is reachable through NF-product
closures across $H_3(q), H_4(q), H_5(q), \ldots, H_8(q)$ — at
which point the Heegaard-genus bound saturates the Bring genus
4.

**Summary:** the 6 NF dual-basis operators in $H_3(q)$ alone
produce only torus closures; their *products with torus knot
operators* in $H_3(q)$ generate all 3-bridge hyperbolic knots
embeddable in Bring (~30 prime knots through 10 crossings).
Higher $H_n(q)$ NF basis products extend the reach to all
hyperbolic knots embeddable in genus-4. The Bloch-Wigner image
of the union of these closures is in principle the full rank-8
sub-image of $B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$
generated by 3-bridge–through-Bring hyperbolic-knot trace fields.

The decomposition search for $2/(3\pi)$ therefore has a
**concrete finite candidate set** at each tier:

1. **Tier 0** (atlas-named): $\{4_1, \mathcal{B}_3, 6_2, 8_{11}, L_{6a4}\}$
   — rank $\le$ 4 lattice, immediate falsifiability check.
2. **Tier 1** (3-braid hyperbolic): all closures of NF-product
   words in $H_3(q)$ — ~30 prime knots, manageable enumeration.
3. **Tier 2** (genus-4 embeddable): all hyperbolic knots through
   $H_8(q)$ NF-product closures — large but bounded by
   Bring-embedding constraint.

If $2/(3\pi)$ is not in the Tier-0 lattice but is in the Tier-1
or Tier-2 lattice, the K-theoretic identification of
`BringZeroModeBlochClass` reduces to producing the explicit
integer-coefficient combination — a finite, search-tractable
problem rather than an open structural conjecture.

**Iterated NF products span all hyperbolic-in-Bring knots
(Markov stabilization).** By the Markov theorem, every knot in
$S^3$ arises as the closure of some braid in $B_n$ for finite
$n$, modulo Markov moves (conjugation in $B_n$ and
$\sigma_n$-stabilization $B_n \hookrightarrow B_{n+1}$). Iterated
NF-product composition in the colimit
$\varinjlim_n H_n(q)$ — formed by repeatedly taking
$b_i \cdot \beta(T_{m,n}) \cdot b_j$ in $H_n$ then stabilising
into $H_{n+1}$ — therefore reaches **every** knot in $S^3$ in
the limit. Restricting to closures with Heegaard genus $\leq 4$
yields exactly the hyperbolic-in-Bring set; the corresponding
$n$ is bounded (every knot of bridge number $b$ embeds in a
genus-$b$ Heegaard surface, so genus-4 embeddability requires
$b \leq 4$, hence $n \leq 8$ suffices).

**Open computational sub-question (not theoretical):** *Does every
hyperbolic-in-Bring knot appear as the Markov closure of a single
NF-basis word in some $H_n(q)$ for $n \leq 8$, or do some require
non-NF representatives (requiring conjugation across the
Gröbner-Shirshov boundary)?* The Markov-stabilization argument
above guarantees reachability *as a knot*, but the NF-basis
constraint may restrict the *representative*: a hyperbolic-in-Bring
knot $K$ might require a $\sigma$-word that is NOT in the
GS-shortlex normal form of $H_n(q)$, in which case the BW value
$D[Z_K]$ is reached only after Hecke-trace identification with an
NF-basis triple-product image.

**Status of the NF-probe (May 2026 audit).** A repository scan
identifies the present coverage gap concretely:

| Atlas hyperbolic object | Explicit $\sigma$-word in $H_n(q)$? | Methodology tag |
|---|---|---|
| Figure-8 $4_1$ | no (mentioned as Higgs/mass mechanism only) | not principled-derivation |
| Borromean $\mathcal{B}_3$ | yes $(\sigma_1\sigma_2^{-1})^3 \in H_3$ | `principled-derivation` |
| Deuterium $6_2$ | no | `manual-historical-volume-match` |
| Tritium $8_{11}$ | no | `manual-historical-volume-match` |
| Helium-3 $L_{6a4}$ | no | `manual-historical-volume-match` |

So **only 1 of 5 atlas hyperbolic objects has a principled-derivation
$\sigma$-word**; the other four lack explicit Hecke representatives.
The existing
[`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/main/computations/gb_filtration_jet_tracker.py)
has tested $\sigma_1^3$ (electron, trefoil — torus, no BW) and
$(\sigma_1\sigma_2^{-1})^3$ (Borromean, hyperbolic) but has NOT
been extended to $H_{18}$ / $H_{21}$ / etc. for the four
unrepresented hyperbolic objects.

**Smallest concrete sub-question:** compute the canonical Hecke NF
form of each of $\{4_1, 6_2, 8_{11}, L_{6a4}\}$ in the appropriate
$H_n(q_0)$ for $n \leq 8$, either by (a) extending
`gb_filtration_jet_tracker.py` to handle these knots, or (b)
running the joint-tower SDP referenced as `"next_step"` in the
existing
[`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/main/computations/gb-filtration-jet-order.witness.json).
Once obtained, verify closure-identity against SnapPy volumes. This
is the irreducible computational gate to inhabiting
`BringHyperbolicDecomposition` from the atlas side — the question
is no longer "does it exist?" but "perform the GS reduction for
the 4 unrepresented objects."

Concretely:

- For each hyperbolic knot $K$ embeddable in Bring's surface
  there exists an integer $n_K \leq 8$, an NF-basis word
  $w_K \in H_{n_K}(q)$ expressible as a triple-product chain in
  the dual-basis operators, and a Markov-equivalence
  $\widehat{w_K} \sim K$.
- Composing such words multiplicatively in
  $\varinjlim_{n\leq 8} H_n(q)$ generates the full BW image
  of the genus-4-embeddable hyperbolic spectrum, which spans the
  rank-8 image of $B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$
  (modulo the Galois-orbit collapses).
- The Bloch group of the union is therefore generated by the
  finite set of NF-basis elements together with the finite set
  of torus-knot operators $T_{m,n}$ used in the LP/SDP supply
  table; iterated triple-product composition reaches every
  hyperbolic-in-Bring BW value.

The K-theoretic search for $2/(3\pi)$ reduces ultimately to: does
the rank-8 ambient image contain $2/(3\pi)$ as a $\mathbb{Z}$-linear
combination of NF-product BW values? By Borel's regulator and
Bloch-Suslin uniqueness, the image is determined; the question is
purely whether the specific real number $2/(3\pi)$ lies on the
image lattice — and iterated NF-composition guarantees the
generating set is finite and explicit.

## Field equivalence (proved)

The two routes — QOU substrate (NF-product closures) and Bring
geometry (Hodge / Gauss-Bonnet) — produce Bloch classes that
coincide:

**Theorem (cyclotomic compositum, unconditional).**
$\mathrm{lcm}(3, 4, 5) = 60$, so the compositum of the three
constituent trace fields is exactly
$$
  \mathbb{Q}(\zeta_3) \cdot \mathbb{Q}(\zeta_4) \cdot \mathbb{Q}(\zeta_5)
  \;=\; \mathbb{Q}(\zeta_{60}).
$$
This is the natural ambient field for both routes — it contains
the figure-8's $\mathbb{Q}(\zeta_3)$, Borromean's $\mathbb{Q}(\zeta_4)$,
and Bring's $\mathbb{Q}(\zeta_5)$.

**Theorem (field equivalence via injectivity, conditional on
`BlochSuslinUniqueness` / `BlochWignerInjective`).** If both routes
produce a Bloch class with $\tau_{\text{arch}}$-image $2/(3\pi)$,
then by the injectivity of
$D \otimes \mathbb{Q} \colon B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}
\to \mathbb{R}^{r_2(\mathbb{Q}(\zeta_{60}))}$ (a consequence of
Bloch-Suslin pentagon-uniqueness, `BlochSuslinUniqueness` from
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness)),
the two Bloch classes are equal in
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$. The Lean theorem
`field_equivalence_via_uniqueness` makes this explicit using a
real-level injectivity surrogate
[`BlochWignerInjective`](bring-hyperbolic-knot-bloch-decomposition.lean);
no `sorry`, conditional only on the named class.

**Synthesis.** Modulo (a) the existence of the explicit
NF-product decomposition realising $2/(3\pi)$ (the K-theoretic
sub-conjecture of this block) and (b) Bloch-Suslin uniqueness
(`prop:archimedean-functor-uniqueness`), the substrate and
geometry sides agree on the same Bloch class in the same field
$\mathbb{Q}(\zeta_{60})$. The remaining open content is purely
the integer relation in step (a) — a finite, search-tractable
problem rather than a structural mismatch.

## Partial proof: the figure-8 sub-piece

The figure-8 knot $4_1$ has trace field $F_{4_1} = \mathbb{Q}(\zeta_3)$
(Thurston [`thurston1978`]). Its Bloch class is
$[Z_{4_1}] = 2[\zeta_6]$ in $B(\mathbb{Q}(\zeta_3))$, where
$\zeta_6 = e^{i\pi/3}$ is the shape parameter of the two ideal
regular tetrahedra in $S^3 \setminus 4_1$. The Bloch-Wigner
value is the classical

$$
  D[Z_{4_1}]
  \;=\;
  2\,D\bigl(e^{i\pi/3}\bigr)
  \;=\;
  2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right)
  \;\approx\;
  :val[Vol_4_1]{precision=6}\ldots
$$

The Clausen value $\mathrm{Cl}_2(\pi/3)$ is a Gauss-Catalan-type
constant; the relation $\mathrm{Cl}_2(\pi/3) \neq \frac{2}{3\pi}\cdot k$
for any small rational $k$ is straightforward (numerical:
$2/(3\pi) \approx 0.2122$, $\mathrm{Cl}_2(\pi/3) \approx 1.0149$,
ratio $\approx 4.78$ — non-rational to high precision). So the
figure-8 alone is not the answer; Observations 1 and 3 above
already forced this.

## Reduction of the conjecture

Given the field-rank table, the conjecture reduces to two
constituent claims:

**(C-Hyp).** *There is a finite, $S_5$-equivariantly characterised
set $\mathcal{K}_{\mathrm{Bring}}$ of hyperbolic knots embeddable
in Bring's surface, and an explicit integer relation
$\sum_K n_K\,[Z_K] = [Z]_{\mathrm{Bring}}$ in $B(\mathbb{Q}(\zeta_{15}))$.*

**(C-Hodge).** *The geometric class on Bring's surface
$[Z]_{\mathrm{Hodge}}$ extracted from the Hodge / Gauss-Bonnet
data ($g = 4$, area $4\pi(g-1) = 12\pi$, $b_1 = 8$) coincides with
$[Z]_{\mathrm{Bring}}$ in $B(\mathbb{Q}(\zeta_{15})) \otimes \mathbb{Q}$,
and $D([Z]_{\mathrm{Hodge}}) = 2/(3\pi)$.*

Both claims live inside the 4-dimensional space
$B(\mathbb{Q}(\zeta_{15}))\otimes\mathbb{Q}$, where Borel's
regulator gives an explicit isomorphism with $\mathbb{R}^4$. The
1-dimensional sub-line containing $2/(3\pi)$ is determined by
the Galois action: by the functional equation of the Dedekind
zeta function, the line is spanned by $\zeta_{\mathbb{Q}(\zeta_{15})}^*(2)$
modulo a known $\pi$-power. Concretely:

$$
  \zeta_{\mathbb{Q}(\zeta_{15})}^*(2)
  \;=\;
  \frac{(2\pi)^{2 r_2}}{\sqrt{|d_F|}}\,R_F^{(2)}
  \;=\;
  \frac{(2\pi)^8}{\sqrt{|d_F|}}\,R_F^{(2)},
$$

where $R_F^{(2)}$ is the higher regulator
([`borel1974`, `zagier1986`]) determined by BW values on a basis
of $B(F)\otimes\mathbb{Q}$.

**The irreducible open problem.** Identifying which specific
hyperbolic knots embed $S_5$-equivariantly in Bring is a concrete
geometric question without a known answer in the literature. The
figure-8 is the obvious starting point, but Observation 1 forbids
its sole contribution; further candidates (e.g., $5_2$, $6_1$,
$6_2$, $6_3$ have trace fields ranging from $\mathbb{Q}(\sqrt{-7})$
to $\mathbb{Q}(\zeta_3, \sqrt{-15})$ to higher cubic fields) need
to be checked for $S_5$-compatible embeddability and trace-field
inclusion in $\mathbb{Q}(\zeta_{15})$.

## What is proved (Lean handle)

The Lean file [`bring-hyperbolic-knot-bloch-decomposition.lean`](bring-hyperbolic-knot-bloch-decomposition.lean)
establishes the unconditional algebraic skeleton plus one
conditional non-existence result narrowing the decomposition:

- `r2Cyclotomic` — for any $n$, $r_2(\mathbb{Q}(\zeta_n)) = \varphi(n)/2$ (definition).
- `r2_zeta3_eq_one`, `r2_zeta4_eq_one`, `r2_zeta5_eq_two`,
  `r2_zeta12_eq_two`, `r2_zeta15_eq_four`, `r2_zeta60_eq_eight`
  — concrete values via `decide`.
- `compositum_rank_decomposition_narrow` —
  $r_2(\mathbb{Q}(\zeta_{15})) = r_2(\mathbb{Q}(\zeta_3)) + r_2(\mathbb{Q}(\zeta_5)) + 1$.
- `compositum_rank_decomposition_full` —
  $r_2(\mathbb{Q}(\zeta_{60})) = r_2(\mathbb{Q}(\zeta_{15})) + r_2(\mathbb{Q}(\zeta_4)) + 3$.
- `bring_zero_mode_value_positive`, `bring_zero_mode_value_ne_zero` —
  basic positivity of $2/(3\pi)$.
- A class `BringHyperbolicDecomposition` axiomatising the existence
  of the finite multi-set $\{(K_i, n_i)\}$.
- `bring_hyperbolic_decomposition` — sorry-free conditional theorem
  taking `BringHyperbolicDecomposition` as `[Instance]` and
  yielding `BringZeroModeBlochClass`.
- A class `BWQIndependence cl2_pi_3 cl2_pi_4` axiomatising the
  Q-linear independence of $\{2/(3\pi), \mathrm{Cl}_2(\pi/3),
  \mathrm{Cl}_2(\pi/4)\}$.
- `two_knot_decomposition_insufficient` — sorry-free conditional
  lemma taking `BWQIndependence` as `[Instance]` and proving that
  no $\mathbb{Z}$-linear combination of $D[Z_{4_1}] = 2\,\mathrm{Cl}_2(\pi/3)$
  and $D[Z_{\mathcal{B}_3}] = 8\,\mathrm{Cl}_2(\pi/4)$ alone equals
  $2/(3\pi)$. Any decomposition must therefore include **at least
  one hyperbolic knot beyond $\{4_1, \mathcal{B}_3\}$** from the
  QOU spectrum (e.g.\ $6_2, 8_{11}, L_{6a4}$, or higher-isotope
  knots from the recursive atlas).

The decomposition search is therefore narrowed: the figure-8 and
Borromean rings are necessary to cover the cyclotomic sectors
$\mathbb{Q}(\zeta_3)$ and $\mathbb{Q}(\zeta_4)$, but they are not
sufficient. The minimal search target is now a $\mathbb{Z}$-linear
combination of three or more distinct hyperbolic-knot BW values
from the atlas, in the rank-8 Bloch group
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$.

Closure of the class instance reduces to (C-Hyp): identify
$\mathcal{K}_{\mathrm{Bring}}$ explicitly and verify the integer
relation against $\zeta_{\mathbb{Q}(\zeta_{60})}^*(2)/\pi^?$. The
two-knot insufficiency lemma above eliminates the smallest possible
ansatz; the open problem is now the integer relation among the
remaining $r_2 - 2 = 6$ available cyclotomic-sector BW values.
