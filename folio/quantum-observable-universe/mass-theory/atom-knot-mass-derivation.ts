import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atom-knot-mass-derivation",
  title:
    "End-to-end derivation of atomic binding energies $B = \\nu_{\\mathrm{SDP}} \\cdot m_e \\cdot \\mathrm{Vol}_{\\mathrm{hyp}}(\\widehat{T_w})$ from the categorical action",
  lean: {
    ref: "qou:QOU.BraidKnot.atom_knot_mass_derivation",
    validation: "not_checked",
  },
  uses: [
    "prop:alpha-k-derivation-procedure",
    "prop:recursive-atom-knot-atlas",
  ],
  tags: [
    "mass-derivation",
    "two-leg",
    "geometric-leg",
    "algebraic-leg",
    "stokes",
    "frobenius-pairing",
    "reeb-density",
    "wedderburn",
    "hecke-trace",
    "gb-filtration",
    "jet-order",
    "volume-conjecture",
    "principled-pipeline",
    "algorithm",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/d_from_scratch.py",
    witness: [
      "computations/d-from-scratch.witness.json",
      "computations/unified-low-isotope-predictor.witness.json",
    ],
    status: "not_run",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Two hypotheses that appear in the Lean statement are shown there to be free rather than load-bearing: the $E_2$-collapse condition unfolds to $2 = 2$ and is discharged by reflexivity, and the Yekutieli condition is inhabitation of the braid-element type, which the mass identity does not mention." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling carries one condition the display above leaves implicit: that the certificate under discussion is one the pipeline actually emitted. A `MassDerivationCertificate` is a tuple of numbers, and its type records no provenance — a tuple with a negative $B_{\\mathrm{pred}}$ is well-typed. Stated for *every* certificate, the mass identity is false, so the conditional class carries an `IsPipelineDerived` predicate and the theorem takes it as a hypothesis. The ten AME-validated atoms below are proved to satisfy the identity directly, without the class." },
    {
      kind: "note",
      body: "**Notation.** The prefactor previously written $\\rho$ in this block is the **SDP-solution multiplicity** in the Wedderburn decomposition, an integer $\\in \\mathbb{Z}_{>0}$. To disambiguate from the distinct **categorical density** $\\rho_K \\in \\mathbb{R}_{>0}$ used in `prop:atomic-mass-gb-nf` (CODATA-fit scalar, e.g. $\\rho_K^{\\mathfrak{p}} \\approx 1723.6$), this block uses **$\\nu_{\\mathrm{SDP}} \\in \\mathbb{Z}_{>0}$** throughout. The old symbol $\\rho$ is reserved (i) for the Hoefsmit irrep representation $\\rho_\\lambda \\colon H_n(q) \\to \\mathrm{GL}_{d_\\lambda}$ and (ii) for $\\rho_K$ in `prop:atomic-mass-gb-nf`. See `docs/audits/-rho-notation-fix-recommendation.md` for the full notation audit.",
    },
    {
      kind: "caveat",
      body: "**Caveat (structural form).** The multi-term formula is the **first-principles structural form** of the mass invariant. At the substrate value $q_0$ it predicts $m_{\\mathfrak{p}} \\approx 5\\,\\mathrm{MeV}$ (off CODATA $938\\,\\mathrm{MeV}$ by $\\approx 173\\times$). The remaining factor is the **categorical density $\\rho_K$** of `prop:atomic-mass-gb-nf`, whose substrate-only derivation is an **open problem**. This block formalises what the brane-tower contributes; closure of the nucleon-mass anchors requires the additional categorical content in $\\rho_K$.",
    },
    {
      kind: "status",
      body: "**Class-A discipline status.** The 173$\\times$ shortfall is captured by $\\rho_K$ in `prop:atomic-mass-gb-nf`, which admits a **graded substrate expansion** (`prop:rho-k-graded-expansion`) — the LO piece $Z m_{\\mathfrak{p}} + N m_{\\mathfrak{n}} + Z m_e$ is **proved** (Wenzl 1988 Markov multiplicativity); the single-gen piece closes empirically to $0.18\\%$; the pair-gen piece is open. On the nucleon-anchor side, $m_{\\mathfrak{p}}$ has a **conjectural substrate form** (`prop:lambda-scale-substrate-form`) matching CODATA to ~5.4 ppm. This proposition is therefore a Class-A opt-out (conditional on the substrate forms above) per the three-calibration discipline; the structural form (this block) is correct and independent of the open pieces.",
    },
    {
      kind: "note",
      date: "2026-05-23",
      body: "**Historical note — single-term shorthand retired.** An earlier wording wrote $M(\\mathfrak{H}) = \\nu_{\\mathrm{SDP}} \\cdot \\mathrm{tr}_M(T_w)$ (single term, dropping the tower and Frobenius co-Casimir). That single-term form is **shorthand** for the multi-term sum and is structurally inadequate as a mass formula on its own (single-term fails by 87--100% on $D$, $T$, ${}^3\\mathrm{He}$; multi-term without the brane tower reduces error to 36--63%; the multi-term form with the canonical $\\mathrm{Li}_2^q$ brane tower reaches $\\approx 5\\,\\mathrm{MeV}$ for $\\mathfrak{p}$ at $q_0$). This block uses the multi-term form throughout; the single-term shorthand should not appear elsewhere in the paper.",
    },
  ],
});
