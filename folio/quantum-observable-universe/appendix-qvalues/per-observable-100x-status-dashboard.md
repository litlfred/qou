**Remark (per-observable $100\times$ experimental status).**

*The per-observable accuracy record is the witness `computations/per-observable-100x-status.witness.json`, emitted by `per_observable_100x_status.py`. It records, for each predicted observable, whether the prediction meets its $100\times$ absolute-accuracy target against experiment. Its `summary` field carries the headline counts. **The accuracy result is `beats_100x_scoreable` out of `scoreable_total`**, which count predictions only. `beats_100x_count` must *not* be quoted as an accuracy result: it also counts the calibration inputs the witness lists in `summary.calibration_inputs`, whose residuals are fixed by construction rather than measured. The remainder do not meet the target, and closing them is open.*

**Target.** For each predicted observable $O$ with experimental
uncertainty $\sigma_{\mathrm{exp}}(O)$, the $100\times$ target is
$\sigma_{\mathrm{pred}}(O) \leq \sigma_{\mathrm{exp}}(O) / 100$.

**Current status.** Numbers are not inlined here, because they change as the
predictions are sharpened; the authoritative values are the witness's per-row
`pred_err`, `100x_target` and `beats_100x` flags, together with the `summary`
counts `beats_100x_scoreable` / `scoreable_total`. The witness is recomputed whenever its upstream inputs change — the
per-observable comparison values are read from the production witness for each
anchor — so it does not go stale silently.

**Scope of the target.** The $100\times$ target is one of two accuracy
sub-goals, both measuring absolute accuracy against experiment. Both are
distinct from the separate requirement of internal compute agreement, and both
are bounded below by the CAL-2 calibration floor: no prediction can be sharper
than the calibration it rests on.
