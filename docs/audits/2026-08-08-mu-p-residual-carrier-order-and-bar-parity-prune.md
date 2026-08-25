# The μ–p residual on the muon carrier: order window, bar-parity rule, and why the datum cannot identify a closure

**Date:** 2026-08-08
**Bean:** [`qou-6gf9`](../../.beans/qou-6gf9--class-i-derive-a-correction-to-m-mum-e-vol4-1hbar.md)
**Branch:** `claude/6gf9-mu-p-residual-carrier-2026-08-08`
**Probe:** [`scripts/mu_p_carrier_order_window_probe.py`](scripts/mu_p_carrier_order_window_probe.py) (self-contained, proton pin only)
**Lean:** [`QOU/BraidKnot/MuPCarrierBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MuPCarrierBarParity.lean)
(generic `[Field K]`) + [`QOU/BraidKnot/MuPCarrierOrderWindow.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MuPCarrierOrderWindow.lean)
(archimedean; split per §7c on the `scripts/check-sidecars.sh` flag).
**Verification:** `scripts/lean-direct-cone.sh QOU.BraidKnot.MuPCarrierOrderWindow`
builds the real 4-module import cone, exit 0; `scripts/lean-verify.sh` exit 0 on both
files; 0 sorries; `#print axioms` on all **11** declarations returns exactly
`[propext, Classical.choice, Quot.sound]` — no `sorryAx`. (CI is unavailable
repo-wide, so this agent-side verification is the gate.)

**Verdict: NOT CLOSED.** No correction is derived and nothing is wired. What
landed is three prunes that bound the front, plus one concrete defect found in
the corpus's own m_μ closure. An honest negative, per AGENTS.md §"When you
can't close it".

## 0. Scope, and the q₀ gate

The **muon carrier** is `m_μ/m_e = Vol(4₁)/ℏ_q²`. The question asked was whether
that carrier is only the leading term of a series whose first correction is the
~11.5 ppb μ–p residual.

This route **does not derive `q₀`** and therefore does not touch the permanent
2026-08-02 owner gate (bean `qou-eic1`). It corrects a *mass-ratio relation at
fixed `q₀`*: `q₀` is read from the package constant and held fixed throughout;
every quantity computed below is a function of that fixed `q₀`. Confirmed
explicitly, as required.

**Pin discipline.** Everything is at the **experimental (proton) pin**,
`q₀ = 1.109978582751380807591669` (`qou_substrate.constants.Q_50_DIGIT_STR`),
per the 2026-08-07 owner directive. The probe reads no `computations/` witness
and no muon-built cache, so there is no ideal/experimental layer straddle — a
straddle here would itself be an 11.5 ppb error, i.e. exactly the size of the
object under study (`2026-08-07-mu3-door-status-consolidated.md` §4ter).

**Distinct angle.** Sibling work on this front runs the `Q_β` `c_k` ladder and
the `F_Bor` `c₄` dressing. This attack is on the muon carrier itself. It
consequently touches **neither `F_Bor` nor the Borromean Markov trace**, so it
has no exposure to the unconfirmed 6.7 % `tr_M_atomic` convention gap being
investigated under `qou-3qrv`.

## 1. What was already known (corpus-grep, run first)

| Source | Established |
|---|---|
| [`2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md) | The tension is 11.5 ppb in `q₀` ≈ 240 ppb in `m_p` ≈ 210 ppb in `m_μ`; anything closed below that floor against CODATA is noise. |
| [`2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md) | `c₄` is *exactly affine* in the pin offset (0 at proton, 46.04 at muon) — `c₄` **is** the tension, not a closure of it. At the proton pin the production `c₄` is 0 and the tension surfaces entirely as the m_μ prediction. |
| [`2026-06-20-keystone-branching-shift-first-crack.md`](2026-06-20-keystone-branching-shift-first-crack.md) §Consequence | Any sub-ppm correction candidate **must be argued bar-even** (from 4₁ amphichirality). Classical-multiplicity branching is null. |
| [`2026-06-22-keystone-qdeform-projector-shift.md`](2026-06-22-keystone-qdeform-projector-shift.md) | The q-deformed projector-weight shift gives `δ = 0.2074961`, 6–7 orders too large, **and bar-MIXED** — disqualified on parity as well as magnitude. |
| [`2026-08-01-mu-p-tension-attack-recon-floor-verdict.md`](2026-08-01-mu-p-tension-attack-recon-floor-verdict.md) | Markov-trace surface exhausted; only the Σ(2,3,5) WRT / s5-so3 route survives; `MmuR9V9Closure.lean` is labelled NEAR-MATCH-NOT-DERIVED. |

So the front already carried a **magnitude** constraint and a **parity**
precondition. What it did not carry — and what this audit adds — is the
*order* structure, the *entropy* accounting, and the observation that the
parity precondition **also disqualifies the corpus's own m_μ closure**.

## 2. The datum, measured

At the proton pin (probe, 60 dps):

| quantity | value |
|---|---|
| `ℏ_q = 1 − q₀⁻¹` | `0.09908171604425850783917712` |
| `Vol(4₁)` | `2.029883212819307` (cross-checked against `2·Im Li₂(e^{iπ/3})`) |
| `m_μ/m_e` predicted | `206.76832637067386482` |
| `m_μ/m_e` CODATA | `206.7682830` |
| residual | **`+209.755 ppb` = 9.534 σ** |
| required correction `t` (carrier·(1−t) = CODATA) | **`t = 2.09754920524e-7`** |
| `σ_exp / t` | **10.49 %** |

## 3. Prune 1 — the order window (Lean-proved)

If the correction is a monomial `t = |c|·ℏ_q^k` with a **small-height**
coefficient `|c| ∈ [1/5, 5]`, the measured `t` forces `k ∈ {6, 7}`:

```
 k | ℏ_q^k        | c_k = t / ℏ_q^k | admissible?
 1 | 9.9082e-2    | 2.1170e-6       | no  (5 orders too small a coefficient)
 …
 5 | 9.5492e-6    | 2.1966e-2       | no
 6 | 9.4615e-7    | 0.2216925195    | YES
 7 | 9.3746e-8    | 2.237471537     | YES
 8 | 9.2886e-9    | 22.582          | no
```

Formalized as `MuPCarrierOrderWindow.order_window` (ℝ; genuinely archimedean, so
`ℝ` is correct per §7c). Orders `k ≤ 5` give at least `0.098⁵/5 ≈ 1.81e-6`, over
7.5× the top of the window; orders `k ≥ 8` give at most `5·0.1⁸ = 5e-8`, under
0.28× the bottom.

**Immediate corollary — the Ohtsuki / volume-conjecture route is pruned.** The
natural reading of "`Vol(4₁)` is the leading term of a series" is the Ohtsuki
asymptotic expansion of the 4₁ Kashaev invariant, whose coefficients are known
O(1) rationals over `√−3`. A 1-loop term would enter at `k = 1` and overshoot
by **4.7 × 10⁵×**; 2-loop at `k = 2` overshoots by **4.7 × 10⁴×**. The residual
is not a low-loop correction to the volume conjecture.

**Scope: (b), relative to the stated hypothesis class** — monomials in `ℏ_q`
with a small-height coefficient. Named invariant: the magnitude bound. It
excludes nothing outside that class.

**What is deliberately NOT claimed.** The tighter class `|c| ∈ [1/2, 2]`
("the correction is `±ℏ_q^k` up to a factor of two") is empty at the *central*
value — `c₆ = 0.2217`, `c₇ = 2.2375`, both outside `[1/2, 2]` — but at the −1σ
edge `c₇` falls to **2.003**, exactly on the boundary. That exclusion is
knife-edge and is not formalized. Recording it as a non-claim, not a result.

**Honesty caveat: "order" is not an invariant of the residual.** It depends on
which deformation parameter you expand in:

| parameter | value at q₀ | order of `t` |
|---|---|---|
| `ℏ_q = 1 − q⁻¹` | 0.09908171604 | 6.65164 |
| `ℏ_q²` | 0.009817186454 | 3.32582 |
| `w = [2]_q − 2` (bar-even) | 0.01089686671 | 3.40261 |
| `(q − q⁻¹)²` (bar-even) | 0.04370620853 | 4.91247 |
| `ln q` | 0.1043407203 | 6.80384 |

So "the order is non-integer" is only meaningful once a parameter is declared.
The invariant content is the *entropy* bound (§5) and the *parity* rule (§4).

## 4. Prune 2 — the bar-parity selection rule (Lean-proved), and a defect it exposes

Under the bar involution `q ↦ q⁻¹` the substrate is **not** fixed:

```
ℏ_{q⁻¹} = 1 − q = −q·ℏ_q                      (MuPCarrier.hbarGen_bar)
```

Hence `bar(ℏ_q^k · q^m) = (−1)^k q^{k−m} ℏ_q^k`, which equals `ℏ_q^k q^m` for
all `q` exactly when `k` is even and `m = k/2`. So:

> **The bar-even part of the `ℏ_q`-monomial family is precisely the tower of**
> `w := q·ℏ_q² = q + q⁻¹ − 2 = [2]_q − 2`.

Proved as `hbarGen_pow_two_mul_eq_wGen_pow` (`ℏ_q^{2j}·q^j = w^j`) plus
`wGen_bar` (`w_{q⁻¹} = w_q`), giving `hbarGen_monomial_bar_even`. All generic
over `{K : Type*} [Field K]` — no archimedean content, per §7c.

### 4a. The corpus's own m_μ closure fails this precondition

`MmuR9V9Closure.lean` carries the NEAR-MATCH m_μ rungs

```
δ_R9 = ℏ_q⁶ · q / 5          (k=6, m=1 — needs m=3)
δ_V9 = ℏ_q⁸ · [3]_q / 25     (k=8, [3]_q is bar-even — needs a q⁴ dressing)
```

Neither has `m = k/2`, so **both are bar-mixed**. Proved in Lean *against the
production definitions themselves* (the file imports `MmuR9V9Closure`):

- `MuPCarrierOrderWindow.delta_R9_not_bar_even` — witness `q = 2`: `δ_R9(1/2) = 1/10` vs `δ_R9(2) = 1/160`.
- `MuPCarrierOrderWindow.delta_V9_not_bar_even` — witness `q = 2`: `δ_V9(1/2) = 21/100` vs `δ_V9(2) = 21/25600`.

At the pin the violation is not marginal: the probe measures
`δ_R9(1/q₀)/δ_R9(q₀) = 1.5180` and `δ_V9(1/q₀)/δ_V9(q₀) = 2.3042`.

**This is a new finding.** The recon verdict flagged `MmuR9V9Closure` as a
sub-floor *fit*; it is additionally **disqualified by the same bar-even
precondition that killed the projector shift** — the corpus applied that
precondition to the projector-weight candidate but never to its own closure.

**Scope.** The bar-*mixedness* is proved unconditionally. The *exclusion* it
licenses is **conditional** on the bar-even precondition, which is *argued* in
`2026-06-20-…-first-crack.md` §Consequence from 4₁ amphichirality — it is not a
proved theorem. Per AGENTS.md §"Conditional-proved ≠ premise-established", the
premise is not hereby established. If the precondition were dropped, so is this
exclusion (but §5 still applies).

### 4b. The bar-even tower has no admissible order either

Combining prunes 1 and 2: the correction should be `c·w^j`. It is not, for any
small-height `c`:

```
 j |  w^j          | c = t / w^j   | in [1/5,5]?
 1 |  1.0897e-2    | 1.9249e-5     | no
 2 |  1.1874e-4    | 1.7665e-3     | no
 3 |  1.2939e-6    | 0.162109043   | no  (just under 1/5)
 4 |  1.4100e-8    | 14.877        | no  (just over 5)
```

Order in `w` is 3.4026 — the residual straddles `w³` and `w⁴` with no
small-height coefficient at either. **Admissible `j`: none.**

## 5. Prune 3 — the entropy bound: this datum cannot identify a closure

`σ_exp/t = 10.49 %`, so **`t` is a 0.98-significant-digit datum.** The
experimentally indistinguishable order-6 coefficient window is
`c ∈ [0.19844, 0.24494]`, **21 % wide**. Every one of twelve hand-listed
small-height "categorical-looking" constants lands inside it:

```
1/(4q₀²)=0.20291   0.2075 (the REFUTED projector δ)   [3]_q/(7[2]_q)=0.21623
q₀/5=0.22200 (the R9 fit)   2/9=0.22222   [2]_q/9=0.22343
1/(2√5)=0.22361 (icosahedral)   π/14=0.22440   9/40=0.22500   Vol(4₁)/9=0.22554
```

The presence of `0.2075` in that list is the punchline: the coefficient of a
mechanism the corpus **already refuted** is indistinguishable from the target.

**Therefore: matching a closed form to `t` carries essentially no evidential
weight.** This is the μ–p analogue of the PSLQ entropy bound that killed the
12-constant `α_EM` basis (PR #1805) and the `c₄ ≈ 46` identification
(`2026-07-04` §"The precision (entropy) bound…"). Only a coefficient
**predicted a priori** — before looking at `t` — can count as a derivation.

### 5a. Consequence: `δ_V9` is unfalsifiable decoration, and makes m_μ worse

| quantity | value | as % of `t` |
|---|---|---|
| `t` | `2.09755e-7` | 100 % |
| `δ_R9 = ℏ_q⁶q/5` | `2.100418e-7` | 100.14 % |
| `δ_V9 = ℏ_q⁸[3]_q/25` | `1.130865e-9` | 0.539 % |
| `σ_exp` on `t` | `2.200e-8` | **10.49 %** |

`δ_V9` sits **19.45× below the experimental resolution of the datum it
purports to close.** And at the proton pin the two rungs together *over*-correct:
`R9` alone leaves **−0.287 ppb**, `R9 + V9` leaves **−1.418 ppb** — five times
worse. The file's headline "0.036× L2 miss" is not reproducible at the
documented proton pin with CODATA `206.7682830`; it is in any case a number
quoted far inside the ±22 ppb uncertainty of its own input.

**Recommended follow-up (not done here, no scope):** relabel the
`MmuR9V9Closure` m_μ rungs to record (i) bar-mixedness and (ii) sub-resolution
`δ_V9`, and re-measure the quoted L2 miss at the documented pin. Filed as a
note on the bean rather than actioned, to keep this branch to its stated scope.

## 6. What survives

The hypothesis class is now bounded from three sides. A candidate correction
must simultaneously:

1. be **bar-even** — hence live in the `w = [2]_q − 2` tower, or carry its own
   compensating `q`-dressing (§4);
2. land at `ℏ_q`-order 6–7 equivalently `w`-order between 3 and 4 (§3, §4b) —
   note **no** integer order in either parameter admits a small-height
   coefficient, so a pure monomial is excluded and the correction must be a
   *sum* or carry a genuinely non-unit-height coefficient;
3. have its coefficient **fixed before the fact**, since the datum supplies
   under one significant digit (§5).

Requirement 2 is the sharpest new constraint: it says the object is not a
single clean monomial in any of the natural deformation parameters. The
surviving un-refuted route named by the recon verdict — the Σ(2,3,5) WRT /
s5-so3 Habiro series (bean `s5bb`) — is untouched by anything here, and is the
only route that could satisfy requirement 3, because its coefficients are fixed
by quantum topology rather than chosen.

## 7. Anti-recurrence

- Do **not** re-propose an `ℏ_q^k` monomial correction at `k ≤ 5` or `k ≥ 8`
  (§3), nor a 1-/2-loop volume-conjecture term (§3).
- Do **not** re-propose a bar-mixed rung of the `ℏ_q^k q^m`, `m ≠ k/2` shape
  (§4) — that includes the existing `δ_R9`/`δ_V9`.
- Do **not** report a match of a small-height constant to `t` as evidence
  (§5); twelve of them fit. State the a-priori derivation or state the gap.
- Do **not** quote an m_μ closure accurate to better than ~22 ppb as a win
  (§5a): that is inside the input's own error bar.

## Cross-references

- [`2026-08-01-mu-p-tension-attack-recon-floor-verdict.md`](2026-08-01-mu-p-tension-attack-recon-floor-verdict.md) — the front's standing verdict; this audit sharpens §3 and §4 of it.
- [`2026-06-22-keystone-qdeform-projector-shift.md`](2026-06-22-keystone-qdeform-projector-shift.md) — where the bar-even precondition was last applied.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the surviving route.
- [`content/quantum-observable-universe/lean/QOU/BraidKnot/MmuR9V9Closure.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MmuR9V9Closure.lean) — the closure examined in §4a / §5a.
