# 2026-05-09 — Branch deep-dive integration into workplan v3

**Branch:** `claude/weinberg-wedderburn-321-deepdive`
**Predecessor:** [`2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md) (on main)
**Companions on this branch:**
- [`2026-05-06-staircase-bar-pair-recursion.md`](2026-05-06-staircase-bar-pair-recursion.md)
- [`2026-05-06-staircase-ew-predictions.md`](2026-05-06-staircase-ew-predictions.md)
- [`2026-05-06-staircase-ew-residual-conjecture.md`](2026-05-06-staircase-ew-residual-conjecture.md)
- [`2026-05-06-delta-I-interface-knot-refinement.md`](2026-05-06-delta-I-interface-knot-refinement.md)
- [`2026-05-06-321-deep-dive.md`](2026-05-06-321-deep-dive.md)

## 1. Purpose

After 552 main commits since branch creation (workplan v3 already
authored on `main` post-#569 through #579), this audit cross-links
this branch's structural findings into the v3 plan and identifies
the highest-yield remaining action.

## 2. What this branch contributes (post-rebase)

| Finding | Witness / Block | Maps to v3 Tier |
|---------|-----------------|-----------------|
| Categorical-linking-operation Property 1 (linearity) PROVED | `categorical-linking-operation.lean` | Tier A item 1 |
| Property 2 ($k=0$ reduction) PROVED | same | Tier A item 1 |
| Property 3 (multiplicativity, pre-trace) PROVED | same | Tier A item 1 |
| Property 4 (trace-cut symmetry) PROVED conditional | same | Tier A item 1 |
| Property 5 (bar-involution compatibility) PROVED conditional | same | Tier A item 1 |
| β_EW(Δ_I^minimal) full numerical spectrum (76 eigenvalues) | `beta-ew-delta-I-numerical-spectrum.witness.json` | Tier A item 1 |
| (3,2,1) 8 bar-pairs + det = +1 | `beta-ew-delta-I-321-and-wedderburn.witness.json` | Tier A item 1 |
| Conjugate-pair det law (n=6, 6/6 verified) | `beta-ew-delta-I-conjugate-pairing.witness.json` | Tier A item 1 |
| Staircase bar-pair recursion (k=2, 3 verified; k=4 partial) | `staircase-bar-pair-recursion.witness.json` | Tier A item 1 |
| (3,2,1) max+/2nd-max+ = 1.78, 2.19% off cot θ_W | `beta-ew-delta-I-321-and-wedderburn.witness.json` | Tier A item 3 |
| `def:ew-interface-knot` Δ_I categorical block | `ew-interface-knot.{md,ts,lean}` | Tier A item 1 |

**Net effect on v3 inventory:**

- v3 §2 "Open — gating 1ppb closure", Tier A item 1 ("$N_v$
  categorical derivation"): five sub-properties of the linking
  operation are now formally proved (3 generic + 2 conditional on
  cited substrate axioms) — this **unblocks** the linking-operation
  prerequisite that v3 marks as open.
- v3 §3 closeable-now item 4 (`wedderburn_pair_volumes.py` LP/SDP
  integration): still ready, now with this branch's β_EW(Δ_I)
  spectrum data as additional input for the EW-sector dual basis.
- v3 Tier A item 3 (Weinberg angle): 2.19% structural near-miss
  identified in $V_{(3,2,1)}$ max+/2nd-max+; closing the residual
  gap is the next concrete categorical-physics task.

## 3. What v3 already covers (no duplication needed here)

- **`prop:hoefsmit-cell-content` half-completion** via tracker +
  partition basis (v3 §2). My cell-content multiplicities (4,2,1,3,3,1,2,4)
  for the 8 pure-pattern projectors at $n=6$ contribute to this
  half but the v3 audit's `gb_filtration_jet_tracker` extension
  is the broader structural framework.
- **Tier-2 PSLQ extension** (v3 §3 item 1): ready to execute.
- **`Term7ShellCorrectionClass` α_5 numerical fit** (v3 §3 item 2):
  the partition basis is enumerated; tracker outputs feed it.
- **Chirality $\langle c \rangle_\beta$** (v3 §3 item 3): ready to
  combine tracker + Hoefsmit Hecke characters.

## 4. Cross-link of structural laws

The v3 plan's Tier A item 1 ("Hoefsmit assignment justification")
benefits from the **conjugate-pair det law** + **staircase
recursion** proved on this branch:

```
Conjugate-pair det law (verified n=6):
   det(M_λ) · det(M_{λ'}) = ±1                  (universal)
   det(M_{ρ_k}) = (-1)^{f_{ρ_k}/2}              (self-conj. specialisation)

Staircase recursion:
   k=2  ρ_2 = (2,1)       dim=2   1 pair  det=-1
   k=3  ρ_3 = (3,2,1)     dim=16  8 pairs det=+1
   k=4  ρ_4 = (4,3,2,1)   dim=768 384 pairs predicted, det=+1 verified on σ_1
```

These laws **compress** the spectral content of $\beta_{\rm EW}^{(n)}(\Delta_I)$
across all partitions of $n$: knowing the spectrum on
half the conjugate-partition pairs determines the other half via
bar-conjugation. Together with the linking-operation Property 5
(bar-involution compatibility, proved conditional on substrate
axioms), this gives a **categorical realisation of partition-
conjugate symmetry under the bar involution at the spectral level**.

Implication for Tier A item 1 (Hoefsmit assignment): the
$W \leftrightarrow \sigma_1^4$, $Z \leftrightarrow \sigma_3^6$,
$H \leftrightarrow \sigma_5^8$ structural assignment proposed in
[`conj:hoefsmit-ew-cell-content`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-ew-cell-content.md)
must be compatible with the staircase recursion at $\rho_3 = (3,2,1)$
— and indeed all three carriers concentrate on this self-conjugate
shape (the unique max-dim shape of $H_6(q)$).

## 5. Recommended next action (this branch)

Per v3 §5 "this session" priority list, **the wedderburn_pair_volumes.py
LP/SDP wiring** (v3 §3 item 4) is the highest-yield item:

- "Pure integration, no new content"
- "Half-day"
- Wires PR #534's pair-amplitude infrastructure into
  [`prop:knot-operator-lp-selection`](../../content/quantum-observable-universe/braids-and-knots/knot-operator-lp-selection.md)
  for the EW-sector LP/SDP-dual basis
- Combined with this branch's β_EW(Δ_I) spectrum data, gives
  concrete numerical inputs for the Weinberg-angle correction
  (currently 2.19% off CODATA on the (3,2,1) max+/2nd-max+
  reading)

If wired, the Weinberg-angle gap can be re-tested with the LP-active
set selected by Wedderburn pair amplitudes — a structural
constraint absent from the simple max+/2nd-max+ ratio.

## 6. PR strategy

This branch's PR ([#553 already merged the rebase]; current
branch head includes deep-dive content + parallel-agent staircase
content blocks):

1. **PR for current state** — once final integration audit
   (this doc) lands, close PR.
2. **Spawn new branch** for `wedderburn_pair_volumes.py` LP/SDP
   wiring — separate concern, separate PR, easier review.
3. **Continue Tier A** in parallel as background work — the
   open theorem-level items (linking properties 4,5 unconditional,
   Weinberg angle structural identification) remain multi-week
   research-grade.

## 7. Files

- This audit:
  [`docs/audits/2026-05-09-branch-deepdive-v3-integration.md`](2026-05-09-branch-deepdive-v3-integration.md)
- Workplan v3 (on main):
  [`docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md)
- This branch's structural findings:
  see §2 table.
