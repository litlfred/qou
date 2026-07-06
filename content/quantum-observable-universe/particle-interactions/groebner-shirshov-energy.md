The Gröbner--Shirshov basis theory for the Iwahori--Hecke algebra
$H_A(q)$ gives a stronger result than uniqueness of normal
forms: the **energy** of the nuclear braid word is a topological
invariant, computed by the division algorithm with no path
dependence.

**Theorem.**
Let $G = \{\sigma_i^2 - (q - q^{-1})\sigma_i - 1, \sigma_i \sigma_{i+1} \sigma_i - \sigma_{i+1} \sigma_i \sigma_{i+1}, \sigma_i \sigma_j - \sigma_j \sigma_i\}$ be the Gröbner--Shirshov basis
for $H_A(q)$
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)).
Define the **energy functional** on $H_A(q)$ by

$$
  E(\xi) =  \sum_{w \in B} |c_w(q)| \cdot \ell(w)
$$

where $\xi = \sum_w c_w(q) \cdot w$ is the normal form
$\mathcal{N}(Z, N)$ and $\ell(w)$ is the word length.
Then:

1. **Only Hecke reductions change energy.**
   The Yang--Baxter relation $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ and the far
   commutativity $\sigma_i \sigma_j = \sigma_j \sigma_i$
   preserve all coefficients and word lengths.  The Hecke
   relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ is the
   unique energy-changing generator in $G$.

2. **Energy is path-independent.**
   The total energy change from the unreduced braid word
   $\mathcal{N}_{\mathrm{raw}}(Z, N)$ to the normal form
   $\mathcal{N}(Z, N)$ is independent of the order
   in which the Gröbner--Shirshov basis elements are applied.  This
   follows from the confluence (Bergman diamond lemma) of the
   Gröbner--Shirshov basis: all reduction paths lead to the
   same normal form, and the energy is a function of the
   normal form alone.

3. **Each Hecke step has a definite energy.**
   When $\sigma_i^2$ is replaced by $(q - q^{-1})\sigma_i + 1$,
   the energy change at that step is

   $$
     \Delta E_{\mathrm{step}}
     = 
     |c| \cdot \bigl(|q - q^{-1}| + 1 - 1\bigr)
     = 
     |c| \cdot |q - q^{-1}|
   $$

   where $c$ is the coefficient of the $\sigma_i^2$ term.  Every
   Hecke step **increases** the total weight by $|c| \cdot (q - q^{-1})$
   (since $q > 1$ ensures $q - q^{-1} > 0$).

**Archimedean specialisation (§7c).** The energy $|c|\,(q - q^{-1})$ and its positivity for $q > 1$ are stated over $\mathbb{R}$ using the real ordering, so this block sits on the archimedean side of the substrate wall.
