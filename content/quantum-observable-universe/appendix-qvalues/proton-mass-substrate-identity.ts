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
 * from only (m_e, m_μ, q_0) — CAL-3 (𝔔_β) becomes a DERIVED quantity,
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
    "Substrate evaluation: $m_p = 2 \\cdot m_\\mu \\cdot F_{\\mathrm{Bor}}(q_0) - 12 \\cdot m_e$ to $0.24\\,\\mathrm{ppm}$ at $q = q_0$",
  uses: [
    "def:f-bor-borromean-observable",
    "prop:flavor-split-substrate",
  ],
  cites: [
    "adams1985hyperbolic",
    "wenzl1988c",
    "chlouveraki2016hdr",
  ],
  // lean ref deferred: this block's uses[] cone transitively touches
  // conjectural categorical derivations (the "2" structural integer,
  // the "12" via Ocneanu, F_Bor categoricity). Per AGENTS.md §3b-cond,
  // declaring a `lean:` field on a provable kind whose uses[] cone
  // touches `conj:` requires either downgrade to `remark`/`conjecture`
  // OR the conditional-class banner + [Class] Lean hypothesis pattern.
  // The Lean sibling (proton-mass-substrate-identity.lean) is currently
  // unconditional; without the banner + class hypothesis on the .md +
  // .lean, declaring the ref here trips the §3b-cond strict audit (CI
  // validate fail; see PR #1690 round-3 CI fail).
  // Follow-up: separate PR adding the conditional banner + restructure
  // the Lean theorem to take an explicit [ProtonMassSubstrateClass]
  // hypothesis. Until then the `validate` step warns
  // "no Lean declaration yet" (non-blocking).
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
