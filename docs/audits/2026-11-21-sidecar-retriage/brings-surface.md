# Sidecar re-triage, 2026-11-21: brings-surface

Scope: every stale `proof-narrative-lean-equiv` verdict (statement vs Lean) and
`da-non-sequitur` verdict (proof vs statement) in this chapter, 18 in all. A
verdict is stale when the block's md, ts or Lean changed after it was written.
The owner chose triage on 2026-11-21: read the diff of every stale block,
re-stamp where only wording changed, and review in full where the mathematics
or the Lean changed. Reviewer id `agent:sidecar-review-2026-11-21`.

## Re-stamped (17)

The diff since the 2026-11-15 review is wording only, so the earlier result is
kept. Each new verdict names the diff and repeats the earlier evidence.

- Voice edits ("We substitute" to "Substitute", and so on): color-elliptic,
  x5-bring-weight-identification, chebyshev-degree-genus-proof,
  torus-embeddable-complete-proof, bring-cone-reeb-quaternionic-twist-proof,
  brings-is-qou-proof, genus-from-hecke-completeness-proof.
- Symbol rename `\chi(A)` to `\chi_{\mathrm{eu}}(M_0)`: genus-maximal-descent,
  descartes-elliptic-curve, embeddability-closure, descartes. The Lean is
  unchanged, and the identification the symbol names is still a hypothesis.
  descartes also gained "at a fixed value of the substrate parameter q", which
  does not touch either earlier objection (automorphisms of Bring's curve
  break uniqueness; Riemann-Hurwitz forces degree 1, which breaks existence).
- Label references replaced by titles, Lean names removed from prose:
  jet-sw-tau-decomposition and its proof, sw-classical-jet-exactness and its
  proof, sw-period-residue-sum and its proof. sw-classical-jet-exactness-proof
  added the word "(positive)", but the binding period is still checked only at
  q = 1, so its warn stands.

## Full review (1)

**brings-smoothness-resolution: fail to warn (major).** The Lean was rewritten.

- Item 1, smoothness, is now genuinely proved and matches the md. Every nonzero
  point of the cone has a nonzero 3x3 Jacobian minor. This follows from the
  Vandermonde form of the minor and the fact that p1 = p2 = 0 with only two
  distinct coordinate values forces x = 0. Checked by hand.
- Item 2, intrinsic resolution, is not encoded. The Lean states the identity
  x_i^2 + x_j^2 - 2((x_i+x_j)/2)^2 = (x_i-x_j)^2/2, which holds for any two
  numbers and never mentions z, the colour projection or a branch point.
- The Lean's third claim (zeta*w is not w) is trivial, and the md no longer has
  a third item.

## Never reviewed

None in this chapter. After this commit, all 20 Lean-backed statements and all
23 proof blocks have fresh verdicts.

## Check against the current owner rulings

Every block was checked against `docs/coordination/owner-rulings.md`: the photon
1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹ with no virtual photons, the electron as σ₀σ₁σ₀
with Hopf-link closure, and the two-term Lagrangian trace. None of these 18
blocks uses the photon form, an electron braid word or the Lagrangian trace.
jet-sw-tau-decomposition says "electron period", but only as a name for the
n = 0 term. So no re-stamp here keeps a verdict that rests on a superseded
definition. Every later chapter gets the same check, and a block built on an
old form is reviewed in full rather than re-stamped.
