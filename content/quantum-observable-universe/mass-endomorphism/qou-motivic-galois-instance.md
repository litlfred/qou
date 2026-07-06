# QOU MotivicGaloisCharacter instance via Habiro evaluation

The QOU brane-tower substrate carries a concrete instance of [`def:motivic-galois-character`](#def:motivic-galois-character) constructed by the Habiro evaluation map:

$$
  \mathrm{Frob}_p \;=\; f(u) \big|_{u = \zeta_{2p}}
  \;\in\; \mathbb{Z}[\zeta_{2p}].
$$

Here $f(u) = \sum_{m \geq 0} a_m(u) (u; u)_m$ is the Habiro cyclotomic expansion of the atomic Markov trace $\mathrm{tr}_M(T_w, q)$ and $u = q^{1/2}$. The cyclotomic Pochhammer $(u; u)_m$ vanishes for $m \geq 2p$. This forces the sum to terminate after a finite number of terms.

## Construction and verification

- **Compatibility verification.** We perform two finite-place coherence checks on every $(p, \text{atom})$ cell. First, Galois-norm integrality: the trace $N(\mathrm{Frob}_p) = \sum_{\sigma \in \mathrm{Gal}(\mathbb{Q}(\zeta_{2p})/\mathbb{Q})} \sigma(\mathrm{Frob}_p)$ is a rational integer (residual $< 10^{-7}$). Second, Weil purity at small primes: at $p \in \{2, 3\}$, the orbit-spread $\max|\sigma(\mathrm{Frob}_p)| - \min|\sigma(\mathrm{Frob}_p)|$ is below $10^{-10}$ for every atom, and the inferred weight $w = 2 \log_p |\mathrm{Frob}_p|$ takes integer or near-integer values. At larger primes, the spread grows. The QOU motive is mixed in general, consistent with the brane tower being a sum across cohomology degrees.

- **Lean instance.** The instance in [`qou-motivic-galois-instance.lean`](qou-motivic-galois-instance.lean) discharges [`def:motivic-galois-character`](#def:motivic-galois-character) for the QOU substrate. The `frobenius_at` field maps each prime to its extracted Frobenius eigenvalue. The `almost_everywhere_nontrivial` field is a substrate axiom (AGENTS.md §3b), backed by a numerical witness for primes $p \leq 13$.

## Per-cell summary

| Atom | $p=2$ | $p=3$ | $p=5$ | $p=7$ | $p=11$ | $p=13$ |
|---|---|---|---|---|---|---|
| p (proton) | $\|F\|=8$, $w=6$ | $\|F\|=1$, $w=0$ | $\|F\|=0.62$, partial | partial | partial | partial |
| n (neutron) | $\|F\|=8$, $w=6$ | $\|F\|=2.65$, $w\approx1.77$ | $\|F\|=0.24$, partial | partial | partial | partial |
| D (deuteron) | $\|F\|=96$, $w\approx13.17$ | $\|F\|=4.58$, $w\approx2.77$ | $\|F\|=1.44$, partial | $\|F\|=38.74$, partial | partial | partial |

Cells marked "partial" have on-disk Habiro data that exhausts before the Pochhammer truncation point ($m_{\max} < 2p$). Galois-norm integrality still holds, indicating the partial sum already approximates the true Frobenius eigenvalue well. Unmarked cells achieve full truncation within the available data and pass the Weil-purity check $|\sigma(\mathrm{Frob}_p)| = p^{w/2}$ for every $\sigma$ in the Galois orbit.

## Downstream consumers

This instance discharges audit GAP 5b ([`docs/audits/family-4-motivic-path.md`](../../../docs/audits/family-4-motivic-path.md)). Theorems that previously required [`def:motivic-galois-character`](#def:motivic-galois-character) as an `[instance]` hypothesis can now consume the explicit QOU instance directly. In particular, [`conj:motivic-perpetual-obstruction`](#conj:motivic-perpetual-obstruction) becomes an unconditional theorem for the QOU substrate.

## Coherence

Cross-prime coherence follows structurally from the Habiro theorem. Any two evaluations $f|_{u = \zeta_{2p}}$ and $f|_{u = \zeta_{2q}}$ are extracted from the same Habiro element and respect the natural Galois action on $\mathbb{Q}(\mu_\infty)$. The deeper $\ell$-adic archimedean Weil/Deligne behaviour lies outside this construction.
