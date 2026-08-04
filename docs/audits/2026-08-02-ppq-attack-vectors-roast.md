# "Close 1ppq" — attack-vector audit + roast (2026-08-02)

Branch `claude/q-deformed-saddle-offsets-bdn992`. Follow-up to the merged PR #4573.
Four parallel agents surveyed the precision-accuracy attack vectors (options 1,2,3,5
of the "close 1ppq" menu; option 4 = derive q₀ was declined by the owner). This
records the findings with the critical-distance license applied — a roast, not a
sales pitch.

## The framing correction (read first)

"Close 1ppq" conflates two legs (`docs/precision-goals.md`):
- **L1 — compute cross-method agreement ≤ 1 ppq.** Already MET (65-dps mpmath).
- **L2 — per-observable accuracy** (σ_pred ≤ σ_exp/100). Mostly NOT met, and for the
  headline masses **structurally blocked or measurement-limited** — see below.

There is no low-difficulty compute route to ppq *accuracy*. The honest ppq wins are
L1 (already banked). Anyone quoting "ppq" for m_p accuracy is conflating the legs.

## Roast 1 — m_K/m_π "meets 100×" leans on the experimental α_em (bean qou-5ipv)

The one L2-passing prediction is `m_K²/m_π² = [3]_q·[4]_q + (α_em/π)·(3q²−1)/(2q²)`.
Dissected (`meson_em_sinh_closed_form.py` + roast probe):

- **The core `[3]_q·[4]_q` is exact and Lean-proved.** Good. It supplies ~99.98% of
  the ratio. The EM term is a ~203 ppm correction.
- **α_em = 137.035944 is HARDCODED** ("CS-corrected, Witten κ, 399 ppb") — the
  *experimental* value. Substituting the framework's own **derived** α_em
  (`q·[9]_q·[10]_q` → α_em⁻¹ = **136.82**, itself −1553 ppm from CODATA) degrades
  m_K/m_π from ~47 ppb to **~363 ppb (~8×)**. So the "meets 100×" claim is
  `[3][4] + (measured α_em/π)·EM` — it **imports the measured fine-structure constant**;
  the derived one is ~8× worse. The dependence is real, though not catastrophic.
  **[CORRECTION 2026-08-02:** an earlier version of this audit cited α_em⁻¹≈609 and a
  −157,000 ppb miss — that used a wrong `ℏ_q²` numerator instead of the skein amplitude
  `(q−q⁻¹)²`; the correct derived α_em⁻¹ is 136.82, flagged by the α_EM per-loop agent.**]**
- **The EM factor's justification is undermined.** `(3q²−1)/(2q²)` is presented as
  "the leading two terms of `1+log(1+ℏ_q)`", with "3 = generations" (T(2,3/5/7))
  bolted onto the coefficient. But the **full** `1+log(1+ℏ_q)` fits *worse* (+103 ppb)
  than the 2-term truncation (+47 ppb). A truncation that beats its own parent series
  is a fit, not a convergent approximation — the "truncated-log / 3-generations" story
  is numerology on a Taylor coefficient.
- **The residual is structure-dominated, not α_em-precision-dominated:** swapping
  α_em 137.035944 → CODATA 137.035999 barely moves the miss (46.9 → 46.8 ppb).

**Verdict:** m_K/m_π is the best *ratio* target (q₀-robust, S=+0.40 — Agent 1), but its
"exactness" is overstated: it is exact in the Hecke core and *anchored + truncated* in
the EM correction. Closing it to ppq requires a **derived** α_em (blocked — see Roast 3)
and a derived (not truncated) EM factor. Re-scope the corpus claim accordingly.

## Roast 2 — ν_SDP {1,2,2} is the bond count A−1 in disguise (beans qou-k2xr, qou-58r5)

Agent 5's sharp result. Every categorically-honest candidate count for ν_SDP collapses
to **sc(n) = #self-conjugate (bar-fixed) Wedderburn blocks of H_{3A}(q) = #partitions
into distinct odd parts**. And (verified this session):

| A | n=3A | sc(n) | A−1 (bond count, Lean-proved M_n=n−1) | agree |
|---|------|-------|----------------------------------------|-------|
| 2 | 6 | 1 | 1 | ✓ |
| 3 | 9 | 2 | 2 | ✓ |
| 4 | 12 | **3** | **3** | ✓ |
| 5 | 15 | 4 | 4 | ✓ |
| 6 | 18 | 5 | 5 | ✓ |
| 7 | 21 | **8** | **6** | ✗ (first divergence) |

**sc(3A) = A−1 for every A ≤ 6** — i.e. for the entire range where the linear-chain
knot/SDP framing is even viable. So on all accessible light data, ν_SDP is
*indistinguishable* from the bond count A−1 the corpus **already derives**. The real
open content of `conj:kashaev-density-equals-sdp-multiplicity` is therefore **NOT
"which integer"** (it is A−1) but the unproved **identity** "SDP-saturating-multiplicity
= bar-fixed-block count = bond count." Wiring ν_SDP = sc(n) without proving that
identity is anti-laundering (Axiomatization is NOT a Proof).

**The decisive datum:** every monotone count (sc, A−1, distinct-odd-parts) predicts
**⁴He ν_SDP = 3**, but the corpus *assumes* 2 (extrapolated, no census knot). Resolving
⁴He (3 vs 2) is the single highest-value next step:
- ⁴He = 2 ⇒ the whole monotone family is refuted together ⇒ ν_SDP must be
  **non-monotone / knot-intrinsic** (an object not yet in the corpus).
- ⁴He = 3 ⇒ sc(n) and A−1 survive, degenerate; the identity-proof is the sole gap.

Blocked routes (honest negatives): MTC / fusion quantum-dimension count is **not viable**
(q₀ ≈ 1.11 is real, not a root of unity — no Weyl-alcove truncation); plain
Frobenius–Schur indicators are uninformative (all Sₙ irreps real); the direct SDP
support is the 0/3558 over-determination artifact (bean qou-vd7j; Frobenius re-pose in
progress).

## Roast 3 — the exact-element attack vector (#3) is largely exhausted (bean qou-5et6)

Agent 3's survey. Exact fibre elements already banked: α_EM factor `[2]_q(1−h²α)`
(proved), m_K/m_π core, Q_β `c_2=−1` (proved), `tr_M` (finite Habiro). The L2-missing
observables are:
- **Q_β c_3+ / m_n / Δ_pn — proved-CLOSED for the Habiro/q-difference route.** KC20
  (Lean): no real-q/quadratic fibre element. KC22: the bar-odd D-ladder is proved
  non-(q-)holonomic. Only transcendental/resurgent (Écalle) machinery remains, and even
  that resolves *structure* while the value stays measurement-limited.
- **m_p, m_μ — measurement-limited** (μ–p tension; next-gen neutron Q_β), not
  compute-limited (`PinRobustnessOfRatios.lean`, sorry-free — ratios are provably blind
  to the μ–p split).

The one genuine open *derivation* lever: **α_EM per-loop measure Clauses A+B** (the
θ-factor). Deriving them would upgrade α_EM from "exact factor, open normalization"
toward a closed prediction — and would feed Roast 1 (a derived α_em for m_K/m_π). Hard,
but well-posed and not a fit.

## Net

The "close 1ppq (accuracy)" program is mostly blocked: masses are measurement-limited
(proved), Q_β is structure-closed for the tractable route (proved), and the one L2 pass
(m_K/m_π) imports the experimental α_em + a truncated EM factor. The honest, non-fit
attack surface reduces to:
1. **Resolve ⁴He ν_SDP 3-vs-2** (qou-k2xr) — cheap, decisive, kills or saves a whole family.
2. **Prove/refute the SDP-mult = sc(n) = A−1 identity** (qou-58r5) — the real content.
3. **α_EM per-loop measure** (qou-5et6) — the one open derivation that also unblocks m_K/m_π.
4. **Re-scope the m_K/m_π "meets 100×" claim** (qou-5ipv) — it is α_em-anchored, not parameter-free.

Nothing here reaches ppq accuracy; the value is in *sharpening the open problems and
removing overclaims*, which is what the anti-fit discipline is for.

## Roast 4 — the Frobenius knot-solver LP has NO selective power (bean qou-vd7j)

Option 2 result (`frobenius_repose_probe.py` + `2026-08-02-frobenius-repose-nonselective.md`).
Re-posing the LP without the inconsistent net row **removes the 0/3558 over-determination
artifact** but does NOT recover a selective ν_SDP — both variants (drop net; net→`1ᵀG⁻¹nf`)
give active-channel count 1 for **every** nucleus (²H,³H,³He all → 1, not {1,2,2}). Mechanism:
G (H₃ NF Gram) is 6×6 **full-rank/invertible**, so `Gx=nf` is a unique linear solve with no
optimisation freedom; the shadow prices `y=G⁻ᵀt=(γ:1,else:0)` are **independent of the
nucleus**, and `nf∈range(G)` is guaranteed. So the nucleus's identity lives entirely in `nf`
and `x=G⁻¹nf` carries nothing extra. Scope-(a): this LP, as posed or re-posed, cannot select
ν_SDP. A real selector must come from something the invertible H₃ solve doesn't see — the
brane-tower/Δ_λ, a genuine PSD *inequality* relaxation, or a rank-deficient demand map. None wired.

Option 4 (derive q₀) declined by owner.
