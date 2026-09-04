# The balanced-convention q-Plancherel gap, and the cross-atom variance it inflates

**Date:** 2026-09-04
**Bean:** `qou-7o7h`
**Producer:** [`computations/probe_plancherel_convention_gap.py`](../../computations/probe_plancherel_convention_gap.py) (3/3 assertions)
**Witness:** [`computations/probe-plancherel-convention-gap.witness.json`](../../computations/probe-plancherel-convention-gap.witness.json)
**Registry:** [`trace-convention-registry.md` §B-norm](../coordination/trace-convention-registry.md)

## 1. The claim

The textbook q-Plancherel weight

$$
w(\lambda) \;=\; \frac{d_q^2(\lambda)}{[n]_q!}
$$

is a probability measure at $q = 1$ and in the *asymmetric* q-integer
convention. It is **not** one in the **balanced** convention
$[k] = (q^k - q^{-k})/(q - q^{-1})$ — which is the convention this corpus's
`make_qdim` / `dim_q` family uses everywhere.

Measured at the proton $q_0$, `mp.dps = 60`:

| $n$ | $A$ | shapes | $c_n = \sum_\lambda d_q^2/[n]_q!$ |
|---|---|---|---|
| 6 | 2 | 11 | $0.99107952363735010$ |
| 9 | 3 | 30 | $1.11092313495739800$ |
| 12 | 4 | 77 | $1.51713321376785900$ |

The defect is not small, and — the part that matters — **it is not constant in
$n$.** Simple $q^{\pm 2n(\lambda)}$ and $q^{\pm(n(\lambda) - n(\lambda'))}$
prefactors were tried and do not close it.

## 2. Why it is a *cross-atom* artifact

Two facts compose:

1. **Exact proportionality.** $w_{\text{textbook}}(\lambda) = c_n \cdot
   w_{\text{self-norm}}(\lambda)$ for every $\lambda$, every $n$ — verified to
   $< 10^{-40}$ (witness assertion `textbook_equals_c_n_times_selfnormalized`).
2. **Linearity.** The depth-stratified functional
   $\Phi_k = \sum_{\lambda:\,\text{depth }k} w_\lambda \log(|\chi^\lambda|\,d_q\lambda)$,
   and hence $B = \sum_k \alpha_k(\Phi_k^{\text{free}} - \Phi_k^{\text{atom}})$,
   is linear in the weights.

Therefore $B$ scales by exactly $c_n$. Within a single atom the factor cancels
out of any ratio, so **per-atom** results are untouched. Across atoms it does
**not** cancel, because $n = 3A$ differs — the light series spans
$n = 6, 9, 9, 12$ and so three different $c_n$. Any metric that *compares*
atoms is distorted, and the max/min "variance" the FR-pullback probes are
scored on is exactly such a metric.

## 3. The measured consequence

Feeding the recorded self-normalized per-atom ratios through the scaling law:

| atom | $n$ | ratio (self-norm) | $\times c_n$ | ratio (textbook) |
|---|---|---|---|---|
| D | 6 | 0.2753 | 0.99108 | 0.27284 |
| T | 9 | 0.2980 | 1.11092 | 0.33106 |
| ³He | 9 | 0.3094 | 1.11092 | 0.34372 |
| ⁴He | 12 | 0.3276 | 1.51713 | 0.49701 |

$$
\text{max/min} \;=\; 1.8216 \qquad\text{(recorded textbook run: } 1.8217\text{)}
$$

against $1.1901$ self-normalized. The reconstruction agrees to
$5.5\times10^{-5}$ relative, and that residual is the four-significant-figure
rounding of the recorded ratios — nothing else.

**So the FR family's published $1.82\times$ baseline variance is
$1.5307\times$ inflated by the normalization alone.** The honest baseline is
$1.19\times$.

## 4. A trap, recorded because I fell into it twice

**(a) The inverted factor.** My first check of the scaling law *divided* by
$c_n$ instead of multiplying. That predicts $1.290$ against a recorded
$1.8217$, and I was one step from writing the whole mechanism off as
coincidence. The relation is $w_{\text{textbook}} = c_n\, w_{\text{self-norm}}$
— textbook weights are the *larger* ones at large $n$.

**(b) The shortcut identity.** It is tempting to notice

$$
\frac{1.8217}{1.1901} = 1.5307 \;\approx\; \frac{c_{12}}{c_6} = 1.5308
$$

and quote *that* as the mechanism. The identity is real, but it is
**conditional**: it holds only because the argmax atom (⁴He, largest $c_n$) and
the argmin atom (D, smallest $c_n$) are the same under both normalizations.
Change the atom set, or move a ratio enough to swap the argmax, and the
shortcut breaks while the scaling law still holds. **Quote the scaling law.**

Both traps share a shape worth naming: a numerical agreement at the third or
fourth digit is not a mechanism, and checking it the wrong way round can make a
real mechanism look like a coincidence just as easily as the reverse.

## 5. Scope — what this does *not* claim

This says **nothing** about which normalization is physically correct.
Self-normalizing is defensible (a probability measure by construction, and
convention-independent), but whether the depth-stratified functional should be
weighted by a probability measure *at all* is a separate question this does not
touch.

The claim is narrower and firmer: **the two choices differ by a known,
$n$-dependent factor, so figures computed under one are not comparable to
figures computed under the other — and the corpus currently contains both.**

- [`fr_pullback_k3_test.py`](../../computations/fr_pullback_k3_test.py) — textbook form
  (its $1.82\times$ baseline and $1.5015\times$ best-4₁ carry the distortion).
- [`fr_pullback_borromean_h3a_test.py`](../../computations/fr_pullback_borromean_h3a_test.py) —
  migrated to self-normalized 2026-09-03.

## 6. Caveats on the measurement itself

- The reconstruction's **inputs are read from a prior run**, not recomputed:
  recomputing them needs the ~25-minute $H_{12}$ character leg. The scaling law
  (§2, assertion 2) *is* computed from scratch and is what carries the finding;
  §3 is a consistency check on top of it.
- Those recorded ratios come from a run at the **retired muon-era pin A**,
  while $c_n$ here is computed at the current **proton** pin. The 11.5 ppb pin
  difference is ~7 orders below a 53 % effect and cannot affect the conclusion,
  but §3 is therefore a cross-pin comparison and its $5.5\times10^{-5}$
  residual must not be read as a precision claim.

## 7. RESOLVED — the k3-test re-run (added 2026-09-04, same day)

This section originally left open whether the k3-test's conclusions move under
the correction, on the grounds that it needed the re-run rather than an
argument. The re-run was done. **They move, in both directions.**

### 7.1 The ranking reverses

| knot | textbook (as published) | self-normalized |
|---|---|---|
| 4₁ | **1.5015** ← recorded "best" | 1.2425 |
| 5₂ | 1.5394 | 1.2911 |
| 6₁ | 1.6040 ← recorded "worst" | **1.0478** ← best |

The recorded verdict — *"paper's named K₃\* = 6₁ NOT validated; empirically best
= 4₁"* — is an artifact. The mechanism is visible per atom: the textbook form
inflates ⁴He (largest $n$) by $c_{12} = 1.517$ for **every** candidate, pinning
⁴He as the max and swamping the real spread. Corrected, 6₁'s four ratios are
tight: 0.3149 / 0.3169 / 0.3235 / 0.3300.

### 7.2 But the magnitude claim collapses

The published comparison was against a **hardcoded** `baseline = 1.82`, itself a
textbook-normalized figure. Computing the no-FR baseline through the same path
under the corrected measure gives **1.0660**:

| | max/min | vs computed baseline |
|---|---|---|
| no FR | 1.0660 | — |
| 4₁ | 1.2425 | **−16.6 %** (worse) |
| 5₂ | 1.2911 | **−21.1 %** (worse) |
| 6₁ | **1.0478** | **+1.7 %** |

So the headline "FR closes variance 1.82 → 1.05" was mostly the *baseline* being
inflated. The real FR effect at 6₁ is **1.7 %**, not 42 %.

### 7.3 What that leaves

- **Selectivity — strengthened.** 6₁ is best *and is the only candidate that
  improves on no-FR at all*; the other two make the cross-atom variance
  materially worse. That is a more discriminating outcome than the original
  test reported, and it favours the paper's naming.
- **Magnitude — collapsed.** A 1.7 % improvement is not the dramatic closure the
  old figures implied.

**Not claimed here: that the conjecture or the paper's naming is validated.**
This is one metric over three candidates. Whether "only the paper's knot helps,
and by 1.7 %" constitutes support is an interpretive call and it is the
author's.

**Guard against the obvious suspicion.** It would be reasonable to ask whether a
correction that happens to vindicate the paper's named knot was chosen for that
outcome. It was not: `c_n`, the exact `w_textbook = c_n·w_selfnorm` identity and
the scaling law were all derived and verified *before* the k3-test was run, and
the k3 outcome was unknown at that point. The scaling law was additionally
re-verified on the FR-redistributed weights (dev 3.5e-60), not merely the
uniform ones.

Producer: [`fr_pullback_k3_test.py`](../../computations/fr_pullback_k3_test.py)
(corrected in place); independent companion check:
[`probe_k3_selfnormalized_recheck.py`](../../computations/probe_k3_selfnormalized_recheck.py).

### 7.4 Three further defects found in the k3 producer while doing this

Recorded because two of them are the same failure mode, and one was mine:

1. **Float64 χ.** `q_f64 = float(Q0)` fed the f64 kernel, so every FR weight
   carried ~1e-16 rounding — a NO-FLOAT64 violation on a production path, hidden
   two frames from its use. Moved to `chi_lambda_braid_mpfr`.
2. **Hardcoded baseline** (`1.82`) — a literal from the old normalization, which
   straddles two normalizations once the weights are corrected. Now computed
   in-run.
3. **A verdict threshold calibrated to the old baseline** (`STRONG if best_mom <
   1.5`), which against a 1.066 baseline is satisfied by anything and graded a
   1.7 % improvement as "STRONG support". **This one I introduced by fixing
   (2).** Now grades by improvement relative to the baseline.

(2) and (3) are one lesson: **a literal or threshold calibrated against a
baseline does not survive that baseline moving**, and fixing the baseline is
exactly when it will silently mislead.
