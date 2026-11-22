**Definition.**
**Methane** *$CH_4$ is the **molecular braid** of one carbon atom $C(6, 6)$ and four hydrogen atoms $H_1, H_2, H_3, H_4$, each sharing one electron pair (four single bonds).*

### Stage 1: Constituent atoms

- *Carbon: $\mathcal{A}_C \in H_{18}(q)$, valence 4*
- *Hydrogen $H_k$: $\mathcal{A}_{H_k} \in H_2(q)$, valence 1, for $k = 1, 2, 3, 4$*

### Stage 2: Molecular assembly in $H_{26}(q)$

*Total strands: $18 + 4 \times 2 = 26$. Each of carbon's 4 valence electrons is shared with one hydrogen, forming 4 single C--H bonds. Each bond contributes 2 attractive $\sigma^{-1}$ crossings.*

### Stage 3: Iterative construction

1. *Start with $\mathcal{A}_C$ in NF.*
2. *Assemble $H_1$: embed in $H_{20}(q)$, apply inter-atomic crossings, apply 1 covalent bond operator (2 attractive crossings), reduce to NF.*
3. *Assemble $H_2$: embed in $H_{22}(q)$, reduce to NF.*
4. *Assemble $H_3$: embed in $H_{24}(q)$, reduce to NF.*
5. *Assemble $H_4$: embed in $H_{26}(q)$, reduce to NF.*

*The construction order ($H_1$ first, then $H_2$, etc.) does not affect the final NF (confluence). It affects intermediate complexity. The LP dual optimises the assembly ordering to minimise intermediate word count. Confluence concerns one fixed assembly word. If each bond word is re-selected as the bonds form, the selected word, and with it the final normal form, can depend on the order.*
