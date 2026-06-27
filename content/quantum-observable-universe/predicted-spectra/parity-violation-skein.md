*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Parity is violated by the weak interaction if and only if
$q \neq 1$.**

### Origin: Hecke eigenvalue asymmetry

The parity violation follows directly from the categorical origin of
the crossing energy
([crossing energy](#def:crossing-energy)): the Hecke generator $\sigma =
P \circ R$ has eigenvalues $(q, -q^{-1})$ on $S^{2} V \oplus \Lambda^{2}
V$, and $\lvert q \rvert \neq \lvert {-q^{-1}} \rvert$ for $q \neq 1$.
A positive crossing $L_{+}$ carries the eigenvalue $q$; a negative
crossing $L_{-}$ carries $-q^{-1}$.  Parity $\mathcal{P}$ exchanges
$L_{+} \leftrightarrow L_{-}$ but does not change $q$ --- hence
$\mathcal{P}$-invariance forces $q = -q^{-1}$, i.e.\ $q^{2} = -1$,
impossible on the substrate ray.  The sign-asymmetry of the eigenvalue
pair (inherited from $P|_{\Lambda^{2} V} = -\mathrm{id}$) is the
algebraic source of P-violation; it is not a physical postulate added
to the framework.

The detailed Skein derivation below rederives the same conclusion from
the Skein relation; both are consequences of the same eigenvalue
structure.

### Skein derivation

The parity operation $\mathcal{P}$ on a link is the **mirror**:
reverse all crossings ($L_+ \leftrightarrow L_-$).  In the braid
group $B_n$, this is the involution
$\sigma_i \mapsto \sigma_i^{-1}$.

**The Skein relation under parity.**

The Skein relation at a single crossing:

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0]
$$

Apply the mirror $\mathcal{P}$: $L_+ \mapsto L_-$,
$L_- \mapsto L_+$, $L_0 \mapsto \mathcal{P}(L_0)$.  The
mirrored Skein relation reads:

$$
  q  [L_-] -  q^{-1} [L_+]
  = 
  (q^{1/2} - q^{-1/2})  [\mathcal{P}(L_0)]
$$

Rearranging:

$$
  q^{-1} [L_+] -  q  [L_-]
  = 
  -(q^{1/2} - q^{-1/2})  [\mathcal{P}(L_0)]
$$

Compare with the original:

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0]
$$

These are the **same** equation if and only if $q = q^{-1}$,
i.e., $q = 1$.

**Proposition.**
*The Skein relation is invariant under parity
$\mathcal{P}: L_+ \leftrightarrow L_-$ if and only if $q = 1$.
For any $q \neq 1$, the weak interaction
([beta decay](#def:beta-decay-skein)) violates parity.*

*Proof.*
The Skein relation assigns coefficient $q$ to $[L_+]$ and
$q^{-1}$ to $[L_-]$.  Parity exchanges $L_+ \leftrightarrow L_-$
but does not change $q$.  The relation is $\mathcal{P}$-invariant
iff $q = q^{-1}$, which holds iff $q^2 = 1$, hence $q = 1$
(since $q > 0$).  $\square$
