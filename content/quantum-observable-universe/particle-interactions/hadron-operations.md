The braiding and Hopf link structure of $\mathbf{C}$ induce natural operations on the symmetric product $\mathrm{Sym}^n(K)$.

**Braiding.** The braiding $\beta_{K_i, K_j} \colon K_i \otimes K_j \xrightarrow{\sim} K_j \otimes K_i$ permutes constituent knots within a hadron. Because $\mathrm{Sym}^n$ quotients by the symmetric group action, this braiding descends to an involution on $\mathrm{Sym}^n(K)$. For the antisymmetric product (fermions), exchanging identical constituents yields $-1$.

**Hopf linking.** Two knots $K_i, K_j$ in the same hadron link via the Hopf link $\mathcal{L}_{\mathrm{Hopf}}$. The linking operation

$$
  \ell_{ij} \colon K_i \otimes K_j \longrightarrow K_i \mathbin{\#_{\mathrm{Hopf}}} K_j
$$

replaces two constituents with a linked pair. The inverse operation (unlinking) decomposes a linked pair into separated constituents when the linking number is trivial.

**Skein action.** The $q$-deformed Skein relations act on $\mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ by resolving link crossings. At each crossing, the relation dictates the decomposition:

$$
  q \cdot L_+ - q^{-1} \cdot L_- = (q - q^{-1}) \cdot L_0,
$$

where $L_+$, $L_-$, and $L_0$ are the positive, negative, and smoothed configurations. Iterating across all crossings resolves the composite into unlinked constituents scaled by a polynomial in $q$. This yields the mass formula $\mathcal{M}(\mathfrak{H}) = Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}}) + \sum_i \mathcal{M}(K_i)$.

**Fusion.** We fuse two hadrons $\mathfrak{H}_1 \in \mathrm{Sym}^{n_1}(K)$ and $\mathfrak{H}_2 \in \mathrm{Sym}^{n_2}(K)$ into a composite $\mathfrak{H}_1 \star \mathfrak{H}_2 \in \mathrm{Sym}^{n_1 + n_2}(K)$ by constructing the Hopf link between their binding structures. This provides a categorical model for hadron scattering.
