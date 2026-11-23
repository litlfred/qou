import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:spectral-sequence-h3-explicit",
  title:
    "Explicit $d_1, d_2$ on $H_3(q)$ over $\\mathbb{R}[q, q^{-1}]$",
  lean: {
    ref: "qou:QOU.BraidKnot.SpectralSequenceH3Explicit",
    validation: "not_checked",
  },
  uses: ["prop:e-infinity-page-identifications"],
  tags: [
    "spectral-sequence",
    "explicit-differentials",
    "hecke-h3",
    "computation",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-20",
      body: "**Measured pages (W8, 2026-11-20, bean `qou-6qbv`, PR to follow).** Exact computation of the Hochschild spectral sequence of $H_3(q)$ (`computations/probes/gb_spectral_sequence_h3_probe.py`; integers mod two primes, $q = 2, 3$, all four runs agree; $d \\circ d = 0$ checked; $\\mathrm{HH}^{0,1,2} = 3, 0, 0$). Under the Coxeter-length filtration (weight $\\sum \\ell(w_i) - \\ell(v)$), the only filtration under which the complex is filtered: $d_1 = 0$; $d_2$ has rank 1, from degree 1 weight 0 to degree 2 weight 2; $d_3 = 0$; $d_4$ has rank 1, from degree 1 weight $-2$ to degree 2 weight 2; $E_5 = E_\\infty$. Degree 0 is untouched from $E_1$ on: three classes at weights $0, -2, -3$, the leading terms of the centre $Z(H_3)$. So the statement's \"$d_1$ acts through the Hecke relation\" is false for this filtration ($d_1 = 0$), and the cancellation happens at $d_2$ and $d_4$. Under the confinement filtration the sequence does not exist (see `prop:gb-spectral-sequence`).",
    },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
  ],
});
