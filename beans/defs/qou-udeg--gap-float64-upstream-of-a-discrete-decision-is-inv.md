---
# qou-udeg
title: 'GAP: float64 upstream of a discrete decision is invisible to all four float64 detectors'
status: todo
type: task
priority: normal
created_at: 2026-09-26T11:57:46Z
updated_at: 2026-09-26T12:22:48Z
---

## The class, and why it is uncovered

Every float64 detector in this corpus keys on **the stored value's type**:

| detector | asks |
|---|---|
| `witness_raw_float64_audit` | is there a float in any witness field? |
| `witness_float64_padding_audit` | is a 16-digit float serialized to 60? |
| `audits/assertion_value_float64_triage` | is `.assertions[].computed`/`.expected` a float? |
| `audits/assertion_value_provenance_audit` | where did that assertion float come from? |

All four ask *"is there a float in the JSON?"*. So a `float()` cast whose result
is consumed by a **count, a set, a comparison or a round** is invisible to every
one of them: the witness records an `int` or a `bool`, which is the **correct**
type, and nothing fires.

**Confirmed instance**, `probe_bring_residue_resolvent.py:85`:

    vals = [float(canonical_resolvent(q, n)) for n in POLE_ORDERS]
    distinct_count = len(set(round(v, 20) for v in vals))
    w.add_assertion(name="resolvent_values_distinct", computed=distinct_count, ...)

`canonical_resolvent` returns an mpf; the cast keeps ~16 digits; `round(v, 20)`
on a binary64 is a **no-op past ~17 significant digits**, so the code's shape
implies a 1e-20 distinctness bar the arithmetic cannot certify. Measured impact
there is **nil** — the four values are separated by 0.0645, fourteen orders
above the floor — so it is a false precision *claim*, not a wrong number.
`qou-p77d`'s drain ledger records that file as done, because the fields it could
see were done.

## A detector was built, MEASURED, and DELETED rather than shipped

`computations/audits/float64_upstream_of_discrete_audit.py` — AST pass, name
tainted by a `float()` cast in scope, flagged when consumed by
`set`/`sorted`/`round`/`int`/`len`/a comparison/a dict key. It passed a
`--selftest` pinned to the instance above.

Corpus-wide it is **not precise enough to ship**, and the numbers say so:

    files scanned 4499 | flagged 434 | candidates 1040
    of the 82 equality/inequality candidates:
       36  zero guards  (`== 0`, `!= 0`)        -- correct and idiomatic
       14  float only inside a `key=` lambda    -- the compared value is an int
       32  everything else, and most of THOSE read benign too:
             `rs == rs`                         -- a NaN check
             `cache_version != CACHE_FORMAT_VERSION`, `sign == "+"`, `qp == ""`
                                                -- string comparisons
             `len(rows) == 77`                  -- an int

False-positive rate **well above 90 %** on the sub-class I sampled. Two
scoping bugs were found and fixed during the build (a `Module` walk that
descended into function bodies and matched a name bound at L194 against a use
at L98; and a duplicate-count bug the selftest exposed by reporting its 2 real
hits as 4) — and even corrected, the approach is wrong.

**The root defect is name tainting.** Knowing a `float()` appears in the
expression that bound a name says nothing about what the name *holds*: an int
index, a bool ordering, a string, a NaN sentinel. A useful detector needs
**value-type inference**, not name provenance.

## What would actually work

Flag only where the compared/hashed/rounded operand is itself float-valued —
i.e. infer the type, or restrict to the narrow shape `round(<float-expr>, N)`
with `N > 15`, which is self-evidently a no-op and is exactly the confirmed
instance's signature. That narrow rule would have ~no false positives and would
still catch the one known case.

## One candidate NOT dismissed

`derive_binding_bond_type.py:101-128` compares `t_gt_he3 == ame_t_gt` — two
**orderings** (bools) derived from float64 bindings, written into the witness as
`t_he3_ordering_matches`. The equality is on bools, so the detector's hit is
technically a false positive; but the *orderings themselves* are float64-decided,
and if the two bindings are close the ordering could flip. Not measured. That is
the shape worth a real look, and it is the same shape as the confirmed instance:
the float decides something discrete that gets recorded as a non-float.

## RESOLVED 2026-09-26: the one undismissed candidate is BENIGN on float64

`derive_binding_bond_type.py` was left open here as "float64-decided ORDERINGS,
recorded as bools — same shape as the confirmed instance, not measured". Now
measured, and the float64 concern does **not** hold: the bond counts make
`B_T - B_3He == B_nn - B_pp`, whose live value is `-0.0785` MeV — fourteen
orders above the binary64 floor, so the casts cannot flip the verdict.

So this arc's candidate list is fully triaged and the deleted detector's
precision bar was the right call: this was its last survivor and it was a false
positive too.

**But the file carries two real defects of other classes**, moved to bean
`qou-7xa5`: the producer implements the REFUTED Delta_tr law (the live law is
the log-ratio in `binding_log_free_energy.py`), and its committed witness is
stale in a way that INVERTS its verdict (B_T 7.515 -> 1.795, bond ordering
flipped) through import-cone drift in `mass_at_3A_proper.atom_braid_word_3A`
that a `git diff <producer>` cannot see.
