# bk-crossing mass-binding arc — reassessment + consolidated ledger (2026-08-29)

**Tier:** coordination (no new results). Refreshes the 2026-08-19 arc-refresh
([`2026-08-19-bk-crossing-coordination-arc-refresh.md`](2026-08-19-bk-crossing-coordination-arc-refresh.md))
against ~10 days of further main landings, and re-scopes the workplan. The arc has **no active
branch** — work has diffused into loose beans (`qou-dcvv`, `klgu`, `avt1`, `qb8g`, `qou-brng`,
`qou-e5jf`, `qou-k5r5`), which is itself the first finding.

Arc structure (audit `2026-07-11-bk-crossing-coordination-multiplicity.md`):
`w_n(K) = M_n(A)·Vol_n(K)`, `M_n(A) = z(A)·a_D^(A)`, `z = A−1` per-nucleon coordination;
α-cluster `B(n_α) ≈ n_α·B(⁴He) + N_bonds·b_αα`.

## The four items collapse to two open problems + two settled

| # | Item | Reassessed status | Note |
|---|---|---|---|
| 1 | derive `M = z = A−1` | **refuted-as-stated** | ⁴He falsifies universality (M≈2 not 3). No single M(A) law; regime-dependent. Lane 1 (`CoordinationBinding.lean`, sorry-free) only formalizes z=A−1 = complete-graph degree — nearly tautological; the physics law `B=ε·C(A,2)` sits unfilled in `BondExtensiveBinding`. |
| 2 | magic `a_D^(A)` activation | **open, narrowing by exclusion** | since 08-21: `a_D` obstruction proved-lean (`37cfae1a4d`); ⁴He magic surplus proved *not* a Milnor μ̄ term (`1e4afe69fd`, `klgu`). Magnitude `a_D^(4)≈2.52` still an AME read. **Same phenomenon as item 1** — the magic-shell regime. |
| 3a | close-packing count (n_α≥5) | **settled / derived** | fcc contact-graph, one `b_αα` → ²⁰Ne/²⁴Mg/⁴⁰Ca to <0.5%. The arc's real win. |
| 3b | derive `b_αα ≈ 2.41` | **retire → scope-(a) negative** | VolDensity overshoots 259×; SU(4) base scale forever-gated; `ρ_αα ≈ ℏ_q²` demoted to a definitional restatement (circular). No in-scope route survives; stop carrying it as a derivation target. |
| 4 | deuteron crossing weight | **RE-SCOPED — Owner Ruling A (2026-08-29)** | knot = canonical braid closure (Vol=0) ⇒ binding is **not** a volume term; sourced from the **Gram/Frobenius pairing (⟨g,g⟩) + confinement SDP** channel. 6₂ census assignment retired. `qou-e5jf` unblocked. Magnus Ω₂ progress (`acc9c651a6`) folds into the pairing channel. See the owner-decision doc. |

**Net:** the arc reduces to (i) the **magic-shell regime switch** (items 1+2, the same object seen
twice — `A−1` in the linear chain vs ~2 at doubly-magic ⁴He) and (ii) the **deuteron knot
identity** (item 4, foundational). 3a is done; 3b should be retired.

## Two currency flags from this reassessment

- **Convention D (open, inherited).** The arc's `b_αα` / deuteron trace numbers do **not** spell
  `z` locally — they inherit it from `markov_trace_for_knot` → `pyhecke/gram.py`, whose D-migration
  is bean `qou-cds2` (in-progress, blocked on a Gram singularity under D). So these numbers are
  **convention-inherited, D-status open** — not yet canonical. Full finding:
  [`2026-08-29-arc-convention-d-inheritance-audit.md`](../audits/2026-08-29-arc-convention-d-inheritance-audit.md).
- **Absolute-mass excision (2026-08-11).** The rung dichotomy ("mass ~ 1/ℏ_q², binding ~ M") is
  fine as *structure/ratios* (`BindingMassRung.lean`, sorry-free), but the arc must report binding
  and ratios, not absolute MeV.

## Reassessed priority (post-session queue)

1. **Merge items 1+2 → derive the magic-shell regime switch** (`z=A−1` chain ↔ M≈2 magic). In
   scope (does not route through the forever-gated q₀). `BondExtensiveBinding` is the slot the
   derived law must fill. Deepest, highest value.
2. **Item 4 — OWNER RULED A (2026-08-29); Gram/SDP compute done → scope-(a) negative.**
   [`2026-08-29-deuteron-knot-owner-decision.md`](../audits/2026-08-29-deuteron-knot-owner-decision.md).
   Deuteron binding is *not* a volume term; the mechanism tested is the **Gram/Frobenius pairing
   (⟨g,g⟩) + confinement SDP**. **Computed** (`deuteron_real_sdp.py`, H₆): the block-diagonal Gram
   SDP is degenerate (~3.7e-43), and **0 of 6 off-diagonal constraint encodings derive the binding**
   — five give 0 / infeasible / ansatz; the only non-zero (2.22456607) is the AME value *fed in* as
   the constraint (circular). This is the **intensive/extensive gap** (a per-nucleus block-selection
   SDP is intensive; binding is extensive) — the same missing term the Δ_λ magnitude gate is open on.
   Full: [`2026-08-29-deuteron-binding-via-gram-sdp-compute.md`](../audits/2026-08-29-deuteron-binding-via-gram-sdp-compute.md).
   Remaining sub-route: the un-run full H₆ off-diagonal Hecke Gram (720 elements) — **negative
   prior** (still per-nucleus), do not run speculatively. All numbers convention-inherited
   (`qou-cds2`).
3. **Gate the arc's `b_αα`/deuteron numbers on `qou-cds2`** (engine-level D migration) before any
   canonical use.
4. **Retire 3b** to a scope-(a) negative; **keep `qou-brng`** (prove saturated binding fraction is
   *exactly* ℏ_q², not merely O(ℏ_q²)) as the one clean forward kernel.
5. **Re-open a coordinating branch** for the arc — the work is currently fragmented across beans
   with no consolidated owner.

## The one genuine forward kernel

`qou-brng` — the analytic dichotomy is already Lean-proved (mass = order-2 pole residue `lw`;
`binding/mass = (M/lw)·ℏ_q² → 0`), and the CAL-2 cusp factor explains the `1/ℏ_q²`. What remains is
a first-principles proof that the *saturated* binding fraction is exactly ℏ_q² (physically it rises
to 0.95·ℏ_q² at ⁵⁶Fe). This is in scope, non-circular, and the cleanest open target in the arc.
