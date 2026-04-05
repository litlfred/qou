The **categorical probability of QOU existence** is the ratio
in the localized Grothendieck ring:

$$
  \mathrm{Prob}_q(\mathrm{QOU})
  \;:=\; \frac{\mu_q(\mathfrak{M}_{\mathrm{QOU}})}
              {\mu_q(\mathfrak{M}_{\mathrm{QO}})}
  \;\in\; K_0(\mathbf{C})[L_q^{-1}]
$$

This is not a real number but an element of $K_0(\mathbf{C})$ —
"logical existence as a categorical quantity" in the sense of
Denef–Loeser. It measures: given a random quantum observable
(a Frobenius–Hopf object in a rigid monoidal category), what
fraction of the [moduli](#def:qo-moduli) satisfies the full
[QOU axioms](#def:qou-locus)?

The [axiom filtration](#def:qou-locus) gives a factorisation:

$$
  \mathrm{Prob}_q(\mathrm{QOU})
  \;=\; \mathrm{Prob}_q(\mathrm{obs})
  \;\cdot\; \mathrm{Prob}_q(\mathrm{meas} \mid \mathrm{obs})
  \;\cdot\; \mathrm{Prob}_q(\mathrm{vol} \mid \mathrm{meas})
$$

where:

1. $\mathrm{Prob}_q(\mathrm{obs})
   = \mu_q(\mathfrak{M}_{\mathrm{obs}}) /
     \mu_q(\mathfrak{M}_{\mathrm{QO}})$ — the probability
   that $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
   This is the "largest" cut: it kills the Lie algebra of
   $\mathrm{Aut}^\otimes(\tau)$, eliminating continuous
   automorphism families. Motivic codimension:
   $[\mathrm{Ad}(A)^{\mathbf{1}}]$.

2. $\mathrm{Prob}_q(\mathrm{meas} \mid \mathrm{obs})
   = \mu_q(\mathfrak{M}_{\mathrm{meas}}) /
     \mu_q(\mathfrak{M}_{\mathrm{obs}})$ — the conditional
   probability of anomaly cancellation ($c_1 = c_2 = 0$)
   given observability. Motivic codimension:
   $[H^2(\mathbf{C}, \mathbb{G}_m)]$.

3. $\mathrm{Prob}_q(\mathrm{vol} \mid \mathrm{meas})
   = \mu_q(\mathfrak{M}_{\mathrm{QOU}}) /
     \mu_q(\mathfrak{M}_{\mathrm{meas}})$ — the conditional
   probability of the volume constraint
   ($\Lambda^2 V \twoheadrightarrow \mathbf{1}$) given
   measurability. This pins $G = \mathrm{SU}(2)$. Motivic
   codimension: $[\mathrm{GL}(V) / \mathrm{SU}(V)]$.

The [axiom independence](#rem:axiom-independence) result ensures
the factors are genuinely multiplicative — the axioms cut
**transversely** in the motivic sense.

**Explicit values.** By the
[motivic Euler characteristic](#prop:qou-motivic-euler), the
numerator is a four-term sum over divisors of $\chi(A) = -6$.
The Yekutieli obstruction class $\kappa_0$ with
$\mathrm{tr}(\kappa_0) = -6$ forces:

$$
  \mu_q(\mathfrak{M}_{\mathrm{QOU}})
  \;=\; \sum_{d \mid 6}
  \mu_q(\mathfrak{M}_{\mathrm{QOU}}^{(d)}) \cdot L_q^{-d}
$$

At each surviving Kummer level $d \in \{1, 2, 3, 6\}$, the
motivic contribution is:

$$
  \mu_q(\mathfrak{M}_{\mathrm{QOU}}^{(d)})
  \;=\; \frac{[\mathrm{pt}]}{[\mathrm{Aut}^{(d)}]}
  \;=\; \frac{1}{|\mu_d(\kappa_0)|}
  \;\cdot\; [\mathrm{pt}]
$$

where $\mu_d(\kappa_0)$ is the $d$-th Kummer reduction of
$\kappa_0$ and $|\mu_d(\kappa_0)|$ counts the residual
automorphisms at level $d$.

The denominator $\mu_q(\mathfrak{M}_{\mathrm{QO}})$ encodes the
full continuous moduli of Frobenius–Hopf objects. The ratio is
therefore "small" — the QOU locus is **discrete inside a
continuous moduli** — yet non-zero.

In the archimedean case, $\chi_{\mathrm{mot}}
(\mathfrak{M}_{\mathrm{QOU}}^{\mathrm{arch}}) = [\mathrm{pt}]$,
so the probability reduces to:

$$
  \mathrm{Prob}_q^{\mathrm{arch}}(\mathrm{QOU})
  \;=\; \frac{[\mathrm{pt}]}
              {\mu_q(\mathfrak{M}_{\mathrm{QO}}^{\mathrm{arch}})}
$$

The QOU exists with "probability zero yet necessarily" — the
locus is measure-zero but non-empty, and once found, completely
rigid.
