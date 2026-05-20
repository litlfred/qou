This audit catalogues every place in the mass, beta-decay, and
binding-energy computations of the Quantum Observable Universe framework
where the derivation relies on empirical data, fitting, numerology, or
an unproven assumption rather than on a completed categorical derivation.

**Pre-approved calibration inputs** (NOT flagged):

| Input | CODATA 2022 | Role |
|-------|------------|------|
| $m_e = 0.51099895000$ MeV | Leptonic mass scale | |
| $m_\mu/m_e = 206.7682830$ | Fixes $q_0$ | dimensionless |
| $Q_\beta(n) = 0.78233341$ MeV | Hadronic energy scale $\mathfrak{E}_0$ | |

**Gap categories:**
- **GAP-A** Missing categorical derivation (formula used without proof from categorical axioms)
- **GAP-B** Empirical fitting (parameter fitted to data rather than derived)
- **GAP-C** Numerology/pattern match ($q$-integer product matches experimental value but derivation not shown)
- **GAP-D** Open conjecture backing (computation rests on an unproved assumption)

---

## GAP-A-1 — Canonical knot identification for $^2$H, $^3$H, $^3$He

**Source:** `atom-knot-mass-derivation.md`, pipeline step "Confinement SDP".

**Description.**  The canonical Hecke elements $T_w$ for the light
nuclei deuterium ($^2$H = $6_2$), tritium ($^3$H = $8_{11}$), and
helium-3 ($^3$He = $L_{6a4}$) were identified historically by matching
hyperbolic volumes to AME binding energies, not by executing the
categorical confinement SDP from first principles.  The SDP pipeline
([prop:confinement-sdp](#prop:confinement-sdp)) is defined, but the
proof that it *selects* these specific knots as its unique minimizers
(at $\rho = 1$ for $^2$H and $\rho = 2$ for $^3$H/$^3$He) has not been
completed.

**Resolution path.**  A conjecture stating the SDP uniqueness result
has been created:
[conj:canonical-knot-id-sdp](#conj:canonical-knot-id-sdp).

---

## GAP-A-2 — Chirality formula $a_K = 1 + w \cdot h$ (chiral case)

**Source:** `chirality-writhe-ribbon-derivation.md` §Caveat.

**Description.**  The proposition
([prop:chirality-writhe-ribbon-derivation](#prop:chirality-writhe-ribbon-derivation))
derives $a_K = 1 + w(K) \cdot h + O(h^2)$ to first order in $h$
from the Kauffman framing formula applied to the ribbon twist $\varTheta$
on $H_n(R, q)$.  However, the remark at line 150 of the source notes
this is described as "paper-empirical" in upstream commits.  The
derivation is partially complete (first-order term is categorical) but
the exactness beyond first order — and the claim that this particular
first-order expansion is *the* chirality factor for all chiral knots
in the model — is not fully justified.

Additionally, the mean content $\langle c(\lambda) \rangle_\beta$
appearing in the derivation needs explicit evaluation for all
nucleon/nuclear braids; a weighted Plancherel argument is present but
not closed for general $w$.

**Resolution path.**  [conj:chirality-ribbon-frobenius](#conj:chirality-ribbon-frobenius)
states the complete form and flags the proof obligations.

---

## GAP-A-3 — Brane-tower level-selection rule $n_\star(\mathfrak{H})$

**Source:** `brane-tower-z-habiro.md` §Statement.

**Description.**  The brane-tower regularization requires a canonical
level-selection rule $n_\star : \{\text{confined particles}\} \to \mathbb{N}$
that is derivable from QOU substrate data alone.  The conjecture
([conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro)) states its
existence, but no formula for $n_\star$ has been derived.  For low
isotopes the truncation depth was chosen by matching empirical binding
energies (GAP-B overlap); for heavier nuclei no rule is specified.

**Resolution path.**  [conj:brane-level-selection](#conj:brane-level-selection)
isolates the level-selection sub-problem from the broader Habiro
convergence conjecture.

---

## GAP-A-4 — Structural prefactor $\rho(Z, N)$ general rule

**Source:** `atom-knot-mass-derivation.md` §Architecture, note on SDP multiplicity.

**Description.**  The SDP multiplicity $\rho \in \mathbb{Z}_{>0}$ for
a nucleus $(Z, N)$ is found as a by-product of the Wedderburn SDP
witness (e.g. $\rho = 1$ for $D$, $\rho = 2$ for $T$ and $^3$He).
No general derivation of $\rho(Z, N)$ from the categorical data alone
(confinement level $\ell$, strand count $n_0$, quark flavors) has been
given.  Individual values are discovered by running the SDP numerically,
which is an empirical search, not a derivation.

**Resolution path.**  [conj:rho-prefactor-structural](#conj:rho-prefactor-structural)
frames the conjecture.

---

## GAP-A-5 — Binding gap for light isotopes $A \geq 5$

**Source:** `derived-mass-formula-light-isotopes.md` §Note on $^6$Li, $^7$Li.

**Description.**  The derived mass formula for light isotopes
([prop:derived-mass-formula-light-isotopes](#prop:derived-mass-formula-light-isotopes))
is validated for $A \leq 4$ (no fitting, zero free parameters).  The
extension to $^6$Li and $^7$Li is described as a "predictive" extension,
but the knot-atlas entries for $A = 5, 6, 7$ isotopes are not yet
produced by the categorical SDP; they rely on the recursive atom-knot atlas,
which itself is only proved to be complete for $A \leq 60$ under
Plancherel-bound certificates — not from a first-principles completeness
theorem.

**Resolution path.**  The recursive-atlas completeness proof is needed;
this is flagged as an open sub-problem (see `recursive-atom-knot-atlas` block).

---

## GAP-B-1 — Per-nucleon scaling between $A = 2$ and $A = 3$

**Source:** `commutative-crossing-energy.md` §Caveat.

**Description.**  The proposition derives the binding scale from
Hecke-algebra structure, but explicitly notes (line 211): "the
per-nucleon scaling between $A = 2$ and $A = 3$ remains underived."
The numerical coefficient relating deuterium binding to tritium/helium-3
binding is an empirical fit at this stage.

---

## GAP-B-2 — Fitted $\beta_3$ in atomic braid mass

**Source:** `atomic-braid-mass.md` §Definition.

**Description.**  The atomic braid mass formula uses an internal
parameter $\beta_3 \approx 0.050$ for the gluon-contribution weight
of the third-generator crossing in nucleon internal structure.  This
value is fitted to reproduce proton/neutron masses rather than derived
from the Hecke algebra structure.

---

## GAP-B-3 — Compound $\beta$-decay shell calibration ($y_{\mathrm{target}}$ values)

**Source:** `prop:compound-beta-shell-calibration`.

**Description.**  The compound $\beta$-decay shell calibration uses
target $y$ values for the Markov-trace expansion that are calibrated
to reproduce a set of measured $Q$-values, rather than predicted from
the categorical derivation chain.  The framework in principle gives
these from the Markov weights $y_\lambda$
([prop:alpha-k-derivation-procedure](#prop:alpha-k-derivation-procedure)),
but the connection from the abstract $y_\lambda$ to the shell-model
$y_{\mathrm{target}}$ values used in practice has not been derived.

---

## GAP-C-1 — $q$-integer BW coefficients (pattern match)

**Source:** `q-integer-mass-formula.md`.

**Description.**  The extended Bethe--Weizsäcker coefficients are
expressed as products of $q$-integers $[n]_q$ evaluated at $q_0$.
The proposition notes "derivation of the five standard terms" from
Wedderburn and crossing counts, but the specific $q$-integer factors
(e.g.\ $[7]_q$ from "7 crossings on generator 0: 3 B₃ + 1 uu +
2 gluon + 1 ud") rest on counting arguments that have not been
derived from first principles within the Hecke algebra framework.
The crossing counts themselves are empirically motivated (they
reproduce known BW values to $< 2\%$) rather than derived from the
confinement SDP.

---

## GAP-D-1 — Energy scale $\mathfrak{E}_0$ predicted vs. calibrated

**Source:** `beta-decay-energy-scale.md`, `negative-debt-confinement.md`.

**Description.**  The leptonic derivation gives
$\mathfrak{E}_0^{(\mathrm{lept})} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV,
while the hadronic calibration gives $\mathfrak{E}_0^{(\mathrm{had})} \approx 4.155$ MeV.
The $0.75\%$ discrepancy is attributed to the brane tower correction,
but the *specific* tower correction that would close this gap has not
been computed.  In the 9-strand ($H_9(q)$) picture the gap should
close, but this is an open direction (noted in `negative-debt-confinement.md`
§Status: the nine-strand direction).

The current hadronic calibration rests on
[conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro) (GAP-D);
once the brane tower is controlled algebraically the $0.75\%$ gap
becomes a computable correction and $Q_\beta$ remains the single
hadronic input for normalization only.

---

## Gap summary table

| ID | Category | Description | Status | Conjecture created |
|----|----------|-------------|--------|--------------------|
| GAP-A-1 | GAP-A | Canonical knot ID ($^2$H/$^3$H/$^3$He) from SDP | Open | [conj:canonical-knot-id-sdp](#conj:canonical-knot-id-sdp) |
| GAP-A-2 | GAP-A | Chirality formula $a_K = 1 + wh$ exactness | Partial derivation | [conj:chirality-ribbon-frobenius](#conj:chirality-ribbon-frobenius) |
| GAP-A-3 | GAP-A | Brane-tower level-selection $n_\star(\mathfrak{H})$ | Open | [conj:brane-level-selection](#conj:brane-level-selection) |
| GAP-A-4 | GAP-A | Structural prefactor $\rho(Z,N)$ general rule | Open (SDP witness only) | [conj:rho-prefactor-structural](#conj:rho-prefactor-structural) |
| GAP-A-5 | GAP-A | Binding gap for $A \geq 5$ | Open (atlas not complete) | open sub-problem in recursive-atom-knot-atlas block |
| GAP-B-1 | GAP-B | Per-nucleon $A=2\to A=3$ scaling fit | Open | — |
| GAP-B-2 | GAP-B | Fitted $\beta_3 \approx 0.050$ parameter | Open | — |
| GAP-B-3 | GAP-B | Compound $\beta$-decay $y_{\mathrm{target}}$ calibration | Open | — |
| GAP-C-1 | GAP-C | $q$-integer BW coefficient counting | Partially derived | — |
| GAP-D-1 | GAP-D | $\mathfrak{E}_0$ leptonic vs.\ hadronic $0.75\%$ gap | Open (brane tower) | [conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro) |
