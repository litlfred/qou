**Definition.**
*Methane ($\mathrm{CH_4}$) is the molecular braid of one carbon atom $\mathrm{C}(6, 6)$ and four hydrogen atoms $\mathrm{H}_1, \mathrm{H}_2, \mathrm{H}_3, \mathrm{H}_4$. Each hydrogen shares one electron pair with the carbon, forming four single bonds.*

### Stage 1: Constituent atoms

- *Carbon: $\mathcal{A}_{\mathrm{C}} \in H_{18}(q)$, possessing valence 4.*
- *Hydrogen $\mathrm{H}_k$: $\mathcal{A}_{\mathrm{H}_k} \in H_2(q)$, possessing valence 1, for $k = 1, 2, 3, 4$.*

### Stage 2: Molecular assembly in $H_{26}(q)$

*The total strand count is $18 + 4 \times 2 = 26$. Carbon shares each of its four valence electrons with one hydrogen, yielding four single $\mathrm{C\!-\!H}$ bonds. Each bond supplies two attractive $\sigma^{-1}$ crossings.*

### Stage 3: Iterative construction

1. *Begin with $\mathcal{A}_{\mathrm{C}}$ in normal form (NF).*
2. *Assemble $\mathrm{H}_1$. Embed the state in $H_{20}(q)$, apply inter-atomic crossings, insert one covalent bond operator (two attractive crossings), and reduce to NF.*
3. *Assemble $\mathrm{H}_2$. Embed in $H_{22}(q)$ and reduce to NF.*
4. *Assemble $\mathrm{H}_3$. Embed in $H_{24}(q)$ and reduce to NF.*
5. *Assemble $\mathrm{H}_4$. Embed in $H_{26}(q)$ and reduce to NF.*

*Confluence guarantees that the assembly order ($\mathrm{H}_1$, then $\mathrm{H}_2$, etc.) does not alter the final NF. However, it affects intermediate complexity. The LP dual optimises the assembly sequence to minimise intermediate word count.*
