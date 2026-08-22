*Proof of (a).* Three ingredients combine:

**Step 1: Observability kills $HH^0$.**
The QOU axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([observability](#def:quantum-observable-universe)) is the statement

$$
HH^0(\mathcal{U}_q, \mathrm{Ad}) = \mathrm{Ad}^G = 0.
$$

The adjoint representation of a semisimple group has no invariant
vectors (equivalently: $\mathfrak{g}$ has trivial center).

**Step 2: Frobenius duality relates $HH^0$ and $HH^d$.**
The Frobenius--Hopf self-duality $A \cong A^\vee$
(the non-degenerate pairing from
[Frobenius--Hopf data](#def:frobenius-hopf-substrate)) induces a
Poincaré duality on Hochschild cohomology
\cite{yekutieli2010}:

$$
HH^n(\mathcal{U}_q, \mathrm{Ad})
 \cong 
HH^{d-n}(\mathcal{U}_q, \mathrm{Ad})^\vee,
\qquad d = \dim G.
$$

This is the Van den Bergh duality for Frobenius algebras:
the dualizing bimodule is trivialized by the Frobenius form
$\lambda : A \to \mathbf{1}$.

**Step 3: Dimension count for $G = \mathrm{SU}(2)$.**
With $d = \dim \mathrm{SU}(2) = 3$:

See [Table 2](#tbl:qou-obstruction-reduction-table2-data).

The key: $HH^2 \cong (HH^{d-2})^\vee = (HH^1)^\vee$. The
outer derivation space is one-dimensional because the Lusztig
integral form $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$
is a **one-parameter** family — $q$ itself is the unique
deformation direction. There are no other independent deformation
parameters (this is a theorem of Drinfeld: the quantized
enveloping algebra is the unique deformation of
$\mathcal{U}(\mathfrak{g})$ for simple $\mathfrak{g}$).

Therefore $HH^2 \cong k$: the obstruction space is
one-dimensional. $\square$

*Proof of (b).*
The HKR comparison map sends the generator of $HH^2$ to the
Euler class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathcal{B})$,
whose trace is $\chi(A)$
([QU-to-QOU theorem](#thm:qu-to-qou), item 2).
Since $HH^2 \cong k$ is one-dimensional, the entire obstruction
is determined by the single scalar $\chi(A)$. $\square$

*Proof of (c).*
This is the Kummer specialisation
([Kummer](#prop:ns-kummer-specialisation)): $\kappa_0 \bmod n = 0$
in $H^2(\mathcal{S}, \mathbb{G}_m) / nH^2(\mathcal{S}, \mathbb{G}_m)$
iff $n$ divides the trace $\chi(A)$. Equivalently, the motivic
Galois character $\chi^{\mathrm{mot}}_A$ is non-trivial at every
finite place $p \nmid \chi(A)$
([motivic perpetual obstruction](#conj:motivic-perpetual-obstruction), proved via Route A: prime-ideal collapse, $C = a_0(-1) + 2 \cdot a_1(-1)$). $\square$
