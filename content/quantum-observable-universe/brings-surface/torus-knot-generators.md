*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The Euler characteristic $\chi(A) = -6$ of the Bring's surface is
the reason torus knots serve as the generators of the particle
spectrum. Because the Bring's surface has genus $g = 4$
(from $\chi = 2 - 2g = -6$), there is a hard upper bound on
which torus knots can be localized in the fibre: any $T_{m,n}$
whose Seifert genus exceeds $4$ cannot embed. This
constraint selects a finite, enumerable generator set
$\mathcal{G}$ ([knot-particle generation](#def:knot-particle-generation))
whose cardinality is entirely determined by $\chi$.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\chi(A) = -6$ (Descartes universe). The torus knot $T_{m,n}$
with $\gcd(m,n) = 1$ and $m < n$ embeds into the Seifert genus-$g$
surface of $A$ only if the Seifert genus satisfies

$$
  g(T_{m,n}) =  \frac{(m-1)(n-1)}{2}  \leq  g(A) =  4.
$$

The constraint $(m-1)(n-1) \leq 8$ admits exactly six coprime pairs
with $m \geq 2$, tabulated in
[Table: Torus-knot generators](#tbl:torus-knot-generators-table-data).
Together with the unknot $T_{1,0} = 0_1$ (genus $0$), the generator
set has $|\mathcal{G}| = 7$.

**Genus bound from $\chi(A) = -6$.**
The Bring's surface $\Sigma_4$ has genus $g = 4$ and Euler
characteristic $\chi = 2 - 2g = -6$. A knot $T_{m,n}$ localized
in the fibre $\mathcal{S}_c$
([localized knot](#def:localized-knot)) inherits a Seifert surface
that must embed in the genus-$4$ handlebody provided by $\Sigma_4$.
The Seifert genus of $T_{m,n}$ is $(m-1)(n-1)/2$, so
embeddability requires $(m-1)(n-1) \leq 2g = 8$.

**Physical interpretation.**

1. **Lepton generations.** Charged leptons are $T_{2,3}$
 (electron), $T_{2,5}$ (muon), $T_{2,7}$ (tau) at Reeb degrees
 $\deg\alpha_V = 1, 2, 3$. Only the first two are
 $S_5$-equivariant
 ([prop:s5-equivariant-torus-knots](#prop:s5-equivariant-torus-knots));
 the tau embeds topologically but breaks its $\mathbb{Z}_7$
 symmetry. $T_{2,9}$ saturates $g = 4$ also symmetry-broken, and
 $T_{2,11}$ is genus-excluded --- so no fourth generation.

2. **Quark sector.** The $(3,n)$-family generators $T_{3,4}$ and
 $T_{3,5}$ are $H^{0,1}$ force carriers
 ([cohomological embedding](#prop:cohomological-embedding)):
 $T_{3,4}$ encodes Hopf-squared color binding, while $T_{3,5}$
 mediates the weak interaction. The three-strand meridional
 winding $m = 3$ of these torus knots resonates with the three
 coral tubes
 ([color tube interpretation](#rem:color-tube-interpretation)):
 each meridional strand threads one color fiber.

3. **Saturation.** The seventh generator $T_{2,9}$ at genus $4$
 exactly saturates the Bring's surface. Beyond this, new particle
 types require either a higher-genus QOU (different $\chi$) or
 composite construction via the linking operations.

4. **Hyperbolic knots are derived.** The figure-eight $4_1$ (Higgs
 boson), the three-twist $5_2$, and all other hyperbolic
 knots in the dictionary are *not* generators. They arise from
 Skein crossing changes applied to linked torus-knot
 configurations, inheriting nonzero hyperbolic volume — and
 hence nonzero bare mass — from the linking process.

**Remark on the cutoff.**
The bound $N(\chi) = 1 - \chi = 1 - (-6) = 7$ on the number of
nontrivial generators is not accidental: it equals the number of
handles ($g = 4$) of Bring's surface plus the three independent
Seifert genus values ($1, 2, 3, 4$) available within those handles.
The recursive brane tower
([recursive brane tower](#def:recursive-brane-tower)) does not
increase the genus — it refines the blow-up structure within the
existing handles — so the generator count is stable across all
brane levels.
