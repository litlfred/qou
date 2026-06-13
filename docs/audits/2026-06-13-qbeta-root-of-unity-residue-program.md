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
- **Newly pinned obstruction → RESOLVED below:** ζ₄ is *not* in the summed
  spectrum. The two falsifiable sub-probes named here (per-cell `[c][c+1]`
  ladder; `cos α_eff` framing) were both run — see *Follow-up probes (options
  1 + 2)* — and the verdict is that **ζ₄ is not a fibre constraint at all**
  (relaxed), not that it lives somewhere harder to reach.
- **No value pressure:** none of this asserts a `c_3` value; it constrains the
  *carrier* `κ_(2,1)` (already known: `(q-1)³(q+1)/q²`, pure-q, bar-odd, #2240)
  and the *mode set* `Λ`.

## Follow-up probes (options 1 + 2): the ζ₄ obstruction is RELAXED

The mode-sum program above left ζ₄ as the one unsupplied constraint and named
two falsifiable next steps. Both were run.

### Option 1 — per-cell ζ₄ ([`qbeta_per_cell_zeta4_subprobe.py`](https://github.com/litlfred/qou/blob/claude/qbeta-heat-fmap-symbolic-explore-2026-06-13/folio-assistant/computations/qbeta/qbeta_per_cell_zeta4_subprobe.py))

Drops to the **un-summed** per-cell `[c]_q[c+1]_q` and asks whether ζ₄ survives
with a bar-odd-compatible parity.

```
ζ_4-carrying contents (per-cell):  c ∈ {-5, -4, 3, 4}   ([4]_q = [2]_q·Φ_4)
per-cell κ_c parity at those c:    all "—" (bar-neither)
only bar-ODD per-cell content:     c = 1  →  carries ζ_2 ONLY
mode that is bar-odd AND ζ_4:      NONE  (every λ with a content-3 cell has λ_1≥4, bar-neither)
```

So ζ₄ *is* a per-cell feature (content c=3 carries `Φ₄` via `[4]_q`), **but the
ζ₄-carrying cells are bar-neither, and the one bar-ODD per-cell content (c=1)
carries only ζ₂.** Bar-odd ∧ ζ₄ is therefore incompatible at the cell level too
— not just after the mode-sum. Even abandoning the `Z_q` partition-function form
for per-cell data does not rescue a bar-odd ζ₄ from the content-Casimir.

### Option 2 — framing factor `cos α_eff` ([`qbeta_framing_zeta4_subprobe.py`](https://github.com/litlfred/qou/blob/claude/qbeta-heat-fmap-symbolic-explore-2026-06-13/folio-assistant/computations/qbeta/qbeta_framing_zeta4_subprobe.py))

Tests the other named source: the framing factor of `F = Q_β/(Q_A·cos α_eff)`,
with the on-main closed form `α_eff = (z−1)·h/2`, `z = √q/(q+1)`, `h = q−1/q`.
Because the framing carries `√q` it is *not* rational in `q`; the probe factors
everything in `s = √q` and maps each `Φ_d(s)` root to its **order in `q = s²`**
(`d/gcd(d,2)`). A *genuine* ζ₄ in `q` would require `Φ₈(√q)`.

```
Φ_d(√q) appearing in z, h, α_eff, [2]_q(1−h²α_eff):   d ∈ {2, 4, 6}
their orders in q:                                    {1, 2, 3}
genuine ζ_4 in q  (needs Φ_8(√q)):                    FALSE
Φ_4(√q) ≡ Φ_2(q) identity:                            TRUE  (same locus q=-1)
```

The framing's only "ζ₄-looking" factor is `q+1 = Φ₂(q)`, which reads as
`Φ₄(√q) = s²+1` in the double cover — **the same vanishing locus `q = −1`, the
bar-FIXED point, not a primitive 4th root of unity in `q`.** No `Φ₈(√q)` appears
anywhere, so there is **no genuine ζ₄(q) in the framing.** (Bonus: `α_eff`
carries `Φ₆(√q) →` q-order 3, i.e. ζ₃ — independently reproducing the option-0
period-3/ζ₆ constraint from a *different* fibre object.)

### Combined verdict — ζ₄ is not a fibre constraint

Neither fibre object — the content-Casimir `μ_λ` **nor** the framing
`cos α_eff` — supplies a bar-odd-compatible **genuine ζ₄ in the `q` variable**.
The synthesis's "ζ₄ residue" kernel constraint is therefore one of:

- **(a) a √q double-cover artifact** — the radial `√u → u²` lift reads the
  bar-fixed `Φ₂(q)` (locus `q = −1`) as `Φ₄(√q)`; this is ζ₂ in `q`, not ζ₄; or
- **(b) a post-`cos`-wrap archimedean feature** — the Kashaev/Ohtsuki asymptotic
  near `q = i` lives *after* the τ functor (the archimedean wall), exactly where
  Zagier's quantum modularity acts, and is **not** a pre-wrap fibre residue.

**Either way the fibre kernel `R` need not carry ζ₄** — that constraint is
**relaxed**, removing it from the pre-flight checklist for fibre-level candidates.
This is a genuine structural prune (formalize-first §): a constraint that would
have driven a wide search for a `Φ₄`-carrying fibre element is shown not to apply
to the fibre at all.

### Live fibre constraints after this program

| Constraint | Status | Realisable in fibre? |
|---|---|---|
| bar-ODD `a_1 = -c_3` | live | ✓ — carrier `κ_(2,1) = (q-1)³(q+1)/q²` (#2240) |
| period-3 / ζ₆ | live | ✓ — modes `(2,1,1),(2,2,1),(2,2,2)` (option 0) **and** `α_eff`'s `Φ₆(√q)` (option 2) |
| simple pole at `u_substrate` | live (archimedean) | n/a — evaluation feature |
| **ζ₄ residue** | **relaxed** | ✗ in fibre — √q double cover (ζ₂) or post-wrap archimedean |

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
