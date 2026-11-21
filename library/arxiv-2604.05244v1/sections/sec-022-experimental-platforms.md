---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-022-experimental-platforms
section_title: "Experimental platforms"
section_number: null
pages: 25-26
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.98
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
The six conditions of the Introduction are restrictive but not unrealizable. We briefly assess the main candidate platforms.

Two requirements pull in different directions. For the *theorem* (Airy edge of the sideband kernel), the ideal setting is a channel with energy-independent transmission under monochromatic drive---a QPC conductance plateau helps with the energy-independence part, but the sharp-step assumption (condition (4)) is a separate requirement. For the *transport prediction* (shot-noise plateau deficit), the signal carries the prefactor $\mathcal T(1-\mathcal T)$, which vanishes on a plateau where $\mathcal T\approx 0$ or $1$. The cleanest measurement therefore uses a partially transmitting single-channel beam splitter with approximately energy-flat transmission over the relevant sideband window $\sim 2A\hbar\Omega$.

Condition (4) requires care: a biased two-terminal device has two Fermi steps, giving a double-step occupation (Sec. [\[sec:multi-step\]](#sec:multi-step){reference-type="ref" reference="sec:multi-step"}), but when the bias window exceeds the edge width $\kappa_A$, the edge correlations near each step are governed by a thinned Airy kernel; the upper edge is clean, while the lower edge carries a smooth bulk background that is negligible for $\mathcal T\ll 1$. Condition (5) requires $T_{\rm el}\ll T_{\rm cross}\sim hf\kappa_A/k_B$, which at $f=10\;\mathrm{GHz}$ and $A=20$ gives $T_{\rm cross}\approx 1.1\;\mathrm{K}$---easily satisfied in a dilution refrigerator. Larger values $A\sim 50$--$200$ sharpen the collapse but make the wide-band requirement more demanding; moderate $A$ may be the most practical starting point. Condition (6), $A=eV_{\rm ac}/hf\gg 1$, requires $V_{\rm ac}\sim 0.8$--$8\;\mathrm{mV}$ at $10\;\mathrm{GHz}$ for $A\sim 20$--$200$, which is accessible though large enough that drive-induced heating must be monitored.

The most directly testable prediction is the Airy collapse of the shot-noise plateau deficit (Sec. [\[sec:transport\]](#sec:transport){reference-type="ref" reference="sec:transport"}). Photo-assisted shot noise measurements in QPCs are well established [@Schoelkopf1998; @Reydellet2003].

*Metallic tunnel junctions* [@LesovikLevitov1994] (Al/AlO$_x$/Al) are multichannel devices, but in the tunnel limit ($\mathcal T_i\ll 1$ for each channel) the shot noise is a sum of independent single-channel contributions, each weighted by $\mathcal T_i(1-\mathcal T_i)\approx\mathcal T_i$. The plateau deficit for each channel carries the same Airy edge structure; what changes is only the overall prefactor.

*SIS junctions* [@TienGordon1963], the historical setting of Tien--Gordon physics, satisfy conditions (2) and (6) but the BCS gap structure violates the wide-band condition (3) near the gap edge; whether the $A^{1/3}$ scaling survives there is open. *Superconducting microwave circuits* [@Clerk2010] are typically bosonic, invalidating the determinantal structure, unless a fermionic channel (e.g., an embedded normal-metal junction) is present. *AC-gate-driven quantum dots* [@PedersenBuett1998] suffer from Coulomb blockade (violating condition (1)) except in the open-dot regime, where achievable amplitudes ($A\sim 1$--$10$) limit the edge-scaling window. *Cold atoms in driven optical lattices* [@PlateroAguado2004] realize non-interacting Floquet regimes, but the Landauer scattering framework does not directly apply and a separate reformulation in terms of quasienergy band structure would be needed.
