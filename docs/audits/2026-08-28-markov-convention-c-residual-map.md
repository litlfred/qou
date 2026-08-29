# The residual convention-C surface in `computations/`, measured

Companion to the `free-neutron-decay` fix (this branch). The 2026-08-15 owner
ruling (R1) made convention **D** (`z = q³/(q²+1)`, `z_D(q₀) = 0.6126880…`)
canonical and excised **C** (`z = √q/(q+1)`, `z_C(q₀) = 0.4993203…`).
AGENTS.md records the `computations/` surface as *measured but not clear*.
This is the `z_markov`-keyed slice of it, measured end to end.

## Method

`z_markov` is a **published witness field** and a **library attribute**, so it
is detectable by *value* rather than by spelling — which is what makes this
slice measurable at all. `z_C(q₀) = 0.4993203…` and `z_D(q₀) = 0.6126880…`
differ in the first digit, and the two values are anchor-independent to 7
figures (proton and muon agree), so the classification cannot be confounded by
the q₀ pin.

That is worth stating because every other convention audit in this corpus keys
on *how the convention was written*. Thirteen blind spellings are catalogued in
[the blindness taxonomy](2026-08-15-detector-blindness-taxonomy.md); a
value-keyed test is immune to all thirteen.

## Result: 7 live convention-C witnesses, 17 convention-D

| witness | source convention | disposition |
|---|---|---|
| `free-neutron-decay` | was **C** | **FIXED** on this branch — source *and* witness |
| `q-pinning-50-digit` | already **D** | **leave** — see below |
| `qou-mass/…/q-pinning-50-digit` | generated mirror | follows the above |
| `hadron-knot-table` | already **D** | witness stale; producer is >50 min/atom |
| `t35-weak-vertex` | **C**, via `hecke_division` | open |
| `deuteron_trefoil_qinvariant_closed_form` | **C** | open |
| `trefoil-complex-volume-probe` | **C** | open |

**Two of the seven have a D source and a stale C witness.** They are not
convention defects at all — they are un-regenerated witnesses, and they
self-correct on the next run. Do not "fix" them at the source; there is
nothing there to fix.

`q-pinning-50-digit` in particular must be **left alone**, and its own producer
says why ([`q_pinning_50_digit.py`](../../computations/q_pinning_50_digit.py):123–131):
it is **anchor-defining** (AGENTS.md rule 1 — it is what `_q0_value_for_anchor`
reads), the field is read by nothing, and regenerating it to correct one inert
field risks the q₀ anchor for no gain. That reasoning is sound and predates
this audit.

## The three genuine live-C sources

### 1. `computations/hecke/hecke_division.py:186` — a library, and float64 too

```python
self.z_markov = 1.0 / (self.q_half + self.q_half_inv)   # z_C, and a float64 literal
```

Used at line 760 inside `_trace_word`, so it is **live in an actual Markov
trace**, not merely published.

**Its reach is much narrower than the import graph suggests.** `hecke_division`
has ~25 live importers, but `HeckeDivision.markov_trace` has only **one** live
external caller: `t35-weak-vertex.py` (lines 84, 102). `hecke_engine.py` and
`hecke_rust_bridge.py` call `self.qr.markov_trace`, where `qr` is
`HeckeRational` — a **different class** whose `markov_trace` is a product of
traced volumes and contains no `z` at all. So the central engine is untouched
by this, and the "one name, two conventions" hazard AGENTS.md documents for
Lean's `markovZ` is present here in Python as well.

### 2 & 3. Two probes that justify C by citing a witness that is D

Both adopt convention C and both point at a committed witness as the
authority — and in both cases that witness now carries **D**:

- [`trefoil_complex_volume_probe.py`](../../computations/probes/trefoil_complex_volume_probe.py):29
  — *"matching the repo's z_markov ≈ 0.49932 in pentagon-reduction-li2q.witness.json"*.
  Measured: `pentagon-reduction-li2q.witness.json` carries
  **0.6126880371464652515958298639458992480263083915450636084720501751483235**.
  The citation is stale; the witness moved to D and the probe did not.
- [`deuteron_trefoil_qinvariant_closed_form_probe.py`](../../computations/deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py):18–24
  — *"Canonical conventions (verified against committed witness) … z_markov =
  1/(A + 1/A) (committed 0.49932…), s_skein (committed 0.10439…)"*. Those two
  values are `free-neutron-decay`'s old `constants_at_q0` — i.e. the witness
  corrected to D on this branch. Its stated authority no longer says what it
  says.

**These are not deliberate historical comparisons.** A deliberate comparison
declares itself (AGENTS.md's `stale_muon_pin_q0` / `q0_muon_pin` pattern, or a
`_legacy` name). These two claim to be *canonical* and cite an authority for
it. That is the defect: not the value, but the claim about it.

## What is NOT established here

- **Whether re-deriving the two probes under D changes their conclusions.**
  It changes their numbers — `z` moves 0.4993 → 0.6127, ~23 % — and neither
  probe has been re-run under D. The trefoil probe's own reduction
  `tr_M(σ³) = (h²+1)·z + h` is linear in `z`, so the shift is not small.
- **Whether `t35-weak-vertex`'s `W_q` conclusions survive the switch.**
- Nothing here re-scopes any refutation. Scope-(a) throughout.
