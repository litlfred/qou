#!/usr/bin/env python3
"""(P), the Pieri step of the Macdonald hook telescope — measured, not recalled.

The telescope `Z_n = Σ_{λ⊢n} f_λ · s_λ(Q,X) = ((1−X)/(1−Q))^n` is proved in
`y_lambda_macdonald_telescope.py` for n = 0…8 by direct expansion. It also
follows by induction from two elementary statements, which is the route the
Lean formalisation takes (`QOU/MathlibExt/MacdonaldTelescope.lean`):

  (P)  Σ_{μ = λ + box}  s_μ(Q,X)  =  ((1−X)/(1−Q)) · s_λ(Q,X)
  (F)  f_λ = Σ_{ν = λ − box} f_ν

This probe establishes three facts about (P) that were previously being
asserted from memory. Each was wrong at least once when asserted that way.

1. **(P) itself**, symbolically with X FREE — not merely at X = Q^r.

2. **The per-shape ratio has a closed form**, and it is exactly

       s_{λ+□(r)} / s_λ
         =  Q^r · (1 − X·Q^{λ_r − r}) / (1 − Q^{h_μ(r, λ_r)})
              · ∏_{h ∈ arm ∪ leg} (1 − Q^h) / (1 − Q^{h+1})

   where arm = {h_λ(r,j) : j < λ_r} and leg = {h_λ(i,λ_r) : i < r, λ_i > λ_r}
   are exactly the cells the Lean hook-length update rule moves. Q^r is
   `nLambda_addBoxRow`.

3. **The shift product does NOT collapse.** At λ = (3,2,1), r = 1 it is
   `(Q²+Q+1)/((Q+1)³(Q²+1))` — a genuine rational function. This matters
   because it is the opposite of what I recorded on 2026-08-26: I wrote that
   relating the shifted and unshifted row products "collapses only because of
   what a row's hook lengths actually are — the hook-walk". It does not
   collapse at all. What telescopes is the SUM over corners, not the summand.

Precision: this probe is EXACT throughout — sympy symbolic over ℚ(Q,X), with
`cancel` deciding equality. No float appears anywhere, so the NO-FLOAT64
discipline (AGENTS.md §"PROBES ARE NOT EXEMPT") is satisfied by construction
rather than by tolerance. No witness is emitted: every output is a symbolic
identity that re-derives in seconds, and there is no measured number to record.
"""

from sympy import symbols, prod, factor, cancel

Q, X = symbols("Q X")


def hook(lam, i, j):
    """Hook length of cell (i, j), 0 outside the diagram. Mirrors the Lean
    `Partition.hookLength` exactly: arm + leg + 1, leg counted over rows below."""
    if i >= len(lam) or j >= lam[i]:
        return 0
    arm = lam[i] - j - 1
    leg = sum(1 for x in lam[i + 1:] if x > j)
    return arm + leg + 1


def n_lambda(lam):
    """n(λ) = Σ_i i·λ_i, 0-indexed rows. Mirrors the Lean `nLambda`."""
    return sum(i * lam[i] for i in range(len(lam)))


def schur_element(lam):
    """s_λ(Q, X) = Q^{n(λ)} ∏_{cells} (1 − X·Q^{c}) / (1 − Q^{h})."""
    out = Q ** n_lambda(lam)
    for i in range(len(lam)):
        for j in range(lam[i]):
            out *= (1 - X * Q ** (j - i)) / (1 - Q ** hook(lam, i, j))
    return out


def addable_corners(lam):
    """Rows where a box may be added: row 0, any row shorter than the one above,
    and a new bottom row.

    NOTE for the Lean side: `addBoxRow` is `List.set`, which is a NO-OP out of
    range, so `addBoxRow λ (length λ)` is `λ` and NOT `λ ++ [1]`. The new-bottom-row
    corner is therefore not expressible by `addBoxRow` and needs its own operation.
    """
    out = []
    for r in range(len(lam)):
        if r == 0 or lam[r] < lam[r - 1]:
            grown = list(lam)
            grown[r] += 1
            out.append((r, tuple(grown)))
    out.append((len(lam), tuple(list(lam) + [1])))
    return out


def check_pieri(lam):
    corners = addable_corners(lam)
    lhs = sum(schur_element(mu) for _, mu in corners)
    rhs = (1 - X) / (1 - Q) * schur_element(lam)
    return cancel(lhs - rhs) == 0, [c[1] for c in corners]


def check_ratio(lam, r):
    """Fact 2: the closed form for one corner's ratio."""
    grown = list(lam)
    grown[r] += 1
    mu = tuple(grown)
    m = lam[r]
    arm = [hook(lam, r, j) for j in range(m)]
    leg = [hook(lam, i, m) for i in range(r) if lam[i] > m]
    shift = prod([(1 - Q ** h) / (1 - Q ** (h + 1)) for h in arm + leg])
    predicted = Q ** r * (1 - X * Q ** (m - r)) / (1 - Q ** hook(mu, r, m)) * shift
    actual = schur_element(mu) / schur_element(lam)
    return cancel(actual - predicted) == 0, arm, leg, factor(cancel(shift))


def main():
    shapes = [(1,), (2,), (1, 1), (2, 1), (3,), (2, 2), (3, 1), (3, 2, 1)]

    print("(P): Sum over addable corners == ((1-X)/(1-Q)) * s_lambda, X free")
    ok_all = True
    for lam in shapes:
        ok, corners = check_pieri(lam)
        ok_all &= ok
        print(f"  lam={lam!s:<12} corners={len(corners)}  {'OK' if ok else 'FAIL'}")

    print("\nPer-shape ratio closed form (fact 2), and the shift product (fact 3)")
    for lam, r in [((3, 2, 1), 1), ((2, 1), 0), ((3, 1), 1)]:
        ok, arm, leg, shift = check_ratio(lam, r)
        ok_all &= ok
        print(f"  lam={lam!s:<10} r={r}  arm={arm} leg={leg}  {'OK' if ok else 'FAIL'}")
        print(f"    shift product = {shift}   <- does not collapse")

    print("\nall exact:", ok_all)
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
