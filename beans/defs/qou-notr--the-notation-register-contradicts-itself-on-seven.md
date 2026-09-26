---
# qou-notr
title: 'The notation register contradicts itself on seven points, including the z convention the owner settled and its own E rule'
status: todo
type: task
priority: normal
tags:
    - notation
    - convention-d
created_at: 2026-08-22T07:40:00Z
updated_at: 2026-08-22T08:05:00Z
---

From `agent:pq_11`, the batch that closed the trap drain. These matter more than
their block count because AGENTS.md §7aa points **every other chapter** at this
register as the authoritative source for symbols and collision rules — so a
defect here is a corpus-wide instruction, not a local error.

Numbers re-derived in the coordinating session where they are arithmetic.

## 1. ~~The register contradicts itself on the z convention~~ — FIXED 2026-08-22

`notation-collisions.md` closes with *"(The z convention itself is unsettled and
is not changed here…)"*. `notation-register-table3-data.md`, in the same chapter,
calls convention D *"the framework's production trace"* and says the selection is
*"**forced, not stipulated**"*. The owner ruling R1 of 2026-08-15 settled it and
excised C.

**Sharper than "it disagrees with its sibling table": it disagreed with the very
block it was citing.** The parenthetical's own cross-reference,
[`def:markov-axioms-primitive`](../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md),
states `z = q^3/(q^2+1)` as **convention D** in its axiom 3 and carries the
selection note recording the 2026-08-09 owner ruling that excised C. So a reader
following the pointer to settle the question found it already settled, by the
document the pointer led to.

**Fixed**: the parenthetical now reads *"The `z` convention is settled
independently of this: convention D, `z = q^3/(q^2+1)`, is canonical and C is
excised"*, keeping the cross-reference. The surrounding claim — that the
bar-partner is `z - h`, not `z`, because M3 contains `sigma_n` — is separate and
stands; `pq_11` verified `z - h = z-bar` exactly under D. Everything else in that z entry
checks out — `1/δ = 0.4972905456`, `z_C = 0.4993203342`, the 0.408 % gap, the D
three-strand weights `(0.5054042, 0.2472979, 0)`, and the neat fact that
`z − h = z̄` exactly under D.

## 2. `z(q₀)` is printed to 20 digits and about 16 are backed

Printed in **7 `.md` blocks**: `0.61268803714646525160`.

```
exact (proton pin) :  0.612688037146465243650558825336
float64 of exact   :  0.612688037146465247495541461831
printed            :  0.61268803714646525160
```

The printed tail matches **neither** — not the exact value, not the float64
rounding. Agreement is to 16 significant digits, and the last four are
unaccounted for. The string appears in no `.py` and no `.json` under
`computations/`, so it is a documentation-only constant propagated by copy, with
no producer to regenerate it.

## 3. The register's own `q₀` example is the superseded muon string

`notation-register-table3-data` and `-table9-data` both print
`q_0 = 1.109978595554181…` labelled "(muon pin, 16 dps)". That is the **old**
muon value; the current one is `1.10997859555733471`, differing at the **12th**
digit — so ~11 digits are backed and 16 are shown. The string is in **10 `.md`
files** corpus-wide. And per the owner directive of 2026-08-07 the **proton** pin
is the default for compute, which the register does not offer at all.

## 4. The register violates its own `E` rule, inside the rule's own document

`notation-collisions.md` bullet 4: *"**$E$** alone = not used"*, and the next
bullet: *"Using `E_0` for a $Q_\beta$-valued binding-scale variable is a
**registered notation violation**"*. Both `notation-register-table7-data` and
`notation-collisions` itself then write `\mathfrak{V}(K) = E_0\,\mathrm{tr}_M(…)`
with bare `E_0`. Live in 7 `.md` files, including one that prints the
**muon**-pin value 4.1859808 MeV (proton gives 4.1859814).

## 5. The collision register introduces a `Δ_λ` collision

Its binding bullet writes *"the **Δ_λ = B_AME/B_lin** residual"*. `Δ_λ` is the
per-partition signed Springer dimension `(−1)^{n(λ)}·dim V_λ` — proved,
integer-valued, general-n — everywhere else in the corpus, including the `B_λ`
row two lines above it in the same table.

In the same bullet, `𝔈₀/Q_β(n) ≈ 5.31` does not reproduce: `4.1859814 /
0.78233341 = 5.3506`, 0.8 % off, and the muon-pin numerator gives the same to 6
digits. (`Q_β(n) = 0.78233341` is correctly the experimental value; the closed
form gives 0.78365, +0.168 %.)

## 6. The `μ_λ(1)` table is wrong at two of three entries

The register and `information-theory/q-heat-kernel-peter-weyl.md:11` define
`μ_λ(q) = ℏ_q² Σ_□ [c(□)]_q[c(□)+1]_q`. At `q = 1`, summing over cell contents:

| λ | contents | Σ c(c+1) |
|---|---|---|
| `(3)` | 0, 1, 2 | `0 + 2 + 6` = **8** |
| `(1³)` | 0, −1, −2 | `0 + 0 + 2` = **2** |
| `(2,1)` | 0, 1, −1 | `0 + 2 + 0` = **2** |

The table prints `0, 2ℏ_q², 0`. Only `(2,1)` matches. Either the table is wrong
twice, or the formula is missing the normalisation that makes the trivial rep
decay-free — and then it is wrong in two files. `(2,1)`'s agreement with the
literal formula favours the first reading; `(1³)` is wrong under either.

## 7. The bold-`Rep` convention it mandates is the corpus minority

Measured in `.md`: `\mathbf{Rep}` **42** occurrences across 31 files;
`\mathrm{Rep}` **62** across 44. The register and AGENTS.md §7 both mandate bold.
This is a corpus-scale drift, so it wants a single owner decision, not a sweep
driven by an audit.

## Smaller, same document

~~`\wp` labelled "fraktur cap"~~ — **fixed 2026-08-22** to `script`. It is not
fraktur (`\mathfrak{P}` is a different glyph entirely), and while Unicode names
U+2118 "SCRIPT CAPITAL P", the glyph is lowercase, so "cap" misleads a reader
choosing a symbol. The table's own Font column already uses bare family names
("calligraphic", "Greek") alongside cased ones. Table 10 presented before Table 9;
no table for chapters 3, 5, 7. `\mathcal{P}` reserved for parity in one paragraph
and for the Goncharov filtration `\mathcal{P}_n` in Table 4, uncross-referenced.
`T_e` written for the Hecke identity against §7a's *"never `T`"*. `G` carries
three live meanings — gauge group, `G_q` gravitational, Catalan's `G` — of which
two are registered.

## Disposition

Item 1 is the one to fix first and is nearly free: delete the "unsettled"
parenthetical, which the owner ruling has superseded. Items 2 and 3 are digit
hygiene with a real trap — do not "correct" the printed tails by hand, since
that is what produced them; either give the constants a producer or truncate to
what is backed. Item 6 needs someone to decide which of the formula and the
table is right, which is a math call. Item 7 is an owner decision.
