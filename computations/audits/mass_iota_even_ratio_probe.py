"""Pre-registered Test B (audit 2026-11-21 alpha-em, section 24).

R = |E(beta_p)| / |E(beta_e)|, E = iota-even part of tr_M under convention D:
E = y21*chi21 + (y3/2)*(chi3 + chi111), y3 = (q^4+1)/(q^2+1)^2, y21 = q^2/(q^2+1)^2.
beta_e = s0 s1 s0, beta_p = (s0 s1^-1)^3. Proton q0, mpmath only (no float).
Compared to m_p/m_e = 1836.15267343 (CODATA 2022). Pass: within 1 %.
"""
import sys
from mpmath import mp, mpf, matrix, nstr
from qou_substrate.constants import MASS_RATIO_P_E_STR, q_at

mp.dps = 70
q = q_at(70)
qi = 1 / q
G = {(0, True): matrix([[q, 1], [0, -qi]]), (1, True): matrix([[-qi, 0], [1, q]]),
     (0, False): matrix([[qi, 1], [0, -q]]), (1, False): matrix([[-q, 0], [1, qi]])}


def chars(word):
    e = sum(1 if b else -1 for _, b in word)
    M = matrix([[1, 0], [0, 1]])
    for l in word:
        M = M * G[l]
    return q ** e, M[0, 0] + M[1, 1], (-qi) ** e


y3 = (q**4 + 1) / (q**2 + 1) ** 2
y21 = q**2 / (q**2 + 1) ** 2


def E(word):
    c3, c21, c111 = chars(word)
    return y21 * c21 + y3 / 2 * (c3 + c111)


def O(word):
    c3, _, c111 = chars(word)
    return y3 / 2 * (c3 - c111)


be = [(0, True), (1, True), (0, True)]
bp = [(0, True), (1, False)] * 3
target = mpf(MASS_RATIO_P_E_STR)  # CODATA 2022 m_p/m_e, read rather than typed (#9104)
R = abs(E(bp)) / abs(E(be))
print("q0      ", nstr(q, 20))
print("E(e)    ", nstr(E(be), 20), " O(e)", nstr(O(be), 20))
print("E(p)    ", nstr(E(bp), 20), " O(p)", nstr(O(bp), 20))
flip = [(i, not b) for i, b in be]
print("E(Ce)   ", nstr(E(flip), 20), "(Test A: expect -E(e))")
print("R       ", nstr(R, 20))
print("R/target", nstr(R / target, 20))
ok = abs(R / target - 1) < mpf("0.01")
print("Test B:", "PASS" if ok else "FAIL (scope-(a) negative)")
assert abs(E(flip) + E(be)) < mpf(10) ** -60, "Test A Lean result not reproduced"
sys.exit(0)
