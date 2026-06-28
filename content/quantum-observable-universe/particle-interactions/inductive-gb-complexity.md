The nuclear normal form computation involves multiplying and reducing
elements in the Hecke algebra $H_A(q)$. While the total number of
Hecke reduction steps grows as $O(A^3)$, the number of terms in the
Gröbner--Shirshov normal form is bounded by the central binomial
coefficient $\binom{A-1}{\lfloor(A-1)/2\rfloor}$. This bound grows
exponentially, scaling as $O(2^A / \sqrt{A})$.

As a result, the computational time in the mass number $A$ scales
exponentially when calculating explicit normal forms for large nuclei,
dominated by the term expansion.
