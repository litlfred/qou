# Geometric `W_λ` — the q₀ residual is the framing monomial `q₀^{f·c(λ)}`, exactly trivial on the electron block

**Date:** 2026-07-12 · **Axis:** s5-so3 keystone geometric `W_λ`, q₀ residual ·
**Branch:** `claude/keystone-wlambda-q0-residual-2026-07-12` · **Follow-up to** #3685 (value map) +
#3699 (Lean identities) + #3681 (Habiro/Stokes carriers) + #3662 (de-opaqued gate). **No fit.**

## The residual, made explicit

The concrete colored-WRT vacuum row (de-opaqued gate #3662) is
`bwS0Concrete(λ)(q) = S_{0λ}(q)·θ_λ(q)^f = (d_q(λ)/D(q))·q^{f·c(λ)}`, with `θ_λ=q^{c(λ)}` the ribbon
twist, `c(λ)` the content sum, `f` the Seifert framing forced by Σ(2,3,5). The framework's
Verlinde/Plancherel value is the framing-**stripped** `bwS0(λ)=d_q(λ)/D`.

#3685 derived `d_q(λ)=[mark]_q` — a **Laurent polynomial**, a global function of `q`, identical at
roots of unity and at `q₀` (no Habiro completion needed for the numerator; `D` and `θ_λ^f` are global
too). Therefore the **entire** fibre→observable "archimedean continuation" residual reduces to the one
framing factor

  `θ_λ(q₀)^f = q₀^{f·c(λ)}`,

a phase (`|·|=1`) at a root of unity but a real factor `≠ 1` at `q₀>1` for `c(λ)≠0` (the #3652
refutation, now written explicitly).

## The electron block is derived outright (no continuation)

`c(λ') = −c(λ)` (proved twist chirality `θ_{λ'}=θ_λ^{-1}`) and `c(λ)=0` **iff** `λ` is self-conjugate.
The **only** self-conjugate `n=5` block is the **electron** `(3,1,1)` — the A₅-split mark-6 McKay node.
Hence `c((3,1,1))=0`, so `θ_λ^f = 1` for **any** framing `f`, and

  `bwS0Concrete((3,1,1))(q₀) = d_{q₀}((3,1,1))/D = ([5]_{q₀}+1)/D ≈ 0.547724` **exactly.**

There is **nothing to continue** for the electron block: its value is a Laurent polynomial with zero
framing, so the #3681 Habiro-rigidity carrier is **discharged concretely** — rigidity is trivial (no
root-of-unity reconstruction), and the geometric derivation of the electron block's `q₀` value is
**complete, no fit, f-independent** (hence robust to the exact Seifert framing).

| λ | mark | c(λ) | self-conj | `bwS0=d_q/D` | framing residual `q₀^{f·c}` |
|---|--:|--:|:-:|--:|---|
| (5) | 1 | +10 | — | 0.08805 | `q₀^{10f}` |
| (4,1) | 4 | +5 | — | 0.36187 | `q₀^{5f}` |
| (3,2) | 5 | +2 | — | 0.45967 | `q₀^{2f}` |
| **(3,1,1)** | 6 | **0** | **✓** | **0.54772** | **1 (any f) — derived outright** |
| (2,2,1) | 5 | −2 | — | 0.45967 | `q₀^{−2f}` |
| (2,1,1,1) | 4 | −5 | — | 0.36187 | `q₀^{−5f}` |
| (1⁵) | 1 | −10 | — | 0.08805 | `q₀^{−10f}` |

Every non-self-conjugate block carries the explicit content-sum framing monomial `q₀^{f·c(λ)}`
(opposite on a conjugate pair) — the standing open piece, now written per block rather than as an
opaque "archimedean continuation."

## Scope (STRICT — anti-laundering)

Derives the electron block's `q₀` value with no fit and no free constant (the `c=0` result is
framing-`f`-independent); quantifies the residual for the other six blocks as an explicit framing
monomial. Does **not** close the gate for the non-self-conjugate blocks (the framing residual there is
the genuine open object), and wires **no** constant to production. No fit; no numerology. Probe +
witness: [`keystone_q0_framing_residual.py`](../../computations/probes/keystone_q0_framing_residual.py).
