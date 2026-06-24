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

**Physical interpretation.**

The Hecke relation $\sigma^2 = (q - q^{-1})\sigma + 1$ breaks
the symmetry between positive and negative crossings.  At $q = 1$:
$\sigma^2 = 1$ (positive and negative crossings cancel — parity
conserved).  At the substrate parameter $q$:
$\sigma^2 = 0.209\,\sigma + 1$ (the $0.209\,\sigma$ term
distinguishes positive from negative — parity violated).

The **degree of parity violation** is controlled by:

$$
  q - q^{-1} = 0.209 \quad (\text{at } q = q_0)
$$

This is the same quantity that appears in the Skein amplitude
$(q^{1/2} - q^{-1/2})$ and the Hecke deformation.  All parity
violation traces back to $q \neq 1$.

**Maximal parity violation.**

In the Standard Model, the weak force violates parity
*maximally* — it couples only to left-handed particles.  In the
Descartes framework, this corresponds to the crossing chirality:

- A **positive crossing** $\sigma_i$ contributes weight $q$
  to the categorical action.
- A **negative crossing** $\sigma_i^{-1}$ contributes weight
  $q^{-1}$.

The ratio $q / q^{-1} = q^2 = 1.232$ measures the
left-right asymmetry.  At $q = 1$: ratio $= 1$ (no asymmetry).
At $q \to \infty$: ratio $\to \infty$ (maximal asymmetry).

The Wu experiment (1957) measured the angular distribution
of electrons from ${}^{60}\mathrm{Co}$ beta decay and found a
strong forward-backward asymmetry.  In the Descartes framework,
this asymmetry is the **crossing chirality** of the nuclear link:
the ${}^{60}\mathrm{Co}$ braid word has a specific writhe
$w \neq 0$, and the Skein crossing change at the substrate parameter $q$
produces an asymmetric emission pattern determined by $q^w$.

**Connection to the $\mathbb{Z}/2$ of beta decay.**

The $\mathbb{Z}/2$ symmetry $q \leftrightarrow q^{-1}$ that
exchanges $\beta^- \leftrightarrow \beta^+$
([beta decay](#def:beta-decay-skein)) is the **combined**
$\widehat{CP}$ operation: parity $\mathcal{P}$ (mirror all
crossings) composed with charge conjugation $\hat{C}$
(exchange particle $\leftrightarrow$ antiparticle, i.e.,
$T_{2,3} \leftrightarrow T_{2,3}^{\sigma}$).

- $\mathcal{P}$ alone: violated ($q \neq q^{-1}$)
- $\hat{C}$ alone: violated (electron $\neq$ positron in
  mass ordering)
- $\widehat{CP}$: the $q \leftrightarrow q^{-1}$ involution,
  which IS a symmetry of the Iwahori--Hecke algebra

This gives the standard result: $\mathcal{P}$ violated,
$\hat{C}$ violated, $\widehat{CP}$ conserved (to leading
order in the Descartes framework).
