# The q₀ migration work-list is 5 confirmed, not 624 — and the largest muon population is a *different* defect

**Date:** 2026-08-22
**Bean:** `qou-1c4y` (re-baseline)
**Branch:** `claude/q0-migration-rebaseline-2026-08-22`

## Summary

`qou-1c4y` has carried a headline of "~840 muon-q₀ witnesses", which I
re-baselined earlier this session to a measured "624 fingerprint / 65
stamped". **Both numbers are wrong in the same way**: they were produced
by grepping a 12-digit prefix of the muon pin, and that prefix does not
identify the muon pin. It conflates two distinct q₀ values.

Measured over the 3030 tracked `computations/**/*.witness.json`:

| population | count | what it is |
|---|---:|---|
| current muon `1.109978595557334…` | 212 | the live ideal/CAL-2 pin |
| **superseded muon `1.109978595554180…`** | **375** | the *old* muon value — a pin-currency defect |
| both values present | 24 | deliberate cross-anchor comparison, mostly |
| rounded / low-precision variants | 31 | e.g. `1.10997859556` |
| **loose-prefix total** | **642** | |

The prefix sensitivity is the tell:

```
1.1099785955        -> 642
1.10997859555       -> 624   <- the number I re-baselined to
1.109978595557334   -> 236
1.10997859555733471 -> 206
```

The drop from 624 to 236 is not precision loss. It is 388 witnesses
carrying a **different number**. The two muon values diverge at the 12th
decimal digit.

## The superseded value is already documented

`1.109978595554181` is named in
[`.claude/skills/local/language-trap-agent-audit.md`](../../.claude/skills/local/language-trap-agent-audit.md)
as *"the **old muon value** — arithmetically correct (it solves the CAL-2
identity and back-implies CODATA m_μ/m_e to 12 digits), so report it as a
pin-currency defect, not a corrupt number"*. That guidance is right and I
am not restating it as new. What is new is the **size**: it is the
largest single muon population in `computations/`, and it was invisible
inside the "624 muon witnesses" headline.

This matters for how the sweep is framed. A witness on the superseded
muon value is wrong **under either convention** — re-pinning it to proton
and refreshing it to the current muon value are both improvements, and
leaving it is wrong either way. It is not "awaiting the proton
migration"; it is stale on its own terms.

## The confirmed defect class: declared proton, pins muon

Separately, and much sharper — the `q-pinning-50-digit.witness.json`
read path.

That witness is **muon-anchored** (`q0Anchor: "muon"`,
`q0Value: 1.10997859555733471…`). Narrowing over live (non-`_deprecated`)
producers:

| | count |
|---|---:|
| reference the file (152 including `_deprecated/`) | 136 |
| … read the JSON directly **and never import `q_parameter`** | 69 |
| … and bind q₀ from `derived_50_digit["q"]` | **56** |

Those 56 pin to muon with no anchor resolution at all — they get whatever
that witness happens to carry, regardless of the 2026-08-07 owner
directive that compute defaults to proton. Crossed against
`q0_anchor_manifest.json`:

- **51 UNDECLARED** — nobody has classified them.
- **5 declared `physical_proton`** — a flat contradiction.

The 5:

| producer | witness |
|---|---|
| `aK_via_lp_dual_hecke_basis.py` | `a-K-via-lp-dual-hecke-basis.witness.json` |
| `b_over_m_order_probe.py` | `b-over-m-order-probe.witness.json` |
| `path4_rho_K_at_h3A.py` | `path4-rho-K-at-h3A.witness.json` |
| `q1_mass_gap_probe.py` | `q1-mass-gap-probe.witness.json` |
| `q_beta_form_a_n1_extension.py` | `q-beta-form-a-n1-extension.witness.json` |

**Confirmed in both directions, not inferred.** Each of the five is
declared `physical_proton` in the manifest, binds q₀ from the
muon-anchored witness in code, *and* emits a witness stamped
`q0Anchor: "proton"` whose recorded q₀ is the muon value. The witness
contradicts itself.

`q1_mass_gap_probe.py:170` is the clearest instance — the line reads

```python
# q₀ from the canonical pinning witness (proton anchor)
```

directly above a read that returns the muon value.

## The disposition of the 5 is not uniform — but not for the reason I first wrote

**Corrected in the same session.** My first pass read
`q_beta_form_a_n1_extension`'s comment *"Load **CAL-2** q_0 from canonical
pinning witness"* as evidence that the producer deliberately wants the
ideal muon layer, and concluded the *manifest* was the bug. That was
wrong, and it inverted the argument I built on it.

AGENTS.md §"q₀ anchor convention" is explicit that the 2026-08-07
directive *"is about which **numerical evaluation** code defaults to, not
about redefining the 3-CAL triple"* — the ideal CAL-2 definition
(`𝔇_β`, proxy `m_μ/m_e`) is untouched, while **compute evaluates at the
proton pin**. So naming CAL-2 identifies *which calibration*, not *which
pin*. Treating it as a pin choice is exactly the conflation the directive
exists to prevent. The manifest entry is right; the read is the bug.

Corrected dispositions:

| producer | evidence | disposition |
|---|---|---|
| `b_over_m_order_probe` | docstring: *"Computed at the **proton-pinned** q₀"* | **read is the bug** |
| `path4_rho_K_at_h3A` | compares against proton/neutron `ρ_K_CODATA` | **read is the bug** |
| `q_beta_form_a_n1_extension` | *"Load CAL-2 q_0"* names the calibration, not the pin | **read is the bug** |
| `q1_mass_gap_probe` | reads the witness for **two** purposes — binds q₀ from it *and* uses its `plancherel_weights_n3` / `[2]_q` as a reference table | **dual-purpose read** |
| `aK_via_lp_dual_hecke_basis` | "H_3 (proton, neutron)" names the *particle*, not the pin | no stated intent — directive default applies |

### What survives, and what does not

**Does not survive:** my claim that a mechanical re-pin would have broken
`q_beta_form_a_n1_extension` by overriding a deliberate ideal-layer
choice. Under the directive, re-pinning it to proton is the *correct*
action. Three of the five are now plain read-bugs.

**Survives, but narrower:** `q1_mass_gap_probe` still resists a mechanical
sweep, for a different reason. It reads
`q-pinning-50-digit.witness.json` for two things at once — its q₀ bind
*and* its recorded Plancherel weights, used as a cross-check reference
table. A naive re-pin that redirects the whole read to the proton source
fixes the first and breaks the second. The hazard is a **dual-purpose
read**, not a layer-intent conflict.

That is a weaker argument than the one I first made, and it is the one
the evidence actually supports. The sweep still needs per-file reading —
but to find dual-purpose reads, not to adjudicate which layer each
producer wants.

## Relation to the trap `qou-1c4y` already names

The bean already flags `wedderburn_jones_markov.y_lambda_at`, where a
muon-built cache is served to a caller that passed the proton constant,
with no signal that a layer boundary was crossed. The 56 above are the
**direct-read sibling** of that trap: instead of a cached accessor
silently returning the ideal-layer value, the producer opens the
ideal-layer witness itself and never asks which anchor it wants. Same
failure, one layer down, and it bypasses every guard built into the
accessor path.

## What this does and does not license

- **It does not authorise the bulk sweep.** The first attempt broke
  `main` for 208 producers (`qou-m9xp`). Constraints 1–4 in AGENTS.md
  §"q₀ anchor convention" rule 4 stand.
- **It does not make the 51 undeclared producers defects.** A producer
  legitimately in the ideal/CAL-2 layer *should* read the muon pin. What
  the measurement shows is that 56 producers pin muon while the manifest
  declares exactly 3 producers `ideal_muon` — the discrepancy is the
  work, and classifying the 51 is the next honest step, not re-pinning
  them.
- **The 5 contradictions are actionable now.** Each is a single-file
  decision: either the manifest entry is wrong or the read is. They do
  not need the sweep.

## Corrected baseline for `qou-1c4y`

| claim | status |
|---|---|
| "~840 muon witnesses" | superseded |
| "624 fingerprint / 65 stamped" (my earlier re-baseline) | **superseded — the 624 conflates two q₀ values** |
| 212 current-muon + 375 superseded-muon + 24 both + 31 rounded | measured 2026-08-22 |
| 65 stamped `muon` = 3 `ideal_muon` + 11 `physical_proton` + 51 undeclared | measured; the 3 are the legitimately-muon producers |
| 56 producers pin q₀ directly from the muon witness; 5 contradict their own manifest entry | measured, confirmed both directions |
