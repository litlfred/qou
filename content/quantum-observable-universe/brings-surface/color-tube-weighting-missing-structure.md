The low-isotope sign-flip diagnostic ([`low-isotope-sign-flip-diagnostic.witness.json`](../../computations/low-isotope-sign-flip-diagnostic.witness.json), PR [#1089](https://github.com/litlfred/qou/pull/1089)) shows that the per-isotope error correlates with inter-nucleon arc **count** at $R^2 = 0.83$, not with the signed-h weight ($R^2 = 0.26$). This indicates the **uniform-flavor projection** is missing a per-arc structural detail. The color-pair weight $W_{c_1 c_2}$ encodes exactly this detail.

The empirical match between the (now-purged) $\lambda_{\mathrm{scale}}$ literal $2.4599527869$ and the color-tube Faddeev resummation $1/(1 - h_q \cdot q_0^{10}) \approx 2.450$ (per [`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)) provides independent evidence that 10-fold color-tube averaging is the categorical structure behind the historical numerology.

Probe scripts [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py) and [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py) report that Scheme 4 (per-sheet PL integration on Bring's surface with quark-content weighting) reproduces $\Delta m_{n-p}$ to ${\sim}0.14\%$. This dramatically improves on the uniform-flavor projection's ${\sim}305\,\mathrm{ppm}$ flavor split ratio.

The **gg-production collapse** isolates the cost of the projection directly. Decomposing the production binding $B_{\mathrm{sym}} = \alpha\,\ln(\mathrm{tr}_{\mathrm{free}}/\mathrm{tr}_{\mathrm{atom}})$ into its per-bond log-suppressions $L_{\mathrm{pp}}, L_{\mathrm{pn}}, L_{\mathrm{nn}}$ at $q_0$ gives $L_{\mathrm{nn}}/L_{\mathrm{pp}} - 1 \approx 78\%$ ([`charge-symmetry-bond-probe.witness.json`](../../computations/probes/charge-symmetry-bond-probe.witness.json)). This represents roughly $570\times$ the substrate-derived $p/n$ flavor split $\delta_{\mathrm{lead}} \approx 0.14\%$ and $78\times$ the experimental charge-symmetry-breaking bound. This over-break derives entirely from the $\sigma$-vs-$\sigma^{-1}$ inter-crossing sign of the flavor-only projection. Gluons couple color, not flavor. The leading gg interface is the single flavor-blind color-average $\sigma_{\mathrm{avg}} = \sigma - (h/2)\cdot 1$ for every bond type. Forcing all inter-nucleon crossings to $\sigma_{\mathrm{avg}}$ collapses the $78\%$ asymmetry to $0$ ([`gg-production-bond-probe.witness.json`](../../computations/probes/gg-production-bond-probe.witness.json)). The sub-leading flavor weighting $W_{c_1 c_2}$ reintroduces the correct $\delta_{\mathrm{lead}}$-scale split. The uniform-flavor projection manufactures an $O(1)$ charge asymmetry that the color-tube average removes.

## Open questions

1. **Closed form for $W_{c_1 c_2}$.** What are the exact rational weights from the SO(3)-fiber tensor over Bring?
2. **Color-pair $\to$ chirality sign $\epsilon$ rule.** Why is same-color $\mapsto +1$, opposite-color $\mapsto -1$?
3. **${}^{4}\mathrm{He}$ magic-shell saturation.** Does the color-tube weighting saturate at $A = 4$ (filled-shell analogue), producing the $A \cdot 8G$ closure observed in [`isotope_record_schema.py:186`](../../computations/isotope_record_schema.py)?
4. **Cross-check $\rho_F$ density rule.** Does color-tube weighting yield a categorical reading of the Kashaev density factor $\rho_F \in \{m_e, 2 m_e\}$?

## Cross-references

- Parent sign-flip audit: [`docs/audits/-sign-flip-interpretation.md`](../../docs/audits/-sign-flip-interpretation.md)
- ${}^{4}\mathrm{He}$ magic-shell color-tube reading: [`docs/audits/-4he-magic-shell-color-tube-audit.md`](../../docs/audits/-4he-magic-shell-color-tube-audit.md)
- Bring color-tube weighted averaging cheat-sheet entry: [`docs/canonical-derivation-cheat-sheet.md` §"Bring color-tube weighted averaging"](../../docs/canonical-derivation-cheat-sheet.md)
- Empirical probe scripts: [`probe_pn_flavor_asymmetry.py`](../../computations/probe_pn_flavor_asymmetry.py), [`probe_per_sheet_flavor_nonin.py`](../../computations/probe_per_sheet_flavor_nonin.py)
