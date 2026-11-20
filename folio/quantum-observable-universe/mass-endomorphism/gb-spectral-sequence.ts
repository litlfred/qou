import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gb-spectral-sequence",
  title:
    "GB-filtration spectral sequence and $E_\\infty$ convergence of the 6-term mass",
  lean: {
    ref: "qou:QOU.BraidKnot.gb_spectral_sequence",
    validation: "not_checked",
  },
  uses: ["def:hecke-normal-form"],
  tags: [
    "spectral-sequence",
    "cohomology",
    "hochschild",
    "gb-filtration",
    "e-infinity",
    "convergence",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-20",
      body: "**Caveat (W8, 2026-11-20, bean `qou-6qbv`): the confinement filtration does not filter the Hochschild complex.** At $n = 3$ the only block with nonzero knot-operator energy is $(2,1)$, so the decreasing reading used in the proof is $J^0 = H_3 \\supset J^1 = B_{(2,1)} \\supset J^2 = 0$. The proof's step that $J^\\bullet$ is an ideal filtration compatible with multiplication, so $d(F^p) \\subset F^p$, needs $J^a J^b \\subseteq J^{a+b}$, but $J^1 J^1 = J^1 \\neq 0 = J^2$. Explicitly, for $a = E_{00}$ and $x = E_{01}$ in $B_{(2,1)} \\cong M_2$, the 0-cochain $a \\in F^1$ has $(da)(x) = xa - ax = -E_{01} \\notin J^2$; 1020 entries of the differential lower the filtration (`computations/probes/gb_spectral_sequence_h3_probe.py`, exact). The Coxeter-length filtration does work. Separately, the rewriting map $d_H + d_F + d_{YB}$ of the definition paragraph is not a differential (`QOU.BraidKnot.GBRewriteDifferential`); the proof uses the Hochschild differential instead. Kind left unchanged pending the owner.",
    },
  ],
});
