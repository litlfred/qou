The symmetric product $\mathrm{Sym}^n(K)$ carries natural operations
inherited from the braiding and Hopf link structure of $\mathbf{C}$.

**Braiding.** The braiding $\beta_{K_i, K_j} \colon K_i \otimes K_j \xrightarrow{\sim} K_j \otimes K_i$ permutes constituent knots within
a hadron. Since $\mathrm{Sym}^n$ quotients by the symmetric group
action, the braiding descends to an involution on
$\mathrm{Sym}^n(K)$. For fermions (antisymmetric product), the
braiding picks up a sign: exchanging two identical constituents
produces $-1$.

**Hopf linking.** Two knots $K_i, K_j$ within the same hadron can be
*linked* via the Hopf link $\mathcal{L}_{\mathrm{Hopf}}$. This
linking operation

$$
  \ell_{ij}  \colon 
  K_i \otimes K_j
   \longrightarrow 
  K_i \mathbin{\#_{\mathrm{Hopf}}} K_j
$$

replaces two separate constituents with a single linked pair. The
inverse operation (*unlinking*) decomposes a linked pair back into
its constituents, when the linking number is trivial.

**Skein action.** The $q$-deformed Skein relations act on
$\mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ by resolving
crossings in the linked configuration. At each crossing, the Skein
relation provides the decomposition:

$$
  q \cdot L_+ -  q^{-1} \cdot L_-
  =  (q - q^{-1}) \cdot L_0
$$

where $L_+$, $L_-$, $L_0$ are the positive-crossing, negative-crossing,
and smoothed configurations. Iterating over all crossings resolves
the linked composite into a polynomial in $q$ times unlinked
constituents, yielding the mass formula
$\mathcal{M}(\mathfrak{H}) = Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}}) + \sum_i \mathcal{M}(K_i)$.

**Fusion.** Two hadrons $\mathfrak{H}_1 \in \mathrm{Sym}^{n_1}(K)$ and
$\mathfrak{H}_2 \in \mathrm{Sym}^{n_2}(K)$ can be *fused* into a composite
$\mathfrak{H}_1 \star \mathfrak{H}_2 \in \mathrm{Sym}^{n_1 + n_2}(K)$ by forming the
Hopf link between their binding structures. This models hadron
scattering at the categorical level.
