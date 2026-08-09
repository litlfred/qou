# q₀ pin coverage: +165 checkable witnesses — and the manifest is configuration, not documentation (2026-08-08)

**Tier:** infrastructure audit + coverage extension · **Wired:** manifest entries only,
all behaviourally inert · **No fit.**
Producer: [`q0_producer_pin_classifier.py`](../../computations/audits/q0_producer_pin_classifier.py).
Follows [`2026-08-08-q0-declared-vs-recorded-sweep.md`](2026-08-08-q0-declared-vs-recorded-sweep.md).

---

## 1. The correction that governs this whole exercise

The declared-vs-recorded sweep closed by recommending: *"extending the manifest
is what converts `UNDETERMINED` into a verdict."* That framing treats
`q0_anchor_manifest.json` as a passive registry. **It is not.**

`computations/substrate/q_parameter.py` reads the manifest at import time and
applies the **muon** anchor when the running producer's stem is listed under
`ideal_muon`:

```python
_stem = _MP(_sys.argv[0]).stem if (_sys.argv and _sys.argv[0]) else ""
if _stem in _man.get("ideal_muon", []):
    _anchor = "ideal"
```

So the manifest is a **control input**:

- adding a stem to `ideal_muon` **re-pins that producer to muon** — a live
  numerical change, not a note about one;
- adding a stem to `physical_proton` is **inert**, since anything not in
  `ideal_muon` already resolves to proton.

The first version of this classifier ignored that and proposed **26
`ideal_muon` additions**. Applying it would have silently re-pinned 26
producers — changing their outputs while claiming to document them. The
proposal now emits `physical_proton` only, and an assertion at the apply step
refuses any proposal containing another key. That assertion fired on a stale
proposal file during this session and did its job.

This also revises the earlier sweep's closing advice: *"each producer added
brings its witnesses under both audits"* is true only in the proton direction.
Muon declarations are per-producer decisions and belong to the `tnjb`
migration.

## 2. Coverage

Applied: **44 `physical_proton` entries**, each one where the producer resolves
to proton today **and** its witness already records `proton` — so the entry
asserts nothing new about the value, it only makes the pairing checkable.

```
                    before      after
checkable              309        474      (+165 witnesses)
undeterminable         266        101      (−165)
unpinned              2477       2478
DECL_MISMATCH            1          0
```

Verified inert: no proposed stem appears in `ideal_muon` (asserted at apply
time), so `q_parameter` resolves identically before and after. Substrate suite
33 passed; the label-vs-value audit still reports `Q0_FLIP: 0`.

## 3. `qou-pin1` resolved

`chi-deuteron-h6.witness.json` recorded `proton` while
`per_irrep_pole_deuteron_h6.py` was declared `ideal_muon`. Traced the full
chain — `canonical_braid_crossings`, `hoefsmit_symbolic`,
`per_irrep_pole_proton_h3` — and it is **purely symbolic**: module-level
`Q = sp.symbols('q', positive=True)`, and the one numeric import
(`from q_parameter import Q as q_num`) lives inside `hoefsmit_symbolic`'s
`if __name__ == "__main__"` self-test, unreachable from any import path.

So neither label was meaningful. Resolution: stem moved `ideal_muon → ambiguous`,
and the spurious `q0Anchor`/`q0Value` dropped from the witness.

**Note this was a live re-pin, and safe only by inspection.** Removing the stem
from `ideal_muon` changes what `q_parameter` would serve that producer — it is
inert here *only because the producer never imports `q_parameter` outside its
self-test*. That check was the precondition, not a formality.

That `__main__` exclusion is now a rule in the classifier: without it,
`hoefsmit_symbolic` classifies as proton-pinned, which is the same misreading
that put the spurious stamp on the witness in the first place.

## 4. What the classifier found beyond the proposal

| class | count | disposition |
|---|---:|---|
| resolves proton, witness agrees | 44 | **applied** |
| resolves muon, witness agrees | 26 | **not applied** — an `ideal_muon` entry re-pins; decision, not sweep |
| resolves proton today, witness says muon | 46 | stale stamps; regeneration would move the value. `tnjb` scope |
| reads **both** layers | 13 | bean `qou-pin2` — 8 with hard code evidence |
| no numeric q₀ (symbolic) | 13 | left undeclared; `none` is not evidence of `ambiguous` |
| producer not found | 1 | — |

**The 46 "resolves proton today, witness says muon"** are the same shape as the
`qbeta-ck-cache` defect: the producer would compute proton now, but the witness
carries a muon label preserved from before the re-pin. They are *not* fixed
here — each is a value that would move on regeneration, which is exactly the
`tnjb` sweep that still needs its scoped sign-off.

**The 13 both-layer readers** are the more interesting find: a stem-resolved
`q₀` *and* a muon artifact inside one producer. Three are stamped `proton`
while reading muon-layer data — including `delta_lambda_fr_identity_phase5c.py`,
which reads `y-lambda-at-q0.witness.json`, the exact accessor AGENTS.md flags as
reaching an experimental-layer caller with no signal that a boundary was
crossed. Filed as `qou-pin2` with per-producer evidence; not fixed, because each
needs a layer decision.

## 5. Honest limits

- **String matching does not distinguish a docstring from a live path.** Five of
  the 13 both-layer hits are likely false positives that merely *mention* a muon
  artifact in prose — `y_lambda_at_q0_cache.py` most obviously, since naming its
  own output is not a straddle. Recorded in the bean rather than presented as 13
  defects. Tightening to "strings reaching an `open`/`load_witness` call" is the
  obvious follow-up.
- **`none` is not proposed as `ambiguous`.** A producer with no numeric q₀ in
  the code this analyser reads may still have a pin expressed some other way.
- **101 witnesses remain undeterminable**, down from 266. Closing the rest needs
  either muon declarations (decisions) or producer-by-producer reading.
- **Nothing here validates a value.** Coverage means a mismatch would now be
  *detected*; it does not mean the 474 are correct.
