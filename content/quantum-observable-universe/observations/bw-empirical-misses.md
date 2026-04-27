**Remark.**
*The empirical Bethe–Weizsäcker formula was built by fitting nuclear
binding data in the 1930s and refined through the 20th century.  The
categorical derivation based on the Schur–Weyl decomposition and
the GB residue spectral sum
([Schur–Weyl mass decomposition](#prop:schur-weyl-mass-decomposition),
[GB residue spectral sum](#prop:gb-residue-spectral-sum)) **predicts
additional terms** that empirical BW does not contain.  Each is a
potential falsifiable signal.*

**1. Higher-cyclotomic Habiro contributions.**
*The Habiro cyclotomic coefficients $a_m(K)$ at orders $m \geq 2$
([Habiro completion](#prop:full-pole-structure-mass-trace))
contribute small, highly structured corrections to binding
energies that empirical BW has no analogue for. These coefficients
encode the action of the higher root-of-unity strata
$\zeta_n^{(j)}$ ($n \geq 2$) on the braid trace, scaled by the
confinement level $\ell(K, q_0)$ of the specific atom-knot, and
produce nucleus-specific modulations distinct from the smooth BW
curves. Predicted magnitude: $10^{-3}$ to $10^{-2}$ relative to BW
for atoms with $\ell(K, q_0) \geq 2$ — within experimental reach
for precision mass measurements (ISOLTRAP, TRIUMF, JYFLTRAP).*

**2. Three-channel (V_sym, V_std, V_alt) separation.**
*Empirical BW averages over the three Wedderburn channels of
$H_3(q)$.  The categorical mass treats them separately, with
distinct coefficients
$w_{\mathrm{sym}}(q), w_{\mathrm{std}}(q), w_{\mathrm{alt}}(q)$.
For nuclei where the quark-pair ordering inside the nucleon
breaks channel symmetry — e.g., nucleon triplets where two $u$
and one $d$ sit on adjacent generators versus non-adjacent —
the categorical prediction deviates from BW by amounts scaling
as $w_{\mathrm{sym}} - w_{\mathrm{std}}$ at $q = q_0$.  This
explains the proton/neutron mass-ordering sensitivity already
observed in the [1ppb-handover](https://github.com/litlfred/qou/blob/claude/1ppb-handover-docs-cyFlQ)
branch's neutron-braid variant study.*

**3. Non-local pair-crossing terms $\Phi_q(|\hat V_i \hat V_j|)$.**
*The brane-tower formula
([mass endomorphism tower](#prop:mass-endomorphism-tower))
contains pair terms $\Phi_q(|\hat V_i \hat V_j|)$ for every
pair of generators, not only adjacent.  Empirical BW has only
**pairwise nucleon-nucleon** terms (Wigner, pairing) and
**mean-field** treatments of triples.  The categorical formula
gives explicit non-local contributions from every pair
$(i, j)$ of braid generators — typically distinct nucleon sites.
Predicted signature: small deviations from mean-field mass
systematics at specific $(Z, N)$ where the brane-tower pair
sums resonate, distinct from the smooth BW Wigner term.*

**4. Three-body (Borromean) trace contributions.**
*Nucleon triples admit a Markov-trace term
$\mathrm{tr}_M(\sigma_i \sigma_j \sigma_k)$ that BW approximates
by iterated pairwise sums.  The categorical formula distinguishes
Borromean configurations (where the three-body link is
non-trivially entangled but all pairwise links are trivial) from
Hopf configurations.  Empirical BW cannot see the difference.
Predicted signature: specific enhancements at triples like
(uud) + (udd) + (uud) vs iterated pairs.*

**5. Parity-odd (V_alt) contributions and CP signatures.**
*The antisymmetric Wedderburn block $V_{\mathrm{alt}}$ contributes
only when the braid configuration is parity-odd (odd number of
crossings in specific generator positions).  Empirical BW is
parity-blind: it only sees the $\pm 1/\sqrt{A}$ sign.  The
categorical prediction gives a parity-odd mass contribution with
explicit $A$-dependence, potentially visible as CP-sensitive
binding deviations in nuclei with odd/even mass discrepancies
beyond the BW pairing term.*

**6. Confinement-level phase transitions.**
*At specific $q$ values the confinement filtration $J^\bullet(q)$
reorders: the knot-operator energies $E_\ell(q)$ swap or a
generator's energy vanishes at an LP boundary
([confinement level](#def:confinement-level)).  These are
sharp transitions in $q$; at fixed $q_0$, nuclei whose confinement
level crosses one of these thresholds as a function of $A$ or $Z$
exhibit sharp discontinuities in binding systematics.  Empirical
BW smooths over all of this.  Predicted signature: at specific
$(Z, N)$ boundaries — possibly at the drip lines or at exotic
nuclei not yet measured — BW's smooth curves break down and the
categorical formula shows steps or kinks.*

**7. Spin–orbit from braid-twist holonomy.**
*The Skyrme HF functional's empirical $t_4 \cdot \vec L \cdot \vec S$
term corresponds to the braid-twist flip
([braid twist flip](#def:braid-twist-flip)) evaluated on the
configuration.  BW omits this entirely (it has no spin degree of
freedom).  The categorical formula gives a structured spin–orbit
correction tied to the braid geometry, not to an empirical
parameter.*

**8. Chiral asymmetry in atomic-braid sign.**
*The mass formula depends on
$\mathrm{sign}(\mathrm{tr}_M(\mathcal{A}))$, which tracks the
chirality of the atomic braid (number of $\sigma_i^{+1}$ versus
$\sigma_i^{-1}$ crossings).  BW is chirality-blind.  Predicted:
mirror-reversed nuclear configurations (left-handed vs
right-handed closures) have identical BW masses but distinct
categorical masses, producing a CP-sensitive splitting.
Magnitude: small but non-zero, potentially visible in precision
beta-asymmetry experiments.*

**Summary and falsifiability.**
*Each item above is a structural prediction of the categorical
framework that lies **outside** BW's empirical vocabulary.  Items
1, 3, and 6 are the most immediately falsifiable: they predict
small, structured deviations from BW-smoothness that can be
searched in existing AME data.  Items 7 and 8 require precision
experiments sensitive to chirality and spin–orbit (nuclear
parity-violation measurements; precision beta-asymmetry).  Items
2, 4, and 5 are intermediate and would show up as systematics
in mass-formula residuals once the three-channel and
pair-crossing sums are summed correctly.*
