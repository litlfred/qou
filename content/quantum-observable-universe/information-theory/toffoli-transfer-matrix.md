**Proposition.**
*Let $P_{\mathrm{flip}}(q; k_1, k_2)$ be the target-flip
amplitude on a $3$-strand nuclear braid with control types
$(k_1, k_2) \in \{0,1\}^2$ and target strand $3$, constructed
from the Hecke crossing coefficients
([transfer matrix product](#prop:skein-polynomial-transfer-matrix)).
Then:*

1. **(Universal factorization.)** *Every target-flip amplitude
   factors as*

$$
  P_{\mathrm{flip}}(q; k_1, k_2)
  = 
  c_{k_1 k_2}(q)  \cdot  \Phi(q)
$$

*where $c_{k_1 k_2}$ is the crossing coefficient of the
**control–control pair** (the two strands that do not flip)
and $\Phi(q)$ is a **universal core amplitude** independent
of the control types:*

$$
  \Phi(q)
  = 
  \frac{
    (q - 1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1)
  }{
    2(q + 1)^2
  }
$$

| Control pair | $c_{k_1 k_2}$ | $d_{k_1 k_2}$ |
|:------------:|:--------------:|:--------------:|
| $\mathfrak{p}\mathfrak{p}$ | $1$ | $0$ |
| mixed | $1$ | $-\frac{q - q^{-1}}{2}$ |
| $\mathfrak{n}\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ |

2. **(Single-crossing type-blindness.)** *At generator
   $\sigma_1$ (one crossing), the traced volume
   $\hat{V}_1 = z(q) = 1/(q^{1/2} + q^{-1/2})$ regardless
   of crossing type.  A single crossing carries no type
   information: $\Delta_1 = 0$ for every transition.  The
   entire target-flip amplitude is concentrated at generator
   $\sigma_0$ (whose chain has $2$ crossings).*

3. **(The q-AND = governor choice.)** *The Toffoli gate
   selects the target strand whose control–control pair has
   $c = 1$ ($\mathfrak{p}\mathfrak{p}$ crossing).  Among
   the $S_3$ orbit of target choices in the exceptional
   divisor, this is the **governor basis** — the choice
   with unit prefactor:*

$$
  P_{7,6}(q) = 1 \cdot \Phi(q)
  = \frac{(q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1)}{2(q+1)^2}
$$

4. **(Antisymmetry.)** $P_{6,7}(q) = -P_{7,6}(q)$.*

5. **(Classical limit.)** *All target-flip amplitudes vanish
   as $q \to 1$: the core $\Phi(q)$ carries the factor
   $(q - 1)$.*

6. **(Toffoli diagonal.)**

$$
  P_{7,7}(q) = \frac{q + q^{1/2} - 1}{q + 1}
$$

*This entry vanishes at $q = 1/\varphi^2$
([golden ratio degeneration](#rem:golden-ratio-degeneration)):
the all-proton diagonal amplitude has a zero at the golden
ratio threshold.*

**Explicit values at $q = q_0$
([local substrate $q$](#prop:local-substrate-q)):**

| Controls | $c_{k_1 k_2}$ | $P_{\mathrm{flip}}$ | $P_{7,6}$ ratio |
|:--------:|:-----------:|:-------------------:|:---:|
| $\mathfrak{p}\mathfrak{p}$ | $1$ | $+0.0495$ | $1\times$ |
| mixed | $1$ | $+0.0495$ | $1\times$ |
| $\mathfrak{n}\mathfrak{n}$ | $1$ | $+0.0495$ | $1\times$ |

| Entry | Symbolic | Numerical |
|:-----:|----------|:---------:|
| $P_{6,6}$ | $\frac{q^4 + q^{7/2} + 2q^{3/2} + q^{1/2} - 1}{2(q+1)^2}$ | $0.6010$ |
| $P_{7,6}$ | $\Phi(q)$ (q-AND) | $+0.0495$ |
| $P_{6,7}$ | $-\Phi(q)$ | $-0.0495$ |
| $P_{7,7}$ | $\frac{q + q^{1/2} - 1}{q + 1}$ | $0.5515$ |
