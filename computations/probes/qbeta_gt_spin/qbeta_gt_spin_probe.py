#!/usr/bin/env python3
"""qbeta_gt_spin_probe — the Gamow–Teller (spin) part of the β amplitude, λ(q).

Bean qou-99qc. Pre-registered in PREREGISTRATION.md (commit 43739c0575) before this file was run.
Lean twin: QOU/QuarkState/GamowTellerSpin.lean (sorry-free).

Exact sympy over Q(q) for every amplitude; mpmath at 70 dps, proton q0, for numbers. No float64
in any computed value. The PDG value |λ| = 1.2754 enters only in the comparison block.

Premises (PREREGISTRATION.md):
  (A) factorised strand space V_iso ⊗ V_spin, isospin Jimbo-braided at q, spin by the swap P;
  (W) unfactorised strand space C^4 = {u↑,u↓,d↑,d↓} with the U_q(gl_4) Jimbo crossing, which
      needs an ORDERING of the four labels.
Inherited from #8638: lepton = fourth strand carrying a copy of the strand space, ν = u, e⁻ = d;
β block = leftward positive passage σ1σ2σ3 restricted to n⊗ν → e⁻⊗p.
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
from qou_substrate.precision import fmt  # noqa: E402

DPS = 70
mp.mp.dps = DPS
T0 = time.time()
ASSERTS: list = []
FAILED: list = []

q = sp.symbols("q", positive=True)
h = q - 1 / q
UP, DN = 0, 1
U, D = "u", "d"


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def zero(e):
    return sp.simplify(sp.together(e)) == 0


# ------------------------------------------------------------------ vectors as dicts on label tuples
def add(v, k, c):
    if c != 0:
        v[k] = v.get(k, 0) + c


def apply_cross(v, i, cross):
    """Apply the crossing on positions (i, i+1) to the vector v."""
    out = {}
    for k, c in v.items():
        for (x, y), cc in cross(k[i], k[i + 1]):
            add(out, k[:i] + (x, y) + k[i + 2:], c * cc)
    return {k: sp.expand(c) for k, c in out.items() if sp.expand(c) != 0}


def jimbo(rank):
    """Jimbo Ř on a pair of labels, ordering given by rank: aa→q aa; a<b: ab→ba; a>b: ab→ba + h ab."""
    def cross(a, b):
        if a == b:
            return [((a, b), q)]
        if rank(a) < rank(b):
            return [((b, a), 1)]
        return [((b, a), 1), ((a, b), h)]
    return cross


def cross_A(a, b):
    """Premise (A): label = (iso, spin). Jimbo on iso, swap P on spin (spin rides on the strand)."""
    (ia, sa), (ib, sb) = a, b
    out = []
    for (x, y), c in jimbo(lambda t: 0 if t == U else 1)(ia, ib):
        out.append((((x, sb), (y, sa)), c))
    return out


def passage(v, cross):
    """Leftward positive passage σ1σ2σ3 (σ3 applied first)."""
    for i in (2, 1, 0):
        v = apply_cross(v, i, cross)
    return v


def inner(v, w):
    return sp.expand(sum(c * w.get(k, 0) for k, c in v.items()))


# ------------------------------------------------------------------ classical SU(6) nucleon (choice C-SU6)
def spin_ops_classical():
    """Total spin S² (classical, q-independent) on 3-quark states with labels (iso, spin)."""
    def s_dot_s(v, i, j):
        out = {}
        for k, c in v.items():
            (ii, si), (ij, sj) = k[i], k[j]
            # s_i·s_j = ½ P_ij^spin − ¼
            kk = list(k)
            kk[i], kk[j] = (ii, sj), (ij, si)
            add(out, tuple(kk), c / 2)
            add(out, k, -c / 4)
        return out

    def S2(v):
        out = {k: sp.Rational(9, 4) * c for k, c in v.items()}  # Σ s_i² = 3·¾
        for i, j in ((0, 1), (0, 2), (1, 2)):
            for k, c in s_dot_s(v, i, j).items():
                add(out, k, 2 * c)
        return out
    return S2


def sym3(k):
    out = {}
    for p in itertools.permutations(range(3)):
        add(out, tuple(k[p[t]] for t in range(3)), 1)
    return out


def lower_spin(v):
    """Classical total S⁻ on 3-quark states (Condon–Shortley phase)."""
    out = {}
    for k, c in v.items():
        for i in range(3):
            f, s_ = k[i]
            if s_ == UP:
                kk = list(k)
                kk[i] = (f, DN)
                add(out, tuple(kk), c)
    nrm = sp.sqrt(sum(c ** 2 for c in out.values()))
    return {k: sp.nsimplify(c / nrm) for k, c in out.items() if c != 0}


def nucleon(iso_major_flavour, spin):
    if spin == DN:
        return lower_spin(nucleon(iso_major_flavour, UP))
    """SU(6) nucleon with S = ½, spin projection `spin`: S = ½ vector in the symmetric
    weight space (flavour multiset fixed). `iso_major_flavour` = 'p' (uud) or 'n' (udd)."""
    two, one = (U, D) if iso_major_flavour == "p" else (D, U)
    s, sbar = spin, 1 - spin
    b1 = sym3(((two, s), (two, s), (one, sbar)))
    b2 = sym3(((two, s), (two, sbar), (one, s)))
    S2 = spin_ops_classical()
    a, b = sp.symbols("a b")
    vec = {}
    for k, c in b1.items():
        add(vec, k, a * c)
    for k, c in b2.items():
        add(vec, k, b * c)
    s2v = S2(vec)
    eqs = [sp.expand(s2v.get(k, 0) - sp.Rational(3, 4) * vec.get(k, 0)) for k in set(vec) | set(s2v)]
    sol = sp.solve([e for e in eqs if e != 0], [a, b], dict=True)
    # one-parameter family; fix b = 1 then normalise
    sol = [s_ for s_ in sol if s_] or [{}]
    vv = {k: sp.simplify(c.subs(sol[0]).subs({a: 1, b: 1}) if b in sol[0] else c.subs(sol[0]).subs({b: 1}))
          for k, c in vec.items()}
    nrm = sp.sqrt(sum(c ** 2 for c in vv.values()))
    return {k: sp.nsimplify(c / nrm) for k, c in vv.items() if c != 0}


SIGMA = [
    sp.Matrix([[1, 0], [0, 1]]),
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]


def fierz(A):
    """A[(sp, se), (sn, snu)] → 4×4 coefficients c[μ][ν] of σ^μ_N ⊗ σ^ν_ℓ."""
    c = [[0] * 4 for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            tot = 0
            for spp, se, sn, snu in itertools.product((0, 1), repeat=4):
                tot += sp.conjugate(SIGMA[mu][spp, sn] * SIGMA[nu][se, snu]) * A[(spp, se), (sn, snu)]
            c[mu][nu] = sp.simplify(sp.together(tot / 4))
    return c


def beta_block(cross, lab):
    """A[(sp,se),(sn,snu)] = <e_se ⊗ p_sp | σ1σ2σ3 | n_sn ⊗ ν_snu> with nucleon states C-SU6."""
    A = {}
    nst = {s: nucleon("n", s) for s in (0, 1)}
    pst = {s: nucleon("p", s) for s in (0, 1)}
    for sn, snu in itertools.product((0, 1), repeat=2):
        vin = {tuple(lab(x) for x in k) + (lab((U, snu)),): c for k, c in nst[sn].items()}
        vout = passage(vin, cross)
        for spp, se in itertools.product((0, 1), repeat=2):
            bra = {(lab((D, se)),) + tuple(lab(x) for x in k): c for k, c in pst[spp].items()}
            A[(spp, se), (sn, snu)] = inner(bra, vout)
    return A


def summarise(c):
    c0 = c[0][0]
    diag = [c[k][k] for k in (1, 2, 3)]
    off = [c[m][n] for m in range(4) for n in range(4) if m != n]
    iso = all(zero(d - diag[0]) for d in diag)
    offzero = all(zero(o) for o in off)
    R = sp.simplify(sum(sp.Abs(c[m][n]) ** 2 for m in range(4) for n in range(4)) / sp.Abs(c0) ** 2) if c0 != 0 else None
    lam = sp.simplify(diag[0] / c0) if (iso and c0 != 0) else None
    lam_perp = sp.factor(diag[0] / c0) if c0 != 0 else None
    lam_z = sp.factor(diag[2] / c0) if c0 != 0 else None
    return {"c0": c0, "cdiag": diag, "isotropic": iso, "offdiag_zero": offzero, "lambda": lam, "R": R,
            "lambda_perp": lam_perp, "lambda_z": lam_z}


# ------------------------------------------------------------------ single crossing, premise W, all orderings
LABELS4 = [(U, UP), (U, DN), (D, UP), (D, DN)]


def single_cross_block(order):
    rank = {lab: order.index(lab) for lab in LABELS4}
    cr = jimbo(lambda x: rank[x])
    A = {}
    for s, s2 in itertools.product((0, 1), repeat=2):
        # strand-tracked: P·Ř; input quark d_s left, lepton ν_s2 = u_s2 right
        out = {}
        for (x, y), c in cr((D, s), (U, s2)):
            add(out, (y, x), c)  # P relabels by strand
        for t, t2 in itertools.product((0, 1), repeat=2):
            A[(t, t2), (s, s2)] = sp.expand(out.get(((U, t), (D, t2)), 0))
    return A


def classify(order):
    c = fierz(single_cross_block(order))
    return c, summarise(c)


def main():
    log("premise (A): factorised iso ⊗ spin, spin carried by the swap")
    labA = lambda x: x  # noqa: E731
    cA = fierz(beta_block(cross_A, labA))
    sA = summarise(cA)
    log(f"  c0 = {sA['c0']}, c_k = {sA['cdiag']}")
    check("PA1_fermi_only", all(zero(cA[m][n]) for m in range(4) for n in range(4) if (m, n) != (0, 0))
          and not zero(sA["c0"]), "under (A) every σ^μ⊗σ^ν coefficient except c00 vanishes: λ ≡ 0")
    lim_A = sp.limit(sA["c0"] / h, q, 1)
    check("PA1_c0_fermi_limit", sp.Abs(lim_A) == 1,
          f"c00 = {sp.factor(sA['c0'])}; c00/h → {lim_A} at q → 1 (classical M_F = 1, sign = state phase)")

    log("premise (W): single crossing, all 24 orderings of {u↑,u↓,d↑,d↓}")
    classes = {"full_pos": [], "none_pos": [], "partial": []}
    single = {}
    for order in itertools.permutations(LABELS4):
        c, s = classify(order)
        key = "".join(f"{f}{'↑' if sp_ == UP else '↓'}" for f, sp_ in order)
        nz = [(m, n) for m in range(4) for n in range(4) if not zero(c[m][n])]
        if s["isotropic"] and s["offdiag_zero"] and not zero(s["c0"]):
            classes["full_pos"].append(key)
            single[key] = s
        elif not nz:
            classes["none_pos"].append(key)
        else:
            classes["partial"].append(key)
    log(f"  full rotation-invariant current in σ: {classes['full_pos']}")
    check("PW2_counts", (len(classes["full_pos"]), len(classes["none_pos"]), len(classes["partial"])) == (4, 4, 16),
          f"full/none/partial = {len(classes['full_pos'])}/{len(classes['none_pos'])}/{len(classes['partial'])}")
    check("PW2_full_is_u_first", all(k[0] == "u" and k[2] == "u" for k in classes["full_pos"]),
          "the 4 full orderings are exactly those with both u states first")
    lam_q = {k: s["lambda"] for k, s in single.items()}
    check("PW1_quark_lambda_one", all(zero(v - 1) for v in lam_q.values()),
          "quark level: c0 = c_x = c_y = c_z = h/2, i.e. h·P_spin = (h/2)(1 + σ⃗·σ⃗), λ_q = 1 for all q")
    check("PW1_c0_half_h", all(zero(s["c0"] - h / 2) for s in single.values()), "c0 = h/2")

    # a representative partial ordering (spin-major) for the record
    cpm, spm = classify(((U, UP), (D, UP), (U, DN), (D, DN)))
    partial_record = {f"c{m}{n}": str(cpm[m][n]) for m in range(4) for n in range(4) if not zero(cpm[m][n])}
    log(f"  spin-major u↑d↑u↓d↓ single crossing: {partial_record}")

    log("premise (W), iso-major u↑u↓d↑d↓, full passage with C-SU6 nucleons (labelled CHOICE)")
    order = LABELS4
    rank = {lab: order.index(lab) for lab in LABELS4}
    cW = fierz(beta_block(jimbo(lambda x: rank[x]), lambda x: x))
    sW = summarise(cW)
    lamN = sp.factor(sW["lambda"]) if sW["lambda"] is not None else None
    cWf = {f"c{m}{n}": sp.factor(cW[m][n]) for m in range(4) for n in range(4) if not zero(cW[m][n])}
    log(f"  isotropic={sW['isotropic']} offdiag_zero={sW['offdiag_zero']}")
    for k_, v_ in cWf.items():
        log(f"    {k_} = {v_}")
    lam_perp, lam_z = sW["lambda_perp"], sW["lambda_z"]
    RN = sp.factor(sW["R"].rewrite(sp.Piecewise)) if False else None
    lp1, lz1 = sp.limit(lam_perp, q, 1), sp.limit(lam_z, q, 1)
    check("PW3_su6_limit", sp.Abs(lp1) == sp.Rational(5, 3) and lz1 == lp1,
          f"q → 1: λ_⊥ = {lp1}, λ_z = {lz1} (SU(6) |g_A| = 5/3, isotropic)")
    check("PW3_anisotropic_at_q", not sW["isotropic"] and not sW["offdiag_zero"],
          "at generic q the C-SU6 nucleon block is NOT rotation-invariant: λ_⊥ ≠ λ_z and an "
          "antisymmetric c12 = −c21 term (σ_N × σ_ℓ)_z appears at O((q−1)²)")
    per_order = {}
    for k in classes["full_pos"]:
        o = tuple(((k[2 * i]), UP if k[2 * i + 1] == "↑" else DN) for i in range(4))
        rk = {lab: o.index(lab) for lab in LABELS4}
        sk = summarise(fierz(beta_block(jimbo(lambda x, rk=rk: rk[x]), lambda x: x)))
        per_order[k] = {"lambda_perp": sk["lambda_perp"], "lambda_z": sk["lambda_z"],
                        "lim_perp": sp.limit(sk["lambda_perp"], q, 1), "lim_z": sp.limit(sk["lambda_z"], q, 1)}
        log(f"    ordering {k}: λ_⊥ = {sk['lambda_perp']}, λ_z = {sk['lambda_z']}")
    distinct = len({str(sp.simplify(v["lambda_perp"])) for v in per_order.values()})
    check("PW3_all_orderings_su6_limit", all(sp.Abs(v["lim_perp"]) == sp.Rational(5, 3) and v["lim_z"] == v["lim_perp"]
                                              for v in per_order.values()),
          "every iso-major ordering gives |λ| → 5/3 at q → 1")
    check("PW3_ordering_dependence_recorded", distinct > 1,
          f"NOT predicted: the within-u / within-d order changes λ at q ≠ 1 ({distinct} distinct λ_⊥(q)); "
          "a remaining choice, recorded")

    lamN = lam_perp

    # ---------------------------------------------------------------- numbers at proton q0
    q0 = C.q_at(DPS)
    q0s = sp.Float(mp.nstr(q0, DPS + 5), DPS + 5)

    def ev(e):
        return mp.mpf(str(sp.N(sp.sympify(e).subs(q, q0s), DPS + 5)))
    cq0 = {k_: ev(v_) if "I" not in str(v_) else ev(sp.im(v_)) for k_, v_ in cWf.items()}
    c00 = cq0["c00"]
    lamP_q0, lamZ_q0 = ev(lam_perp), ev(lam_z)
    anti_q0 = cq0.get("c12", mp.mpf(0)) / c00
    RN_q0 = (sum(v_ ** 2 for v_ in cq0.values())) / c00 ** 2
    lamN_q0 = mp.sqrt((RN_q0 - 1) / 3)
    log(f"q0 = {mp.nstr(q0, 25)}; λ_⊥(q0) = {mp.nstr(lamP_q0, 20)}; λ_z(q0) = {mp.nstr(lamZ_q0, 20)}; "
        f"Im c12/c00 = {mp.nstr(anti_q0, 12)}")
    log(f"  rate factor R(q0) = Σ|c|²/|c00|² = {mp.nstr(RN_q0, 20)}; λ_eff = √((R−1)/3) = {mp.nstr(lamN_q0, 20)}")
    lp_at1 = mp.mpf(5) / 3
    per_order_q0 = {k: {"lambda_perp_q": str(v["lambda_perp"]), "lambda_z_q": str(v["lambda_z"]),
                        "lambda_perp_q0": fmt(ev(v["lambda_perp"])), "lambda_z_q0": fmt(ev(v["lambda_z"]))}
                    for k, v in per_order.items()}
    for k, v in per_order_q0.items():
        log(f"  {k}: λ_⊥(q0) = {v['lambda_perp_q0'][:22]}, λ_z(q0) = {v['lambda_z_q0'][:22]}")

    # ---------------------------------------------------------------- comparison only
    lam_pdg = mp.mpf("1.2754")
    comp = {"lambda_pdg_abs": fmt(lam_pdg), "one_plus_3lambda2_pdg": fmt(1 + 3 * lam_pdg ** 2),
            "lambda_eff_q0_vs_pdg_pct": fmt((lamN_q0 - lam_pdg) / lam_pdg * 100),
            "lambda_N_q1_vs_pdg_pct": fmt((lp_at1 - lam_pdg) / lam_pdg * 100),
            "R_q0_vs_pdg_pct": fmt((RN_q0 - (1 + 3 * lam_pdg ** 2)) / (1 + 3 * lam_pdg ** 2) * 100)}
    log(f"comparison: |λ|_PDG = 1.2754; λ_eff(q0) off by {comp['lambda_eff_q0_vs_pdg_pct'][:12]} %")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-gt-spin", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc: Gamow–Teller (spin) sector of the β block. (A) factorised spin: "
                       "λ ≡ 0. (W) U_q(gl4) iso-major: quark-level λ = 1 for all q; nucleon level "
                       "under the labelled C-SU6 nucleon choice. Pre-registered at 43739c0575. "
                       "Not wired to any scorecard.")
    wb.add_parameter("q0", C.Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("lepton_assumption", "fourth strand, copy of the strand space, nu = u, e- = d")
    wb.add_parameter("nucleon_choice_PW3", "C-SU6: classical S=1/2 vector in the symmetric weight space")
    wb.add_data("premise_A", {"c00": str(sA["c0"]), "all_other_coefficients_zero": True,
                              "lambda": "0", "one_plus_3lambda2": "1"})
    wb.add_data("premise_W_single_crossing", {
        "orderings_full_positive": classes["full_pos"], "orderings_none_positive": classes["none_pos"],
        "orderings_partial": classes["partial"], "quark_lambda": "1", "c00": "h/2",
        "spin_major_example": partial_record})
    wb.add_data("premise_W_nucleon_C_SU6", {
        "coefficients_q": {k_: str(v_) for k_, v_ in cWf.items()},
        "lambda_perp_q": str(lam_perp), "lambda_z_q": str(lam_z),
        "lambda_q_to_1": str(lp1), "lambda_perp_q0": fmt(lamP_q0), "lambda_z_q0": fmt(lamZ_q0),
        "Im_c12_over_c00_q0": fmt(anti_q0), "rate_factor_R_q0": fmt(RN_q0),
        "lambda_eff_q0": fmt(lamN_q0), "ordering": "u↑u↓d↑d↓", "per_iso_major_ordering": per_order_q0})
    wb.add_data("comparison", comp)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0", source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
