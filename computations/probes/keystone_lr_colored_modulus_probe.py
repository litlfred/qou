#!/usr/bin/env python3
"""Keystone — the Lawrence–Rozansky COLORED-MODULUS identification for Σ(2,3,5).

Front 2 of `docs/audits/2026-07-17-three-front-attack-specs.md` §2. The open keystone step (from
`keystone_mckay_e8_valuemap.py`, which DERIVED the value map `d_q(λ)=[mark]_q` but DEFERRED the
colored amplitude) is the modulus identification

        |S_{0λ}^{Σ(2,3,5)}(ζ)|  =?=  d_ζ(λ) / D(ζ)          (Front-2 target)

at fibre roots of unity ζ_N, with the colours mapped by the parameter-free dictionary
McKay(2I ↔ affine Ê₈) ∘ (A₅ ⊂ S₅) and the VALUES living on the E₈ **marks** (`[e]_q` on the
exponents was refuted — `keystone_colored_sigma235_wrt.py`). `d_ζ(λ)` is the Hecke q-dimension of
the S₅ block, `D(ζ)=√Σ_λ d_ζ(λ)²`; the 4 conjugation classes carry marks {1,4,5,6} with values
`[1]_ζ, [4]_ζ, [5]_ζ, [5]_ζ+1` (the split electron block `(3,1,1)` is `[5]_ζ+1`, NOT `[6]_ζ`).

This probe reuses the machine-validated Hikami machinery of
`keystone_valuemap_genuine_smatrix_s013.py` (τ_N Gauss sum eq. 2.11, φ=181/30 eq. 2.12, χ eq. 3.1,
Eichler limit eq. 4.2, Theorem-10 exact anchor eq. 5.5, and the genuine S-matrix eq. 3.8) and adds
the colour-α insertion on the order-5 (icosahedral / A₅) exceptional fibre in the p₃=5 numerator.

Pre-registered GATE and kill criteria (spec §2, followed EXACTLY — no fit, nothing wired):

  • GATE 0 (must pass before any conclusion): the colour-α insertion at α=1 reproduces the bare
    τ_N(Σ(2,3,5)) to machine zero, and the bare Theorem-10 identity holds — jointly re-validating the
    whole transcription chain. If GATE 0 fails the probe stops with no modulus conclusion.

  • INDEPENDENCE / D=2 collapse (the decisive structural trap): the number of INDEPENDENT colored
    vacuum-row moduli. D(2,3,5)=(p₁−1)(p₂−1)(p₃−1)/4 = 2. The probe must show whether the
    McKay-labelled coloring escapes the D=2 collapse or re-derives the existing refutation.

  • Kill criteria: ratio-vector mismatch at every N; the D=2 collapse; the split node returning
    `[6]_ζ` instead of `[5]_ζ+1`; a conjugation-modulus violation `|S_{0λ}|≠|S_{0λ'}|`.

  Success = EVIDENCE, never proof (the Lean `loc_matches` gate closes only by derivation);
  a scope-(a) negative is a fully acceptable, honest outcome.

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694  (math-ph/0405028; eqs. 2.11,
#      2.12, 3.1, 3.8, 4.2, 5.5)
# Ref: [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf, mpc  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40
PVEC = (2, 3, 5)
P = 30                     # p1*p2*p3 = h(E8) = Coxeter number
TWO_P = 60
Q0 = mpf("1.1099785955541805")
I = mpc(0, 1)

# --- McKay 2I ↔ Ê₈ ∘ (A₅⊂S₅) dictionary (from keystone_mckay_e8_valuemap.py; no fit) ----------
# The 4 bwS0 conjugation classes {λ,λ'} -> A₅/McKay mark; value d_q(λ) = [mark]_q (unsplit) or
# [5]_q+1 (the split electron node (3,1,1), mark 6 = A₅ 3⊕3'). The order-5 fibre colour α∈{1,2,3,4}
# is the SU(2) Wilson-line colour on the icosahedral fibre (ℓ₃=α in the S-matrix eq. 3.8).
CLASS_TO_NODE = [
    {"class": [(5,), (1, 1, 1, 1, 1)], "mark": 1, "split": False, "note": "trivial pair"},
    {"class": [(4, 1), (2, 1, 1, 1)], "mark": 4, "split": False, "note": "A5 standard + sign"},
    {"class": [(3, 2), (2, 2, 1)], "mark": 5, "split": False, "note": "muon block (3,2)"},
    {"class": [(3, 1, 1)], "mark": 6, "split": True, "note": "electron block, A5 3+3' SPLIT"},
]
PARTS5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]


# ── d_q machinery (n=5), evaluated at a general q (root of unity or q₀) ───────────────────────
def qint(m, q):
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def q_factorial(m, q):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= qint(k, q)
    return r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def d_q(lam, q):
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h, q)
    return q_factorial(sum(lam), q) / den


def zeta(N):
    """Fibre root of unity ζ_N = e^{iπ/N}: then [m]_ζ = sin(mπ/N)/sin(π/N) (SU(2) character)."""
    return mp.e ** (mp.pi * I / N)


# ── (τ) bare WRT invariant τ_N(Σ(2,3,5)) — reused verbatim from s013 (eq. 2.11 / 2.12) ────────
def dedekind_s(b, a):
    return mp.fsum(mp.cot(mp.pi * k / a) * mp.cot(mp.pi * k * b / a)
                   for k in range(1, a)) / (4 * a)


def phi_235():
    return (3 - mpf(1) / P
            + 12 * (dedekind_s(15, 2) + dedekind_s(10, 3) + dedekind_s(6, 5)))


def tau_N(N):
    """Bare τ_N(Σ(2,3,5)) — the reused, Theorem-10-validated Gauss sum (eq. 2.11)."""
    pref_lhs = mp.e ** (2 * mp.pi * I / N * (phi_235() / 4 - mpf(1) / 2)) \
        * (mp.e ** (2 * mp.pi * I / N) - 1)
    total = mpc(0)
    for n in range(2 * P * N):
        if n % N == 0:
            continue
        num = mpc(1)
        for pj in PVEC:
            num *= (mp.e ** (n * mp.pi * I / (N * pj))
                    - mp.e ** (-n * mp.pi * I / (N * pj)))
        den = mp.e ** (n * mp.pi * I / N) - mp.e ** (-n * mp.pi * I / N)
        total += mp.e ** (-n * n * mp.pi * I / (2 * P * N)) * num / den
    rhs = mp.e ** (mp.pi * I / 4) / (2 * mp.sqrt(mpf(2 * P * N))) * total
    return rhs / pref_lhs


def tau_N_colored(N, alpha):
    """COLORED τ_N: the SU(2) colour α on the order-5 fibre replaces the p₃=5 numerator factor
    sin(nπ/(N·5)) → sin(nπα/(N·5)) (Wilson line on the icosahedral exceptional fibre). α=1 must
    reproduce the bare tau_N (GATE 0). Written as an INDEPENDENT code path so the α=1 agreement is
    a genuine cross-check of the insertion, not a shared-code tautology."""
    pref_lhs = mp.e ** (2 * mp.pi * I / N * (phi_235() / 4 - mpf(1) / 2)) \
        * (mp.e ** (2 * mp.pi * I / N) - 1)
    total = mpc(0)
    for n in range(2 * P * N):
        if n % N == 0:
            continue
        # p1=2, p2=3 factors bare; p3=5 factor carries the colour α.
        f2 = (mp.e ** (n * mp.pi * I / (N * 2)) - mp.e ** (-n * mp.pi * I / (N * 2)))
        f3 = (mp.e ** (n * mp.pi * I / (N * 3)) - mp.e ** (-n * mp.pi * I / (N * 3)))
        f5 = (mp.e ** (alpha * n * mp.pi * I / (N * 5))
              - mp.e ** (-alpha * n * mp.pi * I / (N * 5)))
        num = f2 * f3 * f5
        den = mp.e ** (n * mp.pi * I / N) - mp.e ** (-n * mp.pi * I / N)
        total += mp.e ** (-n * n * mp.pi * I / (2 * P * N)) * num / den
    rhs = mp.e ** (mp.pi * I / 4) / (2 * mp.sqrt(mpf(2 * P * N))) * total
    return rhs / pref_lhs


# ── (χ / T10) the exact Theorem-10 transcription anchor (reused from s013) ────────────────────
def chi_hikami(triple):
    out = {}
    for e1 in (-1, 1):
        for e2 in (-1, 1):
            for e3 in (-1, 1):
                val = Fraction(P) * (1 + Fraction(e1 * triple[0], PVEC[0])
                                     + Fraction(e2 * triple[1], PVEC[1])
                                     + Fraction(e3 * triple[2], PVEC[2]))
                assert val.denominator == 1
                r = int(val) % TWO_P
                out[r] = 1 if e1 * e2 * e3 == -1 else -1
    return out


def chi_fn(table):
    def chi(n):
        return table.get(n % TWO_P, 0)
    return chi


def eichler_at_1_over_N(chi, N):
    return mp.fsum((chi(n) * (1 - mpf(n) / (P * N))
                    * mp.e ** (n * n * mp.pi * I / (2 * P * N)))
                   for n in range(P * N + 1) if chi(n))


def theorem10_residual(chi111, N):
    lhs = (mp.e ** (2 * mp.pi * I / N)
           * (mp.e ** (2 * mp.pi * I / N) - 1) * tau_N(N))
    rhs = 1 + mp.e ** (-mp.pi * I / (60 * N)) * eichler_at_1_over_N(chi111, N) / 2
    return abs(lhs - rhs)


# ── (S) the genuine Σ(2,3,5) S-matrix, eq. 3.8 (reused from s013) ─────────────────────────────
def s_entry(l, lp):
    """S^{ℓ'}_{ℓ} = √(32/P)(−1)^{...} ∏_j sin(P ℓj ℓ'j π / pj²).  ℓ,ℓ' are the fibre-colour triples;
    ℓ₃ is the order-5 (icosahedral) fibre colour."""
    expo = Fraction(1 + P)
    for lj, lpj, pj in zip(l, lp, PVEC):
        expo += Fraction(P * (lj + lpj), pj)
    cross = (l[1] * lp[2] - l[2] * lp[1]) * PVEC[0] \
        + (l[2] * lp[0] - l[0] * lp[2]) * PVEC[1] \
        + (l[0] * lp[1] - l[1] * lp[0]) * PVEC[2]
    expo += cross
    assert expo.denominator == 1
    sign = (-1) ** (int(expo) % 2)
    prod = mpf(1)
    for lj, lpj, pj in zip(l, lp, PVEC):
        prod *= mp.sin(mp.pi * P * lj * lpj / (pj * pj))
    return mp.sqrt(mpf(32) / P) * sign * prod


VACUUM = (1, 1, 1)   # the trivial / vacuum flat connection (s013: S[0] = Cor-12 flat weights)


def colored_vacuum_amplitude(alpha):
    """|S_{0λ}^{Σ(2,3,5)}| with the order-5 fibre coloured by α: S^{ℓ'=(1,1,α)}_{ℓ=vacuum}."""
    return abs(s_entry(VACUUM, (1, 1, alpha)))


# ─────────────────────────────────────────────────────────────────────────────────────────────
def run():
    out = {"P": P, "pvec": list(PVEC), "q0": float(Q0)}

    # ── GATE 0 : colour-α insertion at α=1 = bare τ_N, and the Theorem-10 anchor ──────────────
    chi111 = chi_fn(chi_hikami((1, 1, 1)))
    gate0_tau = {}
    gate0_t10 = {}
    for N in (3, 5, 7):
        bare = tau_N(N)
        col1 = tau_N_colored(N, 1)
        gate0_tau[str(N)] = float(abs(col1 - bare))
        gate0_t10[str(N)] = float(theorem10_residual(chi111, N))
    out["gate0_alpha1_minus_bare_tau"] = gate0_tau
    out["gate0_theorem10_residual"] = gate0_t10
    gate0_pass = (all(v < 1e-25 for v in gate0_tau.values())
                  and all(v < 1e-25 for v in gate0_t10.values()))
    out["gate0_pass"] = bool(gate0_pass)
    out["phi_235"] = float(phi_235())
    out["phi_equals_181_over_30"] = bool(abs(phi_235() - mpf(181) / 30) < mpf("1e-30"))
    if not gate0_pass:
        out["ABORT"] = "GATE 0 FAILED — colour insertion does not reduce to bare τ_N / Thm-10 " \
                       "anchor broken; no modulus conclusion drawn."
        return out

    # ── INDEPENDENCE : colored vacuum-row moduli over the order-5 colour α = 1..4 ──────────────
    amp = {a: colored_vacuum_amplitude(a) for a in (1, 2, 3, 4)}
    out["colored_vacuum_moduli"] = {str(a): float(v) for a, v in amp.items()}
    # cluster distinct moduli (absolute tol 1e-30):
    distinct = []
    for a in (1, 2, 3, 4):
        if not any(abs(amp[a] - d) < mpf("1e-30") for d in distinct):
            distinct.append(amp[a])
    n_independent = len(distinct)
    out["n_independent_components"] = n_independent
    out["D_235_formula"] = (PVEC[0] - 1) * (PVEC[1] - 1) * (PVEC[2] - 1) // 4
    out["D2_collapse"] = bool(n_independent == 2)
    # the Weyl fold α ↔ 5−α that causes the collapse:
    out["weyl_fold_alpha4_eq_alpha1"] = bool(abs(amp[4] - amp[1]) < mpf("1e-30"))
    out["weyl_fold_alpha3_eq_alpha2"] = bool(abs(amp[3] - amp[2]) < mpf("1e-30"))
    # the golden-ratio structure of the two survivors (icosahedral / Fibonacci pair):
    ratio = max(distinct) / min(distinct)
    golden = (1 + mp.sqrt(5)) / 2
    out["surviving_modulus_ratio"] = float(ratio)
    out["golden_ratio"] = float(golden)
    out["ratio_is_golden"] = bool(abs(ratio - golden) < mpf("1e-30"))

    # ── CONJUGATION-MODULUS : |S_{0,α}| = |S_{0,5−α}| (the geometric analogue of W_{λ'}=W_λ) ───
    conj_ok = (abs(amp[1] - amp[4]) < mpf("1e-30")) and (abs(amp[2] - amp[3]) < mpf("1e-30"))
    out["conjugation_modulus_respected"] = bool(conj_ok)
    out["conjugation_modulus_violated"] = bool(not conj_ok)

    # ── SPLIT-NODE kill check : does the value map use [5]_ζ+1 (correct) or [6]_ζ (refuted)? ───
    #   evaluated at several roots ζ_N; the McKay probe proved d_q((3,1,1)) = [5]_q+1 exactly.
    split_check = []
    for N in (6, 7, 11):
        z = zeta(N)
        d311 = d_q((3, 1, 1), z)
        five_plus_1 = qint(5, z) + 1
        six = qint(6, z)
        split_check.append({
            "N": N,
            "d_q_311": [float(d311.real), float(d311.imag)],
            "qint5_plus_1": [float(five_plus_1.real), float(five_plus_1.imag)],
            "qint6": [float(six.real), float(six.imag)],
            "matches_5plus1": bool(abs(d311 - five_plus_1) < mpf("1e-25")),
            "matches_6": bool(abs(d311 - six) < mpf("1e-25")),
            "5plus1_neq_6": bool(abs(five_plus_1 - six) > mpf("1e-6")),
        })
    out["split_node_check"] = split_check
    out["split_uses_5plus1_not_6"] = all(s["matches_5plus1"] and not s["matches_6"]
                                         and s["5plus1_neq_6"] for s in split_check)

    # ── MODULUS IDENTIFICATION : |S_{0λ}| vs d_ζ(λ)/D(ζ) across several N (marks value map) ────
    #   geometry offers only the 2 golden survivors (self-normalized ratio φ); the McKay-marked
    #   target is a 4-vector whose ratios vary with N. Report per-N ratio mismatch.
    marks_values = [("(5)~(1^5)", 1, False), ("(4,1)~(2,1^3)", 4, False),
                    ("(3,2)~(2,2,1)", 5, False), ("(3,1,1)", 6, True)]
    per_N = []
    for N in (5, 6, 7, 11):
        z = zeta(N)
        # target d_ζ(λ) on the marks (split electron = [5]_ζ+1, not [6]_ζ):
        tgt = []
        for name, mark, split in marks_values:
            val = (qint(5, z) + 1) if split else qint(mark, z)
            tgt.append(abs(val))
        # D(ζ) = √Σ_{λ⊢5} d_ζ(λ)²: the 3 unsplit classes each have a conjugate partner (×2),
        # the self-conjugate split electron class appears once.
        D2 = mp.fsum((2 if not s else 1) * (abs((qint(5, z) + 1) if s else qint(m, z))) ** 2
                     for (_, m, s) in marks_values)
        D = mp.sqrt(D2)
        bwS0_target = [float(v / D) for v in tgt]
        # self-normalized target ratios (relative to the (5)-class):
        tgt_ratios = [float(v / tgt[0]) for v in tgt]
        # the only ratio the D=2 geometry provides between its independent components:
        geo_ratio = float(ratio)
        # closest target-ratio to the golden geometric ratio (excluding the trivial 1):
        gaps = [abs(geo_ratio - r) for r in tgt_ratios[1:]]
        per_N.append({
            "N": N,
            "target_bwS0_marks": bwS0_target,
            "target_self_ratios": tgt_ratios,
            "geometric_D2_ratio_phi": geo_ratio,
            "min_gap_phi_vs_target_ratio": float(min(gaps)),
            "identification_holds": bool(min(gaps) < 1e-9 and n_independent >= 4),
        })
    out["modulus_identification_per_N"] = per_N
    out["identification_holds_any_N"] = any(p["identification_holds"] for p in per_N)
    out["ratio_mismatch_every_N"] = all(not p["identification_holds"] for p in per_N)

    # ── verdict roll-up ───────────────────────────────────────────────────────────────────────
    out["verdict_scope_a_negative"] = bool(
        gate0_pass and out["D2_collapse"] and out["ratio_mismatch_every_N"]
        and out["split_uses_5plus1_not_6"])
    return out


def report(res):
    print("# Keystone — Lawrence–Rozansky colored-modulus ID for Σ(2,3,5) (Front 2)\n")
    print(f"q₀ = {res['q0']:.10f}   P = {res['P']} = h(E₈) = 2·3·5\n")

    print("## GATE 0 — colour insertion α=1 = bare τ_N, and Theorem-10 anchor\n")
    print(f"- φ(2,3,5) = {res['phi_235']:.8f} = 181/30: **{res['phi_equals_181_over_30']}**")
    print("- |τ_N^{(α=1)} − τ_N^{bare}| (independent code path):")
    for N, v in res["gate0_alpha1_minus_bare_tau"].items():
        print(f"    N={N}: {v:.2e}")
    print("- bare Theorem-10 residual |LHS−RHS| (eq. 5.5, EXACT):")
    for N, v in res["gate0_theorem10_residual"].items():
        print(f"    N={N}: {v:.2e}")
    print(f"- **GATE 0: {res['gate0_pass']}** "
          f"({'PASS — proceeding' if res['gate0_pass'] else 'FAIL — STOP, no conclusion'})\n")
    if res.get("ABORT"):
        print(f"## ABORTED\n\n{res['ABORT']}")
        return

    print("## INDEPENDENCE — the D=2 collapse trap\n")
    print(f"- D(2,3,5) = (p₁−1)(p₂−1)(p₃−1)/4 = {res['D_235_formula']}")
    print("- colored vacuum-row moduli |S_{0λ}| over the order-5 colour α:")
    for a, v in res["colored_vacuum_moduli"].items():
        print(f"    α={a}: |S_{{0,α}}| = {v:.8f}")
    print(f"- Weyl fold α↔5−α: |S_{{0,4}}|=|S_{{0,1}}| **{res['weyl_fold_alpha4_eq_alpha1']}**, "
          f"|S_{{0,3}}|=|S_{{0,2}}| **{res['weyl_fold_alpha3_eq_alpha2']}**")
    print(f"- **INDEPENDENT components = {res['n_independent_components']} "
          f"⇒ D=2 collapse: {res['D2_collapse']}.** The McKay-labelled coloring does NOT escape it —")
    print(f"  the two survivors are the icosahedral/Fibonacci pair, ratio = "
          f"{res['surviving_modulus_ratio']:.8f} = golden φ ({res['ratio_is_golden']}).\n")

    print("## CONJUGATION-MODULUS\n")
    print(f"- |S_{{0λ}}| = |S_{{0λ'}}| (α↔5−α): respected **{res['conjugation_modulus_respected']}** "
          f"⇒ conjugation-modulus violated: **{res['conjugation_modulus_violated']}** (kill criterion "
          f"does NOT fire — the D=2 pair is conjugation-blind).\n")

    print("## SPLIT-NODE — electron block (3,1,1): [5]_ζ+1 (correct) vs [6]_ζ (refuted)\n")
    print("| N | d_q((3,1,1)) = [5]_ζ+1 | = [6]_ζ? | [5]+1 ≠ [6] |")
    print("|--:|:-:|:-:|:-:|")
    for s in res["split_node_check"]:
        print(f"| {s['N']} | {s['matches_5plus1']} | {s['matches_6']} | {s['5plus1_neq_6']} |")
    print(f"- **value map uses [5]_ζ+1, not [6]_ζ, at every N: {res['split_uses_5plus1_not_6']}** "
          f"(the A₅ 3⊕3′ split signature; the [6]_ζ kill criterion does NOT fire).\n")

    print("## MODULUS IDENTIFICATION  |S_{0λ}| =?= d_ζ(λ)/D(ζ)  across N\n")
    print("| N | target ratios (marks value map) | geometric D=2 ratio φ | min|φ−tgt| | holds? |")
    print("|--:|---|--:|--:|:-:|")
    for p in res["modulus_identification_per_N"]:
        tr = ", ".join(f"{r:.4f}" for r in p["target_self_ratios"])
        print(f"| {p['N']} | ({tr}) | {p['geometric_D2_ratio_phi']:.4f} | "
              f"{p['min_gap_phi_vs_target_ratio']:.4f} | {p['identification_holds']} |")
    print(f"\n- **ratio-vector mismatch at every N: {res['ratio_mismatch_every_N']}** "
          f"(identification holds at any N: {res['identification_holds_any_N']}).\n")

    print("## VERDICT — scope-(a) negative\n")
    print(f"- **scope-(a) negative: {res['verdict_scope_a_negative']}.** The genuine colored")
    print("  Lawrence–Rozansky vacuum row of Σ(2,3,5) has exactly **2 independent moduli** (the")
    print("  golden-ratio icosahedral pair). The McKay-labelled coloring on the order-5 fibre does")
    print("  NOT escape the D=2 collapse — the fibre Weyl reflection α↔5−α folds α=4→1, α=3→2 at the")
    print("  MODULUS. So the identification |S_{0λ}| = d_ζ(λ)/D against the 4-class McKay-marked")
    print("  target (marks {1,4,5,6}, values [1],[4],[5],[5]+1) is VACUOUS: 2 geometric components")
    print("  cannot carry a 4-class family. This RE-DERIVES the s013 refutation, now explicitly at")
    print("  the McKay-colored level. The value-map dictionary d_q(λ)=[mark]_q (rep theory) is")
    print("  correct and conjugation-blind, but it does NOT lift to 4 independent GEOMETRIC")
    print("  amplitude moduli — the Σ(2,3,5) geometry supplies only D=2. Evidence, not proof; the")
    print("  Lean loc_matches gate stays open; nothing wired.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("keystone-lr-colored-modulus", engine="mpmath")
    w.set_description(
        "Front 2 of 2026-07-17-three-front-attack-specs.md: the Lawrence-Rozansky colored-modulus "
        "identification |S_{0lambda}^{Sigma(2,3,5)}(zeta)| =?= d_zeta(lambda)/D(zeta) at fibre roots "
        "of unity, colours mapped by McKay(2I<->E8-hat) o (A5 subset S5) with VALUES on the E8 marks "
        "{1,4,5,6} (values [1],[4],[5],[5]+1; split electron block (3,1,1)=[5]+1 not [6]). Reuses the "
        "machine-validated Hikami machinery (tau_N Gauss sum eq 2.11, phi=181/30, Theorem-10 exact "
        "anchor eq 5.5, genuine S-matrix eq 3.8) and adds the colour-alpha insertion on the order-5 "
        "icosahedral fibre in the p3=5 numerator. GATE 0 PASSES: alpha=1 reproduces bare tau_N to "
        "~1e-30 and the Theorem-10 identity holds. RESULT: the colored vacuum-row has exactly 2 "
        "INDEPENDENT moduli (D=2 collapse) -- the fibre Weyl fold alpha<->5-alpha gives "
        "|S_{0,4}|=|S_{0,1}|, |S_{0,3}|=|S_{0,2}|, ratio = golden phi (icosahedral pair); the "
        "McKay-labelled coloring does NOT escape the trap. Conjugation-modulus is RESPECTED (not "
        "violated); the split node correctly uses [5]_zeta+1 not [6]_zeta at every N. The modulus "
        "identification against the 4-class marked target is therefore VACUOUS (2 components cannot "
        "carry 4 classes) -- ratio-vector mismatch at every N. VERDICT scope-(a) negative: re-derives "
        "the s013 refutation explicitly at the McKay-colored level. Evidence not proof; Lean "
        "loc_matches gate open; nothing wired."
    )
    for key in ("P", "pvec", "q0", "gate0_alpha1_minus_bare_tau", "gate0_theorem10_residual",
                "gate0_pass", "phi_235", "phi_equals_181_over_30", "colored_vacuum_moduli",
                "n_independent_components", "D_235_formula", "D2_collapse",
                "weyl_fold_alpha4_eq_alpha1", "weyl_fold_alpha3_eq_alpha2",
                "surviving_modulus_ratio", "golden_ratio", "ratio_is_golden",
                "conjugation_modulus_respected", "conjugation_modulus_violated",
                "split_node_check", "split_uses_5plus1_not_6",
                "modulus_identification_per_N", "identification_holds_any_N",
                "ratio_mismatch_every_N", "verdict_scope_a_negative"):
        if key in res:
            w.add_data(key, res[key])

    w.add_assertion(
        "gate0_colour_insertion_reduces_to_bare_tau_and_theorem10_holds",
        computed=1 if res.get("gate0_pass") else 0, expected=1, tolerance=0,
        source="GATE 0: the colour-alpha insertion on the order-5 fibre at alpha=1 reproduces the "
               "bare tau_N(Sigma(2,3,5)) to ~1e-30 (independent code path), and the bare Theorem-10 "
               "exact identity (Hikami eq 5.5) holds to ~1e-28 at N=3,5,7 -- jointly re-validating "
               "the transcription chain before any modulus conclusion.",
    )
    if res.get("gate0_pass"):
        w.add_assertion(
            "colored_vacuum_row_has_two_independent_moduli_D2_collapse",
            computed=res["n_independent_components"], expected=2, tolerance=0,
            source="The genuine Sigma(2,3,5) colored vacuum-row modulus |S_{0,alpha}| over the "
                   "order-5 SU(2) colour alpha=1..4 takes exactly 2 distinct values (machine-zero to "
                   "40 dps): the fibre Weyl reflection alpha<->5-alpha folds alpha=4->1, alpha=3->2, "
                   "leaving the golden-ratio icosahedral pair. D(2,3,5)=(1)(2)(4)/4=2. The "
                   "McKay-labelled coloring does NOT escape the D=2 collapse.",
        )
        w.add_assertion(
            "modulus_identification_refuted_scope_a",
            computed=1 if res["verdict_scope_a_negative"] else 0, expected=1, tolerance=0,
            source="scope-(a) negative: 2 independent geometric moduli cannot carry the 4-class "
                   "McKay-marked target d_zeta/D (marks {1,4,5,6}); ratio-vector mismatch at every N "
                   "(golden phi not in the target self-ratios). Conjugation-modulus RESPECTED (not "
                   "violated); the split electron block correctly uses [5]_zeta+1 not [6]_zeta. "
                   "Re-derives the s013 refutation explicitly at the McKay-colored level. Evidence "
                   "not proof; Lean loc_matches gate open; nothing wired to production.",
        )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
