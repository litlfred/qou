**Conjecture (symmetric-channel Plancherel normalization).**
*The closed-form expression for $N_v$ in
[`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness)
takes the form*

$$
  N_v
  \;=\;
  \biggl(\prod_{k = 2,3,4} \frac{[2k]_q^{\,2}}{[2]_q}\biggr)
  \cdot
  \mathcal{N}_{\rm sym}(q),
$$

*where $\mathcal{N}_{\rm sym}(q)$ is the
**symmetric-channel Plancherel normalization** of the EW/Higgs
sector — a categorical scalar in $\mathbb{Q}(q)$ analogous to
$\delta_{\rm CS} = \hbar_q^4 \cdot [5]_q$ in*
[`rem:alpha-em-categorical-trace`](#rem:alpha-em-categorical-trace).
*Its value at $q_0$ is fixed by consistency with CODATA $G_F$:*

$$
  \mathcal{N}_{\rm sym}(q_0)
  \;=\;
  \frac{N_v}{\prod_k [2k]_q^{\,2}/[2]_q\bigm|_{q_0}}
  \;=\;
  213.111807\ldots
$$

*(numerically pinned; closed form open).*

### Numerical anchor

At $q_0 = :val[q_0]{precision=6}\ldots$:

| factor | value |
|--------|------:|
| $[4]_q^2/[2]_q$ | 8.39825 |
| $[6]_q^2/[2]_q$ | 20.28859 |
| $[8]_q^2/[2]_q$ | 39.79412 |
| $\prod_k [2k]_q^2/[2]_q$ | 6782.916 |
| $N_v$ (from CODATA $G_F$) | 1,445,519.45 |
| $\mathcal{N}_{\rm sym}(q_0) = N_v / \prod$ | **213.1118** |

### Best q-arithmetic ansatze (probed 2026-05-02)

PSLQ at 50–1000 dps over the basis $\{q^k, [k]_q, \hbar_q^k, \text{small primes}\}$ finds **no** clean closed form for $\mathcal{N}_{\rm sym}(q_0)$. Closest small-form ansatze:

| ansatz | value at $q_0$ | rel err vs $\mathcal{N}_{\rm sym}$ |
|--------|------:|-----:|
| $[7]_q \cdot [8]_q \cdot [3]_q$ | 207.62 | **2.58%** |
| $45 \cdot [5]_q$ | 234.92 | 10.23% |
| $[5]_q!$ | 131.31 | 38.38% |
| $[6]_q^2 [7]_q [8]_q / [10]_q$ | 234.03 | 9.82% |

The leading candidate $[7]_q[8]_q[3]_q$ is suggestive but 2.6%-off — about $25\sigma$ relative to CODATA $G_F$ uncertainty ($\sim 5\times 10^{-7}$). So either:

1. The closed form is $[7]_q[8]_q[3]_q \cdot (1 + \delta_{\rm sym})$ with a small categorical correction $\delta_{\rm sym} \approx 0.0264$ (parallels $1/\alpha$'s $\delta_{\rm CS}$ correction), **or**
2. The closed form involves *non-q-arithmetic* substrate quantities (e.g., genus-counts, partition counts, Plancherel ratios) that aren't in the simple basis.

### Three candidate categorical structures

By analogy with EM where
[`prop:gram-determinant-plancherel-ratio`](#prop:gram-determinant-plancherel-ratio)
supplies $\delta_{\rm CS} = \hbar_q^4 \cdot [5]_q$, three candidate
sources are most plausible for $\mathcal{N}_{\rm sym}$:

#### Candidate (a) — Gram determinant of the EW Wedderburn block

The Gram determinant of the symmetric-channel Hecke action on the
combined EW/Higgs Wedderburn block at level $n_{\rm EW} = 2 + 2 + 2
= 6$ (one B_2 per host) computes a categorical scalar of the form

$$
  \mathcal{N}_{\rm sym}^{(a)}(q)
  \;=\;
  \frac{\prod_{k=2,3,4} \dim_q(\mathrm{sym}^{T(2,2k)})}{\det \mathcal{G}_{\rm EW}(q)},
$$

where $\mathcal{G}_{\rm EW}(q)$ is the Gram matrix of the EW idempotent decomposition under the bilinear pairing
$\langle\cdot, \cdot\rangle_F$ of
[`def:frobenius-pairing`](#def:frobenius-pairing). This is the
**direct analog** of $\delta_{\rm CS}$'s Gram-determinant origin
in the EM derivation.

#### Candidate (b) — Higgs-eaten Goldstone count

The Higgs mechanism eats $3$ Goldstone bosons (per
[`conj:electroweak-mass-eigenstate-count`](#conj:electroweak-mass-eigenstate-count)).
The associated "phase-space volume" of the eaten Goldstones in the
substrate's q-deformed measure is

$$
  \mathcal{N}_{\rm sym}^{(b)}(q)
  \;=\;
  \prod_{i = 1}^{3} \dim_q(\mathrm{Goldstone}_i)
  \;=\;
  [\text{$T_3 - Y$ rotation}]_q \cdot [W^+]_q \cdot [W^-]_q
  \cdot \mathcal{V}_0(q),
$$

where $\mathcal{V}_0(q)$ is the substrate's vacuum-volume constant.
This route ties $\mathcal{N}_{\rm sym}$ directly to the Higgs
mechanism categorical structure (U2/U4).

#### Candidate (c) — Hochschild-Plancherel ratio

By analogy with the GS spectral-sequence
([`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence))
which contributes Hochschild-cohomology factors to $1/\alpha$,
the EW sector should have its own Hochschild filter:

$$
  \mathcal{N}_{\rm sym}^{(c)}(q)
  \;=\;
  \mathrm{tr}_{\rm Plancherel}\bigl(\mathrm{HH}^*(H_{\rm EW}(q))\bigr).
$$

This is the most **abstract** route but inherits all the GS-spectral-sequence machinery already authored.

### Why this single artifact closes three audit flags

If $\mathcal{N}_{\rm sym}(q)$ is derived (any of (a)/(b)/(c)
succeeding):

1. **NV-1** closes: PSLQ on the extended basis
 $\{q^k, [k]_q, \hbar_q^k, [2k]_q^2/[2]_q, \mathcal{N}_{\rm sym}\}$
 would (by the consistency identity above) by definition confirm the
 closed form.
2. **§3.A v4 wiring** closes: $\mathcal{N}_{\rm sym}$ is also the
 correct calibration constant for translating Markov-trace
 tower terms (depth-1 + depth-2) into MeV mass corrections.
 The naïve calibration $\alpha_{\rm bind} = 8 \cdot m_e \cdot G$
 used in [`v4-mass-pipeline.witness.json`](../../computations/v4-mass-pipeline.witness.json)
 evaluates to zero correction; the correct scale is
 $\alpha_{\rm bind}^{\rm EW} = m_e \cdot \mathcal{N}_{\rm sym}(q_0)
   \approx 108.9$ MeV — a categorical EW-sector binding scale.
3. **SHELL-7-SCALE reweighting** informed: the q-deformed
 Wedderburn-block weight
 $\tilde w_\lambda = \dim_q^2/[n]_q!$ used in
 [`shell7-bb-stratum.witness.json`](../../computations/shell7-bb-stratum.witness.json)
 blew up because it has no $q_0 > 1$ damping. $\mathcal{N}_{\rm sym}(q)$ likely
 provides the correct $q_0$-bounded q-deformed weight (its closed
 form is bounded above by the simple $\dim_q^2$ growth — needs the
 (b) or (c) Higgs/Hochschild structure to suppress). Distinct from
 the classical Plancherel measure $w_\lambda = (\dim V_\lambda)^2/n!$
 ([`prop:plancherel-weight-boundedness`](#prop:plancherel-weight-boundedness)).

### Status

**Status: open.** Numerical value $\mathcal{N}_{\rm sym}(q_0) \approx 213.11$ is fixed by consistency. **Closed form requires categorical derivation, not ansatz-fitting** (per the methodological correction documented separately):

1. Discharging
 [`conj:force-carrier-knot-vs-link-dichotomy`](#conj:force-carrier-knot-vs-link-dichotomy)
 (U2 from PR #511) — the categorical Higgs mechanism
2. Discharging
 [`conj:electroweak-mass-eigenstate-count`](#conj:electroweak-mass-eigenstate-count)
 (U4 from PR #511) — the broken-Wedderburn split
3. Compute the symmetric-channel Frobenius trace
 $\mathrm{tr}_F\bigl(e_{\rm sym}^{\rm EW}\bigr)$ where
 $e_{\rm sym}^{\rm EW} = \otimes_{k=2,3,4} e_{\rm sym}^{(T(2,2k))}$
 from the resulting Higgs-mechanism structure — this *is*
 $\mathcal{N}_{\rm sym}(q)$ by construction.

### Empirical anchors recorded (NOT ansatz-fits)

Two zero-free-parameter q-arithmetic forms have been **probed numerically**
([`n-sym-goldstone-phase-space-probe.witness.json`](../../computations/n-sym-goldstone-phase-space-probe.witness.json)):

| Structural form | Match to $\mathcal{N}_{\rm sym}(q_0)$ |
|-----------------|-----:|
| $[3]_q \cdot [4]_q^3$ | 0.87% off |
| $[3]_q \cdot [4]_q^3 \cdot (1 + \hbar_q^2)$ | 0.107% off |

**Caveat**: these matches are recorded as *empirical anchors* for guiding the
forthcoming categorical derivation — NOT as conjectured closed forms.
Searching for next-order $\delta_2$ correction terms (e.g. $\hbar_q^4 \cdot
[k]_q$ for various $k$) was attempted and explicitly stopped as a fishing
expedition. Promotion of either form to a `proposition` requires the
categorical derivation pipeline above, not further empirical sweeping.

### Falsified candidates

Candidate (a) Gram determinant of the EW Wedderburn block: probed in 9
forms ([`n-sym-gram-determinant-probe.witness.json`](../../computations/n-sym-gram-determinant-probe.witness.json));
best fit (3$\times$3 Cartan with diag $[2k]_q$) is 6.16% off — falsified.

### Required next step (single-target)

Author **`prop:categorical-higgs-idempotent`** — the explicit construction
of $e_H : A \to A$ projecting onto the unbroken $\mathrm{U}(1)_{em}$
direction in $\mathbf{Rep}(\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y)$.
This single artifact unlocks:

- $\mathcal{N}_{\rm sym}$ closed form via the trace formula above
- U2 + U4 from `conj:electroweak-higgs-torus-link-triplet`
- The Higgs slot question raised by PR #513 / #514 (the scalar's
 categorical placement)

Until that derivation exists, `conj:n-sym-symmetric-channel-normalization`
remains *open* — the numerical value is pinned, the closed form is not.

### Witness

[`n-sym-numerical-anchor.witness.json`](../../computations/n-sym-numerical-anchor.witness.json)
— numerical pinning of $\mathcal{N}_{\rm sym}(q_0) = 213.111807\ldots$,
all tested ansatze, and the PSLQ negative result.
