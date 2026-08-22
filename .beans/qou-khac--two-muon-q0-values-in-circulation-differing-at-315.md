---
# qou-khac
title: Two muon q0 values in circulation, differing at 3.15e-12
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T21:19:10Z
updated_at: 2026-08-22T12:11:22Z
---


## What

Found while resolving `inter_nucleon_linked_channel`'s q0 (`qou-2ixd`, owner
ruled proton). Scanning every hand-typed `1.10997858…`/`1.10997859…` literal in
`computations/` turned up **18 that match neither canonical pin exactly**. Most
are harmless truncations (1e-16 to 1e-21 — simply fewer digits). Three are not:

| file | literal | \|d\| from muon-canonical |
|---|---|---|
| `gap_a3_overshoot_robustness_check.py` | `1.1099785955541805` | 3.15e-12 |
| `per_basis_row_invariants_probe.py` | `1.1099785955541805752815940796` | 3.15e-12 |
| `probes/flavor_split_alpha_dilog_expansion_probe.py` | `1.1099785955541810` | 3.15e-12 |

They are not truncations. They are a **second muon value**:

    muon-canonical (corpus, Q_MUON)  1.10997859555733471989976322048...
    muon variant   (these 3 files)   1.10997859555418057528159407961...
                                     |d| = 3.15e-12   rel = 2.84e-12

3.15e-12 is far above a rounding difference and far below anything a reader
would notice. The variant is the value recorded elsewhere in this session's
notes as `Vol(4_1)/(m_mu/m_e)`, so both plausibly have derivations — which is
exactly why this needs a ruling rather than a guess.

## Why it matters

The `inter_nucleon_linked_channel` case is the precedent. Its pin was wrong by
1.16e-8 and everything still *looked* right: assertions passed, values were
plausible. What exposed it was that `W_(1,1)` disagreed with the registry's own
`y_(2,1)` at digit 9 — and after the correction they agreed to 22. A near-miss
pin does not fail; it quietly shifts every derived number.

At 3.15e-12 these three would shift results in the 12th figure, which is above
the 1e-40 tolerances the trace gates now use and below the precision most
assertions check.

## Next

1. **Owner ruling: which muon value is canonical?** If `Q_MUON` is, the three
   files should import it; if the variant has a derivation, it needs a registry
   entry naming it, like the proton/muon split already has.
2. Once ruled, take it **by import** rather than retyping — the lesson from
   `qou-2ixd`: a literal cannot drift from a source it does not have.
3. The other 15 near-misses are truncations of a correct pin. Worth converting
   to imports on the same principle, but they are not wrong today.

---

## CORRECTION: not two competing canonicals — a stale pin kept as a control

Owner ruling 2026-08-15: **proton is canonical.** That was never in question and
my framing of this bean was wrong. There is no contest between two muon
"canonicals" needing adjudication. What is actually in the corpus:

| | value | role |
|---|---|---|
| canonical | `1.1099785827513808075916690956107688798744991218736` | **the** pin (registry, AGENTS.md 2026-08-07) |
| muon-current | `1.10997859555733471989976322048322502665620840878…` | `Q_MUON`, the documented muon anchor |
| muon-stale | `1.10997859555418057528159407960950937799328227995870` | a **superseded** muon value, deliberately retained |

The third is not a rival canonical. Two of the three files carrying it say so
in the source:

* `per_basis_row_invariants_probe.py:67` names the variable
  **`Q0_STALE_MUON_PIN`**, and its docstring describes "a q₀-STABILITY test
  across canonical (m_p-pin) and stale (muon-pin)" — the stale value is the
  *control*, and the point of the probe is that results do not depend on it.
* `probes/flavor_split_alpha_dilog_expansion_probe.py:51` has `_muon_q0()` and
  states "anchor-stable (proton-q₀ vs muon-q₀ drift 5.8e-8)".

That is the same pattern as convention C being kept quotable for labelled
comparison: a superseded value retained on purpose, and named as superseded.
Nothing to rule on.

## The one real defect

`computations/gap_a3_overshoot_robustness_check.py:35`

    Q0 = mp.mpf("1.1099785955541805")

is the **stale muon pin, unlabelled, as the file's only q₀** — no `_muon_q0()`,
no `STALE` in the name, no mention of muon anywhere in the module. Its docstring
meanwhile calls its inputs "the canonical inputs" and "the pinned q₀". It also
truncates: `…5541805` against the full `…55418057528159…`.

So the two files that use the stale pin *as a control* are fine, and the one
that uses it *as the pin* does not know it is doing so.

Its `Q0` is live — it feeds `q_int(m)` and an `(q^{1/2}+q^{-1/2})^{4N}` factor —
so this is not cosmetic. (That half-argument factor is a legitimate `[2]_{√q}`
q-integer, correctly not flagged by the producer audit; it is not a `z`.)

**Not changed here.** The module also carries `TRM` values cached "from the
#2635 canonical run", and switching `Q0` without establishing which pin those
were computed at would trade one inconsistency for another. That needs whoever
owns #2635, not a guess from me.

## Next

1. `gap_a3_overshoot_robustness_check.py` → proton pin by import, once the
   cached `TRM` provenance is established.
2. The other two need nothing.
3. Worth considering: the stale pin should live in one named constant that the
   control probes import, rather than being retyped (twice at full precision,
   once truncated, once as `1.1099785955541810` — four spellings of one
   superseded value).


---

## ⚠ CORRECTION 2026-08-16 — this bean has it BACKWARDS. The "variant" is the live value.

The bean calls `1.10997859555418…` *"a second muon value"* / *"the variant"* and
`Q_MUON = 1.10997859555733…` *"muon-canonical"*. **It is the other way round.**

`qou_substrate.constants.q_muon_at()` does not store a pin — it **derives** one:

```
q = 1/(1 − √(Vol(4_1)/(m_μ/m_e)))
```

Evaluated at today's constants (`Vol(4_1) = 2.029883212819307250042405`,
`m_μ/m_e = 206.7682830`) that returns

```
  closed form      1.109978595554180575281594…
  q_muon_at()      1.109978595554180575281594…   identical
```

— which is **the "variant"**. Meanwhile the hand-typed `Q_MUON` implies
`Vol(4_1) = 2.029883212924203479151486`, **1.05e-10** from the current value. So
`Q_MUON` is the frozen one, stranded against a superseded Vol(4₁), and the three
files this bean flagged were faithfully carrying the *live* derivation.

**Root cause, and it is the reason this could happen at all: the muon pin has no
canonical home.** The proton pin has exactly one — `q_parameter.Q_50_DIGIT_STR`.
The muon pin has a derivation in the substrate and **three independent
hand-typed copies** with two different truncations:

```
computations/deltalambda/mu3_anchor_consistency_probe.py:78   Q_MUON = "1.10997859555733471989976322048322502665620840878015405145269"
computations/probes/baldfn_theta_limit_probe.py:677           Q_MUON = "1.10997859555733471"
computations/probes/qbeta_5two_higher_cable_qstar_probe.py:58 Q_MUON = mp.mpf("1.10997859555733471")
```

A literal cannot drift from a source it does not have — and these have none.
That is this bean's actual finding, and it is the opposite of "someone typed a
wrong number".

### Done here

- **`gap_a3_overshoot_robustness_check.py`** — labelled. Its `Q0` is a 17-digit
  truncation of the *current* derived muon anchor, so it is **not** stale; what
  it is not is canonical (the 2026-08-15 ruling makes the proton pin canonical,
  1.28e-8 away). **And its cached `TRM` is CONVENTION C** — `TRM["D"] =
  0.38835725751524` is the C deuteron |tr_M|, against 0.5751 under D. `Q0` and
  `TRM` are a matched #2635 pair; changing either alone breaks the pairing,
  which is why both are labelled rather than "fixed". Its A3-overshoot trend is
  therefore a C-frame, muon-anchored result — stated in the file so it cannot be
  quoted as a convention-D fact by accident.
- **`probes/flavor_split_alpha_dilog_expansion_probe.py`** — the `except` branch
  returned a hand-typed copy of the derived value. Now **raises**. A duplicated
  constant in a fallback is the worst kind: silent, fires only when the import
  is unavailable, and strands itself the moment Vol(4₁) or m_μ/m_e is refined —
  which is exactly what happened to `Q_MUON`.
- **`per_basis_row_invariants_probe.py`** — **no defect.** It names its literal
  `Q0_STALE_MUON_PIN` and imports `Q_50_DIGIT_STR` separately. A correctly
  labelled control, and the bean should not have counted it as one of "three".

### Still open

Give the muon pin a canonical home and convert the three `Q_MUON` copies to
imports. That is a substrate change (`q_parameter`), it moves values by 3.15e-12
in whatever consumes them, and it wants its own scope — not folded into a
labelling pass.

---

## MEASURED 2026-08-22 — there are THREE values, and neither of this bean's two is canonical

The bean asks *"which muon value is canonical?"* and offers two candidates. The
question is malformed on both counts: there is a **third**, and the muon anchor is
**superseded** as a pin.

### The live derivation gives a value neither candidate matches

`qou_substrate.constants.q_muon_at()` computes
`q = 1/(1 − √(Vol(4₁)/(m_μ/m_e)))` from **live** `vol_4_1_at()` and
`MASS_RATIO_MU_E_STR`. Evaluated at 30 dps today:

```
q_muon_at(30)               1.109978595642739046681795129
this bean's "canonical"     1.10997859555733471989976322    ->  8.540e-11 below
this bean's "variant"       1.10997859555418057528159408    ->  8.856e-11 below
"canonical" − "variant"     3.154e-12                        (this bean's figure, confirmed)
```

So the 3.15e-12 gap this bean is about is real — and **both** its values are
stale against the live derivation by **~8.5e-11, twenty-seven times larger** than
the discrepancy being adjudicated. Ruling that either one is "canonical" would
pick between two numbers that are both wrong by more than the amount separating
them.

### This bean's own thesis, harder than it states it

The bean says the variant *"is not a truncation … it is a second muon value"* and
asks for a ruling. The measurement says the failure mode is not "two values needing
adjudication" but **"a hand-typed copy of a derived quantity cannot stay correct"**
— now demonstrated three times over, because the derivation's *inputs*
(`Vol(4₁)`, `m_μ/m_e`) have been refined since each copy was taken. A ruling that
blesses one literal produces a fourth stale value the next time either input moves.

### The witness layer is almost entirely hand-typed

Measured over `computations/**/*.witness.json` (excluding `_deprecated/`):

| value | witnesses |
|---|---|
| stale hand-typed `…55733…` | **236** |
| other hand-typed `…55418…` | **188** |
| **live `q_muon_at()` `…5642739…`** | **2** |

424 witnesses carry a hand-typed muon constant; **two** carry what the derivation
actually produces. And all three source files this bean names still hold their
literals today (`gap_a3_overshoot_robustness_check.py`,
`per_basis_row_invariants_probe.py`,
`probes/flavor_split_alpha_dilog_expansion_probe.py`) — unchanged since filing.

### And the muon anchor is superseded anyway

`q_muon_at`'s own docstring: *"This was the pin until 2026-05-28; now superseded by
`q_at()` (m_p anchor). Differs from `q_at()` by ~11.5 ppb — that gap is the μ-p
tension (9.5σ)."* Confirmed by the 2026-08-15 ruling making the proton pin
canonical.

So no muon value is *the* pin. The muon quantity survives as a **cross-check**, and
a cross-check evaluated from a stale literal is not a cross-check — it silently
compares against a number the framework no longer derives.

### What this bean should now ask

1. **Not** "which literal is canonical" — none is. **Import `q_muon_at()`**, or
   record a frozen value with the `Vol(4₁)`/`m_μ/m_e` it was frozen against, so a
   later input refinement makes the staleness visible instead of silent.
2. The 424 hand-typed witnesses are `qou-cds3`'s migration population. Note the
   interaction recorded there: **22 witnesses carry a muon value in a field named
   `proton`**, and those are invisible to a fingerprint-based migration metric.
   Fixing them after relabelling is impossible — the evidence of which muon value
   they came from is destroyed by the relabel.

### Not done

No literal changed and no witness regenerated. Replacing a hand-typed pin with an
import moves numbers in the 11th figure across 424 witnesses and three producers;
that is a scoped migration, not a hygiene edit, and it needs the same
authorisation `qou-cds3` is waiting on.
