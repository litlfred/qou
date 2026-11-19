import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-plancherel-asymptotic-skeleton",
  title:
    "Asymptotic skeleton of the q-Plancherel measure $\\mathbb{M}_{n,q}$ — convergence on a continuous Young-diagram space",
  lean: {
    ref: "qou:QOU.Observations.QPlancherelAsymptoticSkeleton",
    validation: "not_checked",
  },
  cites: [
    "vershik-kerov1977",
    "biane1998",
    "feray-meliot2012",
  ],
  tags: [
    "causal-fermion-systems",
    "plancherel",
    "asymptotic-plancherel",
    "kerov-vershik",
    "wedderburn-weight",
    "thoma-simplex",
    "partly-established",
  ],
  uses: ["prop:wedderburn-weight-canonical", "prop:algebraic-gns-embedding"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "Owner ruling 2026-09-05, re-affirmed 2026-09-08 and 2026-11-15: the canonical Phi_k weight is Molien $f^\\lambda q^{-\\kappa_\\lambda}\\dim_q(\\lambda)/[n]_q!$ (`QOU.MathlibExt.MolienFakeDegreeGeneralN.molienSum`, `molienSum_eq_qFactorial`, verified against Féray–Méliot M_{n,q^2} in `computations/probes/molien_feray_meliot_bridge_probe.py`); $d_q^2/D^2$ is a labelled comparison arm (bean qou-oots). Prose previously called the choice open.",
    },
    {
      kind: "note",
      body: "Two citation defects were found in the course of this and are only partly repaired. The block cited `feray2010`, which is Féray, *Stanley's formula for characters of the symmetric group* (Ann. Comb. 13(4)) — a different paper by one of the two authors, not the $q$-Plancherel one. That is corrected here to `feray-meliot2012`. Separately, the previous text stated clause 2 as a variance bound $O(1/\\sqrt{n-3})$; that expression does not occur anywhere in [`feray-meliot2012`] (all 27 sections searched), whose fluctuation result is a central limit theorem at scale $\\sqrt{n}$. Clause 2 is restated above as what that paper proves. Where the $O(1/\\sqrt{n-3})$ form came from is not established — a Féray–Śniady-style character upper bound is the plausible family and the corpus holds one (`arxiv-math-0701051v4`), but it has not been checked there, and the honest status is \"unsourced\" rather than \"wrong\".",
    },
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/Observations/QPlancherelAsymptoticSkeleton.lean` uses " +
        "`Real.sqrt`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
