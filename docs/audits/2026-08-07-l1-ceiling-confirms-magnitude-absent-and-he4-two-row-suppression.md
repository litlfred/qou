# The magnitude is genuinely absent — and ⁴He's two-row sector is suppressed 29,000×

**Date:** 2026-08-07 · **Branch:** `claude/1ppq-l2-closure-attacks-ufrfun` · **PR #4664**
**Probe:** [`computations/binding_row_length_stratification.py`](../../computations/binding_row_length_stratification.py)
**Witness:** `binding-row-length-stratification.witness.json` · **Bean:** `qou-kemt`
**Follows:** [`…binding-is-three-row-dominated-hypothesis-refuted.md`](2026-08-07-binding-is-three-row-dominated-hypothesis-refuted.md)

`free_parameters = 0`. Committed 50-dps witnesses, stdlib `decimal` at 60 dps,
**no float64**. Audit-only; nothing wired.

---

## 0. Third independent validation of the implementation

| corpus ℓ¹-ceiling prune | this probe |
|---|---|
| D 0.52 · T 0.36 · ³He 0.59 · ⁴He 0.41 | **0.5161 · 0.3576 · 0.5918 · 0.4059** ✓ |

Together with the two earlier cross-checks (`B(D) = 0.380` → 0.3801; `C_knot = 5.852`
→ 5.8530), the probe now reproduces **three** independent committed corpus numbers.

---

## 1. Q1 — the magnitude is genuinely absent, not merely cancelling

The ℓ¹ norm `Σ_λ |y_λ χ^λ Δ_λ|` is the **absolute ceiling** on what any re-signing of
the existing terms could produce — it is what you would get with *perfect* constructive
interference.

| atom | A | `ℓ¹ / target` | `B_full` | **`B_ℓ¹ ceiling`** | `B_AME` |
|---|---|---:|---:|---:|---:|
| deuteron | 2 | 0.5161 | 0.3801 | **1.1480** | 2.2246 |
| tritium | 3 | 0.3576 | 1.9085 | **3.0328** | 8.4818 |
| ³He | 3 | 0.5918 | 2.3446 | **4.5677** | 7.7180 |
| ⁴He | 4 | 0.4059 | 3.0382 | **11.4852** | 28.2957 |

> **`ℓ¹ / target ∈ [0.36, 0.59] < 1` for all four.** Even with every sign chosen
> optimally and zero cancellation, the existing terms reach at most **59 %** of the AME
> target. **No re-signing, no re-weighting, and no `Δ_λ` re-derivation can close the
> deficit.** A genuinely *new additive* term is required — this is now a hard numerical
> statement, not an inference.

This independently confirms the corpus's ℓ¹-ceiling prune and extends it: that prune
established the point for the *sign* question; the same ceiling forecloses the
*magnitude* question over the whole existing term set.

**Scope, per AGENTS.md §"Before declaring refuted":** this is **scope-(a)** — it
excludes *this term set* from reaching the target by *any* reweighting. It is not a
structural exclusion of any ingredient. What it does exclude, firmly, is the entire
family of "find a better `Δ_λ`" attacks, which is where all six prior ansätze lived.

---

## 2. Q2 — where the ℓ¹ mass sits, and a 29,000× suppression at ⁴He

Per-stratum `ℓ¹` share and cancellation ratio `|Σ| / Σ|·|` (1 = fully coherent,
0 = total cancellation):

| ℓ(λ) | D share / cancel | T share / cancel | ³He share / cancel | ⁴He share / cancel |
|---|---|---|---|---|
| 2 | 82.6 % / 0.346 | 56.6 % / 0.425 | 65.4 % / 0.308 | 37.6 % / **0.0000345** |
| 3 | 13.0 % / 0.674 | 38.2 % / **0.979** | 29.8 % / **1.00000** | 37.5 % / 0.638 |
| 4 | 0.26 % / 0.142 | 4.33 % / 0.360 | 4.26 % / 0.358 | 21.0 % / 0.141 |
| 5 | 0.05 % / 1.000 | 0.66 % / 0.185 | 0.38 % / 0.230 | 3.03 % / 0.030 |

**Two structural facts:**

1. **The ⁴He two-row sector is suppressed by ~29,000×.** It carries `37.6 %` of the
   total ℓ¹ mass — **4.3196 MeV** — and its signed sum survives as **0.000149 MeV**.
   The same ratio at the other three isotopes is `0.31–0.42`, i.e. ordinary partial
   cancellation. **⁴He is four orders of magnitude more cancelled than its neighbours.**

2. **The 3-row sector is coherent where the 2-row sector is not.** At ³He the `ℓ(λ)=3`
   cancellation ratio is `1.00000` — *every term the same sign*, no cancellation at
   all — and at tritium it is `0.979`. The ≥3-body sector adds constructively; the
   pairwise sector interferes destructively.

### Honest reading of the ⁴He suppression — it is **not exact**

The signed sum is `−2.918×10⁻⁴` against an ℓ¹ of `8.4532`. Inputs are 50-dps, so a
*genuine* selection rule would show a residual near `10⁻⁵⁰`, not `10⁻⁴`. Therefore:

- ✅ **Strong suppression** — 29,000×, four orders beyond its neighbours, at the
  doubly-magic nucleus that is also the unique `A=4` Wigner-SU(4) `[1⁴]` singlet
  (`SU4SupermultipletGate.lean`). That coincidence is worth chasing.
- ❌ **Not a proved selection rule**, and **must not be reported as one**. It is an
  approximate cancellation at `q₀`. Possible readings: an exact identity at some
  nearby `q ≠ q₀`; an approximate symmetry of the ⁴He braid word; or an artifact of
  the averaged-crossing convention. **All three untested.**

Next test if pursued: evaluate the same two-row signed sum at several `q` and see
whether it crosses zero — an exact zero at `q ≠ q₀` would make this a real identity
rather than a coincidence.

---

## 3. Consequence for the arc

| question | status after this probe |
|---|---|
| Can a better `Δ_λ` close the deficit? | **No** — ℓ¹ ceiling ≤ 0.59 of target, all four |
| Can re-signing close it? | **No** — same ceiling (this is the ℓ¹ prune, reconfirmed) |
| Is the missing object additive-and-new? | **Required**, by elimination |
| Is the ≥3-body sector the coherent one? | **Yes** — `ℓ(λ)=3` cancels least (0.98–1.00) |
| Is ⁴He structurally special? | **Suggestive** — 29,000× two-row suppression, unverified |

The arc's remaining live question is unchanged in kind but sharper in form: the missing
term is **additive, new, and cannot be manufactured from the existing partition sum by
any weighting**. Everything this branch examined — normalization stripping, Ocneanu `N`,
extended Bloch, SU(4) Casimir, hypernuclei — is a candidate for *that* new term, and the
ℓ¹ ceiling is now the quantitative bar each must clear: it must supply **41–64 %** of
each target on its own.
