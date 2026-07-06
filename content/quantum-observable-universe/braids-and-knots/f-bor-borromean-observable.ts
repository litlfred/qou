import { definition } from "../../schema/builders";

/**
 * The Borromean categorical observable F_Bor(q) — the natural
 * Wedderburn-content-shifted combination
 *
 *   F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q^3
 *             = |tr_M(β_Bor, q)| / y_(3)(q)
 *
 * built from two Lean-proved closed forms:
 *
 *   |tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶) / (h² + 4)
 *                    (thm:borromean-markov-trace-closed-form)
 *
 *   [3]_q! = (q² + 1 + q⁻²)(q + q⁻¹) = (h² + 3) · [2]_q
 *           (thm:q-schur-y-lambda-closed-form)
 *
 * Generic-q identity over any commutative ring carrying q as a unit.
 * No archimedean specialisation, no q_0 numerical pin: those live
 * in the archimedean substrate-evaluation block at
 * appendix-qvalues/proton-mass-substrate-identity.
 *
 * Structural-integer identifications:
 *   - 2  = dim V_{(2,1)} — classical dimension of the standard irrep
 *          of S_3, Lean-proved via hook-length in DimStandardRepS3.lean
 *   - 12 = dim V_{(2,1)} · |S_3| = 2 · 6, Poincaré P_3(1) classical
 *          limit of [3]_q!
 *
 * Both integers are categorical (group dimensions / orders), available
 * over any base ring.
 *
 * Authoring history: factored out 2026-06-01 from the previously-
 * combined prop:proton-mass-substrate-identity block (see q-usage
 * audit, docs/audits/2026-06-01-q-usage-dispensation-plan.md, Policy
 * C/1 split).
 */
export default definition({
  label: "def:f-bor-borromean-observable",
  title:
    "Borromean categorical observable $F_{\\mathrm{Bor}}(q) := |\\mathrm{tr}_M(\\beta_{\\mathrm{Bor}}, q)| \\cdot [3]_q! / q^3$",
  uses: [
    "prop:borromean-markov-trace-closed-form",
    "prop:y-lambda-closed-form-wenzl-bridge",
  ],
  cites: [
    "chlouveraki2016-hdr",
    "wenzl1988c",
  ],
  tags: [
    "borromean",
    "categorical-observable",
    "wedderburn",
    "content-shift",
    "lean-proved-building-blocks",
    "h-expansion-rational",
  ],
});
