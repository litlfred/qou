import sys

with open('content/quantum-observable-universe/appendix-knot-operations-archimedean/gluon-model-comparison.md', 'r') as f:
    text = f.read()

text = text.replace(
    "The nucleon normal form (NF) requires no explicit Hopf-link gluon factors beyond the Borromean braid $B_3 = (\\sigma_0\\sigma_1^{-1})^3$. Five candidate models illustrate this.\n\n**Definition recall** ([Borromean baryon](#def:borromean-baryon)).\n$B = \\mathcal{B}_3(K_{0_1}, K_{0_1}, K_{0_1}) \\oplus \\mathcal{L}_H$.\nThe three constituents are unknots; the Hopf link $\\mathcal{L}_H$ binds them. Flavour is the crossing orientation of each unknot within $\\mathcal{B}_3$: $\\mathfrak{u} = \\sigma$ (positive), $\\mathfrak{d} = \\sigma^{-1}$ (negative).",
    "The nucleon normal form (NF) requires no explicit Hopf-link gluon factors beyond the Borromean braid $B_3 = (\\sigma_0\\sigma_1^{-1})^3$. Five candidate models evaluate this constraint.\n\n**Definition** ([Borromean baryon](#def:borromean-baryon)).\n$B = \\mathcal{B}_3(K_{0_1}, K_{0_1}, K_{0_1}) \\oplus \\mathcal{L}_H$.\nThe three constituents are unknots bound by the Hopf link $\\mathcal{L}_H$. Flavour is the crossing orientation of each unknot within $\\mathcal{B}_3$: $\\mathfrak{u} = \\sigma$ (positive), $\\mathfrak{d} = \\sigma^{-1}$ (negative)."
)

text = text.replace(
    "Model A matches CODATA exactly (residual $< 10^{-6}$ MeV). The other models overshoot $|\\Delta|$, giving $|Q| > 0.87$ MeV.\n\nQuarks interact as single-crossing unknots, not as full trefoils (Definition 4.27.1): replacing each crossing with a full trefoil braid word ($\\sigma_0\\sigma_1\\sigma_0$ for $\\mathfrak{u}$, $\\sigma_0^{-1}\\sigma_1^{-1}\\sigma_0^{-1}$ for $\\mathfrak{d}$) triples $|\\Delta \\times E_0|$ to $-2.51$ MeV, away from CODATA.\n\n**Interpretation.**\nThe Borromean braid $B_3$ has NF:",
    "Model A recovers the CODATA value (residual $< 10^{-6}$ MeV). The other models overshoot $|\\Delta|$, yielding $|Q| > 0.87$ MeV.\n\nQuarks interact as single-crossing unknots, not as full trefoils (Definition 4.27.1). Replacing each crossing with a full trefoil braid word ($\\sigma_0\\sigma_1\\sigma_0$ for $\\mathfrak{u}$, $\\sigma_0^{-1}\\sigma_1^{-1}\\sigma_0^{-1}$ for $\\mathfrak{d}$) triples $|\\Delta \\times E_0|$ to $2.51$ MeV, deviating from CODATA.\n\n**Interpretation.**\nThe Borromean braid $B_3$ evaluates to:"
)

text = text.replace(
    "The $L_+$ and $L_-$ terms constitute the Hopf link $\\mathcal{L}_H$. The $\\oplus$ operation in $B = \\mathcal{B}_3 \\oplus \\mathcal{L}_H$ is intrinsic to the Borromean braid algebra, not an additional factor. Explicitly adding Hopf links (Models B–E) double-counts the gluon contribution. The braid $B_3 = (\\sigma_0\\sigma_1^{-1})^3$ completely encodes confinement ($\\mathcal{B}_3$) and gluon binding ($\\mathcal{L}_H$). \n\nThe near-cancellation $+0.046 - 0.044 = +0.002$ reflects baryon color neutrality. The $\\gamma$ term ($\\approx +0.998$) places $B_3$ perturbatively close to the identity.\n\nWe confirm the Model A proton and neutron NF:",
    "The $L_+$ and $L_-$ terms generate the Hopf link $\\mathcal{L}_H$. The $\\oplus$ operation in $B = \\mathcal{B}_3 \\oplus \\mathcal{L}_H$ is intrinsic to the Borromean braid algebra, not an appended factor. Explicitly adjoining Hopf links (Models B–E) double-counts the gluon contribution. The braid $B_3 = (\\sigma_0\\sigma_1^{-1})^3$ completely encodes both confinement ($\\mathcal{B}_3$) and gluon binding ($\\mathcal{L}_H$). \n\nThe near-cancellation $+0.046 - 0.044 = +0.002$ enforces baryon color neutrality. The $\\gamma$ term ($\\approx +0.998$) constrains $B_3$ perturbatively close to the identity.\n\nThe Model A proton and neutron normal forms evaluate as:"
)

text = text.replace(
    "The proton has net $\\approx +0.999$; the neutron has net $\\approx +0.811$. The difference $\\Delta \\approx -0.188$ calibrates the quark-level energy scale $E_0 = Q/\\Delta \\approx 4.155$ MeV.",
    "The proton evaluates to net $\\approx +0.999$ and the neutron to net $\\approx +0.811$. The difference $\\Delta \\approx -0.188$ normalizes the quark-level energy scale $E_0 = Q/\\Delta \\approx 4.155$ MeV."
)

with open('content/quantum-observable-universe/appendix-knot-operations-archimedean/gluon-model-comparison.md', 'w') as f:
    f.write(text)
