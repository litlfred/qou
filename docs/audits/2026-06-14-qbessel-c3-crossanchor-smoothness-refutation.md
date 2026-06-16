# q-Bessel `c_3` cross-anchor closure — smoothness refutation (2026-06-14)

## Status: read-only formalize-first wire-check → REFUTED (real `x`)

Closes the one open gate that PR #2279 (q-Bessel identification of the Reeb-phase
objects) left standing:

> *"any `c_3` reproduction stays near-match until the cross-anchor gate passes
> with a substrate-fixed `x`."* — PR #2279 discipline note.

**Verdict: that gate cannot pass for any real `x`.** A substrate-fixed real
amplitude in the bar-odd Hahn–Exton / Jacobi–Anger object `sinh(x·sinh η)`
(`η = log q₀`) is refuted as a `c_3` residue-A cross-anchor closed form by the
**same smoothness bound** that killed the real-`q` `c_3` family (PR #1821) and
the fixed-ℓ `sinh(ℓη)/u^k` f-map (PR #1887 swing-lock). No scan was run — a
one-line structural bound prunes the whole real-`x` class (formalize-first).

- **Probe:** [`computations/qbeta/qbeta_qbessel_crossanchor_smoothness_refutation.py`](../../computations/qbeta/qbeta_qbessel_crossanchor_smoothness_refutation.py)
  → `qbeta-qbessel-crossanchor-smoothness-refutation.witness.json` (5/5 assertions, 50 dps).

## The argument

The proton-pinned and muon-pinned substrate anchors are the **same `q₀` to seven
significant figures** — they are two slightly different *calibrations* of the one
substrate, differing only in the 8th decimal:

| anchor | `q₀` | source |
|---|---|---|
| proton-pin | `1.10997858275138…` | `qbeta_chain4_kashiwara_step3_cross_anchor.py` |
| muon-pin | `1.10997859555418…` | same |
| **Δq₀** | **`1.2803e-8`** (rel `1.15e-8`) | |

yet the CAL-anchored `c_3` differs by ~2.9 %:

| anchor | `c_3` | source |
|---|---|---|
| proton-pin | `−2.0693` | `qbeta_eigenphase_taylor_in_u.py` (`C3_EMP_MP`) |
| muon-pin | `−2.0097` | same (`C3_EMP_MUON`, authoritative) |

So the empirical slope is

$$\frac{dc_3}{dq_0} \;\approx\; \frac{-2.0097 - (-2.0693)}{1.28\times10^{-8}} \;\approx\; 4.66\times10^{6},$$

which is exactly the `≈ 4.6e6` smoothness wall recorded in CLAUDE.md from PR #1821.

Any candidate `c_3(η) = K·\sinh(x\,\sinh\eta)` with a **fixed** real `x` is a
*smooth* real function of `η = log q₀`; its cross-anchor relative swing is

$$\frac{\Delta c_3}{c_3}\;\approx\;\coth(x\sinh\eta)\,\cdot\,x\cosh\eta\,\cdot\,\frac{\Delta q_0}{q_0}\qquad(\star)$$

with `K` cancelling. This is a **zero-parameter** test once `x` is pinned.

### Forward (pin `x`, predict the swing)

Pinning `x` at any physical brane-tower scale — `x ∈ {1, 1/\sqrt u, 1/u} ≈ {1,
10.8, 117.4}`, where `u = b·ℏ_q² ≈ 0.00852` and `1/u ≈ 117.4` is the q-difference
pole the q-Bessel recurrence reproduces (`qbeta_qbessel_contiguity_cfinite.py`) —
gives:

| pinned `x` | predicted swing | observed / predicted |
|---|---:|---:|
| `1` | `1.11e-7` | `2.6e5×` |
| `1/√u ≈ 10.8` | `1.55e-7` | `1.9e5×` |
| `1/u ≈ 117.4` | `1.36e-6` | `2.1e4×` |

Every physical-scale `x` **under-predicts the observed `2.9e-2` swing by ≥ 2×10⁴**.

### Dual (match the slope, read off `x`)

Solving `(★)` for the `x` that *would* reproduce the observed slope gives

$$x \approx 2.5\times10^{6}\quad\Rightarrow\quad x\sinh\eta \approx 2.6\times10^{5},$$

i.e. the Jacobi–Anger argument is deep in the asymptotic-oscillatory regime where
the "first few `J_{2m+1}(x)`" truncation PR #2279 uses is meaningless, and `x` is
five orders of magnitude past the `O(117)` tower scale. Physically absurd. (The
verdict is robust to the muon-value discrepancy in the corpus: the scope-doc Φ₂
value `−2.0202` gives slope `3.84e6`, required `x ≈ 2.0e6` — same conclusion.)

## What this does and does NOT say

- **It does not contradict PR #2279.** #2279 identifies the home-grown Reeb-phase
  / Markov-trace objects as the standard q-special functions of `SU_q(2)`
  (Hahn–Exton q-Bessel = `E_q(2)` matrix coefficients; Vaksman–Korogodsky 1989,
  Koelink 1994) **at the fibre / formal-`q` level**, and explicitly claims *no*
  `c_3` closure. This probe **confirms** that caution and retires the open gate
  with a clean negative.
- **It is the forward complement of the Im(q) rule** (CLAUDE.md "Im(q) at fibre
  vs observable level"): a real-`x` q-Bessel is an *archimedean* object
  (`Im(q₀)=0`) and inherits the #1821 smoothness obstruction. The genuine
  resolution lives in the **fibre** — a Habiro element whose *per-anchor*
  archimedean evaluation reproduces `c_3` at that anchor — not in a real
  `f(q₀_real)`.
- **Net for the program:** this retires the speculative `c_3`-via-real-q-Bessel
  upside, parallel to how [PR #2294](https://github.com/litlfred/qou/pull/2294)
  retired the q-Bessel *binding* upside (joint J⊕I combiner, NO-GO). Both leave
  #2279 standing as clean exposition + fibre structure. The productive `c_3`
  direction remains the **fibre-level Q_β Habiro element** (the α_EM
  `[2]_q·(1−h²α)` template), per
  [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).

## Discipline

Three-calibration; **no 7th fit** (zero free parameters — `x` pinned, `K`
cancels); derive-or-refute; TIERED; `c_3` stays cal-anchored; nothing wired to
production.

## Cross-refs

- PR **#2279** (q-Bessel identification — the gate this closes): `docs/audits/2026-06-13-reeb-phase-qbessel-identification.md`.
- PR **#2294** (q-Bessel binding NO-GO — sibling retirement): `docs/audits/2026-06-14-qbessel-joint-ji-binding-probe.md`.
- PR **#1821** (real-`q` `c_3` family killed by the same `dc_3/dq ≈ 4.6e6` bound).
- PR **#1887** (fixed-ℓ `sinh(ℓη)/u^k` f-map swing-lock refutation).
- Scope: [`2026-06-05-qbeta-perblock-collapse-order-scope.md`](../scope/2026-06-05-qbeta-perblock-collapse-order-scope.md) (the "Bessel-like, no single ℓ" survivor).
- Canonical `c_k` framing: [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
