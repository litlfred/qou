---
# qou-i9gk
title: 'ROAST of Steps 27-28: is the trace-blind sector physical, and is E_2/E_1 a vertex or only a propagator?'
status: todo
type: task
created_at: 2026-09-01T04:19:34Z
updated_at: 2026-09-01T04:19:34Z
---

Two self-identified holes in this session's Steps 27-28 (qou-cds1), either of which would deflate the headline. Both are checkable and neither has been checked.

## Hole 1 — the blind sector may be PHYSICALLY EMPTY, not merely unobserved

Step 27 measured that convention D's Ocneanu weights vanish on the seven
partitions of 6 with more than two rows (|omega| < 2e-16, confirmed by
132 = C_6 = dim TL_6 against 720 = 6!), and that the binding character is LARGE
there (chi_(3,2,1) = -9.598, the biggest of any block). It read that as
'588 of 720 dimensions carry information the observable cannot see'.

But qou-fvzm's Schur-Weyl ROW CAP says dim V_lambda = 0 whenever l(lambda) > N,
and the framework has N = 2. If the physical Hilbert space is the Schur-Weyl
image, those blocks DO NOT EXIST physically -- and a nonzero Hecke character in
a block with no Schur-Weyl image is not hidden information, it is no information.

**The two vanishings are DIFFERENT and Step 27 glossed the difference.**
qou-e9le is about chi^lambda = 0 (the characters themselves, by the cap);
Step 27 is about omega_lambda = 0 (the trace WEIGHTS, by the TL quotient). In
Step 27's own numbers the >2-row characters are emphatically NOT zero. Either

  (a) the two coincide, and Step 27 re-measured a known cap -- in which case
      qou-e9le already owns it and the 'first small eigenphases in the arc'
      (0.0252506 in (3,2,1), 0.0195531 in (2,2,1,1)) live in blocks with no
      physical states; or
  (b) they are genuinely distinct, and the blind sector is real -- in which case
      Step 27 stands and the relation to the row cap needs stating properly.

Deciding this is a read of the Schur-Weyl functor at N = 2 against the H_6(q)
block decomposition, not a new computation. It gates everything Step 27 claims.

## Hole 2 — E_2/E_1 may be a PROPAGATOR, not a VERTEX

Step 28 derived the per-bond ratio E_2/E_1 from the transfer step's
Cayley-Hamilton spectrum (-1/q^2 for p-p, -q^2 for n-n, exactly -1 for the
averaged p-n) and offered it as the falloff rate for an ALL-PAIRS coupling,
removing the three-free-parameter objection that stopped Step 27.

That identification is unargued. E_2/E_1 is the rate at which a perturbation
already decays ALONG THE EXISTING CHAIN -- a propagator. A coupling strength for
a new, direct i-j bond is a vertex. Using one as the other conflates them.

Three symptoms that it may be wrong:

  * |r_nn| = q^2 = 1.232 > 1 at q_0. A 'decay rate' above 1 means correlations
    GROW along an n-n chain. Step 28 reported q^-2 / 1 / q^+2 as 'a ladder'
    without confronting that only ONE of the three decays.
  * the per-step ratio is not obviously the right normalisation; the standard
    transfer-matrix falloff is lambda_2/lambda_1 of the FULL matrix, not of one
    step read in isolation.
  * the bar-parity 'match' to the interaction-sector taxonomy is partly
    TAUTOLOGICAL: the p-p and n-n templates are d = 0 and d = -h, i.e. sigma and
    sigma^-1, which are bar-images of each other BY DEFINITION -- so of course
    their rates exchange under q -> 1/q. Step 28 presented that as the taxonomy
    being reproduced. The p-n/EM half (tanh(ln q_0) = 0.103963710 matching the
    taxonomy's EM odd-to-even ratio to 7e-5) is less circular but may be two
    instances of the same triviality: tanh(ln q) = h/(q+1/q) is just 'odd part
    over even part', which ANY bar decomposition produces.

## Why this is a bean and not a footnote

qou-p0be ('all-pairs nonlocal probe -- geometric-decay couplings') is already
completed with an empty body, so somebody has been here; and the natural next
move -- building the all-pairs word on Step 28's rates -- would rest on both
holes at once. Better to spend one session deflating or confirming than to build
on it.

Scope-(a). No convention adjudicated, nothing wired, no c_k value asserted.

---

## Hole 2 is SETTLED by `main` — and against Step 28 (2026-09-01, same day)

`qou-brng` landed `computations/probes/spectral_gap_bond_decay_probe.py` on
`main` while this bean was being written. It derives the same object and gets
the answer right: the rate is `|λ₂/λ₁|` with `λ₁` the larger-magnitude
eigenvalue, and since `σ⁻¹` carries `σ`'s spectrum up to sign, **p–p and n–n are
both exactly `1/q²`** (asserted to 45 digits); **p–n is long-range**.

Step 28 used the fixed `(q, −1/q)` order and reported `q²` for n–n. The symptom
this bean flagged — *"a decay rate above 1 means correlations GROW along an n–n
chain"* — was the error, and the resolution is the standard normalisation.

**Consequence for Step 28:** the "one degree of freedom" relation and the
bar-exchange sector split are **withdrawn** (corrected in the probe, the Lean
file, the audit and `qou-cds1`). The derived-closed-form result and the
p–n/EM `tanh(ln q)·δ` result survive.

**Hole 2 is therefore closed** — the answer is "propagator, and even as a
propagator it was mis-normalised". What remains open from this bean:

- [ ] **Hole 1** — is the trace-blind >2-row sector physical, or does the
      Schur–Weyl row cap (`dim V_λ = 0` for `ℓ(λ) > N = 2`) empty it? Untouched
      by `qou-brng`. Still gates everything Step 27 claims, including the two
      small eigenphases (`0.0252506`, `0.0195531`) that are the first in the arc
      below the required phase.
- [ ] **residual on the surviving EM link** — `tanh(ln q) = h/(q+1/q)` is just
      "odd part over even part", which any bar decomposition produces. Decide
      whether the match to the taxonomy's EM ratio is a link or two instances of
      one triviality. Unlike the withdrawn sector claim this is at least a
      numerical coincidence that has to be explained away.

**Also settled against the recommendation:** `qou-brng`'s
`allpairs_distance_decay_probe.py` already tests the owner's all-pairs proposal
and returns a negative — the strand-routing cost is exactly `z²` per unit
separation but cannot be the binding's distance decay, and the decay AME wants
runs `r* = 0.709..0.827`, falling with `A` rather than constant. So "build the
all-pairs word" was duplicated work twice over, and the honest next item is
neither of this session's candidates.
