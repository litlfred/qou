# Where the ⁴He binding-magnitude shortfall sits — measured

**Date:** 2026-08-29 · **Branch:** `claude/he4-magnitude-fork-2026-08-29` ·
**PR:** [#5966](https://github.com/litlfred/qou/pull/5966) ·
**Type:** measurement + scoping. No corpus rewire, no closure attempt, **no
seventh ansatz**. Every negative is **scope-(a)** unless a proved invariant is
cited; none is cited, so every negative here is scope-(a).

**Producer:** [`computations/probes/he4_body_order_shortfall_location_probe.py`](../../computations/probes/he4_body_order_shortfall_location_probe.py)
· witness `he4-body-order-shortfall-location.witness.json` · mpmath end to end,
no `float()` anywhere, `scripts/precision-gates.sh --changed` run.

---

## 0. Verdict

**The shortfall sits in the body-order weights, not in the bond convention.**

Two things follow, and the second is the more useful one:

1. **The convention leg is closed as an explanation.** Under the canonical
   convention **D** the lumped enhancement is *farther* from target than under
   the excised convention **C** — 0.666 of target vs 0.736 — in both `f_pn`
   typings. The 23 % `z_C → z_D` difference moves the answer the wrong way.
2. **The "26 % short" figure is an artifact of a metric that cannot see the
   defect.** PROBE 2's lumped ratio `1 + |b₄ᶜ|/Σg` compares the 4-body cluster
   against the 2-body sum and **omits the 3-body order entirely**. Resolved by
   body order, the model's connected 3-body cumulant has the **wrong sign** —
   `−2.744` against AME's `+1.426`. A sign error at 3-body, averaged against an
   order-of-magnitude deficit at 4-body, reads as a benign 26–33 % miss.

---

## 1. Currency correction — the audit table in circulation is stale

[`2026-07-05-delta-lambda-gate-status.md`](2026-07-05-delta-lambda-gate-status.md)
§PROBE 2 reports `|b₄ᶜ| = 1.9614`, `Σg = 3.6310`, delivered `×1.540` against
needed `×2.093` — "74 % of target, ~26 % short". Those are **convention-C-frame**
numbers, computed 2026-07-06, before owner ruling R1 (2026-08-15) made
convention D canonical.

The **committed witness has already been regenerated** (2026-08-23) under
convention D and the proton pin, and now carries `z = 0.612688…`,
`|b₄ᶜ| = 1.17395`, delivered `×1.398`. The audit prose was not updated with it.
This unit reproduces the C-frame numbers exactly (`1.9614`, `3.63097`, `1.54019`,
`2.09252`), which is the cross-check that the C branch here is implemented
correctly and that the audit table is C-frame rather than merely old.

Two witnesses on `main` carry prose that contradicts their own data, same class:

| witness | data says | its own `verdict` prose says |
|---|---|---|
| `su4-connected-1111-magnitude` | delivered ×1.398, ungated A=6 cluster 10.17 | "×1.54 delivered vs ×2.09 needed, 74 %"; "overshoots to 22.2" |
| `b4-framework-connected-cumulant-deficit` | `b₄ = −0.304` MeV, **−3.3 %** of target, assertion **failing** | "b₄ = 0.583 MeV = 6.3 % of the 9.243 target"; "must supply ~94 %" |

Both prose strings are hardcoded in their producers and were not regenerated
when the numbers were. Filed as beans below; not fixed here, because fixing them
touches producers a sibling may be holding.

---

## 2. Leg 2 — the bond convention. **Measured; does not close the gap.**

PROBE 2's own lumped metric, recomputed over both conventions and both `f_pn`
typings (`probe2`: `f_pn = z − h(½ − δ/4)`; `chi`: `f_pn = z`, the production
marshalling of `interface_4body_assembly_probe`):

| conv | `f_pn` | \|b₄ᶜ\| | Σg | delivered | needed | delivered/needed |
|---|---|---|---|---|---|---|
| **D** (canonical) | probe2 | 1.17395 | 2.95077 | 1.39785 | 2.09746 | **0.6664** |
| **D** | chi | 0.79211 | 2.53293 | 1.31272 | 1.85636 | 0.7072 |
| C (excised) | probe2 | 1.9614 | 3.63097 | 1.54019 | 2.09252 | **0.7360** |
| C | chi | 1.45456 | 3.21314 | 1.45269 | 1.87575 | 0.7745 |

The ratio **does** move — the concern that `Σg` and `b₄ᶜ` might shift together
and cancel is not what happens — but it moves **away** from 1. Canonical D is
33.4 % short where the excised C was 26.4 % short.

**Scope-(a).** This says the convention is not the missing ingredient; it does
not exclude the bond factors as *part* of the story, and it is not an argument
against convention D, which is forced on independent grounds
(`markovWeights_eq_jones_of_threeRow_eq_zero`, sorry-free) and is not decided by
which value flatters the binding table.

---

## 3. Leg 1 — the body-order weights. **This is where it sits.**

### 3a. The metric that can see it

`thm:binding-closure-conditional` gives `B(K) = m_e Σ_n a_D^{(n)}` — a body-order
series. The matching measurement is the Ursell cumulant inversion, which is a
*definition* of a binding map's body-order content, not a fit:

```
B(A) = C(A,2)·b₂ + C(A,3)·b₃ + C(A,4)·b₄
b₂ = B(D);   b₃ = B̄(3) − 3b₂;   b₄ = B(⁴He) − 6b₂ − 4b₃
```

Applied to AME2020 itself: `b₂ = 2.224566`, `b₃ = +1.426222`,
`b₄ = +9.243387` MeV. Applied to the model
`B(K) = B_AME(D)·W(K)/W(D)` with `W(K) = 1 − ∏_{i<j} f_ij` — one scale, set at
the deuteron, no other input:

| conv | `f_pn` | b₂ | b₃ | b₄ | b₃/target | b₄/target |
|---|---|---|---|---|---|---|
| **D** | probe2 | 2.22457 | **−2.74386** | 2.07699 | **−1.924** | 0.225 |
| **D** | chi | 2.22457 | **−2.02572** | 0.29893 | **−1.420** | 0.032 |
| C | probe2 | 2.22457 | **−3.22385** | 3.21118 | **−2.260** | 0.347 |
| C | chi | 2.22457 | **−2.66794** | 1.72741 | **−1.871** | 0.187 |

`b₂` is 2.22457 by construction (the deuteron is the unit). **`b₃` is
wrong-signed in all four combinations.** `b₄` has the right sign under the
`probe2` typing and reaches at most 35 % of target.

This metric is convention-clean: it consumes only `(z, h, δ)` and AME, and no
cached Markov trace, so swapping the convention cannot produce a layer straddle.

### 3b. Are the `a_D^{(n)}` set to a common value by the probe? **Yes.**

PROBE 2's `delivered = 1 + |b₄ᶜ|/Σg` weights the 4-body cluster and the 2-body
sum with the same coefficient — i.e. it assumes `a_D^{(4)}/a_D^{(2)} = 1` in
Mayer units — and drops `a_D^{(3)}` from the metric altogether.

The corpus does **not** license that. `prop:prolonged-periods-fixed-depth`
proves the periods satisfy a depth-`d` linear recurrence with `n`-independent
kernel, `d ≤ rank V ≤ 2g = 8` for the genus-4 Bring curve — so they are
*constrained* but not *constant*, and the **identification** of `d` and the
kernel with the Bring Picard–Fuchs operator is explicitly open, and explicitly
stated to need "the per-knot weights at `n = 2, 3`". Assuming equality is an
unforced assumption, and it is the assumption the lumped metric encodes.

### 3c. What the weights would have to be — diagnostic, **not** a derivation

Reading the required per-order rescalings off the anchors is **anchor
inversion**. It is a fit if wired, and it is not wired. Its value is that it
converts "the magnitude is short" into a falsifiable target for the open
identification half of §3b:

| conv | `f_pn` | required `a₃/a₂` | required `a₄/a₂` |
|---|---|---|---|
| **D** | probe2 | **−0.5198** | **+4.450** |
| D | chi | −0.7041 | +30.92 |
| C | probe2 | −0.4424 | +2.879 |
| C | chi | −0.5346 | +5.351 |

The canonical row asks for `a₂ : a₃ : a₄ = 1 : −0.52 : +4.45` — a **sign
alternation** between the 2- and 3-body periods, and a fourfold enhancement at
4-body. **The falsifiable question this hands back to the keystone:** does a
depth-≤8 recurrence on the Bring Gauss–Manin local system admit that ratio? If
it does not, the multiplicative/Mayer assembly is wrong upstream of any weight.

### 3d. Held-out check — the ³He−³H isospin splitting

The inversion above consumes only the isospin *average* of ³H and ³He, so their
**difference** is untouched by it and by every `a_D^{(n)}` (a common per-order
weight cancels in the difference). It is a genuine held-out, zero-parameter test
of the bond typing alone:

| conv | `f_pn` | model (MeV) | AME (MeV) | model/AME |
|---|---|---|---|---|
| **D** | probe2 | −0.24427 | −0.76375 | **0.320** |
| D | chi | −0.45075 | −0.76375 | 0.590 |
| C | probe2 | −0.11983 | −0.76375 | 0.157 |
| C | chi | −0.23159 | −0.76375 | 0.303 |

The **sign is right** in all four — ³He is less bound than ³H, the correct
ordering, from the `f_pp ≠ f_nn` typing with no isospin input. The **magnitude
is short by 2–6×**. This matters because the splitting carries no 4-body
content: a shortfall that persists in a pure 2-and-3-body observable is not
localised at 4-body, which is where PROBE 2 and PROBE 2b both went looking.

Worth recording honestly, because it cuts the other way from §2: **convention D
roughly doubles the isospin splitting** (0.157 → 0.320) while making the lumped
4-body enhancement worse. The two metrics respond to the convention in opposite
directions, which is itself evidence that the lumped metric is not measuring
what its name suggests.

---

## 4. What this does and does not establish

**Establishes (scope-(a), measured):**

- The bond convention is not the missing ingredient; canonical D widens the
  lumped gap relative to excised C.
- The lumped PROBE-2 metric omits the 3-body order and therefore cannot detect
  the model's 3-body sign failure; its "74 % of target" reading overstates how
  close the construction is.
- The model's connected `b₃` is wrong-signed under every convention × typing
  combination tested, and its `b₄` reaches at most 35 % of target.
- The held-out isospin splitting is right-signed and 2–6× too small, so the
  deficit is present below 4-body.

**Does not establish, and must not be read as:**

- No **(b) structural exclusion** is claimed anywhere here. No proved invariant
  is cited, so nothing is excluded. The `[1⁴]` ingredient is not excluded; the
  Mayer/multiplicative assembly is not excluded; convention D is not impugned.
- The required weights in §3c are **not** a derivation of `a_D^{(n)}` and are
  not wired. Deriving them from the anchors would be exactly the fit the Δ_λ
  gate forbids.
- Nothing here closes the magnitude. The gate remains **OPEN**.

---

## 5. Corpus-grep

Run per AGENTS.md §"Before declaring open" on {⁴He magnitude, connected cluster,
body-order cumulant, `a_D^{(n)}`, convention C/D}. **None of the six paths
returns empty**, and path 6 (`.beans/`) and path 3 (`computations/`) between
them already carried the body-order framing: `b4_value_cumulant_target_probe.py`
establishes the AME cumulant target `b₄ = 9.24 MeV` and
`b4_framework_connected_cumulant_deficit.py` establishes the framework's deficit
and the `b₃` sign failure. **The framing of §3 is not new to the corpus**; what
is new here is (i) the measurement under canonical convention D with the PROBE-2
bond typing, (ii) the direct C-vs-D comparison on one assembly, (iii) the
required-weight diagnostic, and (iv) the held-out isospin splitting. Nothing is
declared newly open.

---

## 6. Beans filed

- `qou-jqla` — witness prose contradicting witness data in
  `su4-connected-1111-magnitude` and `b4-framework-connected-cumulant-deficit`
  (hardcoded C-era verdict strings; the second has a live failing assertion).
- `qou-34oo` — the 2026-07-05 gate-status audit table is convention-C-frame and
  is being quoted as current.
- `qou-i5yp` — the falsifiable question for the keystone: does a depth-≤8 Bring
  Gauss–Manin recurrence admit `a₂ : a₃ : a₄ = 1 : −0.52 : +4.45`?

## 7. Key files

- [`computations/probes/he4_body_order_shortfall_location_probe.py`](../../computations/probes/he4_body_order_shortfall_location_probe.py) — this unit
- [`computations/probes/su4_connected_1111_magnitude_probe.py`](../../computations/probes/su4_connected_1111_magnitude_probe.py) — PROBE 2 (the lumped metric)
- [`computations/probes/b4_value_cumulant_target_probe.py`](../../computations/probes/b4_value_cumulant_target_probe.py) — the AME cumulant target
- [`computations/probes/b4_framework_connected_cumulant_deficit.py`](../../computations/probes/b4_framework_connected_cumulant_deficit.py) — the framework deficit
- [`content/quantum-observable-universe/mass-theory/binding-closure-conditional.md`](../../content/quantum-observable-universe/mass-theory/binding-closure-conditional.md) — `B(K) = m_e Σ_n a_D^{(n)}`
- [`content/quantum-observable-universe/mass-theory/prolonged-periods-fixed-depth.md`](../../content/quantum-observable-universe/mass-theory/prolonged-periods-fixed-depth.md) — the depth-≤8 recurrence, identification open
- [`docs/audits/2026-07-05-delta-lambda-gate-status.md`](2026-07-05-delta-lambda-gate-status.md) — PROBE 2 / PROBE 2b (C-frame table)
- [`docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md`](2026-08-15-owner-ruling-convention-d-proton-color.md) — ruling R1
