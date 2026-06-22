#!/usr/bin/env python3
"""Decisive parameter-free Pauli-Young / Wigner-SU(4) spin-isospin Delta_lambda test.

The Delta_lambda gate (per-partition binding density in
  B(K) = m_e * |sum_{lambda |- 3A} y_lambda(q0) * chi^lambda(beta_K) * Delta_lambda(K)|)
has resisted six closure ansaetze (Frobenius co-Casimir, Demazure-fibre,
LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov) and Option-E
v1..v9.  Every one of those was a FIT (a tunable q-dependent expression chosen
to land on AME).

This probe tests a DIFFERENT object with ZERO free parameters: the
spin-isospin projection from the Pauli principle + Wigner's SU(4)
supermultiplet symmetry.

Construction (no tunable knobs):
  * Each nucleon is a 3-strand baryon whose internal strands sit in the
    spatially-symmetric (s-shell) state  ->  trivial S_3  ->  the complete
    homogeneous symmetric function h_3.
  * The A baryon-CENTERS occupy the lowest spatial orbital, hence the
    spatial wavefunction is fully SYMMETRIC.  The Pauli principle then forces
    the spin-isospin wavefunction to be fully ANTISYMMETRIC: the SU(4)
    supermultiplet [1^A].
      - A=2 (deuteron):  [1,1]  -> SU(4) "6" = (S=1,T=0) (+) (S=0,T=1)   [the np deuteron channel]
      - A=3 (3H, 3He):   [1,1,1]-> SU(4) "4bar" = (S=1/2,T=1/2)          [mirror pair]
      - A=4 (4He):       [1,1,1,1]-> SU(4) singlet (S=0,T=0)             [alpha; SU(4) shell closure]
      - A>4:             e_A[.] of a 4-dim spin-isospin space VANISHES   [closure predicted, not imposed]
  * On the n=3A strands, "A symmetric baryons combined fully antisymmetrically
    under baryon exchange" is exactly the plethysm  e_A[h_3].
  * Delta_lambda(A) = < s_lambda , e_A[h_3] >  = multiplicity of the S_{3A}
    irrep lambda in that plethysm.  An INTEGER.  Nothing is fit.

Then the canonical Path-D binding is evaluated against AME with the cached,
already-canonical y_lambda(q0) and chi^lambda(beta_K) witnesses.

It either reproduces the AME light-nuclei bindings (and the deuteron 0.572
pn-weight) parameter-free, or it fails cleanly -- closing off another
Delta_lambda direction.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"

# ---- electron mass (CODATA, MeV) -- the single dimensional input of the
#      whole framework (CAL-1).  NOT a Delta_lambda parameter.
M_E = mp.mpf("0.51099895069")

# ----------------------------------------------------------------------------
# Symmetric-group combinatorics (pure, exact)
# ----------------------------------------------------------------------------

def partitions(n, _max=None):
    """All partitions of n as descending tuples."""
    if _max is None:
        _max = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, _max), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def z_mu(mu):
    """Order of the centralizer of a permutation of cycle type mu in S_n."""
    from collections import Counter
    import math
    c = Counter(mu)
    z = 1
    for part, mult in c.items():
        z *= (part ** mult) * math.factorial(mult)
    return z


def mn_character(lam, mu):
    """chi^lambda(mu): irreducible S_n character, Murnaghan-Nakayama rule.

    lam, mu : partitions of the same n (descending tuples).
    Returns an int.
    """
    lam = sorted([p for p in lam if p > 0], reverse=True)
    mu = [p for p in mu if p > 0]
    return _mn(tuple(lam), tuple(sorted(mu, reverse=True)))


_MN_CACHE = {}

def _mn(lam, mu):
    if sum(lam) == 0:
        return 1
    key = (lam, mu)
    if key in _MN_CACHE:
        return _MN_CACHE[key]
    r = mu[0]
    rest = mu[1:]
    total = 0
    for (newlam, height) in _border_strips(lam, r):
        total += ((-1) ** height) * _mn(newlam, rest)
    _MN_CACHE[key] = total
    return total


def _border_strips(lam, r):
    """Yield (lambda \\ strip, height) for every border strip of size r.

    lam is a descending tuple.  Uses the beta-number / first-column hook
    representation.  Height = (#rows spanned) - 1.
    """
    lam = list(lam)
    k = len(lam)
    # beta numbers: beta_i = lam_i + (k-1-i)  for i = 0..k-1  (distinct, descending)
    beta = [lam[i] + (k - 1 - i) for i in range(k)]
    beta_set = set(beta)
    for i in range(k):
        b = beta[i]
        nb = b - r
        if nb < 0:
            continue
        if nb in beta_set:
            continue
        # removing a border strip = move beta value b down to nb
        newbeta = sorted([x for x in beta if x != b] + [nb], reverse=True)
        # height = number of beta values strictly between nb and b
        height = sum(1 for x in beta if nb < x < b)
        # convert newbeta back to a partition
        m = len(newbeta)
        newlam = tuple(newbeta[i] - (m - 1 - i) for i in range(m))
        newlam = tuple(p for p in newlam if p > 0)
        yield (newlam, height)


# ----------------------------------------------------------------------------
# Power-sum symmetric functions as dict: partition(tuple) -> Fraction coeff
# ----------------------------------------------------------------------------

def ps_mul(a, b):
    out = {}
    for pa, ca in a.items():
        for pb, cb in b.items():
            key = tuple(sorted(pa + pb, reverse=True))
            out[key] = out.get(key, Fraction(0)) + ca * cb
    return {k: v for k, v in out.items() if v != 0}


def ps_add(*terms):
    out = {}
    for t in terms:
        for k, v in t.items():
            out[k] = out.get(k, Fraction(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def ps_scale(a, s):
    s = Fraction(s)
    return {k: v * s for k, v in a.items()}


def h_n_in_powersums(n):
    """h_n = sum_{mu |- n} p_mu / z_mu  (complete homogeneous in power sums)."""
    return {mu: Fraction(1, z_mu(mu)) for mu in partitions(n)}


def adams(f, k):
    """psi_k(f) = p_k[f]: substitute p_j -> p_{kj} in the power-sum expansion."""
    return {tuple(sorted((p * k for p in mu), reverse=True)): c for mu, c in f.items()}


def e_plethysm(f, A):
    """e_A[f] via Newton's identities with p_j replaced by psi_j(f).

      1*e1 = psi1
      2*e2 = e1*psi1 - psi2
      3*e3 = e2*psi1 - e1*psi2 + psi3
      4*e4 = e3*psi1 - e2*psi2 + e1*psi3 - psi4
    """
    psi = {j: adams(f, j) for j in range(1, A + 1)}
    e = {0: {(): Fraction(1)}}  # e_0 = 1
    for m in range(1, A + 1):
        acc = {}
        for j in range(1, m + 1):
            sign = (-1) ** (j - 1)
            term = ps_mul(e[m - j], psi[j])
            acc = ps_add(acc, ps_scale(term, sign))
        e[m] = ps_scale(acc, Fraction(1, m))
    return e[A]


def delta_lambda_from_plethysm(A):
    """Delta_lambda(A) = < s_lambda, e_A[h_3] > for all lambda |- 3A.

    Returns dict: partition(tuple, descending) -> int multiplicity.
    """
    n = 3 * A
    g = e_plethysm(h_n_in_powersums(3), A)  # power-sum expansion of e_A[h_3]
    out = {}
    for lam in partitions(n):
        val = Fraction(0)
        for mu, c in g.items():
            val += c * mn_character(lam, mu)
        assert val.denominator == 1, f"non-integer multiplicity {val} for {lam}"
        out[lam] = int(val)
    return out


# ----------------------------------------------------------------------------
# Cached canonical inputs
# ----------------------------------------------------------------------------

def load_y_lambda(n):
    w = json.load(open(COMP / "y-lambda-at-q0.witness.json"))
    by_n = w["data"]["by_n"][str(n)]
    return {tuple(e["partition"]): mp.mpf(e["y_at_q0_50dps"]) for e in by_n}


def load_chi(atom):
    w = json.load(open(COMP / f"atom-chi-rust-{atom}.witness.json"))
    by = w["data"]["atom"]["by_partition"]
    return {tuple(e["partition"]): mp.mpf(e["chi_lambda"]) for e in by}


AME = {k: mp.mpf(v) for k, v in
       json.load(open(COMP / "ame-2020-binding-energies.witness.json"))["data"].items()}

ATOMS = [
    # (label, chi-witness key, A, Z, N, AME key)
    ("deuteron", "d",   2, 1, 1, "B_deuteron_MeV"),
    ("tritium",  "t",   3, 1, 2, "B_tritium_MeV"),
    ("helium-3", "3he", 3, 2, 1, "B_he3_MeV"),
    ("helium-4", "4he", 4, 2, 2, "B_he4_MeV"),
]


def main():
    results = []
    delta_cache = {}
    print("=" * 78)
    print("PAULI-YOUNG / WIGNER-SU(4) SPIN-ISOSPIN  Delta_lambda  TEST  (parameter-free)")
    print("  Delta_lambda(A) = < s_lambda , e_A[h_3] >   (plethysm multiplicity)")
    print("  B_pred(K) = m_e * | sum_lambda y_lambda(q0) chi^lambda(beta_K) Delta_lambda |")
    print("=" * 78)
    for label, key, A, Z, N, amek in ATOMS:
        n = 3 * A
        if A not in delta_cache:
            delta_cache[A] = delta_lambda_from_plethysm(A)
        delta = delta_cache[A]
        ylam = load_y_lambda(n)
        chi = load_chi(key)

        # the signed sum
        S = mp.mpf(0)
        per_lambda = []
        for lam in sorted(delta.keys(), key=lambda p: (-len(p), p)):
            d = delta[lam]
            if d == 0:
                continue
            y = ylam[lam]
            c = chi[lam]
            term = y * c * d
            S += term
            per_lambda.append((lam, d, y, c, term))
        B_pred = M_E * abs(S)
        B_ame = AME[amek]
        rel = (B_pred - B_ame) / B_ame

        sum_delta = sum(delta.values())
        nnz = sum(1 for v in delta.values() if v != 0)
        print(f"\n--- {label}  (Z={Z},N={N},A={A}; n={n} strands, {len(delta)} partitions) ---")
        print(f"    sum_lambda Delta_lambda = {sum_delta}  (= dim of e_{A}[h_3] channel); "
              f"nonzero blocks = {nnz}")
        print(f"    signed sum S            = {mp.nstr(S, 12)}")
        print(f"    B_pred                  = {mp.nstr(B_pred, 10)} MeV")
        print(f"    B_AME                   = {mp.nstr(B_ame, 10)} MeV")
        print(f"    relative error          = {mp.nstr(rel*100, 6)} %   "
              f"(factor {mp.nstr(B_pred/B_ame, 6)})")
        results.append({
            "atom": label, "Z": Z, "N": N, "A": A, "n_strands": n,
            "delta_lambda": {",".join(map(str, k)): v for k, v in delta.items() if v != 0},
            "sum_delta_lambda": sum_delta,
            "nonzero_blocks": nnz,
            "signed_sum": mp.nstr(S, 30),
            "B_pred_MeV": mp.nstr(B_pred, 30),
            "B_AME_MeV": str(B_ame),
            "rel_error_pct": mp.nstr(rel * 100, 12),
            "factor": mp.nstr(B_pred / B_ame, 12),
        })

    # ---- deuteron 0.572 pn-weight cross-check -------------------------------
    # E0 = m_e / (q0 (q0-1)); pn-weight = (B_D/E0)/L_pn, L_pn = -log(f_pn).
    q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")
    E0 = M_E / (q0 * (q0 - 1))
    z = mp.sqrt(q0) / (q0 + 1)
    h = q0 - 1 / q0
    delta_cf = mp.mpf("0.00137705")
    f_pn = z - h * (mp.mpf("0.5") - delta_cf / 4)
    L_pn = -mp.log(f_pn)
    pn_weight_ame = (AME["B_deuteron_MeV"] / E0) / L_pn
    # what THIS construction predicts for the same pn-weight observable:
    B_pred_D = mp.mpf(results[0]["B_pred_MeV"])
    pn_weight_pred = (B_pred_D / E0) / L_pn
    print("\n" + "=" * 78)
    print("DEUTERON pn-WEIGHT cross-check (signed_crossing_feasibility_probe.py object)")
    print(f"    E0 = m_e/(q0(q0-1))        = {mp.nstr(E0, 10)} MeV")
    print(f"    pn-weight from AME B_D     = {mp.nstr(pn_weight_ame, 8)}   (target ~0.572)")
    print(f"    pn-weight from B_pred(PY)  = {mp.nstr(pn_weight_pred, 8)}")
    print("=" * 78)

    verdict = "FAIL_CLEAN"
    dr = abs(mp.mpf(results[0]["rel_error_pct"]))
    if dr < 1:
        verdict = "MATCH_<1pct"
    elif dr < 10:
        verdict = "NEAR_<10pct"
    print(f"\nVERDICT (deuteron): rel-err {mp.nstr(dr,5)}%  ->  {verdict}")
    print("Parameter count: 0 (Delta_lambda are integer plethysm multiplicities; "
          "y_lambda, chi^lambda, m_e all canonical/cached).")

    witness = {
        "computation": "pauli-young-spin-isospin-delta-lambda",
        "description": (
            "Parameter-free Pauli-Young/Wigner-SU(4) spin-isospin Delta_lambda test: "
            "Delta_lambda(A)=<s_lambda,e_A[h_3]> plethysm multiplicities fed into the "
            "canonical Path-D binding B=m_e|sum y_lambda chi^lambda Delta_lambda|."
        ),
        "scriptFile": "computations/probes/pauli_young_spin_isospin_delta_lambda_probe.py",
        "parameters": {"q_0": str(q0), "m_e_MeV": str(M_E), "free_parameters": 0},
        "data": {
            "atoms": results,
            "deuteron_pn_weight": {
                "E0_MeV": mp.nstr(E0, 30),
                "pn_weight_from_AME": mp.nstr(pn_weight_ame, 30),
                "pn_weight_from_pred": mp.nstr(pn_weight_pred, 30),
                "target": "0.572",
            },
            "verdict_deuteron": verdict,
        },
    }
    outp = COMP / "pauli-young-spin-isospin-delta-lambda.witness.json"
    json.dump(witness, open(outp, "w"), indent=1)
    print(f"\nwitness -> {outp.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
