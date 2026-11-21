The shell energy scale $\lambda_{\mathrm{shell}}$ ([Skein shell correction](#rem:skein-shell-correction)) corresponds to the crossing energy of the Skein smoothing $L_0$ at the beta-decay vertex. This threading link interpolates between the parent and daughter nuclear configurations.

**Setup.**

The Skein relation at a single crossing change is

$$
  q  [L_+] -  q^{-1} [L_-]
  = 
  (q^{1/2} - q^{-1/2})  [L_0].
$$

In beta decay $\mathcal{N}(Z, N) \to \mathcal{N}(p\!+\!1, n\!-\!1)$, a neutron $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p$ becomes a proton $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p$. This operates as a Skein crossing change on the $\mathfrak{d} \to \mathfrak{u}$ quark strand inside one nucleon. The terms in the Skein relation evaluate as follows.

- $L_+$ is the parent configuration $\mathcal{N}(Z, N)$ (positive crossing at the $d$-quark site).
- $L_-$ is the daughter configuration $\mathcal{N}(p\!+\!1, n\!-\!1)$ (negative crossing after the $\mathfrak{d} \to \mathfrak{u}$ flip).
- $L_0$ is the smoothing. This threading link interpolates between parent and daughter.

**Conjecture.**
*The shell energy scale equals the crossing energy of the threading link $L_0$.*

The shell energy is determined by the pair Skein mass $\mathcal{S}_{ab}(q)$ evaluated on the threading link $L_0$, using the terminal resolution ([terminal resolution](#prop:terminal-resolution)).

**The threading link $L_0$.**

The smoothing $L_0$ resolves the crossing between the converting quark strand and the surrounding nuclear link. Its topology depends on the local linking structure around the converting nucleon.

For a nucleus where the converting neutron sits inside a closed sub-link (shell closure), $L_0$ threads through that closed sub-link. The threading link's Alexander polynomial encodes the shell structure:

- **No shell closure.** At generic position, $L_0$ is a simple unknotted strand. Then $\Delta_{L_0}(q) = 1$ and $\lambda_{\mathrm{shell}} = E_{\mathrm{Hopf}}$ (the baseline Hopf junction energy). This yields no shell correction.
- **At a shell closure.** When $n$ or $p$ is magic, $L_0$ threads through the closed sub-link and acquires a nontrivial Alexander polynomial. The shell energy exceeds the baseline.

**Example: ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$.**

The parent $\mathcal{N}(6, 8)$ has a magic neutron number $n = 8$. The 8 neutrons form a closed sub-link (the $p$-shell closure). The converting neutron sits inside this closure. The smoothing $L_0$ threads through the remaining 7 nucleons of the closed sub-link and the 6 protons of the core.

Three factors determine the topology of $L_0$ for this transition:

1. The linking structure of the $n = 8$ sub-link (the arrangement of the 4 neutron pairs relative to the 3 $\alpha$-clusters of the ${}^{12}\mathrm{C}$ core).
2. The number of crossings between the converting strand and the closed sub-link.
3. The braid word of the threading in $B_A$.

**Two-level structure of $L_0$.**

The Skein resolution at the beta-decay vertex carries two levels.

*Level 1: Internal (Borromean).*

The crossing change $\mathfrak{d} \to \mathfrak{u}$ inside $\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ is a Skein resolution at the $d$-$d$ crossing of the Borromean link. Smoothing one crossing in $\mathcal{B}_3$ produces the Hopf link $\mathcal{L}_H$. In the Temperley--Lieb algebra $TL_3(\delta)$ with $\delta = -(q^{1/2} + q^{-1/2})$, the smoothing is the generator $e_i$. Its Markov trace involves the quantum integer ratio:

$$
  \frac{\mathrm{tr}(L_0^{\mathrm{int}})}{\mathrm{tr}(e_i^{\mathrm{free}})}
  = 
  \frac{[1]_q  [2]_q}{[3]_q}
   \approx  0.665
  \quad\text{at } q = q_0.
$$

This represents the intrinsic Borromean suppression. The Borromean link resists the internal crossing change by a factor of $[1]_q [2]_q / [3]_q$.

*Level 2: External (nuclear environment).*

The resulting $L_0 = \mathcal{L}_H$ embeds in the multi-nucleon link $\mathcal{N}(Z, N)$. It threads through $Z$ protons and $n - 1$ remaining neutrons. The threading modulates the Markov trace by a factor depending on the shell structure of the nuclear environment:

- **Open configuration.** Without a shell closure, the inter-nucleon crossings commute with $L_0$ in the TL algebra. This introduces no additional modulation. The external factor is $1$.
- **Closed shell.** When $n$ or $p$ sits at a magic number, the inter-nucleon crossings form a chain of non-commuting TL generators adjacent to $L_0$. The Markov trace picks up a factor $f(m, k, q)$ depending on the chain length $m$ and the position $k$ of the converting nucleon within the shell.

The total shell correction is the product of the Borromean suppression and the shell modulation:

$$
  \text{shell factor}
  = 
  \underbrace{\frac{[1]_q  [2]_q}{[3]_q}}_{\text{Borromean factor}}
   \times 
  \underbrace{f(m, k, q)}_{\text{shell modulation}}
$$

Both factors are determined by $q$ and the nuclear braid topology.

**Computations required.**

1. **The external modulation $f(m, k, q)$.** Write the braid word for $\mathcal{N}(6, 8)$ with the converting neutron at position $k$ in the $n = 8$ shell chain. Then compute the Markov trace of the $L_0$ generator $e_k$ embedded in this word.
2. **The crossing matrix.** The $14 \times 14$ crossing matrix of $\mathcal{N}(6, 8)$ has 15 positive ($\mathfrak{p}$-$\mathfrak{p}$), 28 negative ($\mathfrak{n}$-$\mathfrak{n}$), and 48 mixed ($\mathfrak{p}$-$\mathfrak{n}$) crossings. The product $p \times n$ goes from 48 to 49 across the transition, creating one mixed crossing. The smoothing $L_0$ mediates this extra crossing.
3. **Verification.** The corrected half-life should match the observed 5730 yr to within $\sim 5\%$.
4. **Universality.** The same two-level construction applied to ${}^{60}\mathrm{Co}$, ${}^{137}\mathrm{Cs}$, and ${}^{210}\mathrm{Bi}$ should reproduce the observed residuals through the shell modulation factor $f(m, k, q)$.

Under this conjecture, the shell energy is the crossing energy of a computable knot invariant rather than a free phenomenological parameter.
