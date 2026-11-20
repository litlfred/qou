---
# qou-i9gk
title: 'ROAST of Steps 27-28: is the trace-blind sector physical, and is E_2/E_1 a vertex or only a propagator?'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-01T04:19:34Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-q4oa
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

---

## Hole 1 SETTLED (2026-09-01) — the blind sector is unphysical, full stop

[`qbeta_blind_sector_is_the_tl_kernel_probe.py`](../computations/qbeta/qbeta_blind_sector_is_the_tl_kernel_probe.py)
(4/4).

**The two vanishings are one statement.** `ω_λ = 0 ⟺ ℓ(λ) > 2` exactly at
`n = 3..8`, and `∑d²` over the `≤2`-row blocks is `Catalan(n)` at every `n`. The
`>2`-row blocks span the **kernel** of `H_n(q) → TL_n(q) = End_{U_q(sl₂)}(V^{⊗n})`
— the Schur–Weyl row cap, structurally. Not "unobserved": **zero on the physical
space at `N = 2`**.

**And Step 27's reading is self-inconsistent.** `FibreCategoricalTraceForcesJones`
shows convention D is forced by the open premise `MassTraceIsFibreCategorical`
(bean `qou-n1dj`) — the same premise that empties the blind sector. Measuring in
D and reading D's zeros as hidden information asserts the premise and its
negation at once. So hole 1 does **not** resolve to yes/no: it resolves to
*"Step 27's headline is inconsistent with itself."* And — **corrected on a second
pass the same day** — not merely conditional either:

**And the premise is NOT open.** `qou-n1dj` is **resolved** — its status is
`todo` only because closing a bean is a human action (AGENTS.md §4a), and
`qou-cds1` itself already recorded this at line 4285. Verified here:
`lem:feynman-eigenbasis-decomposition` **defines** the mass channel as
`V^{⊗n} ≅ ⊕_{λ ⊢ n, ℓ(λ) ≤ 2} V_λ ⊗ S_λ` — the row cap is **in the index set** —
and `FibreDimensionForcesTL.lean` (sorry-free) proves `z·[N]_q = q^N`, so a
two-dimensional fibre leaves **no residual trace freedom**.
`MassTraceIsFibreCategorical` is a Lean *class* only because no quantum
Schur–Weyl development exists in this tree; its content is already asserted by
the mass chapter. **So the blind sector is unphysical FULL STOP, and Step 27's
headline is false rather than conditional.**

**Bonus, and a cleaner kill than the wall argument.** `N_min(λ) = ℓ(λ)`, so
`0.0252506` (in `(3,2,1)`) needs `N ≥ 3` and `0.0195531` (in `(2,2,1,1)`) needs
`N ≥ 4` — **the sum coincidence requires `N ≥ 4`**, unmotivated anywhere.

- [x] Hole 1 — settled as above.
- [x] Hole 2 — settled against Step 28 by `qou-brng`.
- [ ] residual: is the `tanh(ln q)` / EM match a link or two instances of "odd
      part over even part"? Still the only live item on this bean.

---

## Residual SETTLED (2026-09-01) — the tanh/EM match is formal

[`qbeta_tanh_em_match_is_formal_probe.py`](../computations/qbeta/qbeta_tanh_em_match_is_formal_probe.py)
(4/4). It is a triviality, three ways:

1. **Census.** 5 of 12 unrelated corpus `q`-quantities have odd-to-even ratio
   exactly `tanh(ln q)` — and **`q` alone is one of them**. Every quantum integer
   is bar-even, so `[9]_q[10]_q` divides out of the taxonomy's coupling entirely:
   the matched number is a property of the bare prefactor and the electromagnetic
   content contributes **zero** to it.
2. **Lemma.** `X = q·B` with `B` bar-even gives the ratio identically for *any*
   `B`. And `tanh(ln q)` **is** `h/(q+1/q)`, the ratio of the most basic bar-odd
   and bar-even quantities — exactly how it arises in the p–n departure
   (numerator `h` from the offset `d = −h(½−δ/4)`, denominator `q+1/q` from the
   averaged eigenvalue). The two "matching" expressions are one expression
   written twice, not two computations that agreed.
3. **Discriminator.** The taxonomy documents a **bare** ratio `0.10396` and a
   Chern–Simons-**dressed** `0.10356` — the physical coupling. They differ by
   `3.9e-3` relative, **`54×`** Step 28's `7.2e-5` residual, so the measurement
   distinguishes them and lands on the **bare**, algebraic form. A physical EM
   link should have shown the dressed value.

**Kept:** the p–n departure is exactly `tanh(ln q)·δ + O(δ²)`, a closed form,
with `δ` the derived flavour split at CAL-3's order `h³`.
**Withdrawn:** that it links the p–n bond to the EM sector. It links it to the
bar involution, which every quantity in the algebra is linked to.

- [x] Hole 1 — the blind sector is the TL kernel; unphysical at `N = 2` FULL STOP (`qou-n1dj` is resolved, not open — corrected second pass).
- [x] Hole 2 — settled against Step 28 by `qou-brng`.
- [x] Residual — the tanh/EM match is formal.

## Summary of Changes

All three items closed, all three **against** this session's Steps 27–28.

| claim | status |
|---|---|
| Step 27: 588 of 720 dimensions carry hidden information | **withdrawn** — TL kernel, no states at `N=2`; reading contradicts convention D |
| Step 27: the 0.13 % sum coincidence | **killed structurally** — requires `N ≥ 4` |
| Step 28: n–n bond rate `−q²` | **wrong** — `1/q²`; `qou-brng` had it right |
| Step 28: one degree of freedom (`r_pp·r_nn = r_pn²`) | **withdrawn** — product is `1/q⁴` |
| Step 28: bar-parity → strong/weak sector split | **withdrawn** — vacuous, and partly circular |
| Step 28: p–n departure ↔ EM coupling | **withdrawn** — formal, three ways |

**What survives from both steps.** The construction `Δ_bind = P·(I−1)·N` is
genuine, validated to `5.4e-15` against the corpus's own character routine, and
genuinely `H₆`-valued so Step 24's branching argument does not reach it. The bond
rates are derived closed forms (`1/q²` like-nucleon, p–n long-range) — though
`qou-brng` derived them independently and correctly first. The chain-vs-all-pairs
structural finding (deficit `(A−1)(A−2)/2`, zero at `A=2`, `22.54 %` ordering
spread at `A=3`) stands. And Step 27's blind-sector characters are a measurement
of **what an `N = 3` extension would carry**, which is what `qou-fvzm` says the
super-pairwise binding term requires.


---

## 🛑 Third correction (2026-09-01) — the `N = 3` reading is withdrawn too

**🛑 THIRD CORRECTION, same day — the last positive goes too.** The reading
*"(3,2,1) is an ℓ = 3 block carrying the largest binding character, so this
measures what an `N = 3` extension would carry"* cited **`qou-fvzm`'s REOPENED
paragraph**. That bean is **`status: completed`**, and its line 18 closes
exactly that paragraph: *"my reopened form … is closed — the route is
**UNAVAILABLE**, not merely hard"*, and *"**THE MISSING ADDITIVE TERM IS NOT A
HECKE-TRACE OBJECT AT ALL**."* Moving to `N = 3` re-weights channels the mass
pipeline already evaluates (`y_(2,1)/y_(3) = q[2]_q[N−1]_q/[N+2]_q` differs at
every `q`), so it is a **regression risk, not an opening**. The surviving
candidates that bean names are the ones that were never trace objects — the
extended-Bloch route (`qou-985x`) and the atomic-braid→nucleus map (`qou-imcd`).
>
**So Steps 27–28 retain no positive claim about the blind sector at all.** What
stands from that arc is the construction `Δ_bind = P·(I−1)·N` (validated to
`5.4·10⁻¹⁵`, genuinely `H₆`-valued) and the chain-vs-all-pairs structural
finding.

Found by a dispatched audit of the Standard-Model work against the full tower;
verified against `qou-fvzm` directly rather than taken on the agent's word.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8457)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PairingSpaceActionRetypeRuledOddProjectionLetterInvolutionPullbackQuotientKernelMultiplierSlope.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_h0ou_hlx8_hlxp_i9gk_slpd_probe.witness.json` (`Commit 1` = `6615e05829d98e7dc8f3151a6136022620b0fa75`, `HEAD` = `87f824354a46b08a4af8436ed872967b2f3dfc59`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8457, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-01: "fix(qou-i9gk): the tanh(ln q) / EM match is formal — Step 28's last positive downgraded; bean closed"). The work may be partly or fully done. Read the bean before you close it.
