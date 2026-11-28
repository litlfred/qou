**Proposition.** *Let $K$ be a field and $C_2 \xrightarrow{d_2} C_1 \xrightarrow{d_1} C_0$ finite-dimensional $K$-vector spaces with $d_1 d_2 = 0$. Let $(f_0, f_1, f_2)$ be a chain map, $d_1 f_1 = f_0 d_1$ and $d_2 f_2 = f_1 d_2$. With $H_0 = C_0/\operatorname{im} d_1$, $H_1 = \ker d_1/\operatorname{im} d_2$ and $H_2 = \ker d_2$,*

$$
\operatorname{tr} f_0 - \operatorname{tr} f_1 + \operatorname{tr} f_2 = \operatorname{tr}(f \mid H_0) - \operatorname{tr}(f \mid H_1) + \operatorname{tr}(f \mid H_2).
$$

*If $C_k = K^{X_k}$ for a finite set $X_k$ of cells and $f_k$ permutes the cells, $\operatorname{tr} f_k$ is the number of fixed cells.*

*Proof.* For an endomorphism $f$ of $V$ preserving a subspace $W$, $\operatorname{tr} f = \operatorname{tr}(f|_W) + \operatorname{tr}(f \text{ on } V/W)$. To see this, choose a linear section $s$ of $\pi : V \to V/W$ and put $r = \mathrm{id} - s\pi$, a map into $W$, so $\iota r + s\pi = \mathrm{id}$; then cyclicity of trace gives $\operatorname{tr} f = \operatorname{tr}(r f \iota) + \operatorname{tr}(\pi f s)$. Apply this to $\operatorname{im} d_1 \subseteq C_0$, $\ker d_1 \subseteq C_1$, $\operatorname{im} d_2 \subseteq \ker d_1$ and $\ker d_2 \subseteq C_2$. The isomorphisms $C_1/\ker d_1 \cong \operatorname{im} d_1$ and $C_2/\ker d_2 \cong \operatorname{im} d_2$ intertwine the induced maps, so the two middle terms cancel in pairs. For a permuted basis, the diagonal entry at a cell is $1$ when the cell is fixed and $0$ otherwise. $\square$

**Use.** This is the formula behind `hopf_trace_h1` in [`prop:bring-harmonic-types`](bring-harmonic-types.md), where $\chi_{C_k}(g)$ counts the cells of Bring's map fixed by $g$. What stays cited there is that the cellular homology of the map is the homology of the surface, with $H_0$ trivial and $H_2$ the orientation character, and the Hodge splitting of $H^1$.
