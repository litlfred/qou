**Definition (Markov-axiom recursive ascent).**
*Given a braid $\beta \in B_n$ with Hecke representative $T_w \in H_n(q)$ in Gröbner-Shirshov normal form, the recursive ascent algorithm evaluates the canonical Jones-Markov trace $\mathrm{tr}_M^{(n)}(T_w)$ by:*

1. *Eliminating inverse generators via $\sigma_i^{-1} = \sigma_i - (q - q^{-1})$.*
2. *Peeling the top generator to yield $\mathrm{tr}_M^{(n)}(T_w) = z \cdot \mathrm{tr}_M^{(n-1)}(T_{w'})$.*
3. *Branching on the Hecke quadratic $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$.*
4. *Recursing on $T_{w'}$ until reaching the base case $\mathrm{tr}_M^{(1)}(\mathbf{1}) = 1$.*

The recursive ascent path boundedly evaluates the trace without materialising unwieldy symbolic matrix representations. The production implementation completes the $^4\mathrm{He}$ mass derivation end-to-end in ~60 seconds.


**Terms defined:** :defterm[markov-axiom-recursive-ascent]
