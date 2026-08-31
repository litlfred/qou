import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-31",
      body:
        "**The substrate fixes the closure's component count, and all three " +
        "named links violate it.** The canonical word's letters are " +
        "`c·σ_g + d·1`, and `σ_g`, `σ_g⁻¹` project to the *same* " +
        "transposition, so the underlying permutation — hence the number of " +
        "components of the closure — is identical on every branch and under " +
        "every crossing-sign convention. Measured exact over `0 ≤ Z,N ≤ 5`, " +
        "both `pn_convention`s and nine bond multiplicities: `c_free = 2A` " +
        "(23/23) and `c_atom = 2A − #(odd-multiplicity bonds)` (414/414), so " +
        "`c_atom = A + 1` at the unit multiplicities the trace pipeline uses. " +
        "Independently corroborates `QOU.MassTheory.ClassicalTraceFloor`, " +
        "which derives the same two counts by a combinatorial merge argument. " +
        "Against that: `6_2` has 1 component where 3 are required, `8_11` 1 " +
        "where 4 are, `L6a4` 3 where 4 are. Intersected with each pick's own " +
        "volume window the candidate set is **empty** at ²H (0 of 799 census " +
        "manifolds) and ³H (0 of 1,102), and 29 of 26,843 at ³He. " +
        "**Scope:** this excludes identifying the named links with the " +
        "*closure of the canonical mass word*; it does not settle what object " +
        "`K` this conjecture intends, and the registry does carry `knot_name` " +
        "and `binding_link_name` as separate fields. What it does show is " +
        "that the complexity restriction " +
        "`docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md` asked for " +
        "exists, is derived, takes no `B_AME` input — and leaves nothing " +
        "standing at `A = 2, 3`. The ²H rows restate that audit's scope-(b) " +
        "finding; `A = 3` is new. Probe: " +
        "`computations/probes/link_assignment_census_selectivity_probe.py`; " +
        "beans `t7qv` (Gap #2), `qou-8ms1`.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's `ℝ` are SDP solver data: " +
        "`duality_gap_le : |primal_obj - dual_obj| ≤ (1e-6 : ℝ)` is a " +
        "**numerical tolerance** on an absolute value, and `min_block_eig`, " +
        "`min_dual_y_on_active`, `max_inactive_dual`, `alpha_gap` are " +
        "eigenvalue / shadow-price magnitudes. The uniqueness statement also " +
        "quantifies over `SDPPrimal (heckeDim n) ℝ Empty` and a " +
        "`Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ` — positive-" +
        "semidefiniteness is an ordering notion with no generic-ring " +
        "counterpart. Both the `≤ 1e-6` decimal and the PSD cone require " +
        "`ℝ`; this is the archimedean realisation, not a stray specialisation.",
    },
  ],
  label: "conj:canonical-knot-id-sdp",
  title:
    "Canonical knot identification for ${}^2$H, ${}^3$H, ${}^3$He from the confinement SDP",
  uses: [
    "prop:delta-max-uniform-bound",
    "conj:brane-tower-z-habiro",
  ],
  tags: [
    "tier:E",
    "knot-identification",
    "sdp",
    "confinement",
    "canonical",
    "deuterium",
    "tritium",
    "helium-3",
    "gap-a",
    "audit",
  ],
  lean: {
    // Points at the SORRY-FREE ³He uniqueness closure (interior
    // case, batch 13).  The abstract `canonical_T_w_subsingleton`
    // currently delegates to `strict_complementarity_unique` which
    // still has a sorry for the general kernel-uniqueness step;
    // this manifest cites the proven concrete instance instead.
    ref: "qou:QOU.BraidKnot.CanonicalKnotIdSDP",
  },
});
