Let the three quark strands of the Borromean baryon form a $3$-strand braid in $B_3$, and let $f_i, f_j \in \{\mathfrak{u}, \mathfrak{d}\}$ be the **flavors** of the quarks at positions $i$ and $j$. The **typed crossing operator** of the pair at generator $\sigma_k$ is the element $C(f_i, f_j; \sigma_k) \in H_3(R, q)$:

$$
  C(f_i, f_j; \sigma_k)
  = 
  \begin{cases}
    \sigma_k
      & \text{if } f_i = f_j = \mathfrak{u}
        \quad\text{(both up)}, \\[6pt]
    \sigma_k - (q - q^{-1})\mathbf{1}
      & \text{if } f_i = f_j = \mathfrak{d}
        \quad\text{(both down)}, \\[6pt]
    \sigma_k - \tfrac{1}{2}(q - q^{-1})\mathbf{1}
      & \text{if } f_i \neq f_j
        \quad\text{(mixed)}.
  \end{cases}
$$
