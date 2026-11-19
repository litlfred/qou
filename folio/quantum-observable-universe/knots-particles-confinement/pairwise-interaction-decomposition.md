**Proposition.** *Let $\mathbf{C}$ be a braided monoidal category with braiding $c$. For objects $V_1, \dots, V_n$ of $\mathbf{C}$, write*

$$
  c_i
  \;=\;
  \mathrm{id}_{V_1 \otimes \cdots \otimes V_{i-1}}
  \otimes\, c_{V_i, V_{i+1}} \otimes\,
  \mathrm{id}_{V_{i+2} \otimes \cdots \otimes V_n},
  \qquad 1 \le i \le n-1,
$$

*for the* **elementary crossing** *at position $i$, which exchanges the two adjacent factors $V_i$ and $V_{i+1}$ and fixes the rest. Suppressing associators:*

1. *(Composite reduction.) For all objects $X, Y, Z$,*
$$
  c_{X \otimes Y,\, Z}
  \;=\;
  (c_{X,Z} \otimes \mathrm{id}_Y) \circ (\mathrm{id}_X \otimes c_{Y,Z}).
$$

2. *(Route independence.) For all objects $X, Y, Z$, the two crossings of $X \otimes Y \otimes Z$ satisfy*
$$
  c_1 \, c_2 \, c_1 \;=\; c_2 \, c_1 \, c_2 .
$$

3. *(Crossing count.) Let $w = c_{i_1} \cdots c_{i_\ell}$ be a word in the elementary crossings, and let $P(w)$ be the set of strand pairs whose order the underlying permutation of $w$ reverses. If $P(w)$ is all $\binom{n}{2}$ pairs, then $\ell \ge \binom{n}{2}$.*

Part 1 says a composite system carries no interaction datum of its own. Part 2 says the decomposition into elementary crossings does not depend on the route chosen. Part 3 counts the cost: $n$ mutually interacting strands require $\binom{n}{2}$ pairwise events, so three strands require three rather than two.
