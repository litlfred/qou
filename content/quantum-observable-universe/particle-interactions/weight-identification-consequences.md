**Remark.**
The categorical identification of
[prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification)
is short to state but unifies several threads in the paper.  Three
consequences are worth recording explicitly.

**1.  "Spectral coordinate $w_1$" becomes computable.**  Throughout
the Descartes chapter the phrase *evaluation in spectral coordinates*
refers to the first Lagrange resolvent $w_1$ on Bring's surface ---
an abstract Fourier mode of a complete intersection in $\mathbb{P}^4$.
By the weight identification, every such evaluation is canonically
the same as evaluation of the affine coordinate $x$ on the
hyperelliptic quintic $\mathcal{X}_5 \colon y^2 = x^5 - 1$.  The
latter is an elementary plane-curve coordinate; the former is a
five-term sum on a degree-$120$-symmetric surface.  Both pictures
are valid, but the $\mathcal{X}_5$ picture is dramatically easier
to compute with and to formalise.

**2.  $\mathbb{Z}_5$-isotype dimensions align with $T_{2,3}$ and $T_{2,5}$.**
Under the weight identification, the non-trivial
$\mathbb{Z}_5$-isotypical part of $H^1(\mathcal{X}_5, \mathbb{Q})$ is
the four-dimensional character sum
$\chi_1 \oplus \chi_2 \oplus \chi_3 \oplus \chi_4$
(equivalently, $J(\mathcal{X}_5)$ has complex dimension $2$).
This four-dimensional rational isotype is exactly filled by the
Seifert surface of the Solomon-seal torus knot $T_{2,5}$
(Seifert genus $2$, so $\dim H^1 = 4$ over $\mathbb{Q}$);
a two-dimensional sub-isotype is filled by the trefoil $T_{2,3}$
(Seifert genus $1$).  The representation-theoretic dimensions match
the Seifert dimensions exactly for these two knots --- a
consequence of cyclic representation theory on $\mathcal{X}_5$,
not a phenomenological coincidence.

**3.  "One $\mathrm{U}(1)$ phase tube" is exactly "one cyclic weight observed".**
The collapse of three Descartes color tubes to a single
$\mathrm{U}(1)$ phase tube
([rem:u1-phase-tube](#rem:u1-phase-tube)) reads from the
weight-graded perspective as:
the full non-commutative theory keeps all five Lagrange weights
$\zeta_5^{\,0}, \zeta_5^{\,-1}, \zeta_5^{\,-2}, \zeta_5^{\,-3}, \zeta_5^{\,-4}$
distinguishable as separate observable channels (the trivial weight
plus three colour tubes plus a chiral conjugate, organised by
$\mathrm{SU}(3)$-triality from $S_5$);
the commutative-limit theory keeps only the weight-$(-1)$ channel
visible, identified canonically with $x$ on $\mathcal{X}_5$.
"One tube" thus means *one non-trivial $\mathbb{Z}_5$-weight
observed*, not a vague geometric collapse.

**Applied in existing blocks.**  Two pre-existing blocks have been
updated to cite the present identification where the $w_1$ /
$\mathbb{Z}_5$ structure plays a direct role:
[rem:t211-ideal-annihilation](#rem:t211-ideal-annihilation) gains
a representation-theoretic origin for the $T_{2,3}$ /
$T_{2,5}$ row of its embeddability table, and
[rem:color-tube-constraints](#rem:color-tube-constraints) gains a
commutative-limit specialisation mapping the full $S_5$-symmetric
color system to the single $\mathrm{U}(1)$ tube on
$\mathcal{X}_5$.  Further rewriting of the Descartes chapter to
express "evaluation in spectral coordinates" directly in terms of
$\mathcal{X}_5$ coordinates is deferred to a later pass through
that chapter.
