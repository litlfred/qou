---
# qou-9w5z
title: 'Habiro head criterion A = N(-1): why does the composite factor of 3 appear, and is the multiplier 12 structural?'
status: in-progress
type: task
priority: normal
created_at: 2026-08-28T15:17:19Z
updated_at: 2026-08-28T15:29:32Z
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
