# Re-scope: the `c₃ = −Vol(4₁) + u − (10/3)u²` keystone is a muon-anchor near-match, not an exact derivation

**Date:** 2026-07-11 · **Axis:** z→c_k f-map keystone (c₃ tier) ·
**Corrects:** [`2026-07-08-qbeta-keystone-derivation.md`](2026-07-08-qbeta-keystone-derivation.md)
(commit `e21a9426`, Status: "PROVEN, LEAN-CERTIFIED") ·
**Tier:** measurement-exact (scope-(a) re-scope) · **No `c_k` wired; production unchanged.**

## What was claimed

`2026-07-08-qbeta-keystone-derivation.md` states that
`c₃ = −Vol(4₁) + u − (10/3)u²` is an **exact theorem**, "Lean-certified," and
that "**c₃ is no longer an empirically calibrated input** … the entire Q_β
precision ladder is now derived from first principles." The formula is evaluated
**at the muon anchor** only.

## The measurement — anchor-blind, single-anchor near-match

Probe [`qbeta_c3_keystone_anchor_blind_probe.py`](../../computations/qbeta/qbeta_c3_keystone_anchor_blind_probe.py)
→ [witness](../../computations/qbeta/qbeta-c3-keystone-anchor-blind.witness.json)
(6/6; anchors from `qou_substrate.q_at`/`q_muon_at`, 50 dps):

| anchor | claim `−Vol(4₁)+u−(10/3)u²` | actual c₃ (`c3_target_at`) | miss |
|---|---|---|---|
| **muon** | −2.021608 | −2.020200 | **0.070%** ✓ |
| **proton** | −2.021608 | −2.069343 | **−2.307%** ✗ |

The formula gives **≈ −2.0216 at *both* anchors** (Vol(4₁) is a fixed constant;
`u` moves by ~10⁻⁸ between anchors), while the actual c₃ **swings 2.43%**. So the
formula reproduces the *muon-anchored* c₃ to 0.07% and **misses the proton anchor
by 2.3%** — a single-anchor near-match, **scope-(a)**, not a derivation of the
anchor-swinging c₃.

## Why the "exact theorem" tier is over-claimed

1. **Fails the registry §8 cross-anchor guard.** "A wired c_k≥3 needs a passing
   proton+muon cross-anchor swing < 1%." This is 2.3% > 1%.
2. **Contradicts the live registry §3** — c₃ is "EMPIRICAL — near-match, REFUTED
   as real-q fibre element … swings." The derivation doc did not update the
   registry; the two are inconsistent on `main`, and the registry is authoritative.
3. **Contradicts the c₃-not-exact verdict** ([2026-07-06](2026-07-06-c3-not-exact-cross-anchor-verdict.md),
   the 6th settle) and the [3-rung rigidity falsification](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md).
4. **The Lean does not derive c₃.** `QBetaKeystoneInteraction.lean` *defines*
   `c_3_keystone V u interact := −V + u − interact·u²` and `interaction_factor := 10/3`,
   and `c_3_keystone_structure` is `unfold`-and-done — it proves the definition
   equals its own formula (a tautology), not that this equals the physical c₃.
   Per AGENTS.md §"Axiomatization is NOT a Proof": defining c₃ to be the formula
   is not deriving it.
5. **Contradicts the careful sibling framing.** [#3487 parity-chirality
   dictionary](2026-07-07-parity-chirality-dictionary-closed.md) + #3474 split c₃
   into a **solved bar-even part** (real, `4₁`-amphichiral) and an
   **anchor-swinging bar-odd part (S, complex, Subgoal-2)**, explicitly: "It does
   **not** derive S … remains Subgoal-2."

## What is kept (the structural pieces are real)

This is a **re-scope, not a refutation** — the numerical/structural content stands:

- **`−Vol(4₁)` is the legitimately-solved bar-EVEN part** of c₃ (the amphichiral
  `4₁` real-volume face; #3474/#3487). `Vol(4₁) ≈ 2.02988`.
- **`10/3 = lim_{q→1} [10]_q/[3]_q` is an exact writhe-ratio identity**
  (T_{3,5} mediator crossings / 3₁ electron crossings) — verified symbolically.

What is corrected is only the **tier**: the anchor-swinging remainder of c₃ (the
CAL-2 S-leak) is **Subgoal-2** and is *not* captured by an anchor-blind real
formula. The `+u − (10/3)u²` correction fits the muon odd-residual; it cannot
also fit the proton one, which is what the 2.4% swing measures.

## Disposition

- **Registry §3** already reads c₃ EMPIRICAL/REFUTED — correct; a reconciliation
  bullet is added pointing here.
- A one-line **correction banner** is added atop `2026-07-08-qbeta-keystone-derivation.md`
  pointing to this audit (supersession-banner pattern, §7).
- The Lean (`QBetaKeystoneInteraction.lean`) is left to the owner/originating
  branch; this audit flags it as an axiomatized definition, not a derivation.

## Cross-references

- Corrected doc: [`2026-07-08-qbeta-keystone-derivation.md`](2026-07-08-qbeta-keystone-derivation.md)
- Registry: [`ck-dk-canonical-registry.md` §3 + §8](../coordination/ck-dk-canonical-registry.md)
- c₃-not-exact verdict: [`2026-07-06-c3-not-exact-cross-anchor-verdict.md`](2026-07-06-c3-not-exact-cross-anchor-verdict.md)
- Even part solved / odd part Subgoal-2: [`2026-07-07-parity-chirality-dictionary-closed.md`](2026-07-07-parity-chirality-dictionary-closed.md)
