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

4. **(P) splits into TWO one-variable identities.** The ratio is **linear in
   `X`**, and structurally so: adding one box adds exactly one cell, hence
   exactly one numerator factor `(1 − X·Q^c)`; everything else in the ratio is
   hook lengths, which carry no `X`. So

       R_r  =  K_r · (1 − X·Q^{c_r}),      K_r free of X,

   and matching coefficients of `X` on both sides of (P) gives

       (P1)  Σ_r K_r            =  1/(1 − Q)
       (P2)  Σ_r K_r · Q^{c_r}  =  1/(1 − Q)

   equivalently `Σ_r K_r·(1 − Q^{c_r}) = 0`. **A two-variable identity becomes
   two one-variable ones**, which is the reduction the general proof wants.

5. **The new box's hook is always 1** — at every addable corner, the interior
   ones and the new bottom row alike. Nothing lies to its right or below it.

6. **Both identities have a clean form summing to exactly 1.** Substituting
   fact 5 into `K_r` clears the only denominator outside the product:

       (P1)   Σ_r  Q^{r}      · ∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})  =  1
       (P2)   Σ_r  Q^{λ_r}    · ∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})  =  1

   Same product, two weightings — the **row index** and the **row length**
   (both `0` for the new bottom row) — each summing to `1`.

7. **(P2) IS (P1) at the conjugate partition**, so the two are one identity.
   Transposing sends the corner in row `r` at `(r, λ_r)` to the corner in row
   `λ_r` at `(λ_r, r)`, so "row index" and "row length" swap; and hook lengths
   are transposition-invariant, `h_λ(i,j) = h_{λ'}(j,i)`, so the product is
   unchanged. Hence `(P2)[λ] = (P1)[λ']`.

   **The whole Pieri step therefore reduces to ONE identity:**

       Σ_r  Q^{r} · ∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})  =  1

   (P2) follows by conjugation, and (P) from the two by X-linearity. That is
   the target a Lean proof should aim at: one variable, no outer denominator,
   right-hand side a literal `1`.

8. **(P) at `Q → 1` IS (F), the SYT branching rule.** They are not two
   independent inputs — **(F) is the `q → 1` shadow of (P)**.

   Each factor `(1 − Q^h)/(1 − Q^{h+1}) → h/(h+1)`, so fact 6's (P1) becomes
   `Σ_r ∏_{h ∈ arm ∪ leg(r)} h/(h+1) = 1`. Now the Lean hook-length update rule
   — hook `+1` on `arm ∪ leg`, new box hook `1`, everything else unchanged —
   gives `∏_{c ∈ μ} h_μ(c) = ∏_{c ∈ λ} h_λ(c) · ∏_{h ∈ arm ∪ leg} (h+1)/h`.
   Feed that through Frame–Robinson–Thrall (`f_ν · ∏hooks(ν) = |ν|!`):

       f_μ / f_λ  =  (n+1) · ∏_{h ∈ arm ∪ leg} h/(h+1)

   so `Σ_r ∏ h/(h+1) = 1` **iff** `Σ_{μ = λ+□} f_μ = (n+1)·f_λ`, which is (F).

   **This corrects the framing carried in PR #5857 §4 and #5871**, where (P)
   and (F) were listed as two separate elementary statements the telescope
   needs. They are one statement and its `q → 1` degeneration. The general-`n`
   telescope rests on a single q-deformed identity.

   FRT is **machine-checked in this corpus**, sorry-free, at
   `QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct`
   (`QOU/Mathlib/HookLengthFormula.lean:171`) — so the `q = 1` case of the
   identity is reachable from corpus material plus the update rule already
   proved. Only the q-deformation is genuinely open.

   **Read the evidence for fact 7 carefully.** The **self-conjugate** shapes
   — `(1)`, `(2,1)`, `(2,2)`, `(3,2,1)`, `(3,3,2)` — satisfy
   `(P2)[λ] = (P1)[λ']` trivially, because `λ' = λ`. They are not evidence for
   anything. `main()` therefore labels each shape and reports how many carry
   information; at the shapes currently checked that is **6 of 11**. Do not
   quote a count from this docstring — run it, because the shape list changes
   and a hand-kept number decays. (This note replaces a count of "four" that
   was wrong the moment it was typed.)

Precision: this probe is EXACT throughout — sympy symbolic over ℚ(Q,X), with
`cancel` deciding equality. No float appears anywhere, so the NO-FLOAT64
discipline (AGENTS.md §"PROBES ARE NOT EXEMPT") is satisfied by construction
rather than by tolerance. No witness is emitted: every output is a symbolic
identity that re-derives in seconds, and there is no measured number to record.
"""

from sympy import Rational, cancel, factor, factorial, prod, symbols

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


def shift_product(lam, r):
    """`∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})`, and the row's length.

    `r == len(lam)` is the new bottom row: it has no arm, and its leg is every
    nonempty row above it (all of which exceed column 0)."""
    if r < len(lam):
        m = lam[r]
        arm = [hook(lam, r, j) for j in range(m)]
        leg = [hook(lam, i, m) for i in range(r) if lam[i] > m]
    else:
        m = 0
        arm = []
        leg = [hook(lam, i, 0) for i in range(len(lam)) if lam[i] > 0]
    return prod([(1 - Q ** h) / (1 - Q ** (h + 1)) for h in arm + leg]), m


def check_split(lam):
    """Facts 4 and 5: X-linearity of each ratio, and the new box's hook."""
    Ks, cs, new_hooks = [], [], []
    for r, mu in addable_corners(lam):
        if r < len(lam):
            m, c = lam[r], lam[r] - r
        else:
            m, c = 0, -len(lam)
        K = cancel((schur_element(mu) / schur_element(lam)) / (1 - X * Q ** c))
        Ks.append(K)
        cs.append(c)
        new_hooks.append(hook(mu, r, m))
    x_free = all(K.free_symbols <= {Q} for K in Ks)
    target = 1 / (1 - Q)
    p1 = cancel(sum(Ks) - target) == 0
    p2 = cancel(sum(K * Q ** c for K, c in zip(Ks, cs)) - target) == 0
    return x_free, p1, p2, all(h == 1 for h in new_hooks), cs


def num_syt(lam):
    """`#SYT(λ)` by the classical hook-length formula. Exact `Rational`."""
    hook_prod = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            hook_prod *= hook(lam, i, j)
    return factorial(sum(lam)) / hook_prod


def check_q1_is_branching(lam):
    """Fact 8: at `Q → 1` the identity is the SYT branching rule.

    Returns `(identity holds at q=1, branching rule holds)` — both computed
    independently, so agreement is a cross-check rather than a restatement."""
    q1 = 0
    for r, _ in addable_corners(lam):
        if r < len(lam):
            m = lam[r]
            hs = ([hook(lam, r, j) for j in range(m)]
                  + [hook(lam, i, m) for i in range(r) if lam[i] > m])
        else:
            hs = [hook(lam, i, 0) for i in range(len(lam)) if lam[i] > 0]
        q1 += prod([Rational(h, h + 1) for h in hs])
    branch = sum(num_syt(mu) for _, mu in addable_corners(lam))
    return q1 == 1, branch == (sum(lam) + 1) * num_syt(lam)


def conjugate(lam):
    """The transpose partition: column `j` becomes the count of rows exceeding `j`."""
    if not lam:
        return ()
    return tuple(sum(1 for x in lam if x > j) for j in range(max(lam)))


def weighted_corner_sum(lam, weight):
    """`Σ_r w_r · ∏ (1−Q^h)/(1−Q^{h+1})`, with `w_r = Q^r` or `Q^{λ_r}`."""
    total = 0
    for r, _ in addable_corners(lam):
        prod_r, m = shift_product(lam, r)
        total += (Q ** r if weight == "row" else Q ** m) * prod_r
    return cancel(total)


def check_conjugation(lam):
    """Fact 7: `(P2)[λ]` and `(P1)[λ']` are the same rational function.

    Returns the verdict and whether `λ` is self-conjugate — a self-conjugate
    shape satisfies this trivially and is NOT evidence."""
    lam_c = conjugate(lam)
    same = cancel(weighted_corner_sum(lam, "len") - weighted_corner_sum(lam_c, "row")) == 0
    return same, lam_c == tuple(lam), lam_c


def check_clean(lam):
    """Fact 6: both identities in the form that sums to exactly 1."""
    p1 = p2 = 0
    for r, _ in addable_corners(lam):
        prod_r, m = shift_product(lam, r)
        p1 += Q ** r * prod_r
        p2 += Q ** m * prod_r
    return cancel(p1) == 1, cancel(p2) == 1


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

    print("\n(P) splits into two one-variable identities (facts 4-6)")
    split_shapes = shapes + [(4, 2, 1), (3, 3, 2), (4, 3, 1, 1)]
    for lam in split_shapes:
        x_free, p1, p2, hooks_one, cs = check_split(lam)
        c1, c2 = check_clean(lam)
        ok_all &= x_free and p1 and p2 and hooks_one and c1 and c2
        print(f"  lam={lam!s:<12} X-linear={x_free}  new-box hook=1: {hooks_one}  "
              f"(P1)={p1} (P2)={p2}  clean: {c1}/{c2}  contents={cs}")

    print("\n(P2) is (P1) at the conjugate — fact 7. Self-conjugate shapes are NOT evidence.")
    informative = 0
    for lam in split_shapes:
        same, self_conj, lam_c = check_conjugation(lam)
        ok_all &= same
        informative += 0 if self_conj else 1
        tag = "self-conjugate, trivial" if self_conj else "INFORMATIVE"
        print(f"  lam={lam!s:<12} lam'={lam_c!s:<14} (P2)[lam]==(P1)[lam']: {same}   {tag}")
    print(f"  -> {informative} of {len(split_shapes)} shapes carry information; the rest are self-conjugate.")

    print("\n(P) at Q -> 1 IS the SYT branching rule (F) — fact 8.")
    for lam in split_shapes:
        id_q1, branching = check_q1_is_branching(lam)
        ok_all &= id_q1 and branching
        print(f"  lam={lam!s:<12} identity at q=1: {id_q1}   branching rule: {branching}")
    print("  -> (F) is the q->1 shadow of (P), not an independent input.")

    print("\nall exact:", ok_all)
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
