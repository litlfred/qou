**Proposition (chirality / non-chirality split of the mass tower).**

*Per the
[unified curvature-rank mass formula](#prop:unified-curvature-rank-mass-formula),
the categorical mass of a knot $\mathcal{K}$ probed by test element
$\mathcal{T} \in A = H_n(R, q)$ decomposes as a sum over GB-filtration
strata.  This proposition refines that decomposition by splitting each
stratum into a **chirality** part (Wedderburn blocks at signed-content
zero) and a **non-chirality** part:*

$$
  \boxed{\;
    \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
    \;=\;
    \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
    \;+\;
    \mathfrak{m}^{\neg\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;}
$$

*where*

$$
  \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;=\;
  \sum_{k = 0}^{n-1} \alpha_k \cdot
    \!\!\sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k \\ c_\lambda \,=\, 0}}\!\!
    w_\lambda \cdot
    \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|,
$$

*$c_\lambda := \sum_{(i, j) \in \lambda}(j - i)$ is the signed Young
content, and the chirality cells are exactly those Wedderburn blocks
satisfying $D_q^2(\lambda) = 0$ in the q-Dirac cell scanner — the
gauge-invariant background per
[confinement-categorical](#prop:confinement-categorical),
[rem:confinement-curvature-rank](#rem:confinement-curvature-rank).*

*The non-chirality contribution is defined as the remaining sum.*

**Why $c_\lambda = 0$ is the correct chirality marker.**

*By the q-Dirac operator construction
([cite q-Dirac scanner witness](#)), the q-deformed second-order
Dirac operator $D_q$ acts on the centre $Z(H_n(R, q)) =
\bigoplus_\lambda R \cdot e_\lambda$ with eigenvalues*

$$
  D_q^2(\lambda) \;=\; (q^{c_\lambda} - q^{-c_\lambda})^2 / (q - q^{-1})^2.
$$

*Its kernel $D_q^2(\lambda) = 0$ is exactly the locus $c_\lambda = 0$.
By [confinement-categorical](#prop:confinement-categorical), this
kernel is the gauge-invariant background that survives the
GB-filtration spectral-sequence collapse — the categorical analogue
of the gluon-condensate vacuum.*

**Numerical witness (atomic isotopes).**

*The q-deformed Wedderburn-weighted character contribution from
chirality cells is computed in
[`computations/atomic_chirality_residue.py`](#).
For $\mathcal{T} = 1$ (total mass), the chirality contribution to the
binding energy via $\alpha = m_e \cdot 8G$ is:*

| Isotope | $\alpha\,\mathfrak{m}^{\mathrm{chir}}$ (MeV) | $B_\mathrm{nucl}$ (MeV) | Ratio |
|---|---|---|---|
| ${}^{2}\mathrm{H}$ | $\approx$ 0.000 | 2.225 | < 0.01% |
| ${}^{3}\mathrm{H}$ (T) | +0.072 | 8.482 | 0.85% |
| ${}^{3}\mathrm{He}$ | +0.067 | 8.597 | 0.78% |
| ${}^{4}\mathrm{He}$ | +0.872 | 29.327 | **2.97%** |

*Chirality cells are 4–7% of the total partition count but contribute
disproportionately at deep strata: for $^4$He at depth $k = 4$ the
chirality channel dominates with ratio $-26.6$ relative to the total
$\Phi_4$.*

**Physical interpretation.**

*The chirality contribution is **positive** for all isotopes (an
attractive / confining force) while the total mass tower is mostly
negative (net repulsive at the categorical level, balanced by the
positive m_e baseline).  This is consistent with the chirality
channel being the gauge-invariant background that mediates
confinement — see
[rem:confinement-curvature-rank](#rem:confinement-curvature-rank).*

**Relation to the mass-tower coefficient stratification.**

*By
[mass-tower-coefficient-stratification](#prop:mass-tower-coefficient-stratification),
the prefactor $\alpha_3$ in the unified formula is forced to be the
**self-conjugate restricted weight** on $\Lambda_3$.  The chirality
sub-stratum at depth $3$ is exactly the self-conjugate locus
$c_\lambda = 0$, identifying $\mathfrak{m}^{\mathrm{chir},(3)}$
with the **Wigner $np$-pairing** Bethe--Weizsäcker term
([Wigner $np$ pairing](#prop:wigner-np-pairing)).
This proposition therefore makes the
$\lambda_{\mathrm{Wigner}}$ contribution constructible from the
q-deformed Wedderburn-weighted character data of an atomic braid,
with no fitting input.*

**Plancherel-boundedness of the chirality sub-sum.**

*By [plancherel-weight-boundedness](#prop:plancherel-weight-boundedness),
$\sum_{\lambda \in \Lambda_k} w_\lambda \leq 1$, so the chirality
sub-sum
$\sum_{\substack{\lambda \in \Lambda_k \\ c_\lambda = 0}} w_\lambda$
is also bounded by $1$.  The chirality residue
$\mathfrak{m}^{\mathrm{chir}, (k)}$ inherits this boundedness, and
the cumulative chirality contribution
$\mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}$ is convergent.*

*Remark.* This proposition is a structural refinement of the unified mass formula. No new analytic content is added; the split exists by inspection.  The numerical witness shows that the chirality channel
is small in absolute terms (~3% of $B_\mathrm{nucl}$ at $^4$He) but
is the dominant contribution at deep curvature-rank strata.  This
provides direct empirical access to the $D_q^2 = 0$ kernel from
nuclear binding data, and supplies the constructive form for the
$\lambda_{\mathrm{Wigner}}$ Bethe--Weizsäcker coefficient via
[mass-tower-coefficient-stratification](#prop:mass-tower-coefficient-stratification).*
