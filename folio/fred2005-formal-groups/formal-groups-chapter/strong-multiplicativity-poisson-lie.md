Strong multiplicativity has three readings.

**Primitive elements.** Suppose $x, y \in T$ are primitive, $\Delta x = x \otimes 1 + 1 \otimes x$ and likewise for $y$. Applying $1 \otimes \tau \otimes 1$ to $\Delta x \otimes \Delta y$ gives four terms, which pair the tensor factors as $(x, y)(1, 1)$, $(x, 1)(1, y)$, $(1, y)(x, 1)$ and $(1, 1)(x, y)$. A [Poisson structure](#def:skewed-poisson-structure) is a biderivation, so $\pi(a, 1) = \pi(1, a) = 0$. Every term therefore kills $\pi \otimes \pi$, and only the first and last survive, giving

$$
\Delta\,\pi(x, y) \;=\; \pi(x, y) \otimes 1 \;+\; 1 \otimes \pi(x, y).
$$

For the tensor algebra of a Lie algebra $\mathfrak{g}$ with $\Delta$ induced by the diagonal of $\mathfrak{g}$ (\cite{leitner2006}, Remark 1.12), this holds for every Lie bracket. It imposes no condition on $\mathfrak{g}$ itself.

**Non-primitive elements.** The $\pi \otimes \pi$ term matters on non-primitive basis elements. For example $\Delta(x^2)$ contains $2\,x \otimes x$, so the right-hand side for $\pi(x^2, z^2)$ contains $4\,\pi(x, z) \otimes \pi(x, z)$. In characteristic $p$ the coordinate algebras $A_i$ carry divided powers, and the condition has content there.

**Poisson–Lie groups.** Without the $\pi \otimes \pi$ term the condition reads $\Delta \circ \pi = (\cdot \otimes \pi + \pi \otimes \cdot) \circ (1 \otimes \tau \otimes 1) \circ \Delta$. The operator on the right is the product Poisson bracket on $S \otimes S$, $\{a \otimes b, c \otimes d\} = ac \otimes \{b, d\} + \{a, c\} \otimes bd$. So the truncated condition says $\Delta$ is a map of Poisson algebras. For a group $G$ with coordinate algebra $S$, that is the statement that multiplication $G \times G \to G$ is a Poisson map, which is the multiplicativity of a Poisson–Lie group \cite{luweinstein1990}. Strong multiplicativity adds the quadratic term $\pi \otimes \pi$, which records the deformation of the product of $S$ to that of $U$.

**Necessity.** The computation in the proof of Proposition 1.13 of \cite{leitner2006} runs in both directions. If the quotient $U$ is a bialgebra with the $A_i$ as sub-bialgebras, expanding $\Delta(yx - xy)$ with $y'x' = x' \cdot y' + \pi(y', x')$ gives exactly $(\cdot \otimes \pi + \pi \otimes \cdot + \pi \otimes \pi)(1 \otimes \tau \otimes 1)(\Delta y \otimes \Delta x)$. So on the generators $X$, strong multiplicativity is necessary as well as sufficient for $\Delta$ to descend to $U$.
