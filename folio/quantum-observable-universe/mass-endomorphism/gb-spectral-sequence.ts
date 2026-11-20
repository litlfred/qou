import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gb-spectral-sequence",
  title:
    "Length-filtration spectral sequence of the Hochschild complex of $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.gb_spectral_sequence",
    validation: "not_checked",
  },
  uses: ["def:hecke-normal-form"],
  cites: ["geckpfeiffer2000", "weibel1994"],
  tags: [
    "spectral-sequence",
    "cohomology",
    "hochschild",
    "coxeter-length",
    "nil-coxeter",
    "e-infinity",
    "convergence",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body: "**Rewritten on the Coxeter length filtration (owner, 2026-11-20, bean `qou-6qbv`).** The previous statement used the confinement filtration $J^\\bullet$ and a rewriting map $d_H + d_F + d_{YB}$, and claimed $E_\\infty \\Rightarrow \\mathrm{gr}\\,H_n$. Three defects, all measured: the rewriting map is not a differential (`QOU.BraidKnot.GBRewriteDifferential`, sorry-free); the confinement filtration is not preserved by the Hochschild differential ($J^1 J^1 = J^1 \\neq 0 = J^2$ at $n = 3$, 1020 violating entries); and the abutment of the Hochschild complex is $HH^*(H_n, H_n)$, of rank 3 at $n = 3$, not $\\mathrm{gr}\\,H_n$ of rank 6 (`computations/probes/gb_spectral_sequence_h3_probe.py`). Also dropped, not replaced: the claim that $\\mathrm{tr}_M$ is a $d$-closed $0$-cochain of $C^\\bullet(H_n, H_n)$ (it lies in $\\mathrm{Hom}_R(H_n, R)$, a $0$-cocycle with coefficients in the dual bimodule) and the pairing with the six-term mass, which this proposition does not establish. Downstream readings that need $E_2$ collapse are contradicted at $n = 3$ ($d_4 \\neq 0$). The Lean carrier `GBSpectralSequence` is an abstract class and does not formalise this statement.",
    },
  ],
});
