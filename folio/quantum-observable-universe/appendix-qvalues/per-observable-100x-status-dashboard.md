**Remark (per-observable $100\times$ experimental status).**

*The per-observable accuracy record states, for each predicted observable, whether the prediction meets its $100\times$ absolute-accuracy target against experiment, together with headline counts. **The accuracy result is the number of scoreable predictions meeting the target out of the number of scoreable predictions**, which count predictions only. A count that also includes the calibration inputs must *not* be quoted as an accuracy result: the residuals of those inputs are fixed by construction rather than measured. The remainder do not meet the target, and closing them is open.*

**Target.** For each predicted observable $O$ with experimental
uncertainty $\sigma_{\mathrm{exp}}(O)$, the $100\times$ target is
$\sigma_{\mathrm{pred}}(O) \leq \sigma_{\mathrm{exp}}(O) / 100$.

**Current status.** Numbers are not inlined here, because they change as the
predictions are sharpened; the authoritative values are the record's per-observable
prediction errors, targets and pass flags, together with the summary
count of scoreable predictions meeting the target. The record is recomputed whenever its upstream inputs change — the
per-observable comparison values are read from the production witness for each
anchor — so it does not go stale silently.

**Scope of the target.** The $100\times$ target is one of two accuracy
sub-goals, both measuring absolute accuracy against experiment. Both are
distinct from the separate requirement of internal compute agreement, and both
are bounded below by the CAL-2 calibration floor: no prediction can be sharper
than the calibration it rests on.
