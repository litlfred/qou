# Mass and binding accuracy: what is actually closeable

**Date:** 2026-08-18
**Bean:** `qou-jh26`
**Branch:** `claude/ribbon-downstream-mass-2026-08-17` (PR #5262)
**Probe:** [`computations/accuracy/l2_scoreable_count_probe.py`](../../computations/accuracy/l2_scoreable_count_probe.py)

Asked: *"a systematic analysis of everything downstream to see if the new axioms
can help close derivation gaps — in particular mass and binding accuracy."*

Answer, up front: **the new ribbon/balanced axioms do not touch mass accuracy**,
and the reason is worth more than the answer. Of the four observables that miss
their L2 target, three share one root cause whose **stated closure path is
refuted by results already in the corpus**, and the fourth is structural. Along
the way the headline count itself turns out to be wrong.

---

## 1. The headline number is wrong: 1 of 5, not 2 of 7

`per-observable-100x-status.witness.json` reports `beats_100x_count = 2`, and
AGENTS.md carries it as *"2/7 met (m_e, m_K/m_π)"*. The dashboard separates
calibration inputs from predictions **for one anchor but not the other**:

| obs | role | `err_ppb` | scored? |
|---|---|---|---|
| `m_p` | CAL-2 numerical anchor | 0.002852 | **not scored** — `beats_100x = None` |
| `m_e` | CAL-1 anchor | **0** | scored **`True`** |

`m_p`'s exclusion note is exactly right:

> *"NOT SCORED. `q₀` is pinned from `m_p/m_e`, so this 'prediction' is
> `m_e × (m_p/m_e)` re-evaluated through the identity that pinned it — the
> framework content cancels and the residual is CODATA's own rounding, not
> accuracy."*

`m_e`'s note is *"calibration anchor — err defined as 0"*. **That is the same
argument, only stronger.** `m_e` is the CAL-1 input that fixes the MeV unit, so
its ratio to itself is 1 by construction; its error is not *measured* and found
small, it is *defined* zero. `m_p` at least carries a nonzero round-trip
residual. If the round-trip disqualifies `m_p`, a definitional zero disqualifies
`m_e` a fortiori.

This is the calibration-tautology error class AGENTS.md §"q₀ anchor convention"
rule 1 already names for `m_μ` (*"an `m_μ` value ≈ CODATA computed at the muon
`q₀` is the CAL-2 calibration tautology, not an accuracy win"*). The same rule
applies at CAL-1 and has not been.

Recounting inputs vs predictions:

```
calibration INPUTS      : m_p, m_e
scoreable PREDICTIONS   : m_mu, Q_beta, m_n, Delta_pn, m_K/m_pi
of those, meet 100x     : m_K/m_pi
HONEST SCOREABLE RATIO  : 1/5
```

**One genuine prediction meets the L2 100× target: `m_K/m_π`.** It is also the
only one of the five that is a *ratio* rather than an `m_e`-scaled absolute — a
point the 2026-08-11 absolute-mass excision already made on independent grounds.

This does not change any physics. It changes what the framework may claim.

## 2. The four failures are two root classes, not four

| obs | miss | class |
|---|---:|---|
| `Q_β` | 164.0× | **Q_β chain** |
| `m_n` | 176.7× | Q_β chain (`m_p + Q_β + m_e`) |
| `Δ_pn` | 151.7× | Q_β chain (`≈ Q_β + m_e`) |
| `m_μ` | 970.2× | μ–p substrate tension (independent) |

The Q_β trio's miss factors cluster in a 150–180× band because they are one
number propagated three ways —
[`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)
established this and it stands.

## 3. The Q_β chain's stated closure path is refuted

That audit's closure path reads:

> **Option E** — Kashiwara crystal extension of the τ_M derivation to `k ≥ 3`
> with canonical (non-fitted) rung-selection rule, displacing the current `k=2`
> truncation.

Two results that **postdate it** make this unavailable, and neither is a matter
of difficulty — both are settled.

### 3a. There is nothing at `k ≥ 3` to extend to

[`QOU/QBeta/GreedyLadderTermination.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/GreedyLadderTermination.lean)
is sorry-free and proves that the canonical producer `qbeta_ck_cache.py` extracts
**one** rung by inverting the target, after which the residual is *identically*
zero:

- `greedy_rung_exact` — the extracted coefficient lands on `Qtarget` exactly, for
  every nonzero `Qprev` and `x`.
- `greedy_next_residual_zero` — so the producer's `EPS_RESIDUAL` guard fires at
  the very next `k`, *"not because it converged but because it was solved."*
- `greedy_later_rungs_vanish` — *"`c_4 … c_7` carry no information; they are not
  small, they are `0`."*

So `k=2` is **not a truncation that further work can push deeper.** The ladder
terminates because it was solved, and the rungs beyond are zero as a matter of
algebra, not of precision.

### 3b. What content does exist beyond `k=2` is circular for this purpose

The one extracted rung is `c₃`, and per AGENTS.md it is
`c₃ = (Q_β^exp/Q_N2 − 1)/u³` — **extracted from the experimental `Q_β`**. Using
it to predict `Q_β` is circular. The dashboard is already correct to wire the
deepest *non-fitted* rung `Q_N2`.

The same file makes the general point in one theorem, `exists_rung_hitting_target`:

> *"'the ladder reproduces CODATA' is a property of having one free coefficient,
> carrying no information about the model that coefficient multiplies."*

**Consequence.** The 164× is not a truncation artifact awaiting a longer ladder.
It is the **floor of the ladder's non-circular content**, and `m_n` and `Δ_pn`
inherit it. Closing the Q_β chain requires a *different* derivation of `Q_β`, not
a deeper `c_k`.

### 3c. And the whole ladder is convention-C-frame

Per the 2026-08-15 owner ruling, convention **D** (`z = q³/(q²+1)`) is canonical
and **C** (`z = √q/(q+1)`) is excised — while every `c_k` result was derived in
C. This is not a substitution:
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes the C-frame ladder
and the mass channel's three-row forcing **mutually exclusive**. So the ladder
must be *re-derived* under D (`qou-cds1`), and until it is, every `c_k`
conclusion is C-conditional — including the 164× floor above.

## 4. `m_μ` is structural, not a tuning gap

`m_μ` misses by 970× (211 ppb against a 0.218 ppb target). This is the μ–p
substrate tension: a ~11.5 ppb theory residual that must land *somewhere*. Pinning
`q₀` on the proton (0.06 ppb) puts it on the muon; pinning on the muon puts
~4000σ on the proton. Re-pinning **moves** the residual, it does not shrink it.
Closing this means reducing the residual itself, which is a statement about the
theory, not about the anchor choice. It is also **not** closeable by deriving
`q₀` — that route is permanently gated (owner ruling 2026-08-02).

## 5. Binding: the `Δ_λ` position, stated precisely

Frequently compressed into "Δ_λ is open", which is wrong in both directions:

- **The per-partition VALUE is proved**, sorry-free and general-`n`:
  `Δ_λ = (−1)^{n(λ)}·dim V_λ` (signed Springer dimension) —
  `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`.
- **What is open is the many-body binding MAGNITUDE**, and the six failed
  ansätze failed for a *structural* reason, not for want of a seventh: they tried
  to force an extensive quantity into a per-block (intensive) weight. The pairwise
  cap `ρ_A ≤ C(A,2)` is proved (`QOU.MassTheory.exchangeDet_pow_two_le_four`).
  The missing object is a **separate additive extensive term**, so a seventh
  per-block ansatz is not merely forbidden by policy — it is excluded by shape.

## 6. Do the new ribbon/balanced axioms help?

**No, and the chain says why.** The twist reaches the mass chain through a
*correctness* dependency, not a numerical one:

```
twist θ → θ_{X∨} = (θ_X)∨ → sphericality on all of C → qDim_conj → dim_q(λ)
consistency → G⁻¹ = δ·[n]_q!/(dim_q(λ)·dim(λ)) → the mass chain
```

`qDim_conj` is an **unproved input** the Gram-inverse derivation currently leans
on. Supplying it removes an assumption; it does not change any computed value,
because the derivation already *assumes* what it would prove. Every number in §1
is unmoved: `beats_100x_count = 2` (`1/5` scoreable) before and after.

*"The twist closes a proof gap in the mass chain's derivation"* is supported.
*"The twist improves mass accuracy"* is **not**, and the two must not be traded
for one another.

## 7. What is actually closeable, ranked

1. **The `1/5` recount** — a documentation fix, closeable now. Blocked by
   nothing. (§1)
2. **`c_k` re-derivation under convention D** (`qou-cds1`) — required before any
   `c_k` statement can be quoted unconditionally. Not a `z`-swap; a re-derivation.
   Until it lands, the 164× floor is itself C-conditional. (§3c)
3. **A non-ladder derivation of `Q_β`** — the only route that can move the Q_β
   trio, since the ladder's non-circular content is exhausted. Large, open. (§3)
4. **The `Δ_λ` extensive term** — open, in scope for all agents since the
   2026-07-13 reversal, and constrained to a *separate additive* object rather
   than a per-block weight. (§5)
5. **The μ–p residual** — structural; not addressable by anchor choice, and the
   `q₀`-derivation route is permanently gated. (§4)

## What this audit did NOT do

- It ran **no new physics compute**. Every number is read from the committed
  dashboard or from sorry-free Lean already in the corpus. The probe recounts;
  it does not recompute.
- It did **not** re-derive the `c_k` ladder under convention D, and therefore
  cannot say what the 164× floor becomes under D.
- It did **not** verify the `Δ_λ` magnitude claim beyond citing the proved
  value-lemma and the proved pairwise cap.
