# Scope — Q_β Habiro-PDE + binding Δ_λ jet-exponent + 242 ppb cleanup (2026-06-18)

Owner-directed tranche, branch `claude/sleepy-wozniak-jesgmw`.
Parent bean: [`.beans/qkhc--qbeta-kernel-hunt-stage-c.md`](../../.beans/qkhc--qbeta-kernel-hunt-stage-c.md).
Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).

Discipline: formalize-first (prune the class before any wide scan); tiered
status (proved / near-match / conjecture / refuted), never binary; **no fit**
(Δ_λ gate — do not propose a seventh ansatz); fibre vs observable kept distinct.

## Asks

1. Derive the binding Δ_λ exponent `10A−5 = 5(2A−1)` — are confinement
   (Step 10 SDP), the GB filtration (Step 7), or the jet-prefix order
   (Step 8) used?
2. `c_k` as a Habiro element — what q-difference PDE do they satisfy?
   Is it a q-heat-kernel equation, and does that fix the relevant
   eigenfunction basis?
3. Q_β Hahn–Exton q-Bessel — why proved but **not wired**?
4. Remove / fix the stale `canonical-mass-table-242ppb.witness.json`.

## Item 1 — exponent `10A−5`: confinement / GB / jet are NOT used (finding)

Current derivation
([`delta_lambda_exponent_from_crossings.py`](../../computations/delta_lambda_exponent_from_crossings.py))
is a **raw combinatorial crossing count** off `atom_braid_word_3A(Z,N)`:
`σ = 7Z+5N−1`, `σ⁻¹ = 3Z+5N−1`, so `σ+σ⁻¹ = 10A−2` (Z,N cancels).

| Piece | Status |
|-------|--------|
| Slope 10 / nucleon (`σ+σ⁻¹ = 10A−2`) | **DERIVED** (closed form, verified D,T,³He,⁴He) |
| Per-site re-read `5·(2A−1)` (5 = Bring quintic per chain-site) | **near-match** — `5` asserted, not derived |
| Per-nucleon `9 = intra-𝓑₃` count | **open** |
| Z-excess proton correction (~−1.4/excess-p) | **open** |
| GB normal form (Step 7) in the count | **NOT used** — raw braid word |
| Jet-prefix order (Step 8) in fixing `5` | **NOT used** |
| Confinement SDP (Step 10) | **NOT used** for the exponent (only for binding *magnitude* / operator selection) |

**Reframe (formalize-first target).** The open keystone — why `5` per
chain-site and `9` per nucleon — is exactly the structure the raw count
bypasses. Hypothesis to state as a lemma: the per-site `5` is a
**jet-grade-per-site** statement (Step 8 grades the Markov-trace Laurent
polynomial by h-power), and the intra-𝓑₃ `9` is a **GB-normal-form
crossing count** (Step 7), not a raw-word count. If true, the exponent
becomes a jet/GB statement rather than a numerology of crossing counts.
This is a class-pruning lemma, not a probe.

## Item 2 — c_k PDE, q-heat kernel, eigenbasis: intuition confirmed (fibre-level)

The `c_k` satisfy a **proved** q-difference equation. With `g(w) = Σ_k c_k w^k`:

- **First-order coefficient recurrence (★)** — PROVED (PR #2279,
  [`QBesselContiguityRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBesselContiguityRecurrence.lean), 80 dps):
  `c_{k+1}·(1 − q^{k+1})(1 − a q^k) = −q^k · c_k`, with `a = q^{ν+1}`.
- **Second-order q-difference equation (☆)** — PROVED (60 dps, residual < 1e-30,
  [`qbessel_second_order_qdifference_equation.py`](../../computations/qbeta/qbessel_second_order_qdifference_equation.py)):
  `q^ν·g(q²w) − (1 + q^ν − w)·g(qw) + g(w) = 0`.

q-holonomic (q^k-dependent coeffs), NOT C-finite; contracts to the ordinary
Bessel ODE as q → 1. The linear `−w` middle term is the source of the
descending ladder (`c_2 = −1` leading, proved PR #1602).

| Your question | Answer | Tier |
|---|---|---|
| q-heat kernel? | **Yes** — `g` is the partition function of a q-heat flow on Hecke modules, `Z_q(t) = Σ_λ d_λ(q)·exp_q(−μ_λ(q)·t)`, `μ_λ` = content-Casimir eigenvalues; per-mode depth-1 Jackson eqns compose to finite-depth q-difference. | structural (fibre) |
| Does it fix the eigenbasis? | **Yes** — **Hahn–Exton q-Bessel** (fibre) / ordinary `J_ν` (q→1), via the bar-odd Jacobi–Anger expansion `sinh(x sinh η) = 2Σ_m J_{2m+1}(x) sinh((2m+1)η)`. NOT continuous-q-Hermite / Rogers / q-Laguerre. | structural (fibre) |
| c_k a Habiro element? | **Identified** as `F(q) = Q_β/[Q_A·cos α_eff]` in the cyclotomic completion, mirroring α_EM `[2]_q·(1−h²α)` (PR #1911/#1511). Seed `c_2=−1` proved; `c_3` near-match; `c_4` fit; kernel `R(q,ξ)` structurally constrained but not categorically determined. | identified, not derived |

## Item 3 — why Hahn–Exton q-Bessel is not wired (4 blockers)

1. **Cross-anchor smoothness wall** (PR #1821 / #2300): real-`x` archimedean
   closure refuted — `dc_3/dq₀ ≈ 4.6×10⁶`; matching the 2.9 % cross-anchor swing
   needs `x ≈ 2.5×10⁶` (5 orders past physical tower scale). Refuted.
2. **Fibre vs archimedean**: the q-Bessel identity is fibre-level only; the finite
   per-n spectrum is the compact SU_q(2) q-Casimir, *not* a q-Bessel zero set. The
   q-Bessel/q-Lommel recurrence lives in the **n→∞ brane-tower** limit.
3. **Missing H≥6 typed braids** (the decisive gate): the tower-convergence test
   needs `χ_λ(𝓑_n − 𝓑_p)` at n = 6, 9, 12; only H₃ exists (H₆/H₉ deprecated).
   n=3 physical-weight residual is **6.8 %** (halved from 12.8 %). Gate: residual
   → 0 as tower extends ⇒ confirm; plateau/grow ⇒ refute.
4. **Kernel `R(q,ξ)` not categorical**: c_k still empirical/SDP-sourced past c_2.

## Unifying bottleneck (items 1 + 2/3 converge)

Binding Δ_λ (the **order** recurrence, q-Lommel second kind, item 1) and Q_β c_k
(the **argument**/contiguity recurrence, Hahn–Exton, item 2/3) are the two
recurrences of the **same** q-Bessel/q-Lommel family, and **both are blocked on
the same thing: the n→∞ brane-tower, concretely the H≥6 typed proton/neutron
braid characters `χ_λ(𝓑_n − 𝓑_p)`.** Item 1's open "5 per site / 9 per nucleon"
keystone and item 3's tower-convergence gate are the same missing data at
different indices. Highest-leverage action: **construct the H₆/H₉ typed braids**
— it is the single input that unblocks both axes.

## Item 4 — 242 ppb witness cleanup

[`canonical-mass-table-242ppb.witness.json`](../../computations/canonical-mass-table-242ppb.witness.json)
is (a) **stale** (encodes the muon-pin 242 ppb m_p floor; superseded by
the proton-repin 0.0004 ppb), (b) **provenance-less** (provenance audit
flags missing `engine` / `scriptFile` / `commitSha`), (c) **over-claimed**
— the appendix Step 9b cites it as the "canonical witness" and says it
records the Δ_λ choice + open-gate flag, but the file has no Δ_λ field.
Plan: regenerate from a real producer at canonical q₀ with provenance +
explicit Δ_λ-open flag, or re-point the appendix off the stale orphan.
Feasibility of regeneration (needs pyhecke-native) TBD.

## Acceptance

Per ask: (1) a stated jet/GB formalize-first lemma for the exponent
keystone; (2) the c_k PDE written out + a yes/no on the q-heat-kernel
eigenbasis claim; (3) the precise not-wired blocker for Hahn–Exton;
(4) the 242 ppb stale orphan removed or honestly re-pointed. All tiered,
no production wire/un-wire without ledger + tiered justification.
