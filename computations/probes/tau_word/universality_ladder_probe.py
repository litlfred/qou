"""Lepton-universality ladder Delta^(2k+1) on the ring mass (exact in Q(q); no fitting).

Thread "Derive the tau lepton's word" (2026-11-27). Lean:
QOU/Observations/LeptonUniversalityLadder.lean. Audit: docs/audits/2026-11-27-tau-lepton-word.md.

Checks, exactly in sympy over Q(q):
  * rho(Delta) = [[0,-1],[-1,0]] in the 2-dim Hecke representation of the ring-mass probe;
  * the ring mass of Delta^(2k+1) is [4]/q^3 * q^(-6k) for k = 0..4;
  * the closure of Delta^(2k+1) has two components; the sublink on strands {0,2} is the
    2-strand braid sigma^(2k+1) (torus knot T(2,2k+1)); linking number 2k+1;
  * Seifert genus of the positive closure: g = 3k (chi = 3 - 3(2k+1), two components).
Then, only as a comparison printed after the checks, the q0 values (no measured mass enters a
check).
"""
import sys
import sympy as sp

q = sp.symbols("q", positive=True)
A = sp.Matrix([[q, 1], [0, -1 / q]])
B = sp.Matrix([[-1 / q, 0], [1, q]])
checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


D = sp.simplify(A * B * A)
check("rho(Delta) = [[0,-1],[-1,0]]", D == sp.Matrix([[0, -1], [-1, 0]]))
check("braid relation ABA = BAB", sp.simplify(A * B * A - B * A * B) == sp.zeros(2))

s2 = (q + 1 / q) ** 2
q4 = q**3 + q + 1 / q + q**-3


def ring_mass_word(M, w):
    tr = (1 - 2 / s2) * q**w + M.trace() / s2
    return (q + 1 / q) ** 3 * q ** (-2 * w) * tr


for k in range(5):
    n = 2 * k + 1
    m = ring_mass_word(D**n, 3 * n)
    check(f"m(Delta^{n}) = [4]/q^3 * q^-{6*k}", sp.simplify(m - q4 / q**3 * q ** (-6 * k)) == 0)


def perm(letters):
    p = [0, 1, 2]
    for i in letters:
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


for k in range(3):
    letters = [0, 1, 0] * (2 * k + 1)
    p = perm(letters)
    seen, comps = set(), 0
    for s in range(3):
        if s not in seen:
            comps += 1
            x = s
            while x not in seen:
                seen.add(x)
                x = p[x]
    check(f"Delta^{2*k+1} closes to 2 components", comps == 2)
    # strand tracking: count crossings between the {0,2} component and strand-1 component
    pos = [0, 1, 2]  # pos[slot] = strand label
    lab = {}
    cross_AB = 0
    cross_AA = 0
    for i in letters:
        a, b = pos[i], pos[i + 1]
        compA = {0, 2}
        if (a in compA) != (b in compA):
            cross_AB += 1
        elif a in compA and b in compA:
            cross_AA += 1
        pos[i], pos[i + 1] = b, a
    check(f"Delta^{2*k+1}: lk = {2*k+1}", cross_AB // 2 == 2 * k + 1)
    check(f"Delta^{2*k+1}: sublink {{0,2}} is sigma^{2*k+1}", cross_AA == 2 * k + 1)
    chi = 3 - 3 * (2 * k + 1)
    g = (2 - chi - 2) // 2
    check(f"Delta^{2*k+1}: Seifert genus {3*k}", g == 3 * k)

print()
print("-- comparison only (q0 from the corpus pin) --")
sys.path.insert(0, "computations/substrate")
try:
    from q_parameter import Q_50_DIGIT_STR
    import mpmath as mp
    mp.mp.dps = 30
    q0 = mp.mpf(Q_50_DIGIT_STR)
    for k in range(3):
        print(f"k={k}: m/m_e = q0^-{6*k} = {mp.nstr(q0 ** (-6 * k), 12)}")
except Exception as exc:  # comparison is optional
    print("q0 not available:", exc)
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
