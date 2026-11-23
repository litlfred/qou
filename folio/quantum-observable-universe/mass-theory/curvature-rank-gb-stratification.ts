import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:curvature-rank-gb-stratification",
  title: "Curvature-rank stratification of the GB filtration",
  lean: {
    ref: "qou:QOU.WedderburnMass.CurvatureRankGbStratificationContext",
    validation: "not_checked",
  },
  uses: [
    "prop:frobenius-s-classification",
    "def:hecke-curvature-2-cocycle",
    "def:curvature-rank",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted from `prop:` to `conj:` (owner, 2026-11-20, bean `qou-6qbv`).** The proof's Step 2 reads $J^\\bullet$ as the image of $I^\\ell$, which is zero above degree $0$ because $I = \\ker\\pi$ (`QOU.BraidKnot.WordFiltration.map_pow_eq_bot`). Step 4 cited `prop:gb-spectral-sequence` for $E_0^{\\ell,*} = J^\\ell/J^{\\ell+1}$; that proposition now uses the Coxeter length filtration, because the confinement filtration is not preserved by the Hochschild differential ($J^1 J^1 = J^1 \\neq 0 = J^2$ at $n = 3$; `computations/probes/gb_spectral_sequence_h3_probe.py`). With both steps gone the statement has no proof, so it is a conjecture. The old proof is kept as the remark `rem:curvature-rank-gb-stratification-proof-sketch`. The Lean carrier `CurvatureRankGbStratificationContext` encodes the two inclusions as fields and has no instance.",
    },
  ],
});
