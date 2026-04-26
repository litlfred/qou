Within the Borromean baryon ([Definition](#def:borromean-baryon)),
the three quark strands form a $3$-strand braid in $B_3$.  Each
pairwise crossing between strands $i$ and $j$ is resolved in the
Iwahori--Hecke algebra $H_3(R, q)$
([Hecke algebra](#rem:hecke-algebra-from-braiding)) according to
the **flavors** of the quarks at positions $i$ and $j$.

The **typed crossing operator** $C(f_i, f_j; \sigma_k) \in H_3(R, q)$
for a pair of quarks with flavors $f_i, f_j \in \{\mathfrak{u}, \mathfrak{d}\}$
at generator $\sigma_k$ is:

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

**Motivation.**

- The **up--up** crossing is the bare generator $\sigma_k$:
  positive-orientation unknots cross positively.

- The **down--down** crossing is the *inverse* generator
  $\sigma_k^{-1} = \sigma_k - (q - q^{-1})$, expanded via
  the Hecke relation: negative-orientation unknots cross
  negatively.

- The **mixed** crossing is the arithmetic mean
  $\tfrac{1}{2}(\sigma_k + \sigma_k^{-1})
  = \sigma_k - \tfrac{1}{2}(q - q^{-1})$:
  one positive and one negative orientation average to a
  half-shift.

The three cases are the three crossing types from the
quark flavor assignments
([up quark](#def:up-quark), [down quark](#def:down-quark)).
The typed crossing operator encodes the flavor dependence of
the strong interaction within the Borromean link.
