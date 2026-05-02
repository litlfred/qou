**Statement.**
*The character expansion underlying the
[three-invariant mass formula](#thm:wedderburn-mass-formula) is the
**inverse non-commutative Fourier transform** on $H_n(q)$ in the sense
of Peter--Weyl/Plancherel for finite-dimensional semisimple algebras.*

For $q$ generic, $H_n(q)$ is semisimple and the Wedderburn--Artin
decomposition reads

$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n} \operatorname{End}_{\mathbb{C}}(V_\lambda),
$$

where $\lambda$ ranges over partitions of $n$ and $V_\lambda$ is the
Specht module with $\dim V_\lambda = d_\lambda$. The Markov trace
$\operatorname{tr}_M : H_n(q) \to \mathbb{C}$
([Jones--Markov trace](#thm:jones-markov-trace))
admits the spectral expansion

$$
  \operatorname{tr}_M(\beta)
  \;=\;
  \sum_{\lambda \vdash n}
  w_\lambda \,\frac{\chi_\lambda(\beta)}{d_\lambda},
\qquad
\beta \in H_n(q),
$$

where $\chi_\lambda$ is the irreducible character on the $\lambda$-block
and $\{w_\lambda\}$ are the Markov weights (Jones--Ocneanu coefficients).

**Identification.** Reading $\widehat{H_n(q)} = \{\lambda \vdash n\}$ as
the *non-commutative spectrum*:

| Commutative side ($S^1$ or $U(1)$) | Non-commutative side ($H_n(q)$) |
|:--|:--|
| Frequency $k \in \mathbb{Z}$ | Partition $\lambda \vdash n$ |
| Fourier coefficient $\widehat{f}(k)$ | Character value $\chi_\lambda(\beta)$ |
| Plancherel measure $dk$ | Quantum dimension weight $w_\lambda / d_\lambda$ |
| $f = \sum_k \widehat{f}(k)\,e^{ik\theta}$ | $\operatorname{tr}_M(\beta) = \sum_\lambda w_\lambda \chi_\lambda(\beta)/d_\lambda$ |

The role of $\operatorname{tr}_M$ is the inverse-transform: it
*reassembles* a class function on $H_n(q)$ from its non-commutative
Fourier coefficients $\{\chi_\lambda(\beta)\}_\lambda$.

**Why this is just a renaming.** Nothing new is asserted: this is
exactly the Peter--Weyl/Plancherel formula for the finite-dimensional
semisimple algebra $H_n(q)$, applied to the trace functional
$\operatorname{tr}_M$. The proposition is included because the
"non-commutative Fourier transform" reading clarifies how downstream
results — in particular the
[three-invariant mass formula](#thm:wedderburn-mass-formula) and
the
[Markov trace product factorization](#thm:markov-trace-product)
— *select* a finite set of partitions
$\{\lambda\} \subseteq \widehat{H_n(q)}$ as physical mass channels.

**Scope.** The identification holds whenever $H_n(q)$ is semisimple,
i.e. for $q$ not a non-trivial root of unity. At roots of unity the
spectrum collapses to the *fusion category* $\widehat{H_n(q)}^{ss}$;
the proposition still holds for the surviving simple objects, but the
sum is restricted to the truncated index set. Throughout the QOU mass
formula we evaluate at the substrate parameter $q_0$, which is in the
generic locus, so the full Wedderburn decomposition applies.

**No new physics.** This proposition does not change any computed
quantity. It supplies the conceptual hook for the Pieri-shift
behaviour of the
[degree-one Hecke photon](#prop:pieri-photon-shift) and for the
spectral interpretation of the
[archimedean remainder](#conj:archimedean-remainder-exponential-decay):
both are statements about which partitions $\lambda$ contribute at a
given filtration depth.
