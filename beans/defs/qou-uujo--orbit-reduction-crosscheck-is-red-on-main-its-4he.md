---
# qou-uujo
title: 'orbit_reduction_crosscheck is RED on main: its 4He smoke pin 0.05534833 predates the ordering ruling and its witness (2026-05-30) still claims allPassed'
status: todo
type: task
created_at: 2026-09-14T18:38:47Z
updated_at: 2026-09-14T18:38:47Z
---

## Measured, on a CLEAN tree

Found while draining `atom_orbit_reduction` under `qou-t29k`. Verified by
stashing my own edits and re-running, so this is not from that work:

    N1 ³He |orbit|-guard: via=0.0585962536544363 direct=0.0585962536544363
                          Δ=0.0e+00  [✓]
    N2 ⁴He value smoke:   tr_M=0.011237417659767421
                          (pin 0.0553483351637685668, Δ=4.4e-02)  [✗]
    TIER 1.B ORBIT-REDUCTION CROSS-CHECK: FAIL

The committed witness says **`allPassed: True`, `computedAt` 2026-05-30** —
more than three months old and long before the 2026-09-05 intra-ordering ruling
(`qou-hu1f`).

## Why it fails, and why it is NOT the qou-t29k defect

`tr_M_via_orbit_representative` goes through `atom_braid_orbit_representative`,
which **delegates to the production `atom_braid_word_3A`** — so this path was
always canonical and moved on 2026-09-05 when that builder's default did. The
value it now returns, `0.011237417659767421`, is exactly the canonical ⁴He
constant `0.011237417659767421564199549374410…`, which I confirmed
independently the same session by regenerating the ⁴He binding cache.

So the CODE is right and the PIN is stale. Note the pin is not the grouped
value either: grouped ⁴He is `0.160974145442407…`, and `0.0553483351637685668`
is neither — it is from some earlier state again, so re-pinning wants the
provenance of that number checked rather than just overwriting it with today's.

## Deliberately not fixed here

Re-pinning a smoke test is a one-line change and I did not make it, because the
right value depends on what `N2` is for. Its own source calls it "⁴He value
smoke @50dps vs post-re-pin canonical" — if the point is "this equals the
canonical ⁴He trace", the pin should be the canonical constant and the
tolerance 1e-40 like its sibling `N1`, not 1e-6. That is a decision about the
test, not a number to swap. Also left the witness at its committed state rather
than regenerating a FAIL into the repo: I was not otherwise editing this file,
and flipping someone else's witness in a drive-by is a bigger statement than
recording the finding.

## Third of its kind

After `qou-g5oz` (`qbeta_level_k_binding_operator_probe`, red since the ruling,
witness two days pre-ruling claiming all-pass) and the pre-existing crash in
`canonical_ordering_dof_probe` Part 6 (`TypeError: cannot create mpf from None`,
also reproduced on a clean tree; Part 6 is already tracked as blocked by
`qou-xy5f`). The pattern worth naming: **the ordering ruling left a tail of
probes whose witnesses still claim all-pass**, and nothing re-ran them. Each was
found by working an unrelated site next to it, not by a sweep.

## RESOLVED: the pin is TRACE CONVENTION C, two rulings behind — not one

I flagged `0.0553483351637685668` as "a third value, neither grouped nor
canonical", and said re-pinning needed its provenance checked first. It did.
The number is fully accounted for, from two primary sources in the repo.

**`qou-mass/CHANGELOG.md` names it outright.** The shard
`canonical-mass-table-extended.witness.json` was a 2026-05-19 vintage that
"shipped convention-C traces" after the corpus moved to **trace convention D**
(`z = q³/(q²+1)`, the SU(2)/Temperley–Lieb Markov parameter). Its regeneration
table:

    atom   1.0.0 (conv D)      0.1.0a1 (conv C)     change
    ⁴He    0.16097419322912    0.05534834587670     +191 %

**`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md` explains the last
digits.** The q₀ anchor was re-pinned muon -> proton that day:

    tr_M(⁴He)   pre-re-pin 0.0553483458766980   post-re-pin 0.0553483351637685

So the crosscheck's pin is **convention C at the proton-anchored q₀** — which
is exactly right for 2026-05-30, the day its witness was computed, and has been
superseded twice since.

### The full lineage of tr_M(⁴He), which is the actually useful output

| value | state |
|---|---|
| `0.0553483458766980` | convention C, muon-anchored q₀ |
| `0.0553483351637685` | convention C, **proton** q₀ (re-pin 2026-05-30) **← this pin** |
| `0.160974145442407` | convention **D**, grouped intra ordering |
| `0.011237417659767` | convention D, **borromean** — canonical today |

Two independent cross-checks that this lineage is right, not just plausible:
the CHANGELOG's ³He convention-D value `0.40376713848383` matches the corpus's
grouped ³He constant `0.40376703685142817` to the q₀ re-pin digit; and its ²H
value `0.57509095868245` is the `strict_averaged` deuteron
`0.575090871629810316751633` that `binding_canonical` quotes by name, against
`0.575172243917771870826535` for `bring_color_weighted` — so that column is
convention D + colour-blind + grouped, and the colour ruling is a *further*
step on the same chain.

### My colour-convention hypothesis was WRONG, and the number says why

I guessed the 2.908x gap was the 2026-08-15 colour ruling. It cannot be: the
colour weight δ is ~1e-3 relative, which cannot move a trace by 191 %. The
factor is the **Markov parameter** — `z` going from convention C's
`1/(q^½ + q^-½)` ≈ 0.4993 to D's `q³/(q²+1)` ≈ 0.6127, a 23 % change in z
compounded over an H₁₂ trace.

### Why the obvious experiment could not have settled it

I started a sweep of `atom_braid_word_3A` over both
`pn_convention` × `intra_order` expecting one combination to reproduce the pin.
**None can.** Convention C is a property of the TRACE, not of the word:
`Z_MARKOV = Q0_PROTON**3 / (Q0_PROTON**2 + 1)` is a module constant at
`mass_at_3A_proper:121` with no flag. The sweep was killed after ~11 minutes
once the CHANGELOG made that clear — it was measuring the wrong axis, and
would have returned four non-matches with no explanation attached.

### What the re-pin should be, and the one thing still to decide

The code is right and the pin is three states stale. The value it should carry
is the canonical `0.011237417659767421564199549374410607269662696081262`, which
I confirmed independently this session by regenerating the ⁴He binding cache
(77/77 λ⊢12, f64 gate 1.1e-14).

Still a judgement call, and the reason this is not closed: `N2`'s tolerance is
`1e-6` where its sibling `N1` uses `1e-40`. If `N2` is meant to assert "this
equals the canonical ⁴He trace", it should be pinned to the constant at `N1`'s
tolerance and stop being a "smoke" test. If it is meant to be a loose smoke
check, 1e-6 is fine but the pin still has to move. That is a decision about what
the test is for.

### One measured row survived the kill, and it confirms the lineage

The sweep emitted its first combination before I stopped it:

    target pin                                        0.0553483351637685668
    pn=bring_color_weighted  intra=grouped  |tr_M| =  0.16097414544240738183

That is state 3 of the table above to every digit, and it is 2.908x the pin —
so the current builder, at the convention the corpus calls canonical for the
WORD, lands exactly where the CHANGELOG says convention D lands. The remaining
three combinations would have varied the two word-level axes, neither of which
is the axis that separates the pin from today's value. Measured confirmation of
the documented account, at the cost of the one row that was worth having.

