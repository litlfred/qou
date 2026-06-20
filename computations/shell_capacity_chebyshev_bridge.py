#!/usr/bin/env python3
"""
Shell capacity 2n² from the bar-parity (cosh/sinh) split of ONE sl(2,ℂ) element
— formalize-first verification (no second compact SU(2)).

Owner correction: the n² orbital degeneracy does NOT need a second compact
SU(2) (Runge–Lenz). The cosh (bar-even) and sinh (bar-odd) parts are the two
real forms of a single sl(2,ℂ) = the complex volume 𝔙 (bar-parity-split.md).
This script verifies the chain that reduces 2n² to ONE self-square step, with
everything else an exact q-identity:

  (I)   radial (non-compact, sinh):  (T_γe^n)_{21} — the σ-tower shell entry,
        the bar-ODD partner. NB this is the det(T)=−1 recurrence
        p_n = (q-q⁻¹)p_{n-1} + p_{n-2}, NOT the standard Chebyshev
        U_{n-1}((q-q⁻¹)/2) (det +1, minus sign): exact check below REFUTES
        the equality for n ≥ 3 (e.g. (T³)₂₁ = q²−1+q⁻² ≠ U_2(sinh)=q²−3+q⁻²),
        correcting shell-structure-eigenvalues.md. The radial side carries the
        shell INDEX n / the energy ladder, NOT the degeneracy.
  (II)  angular (compact, cosh):     [n]_q = U_{n-1}((q+q⁻¹)/2)
        — the SAME U_{n-1}, at the bar-EVEN argument (q+q⁻¹)/2 = cosh λ, is the
        q-dimension / character of the n-dim SU(2)_q irrep V_{(n-1)/2}.
        (I) and (II) are the two bar-parities (sinh/cosh) of one element ⇒ the
        𝔙 = cosh + i·sinh unification; the angular and radial structures are
        two evaluations of ONE Chebyshev element, not two groups.
  (III) self-square (the n²):        [n]_q² = Σ_{ℓ=0}^{n-1} [2ℓ+1]_q
        — the q-Clebsch–Gordan dim_q(V_{(n-1)/2} ⊗ V_{(n-1)/2}); at q=1 this is
        n² = Σ_{ℓ=0}^{n-1}(2ℓ+1) = 1+3+…+(2n-1).
  (IV)  capacity:  2[n]_q²|_{q=1} = 2n² = 2, 8, 18, 32, …

PROVEN here (exact symbolic): II, III, IV.
REFUTED/corrected: I — (T^n)₂₁ ≠ U_{n-1}((q-q⁻¹)/2) for n ≥ 3 (det(T)=−1
recurrence); the degeneracy does NOT come from the radial side anyway.
CONJECTURAL (the single remaining physics step): that the shell state space IS
the self-tensor-square [n]_q² of the angular (cosh-parity) shell element — the
"(j,j) doubling" realized as the square of ONE 𝔙-element, NOT a second SU(2).
This replaces the SO(4)/Runge–Lenz input with a self-square of the single
sl(2,ℂ)/𝔙 element.

Refs: bar-parity-split.md, shell-structure-eigenvalues.md, transfer-matrix-operator.md.
"""
from __future__ import annotations

import sympy as sp

q = sp.symbols("q", positive=True)
NMAX = 8


def q_int(n):
    """q-integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return sp.simplify((q ** n - q ** (-n)) / (q - 1 / q))


def main() -> int:
    print("  SHELL CAPACITY 2n² FROM cosh/sinh BAR-PARITY OF ONE sl(2,ℂ) ELEMENT")
    print("  (formalize-first; exact sympy; no second compact SU(2))\n")

    T = sp.Matrix([[q - 1 / q, 1], [1, 0]])
    x_odd = (q - 1 / q) / 2     # sinh argument (bar-odd, radial)
    x_even = (q + 1 / q) / 2    # cosh argument (bar-even, angular)

    print("### Identities (✓ = proved exactly for n = 1..%d)\n" % NMAX)
    print("| n | (I) (T^n)₂₁ = U_{n-1}(sinh) | (II) [n]_q = U_{n-1}(cosh) | "
          "(III) [n]_q² = Σ[2ℓ+1]_q | 2[n]_q²|_{q=1}=2n² |")
    print("|--:|:--:|:--:|:--:|--:|")
    okI = okII = okIII = True
    for n in range(1, NMAX + 1):
        Tn = T ** n
        radial = sp.simplify(Tn[1, 0])                       # (T^n)_{21}
        U_odd = sp.simplify(sp.chebyshevu(n - 1, x_odd))
        i1 = sp.simplify(radial - U_odd) == 0

        qn = q_int(n)
        U_even = sp.simplify(sp.chebyshevu(n - 1, x_even))
        i2 = sp.simplify(qn - U_even) == 0

        lhs = sp.expand(sp.simplify(qn ** 2))
        rhs = sp.expand(sp.simplify(sum(q_int(2 * l + 1) for l in range(n))))
        i3 = sp.simplify(lhs - rhs) == 0

        cap = sp.simplify(2 * qn ** 2)
        cap1 = sp.limit(cap, q, 1)

        okI &= i1; okII &= i2; okIII &= i3
        print(f"| {n} | {'✓' if i1 else '✗'} | {'✓' if i2 else '✗'} | "
              f"{'✓' if i3 else '✗'} | {cap1} |")

    print()
    print(f"  (I)   radial = U_{{n-1}}(sinh-arg)  [bar-odd]   all ✓: {okI}")
    print(f"  (II)  [n]_q  = U_{{n-1}}(cosh-arg)  [bar-even]  all ✓: {okII}")
    print(f"  (III) [n]_q² = Σ_{{ℓ=0}}^{{n-1}}[2ℓ+1]_q  (q-Clebsch–Gordan) all ✓: {okIII}")
    print()

    # The bar-parity unification, explicit: (I) and (II) are the SAME U_{n-1}
    # on the odd vs even argument — the cosh/sinh split of one element.
    print("### The unification (one element, two parities) — n = 3 sample")
    n = 3
    print(f"  shell element  U_{{{n-1}}}(x)            = {sp.expand(sp.chebyshevu(n-1, sp.Symbol('x')))}")
    print(f"  bar-EVEN (cosh) → angular  [{n}]_q       = {sp.expand(q_int(n))}   (= dim_q of the {n}-dim SU(2)_q irrep)")
    print(f"  bar-ODD  (sinh) → radial  (T^{n})₂₁       = {sp.expand(sp.simplify((T**n)[1,0]))}")
    print(f"  n² decomposition  [{n}]_q² = "
          f"{' + '.join('['+str(2*l+1)+']_q' for l in range(n))}  "
          f"→ at q=1: {sp.limit(q_int(n)**2, q, 1)} = " +
          " + ".join(str(2*l+1) for l in range(n)))
    print()

    print("### Reading")
    print("  • The shell-n object is ONE Chebyshev element U_{n-1}. Its bar-EVEN")
    print("    (cosh) evaluation is the angular q-dimension [n]_q (the n-dim SU(2)_q")
    print("    irrep); its bar-ODD (sinh) evaluation is the radial σ-tower entry.")
    print("    Angular + radial = two parities of ONE element (the 𝔙 = cosh+i·sinh")
    print("    unification) — NOT two compact SU(2)s.")
    print("  • 2n² = 2[n]_q²|_{q=1}, and [n]_q² = Σ_{ℓ=0}^{n-1}[2ℓ+1]_q is the")
    print("    EXACT q-Clebsch–Gordan self-square (the (j,j) doubling).")
    print("  • PROVEN: II, III, IV (I refuted: radial ≠ Chebyshev-U, det T=−1).")
    print("    CONJECTURAL (single step): that the shell state space IS the")
    print("    self-square [n]_q² of the angular shell")
    print("    element — the doubling internal to the one sl(2,ℂ)/𝔙, replacing the")
    print("    SO(4)/Runge–Lenz input. No second compact SU(2) is needed.")
    print("  • SEPARATE (Gap 2): the Madelung/noble-gas ORDERING still needs the")
    print("    T_ee screening many-body step (pure-2n² closes at 2,10,28,60).")
    return 0 if (okI and okII and okIII) else 1


if __name__ == "__main__":
    raise SystemExit(main())
