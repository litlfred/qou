#!/usr/bin/env python3
"""
lever1_descent_transfer_operator.py — the descent-set transfer operator for the
2·maj + content∘RSK involution statistic (lever-1 / z2bn follow-up W6; owner-queued
"build the descent-set transfer operator ... explicitly").

Context. PR #3694 identified the binding period exactly as an involution statistic:

  S^bal(n)·q^{n(n−1)/2} = Σ_{w∈Inv(Sₙ)} q^{2·maj(w) + content(λ(w))}          (C)

(witness lever1-kernel-maj-involution-identification), and measured that maj is NOT
Markovian under RSK insertion on the involutions themselves — the fixed-point
insertion ratio is non-monomial, so no finite fixed-coefficient q-difference kernel
closes at the level of the sequence. This probe builds the EXACT kernel object that
(C) points at instead: a transfer operator on Young's lattice with a marked corner.

THE OPERATOR. Involutions w ↔ single SYT P(w) (RSK, Schützenberger), and
2·maj(w) + content(λ(w)) is a SUM OF LOCAL WEIGHTS along the growth path of P(w):
adding entry k+1 at addable corner (i, j) of the shape contributes

  weight exponent  =  content of the new cell (j − i)  +  2k·[i > r],

where r is the row of entry k (descent k ∈ Des(P) ⇔ k+1 strictly below k, and
maj = Σ_{k∈Des} k). Hence the statistic is Markovian on the LIFTED state space

  state = (λ ⊢ k, r) ,  r = row of the marked (last-added) corner,

and the level-k transfer operator factorizes as

  T_k  =  A_k  +  q^{2k}·B_k ,

with A_k (non-descent edges, i ≤ r) and B_k (descent edges, i > r) both
k-INDEPENDENT in q apart from the monomial entries q^{j−i}: the only level
dependence is the scalar q^{2k} on the descent block. Then

  Σ_{w∈Inv(Sₙ)} q^{2maj+content}  =  1ᵀ · T_{n−1} ⋯ T_1 · e_{((1),0)} .

This IS the insertion recursion at statistic level: an exact, local, two-block
kernel — but on a state space that grows like Σ_{λ⊢n} #corners(λ) (≈ p(n)·√n),
which is why its projection to a FIXED finite basis (a depth-d q-difference
operator) cannot close: the combinatorial face of the Habiro tail D(n).

VERIFICATION (all exact, integer polynomial arithmetic):
  V1  Z_n(transfer) == Σ_w q^{2maj+content} by direct involution enumeration, n ≤ 9;
  V2  Z_n(transfer) == Σ_λ q^{content(λ)}·f̃^λ(q²) (Stanley hook side), n ≤ 16;
  V3  Z_n(transfer) == q^{n(n−1)/2}·S^bal(n) (balanced hook formula), n ≤ 12;
  V4  Z_n(1) == I(n) (involution numbers, telephone recurrence), n ≤ 24.

MEASUREMENTS:
  M1  state-space growth  Σ_{λ⊢n} #corners(λ)  vs involution count I(n);
  M2  row-mark sensitivity: # of shape-transitions (λ→λ′) at each level that carry
      BOTH a descent and a non-descent edge depending on the mark r — nonzero counts
      certify that the (λ, r) lift is genuinely needed (λ alone is not Markovian,
      matching the non-monomial insertion ratios of the prior witness).

Scope: exact/structural; EXPLORATORY; no fit; no wiring; binding S(n) only.
Audit trail: docs/audits/2026-07-12-alien-calculus-review-binding-gevrey-half.md.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

N_T = 24        # transfer-operator levels (V4 + M1 + M2)
N_HOOK = 16     # V2 sympy hook-side identity
N_BAL = 12      # V3 balanced-hook-formula identity
N_DIRECT = 9    # V1 direct involution enumeration


# ---------- integer Laurent-dict polynomials ----------

def padd(acc: dict, poly: dict, shift: int, scale: int = 1) -> None:
    for e, c in poly.items():
        acc[e + shift] += c * scale


# ---------- the transfer operator ----------

def corners(lam: tuple) -> list:
    """Addable corners of λ as (row i, col j) with 0-based indices."""
    out = []
    for i in range(len(lam)):
        if i == 0 or lam[i - 1] > lam[i]:
            out.append((i, lam[i]))
    out.append((len(lam), 0))
    return out


def add_cell(lam: tuple, i: int) -> tuple:
    if i == len(lam):
        return lam + (1,)
    return lam[:i] + (lam[i] + 1,) + lam[i + 1:]


def transfer_levels(nmax: int):
    """Run T_{k}: level k → k+1 on states (λ, r); yield (n, Z_n, stats) per level.

    stats = (n_states, n_edges_A, n_edges_B, n_mark_sensitive_shape_edges).
    """
    states = {((1,), 0): {0: 1}}          # entry 1 at cell (0,0): content 0
    yield 1, dict(states[((1,), 0)]), (1, 0, 0, 0)
    for k in range(1, nmax):              # adding entry k+1; descent weight q^{2k}
        nxt: dict = defaultdict(lambda: defaultdict(int))
        edges_a = edges_b = 0
        # shape-edge → set of descent flags seen (for M2)
        shape_edge_flags: dict = defaultdict(set)
        for (lam, r), poly in states.items():
            for (i, j) in corners(lam):
                desc = i > r
                shift = (j - i) + (2 * k if desc else 0)
                padd(nxt[(add_cell(lam, i), i)], poly, shift)
                if desc:
                    edges_b += 1
                else:
                    edges_a += 1
                shape_edge_flags[(lam, add_cell(lam, i))].add(desc)
        states = {s: dict(p) for s, p in nxt.items()}
        z = defaultdict(int)
        for p in states.values():
            padd(z, p, 0)
        sensitive = sum(1 for fl in shape_edge_flags.values() if len(fl) == 2)
        yield k + 1, dict(z), (len(states), edges_a, edges_b, sensitive)


# ---------- reference sides ----------

def involutions(n):
    if n == 0:
        yield ()
        return
    for w in involutions(n - 1):
        yield w + (n,)
    for k in range(1, n):
        for w in involutions(n - 2):
            rest = [i for i in range(1, n) if i != k]
            m = {i + 1: rest[i] for i in range(n - 2)}
            nw = [0] * n
            for i in range(1, n - 1):
                nw[m[i] - 1] = m[w[i - 1]]
            nw[k - 1] = n
            nw[n - 1] = k
            yield tuple(nw)


def maj(w):
    return sum(i + 1 for i in range(len(w) - 1) if w[i] > w[i + 1])


def rsk_shape(w):
    rows = []
    for x in w:
        for row in rows:
            jj = None
            for idx, y in enumerate(row):
                if y > x:
                    jj = idx
                    break
            if jj is None:
                row.append(x)
                x = None
                break
            row[jj], x = x, row[jj]
        if x is not None:
            rows.append([x])
    return tuple(len(row) for row in rows)


def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for row in lam if row > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def nstat(lam):
    return sum(i * r for i, r in enumerate(lam))


def content(lam):
    if not lam:
        return 0
    conj = [sum(1 for row in lam if row > j) for j in range(lam[0])]
    return nstat(conj) - nstat(lam)


def direct_statistic_poly(n) -> dict:
    z = defaultdict(int)
    for w in involutions(n):
        z[2 * maj(w) + content(rsk_shape(w))] += 1
    return dict(z)


def involution_numbers(nmax):
    I = [1, 1]
    for m in range(2, nmax + 1):
        I.append(I[m - 1] + (m - 1) * I[m - 2])
    return I


def main() -> int:
    import sympy as sp
    q = sp.symbols('q')

    def qint_u(k):
        return sum(q ** i for i in range(k))

    def fake_degree(lam):
        n = sum(lam)
        num = q ** nstat(lam)
        for k in range(1, n + 1):
            num *= qint_u(k)
        den = sp.Integer(1)
        for h in hooks(lam):
            den *= qint_u(h)
        return sp.cancel(num / den)

    def qint_b(k):
        return sp.cancel((q ** k - q ** (-k)) / (q - 1 / q))

    def dimq_bal(lam):
        n = sum(lam)
        d = sp.Integer(1)
        for k in range(1, n + 1):
            d *= qint_b(k)
        for h in hooks(lam):
            d = sp.cancel(d / qint_b(h))
        return d

    def to_sympy(z: dict):
        return sp.expand(sum(c * q ** e for e, c in z.items()))

    print("=== lever-1 W6: descent-set transfer operator  T_k = A_k + q^{2k} B_k ===\n")
    Ivals = involution_numbers(N_T)
    okV1 = okV2 = okV3 = okV4 = True
    growth = {}
    print(f"  {'n':>2} {'states':>7} {'A-edges':>8} {'B-edges':>8} {'mark-sens':>9}"
          f"  {'V1':>4} {'V2':>4} {'V3':>4} {'V4':>4}")
    for n, z, (nstates, ea, eb, sens) in transfer_levels(N_T):
        v1 = v2 = v3 = "-"
        if n <= N_DIRECT:
            ok = (z == direct_statistic_poly(n))
            okV1 &= ok
            v1 = "PASS" if ok else "FAIL"
        if n <= N_HOOK:
            rhs = sp.expand(sum(
                q ** content(l) * fake_degree(l).subs(q, q ** 2)
                for l in partitions(n)))
            ok = sp.expand(to_sympy(z) - rhs) == 0
            okV2 &= ok
            v2 = "PASS" if ok else "FAIL"
        if n <= N_BAL:
            rhs = sp.expand(sp.cancel(
                q ** (n * (n - 1) // 2)
                * sum(dimq_bal(l) for l in partitions(n))))
            ok = sp.expand(to_sympy(z) - rhs) == 0
            okV3 &= ok
            v3 = "PASS" if ok else "FAIL"
        ok = (sum(z.values()) == Ivals[n])
        okV4 &= ok
        v4 = "PASS" if ok else "FAIL"
        growth[n] = {"states": nstates, "edges_A": ea, "edges_B": eb,
                     "mark_sensitive_shape_edges": sens,
                     "involutions": Ivals[n]}
        print(f"  {n:>2} {nstates:>7} {ea:>8} {eb:>8} {sens:>9}"
              f"  {v1:>4} {v2:>4} {v3:>4} {v4:>4}")

    print("\nReadings:")
    print("  * The operator is EXACT and local: two fixed blocks (A = non-descent,")
    print("    B = descent), entries q^{content of added cell}; the ONLY level")
    print("    dependence is the scalar q^{2k} on B — a q-difference-like structure,")
    print("    but on the marked-corner Young lattice, not on a fixed finite basis.")
    print(f"  * State space grows sub-exponentially ({growth[N_T]['states']} states at"
          f" n={N_T} vs I({N_T}) = {Ivals[N_T]} involutions) yet UNBOUNDEDLY —")
    print("    no fixed-depth truncation closes, matching the measured")
    print("    non-q-holonomicity and the Habiro tail D(n).")
    print("  * Mark-sensitivity counts are nonzero at every level ≥ 4 (at n ≤ 3 each")
    print("    shape edge still has a unique source state, so nothing to disagree): the same")
    print("    shape edge λ→λ′ carries both descent and non-descent weight depending")
    print("    on the marked row — the (λ, r) lift is genuinely minimal; λ alone is")
    print("    not Markovian (the prior witness's non-monomial insertion ratios).")

    sens_ok = all(growth[n]["mark_sensitive_shape_edges"] > 0
                  for n in range(4, N_T + 1))
    ok = okV1 and okV2 and okV3 and okV4 and sens_ok
    print(f"\n### Verdict: {'ALL CHECKS PASS' if ok else 'CHECK FAILED'}"
          f"  (V1 n<={N_DIRECT}, V2 n<={N_HOOK}, V3 n<={N_BAL}, V4 n<={N_T},"
          " mark-sensitivity > 0 for n>=4)")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-descent-transfer-operator", engine="sympy")
        wb.set_description(
            "Lever-1 W6 (z2bn follow-up): explicit descent-set transfer operator for the "
            "2*maj + content(RSK) involution statistic of the binding period "
            "(S^bal(n)*q^(n(n-1)/2), witness lever1-kernel-maj-involution-identification). "
            "States are (partition, marked corner row); level-k step T_k = A_k + q^(2k)*B_k "
            "with A = non-descent edges, B = descent edges, entries q^(content of added "
            "cell) — the only level dependence is the scalar q^(2k) on the descent block. "
            "Verified exactly: V1 vs direct involution enumeration (n<=9), V2 vs the "
            "Stanley hook side sum_lambda q^content * fakedeg(q^2) (n<=16), V3 vs the "
            "balanced hook formula q^(n(n-1)/2)*S^bal(n) (n<=12), V4 q=1 gives the "
            "telephone numbers I(n) (n<=24). Measured: state space grows like "
            "sum_lambda #corners (sub-exponential, ~p(n)) yet unboundedly — no fixed "
            "finite-basis (depth-d q-difference) projection closes; and every level >=4 "
            "has shape edges carrying BOTH descent and non-descent weight depending on "
            "the mark, so the (lambda, r) lift is genuinely minimal. This is the exact "
            "kernel object the identification points at: an insertion recursion at "
            "statistic level. Exact integer/sympy arithmetic; no fit; no wiring; "
            "EXPLORATORY.")
        wb.add_data("V1_direct_enumeration_max_n", N_DIRECT)
        wb.add_data("V2_hook_side_max_n", N_HOOK)
        wb.add_data("V3_balanced_formula_max_n", N_BAL)
        wb.add_data("V4_telephone_at_q1_max_n", N_T)
        wb.add_data("growth_and_edges_by_n",
                    {str(n): growth[n] for n in sorted(growth)})
        wb.add_assertion(
            name="descent_transfer_operator_reproduces_binding_statistic",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("T_k = A_k + q^(2k)B_k on (partition, marked-corner-row) states "
                    "reproduces Sigma_{w in Inv} q^(2 maj + content(RSK)) exactly "
                    "(V1 n<=9, V2 n<=16, V3 n<=12, V4 q=1 n<=24); mark-sensitive "
                    "shape edges nonzero for all n>=4 (the lift is minimal)."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
