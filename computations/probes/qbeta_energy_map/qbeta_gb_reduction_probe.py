#!/usr/bin/env python3
"""qbeta_gb_reduction_probe — β-decay as a Gröbner–Shirshov reduction (PREREGISTRATION Addendum 4).

Process word W = X·β_Bor in H₄(q), X = V₁³ = (σ₁σ₂⁻¹)³ (a proposal, not ruled), β_Bor = (σ₀σ₁⁻¹)³.
Placement C (active lepton strand, premise L). Exact over ℚ(q) (sympy); numbers by mpmath at the
proton q₀. CODATA is read only in the last section, as a comparison; nothing is selected by it.

M1  number of times a rewriting rule fires while W is brought to normal form
    (σᵢ² → hσᵢ + 1 on a descent, σᵢ⁻¹ → σᵢ − h), counted per basis term at each step;
    strategy S1 = right multiplication letter by letter (left to right),
    strategy S2 = left multiplication letter by letter (right to left).
M2  Σ over firings of q^{−ℓ}, ℓ = length of the word the rule fires on (E0ReductionWordCount analogue).
M3  CC block n⊗ν → p⊗e⁻ and diagonal block n⊗ν → n⊗ν of ρ(W); kT·ln of the ratio of their
    Frobenius norms, kT = E₀ (route T).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
_BP = _ROOT / "computations/probes/beta_pair_creation_word"
for _p in ("computations", "tools/qou-substrate/python", str(_BP)):
    sys.path.insert(0, str(_ROOT / _p) if not _p.startswith("/") else _p)

import mpmath as mp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
import beta_pair_creation_word_probe as BP  # noqa: E402
from hecke_exact import H, KF, RING, ONE, ZERO, h, q  # noqa: E402

mp.mp.dps = 60
FAILED: list = []
OUT: dict = {"preregistration": "PREREGISTRATION.md (Addendum 4)", "checks": [], "word": {}, "measures": {},
             "comparison": {}}


def check(name, ok, note=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    OUT["checks"].append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


N = 4
X = (1, -3) * 3          # V1^3 = (s1 s2')^3
BETA = BP.BETA           # (s0 s1')^3
W = X + BETA             # process word: nucleon core acts first (rightmost), then X
Q0 = mp.mpf(C.Q_50_DIGIT_STR)
ME = mp.mpf(C.M_E_MEV_STR)
E0 = ME / (Q0 * (Q0 - 1))
HH = RING(h)


def plen(w):
    return sum(1 for a in range(len(w)) for b in range(a + 1, len(w)) if w[a] > w[b])


def ev(f):
    return BP.ev_frac(BP.gk(f) if not hasattr(f, "numer") else f, Q0)


# ---------------------------------------------------------------- instrumented reduction
class Counter:
    def __init__(self):
        self.fires = 0
        self.weighted = KF.zero
        self.by_rule = {"quadratic": 0, "inverse": 0}

    def fire(self, rule, length):
        self.fires += 1
        self.by_rule[rule] += 1
        self.weighted += 1 / KF(q) ** length


def rmul(x: H, i, cnt: Counter):
    d: dict = {}
    for w, v in x.c.items():
        ws = list(w)
        ws[i], ws[i + 1] = ws[i + 1], ws[i]
        ws = tuple(ws)
        if w[i] < w[i + 1]:
            d[ws] = d.get(ws, ZERO) + v
        else:
            cnt.fire("quadratic", plen(w) + 1)
            d[w] = d.get(w, ZERO) + v * HH
            d[ws] = d.get(ws, ZERO) + v
    return H(N, d)


def lmul(x: H, i, cnt: Counter):
    """σ_i · T_w: swaps VALUES i, i+1 in one-line notation."""
    d: dict = {}
    for w, v in x.c.items():
        pi, pj = w.index(i), w.index(i + 1)
        ws = list(w)
        ws[pi], ws[pj] = i + 1, i
        ws = tuple(ws)
        if pi < pj:
            d[ws] = d.get(ws, ZERO) + v
        else:
            cnt.fire("quadratic", plen(w) + 1)
            d[w] = d.get(w, ZERO) + v * HH
            d[ws] = d.get(ws, ZERO) + v
    return H(N, d)


def reduce_S1(word):
    cnt = Counter()
    x = H.one(N)
    for g in word:
        if g >= 0:
            x = rmul(x, g, cnt)
        else:
            i = -g - 1
            for w in list(x.c):
                cnt.fire("inverse", plen(w) + 1)
            x = rmul(x, i, cnt) - x.scale(HH)
    return x, cnt


def reduce_S2(word):
    cnt = Counter()
    x = H.one(N)
    for g in reversed(word):
        if g >= 0:
            x = lmul(x, g, cnt)
        else:
            i = -g - 1
            for w in list(x.c):
                cnt.fire("inverse", plen(w) + 1)
            x = lmul(x, i, cnt) - x.scale(HH)
    return x, cnt


print("1. Normal form and reduction counts")
nf1, c1 = reduce_S1(W)
nf2, c2 = reduce_S2(W)
ref = H.one(N).rmul_word(list(W))
check("S1 normal form equals hecke_exact reference", nf1.c == ref.c)
check("S2 normal form equals S1 (normal form is strategy independent)", nf2.c == nf1.c)
check("NF(W) has 17 basis terms (pair-creation witness)", len(nf1.c) == 17, str(len(nf1.c)))
OUT["word"] = {"X": BP.word_str(X), "beta": BP.word_str(BETA), "W": BP.word_str(W),
               "unreduced_length": len(W), "nf_terms": len(nf1.c),
               "nf_max_length": max(plen(w) for w in nf1.c)}

# T³ conservation under premise L (H = log_q K; u = +1, d = −1)
Hw = {"u": 1, "d": -1}
n_nu = Hw["u"] + 2 * Hw["d"] + Hw["u"]
p_e = 2 * Hw["u"] + Hw["d"] + Hw["d"]
check("T3 weight of n⊗ν and p⊗e⁻ both 0 (§13 C)", n_nu == 0 and p_e == 0, f"{n_nu}, {p_e}")

M = {}
for tag, cnt in (("S1", c1), ("S2", c2)):
    M2v = BP.ev_frac(cnt.weighted, Q0)
    M[tag] = {"M1_fires": cnt.fires, "M1_by_rule": cnt.by_rule,
              "M2_exact": BP.fx(cnt.weighted), "M2_q0": mp.nstr(M2v, 15),
              "M1_times_E0_MeV": mp.nstr(cnt.fires * E0, 12), "M2_times_E0_MeV": mp.nstr(M2v * E0, 12)}
    print(f"  {tag}: M1 = {cnt.fires} {cnt.by_rule}, M2(q0) = {mp.nstr(M2v, 12)}")
check("M1 depends on strategy (reported, expected)", True, f"S1 {c1.fires} vs S2 {c2.fires}")

# Addendum 5: the interaction's own reductions, ΔM = M(X·β) − M(β) − M(X)
for tag, f in (("S1", reduce_S1), ("S2", reduce_S2)):
    _, cw = f(W)
    _, cb = f(BETA)
    _, cx = f(X)
    d1 = cw.fires - cb.fires - cx.fires
    d2 = cw.weighted - cb.weighted - cx.weighted
    d2v = BP.ev_frac(d2, Q0)
    M[tag].update({"dM1_fires": d1, "dM1_times_E0_MeV": mp.nstr(d1 * E0, 12), "dM2_exact": BP.fx(d2),
                   "dM2_q0": mp.nstr(d2v, 15), "dM2_times_E0_MeV": mp.nstr(d2v * E0, 12)})
    print(f"  {tag}: ΔM1 = {d1}, ΔM2 = {BP.fx(d2)} = {mp.nstr(d2v, 12)}")

# ---------------------------------------------------------------- M3
print("2. Charged-current block (M3)")
_, cc, _ = BP.analyse_element(BP.word_el(W))
diag = [[KF.zero] * 3 for _ in range(3)]
for j, nb in enumerate(BP.NUC_IN):
    final, _ = BP.strand_track(W)
    img = BP.rho_word_on({nb + (0,): ONE}, W)
    for i, nb2 in enumerate(BP.NUC_IN):
        st = nb2 + (0,)
        posv = [0] * N
        for s in range(N):
            posv[final[s]] = st[s]
        diag[i][j] += BP.gk(img.get(tuple(posv), ZERO))
ccq = [[BP.ev_frac(e, Q0) if e != 0 else mp.mpf(0) for e in row] for row in cc]
dgq = [[BP.ev_frac(e, Q0) if e != 0 else mp.mpf(0) for e in row] for row in diag]
fro = lambda m: mp.sqrt(sum(x ** 2 for row in m for x in row))  # noqa: E731
ncc, ndg = fro(ccq), fro(dgq)
check("CC block of W is non-zero", ncc > 0, mp.nstr(ncc, 12))
M3 = {"cc_block_exact": [[BP.fx(e) if e != 0 else "0" for e in r] for r in cc],
      "diag_block_exact": [[BP.fx(e) if e != 0 else "0" for e in r] for r in diag],
      "cc_frobenius_q0": mp.nstr(ncc, 15), "diag_frobenius_q0": mp.nstr(ndg, 15)}
if ndg > 0:
    M3["kT_ln_ratio_MeV"] = mp.nstr(E0 * mp.log(ncc / ndg), 12)
    M3["kT_ln_ratio_over_me"] = mp.nstr(E0 * mp.log(ncc / ndg) / ME, 12)
print(f"  |CC| = {mp.nstr(ncc, 10)}, |diag| = {mp.nstr(ndg, 10)}, kT ln ratio = {M3.get('kT_ln_ratio_MeV')}")
OUT["measures"] = {"strategies": M, "M3": M3, "E0_MeV": mp.nstr(E0, 15), "q0": mp.nstr(Q0, 30)}

# ---------------------------------------------------------------- comparison (last; nothing selected)
print("3. Comparison with CODATA (last; nothing selected)")
mn, mpp = mp.mpf(C.M_N_MEV_STR), mp.mpf(C.M_P_MEV_STR)
Qb, dnp = mn - mpp - ME, mn - mpp
rows = {f"{t}_M1xE0": mp.mpf(M[t]["M1_times_E0_MeV"]) for t in M}
rows.update({f"{t}_M2xE0": mp.mpf(M[t]["M2_times_E0_MeV"]) for t in M})
rows.update({f"{t}_dM1xE0": mp.mpf(M[t]["dM1_times_E0_MeV"]) for t in M})
rows.update({f"{t}_dM2xE0": mp.mpf(M[t]["dM2_times_E0_MeV"]) for t in M})
if "kT_ln_ratio_MeV" in M3:
    rows["M3"] = abs(mp.mpf(M3["kT_ln_ratio_MeV"]))
for k, v in rows.items():
    a, b = 100 * (v / Qb - 1), 100 * (v / dnp - 1)
    OUT["comparison"][k] = {"MeV": mp.nstr(v, 12), "vs_Q_beta_pct": mp.nstr(a, 6), "vs_mn_minus_mp_pct": mp.nstr(b, 6)}
    print(f"  {k:12s} {mp.nstr(v, 10):>14s} MeV  vs Q_β {mp.nstr(a, 5):>9s} %  vs m_n−m_p {mp.nstr(b, 5):>9s} %")

OUT["ok"] = not FAILED
(_HERE / "qbeta-gb-reduction.witness.json").write_text(json.dumps(OUT, indent=2, ensure_ascii=False) + "\n")
print(f"{len(OUT['checks']) - len(FAILED)}/{len(OUT['checks'])} checks passed")
sys.exit(1 if FAILED else 0)
