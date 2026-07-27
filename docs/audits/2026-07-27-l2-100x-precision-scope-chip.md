# L2 100× precision path — status survey + one honest micro-step (2026-07-27)

**Scope.** A single-session *chip* at the 1ppq / L2-100× precision path.
This is **not** an attempt to "solve" precision. It (1) surveys the live
dashboards, (2) runs the corpus-grep checklists before claiming anything
open/refuted, and (3) takes exactly one honest, anti-fit micro-step. No
fitting, no tuning, no wiring an un-derived constant, no calling a fit a
derivation. Every number below carries an explicit epistemic tier.

## 1. Live dashboard status

### 1a. L1 — compute precision: **MET**

`computations/onepb-status-dashboard.witness.json` (computedAt 2026-07-20,
scriptHash `3fefbce75bf4`):

- `structural_max_non_anchor_delta_ppb = 2.78e-8` ppb — i.e. **2.78e-14 ppQ**,
  far inside the L1 target of 1 ppQ = 1e-6 ppb.
- `markov_trace_max_rel_delta = 0.0` (Hoefsmit vs markov_peel, tol 1e-9),
  `lp_max_duality_gap = 0.0`, Brundan–Kleshchev 20/20.

L1 (internal cross-method agreement ≤ 1 ppQ at substrate q₀) is met and
not at risk here. The entire L2 story below is *accuracy vs experiment*,
a separate leg (AGENTS.md §Precision goals: "L1 ≠ L2").

### 1b. L2 — per-observable 100× accuracy: `beats_100x_count = 2`

`computations/per-observable-100x-status.witness.json` (computedAt
2026-07-18, scriptHash `04904109d041`, scriptCommitSha `909e4e3c58d7`).
**2/7 met** — m_e (CAL-1 anchor, err ≡ 0) and m_K/m_π (23.4 ppb vs a
26 000 ppb experimental floor, miss 0.089 = beats target). The five
failing observables, with the root-cause audit each traces to:

| obs | pred (MeV) | err_ppb | target_100x_ppb | **miss ×** | tier of the residual | documented root cause |
|-----|-----------|---------|-----------------|-----------|----------------------|-----------------------|
| **m_p** | 938.272089427 | 1.35 | 0.00309 | **437** | de-fitted round-trip (honest) | fitted Habiro tower `(1+46u⁴)(1+4u⁵)(1−29u⁶)` **dropped** 2026-07-04; documented-pin round-trip +1.35 ppb — [`2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md) |
| **m_μ** | 105.658397811 | 209.8 | 0.2177 | **964** | proton-anchored **prediction** (9.5σ) | the μ–p substrate tension: post the 2026-05-28 proton re-pin, m_μ is a prediction not the anchor — [`2026-05-30-q0-repin-stale-witness-audit.md`](2026-05-30-q0-repin-stale-witness-audit.md), AGENTS.md §q₀-anchor STRICT rule 1 / bean `tnjb` |
| **Q_β** | 0.782334386518 | 1248 | 7.797 | **160** | honest N=2 fallback (c₂=−1 proved-Taylor-exact only) | the c_k-truncation-order / Habiro-element open problem — [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md), [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) |
| **m_n** | 939.565422765 | 2.39 | 0.00575 | **416** | Path C additive: m_p + Q_β + m_e | shared-root with the trio — [`2026-07-11-trio-shared-root-qbeta-bottleneck.md`](2026-07-11-trio-shared-root-qbeta-bottleneck.md) |
| **Δ_pn** | 1.29333333721 | 756 | 4.739 | **159** | Path C: Q_β + m_e | same trio root (= Q_β) |

The **Q_β / m_n / Δ_pn trio** is one problem, not three: `m_n = m_p + Q_β + m_e`,
`Δ_pn = Q_β + m_e`. The 2026-07-11 audit confirmed the residuals satisfy the
additive identities to ~1e-9 MeV, so **closing the trio ⇒ closing Q_β**. Q_β's
residual is the c_k/Habiro open item; do **not** conflate it with the cruder
observations-level `α·|ΔΦ|` (0.63%) object, which is scoped to its own content
block and ~10⁴× less accurate.

So the L2 gap decomposes into exactly **three independent open fronts**:
(i) **Q_β** (drives the trio, 3 of 5 fails) — c_k/Habiro, research-grade ppb;
(ii) **m_p** — de-fitted, needs substrate-q₀ derivation (Subgoal-2);
(iii) **m_μ** — the μ–p tension, structural not a compute bug.

## 2. Corpus-grep (anti-over-claim, STRICT checklist)

I am not declaring anything newly open/refuted — I am confirming the survey
above reflects the *current* corpus status (that no more-recent audit has
closed these). Grep paths:

- `docs/audits/` + `docs/coordination/` for `q_beta|c_k truncat|habiro|100x|de-fit`:
  the most recent live artifacts are [`docs/coordination/2026-07-26-q0-varies-imq-c3.md`](../coordination/2026-07-26-q0-varies-imq-c3.md)
  and [`docs/coordination/2026-07-24-binding-mass-workplan-refresh.md`](../coordination/2026-07-24-binding-mass-workplan-refresh.md).
- The 2026-07-26 doc confirms Q_β/c₃ is **actively open**: the c₃ anchor-swing
  is **proved non-categorical at strictly real q₀** (exclusion chain #4282 /
  #4288 / #4293 — a *scope-(b) structural exclusion* for the strictly-real-q₀
  hypothesis class), with the remaining Im(q)-carrier route pursued under an
  explicit anti-fit guardrail ("a per-anchor-fitted Im(q) is a FIT, labelled,
  never wired"). **Nothing wired; Q_β not closed.**

Conclusion: the 2/7 count and the five miss factors are the current corpus
status. No over-claim.

## 3. The one honest step — L2 witness currency + internal-consistency audit

**What I could not do (named environment blocker).** The intended micro-step
was to *re-run the L2 producer* (`computations/per_observable_100x_status.py`)
to confirm the committed witness is current, per the witness-refresh
discipline. **This environment blocks it:** the root filesystem is at **100%
(23 MB free)**, `numpy` is absent, and `pip install` fails with
`OSError: [Errno 28] No space left on device`. The producer's transitive
import chain needs numpy, so a clean re-run is not possible here. This is an
infrastructure blocker, not a content finding — flagged so the next agent
(with a healthy disk) can do the machine re-run.

**What I did instead (compute-free, anti-fit).** Using the one available
dependency (`mpmath` 1.3.0, no numpy needed for pure arithmetic), I
recomputed each row's `err_ppb` and `miss_factor` directly from the stored
`pred_MeV` / `codata_MeV` / `sigma_exp_ppb`, and cross-checked the input
`pred_MeV` values against the three root-cause audits. Findings:

1. **Internally consistent.** Every stored `err_ppb` and `miss_factor` matches
   a fresh recomputation to <2% (e.g. m_p 437.0 stored vs 436.87 recomputed;
   Q_β 160.1 vs 160.09; m_μ 963.6 vs 963.49). The dashboard arithmetic is not
   misreporting. *(tier: symbolic-exact — pure recomputation of the witness's
   own stated formulas.)*

2. **The bean-`tnjb` m_μ flip bug is ABSENT.** The committed witness reports
   m_μ = 105.658397811 → **963.6× (FAIL)**, i.e. the *proton-anchored
   prediction*, **not** the muon-q₀ Borromean symptom value (~105.6583756 →
   ~1.36 ppb) that would silently flip m_μ FAIL→MET. This is exactly the
   failure mode AGENTS.md §q₀-anchor rule 3 / bean `tnjb` warns about; the
   committed witness is on the correct side of it.

3. **m_p correctly reflects the DROPPED fitted Habiro tower.** pred = 1.35 ppb
   (437×), matching the 2026-07-04 de-fitted documented-pin round-trip — **not**
   the fitted 0.0004 ppb value that the removed muon-era tower produced. The
   witness is honest (anti-fit) here.

4. **Q_β uses the honest N=2 fallback** (`source_witness: "Q_N2 (fallback;
   qbeta-ck-cache witness not present)"`), i.e. only the proved-Taylor-exact
   c₂=−1 term — the higher c_k are near-match/fitted and correctly **not**
   wired. Residual 1248 ppb matches the trio audit's `r(Q_β)`.

**Net.** The committed 2026-07-18 L2 witness is current and trustworthy: its
arithmetic is self-consistent and its per-observable inputs correctly encode
the *de-fitted, anti-fit* state documented across the three root-cause audits.
The `beats_100x_count = 2` headline is not a staleness artifact. No stale/
misreporting witness was found to refresh; the compute-side machine re-run is
deferred to a healthy-disk environment.

## Feasibility (outside view, blunt)

No L2 observable is closeable by a bounded engineering step:

- **Q_β (trio, 3/5 fails)** is a genuinely open research problem with a
  6+-entry flip-flop history. Its cleanest *hypothesis-class* result is a
  **negative**: the c₃ anchor-swing is proved non-categorical at real q₀. The
  live Im(q)-carrier route is explicitly at risk of becoming "the seventh
  ansatz" and is fenced by an anti-fit guardrail. Do not expect a quick win.
- **m_p / m_μ** require a *substrate derivation of q₀* (Subgoal-2, now
  open-for-all since 2026-07-11 but research-grade). The μ–p tension is
  structural: any q₀ pin puts an ~11.5 ppb theory residual somewhere; pinning
  on m_p makes m_μ a 9.5σ prediction by construction.

The honest posture for a single session is exactly what this doc does: keep
the dashboard trustworthy, keep the fits out, and hand the open fronts to the
research ledgers (`1ppq-qbeta.md`, the 2026-07-26 Im(q) front) rather than
manufacture a number.
