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

**2.  $T_{2,5}$ as the saturating torus knot is forced by representation theory.**
The Seifert bound of [conj:torus-knot-seifert-bound](#conj:torus-knot-seifert-bound)
admits exactly two saturating witnesses:
$T_{2,3}$ (Seifert genus $1$, strict inequality) and
$T_{2,5}$ (Seifert genus $2$, equality).  Under the weight
identification these are not numerical accidents.  The non-trivial
$\mathbb{Z}_5$-isotypical part of $H^1(\mathcal{X}_5, \mathbb{Q})$ is
the four-dimensional character sum
$\chi_1 \oplus \chi_2 \oplus \chi_3 \oplus \chi_4$
(equivalently, $J(\mathcal{X}_5)$ has complex dimension $2 = g(T_{2,5})$).
$T_{2,5}$ is precisely the torus knot whose Seifert surface fills this
representation; $T_{2,3}$ uses a $2$-dimensional sub-isotype.  Higher
torus knots $T_{r,s}$ with $(r-1)(s-1)/2 \geq 3$ would require
representation-theoretic data that does not exist on
$\mathcal{X}_5$.  The privileged role of the *Solomon-seal* knot
$T_{2,5}$ in the paper's particle spectrum is therefore a
consequence of cyclic representation theory, not a phenomenological
choice.

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

**Targets for follow-up.**  The phrasing "in spectral coordinates"
appears in several existing blocks that predate this identification
(among them $T_{211}$ ideal annihilation, knot factorisation,
Coulomb charge, vertex-algebra relations, and the colour-tube
constraint blocks of the Descartes chapter).  Each could be
rewritten to refer to $\mathcal{X}_5$ directly via the present
identification --- a concrete simplification deferred to a later
pass through those chapters.
