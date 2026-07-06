**Tritium beta decay written as a knot/link equation.**

The decay ${}^3_1\mathrm{H} \to {}^3_2\mathrm{He} + e^- +
\nu_e^{\sigma}$ (half-life $\approx 12.3$ yr) is the simplest
non-trivial beta decay: $A = 3$, one neutron converts to a
proton.

**The nuclear links.**

Tritium $\mathcal{N}(1, 2)$ has $A = 3$ nucleons:

$$
  {}^3\mathrm{H}
  = 
  \underbrace{\mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})}_{\mathfrak{p}}
   \bowtie_{\mathrm{Hopf}}
  \underbrace{\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})}_{\mathfrak{n}_1}
   \bowtie_{\mathrm{Hopf}}
  \underbrace{\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})}_{\mathfrak{n}_2}
$$

Helium-3 $\mathcal{N}(2, 1)$ has the same $A = 3$:

$$
  {}^3\mathrm{He}
  = 
  \underbrace{\mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})}_{\mathfrak{p}_1}
   \bowtie_{\mathrm{Hopf}}
  \underbrace{\mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})}_{\mathfrak{p}_2}
   \bowtie_{\mathrm{Hopf}}
  \underbrace{\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})}_{\mathfrak{n}}
$$

Each $\mathcal{B}_3$ is a Borromean link (3 quark strands),
and $\bowtie_{\mathrm{Hopf}}$ is the Hopf junction between
nucleons.

**The braid words in $B_9$.**

With $3A = 9$ strands (3 per nucleon):

Tritium parent (proton on strands 0-2, neutrons on 3-5 and 6-8):

$$
  \beta_{\mathrm{par}}
  = 
  (\sigma_1 \sigma_2^{-1})^3
  \cdot (\sigma_4 \sigma_5^{-1})^3
  \cdot (\sigma_7 \sigma_8^{-1})^3
  \cdot \text{(inter-nucleon crossings)}
$$

The internal Borromean crossings at strands 0-2 have types:
$\sigma_1$: $u$-$u$ (positive), $\sigma_2$: $u$-$d$ (mixed).

For the neutron at strands 3-5:
$\sigma_4$: $u$-$d$ (mixed), $\sigma_5$: $d$-$d$ (negative).

**The Skein crossing change.**

In $\beta^-$ decay, one neutron (say $\mathfrak{n}_1$ on
strands 3-5) converts to a proton. This changes the quark
content $\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d}) \to \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$:
one $d$-quark strand becomes a $u$-quark strand.

The crossing change occurs at the internal $d$-$d$ crossing
of $\mathfrak{n}_1$, at generator $\sigma_5$. Before: $d$-$d$
(negative crossing). After: $u$-$d$ (mixed crossing).

The **knot equation** for the decay:

$$
  q  [\mathcal{N}(1, 2)]
  - 
  q^{-1} [\mathcal{N}(2, 1)]
  = 
  (q^{1/2} - q^{-1/2})
  \left[
    T_{2,3} \sqcup K_{0_1}
  \right]
$$

In expanded link notation:

$$
  q \Big[
    \mathcal{B}_3^{uud}
    \oplus \mathcal{B}_3^{udd}
    \oplus \mathcal{B}_3^{udd}
  \Big]
  - 
  q^{-1} \Big[
    \mathcal{B}_3^{uud}
    \oplus \mathcal{B}_3^{uud}
    \oplus \mathcal{B}_3^{udd}
  \Big]
  = 
  (q^{1/2} - q^{-1/2})
  \Big[
    T_{2,3} \sqcup K_{0_1}
  \Big]
$$

**Markov trace of the transition.**

The factored Markov trace
([factorization theorem](#thm:markov-trace-factorization))
gives the parent and daughter traces as products over generators:

$$
  \mathrm{tr}(\mathcal{N}(1,2))
  = \prod_{i=0}^{7} (z \cdot a_i^{\mathrm{par}} + b_i^{\mathrm{par}})
$$

$$
  \mathrm{tr}(\mathcal{N}(2,1))
  = \prod_{i=0}^{7} (z \cdot a_i^{\mathrm{dau}} + b_i^{\mathrm{dau}})
$$

The traces differ only at generators $\sigma_4$ and $\sigma_5$
(the internal generators of the converting nucleon). At $\sigma_5$:

- Parent: $d$-$d$ crossing $\Rightarrow$ $(c, d) = (q^2, -q(q^{1/2} - q^{-1/2}))$
- Daughter: $u$-$d$ crossing $\Rightarrow$ $(c, d) = ((1 + q^2)/2, -q(q^{1/2} - q^{-1/2})/2)$

**The $Q$-value in pair Skein units.**

The $Q$-value is the difference in categorical actions.
At the converting crossing:

$$
  \Delta \mathcal{S}
  = 
  \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)
  = 
  \frac{q \mu_{\mathfrak{d}} + q^{-1} \mu_{\mathfrak{d}}}{q^{1/2} + q^{-1/2}}
  - 
  \frac{q \mu_{\mathfrak{u}} + q^{-1} \mu_{\mathfrak{d}}}{q^{1/2} + q^{-1/2}}
$$

$$
  = 
  \frac{(q - 1)(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}) + q^{-1}(\mu_{\mathfrak{d}} - \mu_{\mathfrak{d}})}{q^{1/2} + q^{-1/2}}
  = 
  \frac{q(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})}{q^{1/2} + q^{-1/2}}
$$

Wait — this needs the full pair Skein difference, not the
converting crossing. The re-reduction of the braid word after
the crossing change also affects the inter-nucleon crossings:
changing the quark flavour of strand 5 from $d$ to $u$ modifies
every inter-nucleon crossing involving that strand.

**Inter-nucleon crossing changes.**

Strand 5 (was $d$, now $u$) crosses with strands from the other
two nucleons. Each of those crossings changes type:

- Strand 5 $\times$ proton strands (0,1,2): was $d$-$u$/$d$-$u$/$d$-$d$,
 now $u$-$u$/$u$-$u$/$u$-$d$
- Strand 5 $\times$ neutron-2 strands (6,7,8): was $d$-$u$/$d$-$d$/$d$-$d$,
 now $u$-$u$/$u$-$d$/$u$-$d$

These 6 inter-nucleon crossing changes, plus the 1 internal
crossing change at $\sigma_5$, give 7 modified crossings total.
The $Q$-value is the sum of pair Skein differences at all 7:

$$
  \mathfrak{Q}_\beta
  = 
  \sum_{k \in \text{modified}} \left(
    \mathcal{S}_{a_k b_k}^{\mathrm{par}}(q)
    - \mathcal{S}_{a_k b_k}^{\mathrm{dau}}(q)
  \right)
  -  m_e
$$

This is the exact knot equation for the tritium $Q$-value:
no approximation, no fitted parameter. Every term is determined
by $q_0$ and the quark content of the nucleons.
