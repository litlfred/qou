*Proof.*
The Skein relation assigns coefficient $q$ to $[L_+]$ and $q^{-1}$ to $[L_-]$. Parity exchanges $L_+ \leftrightarrow L_-$ but preserves $q$. The relation is $\mathcal{P}$-invariant if and only if $q = q^{-1}$. Since $q > 0$, this requires $q = 1$. $\square$

## Origin: Hecke eigenvalue asymmetry

Parity violation follows directly from the categorical origin of the crossing energy. The Hecke generator $\sigma = P \circ R$ has eigenvalues $(q, -q^{-1})$ on $S^{2} V \oplus \Lambda^{2} V$. The relation $\lvert q \rvert \neq \lvert {-q^{-1}} \rvert$ holds for $q \neq 1$. A positive crossing $L_{+}$ carries the eigenvalue $q$. A negative crossing $L_{-}$ carries $-q^{-1}$. Parity $\mathcal{P}$ exchanges $L_{+} \leftrightarrow L_{-}$ but does not change $q$. Hence $\mathcal{P}$-invariance forces $q = -q^{-1}$, giving $q^{2} = -1$. This is impossible on the aether ray. The sign-asymmetry of the eigenvalue pair is the algebraic source of P-violation. It is inherited from $P|_{\Lambda^{2} V} = -\mathrm{id}$. It is not a physical postulate added to the framework.

The detailed Skein derivation below rederives the same conclusion from the Skein relation. Both are consequences of the same eigenvalue structure.

## Skein derivation

The parity operation $\mathcal{P}$ on a link is the mirror. It reverses all crossings ($L_+ \leftrightarrow L_-$). In the braid group $B_n$, this is the involution $\sigma_i \mapsto \sigma_i^{-1}$.

The Skein relation at a single crossing:

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0]
$$

Apply the mirror $\mathcal{P}$. This sends $L_+ \mapsto L_-$, $L_- \mapsto L_+$, and $L_0 \mapsto \mathcal{P}(L_0)$. The mirrored Skein relation reads:

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

Compare this with the original:

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0]
$$

These are the same equation if and only if $q = q^{-1}$, meaning $q = 1$.
