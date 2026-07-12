# c₃ hypersensitivity — the meridian-holonomy boost is a smooth-quantity NEGATIVE (scope-(a))

**Date:** 2026-07-12
**Branch:** `claude/meridian-exceptional-divisor-znxqcn` (#3639)
**Ledger:** [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)

## The question

This branch's origin thread: **meridian = exceptional divisor**, and *one turn of
the meridian = a boost of rapidity `ln q₀`* (non-compact at real `q₀`, not a
compact spin). The `#3600` Reeb-θ entry explicitly flagged the distinction between
the **braid-operator phase θ** (which `#3600` probed) and **our
meridian-holonomy boost** (which nobody had probed). So: **can the meridian boost
be the seat of the c₃ hypersensitivity** `dc₃/dq₀ ≈ 4.66×10⁶`?

## The number that has to be matched

`c₃` swings across the two `q₀` anchors:

| anchor | `q₀` | `c₃` |
|---|---|---|
| muon-pin | `1.10997859555733471…` | `−2.0097` |
| proton-pin | `≈ 1.10998` (`+11.5 ppb`) | `−2.0693` |

`Δc₃ = −0.0596` over `Δq₀ ≈ 11.5 ppb ≈ 1.28×10⁻⁸`, so

$$\frac{dc_3}{dq_0} \;\approx\; \frac{0.0596}{1.28\times10^{-8}} \;\approx\; 4.66\times10^{6}.$$

## The verdict — scope-(a) NEGATIVE

The meridian boost is parametrized by the **rapidity** `ζ = ln q₀`. Its
`q₀`-sensitivity is

$$\frac{d\zeta}{dq_0} \;=\; \frac{1}{q_0} \;\approx\; 0.90 \;=\; O(1).$$

That is the **same order** as the braid phase `θ` (`#3600`: `dθ/dq ≈ −51°/unit`,
`O(1)`). Both are **6–7 orders of magnitude too small** to supply `dc₃/dq₀ ≈
4.66×10⁶` on their own. So:

> The meridian-holonomy boost, like the braid phase `θ`, is a **smooth geometric
> quantity** (`O(1)` `q₀`-derivative) and **cannot, alone, be the seat of the c₃
> hypersensitivity.**

This is a **scope-(a)** statement (per AGENTS.md §"Before declaring refuted"): it
constrains the *magnitude* the boost can contribute; it does **not** structurally
exclude the boost from appearing as one *smooth* factor in a closure. It is the
**fourth** independent confirmation of the recurring pattern **"smooth geometric
quantity ≠ the hypersensitive phase"**:

| probe | quantity | `q₀`-sensitivity | verdict |
|---|---|---|---|
| `#3600` | braid Reeb phase `θ` | `O(1)` | scope-(a) neg |
| `#3596` | pole-seed | amplification `1.4×10⁻⁴` | (near-singular) |
| `#3573` | near-singular `φ` | large | (near-singular) |
| **this** | meridian boost `ζ = ln q₀` | `O(1)` | **scope-(a) neg** |

## The corollary — where the seat must be (the productive direction)

Writing `c₃ = c₃(u)` and `u = u(q₀)`, the chain rule
`dc₃/dq₀ = (dc₃/du)(du/dq₀)` localises the `4.66×10⁶`. Every **smooth** candidate
for a geometric realisation of `u` or `arg(u)` (θ, the boost) has `du/dq₀ = O(1)`,
so the amplification **cannot** live in a smooth `u(q₀)`. It must therefore live
in a **near-singular / pole structure** — either a pole of `c₃(u)` (the
dilog / `q₀→u` map, `conj:algebraic-geometric-dilog-equivalence`) or a
near-singular `u(q₀)`. This is exactly the structure `#3596` (pole-seed
amplification) and `#3573` (near-singular `φ`) are circling.

**Productive direction (not a closure):** the c₃ seat is the **pole structure of
the `q₀→u` dilog map**, the open keystone `conj:algebraic-geometric-dilog-
equivalence`. The smooth-holonomy family (boost + braid θ) is now closed as a
*sole* mechanism; the search should concentrate on the near-singular map, in
coordination with `#3596`/`#3573`.

## Anti-laundering

No `c_k` value is produced; nothing is wired to production; no tier change. `c₃`
remains a q₀-dependent near-match (SETTLED, PR #1580). This note only *closes our
thread's smooth-boost angle* and *sharpens the seat*.

-- Ref: [manuscript] docs/coordination/1ppq-qbeta.md
