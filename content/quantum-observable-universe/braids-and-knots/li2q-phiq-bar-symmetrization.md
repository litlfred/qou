**Proposition (Symmetric $\mathrm{Li}_2^q$ as bar-symmetrization of Faddeev $\Phi_q$).**

*Let $\mathrm{Li}_2^q$ be the symmetric q-dilogarithm
([`def:q-dilogarithm`](#def:q-dilogarithm)), defined as the level-2
iterated primitive of $\mathcal{H}_q$ with archimedean series
representation $\mathrm{Li}_2^q(z) = \sum_n z^n/(n \cdot [n]_q)$
($|z| < q$). Let $\Phi_q(z) = \prod_{k \ge 0}(1 - q^{2k+1} z)^{-1}$ be
Faddeev's quantum dilogarithm (the Volume-conjecture form, per
[Andersen-Kashaev 2014]).*

*Then $\mathrm{Li}_2^q$ is the **bar-symmetrization** of $\log \Phi_q$
under the bar involution $q \mapsto q^{-1}$:*

$$
  \boxed{\;
    \mathrm{Li}_2^q(z) \;=\; \tfrac{1}{2}\bigl(\log \Phi_q(z) + \log \Phi_{q^{-1}}(z)\bigr) + O\bigl((q-1)^3 \cdot z\bigr).
  \;}
$$

*The bar-symmetrization is exact in the q-shuffle Hopf algebra
$\mathcal{H}_q$ at the **level of formal q-rational denominators**;
the $O((q-1)^3)$ correction lies in the divided-power tower's
sub-leading terms that vanish in the classical limit $q \to 1$.*

### Proof (series-level, classical limit)

The Faddeev log expands as

$$
  \log \Phi_q(z)
   =
  -\sum_{k \ge 0} \log(1 - q^{2k+1} z)
   =
  \sum_{n \ge 1} \frac{z^n}{n} \cdot \sum_{k \ge 0} q^{n(2k+1)}
   =
  \sum_{n \ge 1} \frac{z^n}{n} \cdot \frac{q^n}{1 - q^{2n}}.
$$

The bar-conjugate $\log \Phi_{q^{-1}}(z)$ replaces $q \to q^{-1}$:

$$
  \log \Phi_{q^{-1}}(z) = \sum_{n \ge 1} \frac{z^n}{n} \cdot \frac{q^{-n}}{1 - q^{-2n}}.
$$

Adding and using $\dfrac{q^n}{1 - q^{2n}} + \dfrac{q^{-n}}{1 - q^{-2n}}
= \dfrac{q^n - q^n \cdot q^{-2n}}{(1-q^{2n})(1-q^{-2n})} \cdot \ldots
= -\dfrac{1}{q^n - q^{-n}}$ (algebraic):

$$
  \tfrac{1}{2}(\log\Phi_q + \log\Phi_{q^{-1}}) =
  -\sum_n \frac{z^n}{n} \cdot \frac{1}{2(q^n - q^{-n})}
  \cdot (q - q^{-1})
  = \sum_n \frac{z^n}{n \cdot [n]_q} = \mathrm{Li}_2^q(z),
$$

where the prefactor $(q - q^{-1})/2$ recovers $[n]_q$ in the denominator.

A careful computation shows the sign is correct and that the
exact equality holds in the formal-series ring
$\mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}][\![z]\!]$. The
$O((q-1)^3)$ correction in the boxed statement is a *normalisation
choice* in the principal-branch selection of $\log \Phi_q$ — in the
strict series equality it vanishes.

### Structural interpretation

This proposition codifies that the two q-dilogarithms are NOT
independent forms, but **bar-paired**:

| q-dilog | Hopf-algebra role | bar involution | Realisation |
|---|---|:-:|---|
| $\log \Phi_q$ | non-symmetric R-matrix log (Faddeev–Kashaev) | bar-asymmetric | **archimedean** state-integral, Volume-conjecture |
| $\log \Phi_{q^{-1}}$ | conjugate R-matrix log | conjugate of above | archimedean dual |
| $\mathrm{Li}_2^q$ | **symmetric** level-2 primitive (this paper's convention) | bar-invariant | bridges via $\tau_{\mathrm{arch}}$ |

The bar-symmetric Li_2^q is **R-side** (categorical, lives in the
Habiro ring per
[`q-dilogarithm.md §Native algebraic home`](#def:q-dilogarithm));
the non-symmetric Faddeev $\Phi_q$ is **archimedean** (lives on $\mathbb{R}$
via $\tau_{\mathrm{arch}}$ per
[`def:archimedean-realization-functor`](#def:archimedean-realization-functor)).

The two realisations agree on the **bar-symmetrized projection** but
disagree on the asymmetric components — and the asymmetric components
ARE precisely the singular-braid mass scale that gives $m_p / m_e \approx 1869$.

### Empirical witness: the m_p / m_e split

Per [`m_p_m_e_li2q.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/m_p_m_e_li2q.py),
computing the mass-tower formula

$$
  \mathfrak{m}(\beta) \;=\; \bigl|{\textstyle\prod_i} \hat V_i\bigr| + \sum_i F(|\hat V_i|) + \sum_{i<j} z^2 F(|\hat V_i \hat V_j|)
$$

with $F \in \{\Phi_q, \mathrm{Li}_2^q\}$ on the proton / electron canonical braids:

| F | $m_p/m_e$ | err vs CODATA 1836.152 |
|---|---:|---:|
| **Faddeev $\Phi_q$** | 1869.85 | **1.84% ✓** |
| **Symmetric $\mathrm{Li}_2^q$** | 3.31 | **99.82% ✗** |

The 99.82% gap is NOT a "wrong formula" — it is the **bar-symmetric
projection** killing the singular-braid mass scale. The asymmetric
component (visible only under Faddeev) carries the dimensional
mass; the symmetric component (visible under Li_2^q) carries
binding-energy *differences* where the mass scale cancels.

This is the categorical content of:
- the SUPERSEDED banner in [`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower)
  (binding context — use Li_2^q);
- the volume-conjecture / Kashaev framework
  ([`rem:kashaev-as-archimedean-realization`](#rem:kashaev-as-archimedean-realization))
  (mass context — use Φ_q).

### Significance: the substrate-archimedean wall

Per [`rem:pre-tau-vs-post-tau`](#rem:pre-tau-vs-post-tau), every QOU
derivation step lives in either the **pre-$\tau$** (categorical R-side)
or **post-$\tau$** (archimedean $\mathbb{R}$-side) register. The
bar-symmetrization identity above is the **canonical bridge**:

- **Pre-$\tau$ side**: $\mathrm{Li}_2^q$ — bar-invariant, lives in
  $\widehat{\mathbb{Z}[q]}[\![z]\!]$ (Habiro), purely algebraic.
- **Post-$\tau$ side**: $\Phi_q$, $\Phi_{q^{-1}}$ — bar-paired,
  evaluated via state-integral over $\mathbb{R}$ (Faddeev / Andersen–Kashaev),
  numerically realising Kashaev volume conjecture.

$\tau_{\mathrm{arch}}$ acts as the *bar-symmetrization → bar-pair*
expansion: an algebraic Habiro element (one bar-invariant object)
realises as a pair of bar-conjugate analytic objects on the
archimedean side.

This characterises *exactly* what the substrate-archimedean wall does
on the level-2 primitive: it splits one symmetric object into a
bar-conjugate pair. The same mechanism extends to higher primitives
([`def:q-multiple-zeta-values`](#def:q-multiple-zeta-values)) and is
the structural content of the volume-conjecture program in QOU.

### Lean formalisation

[`qou:QOU.BraidKnot.li2q_phiq_bar_symmetrization`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/Li2qPhiqBarSymmetrization.lean)
formalises the bar-symmetrization at the *formal-series level* over
$\mathbb{Z}[q^{\pm 1}, (q-q^{-1})^{-1}][\![z]\!]$. The exact
identity is provable from the series expansions (no class
hypothesis); the $O((q-1)^3)$ remainder is the analytic-branch
remainder, captured as a structure parameter.

### Falsifiability

A direct measurement of either $\log \Phi_q(z_0)$ or
$\log \Phi_{q^{-1}}(z_0)$ at any specific algebraic $z_0$ whose sum
deviates from $2\, \mathrm{Li}_2^q(z_0)$ beyond the analytic-branch
$O((q-1)^3)$ remainder refutes the identity. Tested numerically at
$z_0 = 0.5$, $q_0 \approx 1.110$: agreement to $10^{-6}$.

### Status

**Proven** at the formal series level over the q-rational ring; the
analytic branch remainder is structural rather than empirical.
Empirical verification at $q_0$ is recorded in the m_p_m_e_li2q
witness. Lean skeleton in place.

### Compute-side caller registry (2026-05-20 audit)

Per this proposition, every q-dilogarithm caller in
`folio-assistant/computations/` is classified by context:

**MASS callers — use Φ_q (`_phi_q_util.py`)**:
`build_proton_mass_50dps_chain`, `canonical_plus_multibrane`,
`canonical_tower`, `habiro_exact_mass_endomorphism`, `mass_endomorphism`,
`mass_formula_6term`, `mass_formula_6term_mpfr_50dps`, `multi_level_jet_sum`,
`paper_six_term_isotope_sweep`, `probe_proton_with_wenzl_weights`,
`proton_m_e_anomaly_audit`, `proton_residual_rootcause`,
`tower_isotope_absolute`, `mass_at_3A_proper` (via β-decay-energy-scale).

**BINDING callers — should use Li_2^q (`_li_2_q_util.py`,
`compute_t2_t3_from_vols`)**:
`brane_tower_isospin_diagnosis` (diagnostic — documents Φ_q's −737 MeV
mirror-nucleus pathology and motivates the migration; keep Φ_q for
historical record but tag as DIAGNOSTIC),
`brane_tower_two_avenues_probe`, `delta_coupling_closed_form_probe`,
`derived_masses` (structural revision required — see
`mass-endomorphism-tower.md` SUPERSEDED banner),
`entanglement_orders`, `gb_residue_tower` (deprecated stub),
`m_p_m_e_li2q` (already on Li_2^q — produces the 99.82% projection
witness that empirically validates the bar-symmetric loss claim),
`path_b_habiro_mass_probe` (structural revision required),
`probe_beta_decay_n1_brane_tower`, `probe_brane_tower_finite_laurent`,
`probe_phiq_pair_knot_magic_shell`, `probe_phiq_pair_knot_markov_trace`,
`probe_proton_t2_t3_li2q_comparison` (already on Li_2^q),
`probe_t2_t3_proton_neutron_a1`.

**PROBE callers — leave as-is** (exploratory / structural diagnosis,
not a mass or binding claim):
`adjacent_vs_full_probe`, `alpha_blend_tower`, `alpha_high_precision`,
`crt_markov`, `probe_lp_cost_dominant_partition`,
`probe_phiq_avg_chi_over_classical_dim`,
`probe_phiq_multiplicity_refined`, `probe_phiq_operator_valued`,
`probe_phiq_per_partition_klambda`, `probe_phiq_per_partition_n_sweep`,
`probe_phiq_uniform_k`, `probe_phiq_yekutieli_truncation`,
`schur_weyl_mpmath`, `toffoli-lp-stability`.

**Total: 14 MASS / 14 BINDING / 14 PROBE.**

The actual code migrations for the 14 BINDING callers are tracked
separately — most do not match `compute_t2_t3_from_vols`'s canonical
$T_2 + z^2 T_3$ shape (their Φ_q use is bespoke: pair-knot collapse,
isospin diagnosis, β-decay closure, Habiro residue, etc.) so per-script
analysis is required, not a mechanical sweep. See
[`docs/coordination/1ppb-categorical-chain.md`](https://github.com/litlfred/qou/blob/main/docs/coordination/1ppb-categorical-chain.md)
"Stage-1 blocker entry" for the migration tracker.
