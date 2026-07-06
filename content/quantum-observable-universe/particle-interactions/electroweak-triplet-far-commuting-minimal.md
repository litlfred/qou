**Theorem (far-commuting minimality of the even-twist triplet).**
*Let $\sigma_a, \sigma_b, \sigma_c$ be pairwise far-commuting braid generators: $|a-b|, |b-c|, |a-c| \geq 2$. Then:*

1. *(Minimality.) These generators require at least $6$ strands. With $1 \leq a < b < c$, the pairwise gap $\geq 2$ forces $c \geq 5$, yielding $n \geq c+1 \geq 6$. The bound is attained **uniquely** by the consecutive odd triple $(a,b,c) = (1,3,5)$ in $B_6$.*
2. *(Enumeration.) The even-twist $2$-component torus links $T(2,2k)$ (braid $\sigma_1^{2k}$, Seifert genus $g = k-1$) with genus strictly between the trivial Hopf endpoint $g=0$ and the genus-$4$ Bring saturation ($1 \leq g \leq 3$) are exactly those with $k \in \{2,3,4\}$: the triplet $T(2,4), T(2,6), T(2,8)$.*

This forms the **physics-free mathematical core** of the electroweak selection principle C1 of ([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)). Both halves rely on elementary $\mathbb{N}$-arithmetic and are Lean-proved sorry-free (`omega`).

**Far-commuting minimality.**

Each even-twist carrier $T(2,2k)$ acts on a single strand-pair. Three mutually non-interfering carriers require three generators $\sigma_a, \sigma_b, \sigma_c$ that pairwise commute without sharing a strand. This is the far-commutativity condition $|i-j| \geq 2$. In $B_n$, a generator $\sigma_i$ requires $1 \leq i \leq n-1$. Three indices with $a \geq 1$, $b \geq a+2$, $c \geq b+2$ dictate $c \geq 5$, so $n = c+1 \geq 6$. Setting $c = 5$ forces $(a,b,c) = (1,3,5)$. This mathematical statement is physically realised in ([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)). The $n=6$ minimum supplies three disjoint strand-pairs $\{1,2\}, \{3,4\}, \{5,6\}$ carrying $\sigma_1^4, \sigma_3^6, \sigma_5^8$.

**Enumeration.**

The genus filtration places the trivial Hopf link $T(2,2)$ at $g=0$ and the force-carrier saturation $\{T(2,9), T(3,5)\}$ at $g=4 = g(\Sigma_4)$. The open window $0 < g < 4$ contains exactly the genera $1,2,3$ ($k \in \{2,3,4\}$). This forward inclusion matches the arithmetic proved sorry-free as `ew_enumeration` in ([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)). It is reproduced inline in the Lean sibling because content-block sibling `.lean` files compile standalone and cannot import one another. The proposition serves as the canonical statement.

**Scope.**

This theorem elevates the mathematical content of C1 to a proved statement. It does **not** assert that the electroweak sector *is* this set of links. That identification remains the conjectural input of ([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)). The far-commuting bound and enumeration provide the facts upon which that postulate operates.
