# The 2026-07-08 "exact topological derivation of c_3" is a muon-anchored fit — re-scope

**Date:** 2026-07-11 · **Axis:** z→c_k f-map keystone (c_3 discipline)
· **Tier:** structural-exact (cross-anchor refutation) · **Discipline:** flip-flop guard
(registry §8), anti-laundering ("Axiomatization is NOT a Proof"), refuted-scope (a)/(b).

Re-scopes [`2026-07-08-qbeta-keystone-derivation.md`](2026-07-08-qbeta-keystone-derivation.md)
(commit `e21a942632`), which claims **"PROVEN, LEAN-CERTIFIED, first-principles
topological derivation"** of `c_3 = −Vol(4₁) + u − (10/3)u²`. Verification probe
[`qbeta_c3_keystone_overclaim_verification.py`](scripts/qbeta_c3_keystone_overclaim_verification.py)
(6/6).

**This is not a hostile finding.** The *numerical near-match at the muon anchor is
real* and worth keeping. What is wrong is the **scope**: "PROVEN / exact
derivation." Per the refuted-discipline, the fix is to re-scope from a claimed
derivation to a **muon-anchored numerical near-match that fails the proton
cross-anchor** — the number stands, the claim does not.

## The cross-anchor test the claim skipped (registry §8 requires it)

The formula's only q-dependence is `u = b·ℏ_q²`, which is **anchor-invariant to
2×10⁻⁷** across the proton/muon pins. So it returns **one fixed value** while c_3
swings 2.4%:

| anchor | c_3 (canonical, 2026-07-06 verdict) | formula `−Vol(4₁)+u−(10/3)u²` | miss |
|---|---|---|---|
| muon | −2.020188 | −2.021619 | **0.07 %** (near-match) |
| proton | −2.069343 | −2.021619 | **2.31 %** (the whole swing) |

The registry §8 flip-flop guard **mandates a proton+muon cross-anchor test before
any c_k≥3 is called derived**; c_3 fails it (2.31 % proton miss). c_3 stays tier
**empirical**.

## Four independent problems

1. **Its own `O(u³)` bound is false.** The doc claims "residual zero within the
   `O(u³)` truncation." The `O(u³)` relative bound is `3.05×10⁻⁷`; the actual muon
   residual is `7.08×10⁻⁴` — **2325× larger** than the claimed bound. Even the muon
   "match" is 3+ orders of magnitude looser than advertised.
2. **Sector conflation.** It uses `−Vol(4₁) = −2.030` as the leading term, but that
   is the **even / amphichiral** face (`CS(4₁)=0`, the *mass* face — #3482/#3487).
   The c_3 near-match `−2` is `J_Hopf(q=1)`, the **odd / chiral** face (the *decay*
   face — #3487, #3489). They are numerically close (Δ=0.03) but structurally
   distinct channels; the derivation puts an even-sector constant where the
   odd-sector value belongs.
3. **The Lean "certification" is vacuous.** `QBetaKeystoneInteraction.lean`'s
   `c_3_keystone_structure` proves `c_3_keystone V u interaction_factor =
   −V + u − (10/3)u²` **by `rfl`**, after hardcoding `Vol_4_1 := 2.029883…`,
   `substrate_u := 0.008505…`, and `interaction_factor := 10/3` as decimal
   literals. It proves *definition = definition*. Zero mathematical content — the
   exact "Axiomatization is NOT a Proof" anti-pattern (AGENTS.md).
4. **The `10/3` is post-hoc knot-picking.** `T₃,₅` (writhe 10) / `3₁` (writhe 3)
   are chosen so `[10]_q/[3]_q → 10/3` reproduces the *fitted* u² coefficient. The
   limit is a trivial `q→1` L'Hôpital; the derivation is choosing the knots to hit
   the number, not deriving the number.

## Production is safe

The commit did **not** wire c_3 into production (grep clean:
`canonical_mass.py` / `derived_masses.py` / registry / dashboards unchanged). So no
table moved. The damage is a durable **"PROVEN" artifact on main that contradicts
the registry** (still tier empirical) and would mislead future agents into
re-opening the settled flip-flop.

## Actions taken (in-place re-scope, per discipline)

- This rebuttal doc + verification probe (6/6).
- Corrected the header of `2026-07-08-qbeta-keystone-derivation.md`: status
  `PROVEN, LEAN-CERTIFIED` → `MUON-ANCHORED NEAR-MATCH — not a derivation (fails
  proton cross-anchor); see this rebuttal`. The numerical observation is kept.
- Flagged `QBetaKeystoneInteraction.lean` with a corrective docstring (the theorem
  is a definitional identity, not a derivation of c_3).

## Cross-references

- Verification: [`qbeta_c3_keystone_overclaim_verification.py`](scripts/qbeta_c3_keystone_overclaim_verification.py)
- Target: [`2026-07-08-qbeta-keystone-derivation.md`](2026-07-08-qbeta-keystone-derivation.md)
- Cross-anchor verdict (6th settle): [`2026-07-06-c3-not-exact-cross-anchor-verdict.md`](2026-07-06-c3-not-exact-cross-anchor-verdict.md)
- Correct sector split: [`2026-07-07-parity-chirality-dictionary-closed.md`](2026-07-07-parity-chirality-dictionary-closed.md) (#3487)
- Truncation-order framing: [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
