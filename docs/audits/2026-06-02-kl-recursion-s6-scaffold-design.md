# Kazhdan–Lusztig recursion scaffold — extend `kazhdan_lusztig.py` past n ≤ 4 cap to S_5, S_6

**Date:** 2026-06-02
**Branch:** `claude/kl-recursion-s6-scaffold-2026-06-02`
**Blocks:** Option-E PROBE 4 full path (the live in-Option-E
direction surfaced by PR #1516's cheap-pass refutation).

## Context

[`computations/kazhdan_lusztig.py`](../../computations/kazhdan_lusztig.py)
is currently capped at **n ≤ 4** (Coxeter rank ≤ 3).  The cap is
NOT theoretically grounded — Brenti (*Combinatorics of Coxeter
Groups* §5.1) shows every Kazhdan–Lusztig polynomial
`P_{x,w}(q) = 1` only at **rank ≤ 2** (dihedral groups, i.e.
n ≤ 3).  S_4 (rank 3) already has the famous

  P_{e, (3,4,1,2)}(q) = 1 + q

as the minimal non-trivial KL polynomial in any symmetric group
("3412" example).  The existing closed-form code's "rank ≤ 3"
applicability claim at n ≤ 4 is a latent bug — it returns 1 in
6 Bruhat pairs at S_4 that should be `1 + q`.  This scaffold
fixes the bug by routing **n ≥ 4** through the full Kazhdan-Lusztig
recursion (K-L 1979 §1.1 + Brenti §5.2).

## Why now: PR #1516 PROBE 4 verdict

PR #1516's PROBE 4 cheap pass tested four single-vertex / closed-
form Δ_λ candidates (χ^λ(w_0), |χ^λ(w_0)|, sgn·dim_λ, peak-diag);
all four refuted (miss ≥ 66 % on deuteron).  Combined with
`rho_w_crystal_vertex_trace.py`'s upstream regular-multiplicity
result (Σ_w ρ_w = χ^λ refuted by trace identity), the **live
in-Option-E direction** is now:

  Δ_λ(K) = Σ_w n^w_λ · ρ_w(K)         (full KL multiplicity)

with **non-trivial** `n^w_λ` = Kazhdan–Lusztig multiplicities from
the cell decomposition of S_n.  This requires computing
`P_{x,w}(q)` for `n = 6` (deuteron is H_6).  Hence the scaffold.

## Algorithm — Kazhdan–Lusztig recursion (1979 §1.1)

Standard recursion (notation: `ℓ(w)` = Coxeter length, `s` =
simple reflection):

For `w` with right descent `s` (i.e. `ws < w`), let

  c(x, w; s) :=
    q · P_{xs, ws}(q) + P_{x, ws}(q)   if xs > x  (c=0)
    P_{xs, ws}(q) + q · P_{x, ws}(q)   if xs < x  (c=1)

Then

  P_{x, w}(q) = c(x, w; s)
              − Σ_{x ≤ z < ws, zs < z}
                  μ(z, ws) · q^{(ℓ(w) − ℓ(z))/2} · P_{x, z}(q)

where `μ(z, w')` is the coefficient of `q^{(ℓ(w') − ℓ(z) − 1)/2}`
in `P_{z, w'}(q)` (the *leading* coefficient, by convention 0
unless the parity is right).

Base cases:

| condition       | value         |
|-----------------|---------------|
| `x = w`         | 1             |
| `x ̸≤ w`        | 0             |
| `ℓ(w) ≤ 1`      | 1 if `x ≤ w` else 0 |

The recursion terminates because each `P_{x', w'}` call has
`ℓ(w') < ℓ(w)`.  With memoization, each `P_{x,w}` is computed at
most once.

## Complexity

| n | \|S_n\| | Bruhat-comparable pairs (rough) | KL polys to memoize |
|---|---|---|---|
| 5 | 120 | ~ 7,200 | 7.2k |
| 6 | 720 | ~ 260,000 | 260k |
| 7 | 5,040 | ~ 12,700,000 | 12.7M |

For S_6 (the immediate need), 260k polynomials × O(720) work per
recursion step × O(n²) Bruhat checks → minutes at sympy native
speeds.  Plenty fast for a one-shot witness computation.

For S_7 the scaffold should still terminate but may take an hour;
that's a separate concern from the deuteron problem.

## Implementation plan — microcommit granularity

1. **commit 1**: this design doc + scaffold marker in
   `kazhdan_lusztig.py` (no recursion yet; updates the
   `NotImplementedError` message to point at the scaffold work).
2. **commit 2**: implement `kl_polynomial_recursive(x, w)` —
   memoized recursion, no public-API change yet; gate behind a
   helper.
3. **commit 3**: cross-check vs Brenti's known S_5 table (e.g.,
   `P_{1432, 4321}` — verify the first non-trivial value).
4. **commit 4**: lift the public `kl_polynomial(x, w)` cap from
   n ≤ 4 to n ≤ 6 (route to the recursive helper for n ≥ 5);
   keep `NotImplementedError` at n ≥ 7 as a soft cap.
5. **commit 5**: extend the self-test for n = 5 and n = 6 —
   Bruhat-count assertion, round-trip T→C→T, bar-invariance,
   and at least one explicit non-trivial KL value match.
6. **commit 6**: extend `canonical_basis_C_w` and the two
   change-of-basis functions to support n = 5, 6 (route through
   the recursive `kl_polynomial`).
7. **commit 7**: witness assertions for n = 5, 6 in the witness
   builder.

After this scaffold lands, **downstream** work (separate PR /
follow-up) extracts `n^w_λ` from KL cells + computes
`ρ_w(β_D)` per crystal vertex + tests Δ_λ(D) closure.  That's
~hours of additional careful implementation; out of scope here.

## Cross-checks (acceptance criteria)

The scaffold is accepted if all hold:

- **S_5**: Bruhat-count `|[e, w_0]| = 120`; round-trip T→C→T = id
  on all 120 elements; first non-trivial `P_{x,w}` matches Brenti
  table (`P_{1432, 4321}(q) = 1 + q` or equivalent canonical
  example).
- **S_6**: Bruhat-count `|[e, w_0]| = 720`; round-trip = id on a
  representative subset (full 720 may be too slow for the
  self-test; sample 50 longest elements); at least 3 explicit
  non-trivial KL values match a reference.
- Memoization cache size for S_6 ≤ 300k entries (sanity bound).
- All assertions emit clean to the witness JSON.

## References

- Kazhdan, Lusztig, *Representations of Coxeter groups and Hecke
  algebras*, Inventiones Math. 53 (1979), 165–184.
- Brenti, *Combinatorics of Coxeter groups*, GTM 231 (2005),
  §5.1 (closed form rank ≤ 3) + §5.2 (full recursion).
- Lusztig, *Hecke algebras with unequal parameters*, CRM Monograph
  Series 18 (2003) — canonical-basis normalisation.
- Goresky, *Tables of Kazhdan–Lusztig polynomials* (online; reference
  for cross-checking computed values at S_5 / S_6).

## Coordination

- **PR #1516** (Option-E Phase 2 entry-point + PROBE 4 cheap-pass
  refutation) is the immediate parent — its refutation establishes
  the need for this scaffold.  This branch is downstream of #1516
  but technically independent (touches only `kazhdan_lusztig.py`
  + adds witnesses; no overlap with #1516's probes).
- **`rho_w_crystal_vertex_trace.py`** (on main) implements the
  Hoefsmit/Young seminormal ρ_w per crystal vertex.  This scaffold
  produces the n^w_λ multiplicities that — when summed against
  ρ_w in the follow-up — give the full Σ_w n^w_λ · ρ_w(K)
  candidate.
- **PR #1709** (volume-Wedderburn) is adjacent: their q-6j saddle
  direction and this scaffold's KL direction are both live
  candidates for Δ_λ closure.  If the KL path closes, the q-6j
  path becomes redundant (and vice versa).
