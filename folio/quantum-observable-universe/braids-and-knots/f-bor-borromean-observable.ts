import { definition } from "../../schema/builders";

/**
 * The Borromean categorical observable
 *
 *   F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q^3
 *             = |tr_M(β_Bor, q)| · c_sign(q)
 *
 * where [3]_q!/q^3 is the Schur element of the sign character of H_3.
 * The normaliser is ASSERTED, not derived: q^k [3]_q! is a linear-
 * character Schur element only for k = ±3 and bar-symmetric only for
 * k = 0 (owner card 2026-11-21, option "PR plus F_Bor text").
 * Lean: QOU/MassTheory/ProtonQ3SchurElement.lean.
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
 * combined conj:proton-mass-substrate-identity block (see q-usage
 * audit, docs/audits/2026-06-01-q-usage-dispensation-plan.md, Policy
 * C/1 split).
 */
export default definition({
  label: "def:f-bor-borromean-observable",
  title:
    "Borromean categorical observable",
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
    "schur-element",
    "asserted-normaliser",
    "lean-proved-building-blocks",
    "h-expansion-rational",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "External-reader provenance note (consolidated after retirement of `appendix-qvalues/proton-borromean-assembly` in `52721aa56f3`): the integer $12 = 2 \\cdot 6 = \\dim V_{(2,1)} \\cdot |\\mathfrak{S}_3|$ is purely categorical (standard irrep dimension times group order, classical limit $P_{\\mathfrak{S}_3}(1) = 6$), and not the inverse of an Ocneanu leading-pole coefficient $-1/12$. Deriving the linear proton-assembly law and the Wenzl-vs-$q$-Schur Poincaré factor $[3]_q!/q^3 = (1 + q^{-2})(1 + q^{-2} + q^{-4}) = P_{\\mathfrak{S}_3}(q^{-2})$ from first principles remains open.",
    },
  ],
});
