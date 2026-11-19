The previous chapter established the knot-particle dictionary: each
observable particle corresponds to a specific braid configuration in the
Iwahori--Hecke algebra $H_n(q)$, and the confinement hierarchy organises
these configurations into shells.  The question this chapter takes up is:
*why do these particles fall into octets and decuplets?*

The candidate answer lies in the representation theory of three-strand
braiding --- but the chapter must open with a warning about the shape of
that answer, because the obvious reading of it is wrong.

**Two different $A_2$s.**
The braid group $B_3$ and its $q$-deformation $H_3(q)$ have Coxeter type
$A_2$: the Coxeter quotient of $B_3$ is $W(A_2) \cong S_3$, permuting the
three *strands*.  This is true, but it is true *by construction* --- the
braid group on $n$ strands has Coxeter type $A_{n-1}$ by definition, so
choosing $n = 3$ is what puts $A_2$ there.  It is not a structural theorem
about the substrate, and nothing is derived from it.

The $A_2$ that the eightfold way needs is a *different* one: the Lie
algebra $\mathfrak{sl}_3$ of flavour $\mathrm{SU}(3)_{\mathrm{f}}$, which in quantum
Schur--Weyl duality \cite{jimbo1986}
([the baryon-multiplet section](#sec:baryon-multiplets)) is
the partner acting
on the *fibre* $V$, and which appears only when $\dim V = N = 3$.  The two
$A_2$s coincide in name --- and in this chapter's diagrams --- solely
because the strand count has been set to $n = 3$ while a fibre dimension $N = 3$ is sought.  Setting $n = 3$ does
not make $N = 3$.

This distinction is the chapter's central honesty constraint, and the
reason [that section](#sec:baryon-multiplets) records the $N = 3$ problem
as the chapter's principal open construction rather than as a solved step: the
single-fibre construction of the
[braiding chapter](#chap:path-integrals-braiding) has exterior square
$\dim \Lambda^2 V = 1$, yielding a quantum form of
$\mathrm{SU}(2)$ with $\dim V = N = 2$, and no choice of $q$ raises it.
Even though the Geer--Patureau-Mirand--Turaev modified trace
($d_{\mathrm{mod}}(1,1,1) \neq 0$) restores the antisymmetric three-strand
$S_3$ sector $S^{(1,1,1)}$ of $H_3(q)$ --- supplying the baryon singlet,
nuclear three-body cumulants, and the axial coupling $g_A$ that bare
Convention D projects out ($y_{(1^3)}(z_D) = 0$) --- a single $N = 2$
fundamental strand still realizes only $\mathfrak{sl}_2$ quantum
Schur--Weyl duality.  Genuine rank-$2$ colour $\mathrm{SU}(3)_{\mathrm{c}}$,
flavour $\mathrm{SU}(3)_{\mathrm{f}}$ octets and decuplets, weak hypercharge
$\mathrm{U}(1)_Y$, and the CKM and PMNS Yukawa mixing parameters remain gated on a
multi-fibre or rank-$2$ HOMFLY-PT $(V_2 \oplus V_3)$ extension.
Every flavour-$\mathrm{SU}(3)_{\mathrm{f}}$ statement below is therefore *conditional
on $N = 3$*, and is marked as such.

[The root-system section](#sec:a2-root-system) derives the $A_2$ root
system from the Hecke
relations of $H_3(q)$ and identifies the hexagonal weight lattice.
[The flavour-representations section](#sec:flavor-representations)
constructs the flavor triplet and
antitriplet from unknot configurations and assigns the charge quantum
numbers (isospin $I_3$, hypercharge $Y$).
[The meson-octet section](#sec:meson-octet) derives the meson octet via
the tensor
decomposition $\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus
\mathbf{1}$, realised through the $\bowtie_K$ product.
[The baryon-multiplet section](#sec:baryon-multiplets) extends to baryons:
$\mathbf{3} \otimes
\mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus
\mathbf{8} \oplus \mathbf{1}$, with the symmetric channel yielding the
decuplet and the Borromean baryon
([Definition](#def:borromean-baryon))
providing the structural realisation.
[The colour-algebra section](#sec:color-algebra) derives the color
$\mathrm{SU}(3)_{\mathrm{c}}$ gauge
algebra from octonionic stabilisation.
[The $q$-deformation section](#sec:q-deformed-eightfold) develops the
$q$-deformation of the
hexagonal weight lattice and connects it to the hyperbolic geometry of
knot complements.
[The dictionary section](#sec:knot-particle-force-dictionary) consolidates
the complete
knot--particle--force dictionary.
[The open-problems section](#sec:eightfold-open-problems) records the open
problems.

**Epistemic tiers.**
Each statement below is marked with one of four tiers, used in the same
sense as in the
[Standard-Model appendix](#app:standard-model):
*proved* (established unconditionally);
*derived* (obtained from framework structure without fitted parameters);
*standard* (a theorem of the ambient mathematics --- Coxeter theory,
Schur--Weyl duality, $\mathrm{SU}(3)$ representation theory --- cited,
not re-derived here, and carrying no QOU content on its own);
*conditional* (a rigorous consequence of a named hypothesis, principally
$N = 3$); and *open* (a precisely identified missing object).

**What this chapter does not do.**
It does not derive flavour $\mathrm{SU}(3)_{\mathrm{f}}$.  The eightfold-way
classification is reproduced *conditionally on $N = 3$*, and $N = 3$ is
not available: the framework supplies $\dim V = 2$.  Most of the
representation theory below is tier *standard* --- correct, and correctly
applied, but true of any $\mathrm{SU}(3)$ and not evidence for the
framework.  What the chapter contributes is the placement of the braid
dictionary against that classification, one derived entry ($I_3$ on the
nucleon doublet), and a sharpened statement of what is missing.  The
consolidated ledger is
[the open-problems section](#sec:eightfold-open-problems).
