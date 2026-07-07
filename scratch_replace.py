import sys

with open("/Users/litlfred/space_cats/qou/amalgamated_input/appendix-knot-periodic-table_seq1.md", "r") as f:
    text = f.read()

replacements = [
    (
        "The atlas answers a single question: if every particle and atom is a\nconfined braid at the substrate value $q_0$, which specific knot or\nlink is each one, and does the invariant that knot carries reproduce\nthe measured mass or binding energy? Collecting the answer as one\n$q_0$-indexed registry — rather than an isolated calculation per\nisotope — lets a composite entry be built recursively from the nucleon\nand $\\alpha$-cluster entries it contains, and lets every prediction be\nread against the same AME 2020 reference column. The construction\nmechanics below make the identification precise; the layered extension\nthen carries the same machinery across every isotope.",
        "This atlas identifies the specific knot or link for each confined braid at the substrate value $q_0$, verifying whether its invariant reproduces the measured mass or binding energy. A single $q_0$-indexed registry enables recursive construction of composite entries from nucleon and $\\alpha$-cluster constituents, ensuring uniform comparison against the AME 2020 reference. We detail the precise identification mechanics below; a layered extension then applies this machinery to every isotope."
    ),
    (
        "*Each entry of the atlas is determined by the\n[GB-NF / confinement source of truth](#def:confined-particle): a\nparticle/atom is identified by the Markov-equivalence class\n$[K]_M$ of its canonical Hecke element $T_w \\in H_{n_0}(q_0)$,\nexpressed in $\\sigma_*$ braid generators of the braid group $B_{n_0}$.\nConfinement at $q_0$ is verified via the\n[confinement SDP](#prop:confinement-sdp).*\n\n*Each entry occupies **two rows**: the first gives the braid word\nin normal form (NF, shortlex Gröbner–Shirshov); the second gives\nthe prediction and AME residual. Composite entries reference\nearlier entries (recursive structure).*".replace("\\n", "\n"),
        "*The [confinement source of truth](#def:confined-particle) determines each entry. A particle or atom is identified by the Markov-equivalence class $[K]_M$ of its canonical Hecke element $T_w \\in H_{n_0}(q_0)$, expressed in $\\sigma_*$ generators of the braid group $B_{n_0}$. The [confinement SDP](#prop:confinement-sdp) verifies confinement at $q_0$.*\n\n*Each entry occupies **two rows**: the first gives the braid word in normal form (NF, shortlex Gröbner–Shirshov); the second gives the prediction and AME residual. Composite entries reference earlier entries.*".replace("\\n", "\n")
    ),
    (
        "Every atlas entry carries a **methodology tag** recording how its\nparticle–knot identification was obtained.",
        "Every entry carries a **methodology tag** recording its derivation method."
    ),
    (
        "The principled pipeline computes $\\mathrm{Vol}_{\\mathrm{hyp}}$ from the\n$\\sigma$-braid word at $\\geq 50$ decimal digits via SnapPy's\n`Link(braid_closure=...).exterior.high_precision` inside\n`mpmath.workdps(50)`; symbolic-in-$q$ Markov-trace coefficients $y_\\lambda$\nare supplied by the Wenzl bridge ([`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/y_lambda_wenzl_bridge_extended.py)).\n\nFor atoms $A \\geq 5$, where the combinatorics of the full $\\mathcal{H}_{3A}$ space explode and `SnapPea` topological limits fail, we bypass the full evaluation by taking the exact symbolic trace restricted solely to **active block-partitions** (`closed_form_tau_M`), sidestepping the combinatorial blow-up. This exact symbolic trace $B_{sym} = -\\alpha \\ln |\\tau_M|$ is shown side-by-side with the rigorous Q-CLT finite-sum approximation $B_{qCLT} = -\\alpha \\sum \\ln |\\hat{V}_i|$.",
        "The principled pipeline computes $\\mathrm{Vol}_{\\mathrm{hyp}}$ from the $\\sigma$-braid word at $\\geq 50$ decimal digits via SnapPy's `Link(braid_closure=...).exterior.high_precision` and `mpmath.workdps(50)`. The Wenzl bridge ([`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/y_lambda_wenzl_bridge_extended.py)) supplies symbolic-in-$q$ Markov-trace coefficients $y_\\lambda$.\n\nFor atoms $A \\geq 5$, the combinatorics of $\\mathcal{H}_{3A}$ explode and `SnapPea` limits fail. We sidestep this by computing the exact symbolic trace restricted to active block-partitions (`closed_form_tau_M`). We show this exact trace $B_{sym} = -\\alpha \\ln |\\tau_M|$ alongside the rigorous Q-CLT finite-sum approximation $B_{qCLT} = -\\alpha \\sum \\ln |\\hat{V}_i|$."
    ),
    (
        "For reference, the following closures appear in the atlas. Each\nshows the braid word and its closed-knot/link form.",
        "The following closures appear in the atlas, providing the braid word and its closed knot/link form."
    ),
    (
        "Word: $\\sigma_1^3$. Closure (in $B_2$, two-strand braid closed\ninto a single circle): the **trefoil knot**, simplest nontrivial\nprime knot. Alternative names: $T_{2, 3}$, left-handed trefoil\n(positive crossings) or right-handed (with $\\sigma_1^{-3}$).\nUsed for: **electron** ($e^-$), and as the binding factor for\nnucleons in $H_3$. Hyperbolic volume: $0$ (torus knot).",
        "Word: $\\sigma_1^3$. Closure: the **trefoil knot** ($T_{2, 3}$, left-handed, or simplest nontrivial prime knot). Used for: the **electron** ($e^-$), and as the nucleon binding factor in $H_3$. Hyperbolic volume: $0$ (torus knot)."
    ),
    (
        "Word: $\\sigma_1 \\sigma_2^{-1} \\sigma_1 \\sigma_2^{-1} \\sigma_1 \\sigma_2^{-1}$.\nClosure: three pairwise-unlinked circles that are jointly linked\n(remove one $\\to$ all separate). Hyperbolic volume:\n$\\mathrm{Vol}(\\mathcal{B}_3) = 8 G \\approx 7.328$ (Catalan-related).\nUsed for: **proton** $B_3(\\mathrm{uud})$, **neutron** $B_3(\\mathrm{udd})$,\nwhere the flavor labels colour the crossings.",
        "Word: $(\\sigma_1 \\sigma_2^{-1})^3$. Closure: three pairwise-unlinked circles that are jointly linked. Hyperbolic volume: $\\mathrm{Vol}(\\mathcal{B}_3) = 8 G \\approx 7.328$. Used for: the **proton** $B_3(\\mathrm{uud})$ and **neutron** $B_3(\\mathrm{udd})$, where flavor labels colour the crossings."
    ),
    (
        "Word: $\\sigma_1 \\sigma_2^{-1} \\sigma_1 \\sigma_2^{-1}$. Closure: the\n**figure-eight knot**, amphichiral (equal to its mirror).\nHyperbolic volume: $\\mathrm{Vol}(4_1) = :val[Vol_4_1]{precision=6} \\cdot \\pi$, the\nsmallest among hyperbolic knots. Used for: **Higgs field** (mass\nmechanism).",
        "Word: $(\\sigma_1 \\sigma_2^{-1})^2$. Closure: the amphichiral **figure-eight knot**. Hyperbolic volume: $\\mathrm{Vol}(4_1) = :val[Vol_4_1]{precision=6} \\cdot \\pi$ (smallest hyperbolic volume). Used for: the **Higgs field** (mass mechanism)."
    ),
    (
        "Word: $\\sigma_1^2$. Closure: two circles linked once. Hyperbolic\nvolume: $0$ (torus link). Used for: **gluon** (lowest force\ncarrier), and as the binding link in deuteron $D = [\\mathfrak{p}, \\mathfrak{n}]_{L_H}$.",
        "Word: $\\sigma_1^2$. Closure: two circles linked once. Hyperbolic volume: $0$ (torus link). Used for: the **gluon** (lowest force carrier) and the binding link in deuteron $D = [\\mathfrak{p}, \\mathfrak{n}]_{L_H}$."
    ),
    (
        "Word: $\\mathbf{1}_{B_4}$ (identity, no crossings). Closure:\n4 disjoint unknots — knot-trivial, but the 4 strands carry\npolarisation $\\times$ chirality components on the exceptional divisor\n$\\mathcal{S}_p$. Used for: **photon**, vacuum-flux carrier.",
        "Word: $\\mathbf{1}_{B_4}$ (identity, no crossings). Closure: 4 disjoint unknots. The 4 strands carry polarisation $\\times$ chirality components on the exceptional divisor $\\mathcal{S}_p$. Used for: the **photon** (vacuum-flux carrier)."
    ),
    (
        "Brief inventory of the hyperbolic-knot identifications used in\nthe atlas. Methodology tag indicates how each identification was\nobtained.",
        "This inventory lists hyperbolic-knot identifications and their methodology tags."
    ),
    (
        "Principled entries:\n\n- Tritium $^3$H at $\\sim 1.6 \\times 10^{-3}$ (`manual-historical`).\n- Deuteron $^2$H at $\\sim 1.1 \\times 10^{-2}$ (`manual-historical`).\n- $\\alpha$-cluster atoms ${}^{8}$Be–${}^{40}$Ca: mean $|\\mathrm{err}| \\sim 8$%\n (`recursive-on-⁴He`).\n\nAtlas covers $\\ell \\leq 2$ at $q_0$; further atoms ($\\ell = 3$\nmolecules, heavier nuclei) are covered by the all-atoms /\nall-isotopes extension below.",
        "Principled entry summary:\n\n- Tritium $^3$H: $\\sim 1.6 \\times 10^{-3}$ error (`manual-historical`).\n- Deuteron $^2$H: $\\sim 1.1 \\times 10^{-2}$ error (`manual-historical`).\n- $\\alpha$-cluster atoms ${}^{8}$Be–${}^{40}$Ca: mean $|\\mathrm{err}| \\sim 8$% (`recursive-on-⁴He`).\n\nThe atlas covers $\\ell \\leq 2$ at $q_0$. The all-isotopes extension below covers $\\ell = 3$ molecules and heavier nuclei."
    ),
    (
        "A layered framework extends the atlas to every isotope (real or\ntheoretical) under a single registry:",
        "A layered framework extends the atlas to all isotopes under a single registry:"
    ),
    (
        "Per-isotope records follow the [`IsotopeRecord`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py)\ndataclass schema with explicit knot-operator catalogue. Layer-1\npipeline implementation: [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_mass_table_extended.py).",
        "Per-isotope records follow the [`IsotopeRecord`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py) schema with an explicit knot-operator catalogue. The Layer-1 pipeline is implemented in [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_mass_table_extended.py)."
    ),
    (
        "Every per-isotope record exposes a structured list of the knot\noperators used to build its canonical braid. The primitives are:",
        "Each per-isotope record lists the knot operators used to build its canonical braid:"
    ),
    (
        "For an atom with mass number $A$, the canonical braid word in\n$B_{3A}$ is built sequentially per nucleon: at each $k \\in \\{0,\n\\ldots, A-1\\}$ apply the intra block at base $3k$ and $3k+1$,\nthen (for $k < A-1$) apply the inter-nucleon interface at $3k+2$\nbetween nucleon $k$ and $k+1$. The full sequence is enumerated by\n[`build_knot_operator_catalogue(Z, N)`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py)\nand reported in every per-isotope record.",
        "For an atom with mass number $A$, we build the canonical braid word in $B_{3A}$ sequentially per nucleon. At each $k \\in \\{0, \\dots, A-1\\}$, we apply the intra block at base $3k$ and $3k+1$. For $k < A-1$, we then apply the inter-nucleon interface at $3k+2$ between nucleon $k$ and $k+1$. The [`build_knot_operator_catalogue(Z, N)`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py) function enumerates this sequence."
    ),
    (
        "_Merged from the legacy `knot-periodic-table-grid` block (deleted as\npart of the atlas consolidation): the predicted neutron count\n$N_{\\mathrm{pred}}$ from the β-stability formula, the closed\n$\\alpha$ sub-links $k_\\alpha$ (structural cluster count), and the\nQOU mass $M_q$ vs. the observed AME2020 mass $M_o$. The per-Z\nsections below give the full isotope chain + L1/L2/L3 layer\nattribution; this section is the one-row-per-element rollup. See\n[knot-periodic-table intro](#prose:knot-periodic-table) for the\nmass-formula derivation and column-key conventions._",
        "_This table summarizes element stability: predicted neutron count $N_{\\mathrm{pred}}$, closed $\\alpha$ sub-links $k_\\alpha$, and predicted mass $M_q$ versus observed AME2020 mass $M_o$. The subsequent per-Z sections provide full isotope chains and layer attributions. See [knot-periodic-table intro](#prose:knot-periodic-table) for derivations and conventions._"
    ),
    (
        "_Auto-rendered from per-Z shards `canonical-isotope-witness-Z<NN>.witness.json` (emitted by [`canonical_isotope_witness.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_isotope_witness.py)). Each row carries the Layer used (L1 canonical |tr_M|, L2 α-cluster recursion, L3 paper-six-term [pending], L4 composite mass), the framework prediction, the AME 2020 reference, and the residual. `Predicts = mass` for free nucleons (p, n) — value is the Borromean tower nucleon mass conditional on `conj:borromean-baryon-mass-formula`. `Predicts = binding_energy` for D and up; AME 2020 reference is the total binding energy. $M_{\\text{composite}}$ is the L4 composite mass $N \\cdot m_n + Z \\cdot m_p - B$ when both nucleon masses (Borromean) and a binding-energy prediction are available; reference is the AME atomic mass converted via 1 u = 931.49410242 MeV._",
        "_Auto-rendered from per-Z shards [`canonical-isotope-witness-Z<NN>.witness.json`](https://github.com/litlfred/qou/blob/main/computations/canonical_isotope_witness.py). Each row reports the Layer used, the framework prediction, the AME 2020 reference, and the residual. Free nucleons (p, n) predict mass via the Borromean tower. Deuterium and heavier atoms predict binding energy. The L4 composite mass $M_{\\text{composite}}$ computes $N \\cdot m_n + Z \\cdot m_p - B$. AME mass is converted via $1 \\text{ u} = 931.49410242$ MeV._"
    )
]

# Ensure we do correct newline substitution
for orig, new in replacements:
    orig = orig.replace("\\n", "\n")
    new = new.replace("\\n", "\n")
    if orig not in text:
        print(f"FAILED TO FIND:\n{orig[:100]}...\n")
    else:
        text = text.replace(orig, new)

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-knot-periodic-table_seq1.md", "w") as f:
    f.write(text)

