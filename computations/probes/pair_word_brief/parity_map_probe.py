#!/usr/bin/env python3
"""Which map is parity? Exact checks on H_3(q) and on the Jimbo representation.

Bean qou-99qc, 2026-11-21, owner: "Settle which map is parity".
Companion to QOU/QBeta/ParityMapCandidates.lean. Exact arithmetic in Q(q) (sympy);
no float anywhere, no witness written (the result is recorded in the brief).

The photon is gamma(phi) = 1 + phi0*s0 + phi1*s1 + phi01*s0*s1^{-1} (owner ruling).

Maps compared (a = s0, b = s1, h = q - 1/q):
  iota  : s -> h - s  (= -s^{-1}),  q fixed, algebra automorphism
  bar   : s -> s^{-1}, q -> 1/q      (semilinear automorphism)
  rev   : reverse words, signs kept   (corpus "T", conj:t-from-trace-cyclicity)
  delta : s0 <-> s1                   (inner: conjugation by the half twist)
  inv   : group inverse = bar o rev   (corpus "P.T")

Checks (all assert-based; exit 0 means every check passed):
  1. Regular representation of H_3 in the basis 1,a,b,ab,ba,aba; Hecke + braid.
  2. Convention-D Ocneanu trace values; tr o rev = tr, tr o delta = tr on the basis.
  3. tr o iota != tr (Markov parameter z_D -> h - z_D); tr_q(bar x) = tr_{1/q}(x).
  4. V-bar^3 is conjugate to V^3 (conjugator ba): equal trace for every trace.
  5. rev, inv, delta do not keep V in span{1,a,b,ab} (the photon span); iota, bar do.
  6. Jimbo 8x8: Hecke, braid, TL relation E0E1E0 = E0 (E = q - s), the highest-weight
     vector |000> has eigenvalue q, and F0F1F0 != F0 (F = s + 1/q = iota(E)). So no
     algebra map of the Jimbo image extends iota.
  7. Jimbo 4x4: R(1/q) = X R(q)^{-1} X with X the spin flip on both sites (u <-> d):
     bar on the Jimbo representation is q -> 1/q composed with the u<->d flip.
"""
import sys
import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
zD = q**3 / (q**2 + 1)

CHECKS = []


def check(name, cond):
    ok = bool(cond)
    CHECKS.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name)


def simp0(M):
    return sp.simplify(M) == sp.zeros(*M.shape)


# ---------------------------------------------------------------- 1. regular rep of H_3
# basis order: 1, a, b, ab, ba, aba
def left_a():
    M = sp.zeros(6, 6)
    # a*1=a ; a*a=h a+1 ; a*b=ab ; a*ab=h ab+b ; a*ba=aba ; a*aba=h aba+ba
    cols = [
        {1: 1}, {1: h, 0: 1}, {3: 1}, {3: h, 2: 1}, {5: 1}, {5: h, 4: 1},
    ]
    for j, c in enumerate(cols):
        for i, v in c.items():
            M[i, j] = v
    return M


def left_b():
    M = sp.zeros(6, 6)
    # b*1=b ; b*a=ba ; b*b=h b+1 ; b*ab=bab=aba ; b*ba=h ba+a ; b*aba=h aba+ab
    cols = [
        {2: 1}, {4: 1}, {2: h, 0: 1}, {5: 1}, {4: h, 1: 1}, {5: h, 3: 1},
    ]
    for j, c in enumerate(cols):
        for i, v in c.items():
            M[i, j] = v
    return M


A, B = left_a(), left_b()
I6 = sp.eye(6)
check("H3 regular rep: a^2 = h a + 1", simp0(A * A - h * A - I6))
check("H3 regular rep: b^2 = h b + 1", simp0(B * B - h * B - I6))
check("H3 regular rep: aba = bab", simp0(A * B * A - B * A * B))


def vec(M):
    """Element of H_3 represented by its left-multiplication matrix -> coordinates."""
    return sp.simplify(M[:, 0])


def from_coords(c):
    basis = [I6, A, B, A * B, B * A, A * B * A]
    M = sp.zeros(6, 6)
    for k in range(6):
        M += c[k] * basis[k]
    return M


# ---------------------------------------------------------------- 2. trace
def tr_vals(z, hh):
    return [1, z, z, z**2, z**2, z * (hh * z + 1)]


def tr(M, z=zD, hh=h):
    c = vec(M)
    t = tr_vals(z, hh)
    return sp.simplify(sum(c[k] * t[k] for k in range(6)))


# trace property: tr(xy) = tr(yx) on generators of the basis
basis = [I6, A, B, A * B, B * A, A * B * A]
cyc = all(sp.simplify(tr(X * Y) - tr(Y * X)) == 0 for X in basis for Y in basis)
check("convention-D trace is a trace (tr(xy)=tr(yx) on all 36 basis pairs)", cyc)
check("Markov at z_D: tr(x b) = z_D tr(x) for x in span{1,a}",
      all(sp.simplify(tr(X * B) - zD * tr(X)) == 0 for X in [I6, A]))


# the maps, as images of basis elements (coordinates computed by matrix algebra)
def iota_elem(c):
    ia, ib = h * I6 - A, h * I6 - B
    imgs = [I6, ia, ib, ia * ib, ib * ia, ia * ib * ia]
    return sum((c[k] * imgs[k] for k in range(6)), sp.zeros(6, 6))


def rev_coords(c):  # 1,a,b,ab,ba,aba -> 1,a,b,ba,ab,aba
    return [c[0], c[1], c[2], c[4], c[3], c[5]]


def delta_coords(c):  # a<->b ; ab->ba ; ba->ab ; aba->bab=aba
    return [c[0], c[2], c[1], c[4], c[3], c[5]]


rev_ok = all(sp.simplify(tr(from_coords(rev_coords(vec(X)))) - tr(X)) == 0 for X in basis)
check("tr o rev = tr on the basis (corpus T is trace-preserving)", rev_ok)
delta_ok = all(sp.simplify(tr(from_coords(delta_coords(vec(X)))) - tr(X)) == 0 for X in basis)
check("tr o delta = tr on the basis (delta inner)", delta_ok)

# ---------------------------------------------------------------- 3. iota and bar vs trace
tr_iota_a = tr(iota_elem(vec(A)))
check("tr_D(iota a) = h - z_D", sp.simplify(tr_iota_a - (h - zD)) == 0)
check("h - z_D = -z_D(1/q)", sp.simplify((h - zD) + zD.subs(q, 1 / q)) == 0)
check("tr_D(iota a) != tr_D(a)  (iota is not a symmetry of the D trace)",
      sp.simplify(tr_iota_a - zD) != 0)
# iota-invariant Markov parameter would be z = h/2
check("z = h/2 is the iota-fixed Markov parameter, != z_D",
      sp.simplify(h / 2 - zD) != 0)
# bar: tr_q(s^{-1}) = z_D - h  equals  tr_{1/q}(s) = z_D(1/q)
check("bar covariance: z_D(q) - h(q) = z_D(1/q)",
      sp.simplify(zD - h - zD.subs(q, 1 / q)) == 0)
# full basis: tr_q(bar x) = tr_{1/q}(x), with bar x computed as the word with inverse letters
Ai, Bi = A - h * I6, B - h * I6
bar_imgs = [I6, Ai, Bi, Ai * Bi, Bi * Ai, Ai * Bi * Ai]
bar_ok = True
tvals_inv = [sp.simplify(sp.sympify(t).subs(q, 1 / q)) for t in tr_vals(zD, h)]
for k in range(6):
    if sp.simplify(tr(bar_imgs[k]) - tvals_inv[k]) != 0:
        bar_ok = False
check("tr_{D,q}(bar T_w) = tr_{D,1/q}(T_w) for all six basis words (Jones mirror)", bar_ok)

# ---------------------------------------------------------------- 4. conjugacy of V^3, Vbar^3
V = A * (B - h * I6)
Vb = (A - h * I6) * B
g = B * A
ginv = (A - h * I6) * (B - h * I6)  # (ba)^{-1} = a^{-1} b^{-1}
check("(ba)(ba)^{-1} = 1", simp0(g * ginv - I6))
check("Vbar = (ba) V (ba)^{-1}", simp0(g * V * ginv - Vb))
check("Vbar^3 = (ba) V^3 (ba)^{-1}", simp0(g * V**3 * ginv - Vb**3))
check("tr_D(Vbar^3) = tr_D(V^3)", sp.simplify(tr(Vb**3) - tr(V**3)) == 0)
# mixed word is NOT conjugate-equivalent at trace level (different (2,1) content is in the
# brief; here only the D-trace, which may or may not separate them)
print("  tr_D(V^3)      =", sp.factor(tr(V**3)))
print("  tr_D(V V Vbar) =", sp.factor(tr(V * V * Vb)))

# ---------------------------------------------------------------- 5. photon span
def in_photon_span(M):
    c = vec(M)
    return sp.simplify(c[4]) == 0 and sp.simplify(c[5]) == 0


check("V in span{1,a,b,ab}", in_photon_span(V))
check("iota(V) = Vbar in span{1,a,b,ab}", in_photon_span(iota_elem(vec(V))))
check("bar(V) = a^{-1} b in span{1,a,b,ab}", in_photon_span(Vb))
check("rev(V) = b^{-1} a NOT in span{1,a,b,ab}",
      not in_photon_span(from_coords(rev_coords(vec(V)))))
check("inv(V) = b a^{-1} NOT in span{1,a,b,ab}", not in_photon_span(B * (A - h * I6)))
check("delta(V) = b a^{-1} NOT in span{1,a,b,ab}",
      not in_photon_span(from_coords(delta_coords(vec(V)))))

# ---------------------------------------------------------------- 6. Jimbo 8x8
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
I2 = sp.eye(2)
S0 = sp.kronecker_product(R, I2)
S1 = sp.kronecker_product(I2, R)
I8 = sp.eye(8)
check("Jimbo: s0^2 = h s0 + 1", simp0(S0 * S0 - h * S0 - I8))
check("Jimbo: s1^2 = h s1 + 1", simp0(S1 * S1 - h * S1 - I8))
check("Jimbo: braid", simp0(S0 * S1 * S0 - S1 * S0 * S1))
E0, E1 = q * I8 - S0, q * I8 - S1
F0, F1 = S0 + I8 / q, S1 + I8 / q
check("Jimbo: TL relation E0 E1 E0 = E0", simp0(E0 * E1 * E0 - E0))
check("iota(E) = F (q - (h - s) = s + 1/q)", sp.simplify(q - (h - q) - (q + 1 / q)) == 0)
v = sp.zeros(8, 1)
v[0] = 1
check("Jimbo: s0 |000> = q |000>", simp0(S0 * v - q * v))
check("Jimbo: s1 |000> = q |000>", simp0(S1 * v - q * v))
check("Jimbo: F0 F1 F0 != F0 (so iota does not descend)", not simp0(F0 * F1 * F0 - F0))

# ---------------------------------------------------------------- 7. bar on Jimbo
X = sp.Matrix([[0, 1], [1, 0]])
XX = sp.kronecker_product(X, X)
Rinv = sp.simplify(R.inv())
check("R(1/q) = (X x X) R(q)^{-1} (X x X)  [bar = q->1/q with the u<->d flip]",
      simp0(R.subs(q, 1 / q) - XX * Rinv * XX))
check("R(1/q) != R(q)^{-1} (the flip is needed)", not simp0(R.subs(q, 1 / q) - Rinv))

nfail = sum(1 for _, ok in CHECKS if not ok)
print(f"\n{len(CHECKS) - nfail}/{len(CHECKS)} checks passed")
sys.exit(1 if nfail else 0)
