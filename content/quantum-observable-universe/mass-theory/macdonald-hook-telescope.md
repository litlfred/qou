**Proposition (Macdonald hook-content telescope).**
*Let $Q = q^2$ and $X = q\,z\,/\,(1 - Q + q\,z)$. The Wenzl-bridge normalisation $Z_n$ telescopes identically to a geometric ratio:*

$$
  \boxed{\;
    Z_n \;=\; \left(\frac{1 - X}{1 - Q}\right)^n.
  \;}
$$

*Therefore, every Jones-Markov coefficient admits a single-product closed form:*

$$
  \boxed{\;
    y_\lambda \;=\; Q^{n(\lambda)}
      \cdot \frac{(1 - Q)^n}{(1 - X)^n}
      \cdot \prod_{x \in \lambda}
        \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}.
  \;}
$$

This algebraic collapse removes the nested polynomial denominators entirely. It reduces evaluation cost from exponential series summation to a single $O(n)$ product over partition cells.
