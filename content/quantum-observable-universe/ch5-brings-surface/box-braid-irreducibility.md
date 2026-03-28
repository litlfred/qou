**Proposition.**
*Let $G = \{T^2 - (q - q^{-1})T - 1,\;
\sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1},\;
\sigma_i\sigma_j - \sigma_j\sigma_i\}$ be the Gröbner basis of
the Hecke algebra $H_n(q)$
([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)).
Then the braid word $\beta_{\mathrm{box}}$ encoding the process
$\gamma\gamma \to \nu\bar{\nu}$ via an electron box is
**irreducible**: no element of $G$ reduces $\beta_{\mathrm{box}}$
to a process with fewer than $10$ crossings or to a direct
$\gamma$–$\nu$ coupling.*

**The box braid: crossing-by-crossing.**

The process $\gamma\gamma \to \nu\bar{\nu}$ has no tree-level
realisation because photons ($K = \varnothing$,
[photon](#ex:photon-wavefront-example)) carry no braid strands and
neutrinos ($K_{0_1}$, [neutrino](#def:neutrino-knot)) have zero
crossing chirality $Q(\nu) = 0$.  The minimal topology is a box
with four vertices and four internal propagators, all at brane
tower level $A_1$
([virtual particles](#rem:virtual-particles-exceptional-divisor)):

```tex
\[
\begin{tikzcd}[row sep=3em, column sep=4em]
  \gamma_1 \ar[r, "\text{EM}" {above}, "\dagger\text{-coupling}" {below}]
  & e^-_{\mathrm{virt}} \ar[d, "\text{Skein}_{T_{3,5}}" {right}]
  \\
  \gamma_2 \ar[u, "\text{EM}" {left}, "\dagger\text{-coupling}" {right}]
  & \nu\,\bar{\nu} \ar[l, phantom, "\text{output}" {below}]
\end{tikzcd}
\]
```

Reading the box as a braid word in $B_3$ (minimum strand count
for the trefoil structure), the crossings decompose into four
groups:

**Group 1: Virtual pair creation (EM vertex 1).**
Photon $\gamma_1$ couples to the $\dagger$-involution of the
category
([force–knot identification](#rem:force-knot-identification),
§I), creating a virtual $e^-e^+$ pair at the exceptional divisor
$E_p$.  This is an R-II embedding move that introduces a trefoil
and its mirror:

$$
  \underbrace{\sigma_1\sigma_2\sigma_1}_{T_{2,3}\;(e^-_{\mathrm{virt}})}
  \;\cdot\;
  \underbrace{\sigma_1^{-1}\sigma_2^{-1}\sigma_1^{-1}}_{\overline{T_{2,3}}\;(e^+_{\mathrm{virt}})}
  \qquad\text{(6 crossings at } A_1\text{)}
$$

**Group 2: Weak vertex 1 — Skein resolution via $T_{3,5}$.**
The virtual $e^-$ (trefoil $T_{2,3}$, crossing chirality
$Q = -1$) undergoes a Skein crossing change mediated by $T_{3,5}$
([force–knot identification](#rem:force-knot-identification),
§III).  The $T_{3,5}$ braid word contributes its full crossing
structure:

$$
  W_{3,5} \;=\;
  (\sigma_1\sigma_2)^5
  \qquad\text{(10 crossings from the weak mediator)}
$$

The Skein relation at this vertex converts the charged trefoil to
the neutral unknot: $T_{2,3} \xrightarrow{\text{Skein}} T_{1,0}$
($e^- \to \nu$).

**Group 3: Virtual pair creation (EM vertex 2).**
Photon $\gamma_2$ creates a second virtual pair at $E_p$,
identical to Group 1:

$$
  \sigma_1\sigma_2\sigma_1 \;\cdot\;
  \sigma_1^{-1}\sigma_2^{-1}\sigma_1^{-1}
  \qquad\text{(6 crossings at } A_1\text{)}
$$

**Group 4: Weak vertex 2 — Skein resolution via $T_{3,5}$.**
The virtual $e^+$ (mirror trefoil $\overline{T_{2,3}}$) undergoes
the mirror Skein crossing change ($q \leftrightarrow q^{-1}$),
converting $\overline{T_{2,3}} \to \overline{T_{1,0}}$
($e^+ \to \bar{\nu}$):

$$
  W_{3,5}^{-1} \;=\;
  (\sigma_2^{-1}\sigma_1^{-1})^5
  \qquad\text{(10 crossings, mirror orientation)}
$$

**Group 5: Virtual pair annihilation.**
The remaining virtual $e^+$ from Group 1 and virtual $e^-$ from
Group 3 annihilate — an inverse R-II move that cancels their
crossing pairs.  This contributes $0$ net crossings
([Reidemeister action table](#prop:reidemeister-action-table)).

**Full box braid word.**

$$
  \beta_{\mathrm{box}} \;=\;
  \underbrace{(\sigma_1\sigma_2\sigma_1)(\sigma_1^{-1}\sigma_2^{-1}\sigma_1^{-1})}_{\text{virtual pair 1 (6)}}
  \;\cdot\;
  \underbrace{(\sigma_1\sigma_2)^5}_{\text{weak vertex 1 (10)}}
  \;\cdot\;
  \underbrace{(\sigma_1\sigma_2\sigma_1)(\sigma_1^{-1}\sigma_2^{-1}\sigma_1^{-1})}_{\text{virtual pair 2 (6)}}
  \;\cdot\;
  \underbrace{(\sigma_2^{-1}\sigma_1^{-1})^5}_{\text{weak vertex 2 (10)}}
$$

Total: $6 + 10 + 6 + 10 = 32$ crossings before Gröbner
reduction.

*Proof of irreducibility.*

Apply the Gröbner basis $G$ to $\beta_{\mathrm{box}}$:

**(i) Hecke reductions.**  The Hecke relation
$\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ eliminates squares
within the virtual pair groups: $(\sigma_1\sigma_2\sigma_1)
(\sigma_1^{-1}\sigma_2^{-1}\sigma_1^{-1})$ reduces via R-II
cancellation.  After full Hecke reduction, the virtual pair
groups collapse — but the $T_{3,5}$ words $W_{3,5}$ and
$W_{3,5}^{-1}$ **cannot** be eliminated.  The word
$(\sigma_1\sigma_2)^5$ has no adjacent squares (it alternates
$\sigma_1, \sigma_2$), so the Hecke relation does not apply
within it.

**(ii) Yang–Baxter reductions.**  The Yang–Baxter relation
$\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$
can reorder generators within $W_{3,5}$ but cannot reduce the
word length: both sides have the same number of crossings.
Yang–Baxter preserves the crossing count
([Gröbner–Shirshov energy](#prop:groebner-shirshov-energy)).

**(iii) Far commutativity.**  The relation
$\sigma_i\sigma_j = \sigma_j\sigma_i$ for $|i-j| \geq 2$
permutes distant generators.  In $B_3$, the only generators are
$\sigma_1$ and $\sigma_2$ with $|1-2| = 1$, so far commutativity
does not apply at all.

**(iv) No direct $\gamma$–$\nu$ coupling exists.**  A direct
coupling would require a braid word connecting the photon (no
strands) to the neutrino (unknot) without charged intermediaries.
But the photon's electromagnetic interaction is the antisymmetric
component of the crossing energy under the $\dagger$-involution
— it requires nonzero crossing chirality $Q \neq 0$ to couple.
The neutrino has $Q(\nu) = 0$.  No element of $G$ can bridge
this: $G$ preserves the parity of crossing chirality under
reduction (the Hecke relation preserves the symmetric/antisymmetric
decomposition, Yang–Baxter preserves all crossing signs, and far
commutativity is trivial in $B_3$).

**Therefore:** the Gröbner normal form
$\bar{\beta}_{\mathrm{box}}$ retains the full $T_{3,5}$ crossing
content.  The minimum crossing count of the normal form is
$c(\bar{\beta}_{\mathrm{box}}) \geq 10$, with the lower bound
saturated by the irreducible $T_{3,5}$ mediator.  $\square$

**Corollary: neutrino stability.**

The neutrino ($K_{0_1}$, mass $m_\nu \sim \mu_0(q-1)$,
[neutrino](#def:neutrino-knot)) is **stable** — it cannot decay
via any process.

1. **No beta decay.** The neutrino is an elementary knot (unknot)
   with no internal constituents, no crossing orientation partition,
   and no substructure to rearrange
   ([electron immortality](#rem:electron-immortality) applies
   *a fortiori*: the unknot is even simpler than the trefoil).

2. **No scattering decay.** Any decay channel
   $\nu \to \gamma + \cdots$ or $\nu \to \nu' + \cdots$ must
   pass through the box topology (or something at least as
   complex), since the reverse process $\gamma\gamma \to
   \nu\bar{\nu}$ is the simplest $\gamma$–$\nu$ interaction and
   it is irreducible.  The crossing energy of the box
   ($\geq 10$ crossings from $T_{3,5}$) vastly exceeds the
   neutrino's vacuum drag mass $m_\nu \sim \mu_0(q-1)$:

   $$
     E_{\mathrm{box}} \;\geq\;
     10 \cdot (q - q^{-1}) \cdot \mu_0
     \;\gg\;
     m_\nu \;=\; \mu_0(q - 1).
   $$

   The neutrino has no energy budget to generate the irreducible
   box structure.

3. **No simpler process.** The irreducibility of
   $\bar{\beta}_{\mathrm{box}}$ means there is no Gröbner
   reduction path from the box to a lower-crossing process.
   The box is the **minimum topology** for any $\gamma$–$\nu$
   interaction, and it is energetically inaccessible to an
   isolated neutrino.

The neutrino is therefore the **most stable** particle in the
Descartes universe: it has no decay channels at any energy below
the $T_{3,5}$ crossing threshold.  Unlike the electron (which is
stable by topological invariance of the trefoil — it *could*
interact but cannot *decay*), the neutrino is stable by
**energetic inaccessibility of its only interaction channel**.
This is why neutrinos pass through matter virtually unimpeded:
every interaction requires the full box machinery, which is both
topologically irreducible and energetically suppressed.
