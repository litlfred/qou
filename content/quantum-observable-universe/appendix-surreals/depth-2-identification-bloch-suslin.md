**Proposition (depth-2 identification of $G^{(2)}(\mathcal{H}_q)$ with the Bloch group $K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q}$).**

*Let $F$ be a number field, let $q \in F$ be generic, and let $\mathcal{H}_q$ be the substrate convolution Hopf algebra over $F$ ([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)). We state the depth-2 identification:*

$$
  \boxed{\;
    \tau_{\mathrm{arch}}\!\bigl( G^{(2)}(\mathcal{H}_q) \big/ \mathcal{P}_1 \bigr)_F
    \;\cong\;
    K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q},
  \;}
$$

*We interpret the right-hand side via the Bloch–Suslin regulator $K_3^{\mathrm{ind}}(F) \otimes \mathbb{Q} \to \mathbb{R} / \pi^2 \mathbb{Q}$. This identification is a theorem. Its proof chain proceeds via the Bloch group $\mathfrak{B}(F)$, Suslin's isomorphism, and the archimedean evaluation of $\mathrm{Li}_2^q$.*

### Significance

The identification is a theorem at depth 2. At depth 3, it is conditional on Goncharov. Combined with [`prop:borel-partial-resolution`](#prop:borel-partial-resolution), this yields:

- **Depth 2.** The depth-2 statement of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) is provably correct over every Bring-natural number field $F = \mathbb{Q}(z_K)$. The keystone is a theorem here.
- **Depth 3.** The depth-3 statement relies conditionally on Goncharov's motivic conjecture. All non-Goncharov steps are provable.
- **Depth $\geq 4$.** The higher-depth statements rely conditionally on Beilinson and Goncharov.

We thus partially prove the keystone conjecture: depth $\le$ 2 is provable, while depth $\ge$ 3 reduces to standard external conjectures (Goncharov, Beilinson).

### Cross-references

- Keystone: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- K-theory bridge: [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Depth-2 numerical witness: [`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
