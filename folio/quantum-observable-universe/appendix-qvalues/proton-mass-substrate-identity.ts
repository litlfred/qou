import { conjecture } from "../../schema/builders";

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
export default conjecture({
  label: "conj:proton-mass-substrate-identity",
  title:
    "Substrate evaluation: $m_p = 2 \\cdot m_\\mu \\cdot F_{\\mathrm{Bor}}(q_0) - 12 \\cdot m_e$ to $0.24\\,\\mathrm{ppm}$ at $q = q_0$",
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
  authorNotes: [
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:proton-mass-substrate-identity` (owner, #8526, 2026-11-21; bean qou-tm3c). The block is `conj:proton-borromean-assembly` with $2 \\cdot 6 = 12$ substituted, plus a numerical comparison. The Lean class field `assembly` is the conclusion (AGENTS.md §3b-cond item 5)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Verification script: [`m_p_substrate_identity_50dps.py`](../../../computations/m_p_substrate_identity_50dps.py)." },
  ],
});
