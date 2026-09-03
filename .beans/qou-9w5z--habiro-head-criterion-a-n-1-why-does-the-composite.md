---
# qou-9w5z
title: 'Habiro head criterion A = N(-1): why does the composite factor of 3 appear, and is the multiplier 12 structural?'
status: completed
type: task
priority: normal
created_at: 2026-08-28T15:17:19Z
updated_at: 2026-08-28T18:39:38Z
---

## ANSWERED — the 3 is not structural, and p=3 closes at j=3

Probe: `computations/probes/habiro_head_criterion_structure_probe.py`.
All arithmetic exact; every claim below is machine-checked in it.

### 1. A = P(-1) is an IDENTITY, and u = -1 is q = 1

`(u;u)_m` at u = -1 has `1 - (-1)^2 = 0` as its second factor, so every
m >= 2 term of the reconstruction `P(u) = sum_m a_m(u) (u;u)_m` drops and

    P(-1) = a_0(-1)*1 + a_1(-1)*2 = A.

No prime enters — this is stronger than the mod-p route the previous probe
used. The extractor substitutes q -> u^2, so u = -1 IS q = 1 reached along
the non-trivial square root, and with shift 0

    A = denom(-1) * tr_M(q=1).

### 2. The trace at q=1 has no 3 in it

Measured 5/5: tr_M(q=1) = 2^(1-2A) — 1/2, 1/2, 1/8, 1/32, 1/32. A pure
power of two. **So the 3 is not in the trace at all**; it enters only
through the normalisation denom(-1).

### 3. The 3 is the denominator of delta

`delta = flavor_split_leading(q) = (q-1)^2 (q^4-1)/(3 q^4)`
`= hbar_q^2 h_q [2]_q / 3` (prop:flavor-split-substrate) carries a literal
/3. Per-kind at u = -1:

    positive           num=1   den=2
    negative           num=1   den=2
    averaged           num=2   den=4
    averaged_weighted  num=12  den=24    <-- the only one with a 3

`averaged_weighted` is the only kind that uses delta, and
`canonical_interface_kinds` places **exactly one** of it per MIXED atom
(Z>=1 and N>=1) — the single p-n junction — and zero for a pure atom.
Verified on all 27 (Z,N) with Z+N <= 6.

**That is why the multiplier was 12 for D, T and 3He alike** rather than
12^(number of interfaces): the junction count is 1 regardless of mass.

### 4. Closed form, and the prediction it makes and passes

    A(Z,N) = 2^(3Z+N) * 12^[Z>=1 and N>=1]

27/27 cells, Z+N <= 6, computed straight from the closed form (A is just
P(-1), so no Habiro expansion is needed — this reaches pure composites the
five on-disk atoms cannot). 3 | A on 15/15 mixed and 0/12 pure, exactly as
predicted. **So 3 is the ONLY odd prime that can ever divide A**, and it
does so exactly for mixed atoms.

### 5. p = 3 CLOSES at j = 3

Raising the head index fires for every composite at j=3. Combined with the
previous probe: **Frob_p != 0 for all five atoms at every odd prime** —
nucleons at j=2 for all odd p, composites at j=2 for odd p != 3 and at j=3
for p=3. The p=3 silence was an artifact of the index, exactly as (2)-(4)
predict.

### 6. p = 2 is a HARD CEILING, not a data gap

In Z[i] the Pochhammer `(i;i)_4 = 0`, so v_(1-i) of the divisor is capped
at 4 (it is 1, 3, 4 for j = 1, 2, 3). The criterion fires iff
v(head_j) < v((i;i)_j). Measured:

    proton    v(head) = 6, 8, 5     vs 1, 3, 4   never
    neutron   v(head) = 2, 2, 2     vs 1, 3, 4   FIRES at j=2
    deuteron  v(head) = 12, 18, 4   vs 1, 3, 4   never (j=3 ties, 4 vs 4)
    tritium   v(head) = 14, 16, 5   vs 1, 3, 4   never
    3He       v(head) = 18, 18, 5   vs 1, 3, 4   never

Only the neutron, with v(head) = 2, is shallow enough. **No additional
coefficients can help** — the ceiling is on the divisor, not the head. So
p=2 is out of reach of this method for four of the five atoms, and a
different argument is needed there. Silence is still not vanishing: the
frobenius probe measures nonzero at p=2 for all of them.

**This is the real 2-adic content, and it is the OPPOSITE of the retracted
finding in qou-iph3.** That claim was "the denominators are powers of two",
measured on stale data. The true 2-adic fact is that the trace's 2-adic
DEPTH is what BLOCKS the criterion at p=2 — deep is bad, not good, and the
neutron wins by being shallow.


## CORRECTION — p=2 is NOT open. I framed it wrong.

I closed the previous entry saying "p=2 needs a different argument" and
reported it to the author as "the honest open item". **That was wrong**, and
the error was conflating two different things:

- the HEAD CRITERION cannot decide p=2 (true, and §6 above proves the
  ceiling is structural rather than a shortage of coefficients);
- therefore the QUESTION is open (false).

p=2 is a **single prime**, and `(i;i)_4 = 0` truncates the sum after four
terms whose coefficients `a_0..a_3` every atom already carries on disk. So
Frob_2 is a finite exact computation in Z[i] — it needs no criterion at all.
There is no infinitude to cover, which is the only thing the criterion buys.

Measured exactly, on every (Z,N) with Z+N <= 6 (27 cells, 0 mismatches):

    P(i) = P(-1) = A                    the SAME integer runs p=2 and odd p
    Frob_2 = P(i)/denom(i) = -2^(1-2M)  M = Z+N;  NEVER zero

so **Frob_2 != 0 for every atom, 27/27** — and with the odd-prime result,
**Frob_p != 0 at EVERY prime.** The arc's non-vanishing requirement is met.

### What IS distinctive about p=2, and it is not vanishing

`Frob_2` is **not an algebraic integer** — 0/27 cells — with
v_(1-i)(Frob_2) = -2(2M-1) < 0. Its Galois trace over Q(i)/Q is an integer
only for M = 1, which is exactly the 2/45 the frobenius probe reports for
`step2_full_trace_passed` (proton and neutron at p=2, Tr(full) = -1).

That is the same fact as the ceiling, seen from the other side: an
integrality-flavoured divisibility criterion has nothing to say at the one
prime where the value is not integral. So §5 and §6 are not in tension —
§5 explains WHY no criterion works there, §6 shows none is needed.

### Cross-check that caught my own reading

I initially thought my Frob_2 = -1/2 contradicted the probe's
`step2_full_trace_passed = True` for the proton at p=2. It does not:
`denom_folded` is not a unit claim, and Tr(-1/2) over Q(i)/Q is -1, an
integer. The two computations agree; my reading of the flag was the error.

### Witness fields corrected

`p2_closes: false` was misleading on its own and is replaced by
`p2_head_criterion_closes: false` + `p2_closed_by_direct_evaluation: true`,
with `frob_2_closed_form` and `frobenius_nonzero_at_every_prime: true`.

### Lean

Four more sorry-free declarations making the p=2 collapse citable rather
than only computed: `qPochDiag_{two,three,four}_of_sq_eq_neg_one`
((z;z)_2 = 2(1-z), (z;z)_3 = 4, (z;z)_4 = 0 at a primitive fourth root) and
`habiroEval_at_sq_eq_neg_one`, which gives the four-term evaluation for
every N >= 4.


## RETRACTION within the correction — non-integrality is GENERIC

The entry above says the distinctive thing about p=2 is that Frob_2 is not an
algebraic integer, and offers that as the reason an integrality-flavoured
criterion has nothing to say there ("two views of the same fact"). **I checked
that instead of asserting it, and it is wrong.**

Measured across all 45 (atom, prime) cells with the tested primes
{2,3,5,7,11,13,17,19,23}: Frob_p is an algebraic integer on **0 of 45**.
Non-integrality holds everywhere, so it cannot distinguish p=2 from any other
prime and explains nothing about the ceiling. Recorded as section [8] of the
probe with the full scan, precisely so the wrong reading is not re-derived.

**What IS special at p=2** is the length of the truncation, nothing subtler.
`(u;u)_m` vanishes at m = 2p, so p=2 gives the criterion the FEWEST usable
indices of any prime — three — and caps the divisor's valuation at 4. That one
fact cuts both ways, and this is the real "two views": a short truncation
starves the criterion and simultaneously makes direct evaluation trivial.
p = 2 is the worst prime for the criterion and the best for evaluation.

The rest of the correction stands unchanged: p=2 is closed by direct
evaluation, Frob_2 = -2^(1-2M) on 27/27 cells, and P(i) = P(-1) = A.

Also added, closing a genuine gap in the "every prime" claim: every
non-vanishing result above is about the NUMERATOR, and Frob_p = P/denom is
equally undefined if the denominator vanishes at zeta_{2p} (a pole, not a
zero). It never does, for any atom at any prime — deg Phi_{2p} = p-1, so once
p-1 > deg(denom) the cyclotomic cannot divide, and every prime below that
bound is checked explicitly (9 to 23 primes per atom, 0 hits).

Note P(i) = P(-1) is forced rather than coincidental: tr_M(-1) = -tr_M(1) and
denom(i) = -denom(-1), and the two sign flips cancel.


## Third correction, and the one with the widest blast radius

While checking whether "non-integrality is generic" was consistent with the
frobenius probe reporting `step2_full_trace_passed` 2/45, I found the two
could not both be true under my description of that test — so I read the code
instead of reasoning about the name.

`habiro_frobenius_probe.py` sets its flag by `sp.invert(denom, Phi_2p)`, which
works over **Q**. Q(zeta_2p) is a field, so that succeeds for ANY nonzero
denominator: the flag is a **nonzero test, not a unit test**. It was named
`denom_unit` and its comment read "Denominator is not a unit in Z[zeta_2p]",
and I took the name at face value.

Consequences, all mine:

- I wrote in PR #5884's body and in a commit message that the full-trace test
  "additionally requires the denominator to be a unit at zeta_{2p}, so
  Tr(Frob_p) itself is an algebraic integer". **Wrong twice**: the flag is not
  a unit test, and Frob_p is an algebraic integer on 0/45 cells, so a real
  unit test would pass nowhere and the test would be 0/45 rather than 2/45.
- The same wrong sentence had been written into the witness `summary_note`.

What the full-trace test actually detects is integrality of the **Galois
trace**, not of the element. Since the denominator never vanishes (section 7),
the discriminating condition is purely `full_trace_is_integer`.

Fixed: variable renamed `denom_unit` -> `denom_nonzero`, the misleading comment
replaced by one stating the ring the inversion happens in and citing the 0/45
measurement, the error string "not a unit" -> "not invertible", and the
witness `summary_note` rewritten with the correction recorded in place.

The witness field name `denom_folded` is kept — it is accurate, the value WAS
folded — and only the internal name was lying.

Worth noting why 2/45 is p=2 and the nucleons: Frob_p = tr_M(zeta_p), so at
p=2 the argument is zeta_2 = -1 and the value lands in Q, where the trace of
-1/2 over Q(i)/Q is the integer -1. p=2 is the only prime whose value is
rational at all. That is a third distinct sense in which p=2 is special, and
it is unrelated to both the truncation length and to integrality.


## CLOSED — PR #5884 merged to main as ef261ff5b6 (2026-08-28)

The question this bean opened — is the composite factor of 3 structural? — is
answered NO, with the mechanism identified and machine-checked: it is the
literal /3 in delta = flavor_split_leading(q), reaching A through the single
averaged_weighted interface that every mixed atom has and no pure one does.

Landed: two probes (habiro_head_divisibility_probe,
habiro_head_criterion_structure_probe), ten sorry-free Lean declarations in
QOU/Habiro/CyclotomicEvaluation.lean, and three retractions recorded in place
rather than dropped.

Verification re-run in full after the rebase onto main, not carried over:
lean-direct exit 0 with #print axioms clean on all ten; all three probes
reproduce identically (empty witness diffs under volatile-key masking); the
one remaining precision-gate RED is in docs/audits/, which the branch touches
zero files of.
