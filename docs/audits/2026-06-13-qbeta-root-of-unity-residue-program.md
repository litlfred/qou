# Q_β heat-route — root-of-unity residue program (over-determination test)

**Date:** 2026-06-13
**Branch / PR:** `claude/qbeta-heat-fmap-symbolic-explore-2026-06-13` (#2240)
**Probe:** [`folio-assistant/computations/qbeta/qbeta_root_of_unity_residue_program.py`](https://github.com/litlfred/qou/blob/claude/qbeta-heat-fmap-symbolic-explore-2026-06-13/folio-assistant/computations/qbeta/qbeta_root_of_unity_residue_program.py)
**Discipline:** STRUCTURAL only. No `c_3` value is claimed or wired. The
four-session flip-flop guard
([`docs/coordination/ck-dk-canonical-registry.md`](https://github.com/litlfred/qou/blob/main/docs/coordination/ck-dk-canonical-registry.md))
is respected — this is a pull-back of Zagier's root-of-unity (Ohtsuki-period)
structure onto the fibre, asking a *closure* question, not a value question.

## The question

The synthesis
([`docs/audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md))
collected four structural constraints the heat-kernel `R(q,ξ)` must satisfy:

1. **bar-ODD** leading coefficient `a_1 = -c_3`;
2. a **simple pole** at the substrate `u_substrate`;
3. a **ζ₄ residue** (the named source of the period-4 structure);
4. a **period-3 (ζ₃/ζ₆)** resonance.

Pulling the Ohtsuki-period reading of Zagier-2010 back to the fibre
(§2-quater of
[`2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md)),
these become statements about **which roots of unity `ζ_d` the content-Casimir
`μ_λ` carries** — i.e. which cyclotomic polynomials `Φ_d(q)` divide
`μ_λ = ℏ_q²·Σ_□[c]_q[c+1]_q`. The owner's question: do bar-parity + ζ₄ +
period-3 **over-determine** the active-mode set `Λ` (a clean closure) or merely
constrain it?

## What the probe computes

For every partition `λ ⊢ n`, `n = 2..6` (27 modes), the probe forms the
content-Casimir sum `Σ_□ [c]_q[c+1]_q` (the `ℏ_q²` prefactor stripped, parity
unaffected), factors its numerator over `ℚ[q]`, and reports **which `Φ_d`
(d = 2..12) divide it** — exactly the `ζ_d` that mode carries. It also reports
the bar-parity of `κ_λ = (q-1)μ_λ` (the `a_1` building block).

## Result (decisive)

```
ζ_2: all 27 modes (the universal Φ_2 = [2]_q factor)
ζ_6: (2,1,1), (2,2,1), (2,2,2)   — exactly 3 modes
ζ_3: ABSENT at the summed level
ζ_4: ABSENT at the summed level
```

Bar-parity of `κ_λ`: **ODD** for exactly `(2)`, `(2,1)`, `(2,2)`; "—"
(neither) for all other modes.

### Reading

| Synthesis constraint | Supplied by summed `μ_λ`? | Detail |
|---|---|---|
| bar-ODD `a_1` | ✓ (partially) | only `(2)`, `(2,1)`, `(2,2)` are bar-odd; they carry **ζ₂ only** |
| period-3 / ζ₆ | ✓ | `(2,1,1)`, `(2,2,1)`, `(2,2,2)` carry Φ₆ — matches the synthesis resonance |
| ζ₄ residue | **✗** | **absent** from every summed `μ_λ` |
| simple pole at `u_substrate` | (archimedean — not a fibre cyclotomic feature) | out of scope of this probe |

The headline correction to the earlier per-term hypothesis: a content-3 cell's
**per-cell** factor `[3]_q[4]_q` *does* contain `Φ_4` (since `[4]_q =
[2]_q·(1+q²)` and `1+q² = Φ_4`), but that factor is **washed out by the
mode-sum** `Σ_□[c][c+1]` — the other cells of the same partition are not
divisible by `Φ_4`, so the sum's numerator loses the `Φ_4` factor. **ζ₄ is a
per-cell feature, not a property of the summed content-Casimir.**

## Over-determination verdict

**Not a clean closure.** The summed-`μ_λ` heat kernel supplies:

- the **bar-odd leading structure** (modes `(2)`, `(2,1)`, `(2,2)`), and
- the **period-3 / ζ₆ resonance** (modes `(2,1,1)`, `(2,2,1)`, `(2,2,2)`),

but it does **not** supply the **ζ₄ residue**. So the four constraints do not
collapse the active-mode set `Λ` to a unique answer from the summed content-
Casimir alone. Two structural facts make this sharper:

1. **The bar-odd modes and the ζ₆-carriers are disjoint.** The bar-odd modes
   `{(2),(2,1),(2,2)}` carry **only ζ₂**; the ζ₆-carriers `{(2,1,1),(2,2,1),
   (2,2,2)}` are bar-**neither**. So no single mode supplies both the bar-odd
   leading structure *and* the period-3 resonance — a **content-spanning `Λ`
   with cancellation** is still required (a bar-neither mode's even part must
   cancel against another's to leave a bar-odd remainder carrying ζ₆).

2. **ζ₄ must come from per-cell data or from outside the content-Casimir.**
   Because `Φ_4` is washed out by the mode-sum, a kernel built from summed
   `μ_λ` cannot carry it. To realise the synthesis's ζ₄ residue the kernel must
   either (a) use **per-cell** content data (the unsummed `[c]_q[c+1]_q` ladder,
   keeping `Φ_4` alive), or (b) source ζ₄ from a different fibre object (e.g. the
   `[2]_q` framing / `cos α_eff` factor of `F = Q_β/(Q_A·cos α_eff)`, which is
   where the period-4 `α_EM` structure already lives).

## Where this leaves the keystone

This **narrows** the heat-route keystone rather than closing it. Concretely:

- **Confirmed compatible:** bar-odd leading + ζ₆ period-3 are both realisable
  from the content-Casimir spectrum (the right modes exist).
- **Newly pinned obstruction:** ζ₄ is *not* in the summed spectrum, so any
  closed `R` must either keep per-cell content or borrow ζ₄ from the framing
  factor. This is a **concrete, falsifiable** next sub-probe (test whether the
  per-cell `[c][c+1]` ladder, or the `cos α_eff` factor, carries Φ₄ with the
  right bar-parity), not an open-ended search.
- **No value pressure:** none of this asserts a `c_3` value; it constrains the
  *carrier* `κ_(2,1)` (already known: `(q-1)³(q+1)/q²`, pure-q, bar-odd, #2240)
  and the *mode set* `Λ`.

## Method notes / honesty caveats

- The bar-parity column uses `κ_λ = (q-1)·ℏ_q²·Σ[c][c+1]`; the `(q-1)` factor is
  what flips the even content-Casimir into the odd `a_1` building block, so
  "ODD" here is the `a_1`-relevant parity, not the parity of `μ_λ` itself.
- Range `n ≤ 6` (27 modes) is enough to see the ζ₄ wash-out and the ζ₆ onset;
  larger `n` only adds higher-content modes that still factor through the same
  `Φ_d` (no new small-`d` cyclotomic appears below the first content reaching
  it). The "needs content `c ≥ d-1`" rule (printed by the probe) bounds this.
- An **earlier draft** of this probe hardcoded a "tension (ζ₃ at content-2, ζ₄
  at content-3)" conclusion that **contradicted its own data** — the per-term
  cyclotomic factors do not survive the mode-sum. That draft conclusion was
  wrong and was replaced by the data-driven verdict above. Recorded here so the
  mistake is not silently repeated.

## Status

Structural exploration; feeds the open heat-route keystone
([`q-beta-c-k-recursion-from-habiro-q-difference.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)).
No production wiring; registry tiers untouched.
