import { remark } from "../../schema/builders";

export default remark({
  label: "rem:curvature-rank-gb-stratification-proof-sketch",
  title: "Proof sketch for the curvature-rank stratification",
  interprets: "conj:curvature-rank-gb-stratification",
  uses: ["conj:curvature-rank-gb-stratification"],
  authorNotes: [
    { kind: "caveat", date: "2026-11-20", body: "**Caveat (2026-11-20, bean `qou-6qbv`): the cited `prop:gb-spectral-sequence` no longer has $E_0^{\\ell,*} = J^\\ell / J^{\\ell+1}$.** It was rewritten on the Coxeter length filtration, because the confinement filtration $J^\\bullet$ is not preserved by the Hochschild differential ($J^1 J^1 = J^1 \\neq 0 = J^2$ at $n = 3$; `computations/probes/gb_spectral_sequence_h3_probe.py`). Step 4 here reads the old statement and is unsupported by its citation." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): > degree $0$, and cannot stratify anything. Proved as\n> `QOU.BraidKnot.WordFiltration.map_pow_eq_bot`." },
  ],
});
