# The q₀ flip detector cannot see the flip that happened (2026-08-08)

**Tier:** infrastructure audit + new sweep · **Wired:** nothing · **No fit.**
Producer: [`q0_declared_vs_recorded_sweep.py`](../../computations/audits/q0_declared_vs_recorded_sweep.py).
Companion to [`2026-08-08-qbeta-l2-anchor-straddle-guard.md`](2026-08-08-qbeta-l2-anchor-straddle-guard.md).

---

## 1. The blind spot

`computations/audits/q0_anchor_consistency_audit.py` is the corpus's flip
detector for bean `tnjb`. Its check, in its own words:

> *"This audit enforces that the recorded pin is **self-consistent**: a witness
> that claims `q0Anchor: "muon"` must carry the muon `q0Value`."*

That is a real check. It is also structurally unable to see the flip that
actually occurred. `qbeta-ck-cache.witness.json` carried `q0Anchor: "muon"` **and**
the muon `q0Value` — perfectly self-consistent, verdict `Q0_OK` — while the
producer computed at the **proton** pin. The Q_β prediction sat 30.4 ppb from
where its label said it was, and the corpus-wide run reported:

```
Q0_FLIP : 0
```

Self-consistency cannot detect a stamp that is internally coherent and
externally wrong. The missing axis is *recorded pin vs the pin the producer
actually runs at*.

## 2. The sweep

`q0_declared_vs_recorded_sweep.py` compares each witness's recorded `q0Anchor`
against its producer's **positively declared** pin.

"Positively declared" is load-bearing and narrow: an explicit `QOU_Q0_ANCHOR`
env var, or the producer's stem listed in `q0_anchor_manifest.json`. It
deliberately does **not** use `resolve_q0_anchor`'s return value alone — that
defaults to `"proton"` for every stem absent from the manifest (~470 producers),
so gating on it would flag legitimate muon witnesses wholesale. Undeclared
producers are reported as `UNDETERMINED`: a coverage gap, not a defect.

## 3. Result

```
witnesses scanned    : 3057
DECL_OK              :  309
DECL_MISMATCH        :    1
UNDETERMINED         :  266
NO_PIN               : 2477
NO_PRODUCER          :    1
PARSE_ERROR          :    3
```

**One contradiction**, and it is a *different* sub-class from the Q_β one:

```
computations/chi-deuteron-h6.witness.json
    recorded=proton but per_irrep_pole_deuteron_h6.py is declared muon
```

The producer appears to be purely **symbolic** — its only `.subs()` calls are
symbol→symbol, it never imports `q_parameter`, and the witness holds
`chi_lambda_symbolic` with an empty `data` block. If that reading holds, there is
no numeric q₀ in the artifact at all, so *both* labels assert a pin that does not
exist and the honest classification is `ambiguous`. Deliberately **not** resolved
here — reclassifying another agent's producer in a shared registry on the
strength of a grep is the kind of unilateral edit the coordination rules
discourage. Filed as bean `qou-pin1` with the evidence and the next step.

## 4. Reading the numbers honestly

**The corpus is in good shape on this axis.** One contradiction in 310 checkable
witnesses is a low rate, and it is not the Q_β-style numeric mislabel.

**But coverage is the real story.** Of 3057 witnesses, only **310** can be
checked at all. 2477 carry no pin, and 266 carry a pin whose producer is not in
the manifest — so nothing can verify it. The Q_β defect lived in that gap for as
long as it did because `qbeta_ck_cache` was undeclared; it became checkable only
once it was added to the manifest in this branch.

So the sweep's `DECL_MISMATCH: 1` should be read as *"one contradiction among the
10% we can see"*, not *"one contradiction in the corpus"*. Extending the manifest
is what converts `UNDETERMINED` into a verdict, and each producer added brings its
witnesses under both this sweep and the existing self-consistency audit.

## 5. Relationship to the infrastructure fix

The companion audit records the `witness.py` changes that stop the mislabel being
created in the first place: `build()` now stamps a positively-declared pin, and
preserve-forward no longer carries a pin that a declaration contradicts. This
sweep is the detection half — it finds stamps that are already wrong, including
ones written before those fixes existed.

Neither replaces `q0_anchor_consistency_audit.py`. The two check orthogonal
things and both are needed: label-vs-value, and label-vs-producer.
