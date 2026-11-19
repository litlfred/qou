import { prose } from "../../schema/builders";

export default prose({
  label: "sec:fine-structure-data",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/meson-em-sinh-closed-form.witness.json",
      "computations/alpha-em-form-ladder.witness.json",
      "computations/alpha-em-schwinger-ladder.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "fine-structure-constant",
    "CODATA",
    "experimental",
    "coupling",
    "data",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "CODATA 2018 (137.035999084(21)) is superseded by CODATA 2022 (137.035999177(21), +0.679 ppb shift) and retained solely as an edition-comparison benchmark.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body: "**`det G_q` disambiguated; $\\alpha^{-1}$ is convention-independent.** This block previously wrote the Chern--Simons damping factor as $\\kappa = \\det G_{\\mathrm{cl}} / \\det G_q$, with no subscript, while the corpus uses the same unsubscripted glyph for the $6 \\times 6$ Markov--Gram $G_{ij} = \\mathrm{tr}_M(b_i b_j)$ of the $H_3(q)$ normal-form basis (`prop:frobenius-gram-matrix`). The two are different matrices, and the distinction is load-bearing: the Markov--Gram determinant is $-0.18920521914403668$ under the excised trace convention C and **$0$ exactly** under the production convention D, where the form is singular and $G^{-1}$ does not exist (`tools/pyhecke/python/pyhecke/gram.py`, `QOU/QBeta/GramSignature.lean`). Had $\\alpha^{-1}$ sat downstream of that determinant, the headline number would be wrong. It does not. $G_{\\mathrm{CS}}$ is the $2 \\times 2$ Chern--Simons pairing Gram of $(T_{2,9}, T_{3,5})$ on Bring's surface, built from $\\pi$, the torus-knot data $(m_i, n_i)$ and the quantum integers $[2]_q, [3]_q, [5]_q, [9]_q$; no Markov parameter $z$ enters it, and none enters $\\hbar_q = 1 - q^{-1}$. Verified by reading the producer `computations/substrate/hecke_core_symbolic.py::alpha_em_inv_sym_exact` and re-evaluating it independently at mpmath 60 dps: bare $136.82320885358258431$, $\\delta_{\\mathrm{CS}} = 0.0015506021328500969$, $\\kappa = 1.721614201708788213$, $\\det G^{\\mathrm{cl}}_{\\mathrm{CS}} = 60.630144110670241284$, $\\det G^{q}_{\\mathrm{CS}} = 35.21703297433989011$, resummed $\\alpha^{-1} = 137.03593509397560466$ ($-0.4676$ ppm vs CODATA 2022) --- every published digit in this block reproduced. **No number was changed**; only the symbol was qualified, here and at the other use sites (`rem:em-coupling-chern-simons`, `rem:alpha-em-derivation-open-problems`). The separate question of whether $\\kappa$ is *derived* is untouched and remains open (`rem:alpha-em-derivation-open-problems`).",
    },
  ],
});
