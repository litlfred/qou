# Deuteron `f_pn` wired against the Step-1 `W_λ` gate (2026-06-20)

**Status:** audit — exploratory, falsifiable, **no fit**. Wires the owner-gated
deuteron pn-channel magnitude to the keystone Step-1 q-Plancherel weight, giving
the geometric `W_λ` realization a second binding-side target.

**Probe:** [`computations/probes/deuteron_fpn_wlambda_wiring.py`](../../computations/probes/deuteron_fpn_wlambda_wiring.py)
· witness `computations/deuteron-fpn-wlambda-wiring.witness.json`. Pure
closed-form `mpmath`; reuses the channel construction
([`hecke_channel_binding_probe.py`](../../computations/probes/hecke_channel_binding_probe.py))
and the gate's `W_λ` emitter
([`keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py),
merged PR #2525) with no re-implementation.

## Why

PR #2503 (keystone DG attack plan) offered to wire the deuteron `f_pn`
extraction against whatever `W_λ` the Step-1 gate emits
([comment](https://github.com/litlfred/qou/pull/2503#issuecomment-4757453822)).
Two corpus facts make this a clean, cheap check:

- **Binding side (#2507).** The chirality × topology probe localized the entire
  light-nuclei residual that is *not* the ⁴He α-cluster term to a single
  owner-gated magnitude: the deuteron pn suppression `f_pn = 0.588` (the value
  reproducing AME `B(²H) = 2.224566 MeV` exactly). The corpus already flags it
  "owner-gated to the s5-so3 fibre keystone" — "no substrate channel lands 0.588"
  ([`2026-06-20-chirality-forces-complete-graph-topology.md`](2026-06-20-chirality-forces-complete-graph-topology.md)).
- **Gate side (#2525).** The Step-1 gate emits `W_λ = d_q(λ)²/[n]_q!` — the
  WRT(S³/2I) per-block weight target that the (still owner-gated) geometric
  realization must reproduce.

## The wiring

The deuteron pn bond rides the **standard Hecke channel** `V_std = z·c + d`,
whose eigenvalue is the standard representation. At the Borromean level `n = 3`
(where the keystone generation blocks live, per #2525) the standard rep is
`λ = (2,1)`. So the gate's binding-side weight for the pn bond is `W_(2,1)`.

The harness `deuteron_fpn_from_Wmap(Wmap, E0)` takes **any** `W_λ` dict at
`n = 3` and returns the predicted pn binding — so a future *geometric* `W_λ`
plugs into the same check with no further wiring.

## Result (E₀ = m_e/(q₀(q₀−1)) = 4.18598 MeV at q₀)

| quantity | `f_pn` | E = E₀·ln(1/f) (MeV) | vs AME 2.2246 |
|---|---:|---:|---|
| std channel `z·c + d` | 0.39479 | 3.8905 | over-binds 74.9% |
| **required (exact AME)** | **0.58776** | **2.2246** | — |
| gate `W_(2,1)` at `n = 3` | 0.66067 | 1.7351 | under-binds 22.0% |

**The required magnitude is strictly bracketed:**

```
f_std   <   f_required   <   W_(2,1)
0.39479 <   0.58776      <   0.66067
```

equivalently `E(W_(2,1)) < E_AME < E(std)` — `1.7351 < 2.2246 < 3.8905`.

## Bring-coordinate cross-check (not just the algebraic weight)

The wiring above rides the *algebraic* q-Plancherel weight and the abstract
standard channel. The geometric question — *does Bring's surface land 0.588?* —
has real compute infrastructure at the Borromean (`𝓑₃`) level, so the probe also
records it:

| Bring-coordinate object | value | role |
|---|---:|---|
| bond-factor coordinate `z = √q/(q+1)` | 0.49932 | what every `f = c·z + d` factor uses |
| coral-fibre coordinate `z₀ = √q − 1/√q` | 0.10439 | where the **open** geometric `W_λ` lives — **unused** by any `f_pn` compute |
| Bring-color-weighted `f_pn = z − h(½ − δ/4)` | 0.39486 | production convention (`closed_form_tau_M.py::bring_color_weighted`); E = 3.890 MeV; `δ = 0.00138` |
| Yekutieli Stokes `𝓑₃`: `κ = 3/16` | 0.18750 | non-abelian-Stokes h²-action of the Borromean braid |
| `tr_M(𝓑₃, q₀)` | 1.00673 | Borromean Markov trace — an action/trace **> 1**, not a per-bond `f < 1` |

Two honest conclusions:

1. **The production Bring-color-weighted convention also gives 0.395** — the *same*
   lower bracket as the abstract std channel (the `δ` flavour split is ~0.001,
   negligible). So the lower bracket is the full production+Bring-color answer, not
   an artefact of using the bare std channel. This robustly confirms the corpus
   statement "no substrate channel lands 0.588".
2. **No available compute — algebraic OR Bring-coordinate — lands 0.588.** The
   bond factor rides `z = √q/(q+1)`, *not* the coral-fibre `z₀ = √q − 1/√q ≈ 0.104`
   where `q₀` is geometrically fixed (`H¹(Bring) = 2W`) and where the geometric
   `W_λ` would live. The genuine Bring-surface geometric object that *does* exist
   (the Yekutieli `𝓑₃` Stokes h²-action) is an *action/trace*, not a per-bond
   suppression `< 1`. The magnitude `0.588` therefore remains gated to the **open
   coral-fibre (`z₀`) geometric `W_λ` realization** — exactly the owner-gated DG
   construction of #2503.

## Verdict

- **REFUTE the naive direct-weight map.** Setting `f_pn := W_(2,1)` (the gate's
  *algebraic* q-Plancherel weight) under-binds by 22% on the binding (12.4% on
  `f`). The algebraic `W_λ` does **not** by itself land `0.588`.
- **But it brackets the target.** The bare std channel over-binds from below; the
  q-Plancherel weight under-binds from above; the required value sits strictly
  between. The structure "no substrate channel lands 0.588" is sharpened: the
  required `f_pn` lies in the open interval `(0.39479, 0.66067)`, between the two
  natural keystone-side quantities.
- **Owner-gating stands, with a sharper target.** The magnitude remains gated to
  the *geometric* `W_λ` realization (WRT(S³/2I) — open differential geometry).
  This audit hands that realization a **second binding-side falsifiable target**
  alongside the m_τ lepton tower: any S¹-equivariant index reproducing `W_λ` must
  land `f_pn = 0.58776` (E = 2.2246 MeV) inside `(0.39479, 0.66067)`.

No production rewire, no Δ_λ ansatz, no attempt to fit 0.588 — that would be the
seventh-ansatz trap the three-calibration discipline forbids. This pins the
structural relationship between the deuteron magnitude and the gate's `W_λ`.

## Cross-references

- PR #2503 — keystone DG attack plan + the `f_pn` wiring offer.
- PR #2507 — chirality × topology binding; `f_pn = 0.588` localization.
- PR #2525 — `W_λ` `Z(n)` defect gate emitter (`keystone_wlambda_Z_defect_n_scaling.py`).
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the keystone ledger.
- [`2026-06-20-chirality-forces-complete-graph-topology.md`](2026-06-20-chirality-forces-complete-graph-topology.md) — the binding-side residual.
