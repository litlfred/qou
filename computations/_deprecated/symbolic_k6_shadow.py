#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Symbolic k=6 shadow prices — all in q.

Extends branching-lp.py to H₆(q): builds seminormal matrices for
all 11 partitions of 6, computes nuclear braid characters
SYMBOLICALLY in q, and extracts the LP dual shadow prices.

The BW coefficient for partition λ ⊢ 6 is the shadow price y_λ(q)
of the Frobenius positivity constraint ⟨Φ, π_λ⟩_F ≥ 0 in the
nuclear operator selection LP (prop:bw-coefficient-shadow-price).

Architecture:
  1. Build seminormal σ₁,...,σ₅ for each λ ⊢ 6 (symbolic in q)
  2. For A nucleons, multiply crossing matrices → Φ_λ(q)
  3. Markov trace: M(q) = Σ w_λ(q) · tr(Φ_λ)/dim(λ)
  4. Shadow prices from the LP dual cone structure

Usage:
    cd computations && python3 symbolic_k6_shadow.py
"""

import sympy as sp
from sympy import cancel, factor, simplify, sqrt, Rational
from sympy import Matrix, eye, zeros
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0_num

q = sp.Symbol('q', positive=True)
qi = 1/q
h = q - qi

def qint(n):
    """Symbolic q-integer [n]_q = (q^n - q^{-n})/(q - q^{-1})."""
    if n == 0:
        return sp.Integer(0)
    if n == 1:
        return sp.Integer(1)
    return cancel((q**n - q**(-n)) / (q - qi))

def qfac(n):
    """Symbolic [n]_q! = [1][2]...[n]."""
    result = sp.Integer(1)
    for k in range(1, n+1):
        result *= qint(k)
    return cancel(result)


# ══════════════════════════════════════════════════════════════
# §1  STANDARD YOUNG TABLEAUX
# ══════════════════════════════════════════════════════════════

def partitions_of(n):
    if n == 0: yield (); return
    def g(n, mx):
        if n == 0: yield (); return
        for i in range(min(n,mx), 0, -1):
            for r in g(n-i, i): yield (i,)+r
    yield from g(n, n)

def young_cells(shape):
    """(row, col) cells of the Young diagram."""
    cells = []
    for i, ri in enumerate(shape):
        for j in range(ri):
            cells.append((i, j))
    return cells

def content(cell):
    return cell[1] - cell[0]

def young_hooks(shape):
    rows = list(shape)
    max_col = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(max_col)]
    hooks = []
    for i in range(len(rows)):
        for j in range(rows[i]):
            hooks.append((rows[i]-j-1) + (cols[j]-i-1) + 1)
    return hooks

def dim_q_symbolic(shape):
    n = sum(shape)
    return cancel(qfac(n) / sp.prod([qint(hk) for hk in young_hooks(shape)]))

def standard_young_tableaux(shape):
    """Generate all SYT. Returns list of dicts {entry → cell_index}."""
    n = sum(shape)
    cells = young_cells(shape)
    nc = len(cells)

    results = []
    def _fill(entry, filled, avail):
        if entry > n:
            results.append(dict(filled))
            return
        for ci in range(nc):
            if not avail[ci]: continue
            r, c = cells[ci]
            # left neighbor must be filled
            if c > 0:
                left = next((k for k, (rr,cc) in enumerate(cells) if rr==r and cc==c-1), None)
                if left is not None and avail[left]: continue
            # above neighbor must be filled
            if r > 0:
                above = next((k for k, (rr,cc) in enumerate(cells) if rr==r-1 and cc==c), None)
                if above is not None and avail[above]: continue
            filled[entry] = ci
            avail[ci] = False
            _fill(entry+1, filled, avail)
            del filled[entry]
            avail[ci] = True
    _fill(1, {}, [True]*nc)
    return results, cells


# ══════════════════════════════════════════════════════════════
# §2  SYMBOLIC SEMINORMAL MATRICES
# ══════════════════════════════════════════════════════════════

def build_seminormal_symbolic(shape):
    """Build σ₁,...,σ_{n-1} in seminormal basis, symbolic in q.

    Returns: list of sympy Matrices, dim, syts
    """
    n = sum(shape)
    syts, cells = standard_young_tableaux(shape)
    contents = [content(c) for c in cells]
    dim = len(syts)

    if dim == 0:
        return [], dim, syts

    sigmas = []
    for k in range(1, n):  # σ_k swaps entries k and k+1
        M = zeros(dim, dim)
        processed = set()

        for i in range(dim):
            if i in processed: continue

            ci_k = syts[i][k]
            ci_k1 = syts[i][k+1]
            rho = contents[ci_k1] - contents[ci_k]

            # a_ρ = h/(1 - q^{-2ρ})
            a = cancel(h / (1 - q**(-2*rho)))

            # Find swap partner
            swap = dict(syts[i])
            swap[k] = ci_k1
            swap[k+1] = ci_k

            j = None
            for jj in range(dim):
                if jj != i and syts[jj] == swap:
                    j = jj
                    break

            if j is None:
                # 1×1 block
                M[i, i] = a
                processed.add(i)
            else:
                # 2×2 block
                a_prime = cancel(h / (1 - q**(2*rho)))
                b_sq = cancel(a * a_prime + 1)
                b = sp.sqrt(b_sq)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)

        sigmas.append(M)

    return sigmas, dim, syts


# ══════════════════════════════════════════════════════════════
# §3  NUCLEAR BRAID CHARACTER (symbolic in q)
# ══════════════════════════════════════════════════════════════

def crossing_coeffs_symbolic(ti, tj):
    """Crossing (c, d) for nucleon types: 1=proton, 0=neutron. Symbolic."""
    if ti == 1 and tj == 1:
        return sp.Integer(1), sp.Integer(0)       # pp: σ
    elif ti == 0 and tj == 0:
        return sp.Integer(1), -h                    # nn: σ⁻¹
    else:
        return sp.Integer(1), -h/2                  # pn: mixed


def nuclear_character_symbolic(Z, N, sigmas, dim, n_gens):
    """Compute χ_λ(nuclear braid) symbolically in q."""
    A = Z + N
    if A <= 1 or dim == 0:
        return sp.Integer(dim)

    # Ground state ordering: interleaved p, n
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append(1); pc += 1
        else:
            ordering.append(0); nc += 1

    I = eye(dim)
    product = eye(dim)

    for i in range(A-1):
        for j in range(i+1, A):
            c, d = crossing_coeffs_symbolic(ordering[i], ordering[j])
            g = (i + j) % n_gens
            M = c * sigmas[g] + d * I
            product = product * M

    return cancel(product.trace())


# ══════════════════════════════════════════════════════════════
# §4  WEDDERBURN-ARTIN WEIGHTS AND SHADOW PRICES
# ══════════════════════════════════════════════════════════════

def content_sum(shape):
    return sum(j - i for i, ri in enumerate(shape) for j in range(ri))

def conjugate(shape):
    if not shape: return ()
    return tuple(sum(1 for r in shape if r >= c+1) for c in range(shape[0]))

def is_self_conjugate(shape):
    return shape == conjugate(shape)


# ══════════════════════════════════════════════════════════════
# §5  MAIN: build everything symbolic, evaluate at q₀
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import time

    k = 6
    n_gens = k - 1  # 5 generators
    nfac = qfac(k)

    print("="*70)
    print(f"SYMBOLIC k={k} SHADOW PRICES — all in q")
    print("="*70)

    # ── Build seminormal matrices for all partitions ──────────
    print(f"\nBuilding seminormal matrices for partitions of {k}...")
    partition_data = {}

    for shape in partitions_of(k):
        t0 = time.time()
        sigmas, dim, syts = build_seminormal_symbolic(shape)
        dt = time.time() - t0

        dq = dim_q_symbolic(shape)
        w = cancel(dq**2 / nfac)
        cs = content_sum(shape)
        sc = is_self_conjugate(shape)

        partition_data[shape] = {
            'sigmas': sigmas, 'dim': dim, 'syts': syts,
            'dim_q': dq, 'w': w, 'cs': cs, 'sc': sc,
        }

        # Verify Hecke relation symbolically: σ₁² = h·σ₁ + I
        if dim > 0 and len(sigmas) > 0:
            check = sigmas[0]*sigmas[0] - h*sigmas[0] - eye(dim)
            check_ok = all(cancel(check[i,j]) == 0 for i in range(dim) for j in range(dim))
            status = "✓" if check_ok else "✗"
        else:
            status = "—"

        dq_num = float(dq.subs(q, q0_num))
        print(f"  {str(shape):>20} dim={dim:>3} dim_q={dq_num:>8.3f} "
              f"c={cs:>+3} {'SC' if sc else '  '} Hecke:{status} ({dt:.1f}s)")

    # ── Compute nuclear characters for small nuclei ───────────
    print(f"\n{'='*70}")
    print("NUCLEAR CHARACTERS χ_λ(q) for small nuclei")
    print(f"{'='*70}")

    test_nuclei = [
        ('D',  1, 1),  # deuterium: 1 crossing
        ('3H', 1, 2),  # tritium: 3 crossings
        ('3He',2, 1),  # helium-3: 3 crossings
        ('4He',2, 2),  # helium-4: 6 crossings
    ]

    for name, Z, N in test_nuclei:
        A = Z + N
        print(f"\n  {name} (Z={Z}, N={N}, A={A}, {A*(A-1)//2} crossings)")

        for shape in partitions_of(k):
            pd = partition_data[shape]
            if pd['dim'] == 0: continue

            t0 = time.time()
            chi = nuclear_character_symbolic(Z, N, pd['sigmas'], pd['dim'], n_gens)
            dt = time.time() - t0

            chi_num = complex(chi.subs(q, q0_num))
            chi_str = str(factor(chi))
            if len(chi_str) > 80:
                chi_str = chi_str[:77] + "..."

            print(f"    {str(shape):>20} χ = {chi_str}")
            print(f"    {'':>20} χ(q₀) = {chi_num.real:+.6f}  ({dt:.1f}s)")

    # ── Shadow prices from Frobenius cone ─────────────────────
    print(f"\n{'='*70}")
    print("SHADOW PRICES y_λ(q) = (w_λ/d_λ − y₀)")
    print(f"{'='*70}")

    # y₀ = min_λ (w_λ/d_λ) = w_{(6)}/1 = 1/[6]!
    y0 = cancel(sp.Integer(1) / nfac)
    print(f"\n  y₀ = 1/[6]! = {y0}")
    print(f"  y₀(q₀) = {float(y0.subs(q, q0_num)):.10f}")

    print(f"\n  {'Partition':>20} {'w_λ/d_λ':>30} {'y_λ':>40} {'y_λ(q₀)':>12}")
    print(f"  {'-'*105}")

    for shape in partitions_of(k):
        pd = partition_data[shape]
        if pd['dim'] == 0: continue
        d = pd['dim']
        w_over_d = cancel(pd['w'] / d)
        y_lam = cancel(w_over_d - y0)
        y_num = float(y_lam.subs(q, q0_num))

        w_str = str(factor(w_over_d))[:30]
        y_str = str(factor(y_lam))[:40]

        tag = ""
        if shape == (3,2,1): tag = " ◀ WIGNER-2"
        print(f"  {str(shape):>20} {w_str:>30} {y_str:>40} {y_num:>12.8f}{tag}")

    # ── Per-nucleon Garside trace in each channel ─────────────
    # For a SINGLE nucleon (proton or neutron), compute
    # tr(crossing product) / dim for each partition.
    # This is the per-nucleon "channel weight" G_{type}(λ).
    print(f"\n{'='*70}")
    print("PER-NUCLEON GARSIDE TRACE: tr(crossings)/dim for single nucleon")
    print(f"{'='*70}")

    # A single proton has crossings: B₃ confinement (σ₀σ₁⁻¹)³ + quark crossings
    # But in H₆ representation, σ₀ → σ₁ (gen index 0 → sigmas[0])
    # σ₁⁻¹ = σ₁ - h·I (from Hecke relation σ² = hσ + I → σ⁻¹ = σ - h)

    # For the simple LP dual, we just need the generator traces
    print("\n  Generator traces tr(σ_g)/dim for each partition:")
    print(f"  {'Partition':>20}", end="")
    for g in range(n_gens):
        print(f"  {'σ_'+str(g+1):>10}", end="")
    print()

    for shape in partitions_of(k):
        pd = partition_data[shape]
        if pd['dim'] == 0: continue
        d = pd['dim']
        print(f"  {str(shape):>20}", end="")
        for g in range(n_gens):
            tr_g = cancel(pd['sigmas'][g].trace() / d)
            tr_num = float(tr_g.subs(q, q0_num))
            print(f"  {tr_num:>+10.5f}", end="")
        print()

    print(f"\n  Symbolic generator traces for [3,2,1]:")
    pd321 = partition_data[(3,2,1)]
    for g in range(n_gens):
        tr_g = cancel(pd321['sigmas'][g].trace())
        tr_factored = factor(tr_g)
        print(f"    tr(σ_{g+1}) = {tr_factored}")

    print("\nDone.")
