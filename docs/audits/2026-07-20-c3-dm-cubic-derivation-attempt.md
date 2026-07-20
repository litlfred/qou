# Q_β `c_3` — Donagi–Markman cubic / Berezinian even–odd cross-term derivation attempt

**Date:** 2026-07-20
**Branch:** `claude/argument-principle-residue-sum-2026-07-20`
**Bean:** `qou-1dnr` (Derive `c_3` exactly → Q_β 100× target)
**Verdict:** **scope-(a) NEGATIVE** — NOT a derivation, NOT even a near-match.
Q_β does **not** meet its 100× target via this route. Nothing wired.

> **Read the registry, not this doc, for `c_3`'s tier.** The authoritative
> per-rung status is
> [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
> §3/§9. This doc records ONE more attempt and why it fails; it changes no tier.
> `c_3` stays **EMPIRICAL / REFUTED-as-real-q**.

## 1. The route (NEW angle, landed 2026-07-20)

The super-Berezinian / Door-v scaffold
([`QOU.Brings.SuperDMBerezinian`](../../content/quantum-observable-universe/lean/QOU/Brings/SuperDMBerezinian.lean),
[`2026-07-20-super-berezinian-dm-cubic-narrowing.md`](2026-07-20-super-berezinian-dm-cubic-narrowing.md))
reads the ladder `Q_β = Q_base·∏(1+c_k u^k)`, `u = b·ℏ_q²`, as jets of a
prepotential `F`:

* `c_2 = ∂²F` — the period matrix τ (proved-EXACT bar-even 2-jet, `c_2 = −1`);
* `c_3 = ∂³F` — the **Donagi–Markman cubic** 3-jet, bar-ODD (sinh/decay) face;
* the first even/odd **mixing** order is the Berezinian cross-term `B·D⁻¹·C`
  inside `Ber = det(A − B·D⁻¹·C)·(det D)⁻¹` (`berezinian_offDiag_zero`: the
  cross-term vanishes at block-diagonal order — it IS the mixing correction).

The task: build a CODATA-independent realization of `c_3 = ∂³F` (bar-odd) and run
the anchor-invariance falsification.

## 2. Refuted mechanisms this attempt does NOT repeat (corpus-grep, STRICT)

Checked against the registry §3/§9 + the `1ppq-qbeta.md` flip-flop table before
computing. This route is **not** any of:

| mechanism | status | where |
|---|---|---|
| `c_3 = J_Hopf(q=1) = −2` | near-match, 4× flip-flopped | flip-flop table #1–#4 |
| `c_3 = J − ℏ_q²` | near-match | flip #1 |
| `[3]_q/25` 3-rung Habiro | proton-anchor-only, rigidity-falsified | PR #1781/#1842 |
| Li_2^q × spectral combiner | refuted (mech #7) | PR #1609 |
| Δtr_M bar-decomposition value-identity | accidental cross-order coincidence | PR #1593/#1615 |
| `−Vol(4₁)+u−(10/3)u²` | anchor-blind, misses proton | re-scoped 2026-07-11 |
| real-q / quadratic closure | **Lean-EXCLUDED** (degree-3 field, no quadratic anchor is a root) | **KC20** |
| q-difference / (q-)holonomic recurrence | **Lean-EXCLUDED** (`D(ũ)` non-holonomic; resurgent) | **KC22** |

The Berezinian even/odd cross-term framing is genuinely new (the scaffold landed
2026-07-20). The attempt tests whether it escapes KC20/KC21/KC22. **It does not.**

**Task approach #1 ("read `c_3` off the proved q-lift 3-term recurrence
`[n+2]_q b_{n+2} = b_{n+1} + b_n`") is refuted A PRIORI by KC22**: the bar-odd
`c_3` channel `D(ũ)` is proved NOT low-order (q-)holonomic in any tested class —
it is transcendental/resurgent (Écalle acceleration), so it is not the output of
any q-difference recurrence. Running that scan would re-derive a closed negative;
the formalize-first / corpus-grep discipline pruned it before compute.

## 3. What was computed

Probe:
[`computations/probes/qbeta_c3_dm_cubic_berezinian_probe.py`](../../computations/probes/qbeta_c3_dm_cubic_berezinian_probe.py)
→ `qbeta-c3-dm-cubic-berezinian-probe.witness.json` (mpmath, 50 dps, 0.8 s).

Two CODATA-independent realizations of the 3-jet, each evaluated at the
**proton-pinned** and **muon-pinned** q₀:

1. **DM cubic 3-jet `∂³F` of the categorical phase.** `F` = the on-main
   substrate phase; `G(u) = cos(α − u/2)(1 − u²)/cos(α)`, `α = (z−1)h/2` derived
   from the substrate (Markov weight `z`, `h = q−1/q`), NOT from CODATA. `c_3 =
   ` the u³ Taylor coefficient.

2. **Berezinian even/odd cross-fraction `B·D⁻¹·C`** from the `H_3(q)` super-period
   matrix: even (bar-even) sector = the `(3)`, `(1,1,1)` Wedderburn characters;
   odd (bar-odd) sector = `(2,1)` (`κ_{(2,1)}` is exactly bar-odd — KC13); the
   off-diagonal `B, C` carry three natural leading mixings (`z`, `ℏ_q`, mixed).

## 4. Results

| quantity | proton q₀ | muon q₀ | cross-anchor swing |
|---|---|---|---|
| **empirical `c_3`** (CODATA-inverted, FIT side) | −2.06934 | −2.02020 | **+2.43 %** (`dc_3/dq ≈ 3.84×10⁶`) |
| DM cubic 3-jet `∂³F` (phase) | +0.0272833108 | +0.0272833139 | **−1.1×10⁻⁵ %** (`dc_3/dq ≈ 0.24`) |
| Berezinian cross `[markov]` | −44.28513 | −44.28512 | +2.3×10⁻⁵ % |
| Berezinian cross `[hbar]` | −1.743759 | −1.743759 | +1.9×10⁻⁶ % |
| Berezinian cross `[mixed]` | −18.54173 | −18.54173 | +1.2×10⁻⁵ % |

**The decisive facts:**

* **`u, α, b` are anchor-invariant to 8+ digits** (the two anchors differ by
  `Δq ≈ 1.3×10⁻⁸`). The empirical `c_3` swing 2.43 % lives ENTIRELY in the
  `1/u³` ladder inversion (`u³ ≈ 6.2×10⁻⁷` amplifies a smooth numerator zero by
  ~1.6×10⁶) — exactly registry **KC21**.
* **Both derived realizations are anchor-INVARIANT** (swing ~10⁻⁵ %, ~5 orders
  below the empirical 2.43 %); any real-q algebraic construction of the substrate
  is smooth, `dc_3/dq = O(1)`, ~10⁶× too flat to track the empirical swing.
* The DM 3-jet **value** `+0.027` does not even near-match the empirical `−2.07`
  at EITHER anchor (wrong sign and magnitude). The Berezinian cross-fraction
  values are modeling-dependent (the geometric period data is the open keystone),
  but their anchor-invariance is not.

## 5. The anchor-invariance test result — the honest verdict

The task's falsifiable test: anchor-invariant → derivation; swings → fit. The
outcome is the third, sharper case the registry KC21 predicts:

> **The derived `c_3` IS anchor-invariant (a genuine smooth object), and PRECISELY
> BECAUSE it is anchor-invariant it CANNOT reproduce the empirical `c_3`, which
> swings 2.43 %.** An anchor-invariant candidate matches the empirical value at
> **at most one** anchor; here it matches at NEITHER.

This is **scope-(a)**: "this construction, alone, does not reproduce the empirical
`c_3` as-is." It is not scope-(b) (no new structural exclusion — KC20 already
supplies the Lean-proved exclusion of the real-q class).

The falsification is now a **sorry-free Lean theorem**
([`QOU.Mass.QbetaC3DMCubic`](../../content/quantum-observable-universe/lean/QOU/Mass/QbetaC3DMCubic.lean),
verified `lean`-direct exit 0):

* `dmCubic3jet_cannot_match_both_anchors` — an anchor-invariant candidate that
  value-matches empirical at both anchors forces `empP = empM`, contradicting the
  measured `empP ≠ empM`. So **no** anchor-invariant real-q candidate reproduces
  the empirical `c_3`.
* `dmCubic3jet_misses_other_anchor_by_full_swing` — matching one anchor leaves the
  other's residual **exactly** the full swing `empP − empM`.

The genuine OPEN target (per KC21/KC22) is recorded as a content-bearing primary
conjecture class `ResurgentBarOddC3` (no instance): the empirical `c_3` is the
`1/u³` image `empC3·u³ = smoothS` of a **smooth** bar-odd object `S = h·D(ũ)`
(`|S(substrate)| ≈ 0.0094`) — a **resurgent/transcendental** object (KC22), not a
real-q DM cubic. The Berezinian scaffold is structurally consistent with a bar-odd
cross-term but supplies no such derived closure.

## 6. Q_β 100× wiring implication

**Q_β does NOT meet its 100× target (7.8 ppb) via this route.** A derived `c_3`
that does not even near-match the empirical value at one anchor cannot bring the
`|c_3|·u³ ≈ 1240 ppb` gap under target; wiring the phase 3-jet (`+0.027`) would
move Q_β the WRONG way. The best real-q near-matches (`≈ −2` forms) reach ~6 ppb
at the proton anchor ONLY (registry §3); the DM-cubic/Berezinian derivation
reaches neither. Nothing is wired; the honest production state stays **c_2-only,
~0.17 % (~1279 ppb) truncation residual** (registry §6).

## 7. Honesty checklist (§Axiomatization is NOT a Proof, §3b, registry §8)

- [x] `c_3` NOT inverted from Q_β to claim a derivation (that would be a FIT).
      The derived realizations are CODATA-independent; the CODATA-inverted value
      is used only as the comparison target.
- [x] No new `c_k` wired to production; no tier changed.
- [x] Negative labelled **scope-(a)** (construction insufficient alone), not
      scope-(b) — the only structural EXCLUSION cited (KC20) is pre-existing and
      Lean-proved.
- [x] Lean file content-bearing, sorry-free, conjecture class instance-free
      (honest open state); generic `[Ring R]`, no `ℝ`/ordering/`Real.*` (§7c).
- [x] Refuted-mechanism list checked before compute; task approach #1 pruned a
      priori by KC22 (formalize-first).
- [x] No appendix-mass-binding-algorithms change — no algorithm/compute wired;
      this is a negative probe.

## References

- Probe: [`qbeta_c3_dm_cubic_berezinian_probe.py`](../../computations/probes/qbeta_c3_dm_cubic_berezinian_probe.py)
  + `qbeta-c3-dm-cubic-berezinian-probe.witness.json`.
- Lean: [`QOU.Mass.QbetaC3DMCubic`](../../content/quantum-observable-universe/lean/QOU/Mass/QbetaC3DMCubic.lean).
- Scaffold: [`QOU.Brings.SuperDMBerezinian`](../../content/quantum-observable-universe/lean/QOU/Brings/SuperDMBerezinian.lean);
  [`2026-07-20-super-berezinian-dm-cubic-narrowing.md`](2026-07-20-super-berezinian-dm-cubic-narrowing.md).
- Registry (authoritative tier): [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
  §3 (rungs), §9 KC20 (real-q excluded), KC21 (`1/u³` smooth-zero), KC22
  (non-holonomic/resurgent).
- `[donagi1997swintegrable]` alg-geom/9705010; `[donagi-markman1996cubics]`
  alg-geom/9408004 §1.
