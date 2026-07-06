*Proof of (a).* We combine three ingredients.

**Step 1: Observability trivializes $HH^0$.**
The QOU observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ([observability](#def:quantum-observable-universe)) states:

$$
HH^0(\mathcal{U}_q, \mathrm{Ad}) = \mathrm{Ad}^G = 0.
$$

The adjoint representation of a semisimple group lacks invariant vectors; equivalently, $\mathfrak{g}$ has a trivial center.

**Step 2: Frobenius duality relates $HH^0$ and $HH^d$.**
The Frobenius--Hopf self-duality $A \cong A^\vee$ (the non-degenerate pairing from [Frobenius--Hopf data](#def:frobenius-hopf-substrate)) induces Poincare duality on Hochschild cohomology \cite{yekutieli2010}:

$$
HH^n(\mathcal{U}_q, \mathrm{Ad})
 \cong 
HH^{d-n}(\mathcal{U}_q, \mathrm{Ad})^\vee,
\qquad d = \dim G.
$$

This represents Van den Bergh duality for Frobenius algebras. The Frobenius form $\lambda : A \to \mathbf{1}$ trivializes the dualizing bimodule.

**Step 3: Dimension count for $G = \mathrm{SU}(2)$.**
We set $d = \dim \mathrm{SU}(2) = 3$.

See [Table 2](#tbl:qou-obstruction-reduction-table2-data).

We obtain $HH^2 \cong (HH^{d-2})^\vee = (HH^1)^\vee$. The outer derivation space is one-dimensional because the Lusztig integral form $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$ is a one-parameter family. The parameter $q$ acts as the unique deformation direction. Drinfeld's theorem ensures the quantized enveloping algebra is the unique deformation of $\mathcal{U}(\mathfrak{g})$ for simple $\mathfrak{g}$.

Therefore $HH^2 \cong k$. The obstruction space is one-dimensional. $\square$

*Proof of (b).*
The HKR comparison map sends the generator of $HH^2$ to the Euler class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathcal{B})$, which has trace $\chi(A)$ ([QU-to-QOU theorem](#thm:qu-to-qou), item 2). Because $HH^2 \cong k$ is one-dimensional, the scalar $\chi(A)$ determines the entire obstruction. $\square$

*Proof of (c).*
We apply Kummer specialization ([Kummer](#prop:ns-kummer-specialisation)). The class $\kappa_0 \bmod n = 0$ in $H^2(\mathcal{S}, \mathbb{G}_m) / nH^2(\mathcal{S}, \mathbb{G}_m)$ if and only if $n$ divides the trace $\chi(A)$. Equivalently, the motivic Galois character $\chi^{\mathrm{mot}}_A$ is non-trivial at every finite place $p \nmid \chi(A)$ ([motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)). $\square$
