The three-calibration discipline ([`def:three-calibration-discipline`](#def:three-calibration-discipline)) uses $m_e$, $m_\mu/m_e$, and $m_\pi$ as CODATA/PDG inputs. It maps them bijectively to three cohomological data of the Bring Hodge structure $H^1 = 2W$: the $W$-plane scale, the $W$-plane modulus, and the orthogonal $\mathrm{Vol}(\mathrm{Hopf})=0$ meson class. We clarify the epistemic status of each input.

The parameter $\mathfrak{Q}_\beta = P_{\mathrm{skew}}^{\beta}$ proxies CAL-2 (the neutron $\beta$-sector bar-skew channel $P_{\mathrm{skew}}^{\beta}$). It is not a fourth calibration. The CAL-2 modulus is most precisely pinned by $m_\mu/m_e$. Reproducing $\mathfrak{Q}_\beta$ from $q_0$ provides a $0.17\%$ cross-check. CAL-3 is the pion-sector bar-even channel $P_{\mathrm{avg}}^{\pi}$ (proxy $m_\pi$).

We introduce no fourth calibration or numerological substitution. The clauses of [`prop:three-calibration-inputs`](#prop:three-calibration-inputs) remain in force.

## CAL-1 ($m_e$) — unit choice + cohomological period

CAL-1 has two roles:

| Role | Type | Status |
|---|---|---|
| Unit of mass (MeV $\leftrightarrow$ natural units) | dimensional convention | **unit choice** |
| Numerical value $m_e(\text{natural}) = \mathrm{Li}_2(q^{-2}) / \hbar_q^2 \approx 112$ | dimensionless | **cohomologically derived** |

The framework requires the conversion factor $m_e(\text{MeV})/m_e(\text{natural}) \approx 4.57 \times 10^{-3}$ MeV. This is a unit choice, not a fundamental constant.

## CAL-2 ($m_\mu/m_e$) — substrate $q_0$ pin

CAL-2 fixes $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$.

- $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) = 6\,\Lambda(\pi/3) \approx 2.0299$ is pure cohomology (no CODATA input).
- $\hbar_q = (q-1)/q$ is pure algebra (no CODATA input).
- $q_0 \approx {{ qou.computations.q-pinning-50-digit.derived_50_digit.q | precision: 6 }}$ is pinned by matching $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ to the CODATA-2022 value ${{ qou.computations.q-pinning-50-digit.calibration_inputs.m_mu_over_e_str | precision: 10 }}$.

The relation $m_\mu = m_e \times \mathrm{Vol}(4_1)/\hbar_q^2$ is structurally tautological. We defined $q_0$ to enforce it. The muon is the structurally preferred anchor due to a self-duality: the figure-eight knot $4_1$ is amphichiral, and its Neumann–Zagier complex volume is real ([`prop:self-dual-higgs-real-volume`](../braids-and-knots/self-dual-higgs-real-volume.md)). It pins $q_0$ through a quantity with zero imaginary (decay) content. In contrast, the proton pins $m_p/m_e$ through a modulus of a many-body binding endomorphism. The muon provides the cleanest $q_0$ determination. The residual $\mu$–$p$ tension ($\approx 11.6$ ppb in $q_0$) is the genuine substrate floor. The neutron-decay observable does **not** supply an independent third determination of the same modulus, and the $\mu$–$p$ tension is **not** a three-way consistency test. Both would follow from the point $q^{*}$ of [`rem:qstar-decay-sector-q0`](../mass-theory/rem-qstar-decay-sector-q0.md) coinciding with neither mass pin nor their precision-weighted mean, were that argument not circular: $q^{*}$ is *defined* as the root of $S(q) = c_3(q) + \mathrm{Vol}(4_1)$, so locating it presupposes $c_3^{\mathrm{even}} = -\mathrm{Vol}(4_1)$ — the hypothesis such a test would have to be independent of. It is independent of the two *mass* pins, which is a different and weaker statement.

Quantitatively, $q^{*}$'s placement carries no information beyond $\mathrm{Vol}(4_1)$'s own value. Every constant $V$ in the window $(-c_3(\mu), -c_3(\mathfrak{p})) = (2.0202, 2.0693)$ puts a zero between the anchors, and as $V$ sweeps that window $q^{*}_V$ sweeps the whole anchor interval; $\mathrm{Vol}(4_1) = 2.0299$ sits $80.30\%$ of the way from the proton end, which is exactly the "$\approx 80.3\%$ muon-ward" figure quoted for $q^{*}$. The placement is a restatement of $c_3(q_0) \approx -\mathrm{Vol}(4_1)$ to $0.48\%$, not a decay-sector preference.

So the substrate rests on **two** pins, and the $\mu$–$p$ tension ($\approx 11.6$ ppb) is a two-way tension. What the decay sector does supply is a genuine falsifiable lever of a different kind: $dq^{*}/d\mathfrak{Q}_\beta \approx -0.539$, so a sharper neutron $Q$-value sharpens $q^{*}$ — but sharpening a quantity defined by an assumed offset tests the offset, not the modulus.

### Which pin the numbers actually use

The paragraph above argues that the muon is the *structurally* preferred anchor. It is not the pin the computed values use.

| Layer | Pins $q_0$ on | $q_0$ | Status of $m_\mu$ |
|---|---|---|---|
| Ideal (canonical 3-CAL) | $m_\mu/m_e$ — CAL-2, proxy for $P_{\mathrm{skew}}^{\beta}$ | ${{ qou.computations.q-pinning-50-digit.derived_50_digit.q | precision: 17 }}\ldots$ | anchor input; exact *by construction* |
| Experimental (Physical-Observations) | $m_p/m_e$ | $1.1099785827513808\ldots$ | a **prediction**, and a $9.5\sigma$ one |

The two differ by $\approx 11.6$ ppb — the $\mu$–$p$ tension itself. Production compute takes the experimental pin, for one reason: $m_p/m_e$ is known to $0.017$ ppb against the muon ratio's $22$ ppb, so pinning there puts the unavoidable theory residual where it costs least. Anchoring on the muon instead would leave the proton wrong by $\approx 1.4 \times 10^{4}\,\sigma$; anchoring on the proton leaves the muon wrong by $9.5\sigma$. Neither is a free choice, and the arithmetic — not a preference — selects the second.

This is a *precision substitution within one overdetermined datum*, not a fourth calibration and not a redefinition of CAL-2. The canonical triple is unchanged; only the numerical evaluation moves.

Two consequences follow:

- **An $m_\mu$ reproduced at the muon pin is not an accuracy result.** It is the calibration restated. Quoting it as a prediction double-counts the input.
- **The two layers must never be mixed inside a single computed quantity.** A number built from an ideal-layer input and an experimental-layer input carries the $11.6$ ppb tension as a silent error term, regardless of how small the final discrepancy looks.

## CAL-3 ($P_{\mathrm{avg}}^{\pi}$, proxy $m_\pi$) and CAL-2 proxy $\mathfrak{Q}_\beta$

CAL-3 is the pion-sector bar-even channel $P_{\mathrm{avg}}^{\pi}$ (proxy $m_\pi$). This is independent of $(m_e, q_0)$. The parameter $\mathfrak{Q}_\beta$ proxies CAL-2.

The derived $\mathfrak{Q}_\beta$ fixes the hadronic scale $\mathfrak{E}_0$ via $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$.

- The leading-order base $\mathfrak{Q}_\beta = |\varepsilon(\Delta)| \cdot \mathfrak{E}_0$ is evaluated with $\varepsilon$ as the canonical Convention-D Markov trace at $z_D = q^3/(q^2+1)$. With the tower-summed $\mathfrak{E}_0$ this gives $0.4491$ MeV, a $-42.59\%$ miss ($0.4447$ MeV with the order-zero $\mathfrak{E}_0$), pending the convention-D $c_k$ ladder.
- The +0.17% match of the retired Form A ($\varepsilon$ weighting every basis element by $1$, the trace at $z = 1$) is either a truncation residual or a substrate artefact. It is kept only as a historical cross-check.
- Higher-order corrections correspond to traces over Khovanov-Rozansky strata.

## Summary table

| CAL | Pinned quantity | Cohomological derivation candidate | Status |
|---|---|---|---|
| CAL-1 | $m_e$ | $\mathrm{Li}_2(q^{-2}) / \hbar_q^2$ | **unit-choice + derived** |
| CAL-2 | $q_0$ via $m_\mu/m_e$ | $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | **open** |
| CAL-3 | $m_\pi$ | independent of $(m_e,q_0)$ | **genuine input** |
| *(derived)* | $\mathfrak{E}_0$ via $\mathfrak{Q}_\beta$ | Khovanov-Rozansky strata | **open** |

## Scope exclusions

This analysis:
- Proposes no fourth calibration.
- Does not claim $q_0$ is cohomologically derived.
- Retains the no-fourth-CAL discipline.
- Introduces no fitting inputs.

It structuralizes the framework's calibrations.

## Significance

The framework aims to reduce the Standard Model's 19 free parameters to a single unit choice, a categorically extracted $q_0$, and a derived hadronic residual.
