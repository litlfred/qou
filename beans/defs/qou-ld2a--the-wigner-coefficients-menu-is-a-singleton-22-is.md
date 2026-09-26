---
# qou-ld2a
title: 'The Wigner coefficient''s menu is a singleton: (2,2) is the only partition of 4 with content sum zero'
status: completed
type: task
priority: normal
created_at: 2026-09-05T12:56:37Z
updated_at: 2026-09-05T13:02:27Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Answers `qou-w06d`'s
successor: **is `(2,2)` alone enough to reproduce the Wigner term?**

## For the IMPLEMENTED term the question does not arise

`derived-mass-formula-light-isotopes.md` already uses `(2,2)` alone:

    Delta_W = -m_e . H_q((2,2)) . min(Z,N)/A

so the row cap leaves it untouched. **What carries `(3,1,1)` is the `T(T+1)/A`
form in `unified-iterative-correction-proof.md`**, whose `k = 5` half is now
known to price nothing (`qou-w06d`). That block should be re-stated over `k = 4`
alone, or its `k = 5` term dropped. Recorded as the concrete follow-up.

## 🛑 THE NUMBER IS NOT THE RESULT, AND THE CORPUS SAID SO FIRST

`m_e . H_q((2,2)) = m_e [3]_q [2]_q^2 = 6.289300` MeV against an empirically
extracted `Delta_W ~ 6.3` MeV (Satula-Nazarewicz 1997) — 0.17 %. **Already in
the corpus** (`pn-bond-cannot-be-extremal.md:64` records 6.2894), so it is not
new, and the QA note on `mass-formula-regime-switching-table1-data` already
judged the whole family correctly:

> "seven coefficients each written as a short product of q-integers drawn from a
> large menu, agreeing with known LDM values at the 1-6 % level, **is the shape a
> fit takes**; nothing in the table or its parent derives which product goes with
> which coefficient"

That objection is right and is not answered by a good number.

## WHAT IS NEW: on this row the menu has ONE item

`mass-coefficient-shadow-price-proof.md`'s own rule classifies by content sum —
`c > 0` volume, **`c = 0` isospin-type `T(T+1)/A^p`**, `c < 0` charge. The
Wigner energy is T=0 isoscalar pn pairing, a QUARTET correlation, so `n = 4`.
At that level:

| lambda | c | class |
|---|---:|---|
| (4) | 6 | volume |
| (3,1) | 2 | volume |
| **(2,2)** | **0** | **ISOSPIN — the only one** |
| (2,1,1) | -2 | charge |
| (1,1,1,1) | -6 | charge |

Say "isospin-type" and "quartet" and the partition is **forced**, with no
freedom left to fit. **That is exactly the derivation the fit-shape objection
asks for, on this one row.** It is one row of seven; the objection stands for
the other six and nothing here touches them.

## And the row cap empties the class above n = 4

`c = 0 AND ell <= 2` is a singleton at n = 1, 3, 4 and **empty at every
n >= 5** (checked to n = 14). So convention D allows exactly three isospin-type
contributions, and only `(2,2)` sits at the quartet level. Measured alongside:
every `c = 0` shape found is self-conjugate — reported as a measurement to
n = 14, not proved (`c(lambda') = -c(lambda)` gives one direction; the converse
is observed).

## Artifacts

`QOU/Hecke/IsospinClassSingleton.lean`, registered in `QOU.lean`: 5 decls, all
by `decide` and **depending on NO axioms at all**. `lean`-direct exit 0.
`computations/qbeta/qbeta_isospin_class_singleton_probe.py` (7/7, 40 dps).

**The division stated rather than hidden:** the Lean proves the content sums and
uniqueness *within an explicit list*; that the list is all of the partitions of 4
is the standard `p(4) = 5`, verified in the probe rather than in Lean —
formalising partition enumeration over `Nat.Partition` is disproportionate here.
