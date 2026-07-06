# ζ_8 cancellation categorical witness — IDENTIFIED (2026-06-01)

> Track 2 of [PR #1625](https://github.com/litlfred/qou/pull/1625):
> identifies the categorical witness of the universal cancellation
> `S_6(ζ_8) + Δa_7(ζ_8)·(ζ_8;ζ_8)_7 = 0` discovered in Track 1
> ([`docs/audits/2026-06-01-qbeta-habiro-delta-am-partial-sum-scan.md`](2026-06-01-qbeta-habiro-delta-am-partial-sum-scan.md)).
>
> Probe: [`computations/qbeta/qbeta_habiro_zeta8_categorical_witness.py`](../../computations/qbeta/qbeta_habiro_zeta8_categorical_witness.py)
> Witness: [`computations/qbeta/qbeta-habiro-zeta8-categorical-witness.witness.json`](../../computations/qbeta/qbeta-habiro-zeta8-categorical-witness.witness.json)

## TL;DR

**IDENTIFIED.** The categorical witness of the universal Φ_8² factor in atomic-step Habiro elements is the **Level-2 SU(2) Verlinde truncation of H_n(q) at q = ζ_8**, characterised by the **Wenzl projector kernel** for partitions with first column length ≥ k+2 = 4. The universal `S_6(ζ_8) + Δa_7(ζ_8)·(ζ_8;ζ_8)_7 = 0` cancellation expresses the linear relation forced by the Wenzl annihilator on the Markov-trace decomposition of all canonical braid words.

## Three confirming facts

| Identity | Value | Implication |
|---|---|---|
| **`(ζ_8; ζ_8)_7 = 8`** exactly | integer (not a generic algebraic number) | Natural normalisation; equals `ord(σ_i in H_n(ζ_8))` |
| **`σ_i` order in `H_n(q=ζ_8)`** | **8** | `M_first_Φ_8 = 7 = ord(σ_i) − 1` ⇒ Track 1's universal boundary is the σ-order boundary |
| **`[4]_q = 0` at q = ζ_8** | first vanishing quantum integer | Wenzl projector annihilator kicks in at partition first-column = 4 (= k+2 for k=2) |
| **WZW correspondence**: `q = e^(iπ/(k+2)) ⇒ k = 2` for `q = ζ_8` | level-2 SU(2) | matches the WZW root-of-unity formula |
| Per-pair `Δa_7(ζ_8) = −S_6(ζ_8) / 8` | exact algebraic equality (residual = 0) | Verified for ALL THREE pairs (D−n), (³He−D), (⁴He−³He) |

## The categorical content

At `q = ζ_8 = e^(iπ/4)`, the Iwahori–Hecke algebra `H_n(q)` is no longer semisimple. The non-semisimple structure is the **Wenzl projector kernel**: irreducible representations `S^λ` for partitions `λ` with first-column length `≥ k+2 = 4` are *negligible* (have zero quantum trace).

This corresponds to the **Level-2 SU(2) WZW model** — only 3 highest weights survive: `j = 0, 1/2, 1` (matching partitions of `≤ 3` cells in first column).

For the Markov-trace decomposition `tr_M(β_K, q) = Σ_λ y_λ · χ^λ(β_K)` of any canonical braid word, the Wenzl annihilator forces:

$$\sum_{\lambda: \, \text{first col} \geq 4} y_\lambda(\zeta_8) \cdot \chi^\lambda(\beta_K; \zeta_8) \;=\; 0$$

— a structural relation that the *full* Habiro coefficient ladder must respect. Taking differences `Δa_m(X − Y)`, this relation translates into the universal `S_6 + Δa_7·8 ≡ 0 (mod Φ_8)` cancellation.

## Connection to the strand-doubling FALSIFICATION

In the earlier [`2026-06-01-qbeta-habiro-phi8-interpretation.md`](2026-06-01-qbeta-habiro-phi8-interpretation.md), hypothesis (a) — "Hecke at level-2 SU(2) (q² = −1)" — was ruled out as "FALSE in naive form" because "there is no quantum-group level-2 truncation acting on D−n". **That ruling-out was premature.** The level-2 truncation DOES act, but it acts via the **Wenzl annihilator forcing linear relations on the Markov trace**, NOT via a direct (D−n) action — which is why the naive test missed it.

The current Track 1 + Track 2 framing — **"Δa_m interference relations at ζ_8"** rather than "(D−n) directly carries the cyclotomic" — was the missing piece.

## Implications

1. **Φ_8² is structural-categorical**, with a precise definition: the squared Wenzl annihilator (at the [4]_q = 0 vanishing root + its bar-conjugate [−4]_q = 0).

2. **The first-Φ_8 boundary at M=7** has a clean closed form: `M_first_Φ_8 = ord(σ_i in H_n(ζ_8)) − 1 = 7`.

3. **The pair-dependent Φ_8² boundary** (12 for deuteron-pair, 15 for helium pairs) likely tracks the *second* Wenzl annihilator (at [8]_q = 0?) — needs follow-up to confirm.

4. **Falsifiable predictions**:
   - Every isospin-flip OR atomic-step Habiro element on ANY pair of canonical braid words should show `M_first_Φ_8 = 7` (the Wenzl boundary is independent of which two braids you compare).
   - At higher roots of unity ζ_{12}, ζ_{16}, similar Wenzl annihilators may produce additional universal `Φ_{n}` factors at correspondingly-shifted M boundaries.

5. **The Q_β Habiro element keystone**: the canonical formula for the Q_β Habiro element should encode the Wenzl annihilator explicitly. Working ansatz:
$$\text{Q-beta-Habiro}(q) \;=\; (\text{universal Wenzl factor}) \cdot (\text{pair-specific residual})$$
where the universal Wenzl factor includes the squared kernel `[k+2]_q²` and the residual depends on the specific (p, n, D, ³He, ⁴He) coefficient data.

## Lean formalisation targets

1. **`H_n(ζ_8)` Wenzl annihilator**: theorem stating that partitions with first-column ≥ 4 have zero quantum trace. Mathlib has cyclotomic infrastructure; the Hecke algebra side needs Wenzl-projector definitions.

2. **`σ_i` order in `H_n(ζ_8)` = 8**: theorem `Polynomial.Hecke.sigma_order_at_zeta8`. From the Hecke relation `(σ_i − q)(σ_i + q⁻¹) = 0` at q = ζ_8: eigenvalues are `ζ_8` and `−ζ_8⁻¹`. The minimal polynomial has order lcm(8, 8) = 8.

3. **(ζ_8; ζ_8)_7 = 8**: pure algebraic identity, Lean-provable by `decide` or direct sympy-style proof.

## Cross-references

- Track 1 (universal M=7 boundary): [`2026-06-01-qbeta-habiro-delta-am-partial-sum-scan.md`](2026-06-01-qbeta-habiro-delta-am-partial-sum-scan.md)
- Original Φ_8 audit (hypothesis (a) NOW VINDICATED): [`2026-06-01-qbeta-habiro-phi8-interpretation.md`](2026-06-01-qbeta-habiro-phi8-interpretation.md)
- Strand-doubling FALSIFIED: [`2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md`](2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md)
- z(q)² REFUTED: [`2026-06-01-qbeta-habiro-phi8-squared-mechanism.md`](2026-06-01-qbeta-habiro-phi8-squared-mechanism.md)
- Phase 5q convention test (Φ_8² survives): [`2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md`](2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- This branch ledger: [`docs/coordination/2026-06-01-phi8-da-m-interference.md`](../coordination/2026-06-01-phi8-da-m-interference.md)
