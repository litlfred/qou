# Sidecar re-triage: appendix-surreals chapter (2026-11-21)

Umbrella issue #8766. There were 5 stale proofs, plus 1 proof that had never had a hashed review.

## Re-stamped (wording only, earlier verdict kept)

- surreal-rate-calculus (warn)
- b1-soft-sharpness-theorem (fail)
- depth-2-identification-bloch-suslin (fail)
- hoefsmit-is-surreal-construction (fail)
- b1-figure-8-row-theorem (fail)

All of these were label-to-title or Lean-wording changes only.

## First real review

**collatz-no-cycles proof: pass.** I checked by hand:
- The affine iteration and the claim B > 0 rule out every balanced cycle at every real q > 0.
- Coprimality via [3] − q[2] = 1 rules out A = 1 in ℤ[q^{±1}].
- The plastic-number example is correct.

One minor typo: there is a stray exponent in b_i.

Ruling check: no block in this chapter uses the photon form or the electron strand.
