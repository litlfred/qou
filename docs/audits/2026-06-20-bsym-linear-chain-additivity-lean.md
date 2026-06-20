# B_sym linear-chain additivity — Lean formalization (2026-06-20)

**Status:** audit — formalize-first follow-up. Discharges bean `6z40`
("B_sym #2: formalize linear-chain additivity in Lean … BLOCKED: Lean toolchain
un-installable"). The toolchain is available this session (Mathlib oleans restored
from `lake-cache/qou-v4-24-0`), so the structural content is now a checked theorem.

## The distinction the bean draws

`B_sym = α·ln(tr_free/tr_atom)` is a **definition + empirical claim**, not a
theorem — in Lean it would only be a trivial `subst;rfl`. What *is* provable is the
#2343 **linear-chain additivity**
([`2026-06-16-b-sym-linear-chain-closed-form.md`](2026-06-16-b-sym-linear-chain-closed-form.md)):
the bound atom braid orders strands `p^Z n^N` with crossings only between adjacent
nucleons, so the chain carries `(Z−1)` p-p bonds, `1` p-n interface bond, `(N−1)`
n-n bonds (`A−1` total), and — because each crossing sits on a distinct Hecke
generator — the log-binding factorizes additively over the bonds.

## What is formalized

[`content/quantum-observable-universe/lean/QOU/BraidKnot/BsymLinearChain.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/BsymLinearChain.lean)
(namespace `QOU.BraidKnot.BsymLinearChain`). **Verified sorry-free via lean-direct**
(`lean` exit 0).

| Lean decl | statement |
|---|---|
| `Bond`, `chainBonds` | the three bond types; the ordered chain bond list `replicate (Z−1) pp ++ pn :: replicate (N−1) nn` |
| `chain_num_bonds` | `‖chainBonds Z N‖ = Z + N − 1` for `Z,N ≥ 1` (the `A−1` total) |
| `chain_count_pp/pn/nn` | per-type counts `Z−1`, `1`, `N−1` |
| `chain_binding_sum` | `Σ` of per-bond `L : Bond → R` over the chain `= (Z−1)•L_pp + L_pn + (N−1)•L_nn` |
| `Bsym_closed_form` | `B_sym = α·[(Z−1)•L_pp + L_pn + (N−1)•L_nn]` — the #2343 additivity |
| `Bsym_deuteron` | `B_sym(²H) = α·L_pn` (the deuteron *is* the single p-n bond) |

The per-bond energies `L_X : Bond → R` are abstract parameters over a generic
`CommRing R` (CLAUDE.md §7c — the additivity is pure algebra; no archimedean input,
no `q₀`). The proof is `List.sum` over the bond multiset (`abel`).

## What this buys (and what it does not)

- **Does:** turns the "B_sym is *exactly* an additive linear chain" claim — which
  the audit verified numerically to the 50-dps floor — into a checked algebraic
  theorem (the bond-count combinatorics + the additive collapse). It also records,
  as `Bsym_deuteron`, that the deuteron is structurally the single p-n bond.
- **Does not:** assert that the abstract per-bond sum equals the *actual* Markov
  trace — that factorization is the empirical/structural input (audit §1, §5,
  50-dps verified), deliberately left in the audit, not claimed in Lean. Nor does
  it touch the open lever (the ⁴He cooperative α-unit magnitude, audit §6) or
  propose any fit. No production rewire.

Complements `QOU.BraidKnot.ChiralityTopologySelection` (merged #2522, which fixed
`chainPnBonds = 1` and `completePnBonds = Z·N`): this file supplies the full
`(pp, pn, nn)` chain decomposition and its additivity.

## References

- [`2026-06-16-b-sym-linear-chain-closed-form.md`](2026-06-16-b-sym-linear-chain-closed-form.md) — the closed-form derivation + 50-dps verification (PR #2343).
- `content/quantum-observable-universe/lean/QOU/BraidKnot/ChiralityTopologySelection.lean` — the p-n bond-count companion (#2522).
- `content/quantum-observable-universe/lean/QOU/BraidKnot/BsymLinearChain.lean` — this formalization.
- bean `6z40` (parent `qfzy`).
