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

## 7. What this does not resolve

Whether the FR-pullback verdicts change under the corrected normalization is
**not** settled here — the refuted-(a) verdict was already re-run
self-normalized on 2026-09-03 and stood, but the k3-test's own conclusions have
not been re-derived. That is left open rather than asserted either way; it needs
the k3-test re-run, not an argument.
