# Audit & Formalization Ledger — Framed Braid Monodromy Twist Multisets (`qou-kebu`) & `sRow3` Fintype / Braid-Twist Foundations (`qou-jkmh`)

**Date:** 2026-11-24
**Beans:** `qou-kebu` (*T2b: derive per-strand twist multisets from framed braid words*), `qou-jkmh` (*Close `sRow3` Derivation Seam: Prove `≥ 3`-Row Signed Springer-Dimension Table from Hook-Length & Framed Braid Data*)
**Lean 4 Formalizations (`0 sorry`, `0` custom axioms, §7c clean, `BP001`–`BP009` compliant):**
- [`QOU/StandardModel/FramedBraidTwistMonodromy.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/FramedBraidTwistMonodromy.lean)
- [`QOU/MassTheory/ThreeRowSpringerFintypeAndBraidTwist.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/ThreeRowSpringerFintypeAndBraidTwist.lean)
**80-dps & Exact Symbolic Verification Probe & Witness:**
- [`computations/probes/framed_braid_twist_and_srow3_audit_probe.py`](../../computations/probes/framed_braid_twist_and_srow3_audit_probe.py)
- [`computations/probes/framed-braid-twist-and-srow3-audit.witness.json`](../../computations/probes/framed-braid-twist-and-srow3-audit.witness.json)

---

## 1. Upstream State on `origin/main` & Non-Overlapping Scope vs Queued Sibling PR `#9265`

Before writing Lean, `origin/main` (`711de6a488d`) and queued Batch-7 PR `#9265` (`claude/backlog-drain-batch7-20261123`, `83a784c4bdd`) were inspected to prevent merge collisions (`overlapKind = "none"`):

1. **`qou-kebu`:**
   - Already on `origin/main`: `QOU/StandardModel/ComponentFraming.lean` (abstract `IsComponentFraming π t` over `Equiv.Perm (Fin n)`) and `QOU/StandardModel/SignCoherentTwist.lean` (`d_multiset_forced`, `u_multiset_forced`).
   - Queued in PR `#9265`: `QOU/StandardModel/HopfFramingAndHirzebruchDefect.lean` (`piHopf = swap 0 2` on `Fin 3`, `exists_incoherent_in_range_iff`, `CategoricalRibbonHyperchargeDerivationHypothesis`).
   - **Unformalized mathematical gap closed here (`FramedBraidTwistMonodromy.lean`):** Neither `ComponentFraming` nor `#9265` constructed the **semidirect framed braid word monoid** $\mathbb{Z}^n \rtimes B_n^*$ over actual `QOU.BraidKnot.BraidWord n` words and `QOU.Knot.BraidClosure.closurePerm`, nor derived closed-component constancy from **Markov-I pure-twist conjugation coboundaries** $\tau_i \mapsto \tau_i + \delta_i - \delta_{\pi(w)^{-1}(i)}$.
   - **Upstream Rule-13a dependency preserved:** Deriving each chiral fermion's **total** twist $T = 3Q$ and hypercharge formula $Y_t = 2(T/3 - I_3)$ from QOU categorical axioms remains open under `qou-qvpl` Open Check A (and per-chiral-fermion quark words under `qou-h0zz`); per Rule 13a, `qou-kebu` stays tracked against `qou-qvpl` until Check A lands.

2. **`qou-jkmh`:**
   - Already on `origin/main` (`917b6939954`): `QOU/MassTheory/ThreeRowSpringerSYTDerivation.lean` (`sRow3Derived_eq_sRow3` over the fuel-based list enumerator `partitionsOf k` for $k \le 5$), with downstream docstring updates queued in `#9265`.
   - **Unformalized mathematical gaps closed here (`ThreeRowSpringerFintypeAndBraidTwist.lean`):**
     1. **All-$k$ Mathlib `Nat.Partition k` / `dimSYT` Fintype bridge:** `sRow3NatPartition_eq_sRow3Derived` proves for **all** $k \in \mathbb{N}$ (via `PartitionsOfBridge.sum_map_partitionsOf` and `IdentityIHLFBridge.dimSYT_eq_dimHLF`) that the abstract `Fintype` sum over `Nat.Partition k` and genuine `StandardYoungTableau` cardinalities `dimSYT p` equals `sRow3Derived k`, discharging `sRow3NatPartition_eq_sRow3` for all $k \le 5$ and structural vanishing for $k \le 2$ without `decide`.
     2. **Framed-braid half-twist & central full-twist content identity:** proves `sRow3NatPartition_eq_columnHalfTwistParity_sum` (all $k$) and `diagramContentSum_eq_rowHalfTwist_sub_colHalfTwist`, locking the central ribbon-twist exponent $c(\lambda) = \sum_{(i,j)\in\lambda}(j - i)$ to the difference between the Young row half-twist crossing count $\sum_i \binom{\lambda_i}{2}$ and the Young column half-twist crossing count $\sum_j \binom{\lambda'_j}{2} = n(\lambda)$.
     3. **Temperley–Lieb (`\ell(\lambda) \le 2`) vs `\ell(\lambda) \ge 3` kernel decomposition & $k \le 8$ extension:** proves `sTotalDerived_eq_sRowLe2_add_sRow3` for all $k \in \mathbb{N}$ and exact higher-cluster values `sRow3NatPartition (6, 7, 8) = (16, -15, -132)` (alongside the alternating signed Catalan sequence `sRowLe2Derived (0..8) = [1, 1, 0, -1, 0, 2, 0, -5, 0]`).

---

## 2. Exact Coboundary & Springer Stratum Reference Tables

### 2.1 `FramedBraidWord 3` Markov-I Coboundary Classification (`qou-kebu`)

| Corpus `BraidWord 3` Carrier | Word | `closurePerm w` | `components w` | $\mathrm{rank}_{\mathbb{Z}}(I - P_{\pi^{-1}})$ | Slide Coinvariant $H_0(\langle\pi\rangle, \mathbb{Z}^3)$ | Forced Multiset in $\{-1,0,1\}^3$ |
|---|---|---|---|---|---|---|
| `leptonUnknotWord3` ($\nu$) | `σ₀ σ₁` | `(0 1 2)` | `1` | `2` | $\mathbb{Z}$ (`totalTwist`) | `{0, 0, 0}` at $T = 0$ (`3 ∣ T` required for symmetric component framing) |
| `leptonTrefoilWord3` ($e^-$ knot backup) | `(σ₀ σ₁)²` | `(0 2 1)` | `1` | `2` | $\mathbb{Z}$ (`totalTwist`) | `{-1, -1, -1}` at $T = -3$ |
| `hopfElectronWord3` ($e^-$ primary) | `σ₀ σ₁ σ₀` | `(0 2)` | `2` | `1` | $\mathbb{Z}^2$ (`(τ₀ + τ₂, τ₁)`) | `{-1, -1, -1}` at $T = -3$ |
| `borromeanBraidWord3` ($u, d$ sector) | `(σ₀ σ₁⁻¹)³` | `1` | `3` | `0` | $\mathbb{Z}^3$ (`(τ₀, τ₁, τ₂)`) | `{0, 1, 1}` at $T = +2$; `{-1, 0, 0}` at $T = -1$ (sign-coherent normal form) |

### 2.2 Temperley–Lieb (`\ell \le 2`) vs Killed `\ell \ge 3` Springer Stratum (`qou-jkmh`, $k = 0\dots 10$)

| $k$ | `#(Nat.Partition k)` | `sTotalDerived k` | `sRowLe2Derived k` ($\ell \le 2$, TL) | `sRow3NatPartition k` ($\ell \ge 3$, TL kernel) |
|---:|---:|---:|---:|---:|
| 0 | 1 | `1` | `1` | `0` |
| 1 | 1 | `1` | `1` | `0` |
| 2 | 2 | `0` | `0` | `0` |
| 3 | 3 | `-2` | `-1` | `-1` |
| 4 | 5 | `-2` | `0` | `-2` |
| 5 | 7 | `6` | `2` | `4` |
| 6 | 11 | `16` | `0` | `16` |
| 7 | 15 | `-20` | `-5` | `-15` |
| 8 | 22 | `-132` | `0` | `-132` |
| 9 | 30 | `28` | `14` | `14` |
| 10 | 42 | `1216` | `0` | `1216` |
