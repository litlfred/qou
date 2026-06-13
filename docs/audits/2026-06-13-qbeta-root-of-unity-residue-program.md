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

1. **The bar-odd modes and the ζ₆-carriers are disjoint** (at the level of
   *full* `κ_λ` parity). The bar-odd modes `{(2),(2,1),(2,2)}` carry **only
   ζ₂**; the ζ₆-carriers `{(2,1,1),(2,2,1),(2,2,2)}` are bar-**neither**. This
   first suggested a content-spanning `Λ` with cancellation would be required —
   **but that inference is refuted below** (*Period-3/ζ₆ — CLOSED*): the bar-odd
   **projection** of a single ζ₆-carrier already carries ζ₆ (cyclotomic
   bar-stability lemma), so no cross-mode cancellation is needed.

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
| period-3 / ζ₆ | **CLOSED (realisable)** | ✓ — bar-odd projection of `κ_(2,1,1)` carries ζ₆ (bar-stability lemma, *Period-3/ζ₆* below); also `α_eff`'s `Φ₆(√q)` (option 2) |
| simple pole at `u_substrate` | live (archimedean) | n/a — evaluation feature |
| **ζ₄ residue** | **relaxed** | ✗ in fibre — not mode-available (no `κ_λ` carries Φ₄); √q double cover (ζ₂) or post-wrap archimedean |

## Period-3/ζ₆ — CLOSED (the cyclotomic bar-stability lemma)

The mode-sum verdict above worried that, since the bar-odd modes and the
ζ₆-carriers are disjoint *as full `κ_λ`*, a cross-mode cancellation would be
needed to get a bar-odd object carrying ζ₆. The period-3/ζ₆ probe
([`qbeta_period3_zeta6_cancellation_probe.py`](https://github.com/litlfred/qou/blob/claude/qbeta-heat-fmap-symbolic-explore-2026-06-13/folio-assistant/computations/qbeta/qbeta_period3_zeta6_cancellation_probe.py))
shows that worry is unfounded.

**Lemma (cyclotomic bar-stability).** For `d > 1`, `Φ_d(q)` is self-reciprocal:
`bar(Φ_d) = Φ_d(1/q) = q^{-φ(d)}·Φ_d(q)` (a unit multiple). *Verified
symbolically for `d = 2,3,4,6`.*

**Corollary.** `Φ_d ∣ X ⟺ Φ_d ∣ bar(X) ⟺ Φ_d ∣ (X)_odd` (and `(X)_even`),
whenever the part is nonzero. So **the bar-odd projection of any `Φ_d`-carrier
still carries `Φ_d`.**

**Application — ζ₆ is realisable by a single mode.** Each ζ₆-carrier
`κ_λ ∈ {(2,1,1),(2,2,1),(2,2,2)}` is bar-neither, so its odd part
`(κ_λ)_odd = (κ_λ − bar κ_λ)/2` is **nonzero**, is **bar-odd** by construction,
and **carries Φ₆** by the corollary (verified: all three modes give
`Φ₆ ∣ (κ_λ)_odd = True`). The mode-selective f-map (proved by the symbolic
f-map probe) projecting *one* ζ₆-carrier onto its bar-odd part therefore yields
a bar-odd, ζ₆-carrying object — **no content-spanning cancellation needed.**
Period-3/ζ₆ joins bar-odd `a_1 = κ_(2,1)` as a *realisable* fibre constraint.

**Same lemma sharpens the ζ₄ relaxation.** Bar-parity was never the ζ₄
obstruction — by the corollary, odd projection preserves any carried `Φ_d`. The
real reason ζ₄ is unreachable is **mode-availability**: the probe re-confirms
**no full `κ_λ` (n ≤ 6) is divisible by `Φ₄`** (the `Σ_□` wash-out). So ζ₄ would
require finer *per-cell* selection than the established mode-level f-map — or it
is the √q double-cover / post-`cos`-wrap archimedean feature of option 2. Either
way it is not a mode-level fibre constraint.

**Net.** Both live fibre constraints — bar-odd `a_1 = κ_(2,1)` and period-3/ζ₆ —
are now realisable by the mode-selective f-map + bar-odd projection. The
keystone's remaining open piece is the single archimedean scalar `S = Q_β/E₀`.

## Higher coefficients `a_2, a_3` — the parity-alternation theorem

Extending the fibre map beyond the leading coefficient
([`qbeta_higher_aj_carrier_probe.py`](https://github.com/litlfred/qou/blob/claude/qbeta-heat-fmap-symbolic-explore-2026-06-13/folio-assistant/computations/qbeta/qbeta_higher_aj_carrier_probe.py)).
The depth-`d` recursion `c_{k+1} = Σ_j a_j c_{k+1-j}` has, in the heat-route
product picture, coefficients `a_j = e_j({r_λ})` — the elementary symmetric
polynomials of the per-mode **rates** `r_λ = (q−1)·μ_λ = κ_λ` (the q-difference
kernel of a product of depth-1 modes `A_λ(t)=1−(q−1)μ_λ t`).

**Theorem (parity alternation).** If the f-map feeds **bar-odd** rates `r_λ`
(the bar-odd projections, which carry each mode's ζ-content by the bar-stability
lemma), then `bar(e_j) = e_j({−r_λ}) = (−1)^j e_j`, so

> `a_j` is bar-**ODD** for `j` odd, bar-**EVEN** for `j` even — alternating,
> *independent of which modes are active*.

Verified symbolically for `j = 1..4`. This is the structural law behind the
ladder's parity bookkeeping: the bar-even seed `c_2 = −1` is driven by a bar-odd
`a_1` (= −c_3), a bar-even `a_2`, a bar-odd `a_3`, …. It is a one-line consequence
of `e_j(−x) = (−1)^j e_j(x)` (Mathlib-provable; flagged as a formalization
follow-up — sandbox `elan` is firewalled, so not built here).

**Concrete carriers.** For the principled depth-3 active set
`Λ = {(2,1), (2,2), (2,1,1)}` (the bar-odd ζ₂ carrier `(2,1)`, a second ζ₂
carrier `(2,2)`, and the ζ₆-carrier `(2,1,1)`, all bar-odd-projected):

| coeff | parity (matches theorem) | ζ_d content |
|---|---|---|
| `a_1 ~ e_1` | ODD | ζ₂ |
| `a_2 ~ e_2` | EVEN | ζ₂ |
| `a_3 ~ e_3` | ODD | **ζ₂ + ζ₆** |

**ζ₆ enters at `a_3`.** For this depth-3 set, `e_3` is the *full product*
`r_(2,1)·r_(2,2)·r_(2,1,1)`, so it inherits the `Φ₆` factor of the ζ₆-carrier;
`e_1` (a sum) washes `Φ₆` out exactly as before, and `e_2` keeps only ζ₂. So the
period-3/ζ₆ resonance surfaces in the **3rd** recursion coefficient — a pleasing
internal echo of "period 3". *Honesty caveat:* the ζ₆-at-`a_3` onset is
**active-set-specific** (it follows from `e_3` being the top product at depth 3);
only the **parity-alternation law is mode-set-independent**. The residual
freedom is the active set `Λ` (which modes, with what multiplicity); that, times
the owner-**declined** archimedean scalar `S`, would fix the `c_k` *values*. The
fibre **structure** — carriers, parities, ζ-content, the alternation law — is now
mapped through `a_3`.

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
