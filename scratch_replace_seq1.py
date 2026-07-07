import sys

with open("/Users/litlfred/space_cats/qou/amalgamated_input/appendix-qvalues_seq1.md", "r") as f:
    text = f.read()

replacements = [
    (
        "The QOU 3-calibration discipline reduces to **2 calibrations**\n$(m_e, m_\\mu/m_e)$ for the baryon + $\\mathfrak{Q}_\\beta$ sector (or equivalently\n$(m_e, q_0)$ via the muon-anchor identity $m_\\mu/m_e = \\mathrm{Vol}(4_1)/\\hbar_q^2$).",
        "The 3-calibration discipline reduces to **2 calibrations** $(m_e, m_\\mu/m_e)$ for the baryon and $\\mathfrak{Q}_\\beta$ sector. This equates to $(m_e, q_0)$ via the muon-anchor identity $m_\\mu/m_e = \\mathrm{Vol}(4_1)/\\hbar_q^2$."
    ),
    (
        "The production neutron now **consumes** the categorical\n$\\mathfrak{Q}_\\beta \\approx 0.78233\\,\\mathrm{MeV}$ (Kashiwara $b^2$, parameter-free)\ndirectly, so the historical $2113\\,\\mathrm{ppm}$ gap between the flavor-split\nmass-derived $\\mathfrak{Q}_\\beta$ and the categorical ladder is **closed at the\nproduction level**. The remaining open item is the *exact* closure —\npromoting the $\\mathfrak{Q}_\\beta$ near-match to a derivation — which would\ncohomologically prove the $q_0 \\leftrightarrow \\mathfrak{Q}_\\beta$ relationship.",
        "The production neutron directly **consumes** the parameter-free Kashiwara $b^2$ categorical $\\mathfrak{Q}_\\beta \\approx 0.78233\\,\\mathrm{MeV}$. This **closes** the historical $2113\\,\\mathrm{ppm}$ gap between the flavor-split mass-derived $\\mathfrak{Q}_\\beta$ and the categorical ladder at the production level. Exact closure remains open. Promoting the $\\mathfrak{Q}_\\beta$ near-match to a derivation would cohomologically prove the $q_0 \\leftrightarrow \\mathfrak{Q}_\\beta$ relationship."
    ),
    (
        "The ratio $\\mathfrak{D}_\\mu / \\mathfrak{D}_n$ eliminates $G_F$ and\nprovides a $\\mathfrak{Q}_\\beta$-independent consistency test: if both\n$\\mathfrak{m}_\\mu$ and $\\mathfrak{Q}_\\beta$ are substrate-derived, the lifetime\nratio $\\hbar/\\mathfrak{D}_n \\div \\hbar/\\mathfrak{D}_\\mu$ should match\nCODATA ($\\approx 4 \\times 10^8$) from categorical invariants alone.",
        "The ratio $\\mathfrak{D}_\\mu / \\mathfrak{D}_n$ eliminates $G_F$ and provides a $\\mathfrak{Q}_\\beta$-independent consistency test. If both $\\mathfrak{m}_\\mu$ and $\\mathfrak{Q}_\\beta$ are substrate-derived, the lifetime ratio $\\hbar/\\mathfrak{D}_n \\div \\hbar/\\mathfrak{D}_\\mu$ matches CODATA ($\\approx 4 \\times 10^8$) strictly from categorical invariants."
    ),
    (
        "**Remark (per-observable $100\\times$ experimental status — dashboard).**\n\n*This remark declares the live per-observable accuracy dashboard at\n[`computations/per-observable-100x-status.witness.json`](#) — emitted\nby [`per_observable_100x_status.py`](#) — as a first-class,\nauto-regenerated artifact, so its headline counts stay current instead\nof being hand-maintained. The witness reports the **L2 leg** of the\nprecision-goals: for each predicted observable, whether it meets its\n$100\\times$ accuracy target. Its `summary` field carries the headline\n(`total`, `beats_1x_count`, `beats_100x_count`) — read\n`beats_100x_count` for how many of the seven observables currently\npass and which still gate L2 closure.*",
        "**Remark (per-observable $100\\times$ experimental status — dashboard).**\n\n*This block designates the live per-observable accuracy dashboard at [`computations/per-observable-100x-status.witness.json`](#) — emitted by [`per_observable_100x_status.py`](#) — as a first-class, auto-regenerated artifact. Headline counts remain current without manual maintenance. The witness reports the precision-goal **L2 leg**: for each predicted observable, whether it meets its $100\\times$ accuracy target. Its `summary` field carries the headline (`total`, `beats_1x_count`, `beats_100x_count`). The `beats_100x_count` identifies how many of the seven observables currently pass and which still gate L2 closure.*"
    )
]

for orig, new in replacements:
    if orig not in text:
        print(f"FAILED: {orig[:100]}")
    text = text.replace(orig, new)

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-qvalues_seq1.md", "w") as f:
    f.write(text)
