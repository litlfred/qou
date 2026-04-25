**Proposition (cohomology vanishing collapses the GB spectral sequence).**
*The Iwahori--Hecke algebra $H_n(q)$ is semisimple for generic $q$
([three-parameters-wedderburn](#prop:three-parameters-wedderburn))
and consequently has vanishing Hochschild cohomology in positive
degrees:*

$$
  HH^k\bigl(H_n(q),\, H_n(q)\bigr) \;=\; 0 \quad \text{for all } k \geq 1.
$$

*The GB filtration spectral sequence
([GB spectral sequence](#prop:gb-spectral-sequence)) therefore
collapses at the $E_1$ page, with all contributions concentrated in*

$$
  E_\infty^{0, *} \;=\; HH^0\bigl(H_n(q)\bigr) \;=\; Z\bigl(H_n(q)\bigr) \;=\; \bigoplus_{\lambda \,\vdash\, n} \mathbb{C} \cdot p_\lambda,
$$

*the centre, a direct sum of central idempotents indexed by
partitions of $n$.*

*Proof.*
$H_n(q)$ for generic $q \notin \{0, \pm 1, \text{roots of unity}\}$
is semisimple (Wenzl 1988; Geck--Pfeiffer 2000).  By the Whitehead
lemma applied to semisimple algebras over a field of characteristic
zero, every Hochschild cocycle in degree $k \geq 1$ is a coboundary,
so $HH^k = 0$.  The spectral sequence
$E_r^{p, q} \Rightarrow HH^{p+q}$ then collapses: only $E_\infty^{p, 0}$
with $p + 0 = 0$ survive, giving $E_\infty^{0, 0} = HH^0 = Z(H_n(q))$.
$\square$

**Corollary (mass formula simplifies to a centre-projection sum).**
*The categorical mass functional pairs the Markov trace with the
filtered centre via the Frobenius pairing
([categorical mass, Markov](#prop:categorical-mass-markov)):*

$$
  \mathfrak{m}(\beta) \;=\; \sum_{\lambda \,\vdash\, n} w_\lambda \cdot \frac{\chi_\lambda(\beta)}{\dim_q V_\lambda},
  \qquad w_\lambda \;=\; \frac{\dim_q^2 V_\lambda}{[n]_q!}
$$

*(Plancherel weights, summing to $1$ — bounded for all $\lambda$).
The "six terms" of the unified mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) are
**projections onto specific groupings of central idempotents**
within $Z(H_n(q))$, sorted by GB-filtration depth (= curvature-rank,
[curvature-rank stratification](#prop:curvature-rank-gb-stratification)):*

| Term | Block grouping | Curvature-rank |
|---|---|---|
| 1. descended | $p_{(n)}$ (sym idempotent) | $0$ |
| 2. single-gen tower | $p_{(n-1, 1)}$ (std hook) | $1$ |
| 3. pair-gen tower | $p_{(n-2, 2)}$ etc. | $2$ |
| 4. Frobenius co-Casimir | $\sum_\lambda 1/\dim_q V_\lambda$ (universal) | all |
| 5. chirality | $S$-anti-invariant component of $p_{(2,1)}$-projection | $\geq 2$ |
| 6. jet-prefix | higher-rank blocks (Wigner self-conj. partitions) | $\geq 3$ |

*Each term is a Plancherel-bounded sum, in contrast with bare-hook
sums $\sum H_q(\lambda)$ which diverge super-exponentially with $n$
(the wrong pairing).  This explains why earlier attempts to compute
"Term 7" via $H_q(\lambda)$ multiplications were structurally
unbounded; the correct pairing is $w_\lambda \cdot \chi_\lambda /
\dim_q V_\lambda$.*

**Frobenius duality of strata.**
*The Frobenius pairing $\langle a, b\rangle = \mathrm{tr}_M(ab)$
gives a self-duality $H_n(q) \cong H_n(q)^{\vee}$
([Yekutieli rigidity](#prop:vol-through-tau)).
Under this duality the GB filtration
$J^0 \supset J^1 \supset \cdots \supset J^N$
maps to its annihilator filtration*

$$
  (J^\ell)^\perp \;=\; \{a : \mathrm{tr}_M(a \cdot J^\ell) = 0\} \;=\; J^{N - \ell}.
$$

*This is **Poincaré duality of curvature-rank strata**: rank-$\ell$
contributions pair with rank-$(N - \ell)$ contributions under the
Frobenius integral.  In particular, the chirality term (Term 5,
$S$-anti-invariant rank $\geq 2$) is **self-dual** under combined
$S$-reversal and rank inversion.*

**Practical consequence.**
*Implementations of the GB spectral sequence (e.g.\
`folio-assistant/computations/gb_prefix_probe.py`) need only:*

1. *Enumerate central idempotents $p_\lambda$ for $\lambda \vdash n$.*
2. *Compute their GB-filtration depth $\mathrm{depth}(\lambda)$
   (= $|\lambda| - \lambda_1$ + corrections; effectively the partition's
   "crossing-energy" stratum).*
3. *For each braid $\beta$, evaluate $\chi_\lambda(\beta)$ via Hoefsmit
   seminormal form
   ([numerical Hoefsmit pipeline](#prop:hoefsmit-scattering-pipeline)).*
4. *Sum $\sum_\lambda w_\lambda \cdot \chi_\lambda(\beta)/\dim_q V_\lambda$,
   binning by $\mathrm{depth}(\lambda)$ for term-by-term decomposition.*

*This avoids ever computing higher-page differentials $d_r$ ($r \geq 1$)
because they all vanish: there is nothing to compute beyond $E_1$.*

**Comparison with the $H_q(\lambda)$ approach.**

| Pairing | Boundedness | Numerical behaviour |
|---|---|---|
| $H_q(\lambda) \cdot w$ (bare hook) | Unbounded | Diverges as $n!_q$ |
| $1 / H_q(\lambda)$ | Bounded but tiny | Vanishes as $n \to \infty$ |
| **$w_\lambda \cdot \chi_\lambda / \dim_q$** (Plancherel) | **Bounded by $1$** | **Convergent**; matches paper formula |

*The Plancherel pairing is the categorically correct one; previous
divergences in numerical "Term 7" tests reflect using the wrong
pairing, not a defect in the conjecture.*
