The previous chapter established the knot-particle dictionary: each
observable particle corresponds to a specific braid configuration in the
Iwahori--Hecke algebra $H_n(q)$, and the confinement hierarchy organises
these configurations into shells.  The question this chapter settles is:
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
algebra $\mathfrak{sl}_3$ of flavour $\mathrm{SU}(3)$, which in quantum
Schur--Weyl duality (\S\ref{sec:baryon-multiplets}) is the partner acting
on the *fibre* $V$, and which appears only when $\dim V = N = 3$.  The two
$A_2$s coincide in name --- and in this chapter's diagrams --- solely
because we have set $n = 3$ and would like $N = 3$.  Setting $n = 3$ does
not make $N = 3$.

This distinction is the chapter's central honesty constraint, and the
reason \S\ref{sec:baryon-multiplets} records the $N = 3$ problem as the
chapter's principal open problem rather than as a solved step: the
single-fibre construction of
Chapter~\ref{chap:braids-and-knots} yields a quantum form of
$\mathrm{SU}(2)$, with $\dim V = 2$, and no choice of $q$ raises it.
Every flavour-$\mathrm{SU}(3)$ statement below is therefore *conditional
on $N = 3$*, and is marked as such.

\S\ref{sec:a2-root-system} derives the $A_2$ root system from the Hecke
relations of $H_3(q)$ and identifies the hexagonal weight lattice.
\S\ref{sec:flavor-representations} constructs the flavor triplet and
antitriplet from unknot configurations and assigns the charge quantum
numbers (isospin $I_3$, hypercharge $Y$).
\S\ref{sec:meson-octet} derives the meson octet via the tensor
decomposition $\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus
\mathbf{1}$, realised through the $\bowtie_K$ product.
\S\ref{sec:baryon-multiplets} extends to baryons: $\mathbf{3} \otimes
\mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus
\mathbf{8} \oplus \mathbf{1}$, with the symmetric channel yielding the
decuplet and the Borromean baryon (Definition~\ref{def:borromean-baryon})
providing the structural realisation.
\S\ref{sec:color-algebra} derives the color $\mathrm{SU}(3)$ gauge
algebra from octonionic stabilisation.
\S\ref{sec:q-deformed-eightfold} develops the $q$-deformation of the
hexagonal weight lattice and connects it to the hyperbolic geometry of
knot complements.
\S\ref{sec:knot-particle-force-dictionary} consolidates the complete
knot--particle--force dictionary.
\S\ref{sec:eightfold-open-problems} records the open problems.
