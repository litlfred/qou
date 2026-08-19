# Audit: Q_β 1248 ppb — σ_theory vs σ_CAL decomposition (is it improvable by derivation?)

**Date:** 2026-06-29
**Branch / PR:** `claude/qbeta-habiro-residual-2026-06-29`
**Probe:** [`computations/probes/qbeta_habiro_residual_probe.py`](../../computations/probes/qbeta_habiro_residual_probe.py)
→ `computations/probes/qbeta-habiro-residual.witness.json`
**Discipline:** anti-flip-flop per
[`ck-dk-canonical-registry.md §8`](../coordination/ck-dk-canonical-registry.md);
this is a SCOPED INVESTIGATION — it proposes **NO** new c_k wiring.

---

## TL;DR (the verdict)

The production Q_β residual of **~1248 ppb vs CODATA is `σ_theory`**
(the framework's own formula-truncation residual at the c₂-level
derivation order), **not `σ_CAL`** (propagated input error, which is
≈ 0.29 ppb). It is therefore *theory-improvable in principle*.

**But it is NOT improvable by any proved derivation today.** The only
known route below 1248 ppb is the fitted / near-match c₃ ladder, which
is **registry-REFUTED** as a real-q derivation (2.98 % cross-anchor
swing; `dc₃/dq ≈ 4.6×10⁶`). Driving 1248 → 7.8 ppb (the L2 100×
target — itself **below** the 779.7 ppb experimental floor on the Q_β
measurement) is **Subgoal-2 / owner-gated** territory.

**No staleness issue:** the committed witnesses match a live
recomputation at the canonical proton-pinned q₀ to **1.1×10⁻⁴² ppb**.
The 1248 ppb is the genuine, current Q_N2 residual.

---

## 1. The witnesses are NOT stale (q0-repin staleness question — answered)

The cheat sheet flags a "q0-repin staleness class" (a dashboard reading
a muon-q₀ witness and scoring it as the proton-q₀ prediction). This
probe **rules it out for Q_β**:

- The canonical computations-layer q₀ is now **proton-pinned**
  (`q-pinning-50-digit.witness.json`, anchor `m_p/m_e`, recorded
  2026-06-22): `q₀ = 1.10997859555733471989…` — exactly the task's
  proton value `1.1099785955573347`.
- The production single-wrap closed form recomputed **live** at this q₀
  reproduces the committed `Q_A` witness to **1.1×10⁻⁴² ppb**. The
  ladder residuals below are therefore current, not stale.

| Ladder rung | form | residual vs CODATA |
|---|---|---:|
| N=0 (single-wrap closed form) | `m_e·\|q²−2q−1\|(q+1)/(2q³)` | **+1 677 538 ppb** (+0.168 %) |
| N=1 (Kashiwara c₁ = b) | + Kashiwara f̃₁ wrap | +73 797 ppb |
| **N=2 (c₂ = −1, PROVED)** | + bar-even Kashiwara f̃₁² | **+1248 ppb** ← production wire |

The "+0.17 %" reported by `q_beta_predicted.py` is the **N=0**
single-wrap value; the **L2 dashboard** wires **N=2** (c₂ only) at
**1248 ppb**. Both are the same de-fitted production chain at different
truncation depths — neither is stale.

---

## 2. σ_theory vs σ_CAL decomposition (the central result)

Per [`precision-goals.md`](../precision-goals.md), every prediction
carries `σ_total = σ_theory(O,N) ⊕ σ_CAL(O)`. For Q_β at the production
N=2 order:

| term | value | what it is | owner |
|---|---:|---|---|
| **σ_theory** | **1248 ppb** | Q_N2 formula-truncation residual | **us** (derivation) |
| σ_CAL (m_e) | 0.2935 ppb | propagated m_e error (0.29 ppb, linear) | external labs |
| σ_CAL (q₀) | 0.0074 ppb | propagated q₀ error via `dlnQ/dlnq = −2.60` × σ(q₀)=2.85×10⁻¹² | external labs |
| **σ_CAL total** | **0.29 ppb** | propagated input error (m_e-dominated) | external labs |
| σ_exp (target) | 779.7 ppb | experimental error on the Q_β **measurement** | sets L2 100× target = **7.8 ppb** |

**Reading.** The 1248 ppb is **σ_theory** — it is ~4300× larger than
σ_CAL (0.29 ppb), so it is the framework's *own* residual, not
propagated experimental error. q₀'s contribution is negligible
(0.0074 ppb) because the production formula is only mildly sensitive to
q₀ (`dlnQ/dlnq ≈ −2.6`) and q₀ is pinned to 2.85×10⁻¹² (CODATA m_p/m_e,
0.06 ppb).

So in the strict `σ_theory`/`σ_CAL` sense, **the 1248 ppb IS
theory-improvable** — it is not a propagated-CAL floor. The question is
*whether a proved term exists* to improve it.

---

## 3. Anchor-stability cross-check (the disciplined part)

Two distinct anchor-stability questions:

**(a) The production form is parameter-free in q.** It has no fitted
c_k, so its residual inherits only q₀'s own shift on re-pinning. The
worst-case documented μ-p tension (11.5 ppb in q₀,
[`2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md))
moves Q_β by `|dlnQ/dlnq|·11.5 ≈ 30 ppb` — far below the 1248 ppb
residual. The production value is anchor-stable; nothing hidden moves.

**(b) The only known sub-1248-ppb route (c₃) is anchor-UNSTABLE.** The
c₃ "target" that would absorb the residual is ≈ −2.020 at the proton
pin (a near-match to `J_Hopf = −2`). Per the registry's settled verdict
([`ck-dk-canonical-registry.md §3`](../coordination/ck-dk-canonical-registry.md),
falsification PRs #1593/#1842):

- cross-anchor swing **2.98 %** (≫ the 10⁻⁵⁰ compute precision — i.e.
  not a Taylor coefficient),
- `dc₃/dq ≈ 4.6×10⁶` — a real-q rigidity-falsification: a genuine
  Habiro c₃, if it existed, would have to be **complex-analytic /
  root-of-unity at the fibre level** (AGENTS.md §"Im(q) at fibre vs
  observable level"), which is the **open keystone**, not a derived
  value.

> **Correction 2026-08-16.** The `2.98 %` cross-anchor swing cited here is against a **superseded** muon `c_3 = −2.0097` (pre-#1422). The current pair gives **2.3748 %** (proton-normalised). The conclusion is unaffected — 2.3748 % is still vast beside the 10⁻⁵⁰ compute precision — but quote the current figure. Measured: [`qbeta_c3_crossanchor_swing_provenance_probe.py`](../../computations/qbeta/qbeta_c3_crossanchor_swing_provenance_probe.py).


A term that moves this much on re-pinning is a **near-match, not a
derivation** — exactly the trap that drove the documented 6-entry
flip-flop. We do not propose it.

---

## 4. Honest verdict

**Q: Is Q_β's 1248 ppb improvable by derivation, and if so how much?**

- **It is `σ_theory`, not `σ_CAL`** — so it is improvable *in principle*
  by a PROVED higher-order term.
- **No such proved term exists today.** Only c₂ = −1 is Taylor-exact
  and wired. The c₃…c₇ ladder is entirely near-match / CODATA-fit /
  silver-anchored, all anchor-UNSTABLE (registry §3), and the genuine
  fix — the **Q_β Habiro element** F(q) — is the OPEN keystone
  (kernel R(q,ξ) unconstructed; constant-kernel refuted through depth 4).
- **The L2 100× target (7.8 ppb) is below the experimental floor**
  (σ_exp = 779.7 ppb on the Q_β measurement itself). Reaching it is the
  Subgoal-2 regime that the coordination ledger explicitly declined
  (2026-05-08, q₀ substrate-derivation), **owner-gated**.

**Bottom line: the 1248 ppb is NOT improvable by a proved derivation at
present.** It is the honest c₂-level truncation residual. Closing it
requires either (i) constructing the open Q_β Habiro element F(q)
(a genuine, hard, open research target — not a c_k re-fit), or (ii)
owner-reversal of the Subgoal-2 q₀-derivation decline. No production
change is warranted by this investigation.

---

## 5. What did NOT change

- **No c_k wired/un-wired.** Production stays at c₂-only (1248 ppb).
- **No witness migrated.** The ~840 muon-q₀ `computations/` witnesses
  are untouched (bean `tnjb`, owner-gated).
- **No new ansatz proposed.** Per the registry §8 flip-flop guard and
  the precision-goals "no seventh fit" discipline.

## Cross-references

- [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) — the ONE c_k source of truth
- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) — flip-flop saga (6 entries)
- [`docs/precision-goals.md`](../precision-goals.md) — σ_theory/σ_CAL framing
- [`docs/audits/2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md) — μ-p floor
- [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md) — truncation-order framing
