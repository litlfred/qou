The **$q$-Casimir element** is the distinguished central element of the
quantum group $\mathcal{U}_q(\mathfrak{su}(2))$ (cf.
[def:quantum-su2](#def:quantum-su2)) whose eigenvalue on the spin-$j$
irreducible encodes the categorical $q$-angular momentum.

**Definition.**
Inside $\mathcal{U}_q(\mathfrak{su}(2))$ with generators $E, F, K,
K^{-1}$ and parameter $q$ satisfying $q^2 \neq 1$ (so that
$q - q^{-1}$ is invertible), the **(normalised) $q$-Casimir element**
is

$$
  C_q  =  F E  +  \frac{q\,K + q^{-1} K^{-1} - (q + q^{-1})}
                       {(q - q^{-1})^2}.
$$

The subtraction of $(q + q^{-1})$ in the numerator is the standard
normalisation (Kassel VI.4): it ensures the eigenvalue vanishes on
the trivial representation and has a finite classical limit $q \to 1$.
Using the commutation relation
$[E, F] = (K - K^{-1})/(q - q^{-1})$, the element is equivalently

$$
  C_q  =  E F  +  \frac{q^{-1}\,K + q\,K^{-1} - (q + q^{-1})}
                        {(q - q^{-1})^2}.
$$

The element is **central**: it commutes with each generator, i.e.
$C_q E = E C_q$, $C_q F = F C_q$, and $C_q K = K C_q$.

**Action on the spin-$j$ representation.**
On the $(2j+1)$-dimensional highest-weight module $V_j$ of
$\mathcal{U}_q(\mathfrak{su}(2))$, the central element acts as the
scalar

$$
  C_q \big|_{V_j}  =  [j]_q\,[j+1]_q\,\mathrm{id}_{V_j},
$$

with $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ the symmetric $q$-number.
This scalar is the **$q$-Casimir eigenvalue**; the downstream block
[def:q-angular-momentum](#def:q-angular-momentum) specialises it to
$J_q^2(K) = [j]_q\,[j+1]_q$, the $q$-angular momentum of a knot.
In the classical limit $q \to 1$ the eigenvalue becomes $j(j+1)$,
the eigenvalue of the usual Casimir $C = FE + \tfrac12 H(\tfrac12 H + 1)$.

**Role in the categorical framework.**
Centrality of $C_q$ realises it as an endomorphism of the identity
functor on $\mathbf{Rep}(\mathrm{SU}_q(2))$ — equivalently, a natural
transformation $C_q \colon \mathrm{id} \Rightarrow \mathrm{id}$ whose
component at each simple object $V_j$ is
$[j]_q[j+1]_q \cdot \mathrm{id}_{V_j}$.  In the rigid monoidal setting
this is the categorical counterpart of the angular-momentum-squared
operator.

**Terminology.** The $q$-Casimir *element* — the quantum analogue of
Casimir's invariant for $\mathfrak{su}(2)$ — is unrelated to the
Casimir *effect*, the attractive vacuum force between closely spaced
conducting boundaries; the two share only their eponym. The QOU
treatment of the Casimir effect is the $\varepsilon$-vacuum
conjecture
[`conj:casimir-epsilon-vacuum`](#conj:casimir-epsilon-vacuum).
