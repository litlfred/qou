# A5 brick built: the categorical Markov-trace complex volume `𝔙_q(5₂)` by Wedderburn block — 4₁ amphichirality control passes (the raw-trace route fails it)

**Date:** 2026-07-19 · **Branch:** `claude/agent-pickup-stalled-rtugin` ·
**Axis:** c₃ / Q_β bar-odd fibre datum (A5) · **Bean:** `qou-3yxn` ·
**Tier:** fibre-level categorical datum, q-exact · **Discipline:** no fit,
nothing wired, no tier change; the G3 argument→S wall stays open (not laundered).
**Probe:** [`computations/probes/qbeta_5two_categorical_markov_volume_probe.py`](../../computations/probes/qbeta_5two_categorical_markov_volume_probe.py)
· **Witness:** `qbeta-5two-categorical-markov-volume.witness.json` (3/3).

## What was built ("now is later")

The reeb-trace brick isolated the chiral bar-odd datum of 5₂ as the **writhe**,
and flagged the full Markov-trace complex volume `𝔙_q(5₂)` — the QOU analogue of
the Neumann–Zagier `𝕍 = Vol + i·CS` (`conj:binding-qbeta-complex-volume`) — as
"a later brick." This builds it, by Wedderburn block, and **gates it** against the
amphichiral 4₁ control.

`𝔙_q(K) = tr_M(ρ(β_K)) = Σ_λ W_λ·χ_λ(β_K)` over the blocks `λ ⊢ 3 =
{(3),(2,1),(1,1,1)}`, for the canonical 5₂ 3-braid `β = σ₁³σ₂⁻¹σ₁σ₂⁻¹`:

- `χ_(3)(β) = q^e`, `χ_(1,1,1)(β) = (−q⁻¹)^e` (the two 1-dim reps; `e` = exponent
  sum / writhe), `χ_(2,1)(β)` = trace of the 2×2 Hoefsmit seminormal product.
- **Bar-even (Vol/cosh) channel** = the self-conjugate (2,1) block; **bar-odd
  (CS/sinh) channel** = the (3)/(1,1,1) conjugate pair.

## Two gates-first findings (why the naive route is wrong)

1. **The RAW NF Markov trace is framing-contaminated.** Bar-decomposing
   `tr_M(ρ(β)) = Σ_w c_w·τ(w)` (NF basis) directly under `σ:q↦q⁻¹` gives the
   amphichiral **4₁ a nonzero bar-odd part — which is wrong** (4₁ ≅ 4₁* forces
   every fibre invariant bar-even). The raw trace is not a knot invariant (it
   carries the braid's framing), so its `q↦q⁻¹` image is a *different* framed
   representative. The correct object is the block decomposition, where the
   bar-odd lives purely in the conjugate pair and the (2,1) block is bar-even.
2. **The `(σ₁σ₂σ₁)` Markov weight is not `z³`.** `τ(σ₁σ₂σ₁) = tr(σ₁²σ₂) =
   tr((h·σ₁+1)σ₂) = h·z² + z`, `h = q−q⁻¹` — not the naive `z³` (which injects a
   spurious `(q+1)³` denominator).

Both were caught before commit by the gates-first discipline (mirroring the A5.1
R-matrix probe that failed its braid-relation gate pre-commit).

## Results (q-exact, gated)

| # | result |
|---|--------|
| 1 | **(2,1) block bar-even** for both 4₁ and 5₂ — `χ_(2,1)(q)=χ_(2,1)(q⁻¹)`, q-exact (the Vol/binding channel carries no chirality). |
| 2 | **Amphichiral control PASSES:** bar-odd (CS) datum `= 0` for 4₁ (`e=0`), `= ½(q²−q⁻²) ≠ 0` for 5₂ (`e=2`) — the chiral sinh-object 4₁ structurally lacks, matching the reeb-trace writhe result exactly. |
| 3 | The 5₂ bar-odd datum is **anchor-smooth** (`d ln|odd|/dq ≈ 8.8`, O(10⁰)) — the odd *ingredient*, not the ~3.84×10⁶ swing *value* (proved measurement-limited, `SRigidity.no_anchor_invariant_realizes_swing`). A **fifth** independent anchor-smoothness confirmation (A1: 3.6e2, A2: 8.2e2, A4: 8.6, reeb, now the block 𝔙_q). |

## Scope and the G3 wall (STRICT)

This is the **fibre-level** (pre-τ) categorical datum only. It does **not** cross
the **G3 argument→S resurgent-monodromy wall** — the analytic continuation from
the formal-q block characters to the archimedean decay projection `S` — which
**stays open (not laundered)**. No archimedean `S` value is claimed; the swing
value stays measurement-limited; no `c_k` is wired.

## The Ocneanu block weights `W_λ` — determined and held-out-gated (finding 4)

The earlier symbolic solve for the full weights was numerically unstable; redoing
it in `t = √q` gives clean weights, and they are **validated against a held-out
Ocneanu gate**: `tr_M = Σ_λ W_λ χ_λ` reproduces `τ(σ₁σ₂)=z²`, `τ(σ₂σ₁σ₂)=h·z²+z`,
and `τ(σ₂)=z` — elements **not** used in the solve — exactly (q-exact). So the
weights are correct; the "messy/remaining" flag is closed. The bar-even / **Vol
(binding)** channel is then `W_(2,1)·χ_(2,1)`, evaluated at the anchors in the
witness. (Note: the `z = 1/(√q+1/√q)` used here is the QOU Markov convention, not
the Jones-polynomial specialization, so the raw trace is not the Jones polynomial;
the probe makes no Jones claim.)

**What remains** is assembling the framing-**invariant** full `𝔙_q` (the
knot-invariant `Re = Vol` / `Im = CS`), which needs the writhe/Jones
normalization — the piece adjacent to the G3 wall. The raw weighted trace is
framing-covariant (as the raw-trace amphichirality failure above shows), so the
knot-invariant `𝔙_q` requires that normalization, not just the weights.

The brick advances bean `qou-3yxn`: the categorical Markov-trace `𝔙_q(5₂)`
bar-odd channel is now built and gated. The value-leg closure (measurement floor)
and the G3 continuation are unchanged.
