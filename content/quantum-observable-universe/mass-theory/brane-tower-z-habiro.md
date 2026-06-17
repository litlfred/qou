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
   $\Phi_q$ at fixed $z$. The $q$-side termination
   ([atomic Habiro expansion](#cor:habiro-expansion-atomic), proved:
   $m_{\max} \leq \lceil\sqrt{2 \deg p}\rceil$) is the q-analog of
   the parallel claim conjectured for $z$ below.

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

## The open part: $n_\star$

The level-selection rule $n_\star$ is **the open part**. Candidate
structural inputs:

See [Table 1](#tbl:brane-tower-z-habiro-table1-data).

A correct $n_\star$ must (i) be a structural invariant of
$\mathfrak{H}$, (ii) reproduce the empirical $B(\mathfrak{H})$ across
atoms when fed into $\pi_{n_\star}^{(z)}$, and (iii) be derivable from
the QOU substrate without external calibration.

**Empirical observation (uniform-$k$ sweep).** A
uniform-depth probe
([`probe_phiq_uniform_k.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/computations/probe_phiq_uniform_k.py))
sweeping $k \in \{1, 2, 3, 4, 5, 6, 8, 10\}$ uniformly across
$\{D, T, {}^3\mathrm{He}\}$ shows:

1. **The absolute formula** $B = m_e \cdot \rho \cdot (\mathrm{tr}_M(T_w) + \mathrm{tower}^{(k)} + \sigma_{3A})$
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

See [Table 2](#tbl:brane-tower-z-habiro-table2-data).

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
3. Form $B(\mathfrak{H}) = m_e \cdot \rho \cdot (\mathrm{tr}_M(T_w) + \mathrm{tower}(\mathfrak{H}) + \sigma_{3A})|_{q_0}$.
4. Compare with the AME values $\{2.224566, 8.481798, 7.71806\}$ MeV.

A candidate $n_\star$ rule that closes all three to within $\sim 5\%$
**without per-atom retuning** is the empirical signature that
$n_\star$ has been correctly identified. A rule that requires
per-atom retuning is structurally equivalent to Yekutieli's $k_{\max}$
and does not constitute progress.


## Closure attempts: probed $n_\star$ forms

The conjecture's $n_\star$ existence claim asserts a canonical
level-selection rule derivable from substrate data without per-atom
retuning. Six candidate families have been probed against the AME
light-isotope sample $\{D, T, {}^3\mathrm{He}\}$ and **all are
refuted** by the conjecture's own falsifiability criterion (each
exceeds the $\sim 5\%$ confirmation threshold on at least one isotope
without per-atom retuning):

1. scalar uniform-$k$,
2. scalar $\ell\cdot n_0 + k$,
3. per-eigenvalue operator-valued,
4. multiplicity / Type-B-folded-crystal,
5. pair-knot product-volume,
6. pair-knot Markov-trace (full Frobenius Gram + SDP).

The full probe record — sweep tables, error magnitudes, and the
per-form falsification theorems — is consolidated in the
refuted-ansatz audit
([`docs/audits/2026-06-17-refuted-ansatz-lemmas.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-17-refuted-ansatz-lemmas.md)).
The sibling [`brane-tower-z-habiro.lean`](brane-tower-z-habiro.lean)
records the six refutations as witness-driven theorems combined in
`nStar_all_probed_forms_refuted`.

## What survives the closure

The conjecture has two independent claims:

1. **Algebraic Cauchy-limit claim** —
   $\widetilde{\Phi}_q^{\mathrm{tower}}(\beta)$ exists as a Cauchy
   limit in the $z$-Habiro topology
   ([$z$-Habiro ring](#def:z-habiro-ring)). **Untouched by any of the
   $n_\star$ probes and remains open**; a direct algebraic proof
   proceeds via the cyclotomic projections $\pi_n^{(z)}$ and does not
   depend on $n_\star$. The analytic prerequisite — that the infinite
   product $\Phi_q(z) = \prod_{k\geq 1}(1-q^{-k}z)^{-1}$ is a
   well-defined positive real on $|z| < q$ — is formalized in
   `QOU.MassEndomorphism.PhiQConvergence`.

2. **$n_\star$ existence claim** — refuted across every probed form
   (above). The block kind remains `conjecture` because the algebraic
   Cauchy-limit half is still open.

## Structural finding: pair-knot operators are selected at closed shells

Independent of the refuted $n_\star$ forms, the operator-selection LP
dual yields a positive structural result. For magic-shell nuclei the
closed shell contributes as a single composite knot operator (the
Hopf-linked sub-knot of the magic nucleon pair) rather than a sum of
separate per-generator $\Phi_q(|\hat V_i|)$ terms. The per-generator
magnitudes make the duplicated intra-block structure visible:

See [Table 7](#tbl:brane-tower-z-habiro-table7-data).

Solving the operator-selection LP over the basis
$\{\sigma_i,\ \sigma_{pp},\ \sigma_{nn}\}$ with cost $t_i = |\hat V_i|$
and the Frobenius Gram (per
[`prop:operator-selection-lp`](#prop:operator-selection-lp)), with
strong duality verified (gap $= 0$), the dual active set distinguishes
the pair-knot composites $\sigma_{pp}, \sigma_{nn}$ from per-generator
operators **at exactly the magic configurations** — and they are
absent from $D$'s active set, which has no magic shell:

See [Table 8](#tbl:brane-tower-z-habiro-table8-data).

This is the operator-level signature of $Z=2$ / $N=2$ shell closure in
the substrate algebra, recorded in the sibling `.lean` as
`lpDualActiveSetIncludesPairKnotAtMagicShells` for downstream use.

## Structural finding: $Z \leftrightarrow N$ isospin symmetry

At the canonical Markov-trace operator-volume level the two
magic-shell sub-braids are isomorphic Hecke elements:

$$
  \mathrm{tr}_M(\sigma_{pp}) \;=\; \mathrm{tr}_M(\sigma_{nn})
  \;=\; 0.0622 \quad(\text{exactly}),
$$

so $Z \leftrightarrow N$ isospin symmetry holds exactly. (An apparent
$1.326\times$ asymmetry under the cruder product-volume convention was
a product-volume artifact, not a real symmetry breaking.)

## Structural conclusion

No probed $n_\star$ choice and no operator-volume convention (product,
geometric-mean, or canonical Markov trace) recovers the AME
light-isotope binding uniformly; the ${}^3\mathrm{He}$ gap is a
structural deficit of the brane-tower formula at the $A=3$ / $n_0=9$
regime, not an operator-volume choice. The surviving open paths are
the algebraic Cauchy-limit half (above) and the ${}^3\mathrm{He}$
structural-gap branch.
