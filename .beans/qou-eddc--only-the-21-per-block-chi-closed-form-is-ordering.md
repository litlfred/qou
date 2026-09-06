---
# qou-eddc
title: Only the (2,1) per-block chi closed form is ordering-dependent; the q^2-1 vanishing survives
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T13:05:29Z
updated_at: 2026-09-06T13:05:55Z
---

## Measured

`Δ_{T_β} = χ_λ(β_n) − χ_λ(β_p)` at the proton pin, 50 dps, under both orderings,
against the closed forms in
`content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`
(lines 72–99):

| λ | paper closed form | **grouped** | **borromean (canonical)** |
|---|---|---:|---:|
| (3) | $-(q^2-1)(q^2+1)^2/(4q)$ | −0.26038764179012 | −0.26038764179012 |
| (2,1) | $(q^2-1)(-q^4-1)/(4q^3)$ | −0.10681445765158 | **−0.09136297383787** |
| (1,1,1) | $-(q^2-1)(q^2+1)^2/(4q^5)$ | −0.17153864377660 | −0.17153864377660 |

    paper forms reproduce from GROUPED words   : True
    paper forms reproduce from BORROMEAN words : False   (one block only)

**Exactly one of the three is ordering-dependent, and it is the only
2-dimensional block.** (3) and (1,1,1) are the one-dimensional
representations — the generators act by scalars there, so they commute and the
intra-ordering cannot matter. (2,1) is 2-dimensional, where σ₀ and σ₁ genuinely
do not commute.

That is the `qou-hu1f` ruling's own stated reason (*σ₀ and σ₁ do not commute, so
only the alternating word is β_Bor*) reappearing from a direction that did not
assume it: the ordering moves the answer precisely where non-commutativity is
visible, and nowhere else. Worth noting as independent support for the ruling.

## What survives, and it is the load-bearing part

The content block `qbeta-per-block-delta-tau-intro.md` does not rest on the
polynomials; it rests on their **vanishing at the classical point**:

> The per-block characters χ_λ(Δ_{T_β})(q) … vanish at the classical point
> q = 1 … this vanishing forces the trace difference Δtr_M to carry an explicit
> (q²−1) factor

Measured on the borromean (2,1) block as q → 1 along irrational points:

| q − 1 | Δ_(2,1) | Δ/(q²−1) |
|---:|---:|---:|
| 3.14e-6 | −3.1416e-6 | −0.49999842916 |
| 3.14e-4 | −3.1411e-4 | −0.49984247653 |
| 3.14e-2 | −3.0638e-2 | −0.48007006777 |

So the borromean block **also** carries the (q²−1) factor, and its leading
coefficient is **−1/2** — the same limit the paper form gives
($(q^2-1)(-q^4-1)/(4q^3)$ → $-2/4$ at q = 1). The two orderings agree on the
vanishing and on the leading coefficient; they differ only at higher order.

**So nothing downstream of the vanishing is affected.**
`prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor` and the Taylor
data feeding the c_k recursion rest on the factor, which holds either way.

## What needs doing

Restate **one** closed form, `(2,1)`, under the canonical ordering — in
`QBetaPerBlockChiClosedForms.lean` and wherever the block quotes it. The other
two are correct as written and must not be touched.

I have not derived the borromean (2,1) polynomial; only its value at q₀
(−0.091362973837869) and its q → 1 behaviour. Deriving it symbolically is the
work here.

## Scope note

`probes/qbeta_delta_vs_deltaTbeta_settled_probe.py` verifies the paper forms and
is pinned to `intra_order="grouped"` (bean `qou-y2o7`), correctly: its whole
comparison is in that frame. Once the (2,1) form is restated, that probe should
gain a canonical arm rather than being flipped — the grouped arm still records the
historical agreement it was written to guard.

Found while running that probe for the first time in this container: it carried
hardcoded `/home/user/qou/computations` sys.path entries, so every import raised
`ModuleNotFoundError` here and it had never executed. Fixed to derive from
`__file__` (`qou-y2o7`), which is how this became measurable at all.
