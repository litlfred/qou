The [mass-endomorphism conjecture](#conj:mass-endomorphism) states that
the Hecke mass element $\Phi_{\mathrm{mass}}$ admits a closed-form NF
decomposition. Its **transient (brane-tower) component** is the sum

$$
  \Phi_{\mathrm{mass}}^{\mathrm{trans}}(\beta)
  \;=\;
  \sum_{i=1}^{N} \Phi_q(z_i),
$$

where $z_i = |\hat{V}_i|$ are the per-generator algebraic-volume
magnitudes from
[algebraic quantum volume](#def:algebraic-quantum-volume) and
$\Phi_q$ is the [quantum dilogarithm](#cor:quantum-dilogarithm).

For low isotopes $\{D, T, {}^3\mathrm{He}\}$, the per-generator
volumes satisfy $z_i \in [0.85, 1.0]$ — just below the first pole of
$\Phi_q$ at $z = q_0 \approx 1.11$. Numerically
$\Phi_q(0.989) \approx 6.7 \times 10^5$ and $\Phi_q(1) \approx 9 \times 10^5$,
so each summand is enormous and the analytic brane tower dominates the
mass formula by orders of magnitude beyond the empirical AME binding.

Two regularizations have been documented but neither uniformly closes
the gap (see [mass-endomorphism conjecture §"Two distinct convergence problems"](#conj:mass-endomorphism)):

1. **Yekutieli truncation** at GB filtration depth $k_{\max}$ — works
   for $D$ ($k_{\max}=2$, error $\sim 22\%$), grossly fails for $T$
   ($k_{\max}=9$, error $\sim 17000\%$). Empirical, not structural.
2. **$q$-Habiro completion** (the
   [Habiro ring](#def:habiro-ring) at $((q;q)_n)$) — regularizes in
   the variable $q$, not $z$. Does not change the analytic value of
   $\Phi_q$ at fixed $z$.

## Statement

**Conjecture (brane tower in $z$-Habiro).**

*Let $\mathfrak{H}$ be a confined particle/atom with per-generator
volumes $\{\hat{V}_i(q)\}_{i=1}^{N}$ in
$\mathbb{Z}[q^{\pm 1/2}]$. The brane-tower partial sums*

$$
  \widetilde{\Phi}^{(N)}(\beta)
  \;:=\;
  \sum_{i=1}^{N}
    \mathrm{Trunc}_{<n}\!\bigl[\Phi_q(\hat{V}_i)\bigr]
  \;\in\;
  \mathbb{Z}[q^{\pm 1}][z] / (P_n(q, z))
$$

*(where $\mathrm{Trunc}_{<n}$ takes the unique representative of
degree $< n$ in $z$ in the cyclotomic-in-$z$ quotient)
form a Cauchy sequence in the* $z$*-Habiro topology
([$z$-Habiro ring](#def:z-habiro-ring)) **as $N$ varies**. Their limit*

$$
  \widetilde{\Phi}_q^{\mathrm{tower}}(\beta)
  \;\in\;
  \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z
$$

*exists as an algebraic element — well-defined purely algebraically,
with no analytic regularization required.*

*Furthermore, there exists a **canonical level-selection rule***

$$
  n_\star \;:\; \{\text{confined particles}\} \;\longrightarrow\;
  \mathbb{N}_{\geq 1},
  \qquad
  \mathfrak{H} \;\longmapsto\; n_\star(\mathfrak{H}),
$$

*derivable from QOU substrate data alone (e.g. confinement level
$\ell$, strand count $n_0$, GB filtration on $H_{n_0}(q)$,
or analogous structural invariants), such that the cyclotomic
projection*

$$
  \pi_{n_\star(\mathfrak{H})}^{(z)}\!\bigl(\widetilde{\Phi}_q^{\mathrm{tower}}(\beta_\mathfrak{H})\bigr)
$$

*evaluated at $q = q_0$ and $z = z_i$ recovers the empirical brane-tower
contribution to the binding $B(\mathfrak{H})$ uniformly across atoms,
not just for the single atom whose GB filtration depth happens to
match.*

## What this conjecture would buy

If true, the conjecture:

1. **Replaces the analytic infinite product** $\Phi_q(z)$ — which has
   no algebraic home and blows up at $|z| \to q$ — with an algebraic
   element of $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$.
2. **Promotes Yekutieli truncation** from an ad-hoc cutoff at GB depth
   to a **structural cyclotomic projection** at a canonical level.
3. **Predicts the level-selection rule** $n_\star$ structurally — the
   single open computation reduces from "find the right Φ_q
   regularization" to "identify $n_\star$ from substrate data".

## Status of $n_\star$

The level-selection rule $n_\star$ is **the open part**. Candidate
structural inputs:

| Candidate | Source | Match for $D$ ($k_{\max}=2$) | Match for $T$ ($k_{\max}=9$) |
|:---|:---|:---:|:---:|
| GB max grade | $H_{n_0}$ filtration | works (input by construction) | overshoots |
| confinement level $\ell$ | [confinement level](#def:confinement-level) | TBD | TBD |
| $\dim H_{n_0}(q)$ | strand count $n_0 = 3A$ | TBD | TBD |
| Coxeter length $\ell(w)$ | NF word length | TBD | TBD |

A correct $n_\star$ must (i) be a structural invariant of
$\mathfrak{H}$, (ii) reproduce the empirical $B(\mathfrak{H})$ across
atoms when fed into $\pi_{n_\star}^{(z)}$, and (iii) be derivable from
the QOU substrate without external calibration.

**Empirical observation (uniform-$k$ sweep, 2026-04-29).** A
uniform-depth probe
([`probe_phiq_uniform_k.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/folio-assistant/computations/probe_phiq_uniform_k.py))
sweeping $k \in \{1, 2, 3, 4, 5, 6, 8, 10\}$ uniformly across
$\{D, T, {}^3\mathrm{He}\}$ shows:

1. **The absolute formula** $B = m_e \cdot \rho \cdot (|\mathrm{tr}_M(T_w)| + \mathrm{tower}^{(k)} + \sigma_{3A})$
   overshoots at every uniform $k$ — errors grow monotonically with
   $k$ ($+775\%$ at $k=1$, $+1.27 \times 10^6\,\%$ at $k=10$). No
   uniform absolute-form $k$ closes the gap.

2. **The subtractive form** $B = E_0 \cdot (\mathrm{tower}_{\mathrm{free}}^{(k)} - \mathrm{tower}_{\mathrm{atom}}^{(k)})$
   has a **sign-flip at $k = 2$**: for all three atoms,
   $\Delta\mathrm{tower}^{(k=1)} < 0$ but $\Delta\mathrm{tower}^{(k \geq 2)} > 0$.
   At $k = 2$:
   $B(D) \approx +1.74\,\mathrm{MeV}$ (err $-22\%$),
   $B(T) \approx +5.18\,\mathrm{MeV}$ (err $-39\%$),
   $B({}^3\mathrm{He}) \approx +18.05\,\mathrm{MeV}$ (err $+134\%$).

3. **${}^3\mathrm{He}$ overshoots at every $k \geq 2$ in subtractive
   form**, suggesting the per-generator volume list for ${}^3\mathrm{He}$
   carries a doubled $|\hat{V}| \approx 0.989$ contribution that the
   subtractive cancellation does not absorb. This is consistent with
   ${}^3\mathrm{He}$'s 8-generator list having two near-pole entries
   (positions 0 and 3), versus $D$'s single near-pole entry.

The sign-flip at $k = 2$ is structurally interesting: it is the
smallest depth that includes the **Hecke quadratic relation slice**
($\sigma_i^2 = (q - q^{-1})\sigma_i + 1$, two factors of $\Phi_q$).
This may indicate that the correct $n_\star$ rule depends not only on
filtration depth but also on how the per-generator volume list
**multiplicities** interact with the cyclotomic projection — a refined
form of the conjecture would need to fold per-generator-volume
multiplicity into $n_\star$.

## Relation to the $q$-Habiro picture

The two completions are **independent**:

| Direction | Cyclotomic ideal | What it unifies |
|:---|:---|:---|
| in $q$ ([Habiro ring](#def:habiro-ring)) | $((q;q)_n)$ | colored Jones $J_N$ for all $N$ |
| in $z$ ([$z$-Habiro ring](#def:z-habiro-ring)) | $(P_n(q, z))$ | brane-tower partial sums for all $N$ |

The full picture would be a **bicompletion**
$\widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}$ at the bigraded ideal
generated by both $(q;q)_n$ and $P_n(q,z)$, in which the colored Jones
data and the brane-tower data coexist as a single algebraic object.
Construction of the bicompletion is open.

## Falsifiability

The conjecture is **falsifiable** by computation:

1. Pick a candidate $n_\star$ rule (one of the rows above, or a
   combination).
2. Compute $\pi_{n_\star(\mathfrak{H})}^{(z)}(\widetilde{\Phi}^{(N)})$
   at $q_0$ for each isotope in the AME light-isotope sample
   $\{D, T, {}^3\mathrm{He}\}$.
3. Form $B(\mathfrak{H}) = m_e \cdot \rho \cdot (|\mathrm{tr}_M(T_w)| + \mathrm{tower}(\mathfrak{H}) + \sigma_{3A})|_{q_0}$.
4. Compare with the AME values $\{2.224566, 8.481798, 7.71806\}$ MeV.

A candidate $n_\star$ rule that closes all three to within $\sim 5\%$
**without per-atom retuning** is the empirical signature that
$n_\star$ has been correctly identified. A rule that requires
per-atom retuning is structurally equivalent to Yekutieli's $k_{\max}$
and does not constitute progress.
