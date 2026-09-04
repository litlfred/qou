# The cyclic-triple word class under the surviving log binding law — extensive now, and 3–8× too large per bond

**Date:** 2026-09-04 · **Beans:** `qou-rp9i` (this), `qou-sorn` (the linear-law reading it
supersedes), `qou-2pnv` (retraction sweep: this tranche retracts its own two surfaces),
`qou-brng` · **Arc:** many-body collective term / word class · **Scope:** re-reading a measured
result under the binding law #6611 leaves standing; closed forms only, no new mechanism.
**Nothing is wired, nothing is fitted.** Verdict: **scope-(a) negative** for the class under the
log law, for a different reason than under the linear one.

## 1. Why this exists

`2026-09-04-cyclic-triple-word-class-prune-and-probe.md` (bean `qou-sorn`, merged in #6561 this
morning) measured the one cross-term-bearing non-monotone class on the production ²H–⁴He words
and converted it to MeV with `B = Q_β·(tr_free − tr_atom)`, the law `binding_canonical` still
implements. Its §4.3 explicitly deferred: *"under a logarithmic binding law … the same reorder
would read as 2–4 nats per bond … no word-class result is interpretable until [the law question]
does."* Hours later #6611 (merged 09:17 UTC) refuted the linear law at every scale (p5–p95 spread
1592× over 2548 AME nuclides) and derived the replacement, already in the repo as
`binding_log_free_energy.py`:

    B = E₀ · ln( tr_M(free) / tr_M(atom) ),   E₀ = m_e / (q₀(q₀−1)) = 4.18598 MeV   (derived, no fit)

So the deferred question now has an answer to be read against. This note reads it.

**Retraction of my own surfaces.** #6611 notes that the sweep of surfaces still stating
`B = Q_β·Δtr` has not run (`qou-2pnv`). Two such surfaces were created *today*, by me, after
#6611's branch existed and before it merged: the `qou-sorn` audit doc and
`cyclic_triple_bond_cross_term_probe.py`. Both now carry a superseded-law note pointing here.
Their trace-level results (the Lean prune, the 32/32 kernel agreement, the closed form) are
untouched; only their MeV column and its verdict were law-dependent.

## 2. What the log law changes structurally

A monotone word's log-trace is a **sum** of run log-traces (`MonotoneWordTraceFactorizes`), so a
cyclic triple at bond `k` shifts `B` by a **per-bond constant**

    ΔB_k = E₀ · ln( f_prod,k / f_cyc,k ),
    f_prod,k = tr(L₁L₂L₃L₄)·tr(B),   f_cyc,k = tr(L₁L₂L₃L₄)·tr(B²) + b(L₁L₂L₃)·(z² − hz − 1),

depending only on the bond's species pair and its adjacent nucleon — **not on `A`**. Under the
linear law the same reorder was multiplied down by every other letter trace in the word
(intensive); under the log law it is **extensive**. That is a real change in kind, and it is the
reason the class had to be re-read rather than left closed.

Probe: `computations/probes/cyclic_triple_under_log_law_probe.py` — **20/20**, 50 dps, closed
forms only (each one validated byte-for-byte against the production kernel in the earlier probe,
re-checked here against `tr_m_atom_zn` for all four nuclei). Extensivity is checked, not assumed:
equal bond keys give one shift across nuclei to 50 dps.

## 3. Result (proton pin, convention D, `E₀` derived)

Per-bond shift of making one bond a cyclic triple — the same number wherever that bond occurs:

| bond key | production block | cyclic block | ΔB(cyclic) | nats | ΔB(double bond only) |
|---|---:|---:|---:|---:|---:|
| p–p | 0.54740 | 0.22227 | **+3.773 MeV** | 0.901 | −2.555 |
| p–n | 0.45407 | 0.11766 | **+5.653 MeV** | 1.350 | −2.879 |
| n–n | 0.35166 | 0.01213 | **+14.093 MeV** | 3.367 | −3.429 |

Against the log-law residuals:

| nucleus | `B_log` (prod) | `B_AME` | residual | ΣΔB all bonds cyclic | `B_cyc` / AME |
|---|---:|---:|---:|---:|---:|
| ²H | 2.833 | 2.225 | **−0.609** (over-bound) | +5.653 | 3.81× |
| ³H | 6.631 | 8.482 | +1.851 | +19.745 | 3.11× |
| ³He | 4.884 | 7.718 | +2.834 | +9.426 | 1.85× |
| ⁴He | 8.682 | 28.296 | +19.614 | +23.518 | 1.14× |

## 4. Verdict — scope-(a) negative, and what kind

1. **Extensive, right sign, wrong size.** Every cyclic block is smaller than its production block
   (extra binding, 12/12 checks), and the shift is additive across bonds. But it over-shoots the
   residual in every nucleus, by 3.8× at ²H — which the log law **already over-binds** by
   0.61 MeV, so any positive shift there is wrong-signed against the data — and by 3× at `A = 3`.
   ⁴He lands within 14 % only because its residual is large; the same per-bond numbers put
   ³H at 26 MeV against 8.5.
2. **The species pattern is the retracted one.** `n–n ≫ p–n > p–p` (14.1 / 5.7 / 3.8 MeV) is a
   strong `N−Z` asymmetry with the neutron-rich side over-bound — the same sign #6611 measured
   (`κ_derived = +0.22`) and **retracted** against the data optimum (`κ ≈ −0.15`), and it is
   3–4× larger. The n–n figure is also the fragile one: its cyclic block is `0.012`, a
   near-cancellation between `tr(L)·tr(B²)` and the Markov defect, so 3.4 nats is the log of a
   small difference, not a mechanism.
3. **No count to fit.** One cyclic triple per bond is the choice-free member; fractional
   "interleaving weights" per species would be a three-parameter fit and are not done. The
   `qou-sorn` note's option "stop looking inside `tr_M` for the extensive term" is *weakened*
   by this re-read — the log law does make word-level reorders extensive — but the specific
   class still fails on magnitude and on the asymmetry sign, so the recommendation there is
   revised rather than reversed (§5).

## 5. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** The class is recorded closed under both laws, each for its own
  reason (intensive under linear; over-shooting and wrong-asymmetry under log). Cost 0.
- **Revised reading of the word-level route.** Under the log law a reorder *is* extensive, so the
  earlier "not a functional of `tr_M` of the single word" is too strong as stated; what is
  measured is that the **cyclic triple** is the wrong such functional. The one remaining shape
  this arc has not measured is the `A ≥ 3` cyclic coordination graph (band generator, over/under
  choice); its per-bond shift would be a fourth block number of the same kind, and the
  asymmetry argument in §4.2 applies to it unchanged unless the band conjugation moves the
  species dependence. That is an argument, not a measurement.
- **The `E₀` scale.** #6611 records `E₀` as 2.656× below the best single scale. Nothing here
  depends on that: the *ratios* ΣΔB / residual are scale-free, and they are what fail.

**Recommendation (judgement):** default. The log law's own lead is the symmetry energy
(#6611: residual correlates −0.80 with `(N−Z)²/A²`), and this class supplies an asymmetry of the
wrong sign, so pursuing it further would be pursuing the retracted direction.

## 6. Verification

- Probe 20/20; every trace equals the production `tr_m_atom_zn` to 50 dps; the extensivity
  equalities hold to 50 dps for all three bond keys.
- `scripts/precision-gates.sh --changed`: exit 1 on the corpus's standing reds only; this probe
  appears in no red list.
- No Lean changes (the theorems of #6561 are what the closed forms rest on). Repo CI is
  `workflow_dispatch`-only; this agent verification is the gate.
