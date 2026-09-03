# The colour cubic is a rank-3 spectral curve — what that closes in the eightfold-way ledger, and what it does not

**Status:** structural finding, no gap closed, two gaps re-stated as one question.
**Date:** 2026-09-03 · **Branch:** `claude/mt7r-archimedean-eval-2026-08-24` · **Beans:** `qou-m3sh`, `t7qv`.
**Prompt:** owner asked how the global left-invariant frame of $\mathrm{PSL}(2,\mathbb{R})$ —
$X$ (geodesic), $Y$ (horocyclic), $V$ (fibre rotation) — connects to the eightfold way, and
whether gaps there can be closed.

## 1. What the frame is, in Lie-algebra terms

$\{X, Y, V\}$ is a basis of $\mathfrak{sl}_2(\mathbb{R})$ adapted to the Iwasawa
decomposition: $X$ is the Cartan (dilation) generator, $Y$ the nilpotent (horocyclic)
generator, $V = E - F$ the compact rotation. It is the split real form of $A_1$. The
eightfold way is $A_2$. Every positive root $\alpha$ of $A_2$ gives an $A_1$ subalgebra —
the $I$-, $U$-, $V$-spin $\mathfrak{su}(2)$'s of Gell-Mann — so an $A_2$ carries **three**
such frames, permuted by the Weyl group $W(A_2) \cong S_3$. That is the whole of the
connection at the level of algebra, and by itself it is not new: the ledger already has
"$H_3(q)$ has Coxeter type $A_2$; $W(A_2) \cong S_3$".

## 2. Where the corpus already has a second $A_2$, unlabelled

The colour cubic

$$
C(X; z) = X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1)
$$

(`QOU.Mass.ColorSpectralCubicGeometry`, `ColorCubicDiscriminantPositive`,
`bring_cubic_monodromy_probe`) is called the *colour spectral curve* with
$\lambda_{SW} = X\,dz$, and `mi-sw-abelianisation-cartan` reads $X$ on one sheet as the
Cartan (Higgs-eigenvalue) component of an $\mathrm{SU}(2)$ connection.

A degree-3 spectral curve $\det(X - \Phi(z)) = 0$ is, by definition, the spectral curve of
a **rank-3** Higgs field $\Phi$; its three sheets are the three eigenvalues of $\Phi$, i.e.
the three weights of the fundamental of $\mathfrak{gl}_3$ — after the trace shift
$X \mapsto X + (z+1)/3$, of $\mathfrak{sl}_3 = A_2$. Chevalley's theorem says the same
thing from the other side: the space of monic cubics is $\mathfrak{h}/W(A_2)$, so the
$z$-line is a curve in $\mathfrak{h}/W$, and the monodromy of the sheets is the Weyl
monodromy of the covering $\mathfrak{h} \to \mathfrak{h}/W$ along that curve. That is
exactly what `bring_cubic_monodromy_probe` computed: transitive $S_3$, every branch point a
transposition, sign character surjective, cut out by the Vandermonde $\sqrt{\Delta}$.

So the corpus has **two** $A_2$'s:

| | Coxeter $A_2$ | Hitchin / Chevalley $A_2$ |
|---|---|---|
| where | $H_3(q)$, three strands | the colour cubic over the Bring chart |
| $W = S_3$ acts on | strands (braid generators) | sheets (Higgs eigenvalues) |
| Cartan | two independent strand-charges | $(X_1, X_2, X_3)$, $\sum = -(z+1)$ |
| the $A_1$ frames | one per adjacent strand pair | one per root, $\mathfrak{sl}_2$ of each pair of sheets |
| corpus label | flavour (eightfold-way chapter) | colour (colour-tube coordinates $c_r, c_g, c_b$) |

The ledger row **"Flavour vs. colour SU(3): open — same, different, or groupoid-dual"**
gets a definite *shape* from this: they are different because they act on different
objects, strands versus sheets, and the question "same or groupoid-dual" is the question
of whether there is a natural map from the strand $S_3$ to the sheet $S_3$. Nothing here
constructs one.

## 3. What the sign character is, on this reading

`prop:baryon-product-from-alt` takes the totally antisymmetric isotype $\mathrm{Alt}^3 =
(1^3)$ as an input, and item 7 asks where the sign representation comes from. On the
Hitchin reading, the sign character of the Weyl monodromy on the three sheets *is* the
$(1^3)$ isotype of $S_3$ acting on the three colour eigenvalues — "the baryon lives in the
sign line" becomes "the baryon is a section of the Vandermonde double cover
$\mathbb{C}(z)(\sqrt{\Delta})$". That is a reformulation with content (it says which
geometric line bundle the colour-singlet condition is), not a derivation: *why* the
physical state is in the sign line still needs a principle. The corpus's own candidate for
that principle is `AlgebraicSubstrate/TwistSignTorsor.lean`: the ribbon twist sign is a
$\mathbb{Z}/2$ monoidal character — fermion parity. Identifying the Weyl sign on the sheets
with the twist-sign torsor would be the derivation; it is not done here, and it should be
stated as the one step item 7 needs.

## 4. Hypercharge, and why the frame does not manufacture it

The ledger says the writhe map gives $I_3$ and is falsified for $Y$ ($p$ and $n$ share
$Y = +1$, writhes differ). In the $A_2$ Cartan, $I_3$ and $Y$ are the two independent
Cartan coordinates; in the frame language $I_3$ is the $X$-type (dilation) datum of the
$I$-spin $A_1$ and $Y$ is the Cartan direction orthogonal to it, i.e. built from the
$U$- and $V$-spin Cartans. For the nucleon doublet $Y = B + S = 1$ carries no information
beyond baryon number; $Y$ only varies once strangeness exists, which is the third flavour
— the $N = 3$ problem. So hypercharge is not a missing invariant on the strands; it is the
$N = 3$ construction seen from the Cartan. The frame supplies the *place* $Y$ would live
(the second Cartan coordinate) and nothing to fill it.

One more thing the corpus already knows fits here. The Reeb–Bring audit (2026-06-01)
found the braid-word operator's eigen-**phases** blind to $p$ vs $n$ and its eigen-**moduli**
distinguishing them. Phases are the $V$-type (rotation) datum; moduli are the $X$-type
(dilation) datum. The frame names the channels the audit measured.

## 5. The real form, again

`ColorCubicDiscriminantPositive` proves $\Delta(z) < 0$ for all real $z$. A cubic with
negative discriminant has one real root and a complex-conjugate pair. So on the real
spacetime axis the colour Higgs field has eigenvalues $(x, w, \bar w)$: it is conjugate
into the **non-split** Cartan of $\mathfrak{sl}_3(\mathbb{R})$, not the diagonal one, and
not the imaginary-diagonal one of $\mathfrak{su}(3)$ either. This is the same
compact-versus-split question the Bring cone link raises
(`2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md`), now on the colour side, and
it is decided by the corpus's own theorem rather than left open: the colour Cartan on the
real axis is neither purely compact nor purely split.

## 6. What is closed, what is not

Closed: nothing in the ledger changes status. Re-stated: "flavour vs colour" is
"strands vs sheets"; "where does the sign come from" is "identify the Weyl sign on the
sheets with the twist-sign torsor"; "hypercharge" is "$N = 3$ seen from the Cartan". The
frame $\{X, Y, V\}$ is the $\mathfrak{sl}_2(\mathbb{R})$ of each root of the colour $A_2$
and names the phase/modulus channels; it does not construct the third flavour, and no
$A_1$ frame can.

Checkable next steps, in order of cost: (i) verify symbolically that the colour cubic's
shifted roots are the weights of a traceless $3 \times 3$ matrix whose $A_2$ discriminant
is $\Delta(z)$ — definitional, but it pins the dictionary; (ii) compute the Weyl-monodromy
sign around each of the six branch points and compare with the twist-sign torsor's
$\mathbb{Z}/2$ on the corresponding strand configuration; (iii) only then ask whether the
strand $S_3$ and the sheet $S_3$ are related by anything but a coincidence of orders.
