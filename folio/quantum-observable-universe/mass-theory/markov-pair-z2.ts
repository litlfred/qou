import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-pair-z2",
  title:
    "All-pairs Markov-trace identity $\\mathrm{tr}_M(\\sigma_i\\sigma_j) = z^2$",
  tags: [
    "markov-trace",
    "hecke-algebra",
    "pair-factorization",
    "jet-tower",
  ],
  lean: {
    ref: "qou:QOU.Hecke.markov_pair_z2",
    validation: "not_checked",
  },
  uses: ["rem:mass-endomorphism-jet-tower"],
  cites: ["kassel1995", "jones1987"],
  computation: {
    engine: "sympy",
    script: "computations/markov/markov_peel_atomic_witness.py",
    witness: [
      "computations/markov/markov-peel-atomic-tr-m.witness.json",
      "computations/cross-check-trM-1ppb.witness.json",
      "computations/cross-check-trM-wenzl-lr-1ppb.witness.json",
      "computations/sweeps/paper-six-term-isotope-sweep.witness.json",
      "computations/delta-q-decoration.witness.json",
      "computations/probes/reeb-g-structural-identity.witness.json",
      "computations/qbeta/qbeta-c3-ladder-trace-convention-sensitivity.witness.json",
    ],
    consumers: [
      "computations/cross_check_trM_1ppb.py",
      "computations/cross_check_trM_wenzl_lr_1ppb.py",
      "computations/sweeps/paper_six_term_isotope_sweep.py",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-09",
      body: "**The proposition is convention-independent; the Hopf-link normalisation above\nis not, and has not been re-derived.**\n\n$\\mathrm{tr}_M(\\sigma_i\\sigma_j) = z^2$ follows from the Markov axiom alone and\nholds for any Markov parameter, so switching $z$ to **convention D**\n($z = q^3/(q^2+1)$, as the cited theorem now states) leaves the proposition\nuntouched.\n\nThe normalisation $J_{\\mathrm{Hopf}}(q) = -(q^{1/2}+q^{-1/2})\\cdot z^2$ is a\ndifferent matter. Its prefactor is the loop parameter at **half argument**,\n$[2]_{\\sqrt q} = q^{1/2}+q^{-1/2} = 2.0027\\ldots$ at $q_0$, whereas the\nTemperley–Lieb loop value of the production trace is\n$\\delta = [2]_q = q + q^{-1} = 2.010896866707122\\ldots$ — a $0.4\\%$ difference,\nand the two are conflated across the corpus (the reciprocal $1/\\delta =\n0.497290545604915556$ against $z_C = 0.499320334183694452$ is the same\nconfusion). The identity was derived when $z$ was $z_C$, and under convention D\n— which *is* the Jones/Temperley–Lieb trace — both the prefactor and $z^2$\nchange, so the displayed second equality\n$-(q+q^{-1})/(q^{1/2}+q^{-1/2})$ cannot be assumed to survive.\n\nThe displayed normalisation is the one derived under $z_C$. Obtaining the Jones\nnormalisation under D is a derivation, not a substitution.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body: "**Retracted and replaced, 2026-08-09.** This section read:\n\n> The value $z^2$ is the **Jones polynomial of the Hopf link** (unknotted\n> two-component linking) evaluated at the substrate parameter:\n> $J_{\\mathrm{Hopf}}(q) = -(q^{1/2} + q^{-1/2})\\cdot z^2\n> = -(q + q^{-1})/(q^{1/2} + q^{-1/2})$.\n\nThat is wrong three times over, and only the third is about the convention.\n\n1. **Wrong link.** $z^2 = \\mathrm{tr}_M(\\sigma_i\\sigma_j)$. The closure of\n   $\\sigma_1\\sigma_2$ in $B_3$ is the **unknot**; the closure of\n   $\\sigma_1\\sigma_3$ in $B_4$ is the **two-component unlink**. Neither is the\n   Hopf link, which is the closure of $\\sigma_1^2$ in $B_2$ and has trace\n   $\\mathrm{tr}_M(\\sigma_1^2) = hz + 1$, not $z^2$.\n2. **Wrong kind of object.** A raw Markov-trace value is not a Jones\n   polynomial. Without the loop factor $\\delta^{\\,n-1}$ and the framing\n   correction it is not even an invariant of the closure — it changes under\n   Markov stabilisation, which is exactly what $z$ measures.\n3. **Wrong loop parameter.** $q^{1/2}+q^{-1/2}$ is $[2]_{\\sqrt q} = 2.0027\\ldots$\n   at $q_0$; the Temperley–Lieb loop value of the production trace is\n   $\\delta = [2]_q = q+q^{-1} = 2.010896866707122\\ldots$ — the same conflation\n   as $1/\\delta = 0.4972905456\\ldots$ against the excised\n   $z_{\\mathrm{C}} = 0.4993203342\\ldots$.",
    },
    {
      kind: "caveat",
      date: "2026-08-09",
      body: "Hopf-link normalisation flagged as not re-derived under convention D; left as-is rather than patched. Beans qou-98g5 (δ vs z_C conflation) and qou-emyt.",
    },
  ],
});
