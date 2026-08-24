---
# qou-u9o1
title: 'GAP: general JM commutativity and general prod L_i = Delta^2 (adjacent case is the blocker)'
status: todo
type: task
priority: normal
created_at: 2026-08-24T22:13:51Z
updated_at: 2026-08-24T22:14:33Z
---

## Where this stands after PR (HeckeJucysMurphyElements.lean)

The `JucysMurphySpectrum` assumption in `KeystoneJucysMurphyTwist.lean` bundles TWO
independent facts. They are now separated, and only one has a demonstrated route.

### STRUCTURAL half — route demonstrated, not finished

`HeckeGenerators` is the type-A presentation (braid + Hecke relations). Assuming it
is "let A be a Hecke algebra" — a definition, not a world-claim — so it is not the
axiomatization the anti-laundering rule targets.

PROVED from that presentation:

- `jmRaw_closed_two`  L_2 = (q - q^-1) sigma_0 + 1     [Hecke relation]
- `jmRaw_prod_two`    L_1 L_2 = Delta^2 at n=2
- `jmRaw_prod_three`  L_1 L_2 L_3 = Delta^2 at n=3     [BRAID RELATION ONLY]
- `jm_prod_three`     the q-normalized form: q^-3 . Delta^2, and 3 = c([3])
- `sigma_comm_jmRaw_one`  far-commutation of sigma_j past L_2 for j >= 2

The n=3 proof is one braid application on the middle three letters of
`sigma_0 sigma_0 sigma_1 sigma_0 sigma_0 sigma_1`. Worth recording because I nearly
got the CONVENTION wrong: `prod L_i = Delta^2` holds ON THE NOSE only for the
UNNORMALIZED recursion `L_{i+1} = sigma_i L_i sigma_i`. With the q^-1 convention the
product picks up `q^{-n(n-1)/2}` — which is `c([n])`, the same triangular number the
twist arc uses. Do not quote one convention's identity under the other's name.

### OPEN — this bean

1. **General `prod_{i<n} L_i = Delta^2`.** n=2 and n=3 only. The induction step needs
   `L_i` to commute past the newly-introduced generator; n=3 is the first genuine
   instance of that, not a corollary of a finished argument.
2. **General commutativity `L_i L_j = L_j L_i`.** The FAR case is easy
   (`sigma_comm_jmRaw_one` is its first instance). The ADJACENT case is the classical
   hard one and is the actual blocker.

### OPEN — separate, larger, NOT this bean

3. **The SPECTRAL half**: that `L_i` acts on the seminormal basis with eigenvalue
   `q^{2.content}`. Untouched. Needs Young's seminormal form, which the corpus does not
   carry and Mathlib does not have. This is the half that actually discharges
   `JucysMurphySpectrum`, and it is much larger than 1+2.

**Do not read the n=3 result as "prod L_i = Delta^2 is proved."** It is proved at two
values of n. The honest summary is that the structural half now has a demonstrated
proof route in Lean and the spectral half does not exist yet.

Lit is available and is NOT the blocker: `library/hecke-alg`, plus
`arxiv-math-0411647v2` and `arxiv-2607.03827v1`. The mathematics is standard; the gap
is formalization effort.
