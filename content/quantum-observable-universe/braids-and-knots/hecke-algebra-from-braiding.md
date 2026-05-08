The Iwahori--Hecke algebra in which all subsequent Gröbner--Shirshov normal-form
computations take place is *not* an algebra with a free parameter.
It is the quotient of the braid-group algebra by the minimal
polynomial of the categorical braiding.

Concretely, the braiding eigenvalue extraction
([eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
shows that $c_{V,V}$ has eigenvalues $(q, -q^{-1})$ on the
decomposition $V \otimes V = S^2 V \oplus \Lambda^2 V$.
Applying the fibre functor $\tau$ gives the endomorphism
$T = \tau(c_{V,V})$ satisfying the Hecke relation

$$
  (T - q)(T + q^{-1}) =  0,
$$

where $q \in \mathrm{End}(\mathbf{1}) \cong k^{\times}$ is the
braiding eigenvalue — the same $q$ that parametrises the substrate
family $d_q$ ([substrate parameter](#def:substrate-parameter)).

The Iwahori--Hecke algebra on $n$ strands is therefore

$$
  H_n(R, q) =  k[B_n] \big/
  \bigl\langle (\sigma_i - q)(\sigma_i + q^{-1})  \big| 
  i = 1, \ldots, n{-}1 \bigr\rangle,
$$

and the parameter $q$ is a **categorical datum** — determined by
the braiding of $(\mathbf{C}, A, \tau)$, not chosen freely.
Every Laurent polynomial $c_w \in \mathbb{Z}[q, q^{-1}]$ appearing
in a Gröbner--Shirshov normal form
([nuclear normal form](#prop:nuclear-groebner-reduction)) inherits
its $q$ from this categorical source.  The per-crossing weights
$(q, -q^{-1})$ that define the crossing energy
([crossing energy](#def:crossing-energy)) are precisely the two
eigenvalues of $T$ on $S^{2} V \oplus \Lambda^{2} V$, forced by
the categorical volume constraint and not posited separately.
