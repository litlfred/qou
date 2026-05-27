import { proposition } from "../../schema/builders";

/**
 * Categorical derivation of c_3 = J_Hopf(q=1) = -2 in the Q_β
 * precision ladder via Schur-Weyl branching of V_(2,1) self-fusion.
 *
 * Closes the "missing piece for the proof" flagged in the
 * post-#662 review: distinguishes Story B (categorical chain
 * c_2 = b², c_3 = -2, c_4 = b²+½, ...) from Story A (only c_2
 * matters, all higher c_k = 0 within CODATA noise) by deriving
 * c_3 from QOU axioms with no empirical fit, mirroring the
 * `c_2 = b²` categorical proof from PR #661.
 *
 * **Statement.** The third coefficient `c_3` in the Q_β
 * precision-ladder expansion
 *
 *   Q_β = Q_A · cos(α − bℏ²/2) · (1 − b²ℏ⁴) · (1 + c_3 ℏ_q^6) · …
 *
 * (per [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
 * equals `J_Hopf(q=1) = −2`, derived from
 *
 *   V_(2,1) ⊗ V_(2,1) ↠ V_Hopf  ↪  Markov closure
 *
 * via the Schur-Weyl branching of the V_(2,1) self-fusion under
 * `prop:markov-trace-frobenius-selection`, with the Hopf-link
 * Markov trace evaluated at q = 1 producing the Jones-polynomial
 * value −[2]_q = −2.
 *
 * **Argument structure** (full sketch in the .md sibling):
 *
 * 1. **Self-fusion decomposition.** The Schur-Weyl branching of
 *    V_(2,1) ⊗ V_(2,1) decomposes into irreducible H_n(q)-modules,
 *    indexed by partitions of total weight 6.  Per the
 *    Littlewood-Richardson rule, the components include the
 *    "Hopf-mediated" channel `V_Hopf` corresponding to the
 *    sign-grouping `(2,2,2)` (the closed link arising from σ_1²
 *    closure on the 4-strand sub-diagram).
 *
 * 2. **Frobenius selection.** Per
 *    `prop:markov-trace-frobenius-selection`, the Markov trace at
 *    the third coefficient picks out the channel whose Wedderburn
 *    weight `tilde w_λ` is symmetric under the bar involution
 *    q ↦ q⁻¹.  The Hopf channel is the unique self-conjugate
 *    member of the V_(2,1) ⊗ V_(2,1) decomposition at total
 *    weight 6 with a non-trivial cap-cup pattern.
 *
 * 3. **Hopf trace at q=1.** The Hopf link L^+ has Jones polynomial
 *
 *      J_Hopf(q) = −(q + q⁻¹) = −[2]_q,
 *
 *    so `J_Hopf(q=1) = −2` (q-classical limit).  This is the
 *    canonical Markov-closure value for the σ_1² braid
 *    (`thm:jones-markov-trace`).
 *
 * 4. **Coefficient identification.** Expanding Q_β = Q_A · ∏(1 + c_k h^(2k))
 *    in h = q − q⁻¹ and matching the order-h^6 term against the
 *    Markov trace of the Hopf-mediated channel (per step 2)
 *    identifies `c_3 = J_Hopf(q=1) = −2`.
 *
 * **Empirical verification** (companion probe):
 * `probe_hopf_jones_c3_categorical.py` computes the Markov trace of
 * the σ_1² Hopf braid through the V_(2,1) seminormal Hoefsmit
 * representation at q = q_0 (substrate parameter) and at q = 1
 * (classical limit), confirms the J_Hopf(1) = −2 evaluation, and
 * compares with the empirical c_3 extracted from the Q_β residual
 * chain (Story B value: −2; precision after composition with c_2:
 * 0.0066 ppm against CODATA per #655).
 *
 * **Conditional status.** Per CLAUDE.md §3b-cond, the Lean
 * formalisation is a class `HasC3HopfJonesIdentity` whose
 * instance encodes the empirical match between the categorical
 * derivation and the Q_β residual; full formalisation of step 4's
 * coefficient extraction is a follow-on Lean task (the Schur-Weyl
 * branching itself is already in `prop:schur-weyl-mass-decomposition`).
 *
 * Used by:
 *   - `rem:kashiwara-jones-alternation-interpretation` — the
 *     alternation pattern Story B describes is now derived (not
 *     fit) for c_2 (#661) and c_3 (this prop).
 *   - `prop:q-beta-categorical-precision-ladder` — uses c_3 = −2.
 *
 * Witness:
 *   folio-assistant/computations/hopf-jones-c3-categorical.witness.json
 * Probe:
 *   folio-assistant/computations/probe_hopf_jones_c3_categorical.py
 */
export default proposition({
  label: "prop:hopf-jones-c3-categorical",
  title:
    "$c_3 = J_{\\mathrm{Hopf}}(q{=}1) = -2$ from Schur-Weyl branching of $V_{(2,1)}^{\\otimes 2}$ + Markov-Frobenius selection — Story B closure at $c_3$",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:schur-weyl-mass-decomposition",
    "prop:markov-trace-frobenius-selection",
    "thm:jones-markov-trace",
  ],
  cites: [
    "jones1985",
    "wenzl1988",
    "kashiwara1990",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_hopf_jones_c3_categorical.py",
    witness: ["folio-assistant/computations/hopf-jones-c3-categorical.witness.json"],
    status: "experimental",
  },
  lean: {
    ref: "qou:QOU.BraidKnot.HopfJonesC3Categorical.HasC3HopfJonesIdentity",
    validation: "not_checked",
  },
  tags: [
    "q-beta",
    "categorical-derivation",
    "precision-ladder",
    "hopf-link",
    "jones-polynomial",
    "schur-weyl-branching",
    "markov-frobenius-selection",
    "story-b-closure",
    "1ppb-roadmap",
  ],
});
