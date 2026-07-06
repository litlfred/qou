**Proposition (electroweak triplet Bring embedding).**
*The even-twist 2-component torus links $T(2,4), T(2,6), T(2,8)$ — the braids $\sigma_1^{2k} \in B_2$ for $k = 2, 3, 4$ — have Seifert genera $1, 2, 3$ respectively. These genera strictly increase and satisfy $g \leq 4 = g(\Sigma_4)$. The three links therefore co-embed in the genus-$4$ Seifert fiber of ([Bring's surface](#def:brings-surface)) alongside the saturating force-carriers $\{T(2,9), T(3,5)\}$ (genus $4$), by the embeddability bound $g(K) \leq g(\Sigma_4)$ of ([prop:torus-embeddable-complete](#prop:torus-embeddable-complete)). Moreover, the three cells carry the pairwise-orthogonal Hoefsmit idempotent decomposition in $\mathrm{End}_R(V^{\otimes 6})$ of ([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)).*

**Proof.**

The canonical Seifert surface of the 2-component torus link $T(2, 2k)$ has genus $g(T(2, 2k)) = k - 1$. At $k = 2, 3, 4$ the genera are $1, 2, 3$. These strictly increase and remain $\leq 4$. The even-twist links with genus in $\{1, 2, 3\}$ are exactly those with $k \in \{2, 3, 4\}$. The family is finite and closed at these three. The embeddability bound $g(K) \leq g(\Sigma_4) = 4$ places all three in the same genus-$4$ Seifert fiber alongside the saturating carriers.

The genus, enumeration, and embedding steps involve elementary $\mathbb{N}$-arithmetic. They are verified sorry-free in Lean via `omega`: `ew_genus_values`, `ew_enumeration`, and `ew_triplet_embeds`, combined in `electroweak_triplet_bring_embedding`. The Hoefsmit idempotent orthogonality is cited from ([thm:hoefsmit-ew-cell-content](#thm:hoefsmit-ew-cell-content)). $\square$

**Scope.**
This proposition supplies the provable structural half of the electroweak torus-link story. It establishes that the triplet fits the genus-$4$ host. It does not fix *which* link carries $W^\pm$ versus $Z$ versus $H$. That physical identification constitutes the conjecture ([conj:electroweak-higgs-torus-link-triplet](#conj:electroweak-higgs-torus-link-triplet)). This conjecture relies on the open selection, charge, and spin sub-conjectures.
