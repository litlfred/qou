---
# qou-u9o1
title: 'GAP: general JM commutativity and general prod L_i = Delta^2 (adjacent case is the blocker)'
status: todo
type: task
priority: normal
created_at: 2026-08-24T22:13:51Z
updated_at: 2026-08-24T23:33:11Z
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


## 2026-08-24 second pass — the adjacent case is REDUCED, not closed

New file `HeckeJucysMurphyCommutation.lean`, sorry-free, lean-direct exit 0, axioms
clean on all five theorems.

### Proved, general in i (not instances)

    sigma_mul_jm_succ    sigma_i . L_{i+1} = h.L_{i+1} + L_i . sigma_i
    jm_succ_mul_sigma    L_{i+1} . sigma_i = h.L_{i+1} + sigma_i . L_i
    sigma_comm_add       sigma_i commutes with (L_i + L_{i+1})          <-- classical
    sigma_mul_jm_prod    sigma_i (L_i L_{i+1}) = (L_{i+1} L_i) sigma_i
    jmRaw_comm_sigma_far sigma_j L_i = L_i sigma_j  for j > i           <-- general far case

The two exchange relations are each ONE application of the Hecke relation, and they
carry the SAME h.L_{i+1} term — which is why it cancels in the SUM. That is the whole
content of `sigma_comm_add`, the classical "sigma_i commutes with symmetric functions
of the adjacent JM pair".

### Why the adjacent case did NOT fall, recorded so the next attempt does not redo it

Set u := L_i.sigma_i and v := sigma_i.L_i. The exchange relations give

    u = (sigma_i - h) L_{i+1}          v = L_{i+1} (sigma_i - h)

and then L_i L_{i+1} = u^2 while L_{i+1} L_i = v^2. So the goal becomes

    (sigma_i - h) w  =  w (sigma_i - h),   w := L_{i+1} (sigma_i - h) L_{i+1}

i.e. it reduces to ANOTHER commutation of the same shape, not to anything proved.
**The sum is reachable from these relations; the product is not.** Anyone attacking
this again should start from the hook-word form of L_i and the braid relation, not
from the exchange relations — they are exhausted.

`sigma_mul_jm_prod` has an ORDER SWAP on the right and is NOT commutation. It becomes
commutation exactly when L_i, L_{i+1} commute, i.e. it is equivalent to the open
problem, not progress past it. Do not cite it as though sigma_i commutes with the
product.

### A wrong statement the compiler caught

I first stated far-commutation as `i <= j`. That is FALSE: `jmRaw H i` is a word in
sigma_0..sigma_{i-1}, so at j = i the generator is ADJACENT to the outermost letter
and `far` does not apply. The correct hypothesis is `i < j` strictly, and the excluded
boundary j = i is precisely the open adjacent case. Worth recording because the wrong
version looks more general and would have been quoted as covering the adjacent case.

### Status of the general-lambda derivation — UNCHANGED

Still conditional. Two things remain, and neither is closed by this file:

1. adjacent commutativity (above), hence general `prod L_i = Delta^2` (still n=2,3 only);
2. the SPECTRAL half — that L_i acts on the seminormal basis by q^{2.content}.

(2) is the larger and is what actually discharges `JucysMurphySpectrum`. Nothing in
this pass touches it.
