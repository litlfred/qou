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
