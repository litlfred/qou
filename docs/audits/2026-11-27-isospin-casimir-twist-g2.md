# Gap G2: the `T(T+1)` term of the braid channel, block by block

Date: 2026-11-27. Bean: `qou-tcl2` (PR #9660), under `qou-myts`. Ledger: PR #9658,
`docs/audits/2026-11-27-term-completeness-ledger.md` §5, row G2.
Lean: `QOU/Nuclear/IsospinCasimirTwist.lean` (generic field / `ℤ`, no measured value).

## 1. Result

The ledger says the binding closed form `τ_p^Z τ_n^N ∏ f_i` and the q-CLT proxy have no
dependence on the convention-D block, so no `T(T+1)` term, and that `Q_β` therefore has no
isobaric parabola. Its prescribed method is to evaluate the trace block by block at level
`n = 3A` over the `⌊n/2⌋ + 1` two-row blocks.

For the one central braid-channel element whose block scalar the representation theory fixes
without further input, the **Murphy product** `Φ_n = L_0 L_1 ⋯ L_n` (the full twist, by the cited
identity `Δ² = L_1 ⋯ L_n`), this is now proved:

| statement | Lean |
|---|---|
| `Φ_n` acts on every seminormal block `μ` by `q^{2c(μ)}`, `c(μ)` = content sum | `seminormalRep_murphyProd_scalar` |
| the same on every Wedderburn block of `H_{n+1}(q)` (char 0) | `heckeWedderburn_murphyProd` |
| two-row block `(m,k)`, `n = m+k`, `t = m−k = 2T`: `4c = t(t+2) + n(n−4)` | `four_contentSum_twoRow` |
| so `(q^{2c})² = q^{t(t+2)} · q^{n(n−4)} = q^{4T(T+1)} · q^{n(n−4)}` | `twoRow_murphyScalar_sq` |
| at fixed `n`, blocks differ only by `q^{2[T(T+1) − T'(T'+1)]}` | `twoRow_murphyScalar_ratio` |
| checks: `n = 3` (`4c = 12, 0`), `n = 6` (`4c − 4T(T+1) = 12` on all four blocks) | `contentSum_level_three`, `contentSum_level_six` |

So the block-dependent entry that G2 asks for is `T(T+1)`, and its coefficient is **2** (in
powers of `q`), the same at every level `n`. That 2 is the factor in the corpus Murphy convention
`L_k ↦ q^{2·content}`. Nothing is fitted, and the `n`-only factor `q^{n(n−4)/2}` is common to
every block at a given level, so it moves the whole level, not the split between blocks.

Why `T(T+1)`: the content sum of a two-row diagram is `T(T+1) + n(n−4)/4`. At `q = 1` this is
the classical statement that the sum of all transpositions acts on the isospin-`T` block as
`Σ_{i<j} P_ij = T(T+1) + n(n−4)/4`, which is the two-body form of the isospin Casimir. The
`q`-deformed statement is multiplicative (the twist), not additive.

## 2. The isobaric parabola

A nucleus `(Z, N)` has `T_z = (Z−N)/2`. The blocks containing that weight have `T ≥ |T_z|`.
On the lowest, `T = |T_z|`, with `d = N − Z`:

- `4T(T+1) = d² + 2|d|`: a parabola in `T_z` with a cusp at `T_z = 0` (`casimir4_lowest`).
- `T = |T_z|` is the block of least `T(T+1)` among those containing the weight
  (`casimir4_lowest_le`).
- one `β⁻` step `(Z,N) → (Z+1,N−1)` changes `4T(T+1)` by `4d` for `d ≥ 2`, by `0` at `d = 1`
  (the mirror pair, same `T = 1/2`), and by `4d − 8` for `d ≤ 0`
  (`casimir4_beta_step_pos`, `_one`, `_nonpos`).

Which block a nucleus occupies is not decided here. The lowest-block choice is a hypothesis
wherever it is used.

## 3. Scope: what this does not settle

1. **`Φ_n = Δ²`** is cited ([murphy1992] §2; [kassel-turaev2008] §4.3), not proved. No
   theorem here uses it. `KeystoneJucysMurphyTwist.JucysMurphySpectrum` carried the twist's
   block scalar as a hypothesis; `heckeWedderburn_murphyProd` is that hypothesis for `Φ_n`,
   discharged on every block.
2. **That a nucleus's operator contains `Φ_{3A}`** is a statement about the word, which is gap
   G5 and outside the ledger. For a general word `β` the block character `χ_T(β)` depends on the
   word and need not be a function of `T(T+1)`. What this file shows is that the block entry for
   the twist exists, has the form `T(T+1)`, and comes with a fixed coefficient.
3. **No energy scale.** The q-CLT proxy maps a log-product to energy as
   `B = −α Σ ln|V|` with `α = 8G·m_e` (`mass_table_comprehensive.py:try_binding_q_clt_proxy`).
   Carrying the twist factor through that map would give a term `∓ 2α·T(T+1)·ln q`. That is
   producer work: it changes the numbers a reader sees, and the sign follows from the word's
   orientation, which is the G5 question. It is not done in this PR. The analytic step (`ln q`)
   also belongs under the transcendental boundary, so the Lean statement stays multiplicative.
4. The convention-D trace of `Φ_n` itself follows by summing the block scalars against the
   two-row weights `[n−2k+1]_q/[2]_q^n · d_λ`. It is not formalised here.

No value in this note enters a proof.
