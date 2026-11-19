Let $G$ be a group, standing for the braid group $B_n$ or its image in the Hecke algebra $H_n(q)$, and let $R$ be a ring of values. A function $f \colon G \to R$ is an **observable** if $f(xy) = f(yx)$ for all $x, y \in G$. Words $a, b$ are **conjugate**, $a \approx b$, if $b = y a y^{-1}$ for some $y$, and **equal in normal form**, $a \equiv b$, if they reduce to the same Gröbner–Shirshov normal form.

Fix a set $\mathcal{O}$ of observables. A subword $x$ placed between $u$ and $v$ is **virtual** for $\mathcal{O}$ if

$$
  f(u\,x\,v) = f(u\,v) \quad \text{for every } f \in \mathcal{O}.
$$

Let $w$ be a word on $n$ strands and $A \subset \{1, \dots, n\}$. Write $c_A(w)$ for the signed number of crossings between a strand in $A$ and a strand outside $A$, and $s_A(w)$ for the signed number of the remaining crossings. The word is **entangled across** $A \mid A^{c}$ if $c_A(w) \neq 0$. A **prior entangled pair** is a pure subword that is entangled across the cut separating its two partners.

Let $F$ assign a value in a commutative ring to each finite set $T$ of strands. Its **connected part** on $T$ is the Möbius inversion over subsets,

$$
  \phi_F(T) = (-1)^{|T|} \sum_{U \subseteq T} (-1)^{|U|} F(U).
$$
