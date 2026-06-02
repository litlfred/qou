**Algorithm (Witness-JSON pipeline).**
*Cross-language interchange contract for every `*.witness.json`
emitted by a canonical compute script. Maintained as a sidecar to
the canonical chain because every chain step's
`computation.witness` field points to a file that conforms to
this contract.*

### Required JSON shape (top-level)

```json
{
  "schema_version": "1.x",
  "script": "folio-assistant/computations/<name>.py",
  "script_sha256": "<digest>",
  "engine": "python+mpmath",
  "parameters": { … },
  "inputs": { … },
  "outputs": { … },
  "assertions": [
    { "name": "1ppQ_cross_method", "status": "pass", "delta": "..." }
  ],
  "timestamp_utc": "YYYY-MM-DDTHH:MM:SSZ"
}
```

### Precision discipline

- Default compute: **65 dps** mpmath.
- Default serialisation: **50 dps** (truncation at $10^{-50}$
  absolute; smaller values rounded to zero).
- Cross-method assertion at $\leq 10^{-15}$ relative agreement
  (L1 — internal compute precision).

### LP/SDP duals

*If the compute is LP / SDP / operator-selection, the witness
**must** additionally carry the fields specified in
[`alg:lp-sdp-dual-emission`](#alg:lp-sdp-dual-emission).*

### Wedderburn-respecting witnesses

*Every per-partition computation (Step 5 and downstream Step 9b)
must emit the partition tag $\lambda$ alongside each value, so
the witness is partition-respecting and reviewers can audit the
isotypic structure.*

### Algorithm

```
1. Initialize WitnessBuilder(script=__file__, engine="…").
2. Record parameters, inputs.
3. For each computed output: builder.add_output(name, value,
   precision_dps=…, partition=λ_if_relevant).
4. For each assertion: builder.assert_(name, condition, delta).
5. builder.write(path)
```

### Correctness conditions

1. *The Wedderburn decomposition
   ([`prop:wedderburn-trace-identity`](#prop:wedderburn-trace-identity))
   defines the partition structure that the witness records.*
2. *The LP/SDP dual contract
   ([`prop:operator-selection-lp`](#prop:operator-selection-lp))
   defines the dual-emission fields used by Step 10.*

### Canonical entry point

```python
from qou_substrate.witness_builder import WitnessBuilder

w = WitnessBuilder(script=__file__, engine="python+mpmath")
w.add_output("tau_M", value, precision_dps=50)
w.assert_("1ppQ_cross_method", abs(a - b) < mp.mpf("1e-15"))
w.write("folio-assistant/computations/my-result.witness.json")
```

### Witness contract (meta)

*Every `*.witness.json` is itself audited by:
[`lp_dual_witness_validator.py`](../../../folio-assistant/computations/lp_dual_witness_validator.py)
(LP/SDP duals), `q-usage-watcher` (q-regime declarations), and
the q₀ staleness detector. Stale or schema-violating witnesses
fail CI in `witness-pipeline.yml`.*

### Notes

*Cross-language sibling: the
[`witness-schema`](../../../tools/witness-schema/) PyPI + npm
package provides Zod / Pydantic / TypeScript types for every
canonical witness shape, so Pyodide / Node / TS callers see the
same contract.*
