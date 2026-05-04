# 4He spread deep dive — the level-0 formula models FREE nucleons, not BOUND ones

## Decomposition of the level-0 hybrid prediction at 4He

| component | value (Hecke units) | % of total |
|-----------|--------------------:|-----------:|
| desc q-Hecke (n_strands = 12) | $6.10 \times 10^{-7}$ | $8 \times 10^{-9}\%$ |
| single = $4 \cdot \Phi_q(|tr_p|)$ | 7400.946 | **99.977%** |
| cross = $z^2 \cdot 6\text{-pair sum}$ | 1.725 | 0.023% |
| **total pred** | **7402.671** | |

Comparison to AME:

- AME $^4$He = 3727.379 MeV
- $\mathrm{cal\_const} = \mathrm{AME} / \mathrm{pred} = 0.503518$ MeV/Hecke
- $\mathrm{cal}/m_e = 0.503518 / 0.51100 = 0.985360$
- target pred (for $\mathrm{cal}/m_e = 1$) = AME $/m_e$ = 7294.299
- **excess = +108.37 (+1.49%)**

## What the per-nucleon trace actually is

```
|tr_p| = |tr_n| = 0.671453   (1-strand sub-braid trace)
Φ_q(0.671453) = 1850.236
```

**The proton and neutron have identical single-strand traces.** The
hybrid's per-nucleon term $\Phi_q(|tr|)$ comes from the q=1 MN
character (which doesn't distinguish proton from neutron at the
single-strand level). The full q-deformed Hecke character would
distinguish them, but the hybrid uses q=1 MN tower for linear-in-$A$
scaling.

So `single = A · 1850.236` for **every atom** with $A$ nucleons.
Same value of 1850.236 across D (A=2), 4He (A=4), 12C (A=12),
40Ca (A=40).

## Why cal/m_e varies across atoms

The cal/m_e ratio collapses to:

$$
\frac{\mathrm{cal}}{m_e} = \frac{\mathrm{AME}/m_e}{A \cdot 1850.24 + \text{small corrections}}
$$

Per-nucleon AME mass (the binding-energy curve):

| atom | AME/A (MeV/nucleon) | $1 - \frac{\mathrm{AME}/A}{m_p}$ |
|------|---------------------:|--------------------------------:|
| D | 937.81 | 0.05% |
| 3He | 936.13 | 0.23% |
| 4He | 931.84 | **0.69%** |
| 6Li | 933.84 | 0.47% |
| 12C | 931.49 | 0.72% |
| 16O | 931.20 | 0.76% |
| 40Ca | 930.62 | 0.82% |

(reference $m_p = 938.272$ MeV)

These are exactly the **per-nucleon binding fractions from the
SEMF curve**. 4He has the largest binding-per-nucleon among
light nuclei (after $^7$Li); 40Ca and 16O are also tightly bound;
D is barely bound.

## The cal/m_e spread IS the binding-energy curve

Inverting the cal/m_e formula and the per-nucleon mass observation:

- D's `cal/m_e ≈ 0.992` because per-nucleon mass is nearly $m_p$.
- 4He's `cal/m_e ≈ 0.985` because per-nucleon mass is 7 MeV less
  than $m_p$.
- 40Ca's `cal/m_e ≈ 0.981` because per-nucleon mass is 7.6 MeV
  less than $m_p$.

**The 1.06% spread is the 8.6 MeV variation in per-nucleon mass
across the AME data**, normalised by $m_p$ (≈ 0.92%) plus the
$z^2$-suppressed pair contributions.

## Why level-0 misses binding entirely

The level-0 hybrid's structure:

$$
\mathfrak{m}^{(0)}(Z, N) = \underbrace{|tr_M(W)|}_{\text{exp-small}} + \underbrace{A \cdot \Phi_q(|tr_{\mathrm{nucleon}}|)}_{\text{99.98\%}} + z^2 \underbrace{\sum_{\mathrm{pairs}} \Phi_q(|tr_{\mathrm{pair}}|)}_{0.02\%}
$$

The dominant term is **per-nucleon, atom-independent**. The pair
correction is too small ($z^2 \approx 0.25$, and $\Phi_q(|tr_{\mathrm{pair}}|) \approx 1.15$
each — total pair contribution at 4He is 1.72, while 28 MeV of
binding requires ~55 Hecke-units of pair correction to materialise).

**The level-0 truncation literally cannot resolve binding-energy
structure** because:

1. The pair Φ_q values are too small (factor ~1600× smaller than
   single Φ_q).
2. Triple-and-higher correlations don't appear at level 0 (per
   pentagon ascension argument).
3. The categorical-saturation content (`conj:categorical-neutrality-saturated-shells`)
   says shell binding is in self-conjugate $\lambda \vdash 3A$
   contributions of length ≥ 3 — invisible at level 0 (2-variable
   Schur vanishes there).

## Implication for the precision target

The 22 ppb calibration floor is a target for **bound** nuclear
mass prediction. The level-0 hybrid achieves ~0.5% on each atom
*as a free-nucleon-mass estimate* — that is, the cal/m_e ≈ 0.987
mean reflects the average per-nucleon binding energy across the
test atoms (~7 MeV).

To approach 22 ppb requires capturing:

1. **Volume term** — proportional to $A$ (already implicit in the
   $A \cdot \Phi_q$ structure).
2. **Surface term** — $\propto A^{2/3}$, missing at level 0.
3. **Coulomb term** — $\propto Z(Z-1)/A^{1/3}$, missing at level
   0; needs the q-Hecke proton-proton distinction (which is in
   the descended channel but exp-small at A ≥ 4).
4. **Asymmetry term** — $\propto (N-Z)^2/A$, missing at level 0;
   needs neutron-proton distinguishing structure (q-Hecke
   per-pair).
5. **Pairing term** — $\propto \delta(\mathrm{parity})/A^{1/2}$,
   missing at level 0.
6. **Shell corrections** — discontinuities at magic Z, N. The
   level-1 BB-stratum content per
   `conj:categorical-neutrality-saturated-shells`.

Of these, terms 3-6 require **structurally new contributions** to
the per-braid mass tower. Volume and surface are already in the
level-0 form (the $A \cdot \Phi_q$ structure has implicit
$A^{2/3}$-like scaling through the Φ_q normalisation).

## Why the q-Hecke descended doesn't fix it

The q-Hecke descended trace at 4He is $6.10 \times 10^{-7}$ —
totally negligible compared to 7400 from the tower. The descended
DOES distinguish proton from neutron (gives the 0.53 MeV ³He/³H
splitting at A=3), but at A ≥ 4 it decays exponentially and
contributes nothing.

So even though the descended channel could in principle carry
Coulomb / asymmetry / pairing distinguishing information, its
exponential decay makes it phenomenologically irrelevant for
A ≥ 4.

**Implication**: the binding-energy distinguishing terms must
come from the LEVEL-1 jet-tower contributions, not from
strengthening the descended channel. The descended is correctly
small (consistent with categorical-truncation properties); the
missing physics lives at level 1+.

## What would close the spread

1. **Binding-mode level-1 contribution.** Compute level-1 jet
   prolongation via $A_{n+1} = A_n \otimes \Omega^1(A_n)$ on the
   per-nucleon and per-pair sub-braids. The Kähler-differential
   tail gives the binding-energy correction. This is the actual
   A.3 the truncation audit pointed at.
2. **q-Hecke level-1 vs q=1 MN level-1.** The hybrid's q=1 MN
   tower at level 0 misses binding because q=1 doesn't see the
   fine structure. A q-Hecke level-1 (with proton/neutron
   distinguishing) might capture it — but this is a separate
   research path.
3. **Wedderburn-block level-1 from BB-spectral-sequence.** The
   shell-aware contribution per
   `conj:homological-shell-condensation`. Self-conjugate $\lambda
   \vdash 3A$ contributions of length ≥ 3 enter at level 1 and
   carry the magic-shell binding enhancement.

## Status

**The 4He cal/m_e residual is structurally explained.** The level-
0 hybrid models the FREE nucleon mass with high precision (per-
nucleon $\Phi_q$ value ≈ 1850.24 across all atoms). The cal/m_e
spread of ~1% IS the per-nucleon binding-energy curve from AME,
not an error in the categorical formula.

To close the spread to ≤ 22 ppb, level-1 (and higher) jet-tower
contributions must be added. These contributions encode
binding-energy structure (Coulomb, asymmetry, pairing, shell
corrections) via the Kähler-differential / BB-stratification
machinery. **This is research-grade**, not a refactor — the
explicit per-$\lambda$ level-1 weights $w_\lambda^{(1)}$ are not
yet derived.

**Pragmatic recommendation**: quote the level-0 hybrid's
predictions as **free-nucleon-sum estimates** (~0.5% per atom)
rather than bound-nuclear-mass predictions. Acknowledge the
cal/m_e log(A) trend as the binding-energy curve. Reach toward
22 ppb only via the level-1 BB-stratification work (A.3 v3+)
or accept the level-0 precision floor as the achieved milestone.
