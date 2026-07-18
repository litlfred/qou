# Δ_λ gate — forward (non-fit) test of the parameter-free per-pair bond magnitude

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-perpair-magnitude-derive-2026-07-18`
· **Type:** FORWARD (parameter-free → predicted → compare) test of the ONE remaining
gated Δ_λ scalar. **No fit, no tuning, no wiring, no AME inversion.**
**Probe:** [`computations/deltalambda/deltalambda_perpair_bond_magnitude_derive_probe.py`](../../computations/deltalambda/deltalambda_perpair_bond_magnitude_derive_probe.py)
(witness `deltalambda-perpair-bond-magnitude-derive.witness.json`, 4/4 assertions).

## 0. The one gated scalar

Everything *around* the ≥4-body [1⁴] term is DERIVED (merged #3924,
`b4_slater_antisymmetrizer_exchange_sign.py`): ⁴He-locality `C(4,A)=0` for `A>4`
(exact), the exchange spectrum `eig(S)={±√5,±1}` ⇒ closed form
`det(I+mS)=(1−5m²)(1−m²)`, the attractive sign (a negative eigenvalue `−√5·m` is
present for any `m`), and the physicality ceiling `m < 1/√5`. The **single**
undetermined quantity is the **per-pair bond magnitude `m`** — the standing Δ_λ
Track-A gate on which six parameter-free ansätze have failed and for which a
seventh **fit-based** ansatz is forbidden (AGENTS.md).

The single-trace `Δ_λ = (−1)^{n(λ)}·dim` binding `|B_dim|` undershoots AME; the
residual `target/|B_dim|` is `{²H 5.85, ³H 4.44, ³He 3.29, ⁴He 9.31}` (committed
`deltalambda-o1-manybody-residual.witness.json`, consumed as a derived-elsewhere
input, not recomputed). The ≥4-body det term `b = −ln det(I+G)` must supply the
**deficit** `target − B_dim`.

## 1. Method — forward only, never inverted

The corpus supplies **exactly two** parameter-free per-pair magnitudes (no third:
the classical ceiling `1/√5` is the `det=0` boundary where `−ln det` diverges, and
the sine/tangent relation collapses `g = z/√(1+z²)`):

| candidate | value | provenance |
|---|--:|---|
| `z_naive = 1/[2]_v` | 0.499320 | Markov-peel bond factor (TL conditional-expectation weight) |
| `g_reeb = 1/√(5+(q₀−1)²/q₀)` | 0.446727 | CWF/sine-normalized (reeb audit 2026-07-06) |

Each `m` is fixed **first**, parameter-free; the four deficits are **predicted** by
evaluating the exchange determinant on each isotope's complete graph `K_A`
(pp=+1, nn=−1 derived signs; pn=±1 det-invariant by `diag(1,1,−1,−1)` conjugation,
Lean-proved `ReebPnMagnitude.lean`), dressed by `E₀ = m_e/(q(q−1)) ≈ 4.186` MeV;
and **only then** compared. A genuine derivation reproduces all four deficits
with zero free parameters (deficit-ratio ≈ const). Solving `m` from the residuals
would be the forbidden seventh fit — it is **not** done.

## 2. Result

`E₀ = 4.1860` MeV, `q₀ ≈ 1.109979`.

**`m = z_naive = 0.499320` — EXCLUDED.** `det(I+G) = −0.185 < 0` at ⁴He
(exceeds the `1/√5` ceiling): the ⁴He deficit cannot be supplied at all. (Its ³H
`det/deficit = 3.69` is grossly off regardless.)

**`m = g_reeb = 0.446727` — physical for all four, but NO simultaneous match:**

| iso | A | det(I+G) | det-term MeV | deficit MeV | det/deficit | det/AME |
|---|---|--:|--:|--:|--:|--:|
| ²H | 2 | 0.80043 | 0.932 | 1.844 | **0.505** | 0.419 |
| ³H | 3 | 0.22300 | 6.281 | 6.573 | **0.956** | 0.741 |
| ³He | 3 | 0.57961 | 2.283 | 5.373 | **0.425** | 0.296 |
| ⁴He | 4 | 0.0017407 | 26.596 | 25.257 | **1.053** | 0.940 |

The `det/deficit` ratios are **non-monotone** and spread by **2.48×** (0.425 →
1.053). The **³H/³He mirror pair** — identical `B_dim` braid topology
(n_strands=9, 30 partitions) — splits by **2.25×** in the det-term while their
deficits differ only **1.22×**. A parameter-free per-pair magnitude that
*derived* the deficit would give a flat ratio; it does not.

## 3. Verdict — HONEST NEGATIVE, gate stands

The parameter-free palette is **exhausted**: `z_naive` is unphysical at A=4;
`g_reeb` is physical but reproduces **none** of the four deficits at a common
scale. No single parameter-free `m` closes the gate. This corroborates, in the
deficit framing, the corpus findings that (a) no uniform per-pair magnitude fits
both A=2 and A=4 in the det form (reeb audit §3c), (b) the `{z, g}` palette has no
surviving non-uniform option (§3h), and (c) many-body binding is **collective /
non-additive** (§2i) — the residual is not a per-pair det-term at a fixed
categorical magnitude. The `A`-flattened normalization that *would* fix `m` is the
Δ_λ closure itself (§2j), which is gated.

**Classification.** DERIVED (unchanged, #3924): locality, sign, ceiling.
**Δ_λ magnitude gate: STILL OPEN** — this forward test neither closes it nor
narrows the parameter-free palette below the two already-known candidates, both
of which miss. This is the expected, valid outcome after six failed ansätze.

**Not done (STRICT):** `m` was never solved from the residuals; nothing is wired;
no AME point was inverted. A magnitude tuned to flatten the four ratios would be
the forbidden seventh fit-based ansatz.

## 4. Cross-references

- [1⁴] locality/sign/ceiling (DERIVED): [`docs/audits/2026-07-18-deltalambda-manybody-4body.md`](2026-07-18-deltalambda-manybody-4body.md), `b4_slater_antisymmetrizer_exchange_sign.py` (#3924).
- Reeb-flow magnitude provenance + collective-binding findings: [`docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`](2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md) (§2i collective, §3c uniform-magnitude irreconcilability, §3h palette exhaustion, §2j Δ_λ-gate identification).
- Single-trace residual `{5.9,4.4,3.3,9.3}`: `deltalambda_o1_manybody_probe.py`.
- pn-sign det invariance / `1/√5` ceiling (Lean): `QOU/MassTheory/ReebPnMagnitude.lean`.

EXPLORATORY — audit + witness only; no production wiring, no fit, no AME inversion.
