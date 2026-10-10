#!/usr/bin/env python3
"""Convention-D producer for cor:spectral-decomposition-qvalue (bean qou-wlnx).

Recomputes, in convention D (Markov parameter z = q^3/(q^2+1)) at the PROTON
pin q0, every number the spectral-decomposition-qvalue block family quotes:

  * Q_bare = |log_q(P_dau/P_par)| * hbar_q * m_e/3 for the six benchmark
    beta^- decays (3H, 14C, 60Co, 90Sr, 137Cs, 210Bi), with P(q) the
    inductive-chain Skein polynomial of part (i) of the corollary;
  * the H_3(q) Markov traces tr_M(tau(r,s) * T_beta), T_beta = s0 s1^{-1}
    (Table 1 of the block);
  * the Rosso--Jones invariants J(tau(2,9)), J(tau(3,4)) and F_deg2;
  * the Pauli case |tr_M(e_(1^3) tau T_beta e_(1^3))| / |tr_M(T_beta)|,
    which vanishes identically under D (the Ocneanu weight of (1^3) is 0);
  * the residuals of Q_bare and of the combined formula
    Q = Q_bare * F_deg2^[d>=2] * F_Pauli^[N magic] against NNDC/ENSDF.

It replaces, for these purposes, the float-only convention-C producer
computations/_deprecated/rosso-jones-qvalues.py.  That script is ported here,
not re-used: its crossing coefficients (pp: (1,0), nn: (1,-(q-q^-1)),
pn: (1,-(q-q^-1)/2)) are the ones published in prop:beta-decay-transfer-matrix
and are kept; its Markov parameter (convention C) and its float arithmetic are
not.

One discrepancy with the deprecated script is recorded rather than silently
resolved: the deprecated script computes Q_bare = |Delta ln P| * m_e/3 (its
E_cross * mu_0 = m_e/3), while the corollary as published reads
|log_q(...)| * hbar_q * m_e/3 = |Delta ln P| * (hbar_q/ln q) * m_e/3.  The two
differ by hbar_q/ln q ~ 0.9496.  This producer evaluates the PUBLISHED formula;
the other normalisation is emitted alongside it, labelled, so a reader can see
which one any historical figure used.

A labelled convention-C HISTORICAL comparison column is emitted only to
identify the provenance of the figures the block quoted until 2026-10-10
(Sr-90 Q_bare 0.944 MeV, F_Pauli 0.6382).  Nothing downstream consumes it.

No fitting: nothing here is tuned against the Q-value data.  Nucleon ordering
(protons first, then neutrons) is inherited from the deprecated producer and is
a structural choice the block itself lists as an error source.

Run:  PYTHONPATH=computations:tools/qou-substrate/python \
      python3 -u computations/spectral_decomposition_qvalue_d.py
"""

from __future__ import annotations

import itertools
import sys

import mpmath as mp

from qou_substrate.constants import q_at, _E_MEV
from qou_substrate.precision import fmt
from qou_substrate.witness import WitnessBuilder

DPS = 70
mp.mp.dps = DPS

Q0 = q_at(DPS)                     # proton pin (AGENTS.md q0 anchor convention)
QI = 1 / Q0
HA = Q0 - QI                       # q - q^{-1}
HBAR_Q = 1 - QI                    # hbar_q = (q-1)/q
LN_Q = mp.log(Q0)
M_E = mp.mpf(_E_MEV.value_str)     # CODATA 2022, from the string, not a float

Z_D = Q0**3 / (Q0**2 + 1)          # convention D (canonical)


def _z_convention_C_HISTORICAL(q):
    """Excised convention C, z = sqrt(q)/(q+1).  Used ONLY for the labelled
    provenance comparison below; never in a reported D value."""
    return mp.sqrt(q) / (q + 1)


Z_C_HIST = _z_convention_C_HISTORICAL(Q0)

# Observed Q-values (NNDC/ENSDF), as strings -> mpf (no float64 path).
NUCLEI = [
    # (Z, N, name, Q_exp, Q_exp_err)
    (1, 2, "3H", "0.01861", "0.00001"),
    (6, 8, "14C", "0.15648", "0.00004"),
    (27, 33, "60Co", "0.31817", "0.00013"),
    (38, 52, "90Sr", "0.54590", "0.00007"),
    (55, 82, "137Cs", "0.51400", "0.00021"),
    (83, 127, "210Bi", "1.16270", "0.00006"),
]
MAGIC = [0, 2, 8, 20, 28, 50, 82, 126]

# ── H_3(q): Iwahori--Hecke algebra on the T_w basis, w in S_3 ─────────────
# Generators s0, s1; quadratic relation s^2 = (q - q^{-1}) s + 1.
S3 = list(itertools.permutations(range(3)))
IDX = {w: i for i, w in enumerate(S3)}


def _length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


def _rmul_s(w, i):
    """w * s_i as a permutation (s_i swaps positions i, i+1)."""
    v = list(w)
    v[i], v[i + 1] = v[i + 1], v[i]
    return tuple(v)


def _reduced_word(w):
    word = []
    v = tuple(w)
    while _length(v) > 0:
        for i in range(2):
            u = _rmul_s(v, i)
            if _length(u) < _length(v):
                word.append(i)
                v = u
                break
    return list(reversed(word))


RED = {w: _reduced_word(w) for w in S3}


def h_zero():
    return [mp.mpf(0)] * 6


def h_basis(w, c=1):
    x = h_zero()
    x[IDX[w]] = mp.mpf(c)
    return x


ID = tuple(range(3))


def h_rmul_gen(x, i, ha):
    """x * s_i on the T_w basis."""
    y = h_zero()
    for w in S3:
        c = x[IDX[w]]
        if c == 0:
            continue
        ws = _rmul_s(w, i)
        if _length(ws) > _length(w):
            y[IDX[ws]] += c
        else:
            y[IDX[w]] += ha * c
            y[IDX[ws]] += c
    return y


def h_mul(x, y, ha):
    out = h_zero()
    for v in S3:
        c = y[IDX[v]]
        if c == 0:
            continue
        t = list(x)
        for i in RED[v]:
            t = h_rmul_gen(t, i, ha)
        for k in range(6):
            out[k] += c * t[k]
    return out


def h_add(x, y):
    return [a + b for a, b in zip(x, y)]


def h_scale(x, c):
    return [c * a for a in x]


def gen(i):
    return h_basis(_rmul_s(ID, i))


def gen_inv(i, ha):
    return h_add(gen(i), h_basis(ID, -ha))


def word(letters, ha):
    """Product of generators; letter i >= 0 is s_i, letter ~i (i.e. -i-1) is s_i^{-1}."""
    x = h_basis(ID)
    for a in letters:
        g = gen(a) if a >= 0 else gen_inv(-a - 1, ha)
        x = h_mul(x, g, ha)
    return x


def markov_tr(x, z, ha):
    """Ocneanu/Markov trace on H_3, tr(1) = 1, tr(x s_{n-1} y) = z tr(x y).
    On the T_w basis: tr(T_w) = z^{l(w)} except the longest element,
    tr(s0 s1 s0) = z * tr(s0^2) = z (ha z + 1)."""
    total = mp.mpf(0)
    for w in S3:
        c = x[IDX[w]]
        if c == 0:
            continue
        L = _length(w)
        t = z * (ha * z + 1) if L == 3 else z**L
        total += c * t
    return total


def alternating_idempotent(q, ha):
    """e_(1^3) = (sum_w (-q)^{-l(w)} T_w) / [3]_{q^{-1}}! style normaliser:
    sum_w (-q^{-1})^{l(w)} T_w is an eigenvector with s_i -> -q^{-1}; divide by
    its eigenvalue-sum so e^2 = e."""
    x = h_zero()
    for w in S3:
        x[IDX[w]] = (-1 / q) ** _length(w)
    norm = sum(((1 / q) ** (2 * _length(w)) for w in S3), mp.mpf(0))
    return h_scale(x, 1 / norm)


def torus_knot(r, s):
    """tau(r,s) in H_3: (s0)^s for r=2, (s0 s1)^s for r=3."""
    letters = [0] * s if r == 2 else [0, 1] * s
    return letters


T_BETA = [0, -2]                   # s0 * s1^{-1}

# ── Rosso--Jones invariants J(tau(r,s)) = sum_lambda d_lambda omega_lambda^s ─
def qint(n, q):
    return (q**n - q**(-n)) / (q - 1 / q)


def rj_invariant(r, s, q):
    """d_lambda(q) = prod_cells [2 + c]_q / [h]_q (the dimensions used in the
    block, so d_(1^3) = 0); omega as in the deprecated producer."""
    if r == 2:
        irreps = [((2,), q), ((1, 1), -1 / q)]
    else:
        irreps = [((3,), q**3), ((2, 1), mp.mpf(-1)), ((1, 1, 1), -(1 / q) ** 3)]
    total = mp.mpf(0)
    parts = {}
    for lam, om in irreps:
        d = mp.mpf(1)
        conj = [sum(1 for row in lam if row > j) for j in range(lam[0])]
        for i, row in enumerate(lam):
            for j in range(row):
                c = j - i
                h = (row - j - 1) + (conj[j] - i - 1) + 1
                d *= qint(2 + c, q) / qint(h, q)
        parts[str(lam)] = d * om**s
        total += d * om**s
    return total, parts


# ── Q_bare: inductive-chain Skein polynomial (part (i)) ─────────────────────
def crossing_coeffs(ti, tj, ha):
    if ti == "p" and tj == "p":
        return mp.mpf(1), mp.mpf(0)
    if ti == "n" and tj == "n":
        return mp.mpf(1), -ha
    return mp.mpf(1), -ha / 2


def t_mat(c, d, ha):
    return [[c * ha + d, c], [c, d]]


def mat_mul(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def log_abs_skein(p, n, z, ha):
    """sum_j ln|V_j|, V_j = z M_j[0][0] + M_j[1][0]; returns (sum, n_zero, n_neg)."""
    types = ["p"] * p + ["n"] * n
    A = p + n
    acc = mp.mpf(0)
    n_zero = n_neg = 0
    for i in range(A - 1):
        M = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]
        for j in range(i + 1, A):
            c, d = crossing_coeffs(types[i], types[j], ha)
            M = mat_mul(M, t_mat(c, d, ha))
        V = z * M[0][0] + M[1][0]
        if V == 0:
            n_zero += 1
            continue
        if V < 0:
            n_neg += 1
        acc += mp.log(abs(V))
    return acc, n_zero, n_neg


def delta_ln_p(Z, N, z, ha):
    par, z0p, negp = log_abs_skein(Z, N, z, ha)
    dau, z0d, negd = log_abs_skein(Z + 1, N - 1, z, ha)
    return abs(dau - par), {"zero_V_parent": z0p, "zero_V_daughter": z0d,
                            "neg_V_parent": negp, "neg_V_daughter": negd}


def shell_index(n):
    """1-based shell of the n-th neutron: shell k = (MAGIC[k-1], MAGIC[k]]."""
    for k in range(1, len(MAGIC)):
        if MAGIC[k - 1] < n <= MAGIC[k]:
            return k
    return len(MAGIC)


def main():
    out = {}
    # Table 1 traces + Pauli column, both conventions (C labelled historical).
    knots = [(2, 3), (2, 5), (2, 7), (3, 5), (2, 9), (3, 4)]
    tb = word(T_BETA, HA)
    tr_tb_D = markov_tr(tb, Z_D, HA)
    tr_tb_C = markov_tr(tb, Z_C_HIST, HA)
    e = alternating_idempotent(Q0, HA)
    # check e is the (1^3) idempotent
    e2 = h_mul(e, e, HA)
    idem_resid = max(abs(a - b) for a, b in zip(e2, e))
    tr_e_D = markov_tr(e, Z_D, HA)
    tr_e_C = markov_tr(e, Z_C_HIST, HA)

    table1 = []
    for r, s in knots:
        x = h_mul(word(torus_knot(r, s), HA), tb, HA)
        exe = h_mul(h_mul(e, x, HA), e, HA)
        table1.append({
            "knot": f"tau({r},{s})",
            "tr_M_D": fmt(markov_tr(x, Z_D, HA)),
            "pauli_D": fmt(abs(markov_tr(exe, Z_D, HA)) / abs(tr_tb_D)),
            "tr_M_C_HISTORICAL": fmt(markov_tr(x, Z_C_HIST, HA)),
            "pauli_C_HISTORICAL": fmt(abs(markov_tr(exe, Z_C_HIST, HA)) / abs(tr_tb_C)),
        })
    pauli_tb_D = abs(markov_tr(h_mul(h_mul(e, tb, HA), e, HA), Z_D, HA)) / abs(tr_tb_D)
    pauli_tb_C = abs(markov_tr(h_mul(h_mul(e, tb, HA), e, HA), Z_C_HIST, HA)) / abs(tr_tb_C)

    # F_deg2 (as displayed in the interpretation block)
    J29, J29p = rj_invariant(2, 9, Q0)
    J34, J34p = rj_invariant(3, 4, Q0)
    tr29 = markov_tr(h_mul(word(torus_knot(2, 9), HA), tb, HA), Z_D, HA)
    tr34 = markov_tr(h_mul(word(torus_knot(3, 4), HA), tb, HA), Z_D, HA)
    F_deg2_D = (J29 * tr29 + J34 * tr34) / ((J29 + J34) * tr_tb_D)
    weighted_avg_no_div_D = (J29 * tr29 + J34 * tr34) / (J29 + J34)

    # Q_bare and residuals
    rows = []
    for Z, N, name, qexp_s, qerr_s in NUCLEI:
        qexp = mp.mpf(qexp_s)
        dlnD, diagD = delta_ln_p(Z, N, Z_D, HA)
        dlnC, _ = delta_ln_p(Z, N, Z_C_HIST, HA)
        qbare_D = dlnD / LN_Q * HBAR_Q * M_E / 3            # published formula
        qbare_D_lnnorm = dlnD * M_E / 3                     # deprecated normalisation
        qbare_C_lnnorm = dlnC * M_E / 3                     # historical provenance
        qbare_C_pub = dlnC / LN_Q * HBAR_Q * M_E / 3
        shell = shell_index(N)
        magic = N in MAGIC
        deg2 = shell >= 5
        if magic and deg2:
            q_comb = mp.mpf(0)                              # Pauli factor = 0 under D
            rule = "Pauli (magic N, shell>=5): F_Pauli^D = 0 => Q = 0"
        elif deg2:
            q_comb = qbare_D * F_deg2_D
            rule = "degree-2 shell: Q_bare * F_deg2^D"
        else:
            q_comb = qbare_D
            rule = "shell <= 4: F = 1 (Q = Q_bare)"
        rows.append({
            "nucleus": name, "Z": Z, "N": N, "shell_of_converting_neutron": shell,
            "N_magic": magic,
            "delta_ln_P_D": fmt(dlnD),
            "Q_bare_D_MeV": fmt(qbare_D),
            "Q_bare_D_err_pct": fmt((qbare_D - qexp) / qexp * 100),
            "Q_bare_D_ln_normalisation_MeV": fmt(qbare_D_lnnorm),
            "Q_combined_D_MeV": fmt(q_comb),
            "Q_combined_D_err_pct": fmt((q_comb - qexp) / qexp * 100),
            "combined_rule": rule,
            "Q_exp_MeV": qexp_s, "Q_exp_err_MeV": qerr_s,
            "Q_bare_C_HISTORICAL_ln_normalisation_MeV": fmt(qbare_C_lnnorm),
            "Q_bare_C_HISTORICAL_published_formula_MeV": fmt(qbare_C_pub),
            "chain_diagnostics_D": diagD,
        })

    # ── report ──
    print(f"q0 (proton) = {mp.nstr(Q0, 20)};  z_D = {mp.nstr(Z_D, 15)}")
    print(f"tr_M^D(T_beta) = {mp.nstr(tr_tb_D, 12)};  tr_M^D(e_(1^3)) = {mp.nstr(tr_e_D, 5)}"
          f"  (e^2-e resid {mp.nstr(idem_resid, 3)})")
    for t in table1:
        print(f"  {t['knot']:10s} tr_D={mp.nstr(mp.mpf(t['tr_M_D']),8)} "
              f"pauli_D={mp.nstr(mp.mpf(t['pauli_D']),3)} "
              f"[C hist: tr={mp.nstr(mp.mpf(t['tr_M_C_HISTORICAL']),6)} "
              f"pauli={mp.nstr(mp.mpf(t['pauli_C_HISTORICAL']),6)}]")
    print(f"Pauli(T_beta alone): D {mp.nstr(pauli_tb_D,3)}  C-hist {mp.nstr(pauli_tb_C,8)}")
    print(f"J(2,9) = {mp.nstr(J29,8)}, J(3,4) = {mp.nstr(J34,8)}, F_deg2^D = {mp.nstr(F_deg2_D,8)}")
    print(f"hbar_q/ln q = {mp.nstr(HBAR_Q/LN_Q, 8)}")
    for r in rows:
        print(f"  {r['nucleus']:6s} Qbare_D={mp.nstr(mp.mpf(r['Q_bare_D_MeV']),6)} "
              f"({mp.nstr(mp.mpf(r['Q_bare_D_err_pct']),4)}%)  "
              f"Qcomb_D={mp.nstr(mp.mpf(r['Q_combined_D_MeV']),6)} "
              f"({mp.nstr(mp.mpf(r['Q_combined_D_err_pct']),4)}%)  "
              f"[C hist ln-norm {mp.nstr(mp.mpf(r['Q_bare_C_HISTORICAL_ln_normalisation_MeV']),5)}, "
              f"pub {mp.nstr(mp.mpf(r['Q_bare_C_HISTORICAL_published_formula_MeV']),5)}]  {r['chain_diagnostics_D']}")

    w = WitnessBuilder("spectral-decomposition-qvalue-d", engine="mpmath")
    w.set_description(
        "Convention-D (z = q^3/(q^2+1)) recomputation at the proton q0 of every "
        "number quoted by cor:spectral-decomposition-qvalue and its table/"
        "interpretation siblings: Q_bare for six beta^- decays, the H_3 Markov "
        "traces tr_M(tau(r,s) s0 s1^-1), J(tau(2,9)), J(tau(3,4)), F_deg2, and "
        "the Pauli case (identically 0 under D). Replaces the float-only "
        "convention-C producer _deprecated/rosso-jones-qvalues.py (bean qou-wlnx)."
    )
    w.set_content_block("cor:spectral-decomposition-qvalue")
    w.add_parameter("q0", fmt(Q0))
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("markov_convention", "D: z = q^3/(q^2+1)")
    w.add_parameter("z_D", fmt(Z_D))
    w.add_parameter("m_e_MeV", _E_MEV.value_str)
    w.add_parameter("mp_dps", DPS)
    w.add_parameter("nucleon_ordering", "protons first, then neutrons (inherited)")

    w.add_assertion("tr_M^D(e_(1^3)) = 0 (Ocneanu weight of (1^3) vanishes under D)",
                    computed=fmt(abs(tr_e_D)), expected="0", tolerance="1e-55",
                    unit="dimensionless")
    w.add_assertion("e_(1^3) is idempotent", computed=fmt(idem_resid), expected="0",
                    tolerance="1e-55", unit="dimensionless")
    for t in table1:
        w.add_assertion(f"Pauli^D[{t['knot']}] = 0", computed=t["pauli_D"], expected="0",
                        tolerance="1e-50", unit="dimensionless")
    w.add_assertion("tr_M^D(T_beta) = z^2 - (q-q^-1) z", computed=fmt(tr_tb_D),
                    expected=fmt(Z_D**2 - HA * Z_D), tolerance="1e-60",
                    unit="dimensionless")

    w.add_data("table1_traces", table1)
    w.add_data("tr_M_T_beta", {"D": fmt(tr_tb_D), "C_HISTORICAL": fmt(tr_tb_C)})
    w.add_data("tr_M_e_1_3", {"D": fmt(tr_e_D), "C_HISTORICAL": fmt(tr_e_C)})
    w.add_data("pauli_T_beta_alone", {"D": fmt(pauli_tb_D), "C_HISTORICAL": fmt(pauli_tb_C)})
    w.add_data("rosso_jones", {
        "J_tau_2_9": fmt(J29), "J_tau_2_9_parts": {k: fmt(v) for k, v in J29p.items()},
        "J_tau_3_4": fmt(J34), "J_tau_3_4_parts": {k: fmt(v) for k, v in J34p.items()},
        "weight_ratio_J34_over_J29": fmt(J34 / J29),
        "F_deg2_D": fmt(F_deg2_D),
        "weighted_trace_average_without_division_D": fmt(weighted_avg_no_div_D),
    })
    w.add_data("hbar_q_over_ln_q", fmt(HBAR_Q / LN_Q))
    w.add_data("qvalues", rows)
    w.add_caveat(
        "Q_bare uses the published normalisation |log_q(P_dau/P_par)| * hbar_q * m_e/3. "
        "The deprecated producer used |ln(P_dau/P_par)| * m_e/3 (factor ln q/hbar_q "
        "~1.053 larger); both are emitted."
    )
    w.add_caveat(
        "Columns suffixed _C_HISTORICAL use the excised convention C and exist only "
        "to identify the provenance of figures the block quoted before 2026-10-10."
    )
    w.add_caveat(
        "The Pauli branch of part (iii) vanishes identically under D, so the combined "
        "formula gives Q = 0 for 137Cs (N = 82, shell 6). No replacement projection is "
        "derived here."
    )
    path = w.save({"q0Anchor": "proton"})
    print(f"witness: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
