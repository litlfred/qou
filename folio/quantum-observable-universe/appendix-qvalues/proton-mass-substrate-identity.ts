import { proposition } from "../../schema/builders";

/**
 * Archimedean substrate evaluation of the proton-mass identity at
 * substrate q_0:
 *
 *   m_p = 2 · m_μ · F_Bor(q_0) − 12 · m_e
 *
 * Matches CODATA m_p to 0.24 ppm (50-dps MPFR verified).
 *
 * The categorical observable F_Bor and its rational h-expansion live
 * in def:f-bor-borromean-observable (braids-and-knots/, generic q).
 * This block consumes that definition + the canonical flavor-split
 * (observations/flavor-split-substrate) and reports the archimedean
 * specialisation: at q = q_0, with m_e and m_μ in MeV from CAL-1 /
 * CAL-2.
 *
 * Combined with prop:flavor-split-substrate (canonically-derived
 * Hecke-skein flavor split), this gives a full m_p + m_n derivation
 * from only (m_e, m_μ, q_0) — CAL-3 ($\\mathfrak{Q}$_β) becomes a DERIVED quantity,
 * not an input.
 *
 * Authoring history: split out 2026-06-01 from a previously-combined
 * braids-and-knots/proton-mass-substrate-identity block. The
 * categorical F_Bor moved to def:f-bor-borromean-observable; this
 * block keeps only the archimedean substrate evaluation (per q-usage
 * audit Policy C/1 split, docs/audits/2026-06-01-q-usage-dispensation-plan.md).
 */
export default proposition({
  label: "prop:proton-mass-substrate-identity",
  title:
    "Aether-parameter evaluation: $m_p = 2 \\cdot m_\\mu \\cdot F_{\\mathrm{Bor}}(q_0) - 12 \\cdot m_e$ to $0.24\\,\\mathrm{ppm}$ at $q = q_0$",
  uses: [
    "conj:proton-borromean-assembly",
    "def:f-bor-borromean-observable",
    "prop:flavor-split-substrate",
  ],
  lean: {
    // §3b-cond conditional: the theorem takes the [ProtonBorromeanAssembly]
    // class hypothesis (conj:proton-borromean-assembly, in uses[] above) and
    // DERIVES this flat identity from it (12 = 2·6), sorry-free modulo the
    // class instance. Class + theorem live in the qou Lake library
    // (QOU/AppendixQValues/ProtonBorromeanAssembly.lean); no sibling .lean.
    ref: "qou:QOU.AppendixQValues.ProtonBorromeanAssembly.proton_mass_substrate_identity",
  },
  cites: [
    "adams1985hyperbolic",
    "wenzl1988c",
    "chlouveraki2016-hdr",
  ],
  computation: {
    engine: "python",
    script: "computations/m_p_substrate_identity_50dps.py",
    witness: "computations/m-p-substrate-identity-50dps.witness.json",
    status: "verified",
  },
  tags: [
    "mass-formula",
    "proton",
    "borromean",
    "substrate-evaluation",
    "archimedean",
    "ocneanu-cancellation",
    "bernoulli-12",
    "0.24ppm",
    "two-calibration-baryon",
  ],
});
