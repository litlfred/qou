---
# qou-1ngr
title: Gluon stabiliser feasible set is restricted to L± without stating why
status: completed
type: task
priority: normal
created_at: 2026-08-24T19:08:20Z
updated_at: 2026-08-24T21:05:59Z
---

Found while closing the antiquark channel (rem:antiquark-channel-ledger, 2026-08-24). Smaller than that one, and the same shape: a restriction that is correct but unjustified in the text.

`categorical-proton-properties.md:10` — "The integer LP dual enumerates all feasible gluon combinations and selects the configuration minimizing |tr_M|." The feasible set is never defined.

It is in fact well-defined. Line 4 of the same block says "The Hopf link terms L± manifest the gluon field", so the candidates are the L+ = σ₀σ₁ and L− = σ₁σ₀ elements of the six-word Gröbner–Shirshov basis of H_3(q) — not arbitrary knots. Enumeration over combinations of those IS exhaustive.

What is missing is WHY the stabiliser may not be e⁻ = σ₀σ₁σ₀, the trefoil, which is equally a basis word and equally Vol = 0. The answer looks like a conservation law rather than a choice: e⁻ is the lepton channel, so admitting it as a stabiliser would change lepton number. Note that the same block says the Hopf gluon "redistributes normal-form weight from σ₁ into the trefoil channel" — e⁻ is the OUTPUT of stabilisation, so admitting it as an INPUT would also double-count.

Worth writing down because it is load-bearing for the mass split. The proton takes one Hopf link (2 gluon crossings), the neutron two (4 crossings), and that difference is what makes the neutron heavier — which feeds Q_β = m_n − m_p − m_e, i.e. CAL-2. If the feasible set were wrong the mass split would be wrong.

Task: state the conservation argument in the proton/neutron blocks, or in a remark interpreting def:derived-atom step 4, and say explicitly that the enumeration ranges over L± combinations. Check the neutron block for the same omission.


---

**Closed 2026-08-24, branch `claude/mt7r-archimedean-eval-2026-08-24`.**

**The premise was wrong, and that is the finding.** The feasible set is not restricted to L±, so there is no exclusion to justify. Both producers range wider:

  computations/universal-ilp.py                  {sigma_0, sigma_1, sigma_0^-1, sigma_1^-1}, words up to 6 crossings
  computations/_deprecated/integer-lp-gluon.py   {sigma_0, sigma_1, L_+, L_-}, words up to length 3

Either alphabet composes to all six GS basis words. e- = sigma_0 sigma_1 sigma_0 is a three-letter braid word and sits INSIDE the enumeration — reached as sigma_0 . L_- or as L_+ . sigma_0. It is admissible (applied to either bare nucleon the state stays Frobenius-positive) and it simply loses. Re-running the retired producer reproduces its witness exactly (proton 40 survivors, optimum sigma_0->sigma_0 |tr_M| = 0.0274; neutron 26, optimum L_+->L_- 0.1120) and finds e- among the survivors of both: proton rank 35/40 |tr_M| = 1.173, neutron rank 21/26 |tr_M| = 1.105. It also loses on crossings — it costs 3, and both nucleons have admissible stabilisers at 1 or 2.

Incidentally, the 84 of rem:ilp-solution-count-unwrap is 4 + 4^2 + 4^3, the ENUMERATED count over that 4-letter alphabet, not the feasible count (40 / 26). That block calls it feasible; it should say candidate.

**Neither proposed reason holds.**

- Lepton number: refuted by the framework's own definition. def:lepton-number-categorical counts SKEIN SMOOTHINGS, and rem:lepton-number-categorical-properties says the Hecke algebra contains no mechanism to change L — violation "requires a process that changes crossing type without passing through the Skein relation". Gluon stabilisation is Hecke multiplication + GS reduction; it smooths nothing, so Delta L = 0 for every candidate including e-. rem:nucleon-from-photons-summary agrees by construction: its conservation table has NO ROW for step 4, and it assigns L = 0 to a nucleon whose NF is dominated by e- ~ +1.02 — a coefficient the same block calls the beta-decay channel. An e- weight in a Hecke NF is an amplitude, not a lepton. The argument would forbid the OUTPUT the proton block already asserts.
- Double counting: the observation is true (the Hopf gluon does move weight into the trefoil channel, so e- is the output) but it is a consequence of the selection, not a constraint on the search. An e- input is a worse candidate, not a double count.

Also worth knowing: the volume argument that closed the antiquark channel does not transfer. All five non-identity basis words are torus-type with Vol = 0.

**Written up** as rem:gluon-stabiliser-ledger (new .md + .ts, interprets def:derived-atom, registered in sec:nucleon-derivation), plus a sentence in categorical-proton-properties.md and a paragraph in categorical-neutron-properties.md. The neutron block had the same omission; both now name the feasible set.

**Two larger things found and NOT fixed here** — spun out:
- qou-jqjx: the retired producer used tr_M(e-) = z^3; on the corrected h z^2 + z the bare 9-crossing nucleon is ALREADY Frobenius-positive (proton +0.4196, neutron +0.2937 vs the quoted -0.006 / -0.132), so "the gluon is strictly required by the LP dual" may not survive the convention change.
- qou-v5fp: four statements of the proton gluon, three answers; min-cr and min-|tr_M| disagree, and the 2-vs-4 asymmetry feeding CAL-2 exists only under min-|tr_M|. universal-ilp.witness.json is self-certifying and records 1 crossing.
- qou-bzy0: rem:antiquark-channel-ledger and rem:pion-mass-hyperbolic-threshold are unregistered in the chapter manifest, so their labels do not resolve and neither renders. Linking the antiquark ledger from the new block was the one thing that broke validate; the link was dropped.

Gate: bun run scripts/run-validate.ts — Valid, 26 issues, 0 errors, issue list byte-identical to baseline. No Lean touched.
