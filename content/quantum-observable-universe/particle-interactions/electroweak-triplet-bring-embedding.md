**Proposition (electroweak triplet Bring embedding).**
*The even-twist 2-component torus links $T(2,4), T(2,6), T(2,8)$ — the
braids $\sigma_1^{2k} \in B_2$ for $k = 2, 3, 4$ — have Seifert genera
$1, 2, 3$ respectively. These genera are strictly increasing and all
$\leq 4 = g(\Sigma_4)$, so the three links co-embed in the genus-$4$
Seifert fiber of ([Bring's surface](#def:brings-surface)) alongside the
saturating force-carriers $\{T(2,9), T(3,5)\}$ (genus $4$), by the
embeddability bound $g(K) \leq g(\Sigma_4)$ of
([prop:torus-embeddable-complete](#prop:torus-embeddable-complete)).
Moreover the three cells carry the pairwise-orthogonal Hoefsmit idempotent
decomposition in $\mathrm{End}_R(V^{\otimes 6})$ of
([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)).*

**Proof.**

The canonical Seifert surface of the 2-component torus link $T(2, 2k)$ has
genus $g(T(2, 2k)) = k - 1$, an arithmetic progression in $k$. Hence at
$k = 2, 3, 4$ the genera are $1, 2, 3$ — strictly increasing, and each
$\leq 4$. The even-twist links with genus in $\{1, 2, 3\}$ are exactly
$k \in \{2, 3, 4\}$, so the family is finite and closed at these three.
The embeddability bound $g(K) \leq g(\Sigma_4) = 4$ then places all three
in the same genus-$4$ Seifert fiber, alongside the genus-$4$ saturating
carriers.

The genus, enumeration, and embedding steps are elementary
$\mathbb{N}$-arithmetic and are verified sorry-free in Lean via `omega`:
`ew_genus_values` (genera $1, 2, 3$), `ew_enumeration` (the
$\{1,2,3\}$-genus links are exactly $k \in \{2,3,4\}$), `ew_triplet_embeds`
(each genus $\leq 4$), combined in `electroweak_triplet_bring_embedding`.
The Hoefsmit idempotent orthogonality is not re-proved here; it is the
cited theorem
([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)). $\square$

**Scope.** This proposition is the provable structural half of the
electroweak torus-link story: it establishes *that the triplet fits* the
genus-$4$ host. It does not fix *which* link carries $W^\pm$ versus $Z$
versus $H$. That physical identification is the conjecture
([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)),
which rests on the open selection, charge, and spin sub-conjectures.
