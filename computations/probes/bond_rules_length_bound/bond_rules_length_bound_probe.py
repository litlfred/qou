#!/usr/bin/env python3
"""bond_rules_length_bound_probe.py — the three γγ bond rules, and the sum over ALL bond lengths.

Bean `qou-brng` (brief C2, front E). Owner (Carl, 2026-11-27): "bond selection - keep open. exlore
all three. why do we need a lnegth cutoff? can we measure (surrealy) or estimae error bounds?"

Rules (scorecard only; none is adopted here):
  (1) the cheapest passing pure-junction γγ bond (corpus `FrobeniusSelected`, owner card 1);
  (2) the cheapest passing γγ bond that merges closure components;
  (3) the sum over all γγ bond words.
Rules (1), (2) are read from the committed ceiling witnesses (plus `rule1_pure_junction_a3_search.py`
for A = 3). This probe does rule (3) WITHOUT a length cutoff.

Rule (3), cutoff-free. Let S = Σ_s V(s), V(s) = σ_s σ_{s+1}^{-1} (the chiral vertex of the ruled photon
1 + φ0σ0 + φ1σ1 + φ01·σ0σ1^{-1}), s = 0..n-3. The sum over all words in the V(s) of every length,
each vertex carrying weight t, is the resolvent Σ_L (tS)^L = (1 - tS)^{-1}. The words that bond every
junction are obtained by inclusion-exclusion over the junction vertex pairs J_j = {V(3j-2), V(3j-1)}:

    Bsum(t) = Σ_{J ⊆ junctions} (-1)^{|J|} (1 - t S_{-J})^{-1},   Z(t) = Σ_J (-1)^{|J|} / (1 - t c_J)

with S_{-J} the sum without the vertices of J and c_J = n - 2 - 2|J| its vertex count (Z(t) is the
weighted number of bond words). Rule (3a): r(t) = tr(x Bsum(t)) / (Z(t) tr(x)), x = the free word
(V^3 per nucleon), B = -E0 ln r. Reading 3 is evaluated on the WHOLE summed element x·Bsum/Z
(ruling B 2026-09-13: whole element), at every level, on every two-row block.

The series converges iff |t| ρ(S_{-J}) < 1 for every J. Since V(s) fixes |0…0> (σ acts by q, σ^{-1}
by q^{-1}), ρ(S) ≥ n - 2: the radius is at most 1/(n-2). This is computed, with the spectrum.

Rule (3∞), weight-free: the uniform average over bond words of length L, L → ∞:
    lim_L tr(x Bsum_L) / (count_L tr(x)),  Bsum_L = Σ_J (-1)^{|J|} S_{-J}^L.
It exists when n-2 is the only eigenvalue of S of modulus ρ(S) = n-2 and is semisimple; then it is
tr(x P)/tr(x), P the spectral projector of S at n-2. Computed by powers and by the eigen-data.

Tail bound (archimedean, after the wall): for a truncation at length L0 of the weighted sum,
    ||Σ_{L>L0} (tS')^L|| ≤ (|t| ||S'||)^{L0+1} / (1 - |t| ||S'||)        when |t| ||S'|| < 1,
and |tr(Y)| ≤ ||Y||_2 for the normalised quantum trace (K = diag(q, 1/q) is positive with Tr K = [2]).
Lean: `QOU.MassTheory.BondLengthSumTail`.

Representation: Schur-Weyl on (C^2)^{⊗n}, R-matrix with σ - σ^{-1} = h (exactly the independent
trace of the ceiling probe, which agrees with the corpus seminormal trace to 1e-25), block-diagonal
in the number of 1s. Level characters: E_{n→m} is the K^{-1}-weighted partial trace over the last n-m
strands divided by [2]^{n-m}; on two-row λ = (m-k, k), χ_λ = T_k - T_{k-1} with T_k the ordinary trace
on the m-strand weight space with k ones (q-Young rule). Checked against the corpus seminormal level
characters EXACTLY on sample words (K1; with K instead it does not).

Convention D, proton pin (cf.Q), mpmath 40 dps, no float arithmetic. AME is not read here; the
scorecard against AME is in the audit doc. Nothing fitted, selected or wired. The weights t used are
corpus quantities (h, q h, q^{-1} h: the Hecke grading and the photon amplitudes of
V^3 = γ(0,0,qh)·γ(0,0,-q^{-1}h)); NONE is derived as the bond weight.

-- Ref: [leitner2026] bean qou-brng; bean qou-ales; QOU.MassTheory.ClassicalReading3MergeBound
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = int(sys.argv[1]) if len(sys.argv) > 1 else 2
sys.argv = [sys.argv[0], "4", str(A)]
sys.path.insert(0, str(HERE.parent / "binding_ceiling_q0"))
import binding_ceiling_q0_probe as bc  # noqa: E402

mp = bc.mp
mp.mp.dps = 40
Q, H, ONE, ZERO, TOL = bc.Q, bc.H, bc.ONE, bc.ZERO, bc.TOL
N = bc.N
NV = N - 2
JUNCTIONS = [sorted(J) for J in bc.JUNCTIONS]
D2 = Q + 1 / Q
T0 = time.time()
LPOW = 1024     # largest power for the uniform limit; the spectral gap at A = 3 is small (|λ2/λ1| ≈ 0.95)


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ------------------------------------------------------------------ weight-space blocks
STATES = {k: [st for st in itertools.product((0, 1), repeat=N) if sum(st) == k] for k in range(N + 1)}
INDEX = {k: {st: i for i, st in enumerate(v)} for k, v in STATES.items()}


def op_blocks(word):
    """word: list of (gen, inverse?) -> {k: mp.matrix} acting on column vectors (left action, word read
    left to right as in bc._apply: the first letter acts first)."""
    out = {}
    for k, sts in STATES.items():
        d = len(sts)
        M = mp.zeros(d, d)
        for j, st in enumerate(sts):
            v = {st: ONE}
            for (s, inv) in word:
                v = bc._apply(v, s, inv)
            for st2, c in v.items():
                M[INDEX[k][st2], j] += c
        out[k] = M
    return out


def kweight(k, n=N):
    return Q ** (n - 2 * k)


def trace_blocks(Y):
    return mp.fsum(kweight(k) * sum(Y[k][i, i] for i in range(Y[k].rows)) for k in Y) / D2 ** N


def matmul_blocks(X, Y):
    return {k: X[k] * Y[k] for k in X}


# word convention: bc.sw_trace applies letters of x then K, i.e. operator = M_K · M_x on columns.
# trace is cyclic, so tr(x·K) = Tr(K_op x_op). Keep products in the order "later letters on the left".


def level_chars_from_diag(Y):
    """Y: blocks of an element of H_n in the SW rep. Returns {(m, (m-k, k)): χ} for every level m."""
    diag = {}
    for k, M in Y.items():
        for i, st in enumerate(STATES[k]):
            diag[st] = M[i, i]
    out = {}
    for m in range(1, N + 1):
        T = [ZERO] * (m + 1)
        for st, v in diag.items():
            tail = st[m:]
            w = ONE
            for b in tail:
                w *= 1 / Q if b == 0 else Q
            T[sum(st[:m])] += w * v
        T = [t / D2 ** (N - m) for t in T]
        for k in range(m // 2 + 1):
            lam = (m - k, k) if k else (m,)
            out[(m, lam)] = T[k] - (T[k - 1] if k else ZERO)
    return out


def eigvals(M):
    if M.rows == 1:
        return [M[0, 0]]
    return mp.eig(M, left=False, right=False)


def eig_right(M):
    if M.rows == 1:
        return [M[0, 0]], mp.matrix([[ONE]])
    return mp.eig(M, left=False, right=True)


def opnorm2(M):
    """spectral norm sqrt(λmax(MᵀM)); M real."""
    if M.rows == 0:
        return ZERO
    G = M.T * M
    ev = mp.eigsy(G, eigvals_only=True)
    return mp.sqrt(max(ev[i] for i in range(ev.rows)))


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}  ({src})")

    x_word = [(s + 3 * a, i) for a in range(A) for (s, i) in bc.V(0) * 3]
    X = op_blocks(x_word)
    trx = trace_blocks(X)
    trx_c, _ = bc.corpus_trace_and_pass(x_word)
    Vb = {s: op_blocks(bc.V(s)) for s in range(NV)}
    log(f"A={A} n={N}: blocks built; tr(x) = {mp.nstr(trx, 20)} (corpus {mp.nstr(trx_c, 20)})")
    check("K0_sw_trace_matches_corpus_on_free_word", abs(trx - trx_c) < TOL, "seminormal vs Schur-Weyl")

    # K1: level characters from the SW diagonal agree in sign (and up to a positive per-(m,λ) factor)
    # with the corpus seminormal level characters, on the free word and on two bond words.
    samples = [[], [2, 3], [1, 2, 1, 2]] if A == 2 else [[], [2, 3, 4], [1, 4]]
    ratios = {}
    sign_ok = True
    for w in samples:
        word = x_word + [lt for s in w for lt in bc.V(s)]
        Y = op_blocks(word)
        mine = level_chars_from_diag(Y)
        d = bc.base.diag_of(bc.corpus_letters(word), N)
        corp = bc.gga.level_chars(d, N, 1)
        for key, v in corp.items():
            mv = mine[key]
            if abs(v) < TOL and abs(mv) < TOL:
                continue
            if (v > TOL) != (mv > TOL) or abs(v) < TOL or abs(mv) < TOL:
                sign_ok = False
                continue
            ratios.setdefault(key, []).append(mv / v)
    const_ok = all(abs(r - 1) < mp.mpf("1e-25") for rs in ratios.values() for r in rs)
    check("K1_level_characters_equal_corpus_seminormal",
          sign_ok and const_ok,
          f"{len(ratios)} (level, block) pairs, {len(samples)} words")

    # ---------------------------------------------------------------- spectra and norms
    subsets = [J for r in range(len(JUNCTIONS) + 1) for J in itertools.combinations(range(len(JUNCTIONS)), r)]

    def S_minus(J):
        drop = set().union(*[set(JUNCTIONS[j]) for j in J]) if J else set()
        keep = [s for s in range(NV) if s not in drop]
        return {k: sum((Vb[s][k] for s in keep), mp.zeros(len(STATES[k]), len(STATES[k]))) for k in STATES}, len(keep)

    SJ = {J: S_minus(J) for J in subsets}
    S = SJ[()][0]
    vnorm = max(opnorm2(Vb[s][k]) for s in range(NV) for k in STATES)
    snorm = max(opnorm2(S[k]) for k in STATES)
    xnorm = max(opnorm2(X[k]) for k in STATES)
    log(f"||V(s)|| = {mp.nstr(vnorm, 15)} (q^2 = {mp.nstr(Q**2, 15)}), ||S|| = {mp.nstr(snorm, 15)}, ||x|| = {mp.nstr(xnorm, 15)}")
    spec = []
    for k in STATES:
        ev = eigvals(S[k])
        spec += [(k, e) for e in ev]
    rho = max(abs(e) for _, e in spec)
    top = sorted(spec, key=lambda p: -abs(p[1]))[:8]
    log(f"rho(S) = {mp.nstr(rho, 20)}; n-2 = {NV}; top |eig|: " +
        ", ".join(f"k={k}:{mp.nstr(e, 10)}" for k, e in top))
    n_at_rho = sum(1 for _, e in spec if abs(abs(e) - rho) < mp.mpf("1e-20"))
    lam2 = max(abs(e) for _, e in spec if abs(abs(e) - rho) >= mp.mpf("1e-20"))
    log(f"second |eig| of S: {mp.nstr(lam2, 20)}; uniform-limit rate |λ2/λ1| = {mp.nstr(lam2 / rho, 15)}")
    check("K2_rho_S_at_least_n_minus_2", rho >= NV - mp.mpf("1e-30"), "V(s) fixes |0...0>")
    rho_J = {}
    for J in subsets:
        rj = ZERO
        for k in STATES:
            if SJ[J][0][k].rows:
                rj = max(rj, max(abs(e) for e in eigvals(SJ[J][0][k])))
        rho_J[J] = rj
    t_star = 1 / max(rho_J.values())
    log(f"radius of convergence of the weighted bond sum: t* = {mp.nstr(t_star, 20)}")

    # ---------------------------------------------------------------- rule (3a): weighted resolvent
    E0 = bc.mp.mpf("4.2274833556290305503")   # tower E0 (ceiling witness parameter)
    weights = {"h": H, "q*h": Q * H, "h/q": H / Q, "t*/2": t_star / 2}
    rows3a = {}
    for name, t in weights.items():
        conv = abs(t) < t_star
        Bs = {k: mp.zeros(len(STATES[k]), len(STATES[k])) for k in STATES}
        Z = ZERO
        for J in subsets:
            sgn = (-1) ** len(J)
            for k in STATES:
                d = len(STATES[k])
                Bs[k] += sgn * mp.inverse(mp.eye(d) - t * SJ[J][0][k])
            Z += sgn / (1 - t * SJ[J][1])
        Y = {k: Bs[k] * X[k] / Z for k in STATES}
        r = trace_blocks(Y) / trx
        lc = level_chars_from_diag(Y)
        neg = [(key, v) for key, v in lc.items() if v < -TOL]
        rows3a[name] = {"t": mp.nstr(t, 20), "converges": conv, "Z": mp.nstr(Z, 20), "ratio": mp.nstr(r, 25),
                        "minus_ln_r": mp.nstr(-mp.log(r), 20) if r > 0 else None,
                        "B_MeV_tower": mp.nstr(-E0 * mp.log(r), 12) if r > 0 else None,
                        "reading3_pass": not neg, "n_negative_level_chars": len(neg),
                        "most_negative": (str(min(neg, key=lambda p: p[1])[0]), mp.nstr(min(neg, key=lambda p: p[1])[1], 8)) if neg else None}
        log(f"rule 3a t={name}: {rows3a[name]}")

    # ---------------------------------------------------------------- rule (3∞): weight-free limit
    # tr(x S_{-J}^L) / count_L by repeated multiplication; report L = 2^j.
    # successive squaring: L = 1, 2, 4, ..., LPOW
    lim_rows = {}
    powJ = {J: {k: SJ[J][0][k] for k in STATES} for J in subsets}
    L = 1
    while L <= LPOW:
        num, cnt = ZERO, ZERO
        for J in subsets:
            sgn = (-1) ** len(J)
            num += sgn * trace_blocks({k: powJ[J][k] * X[k] for k in STATES})
            cnt += sgn * mp.mpf(SJ[J][1]) ** L
        if cnt == 0:          # no bond word of this length (A >= 3, L < A - 1)
            lim_rows[L] = {"count": "0", "ratio": None, "minus_ln_r": None}
            log(f"rule 3inf L={L}: no bond words")
            if L < LPOW:
                powJ = {J: {k: powJ[J][k] * powJ[J][k] for k in STATES} for J in subsets}
            L *= 2
            continue
        rL = num / cnt / trx
        lim_rows[L] = {"count": mp.nstr(cnt, 12), "ratio": mp.nstr(rL, 25),
                       "minus_ln_r": mp.nstr(-mp.log(rL), 20) if rL > 0 else None}
        log(f"rule 3inf L={L}: {lim_rows[L]}")
        if L < LPOW:
            powJ = {J: {k: powJ[J][k] * powJ[J][k] for k in STATES} for J in subsets}
        L *= 2
    # spectral projector at n-2 on the blocks that carry it (|0..0>, |1..1> plus any interior copies)
    proj_num = ZERO
    Pblocks = {k: mp.zeros(len(STATES[k]), len(STATES[k])) for k in STATES}
    for k in STATES:
        Sk = S[k]
        d = Sk.rows
        ev, ER = eig_right(Sk)
        idx = [i for i, e in enumerate(ev) if abs(e - NV) < mp.mpf("1e-20")]
        if not idx:
            continue
        EL = mp.inverse(ER)
        P = mp.zeros(d, d)
        for i in idx:
            for a in range(d):
                for b in range(d):
                    P[a, b] += ER[a, i] * EL[i, b]
        Pblocks[k] = P
        proj_num += sum(kweight(k) * (P * X[k])[i, i] for i in range(d))
    r_inf = (proj_num / D2 ** N) / trx
    r_inf = mp.re(r_inf)
    log(f"rule 3inf spectral limit: ratio {mp.nstr(r_inf, 25)}, multiplicity of |eig| = rho: {n_at_rho}")
    y_triv = (Q ** (N + 1) - Q ** (-N - 1)) / (Q - 1 / Q) / D2 ** N     # y_(n) = [n+1]/[2]^n
    check("K4_uniform_limit_is_trivial_block_weight_over_tr_x", abs(r_inf - y_triv / trx) < mp.mpf("1e-25"),
          f"closed form y_(n)/tr(x) = {mp.nstr(y_triv / trx, 20)}")
    lcP = level_chars_from_diag({k: (Pblocks[k] * X[k]).apply(mp.re) for k in STATES})
    negP = [kk for kk, v in lcP.items() if v < -TOL]
    log(f"rule 3inf limit element: reading 3 {'PASS' if not negP else 'FAIL'} ({len(negP)} negative)")
    rL_last = mp.mpf(lim_rows[LPOW]["ratio"])
    check("K3_power_average_tends_to_spectral_limit", abs(rL_last - r_inf) < mp.mpf("1e-6"),
          f"L={LPOW} {mp.nstr(rL_last, 12)} vs projector {mp.nstr(r_inf, 12)}")

    # ---------------------------------------------------------------- truncation tail bounds (3a)
    # truncate the weighted sum at length L0 and compare with the exact resolvent; bound:
    #   |N - N_T| <= ||x|| Σ_J (|t| ||S_J||)^(L0+1)/(1-|t| ||S_J||)   (|tr Y| <= ||Y||_2),
    #   |Z - Z_T|  = |Σ_J (-1)^|J| (t c_J)^(L0+1)/(1 - t c_J)| <= Σ_J (|t| c_J)^(L0+1)/(1-|t| c_J).
    sJnorm = {J: max(opnorm2(SJ[J][0][k]) for k in STATES if SJ[J][0][k].rows) for J in subsets}
    trunc = {}
    for name, t in weights.items():
        if not all(abs(t) * sJnorm[J] < 1 for J in subsets):
            trunc[name] = {"bound_available": False}
            continue
        trunc[name] = {}
        exact = mp.mpf(rows3a[name]["ratio"])
        for L0 in (2, 4, 6, 8):
            NT, ZT = ZERO, ZERO
            for J in subsets:
                sgn = (-1) ** len(J)
                Pk = {k: mp.eye(len(STATES[k])) for k in STATES}
                acc = {k: mp.zeros(len(STATES[k]), len(STATES[k])) for k in STATES}
                for L in range(1, L0 + 1):
                    Pk = {k: (t * SJ[J][0][k]) * Pk[k] for k in STATES}
                    acc = {k: acc[k] + Pk[k] for k in STATES}
                NT += sgn * trace_blocks({k: acc[k] * X[k] for k in STATES})
                ZT += sgn * mp.fsum((t * SJ[J][1]) ** L for L in range(1, L0 + 1))
            rT = NT / ZT / trx
            epsN = xnorm * mp.fsum((abs(t) * sJnorm[J]) ** (L0 + 1) / (1 - abs(t) * sJnorm[J]) for J in subsets)
            epsZ = mp.fsum((abs(t) * SJ[J][1]) ** (L0 + 1) / (1 - abs(t) * SJ[J][1]) for J in subsets)
            bound = (epsN / trx + abs(rT) * epsZ) / (ZT - epsZ) if ZT > epsZ else None
            ok = (abs(rT - exact) <= bound) if bound is not None else None
            trunc[name][str(L0)] = {"ratio_truncated": mp.nstr(rT, 20), "abs_error": mp.nstr(abs(rT - exact), 8),
                                    "proved_bound": mp.nstr(bound, 8) if bound is not None else None,
                                    "bound_holds": ok}
            log(f"trunc t={name} L0={L0}: {trunc[name][str(L0)]}")
    check("K5_truncation_error_within_norm_bound",
          all(v["bound_holds"] is not False for d in trunc.values() for v in d.values() if isinstance(v, dict)),
          "every (t, L0) with a geometric norm bound")
    tails = {}
    for name, t in weights.items():
        rt = abs(t) * snorm
        tails[name] = {"t_norm_S": mp.nstr(rt, 15), "geometric": rt < 1,
                       "tail_factor_L4": mp.nstr(rt ** 5 / (1 - rt), 10) if rt < 1 else None,
                       "tail_factor_L6": mp.nstr(rt ** 7 / (1 - rt), 10) if rt < 1 else None}
        log(f"tail t={name}: {tails[name]}")

    wb = (bc.WitnessBuilder(f"bond-rules-length-bound-A{A}", engine="mpmath")
          .set_description(
              "PROBE (bean qou-brng, brief C2 front E): rule (3) 'sum over all gamma-gamma bond words' without a "
              "length cutoff, as the inclusion-exclusion resolvent of S = sum of chiral vertices V(s), with a "
              "per-vertex weight t taken from corpus quantities (h, qh, h/q; none derived as the bond weight), and "
              "the weight-free uniform limit L -> infinity. Spectrum, radius of convergence, norm tail bounds. "
              "Reading 3 on the whole summed element. Schur-Weyl rep, convention D, proton pin. Scorecard only: "
              "AME not read, nothing fitted, selected or wired.")
          .set_audit_only("docs/audits/2026-11-27-bond-rules-and-length-cutoff.md")
          .add_parameter("A", A).add_parameter("n_strands", N).add_parameter("E0_tower_MeV", mp.nstr(E0, 20))
          .add_data("norms", {"V": mp.nstr(vnorm, 20), "S": mp.nstr(snorm, 20), "x": mp.nstr(xnorm, 20),
                              "q_squared": mp.nstr(Q ** 2, 20)})
          .add_data("spectrum", {"rho_S": mp.nstr(rho, 25), "n_minus_2": NV, "n_eigs_at_rho": n_at_rho, "second_abs_eig": mp.nstr(lam2, 25),
                                 "uniform_limit_rate": mp.nstr(lam2 / rho, 20),
                                 "top": [[k, mp.nstr(mp.re(e), 15), mp.nstr(mp.im(e), 15)] for k, e in top],
                                 "rho_by_dropped_junctions": {str(J): mp.nstr(v, 20) for J, v in rho_J.items()},
                                 "t_star": mp.nstr(t_star, 25)})
          .add_data("rule3a_weighted_resolvent", rows3a)
          .add_data("rule3inf_uniform_limit", {"by_L": {str(k): v for k, v in lim_rows.items()},
                                                "spectral_limit_ratio": mp.nstr(r_inf, 25),
                                                "closed_form": "y_(n)/tr(x), y_(n) = [n+1]_q/[2]_q^n",
                                                "limit_element_reading3_pass": not negP,
                                                "spectral_limit_minus_ln_r": mp.nstr(-mp.log(r_inf), 20) if r_inf > 0 else None,
                                                "B_MeV_tower": mp.nstr(-E0 * mp.log(r_inf), 12) if r_inf > 0 else None})
          .add_data("tail_bounds", tails)
          .add_data("truncation_vs_exact", trunc)
          .add_data("subset_norms", {str(J): mp.nstr(v, 20) for J, v in sJnorm.items()}))
    for name, ok, src in checks:
        wb.add_assertion(name, computed=ok, expected=True, tolerance=0, source=src)
    wb.save({"q0Anchor": "proton", "q0Value": mp.nstr(Q, 50),
             "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)"})
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
