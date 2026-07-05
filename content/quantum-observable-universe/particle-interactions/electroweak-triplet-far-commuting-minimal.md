**Theorem (far-commuting minimality of the even-twist triplet).**
*Let $\sigma_a, \sigma_b, \sigma_c$ be braid generators that are pairwise
far-commuting, i.e. $|a-b|, |b-c|, |a-c| \geq 2$ (the far-commutativity
range $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i-j| \geq 2$). Then:*

1. *(Minimality.) They require at least $6$ strands: writing $1 \leq a < b < c$,
   the pairwise gap $\geq 2$ forces the top index $c \geq 5$, hence
   $n \geq c+1 \geq 6$. The bound is attained **uniquely** by the consecutive
   odd triple $(a,b,c) = (1,3,5)$, which fits in $B_6$.*

2. *(Enumeration.) The even-twist $2$-component torus links $T(2,2k)$ (braid
   $\sigma_1^{2k}$, Seifert genus $g = k-1$) whose genus lies strictly between
   the trivial Hopf endpoint $g=0$ and the genus-$4$ Bring saturation, i.e.
   $1 \leq g \leq 3$, are exactly $k \in \{2,3,4\}$: the triplet
   $T(2,4), T(2,6), T(2,8)$.*

This is the **physics-free mathematical core** of the electroweak selection
principle C1 of
([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)).
Both halves are elementary $\mathbb{N}$-arithmetic, Lean-proved sorry-free
(`omega`).

**Far-commuting minimality — why $n=6$.**

Each even-twist carrier $T(2,2k)$ acts on a single strand-pair. Three
mutually non-interfering carriers need three generators $\sigma_a, \sigma_b,
\sigma_c$ that pairwise commute *without sharing a strand* — precisely the
far-commutativity condition $|i-j| \geq 2$. In $B_n$ a generator $\sigma_i$
requires $1 \leq i \leq n-1$. Three indices with $a \geq 1$, $b \geq a+2$,
$c \geq b+2$ give $c \geq 5$, so $n = c+1 \geq 6$; and $c = 5$ forces
$(a,b,c) = (1,3,5)$. This is the mathematical statement realised physically
in
([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)),
where the $n=6$ minimum is the three disjoint strand-pairs
$\{1,2\}, \{3,4\}, \{5,6\}$ carrying $\sigma_1^4, \sigma_3^6, \sigma_5^8$.

**Enumeration — the sub-saturating window.**

The genus filtration places the trivial Hopf link $T(2,2)$ at $g=0$ (vacuum)
and the force-carrier saturation $\{T(2,9), T(3,5)\}$ at $g=4 = g(\Sigma_4)$.
The open window $0 < g < 4$ contains exactly the genera $1,2,3$, i.e.
$k \in \{2,3,4\}$. This forward inclusion is the identical arithmetic proved
sorry-free as `ew_enumeration` in
([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding));
it is reproduced inline in the Lean sibling because content-block sibling
`.lean` files compile standalone (Mathlib-only) and cannot import one
another. The proposition is the canonical statement.

**What is and is not proved here.**

This theorem upgrades the *mathematical content* of C1 — the minimality and
the enumeration — to a proved statement. It does **not** assert that the
electroweak sector *is* this set of links; that identification (the physics
selection postulate: EW carriers $\leftrightarrow$ the sub-saturating
even-twist window) remains the residual conjectural input of
([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)).
The far-commuting bound and the enumeration are the enumerative facts on
which that postulate operates.
