The raw normal form has up to $A!$ terms. Quotienting by the
adjacency / chain-collapse ideals
([quotient ideals $I_8$, $I_9$](#def:gs-quotient-ideals-I8-I9))
reduces this to exactly $A$ terms — the **optimal Gröbner--Shirshov
basis** — for nuclei in the valley of stability ($N \geq Z - 1$).

**Theorem (Optimal Normal Form).**
*For any nucleus $N(Z, N)$ with $N \geq Z - 1$ (valley of stability),
the Gröbner--Shirshov normal form after quotient ideals I$_{8}$ + I$_{9}$ has exactly
$A = Z + N$ terms:*

$$
  \mathcal{N}_{\mathrm{opt}}(Z, N)
  = 
  c_0 \cdot \mathbf{1}
  + c_1 \cdot \sigma_0
  + c_2 \cdot \sigma_1
  + \cdots
  + c_{A-1} \cdot \sigma_{A-2}
$$

*where each coefficient $c_i = \hat{V}_i(q)$ is the Markov-traced volume
from the transfer matrix chain at generator $\sigma_i$.*
