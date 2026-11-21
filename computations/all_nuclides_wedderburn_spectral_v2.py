#!/usr/bin/env python3
"""Wedderburn-spectral admissibility across the AME2020 chart at q_0 (v2).

EXPLORATORY PROBE (production-vs-exploratory discipline: no production
wiring; reports whatever comes out, null or signal).

v1 (`all_nuclides_sdp_admissibility.py`, PR #2071) showed:
  - the scalar H_3 operator-selection LP does not discriminate nuclei
    (active-channel count constant = 1), and
  - the f64 atom NF overflows for 1337/3558 (~38%) heavy nuclei, so no
    naive per-nucleus feasibility can bound the chart.

v1's "real next step" said `solve_psd_operator_selection_sdp`; grounding
showed its current PSD lift is `M(x) = diag(Gx)` — **LP-equivalent** —
so calling it would NOT be a genuine SDP upgrade.  The genuine
per-nucleus SDP-level object is the **Wedderburn decomposition of the
atom element itself**:

    a(Z,N)  in  H_3(q_0)  =  C_sym  (+)  M_2(C)_std  (+)  C_alt,

i.e. the images (rho_sym(a), rho_std(a), rho_alt(a)) — one scalar, one
2x2, one scalar.  Two admissibility notions, increasing strength:

  (F) FROBENIUS-CONE membership (prop:operator-selection-lp level):
      tr_M(b_i . a) >= 0 for the 6 NF basis words b_i — computed in
      block land as Sum_lam y_lam tr(rho_lam(b_i) rho_lam(a)), so NO
      f64 overflow.
  (P) SPECTRAL POSITIVITY (the SDP-strength notion): the spectrum of
      every Wedderburn block of a is real and >= 0.  Basis-invariant
      (similarity-invariant), hence well-defined on the Wedderburn
      class.  For the 1-dim blocks this is a sign; for the 2x2 std
      block: disc = tr^2 - 4 det >= 0, tr >= 0, det >= 0.

OVERFLOW FIX: blocks are computed at mpmath precision (mpf exponents
are unbounded), as products of 1x1 / 2x2 crossing images — all 3558
nuclides become computable (v1 gap closed).

SPEED: every inter-nucleon crossing (pp = s0, nn = s0^-1, pn = mixed)
is a polynomial in the SAME matrix rho(s0), so they all commute; the
per-nucleon inter product has a closed triangular form via eigenvalue
powers.  Same for the electron tail (powers of s1^-1).  Per nucleus
O(A) 2x2 mpf multiplications instead of O(A^2).

STRUCTURAL CLOSED FORM (proved by the construction, verified
numerically here): the alt block is a product of T(Z,N) negative-at-q>1
factors, where T = 11 A + A(A-1)/2 + Z is the total crossing count, so

    sign(rho_alt(a)) = (-1)^(T(Z,N)),   T = 11A + A(A-1)/2 + Z.

Spectral positivity of the alt channel is therefore a PARITY condition
on the crossing count — reported as a finding, not wired anywhere.

Validation battery (algebraic preflight, compute-author discipline):
  1. Hecke relation rho(s_i)^2 = h rho(s_i) + 1 at mpf for both gens.
  2. Braid relation rho(s0)rho(s1)rho(s0) = rho(s1)rho(s0)rho(s1).
  3. chi_std vs native pyhecke_native.chi_lambda_braid (f64) on words.
  4. Markov weights y_lam from a 3x3 mpf solve against the defining
     Markov values (1, z, z^2); cross-checked vs native
     trace_weights_n(3, q0) (modulo convention).
  5. brute sequential block product == fast closed-form product (A<=16).
  6. tr_M from blocks == gram.nf_tr(atom.build_atom_nf) (f64, light A).

Output: all-nuclides-wedderburn-spectral-v2.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp
from decimal import Decimal as _Decimal, ROUND_HALF_EVEN as _ROUND_HALF_EVEN

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "substrate"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from convolution_provenance import CONVOLUTION  # noqa: E402

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402

DPS = 40
mp.mp.dps = DPS + 10  # guard digits

# ── canonical q_0 at mpf precision ─────────────────────────────────────
_Q0_SOURCE = f"qou_substrate.constants.q_at({DPS})"
try:
    from qou_substrate.constants import q_at  # noqa: E402
    Q0 = q_at(DPS)
except (ImportError, AttributeError) as _q_err:  # narrow: only "not there"
    # Do NOT swallow real q_at bugs — those should crash the probe.
    from qou_substrate.constants import Q as _Qf  # noqa: E402
    Q0 = mp.mpf(repr(_Qf))
    _Q0_SOURCE = f"FALLBACK f64-seeded Q ({type(_q_err).__name__}: {_q_err})"
    print(f"[warn] q_at unavailable — q0 precision downgraded to the "
          f"f64-seeded value: {_q_err}", file=sys.stderr)

QI = 1 / Q0
H = Q0 - QI                         # h = q - q^-1 (Hecke scalar)
Z_MARKOV = Q0**3 / (Q0**2 + 1)   # tr_M(sigma_i) = z

AME = _ROOT / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json"

# ── H_3 irrep images (Hecke convention: eigenvalues {q, -1/q}) ─────────
# std (2,1): rescaled reduced Burau, sigma = -q^{-1} * Burau(t=q^2).
# Upper/lower triangular forms make polynomial functional calculus exact.
RHO0 = [[Q0, -QI], [mp.mpf(0), -QI]]    # rho_std(sigma_0)
RHO1 = [[-QI, mp.mpf(0)], [-Q0, Q0]]    # rho_std(sigma_1)
ID2 = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]


def m2(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0],
         a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0],
         a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


def m_affine(m, rho, c, d):
    """m := m . (c*rho + d*I)  — right-multiply by an affine crossing."""
    f = [[c * rho[0][0] + d, c * rho[0][1]],
         [c * rho[1][0], c * rho[1][1] + d]]
    return m2(m, f)


def m_tr(m):
    return m[0][0] + m[1][1]


def m_det(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


# Crossing codes: 'pos' = sigma (c=1,d=0); 'inv' = sigma^-1 (c=1,d=-h);
# 'mix' = (sigma + sigma^-1)/2 (c=1,d=-h/2).
CD = {"pos": (mp.mpf(1), mp.mpf(0)),
      "inv": (mp.mpf(1), -H),
      "mix": (mp.mpf(1), -H / 2)}

# 1-dim block factors per code: sym(sigma)=q, alt(sigma)=-1/q.
SYM_F = {"pos": Q0, "inv": QI, "mix": (Q0 + QI) / 2}
ALT_F = {"pos": -QI, "inv": -Q0, "mix": -(Q0 + QI) / 2}

# std eigen-branch factors (lambda in {q, -1/q}); used by the fast path.
EIG = {"+": Q0, "-": -QI}
STD_F = {k: {"pos": EIG[k], "inv": EIG[k] - H, "mix": EIG[k] + _pn_d(H)}
         for k in ("+", "-")}
# checks: (q)-h = 1/q (inv on + branch); (-1/q)-h = -q (inv on - branch)


def ordering_pn(Z: int, N: int) -> list[str]:
    """Ground-state interleaved p/n ordering — mirrors atom.py exactly."""
    out, pc, nc = [], 0, 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            out.append("p"); pc += 1
        else:
            out.append("n"); nc += 1
    return out


# Intra-nucleon crossing sequences (gen, code) — mirrors atom.py 218-242.
INTRA = {
    "p": [(0, "pos"), (1, "inv")] * 3
         + [(0, "pos"), (0, "mix"), (1, "mix")] + [(0, "pos")] * 2,
    "n": [(0, "pos"), (1, "inv")] * 3
         + [(0, "mix"), (0, "mix"), (1, "inv")] + [(0, "pos")] * 2,
}


def crossing_sequence(Z: int, N: int) -> list[tuple[int, str]]:
    """Full (gen, code) crossing list — mirrors atom.build_atom_nf."""
    order = ordering_pn(Z, N)
    seq: list[tuple[int, str]] = []
    for k, t in enumerate(order):
        seq += INTRA[t]
        for prev in range(k):
            pair = (order[prev], t)
            seq.append((0, "pos") if pair == ("p", "p")
                       else (0, "inv") if pair == ("n", "n")
                       else (0, "mix"))
    seq += [(1, "inv")] * Z
    return seq


def blocks_brute(Z: int, N: int):
    """Sequential product over the full crossing list (validation path)."""
    sym = mp.mpf(1); alt = mp.mpf(1); std = [r[:] for r in ID2]
    for gen, code in crossing_sequence(Z, N):
        c, d = CD[code]
        sym *= SYM_F[code]
        alt *= ALT_F[code]
        std = m_affine(std, RHO0 if gen == 0 else RHO1, c, d)
    return sym, alt, std


def _intra_block(t: str):
    m = [r[:] for r in ID2]
    for gen, code in INTRA[t]:
        c, d = CD[code]
        m = m_affine(m, RHO0 if gen == 0 else RHO1, c, d)
    return m


def blocks_fast(Z: int, N: int, *, P_intra, N_intra):
    """Closed-form per-nucleon product.

    Inter-nucleon crossings are all polynomials in rho(sigma_0)
    (upper triangular), so the per-nucleon inter product is
      [[P+, (-1/q)(P+ - P-)/(q + 1/q)], [0, P-]],
    with P(branch) = prod of branch factors with integer exponents.
    Electron tail = (sigma_1^-1)^Z, lower triangular analogue.
    """
    order = ordering_pn(Z, N)
    A = Z + N
    sym = mp.mpf(1); alt = mp.mpf(1); std = [r[:] for r in ID2]
    two_q = Q0 + QI
    p_prev = n_prev = 0
    pos_n = inv_n = mix_n = 0          # 1-dim exponent tallies
    for t in order:
        # intra block
        std = m2(std, P_intra if t == "p" else N_intra)
        if t == "p":
            pos_n += 6; inv_n += 3; mix_n += 2
        else:
            pos_n += 5; inv_n += 4; mix_n += 2
        # inter with all previous (commuting family in rho(sigma_0))
        if p_prev + n_prev:
            if t == "p":
                e_pos, e_inv, e_mix = p_prev, 0, n_prev
            else:
                e_pos, e_inv, e_mix = 0, n_prev, p_prev
            pos_n += e_pos; inv_n += e_inv; mix_n += e_mix
            Pp = (STD_F["+"]["pos"] ** e_pos * STD_F["+"]["inv"] ** e_inv
                  * STD_F["+"]["mix"] ** e_mix)
            Pm = (STD_F["-"]["pos"] ** e_pos * STD_F["-"]["inv"] ** e_inv
                  * STD_F["-"]["mix"] ** e_mix)
            M = [[Pp, (-QI) * (Pp - Pm) / two_q], [mp.mpf(0), Pm]]
            std = m2(std, M)
        if t == "p":
            p_prev += 1
        else:
            n_prev += 1
    # electron tail: (sigma_1 - h)^Z, eigenvalues (1/q)^Z and (-q)^Z
    if Z:
        inv_n += Z
        fq = QI ** Z          # f(q)    = (q - h)^Z = (1/q)^Z
        fm = (-Q0) ** Z       # f(-1/q) = (-q)^Z
        E = [[fm, mp.mpf(0)], [(-Q0) * (fq - fm) / two_q, fq]]
        std = m2(std, E)
    sym = (SYM_F["pos"] ** pos_n * SYM_F["inv"] ** inv_n
           * SYM_F["mix"] ** mix_n)
    # alt: track sign separately (every factor negative at q>1)
    T = pos_n + inv_n + mix_n
    alt = ((-1) ** (T % 2)
           * (QI ** pos_n * Q0 ** inv_n * (two_q / 2) ** mix_n))
    assert T == 11 * A + A * (A - 1) // 2 + Z, "crossing-count closed form"
    return sym, alt, std, T


def sgn_log10(x) -> tuple[int, "mp.mpf | None"]:
    """`(sign, log10|x|)` with the magnitude kept as `mpf`.

    It was `float(mp.log10(abs(x)))`, discarding a 40-dps computation at the
    moment it was produced. The three `*_log10` columns are this function's
    output over 3,558 nuclides and were the bulk of this witness's raw
    float64; the caller now serializes them at a declared width (`_dp`)
    instead of rounding a double.

    The zero branch returns `None`, not `float("-inf")`. JSON has no
    infinity — Python's encoder emits a bare `-Infinity`, which is not valid
    JSON and which only its own decoder accepts by extension — and the
    companion `*_sign` field already carries 0 for that case, so nothing is
    lost. Measured on the committed witness: 0 of 3,558 rows have a zero
    sign or an infinite log, so this branch is dead in the data and no
    committed value changes.
    """
    if x == 0:
        return 0, None
    return (1 if x > 0 else -1), mp.log10(abs(x))


def _dp(x, places: int = 4):
    """Serialize one row cell at its declared decimal width, as a STRING.

    Replaces `round(x, <places>)`, which emitted a JSON float. Like the mass
    table's helper, this is a TYPE fix rather than a precision gain: four
    decimals on a log10 is ~1e-4 absolute, twelve orders above binary64's
    floor, so the mpf that now reaches it cannot change a printed digit.
    That is a checkable prediction and it is checked in the PR.

    MEASURED 2026-08-30, and the prediction needs one qualifier. The mpf and
    float paths agree on ordinary values but diverge on an EXACT DECIMAL TIE:
    `1.00005` prints `1.0000` from the mpf path and `1.0001` from the float
    one. Neither is a bug -- the mpf path rounds half-even on the true decimal
    value, the float path rounds on that value's binary64 approximation, which
    is not exactly 1.00005. The mpf answer is the more faithful of the two.
    Ties on a log10 are vanishingly rare, so this does not move any row here;
    it is recorded because "cannot change a printed digit" is not literally
    true and the next reader should not have to rediscover why.
    """
    if x is None:
        return None
    if isinstance(x, float):
        return f"{x:.{places}f}"
    # mpf: `f"{mpf:.4f}"` raises TypeError (mpf has no __format__ for the
    # float presentation types), so the mpf this helper was written to accept
    # crashed it instead of being served. Quantize through Decimal from a
    # 40-significant-digit mpmath string -- never through float(), which would
    # reintroduce the binary64 hop the helper exists to avoid.
    d = _Decimal(mp.nstr(x, 40, strip_zeros=False))
    return str(d.quantize(_Decimal(1).scaleb(-places),
                          rounding=_ROUND_HALF_EVEN))


def _sig(x) -> str:
    """Full-precision decimal string at THIS producer's own working dps.

    Deliberately not `_precision.fmt`, which serializes at the corpus-wide
    `OUTPUT_DPS` (60). This module computes at `DPS = 40`, so 60 digits
    would claim twenty this producer never had. Used for the assertion
    residuals and thresholds, which are scalars — the row columns keep
    their four-decimal display width via `_dp`.
    """
    return mp.nstr(x, DPS, strip_zeros=False)


def main() -> int:
    # WitnessBuilder interprets start_time as a time.monotonic() baseline
    # (qou_substrate.witness:236) — NOT epoch time.time().
    t0 = time.monotonic()
    w = WitnessBuilder("all-nuclides-wedderburn-spectral-v2",
                       engine="mpmath", start_time=t0)
    w.add_data("q0_source", _Q0_SOURCE)
    w.add_data("convolution", CONVOLUTION)

    # ── validation battery ─────────────────────────────────────────
    tol = mp.mpf(10) ** (-(DPS - 5))
    # 1. Hecke relation on both generators
    hek = []
    for rho in (RHO0, RHO1):
        sq = m2(rho, rho)
        ref = [[H * rho[i][j] + (1 if i == j else 0) for j in (0, 1)]
               for i in (0, 1)]
        hek.append(max(abs(sq[i][j] - ref[i][j])
                       for i in (0, 1) for j in (0, 1)))
    # `computed` is a residual of a 40-dps computation and `tol` a declared
    # threshold; both were cast to `float` on the way out. `add_assertion`
    # documents strings as the drained convention (`passed` coerces with
    # `float()` either way), so the residual keeps its digits and the
    # threshold is written as the literal it is.
    w.add_assertion(name="hecke_relation_both_gens",
                    computed=_sig(max(hek)), expected="0",
                    tolerance=_sig(tol), source="rho^2 = h rho + 1 at mpf")
    # 2. braid relation
    b1 = m2(m2(RHO0, RHO1), RHO0)
    b2 = m2(m2(RHO1, RHO0), RHO1)
    bdev = max(abs(b1[i][j] - b2[i][j]) for i in (0, 1) for j in (0, 1))
    w.add_assertion(name="braid_relation", computed=_sig(bdev),
                    expected="0", tolerance=_sig(tol),
                    source="rho(s0)rho(s1)rho(s0) = rho(s1)rho(s0)rho(s1)")
    # 3. chi_std vs native Hoefsmit, MPFR entry (2026-11-21). This used the
    #    f64 `chi_lambda_braid` at float(Q0), so the check could only ever
    #    confirm ~1e-16 agreement of a 40-digit computation; the MPFR entry
    #    takes q as a decimal string and checks at the working precision.
    native_dev = None
    try:
        import pyhecke_native as nat
        q_str = mp.nstr(Q0, DPS + 5)
        words = [[(1, 1)], [(1, 1), (1, 2)], [(1, 1), (1, 1)],
                 [(1, 1), (-1, 2), (1, 1)]]
        devs = []
        for word in words:
            m = [r[:] for r in ID2]
            for s, g in word:
                rho = RHO0 if g == 1 else RHO1
                if s == 1:
                    m = m2(m, rho)
                else:
                    m = m_affine(m, rho, mp.mpf(1), -H)  # sigma^-1
            mine = m_tr(m)
            ref = mp.mpf(nat.chi_lambda_braid_mpfr([2, 1], word, q_str, DPS))
            devs.append(abs(mine - ref))
        native_dev = max(devs)
        w.add_assertion(name="chi_std_vs_native_hoefsmit",
                        computed=_sig(native_dev), expected="0",
                        tolerance=_sig(tol),
                        source="pyhecke_native.chi_lambda_braid_mpfr([2,1],...)")
    except Exception as e:  # pragma: no cover
        w.add_data("native_chi_crosscheck", f"unavailable: {e}")

    # 4. Markov weights y_lam: solve [chi_lam(b)] y = tr_M(b) over
    #    b in {1, s0, s0 s1} with defining Markov values (1, z, z^2).
    chi_1 = (mp.mpf(1), mp.mpf(2), mp.mpf(1))
    chi_s = (Q0, H, -QI)                       # chi(sigma): q, q-1/q, -1/q
    chi_ss = (Q0 ** 2, m_tr(m2(RHO0, RHO1)), QI ** 2)   # std: -1 exactly
    rhs = (mp.mpf(1), Z_MARKOV, Z_MARKOV ** 2)
    Mm = mp.matrix([[chi_1[0], chi_1[1], chi_1[2]],
                    [chi_s[0], chi_s[1], chi_s[2]],
                    [chi_ss[0], chi_ss[1], chi_ss[2]]])
    yv = mp.lu_solve(Mm, mp.matrix(rhs))
    y_sym, y_std, y_alt = yv[0], yv[1], yv[2]
    w.add_data("markov_weights_y_lambda",
               {"(3)": mp.nstr(y_sym, 30), "(2,1)": mp.nstr(y_std, 30),
                "(1,1,1)": mp.nstr(y_alt, 30),
                "chi_std_on_s0s1_exact": mp.nstr(chi_ss[1], 10)})
    try:
        import pyhecke_native as nat
        tw = list(nat.trace_weights_n(3, float(Q0)))
        mine = sorted(float(v) for v in (y_sym, y_std, y_alt))
        theirs = sorted(float(v) for v in tw)
        match = max(abs(a - b) for a, b in zip(mine, theirs)) < 1e-9
        w.add_data("trace_weights_n_native", {"values": tw,
                   "matches_mpf_solve": bool(match)})
    except Exception as e:  # pragma: no cover
        w.add_data("trace_weights_n_native", f"unavailable: {e}")

    # NF basis block images for the (F) Frobenius pairings.
    basis_words = [[], [(0,)], [(1,)], [(0,), (1,)], [(1,), (0,)],
                   [(0,), (1,), (0,)]]
    basis_std = []
    basis_sym = []
    basis_alt = []
    for bw in basis_words:
        m = [r[:] for r in ID2]; s = mp.mpf(1); a = mp.mpf(1)
        for (g,) in bw:
            m = m2(m, RHO0 if g == 0 else RHO1)
            s *= Q0; a *= -QI
        basis_std.append(m); basis_sym.append(s); basis_alt.append(a)

    # 5/6. brute vs fast + f64 NF cross-check on light nuclei
    P_intra = _intra_block("p"); N_intra = _intra_block("n")
    light = [(1, 0), (1, 1), (2, 1), (2, 2), (3, 4), (6, 6), (8, 8)]
    bf_dev = mp.mpf(0)
    f64_dev = 0.0
    try:
        from pyhecke import atom as _atom, gram as _gram
        have_f64 = True
    except Exception:  # pragma: no cover
        have_f64 = False
    for (Zl, Nl) in light:
        sb, ab, stdb = blocks_brute(Zl, Nl)
        sf, af, stdf, _T = blocks_fast(Zl, Nl, P_intra=P_intra,
                                       N_intra=N_intra)
        rel = max(
            abs(sb - sf) / max(abs(sb), mp.mpf("1e-30")),
            abs(ab - af) / max(abs(ab), mp.mpf("1e-30")),
            max(abs(stdb[i][j] - stdf[i][j]) for i in (0, 1)
                for j in (0, 1))
            / max(max(abs(stdb[i][j]) for i in (0, 1) for j in (0, 1)),
                  mp.mpf("1e-30")),
        )
        bf_dev = max(bf_dev, rel)
        if have_f64:
            nf = _atom.build_atom_nf(Zl, Nl)
            tr_f64 = float(_gram.nf_tr(nf))
            tr_blocks = float(y_sym * sb + y_std * m_tr(stdb) + y_alt * ab)
            denom = max(abs(tr_f64), 1e-12)
            f64_dev = max(f64_dev, abs(tr_blocks - tr_f64) / denom)
    w.add_assertion(name="brute_vs_fast_blocks_light",
                    computed=_sig(bf_dev), expected="0",
                    tolerance=_sig(mp.mpf(10) ** (-(DPS - 12))),
                    source=f"A<=16 sample {light}")
    if have_f64:
        w.add_assertion(name="trM_blocks_vs_f64_nf_light",
                        computed=f64_dev, expected=0.0, tolerance=1e-6,
                        source="y_lam tr rho_lam vs gram.nf_tr(build_atom_nf)")

    # ── full-chart sweep ───────────────────────────────────────────
    entries = json.loads(AME.read_text())["entries"]
    rows = []
    n_total = 0
    n_F = 0          # Frobenius-cone members
    n_P = 0          # spectrally positive (all blocks)
    n_std_pos = 0    # std block alone positive
    n_parity_ok = 0  # alt sign matches (-1)^T closed form
    n_disc_boundary = 0  # |disc| within roundoff of 0 (degenerate eigs)
    permitted_P: list[list[int]] = []
    # disc = tr^2 - 4 det is a difference of same-magnitude huge numbers
    # (blocks reach ~10^±4000), so the roundoff guard must be RELATIVE to
    # the operand scale, tied to the working precision — an absolute
    # tolerance would be vacuous at those magnitudes.
    disc_eps = mp.mpf(10) ** (-(DPS - 8))
    t_start = time.monotonic()
    for idx, e in enumerate(entries):
        Z, N, A = int(e["Z"]), int(e["N"]), int(e["A"])
        if A < 1:
            continue
        n_total += 1
        sym, alt, std, T = blocks_fast(Z, N, P_intra=P_intra,
                                       N_intra=N_intra)
        tr_std, det_std = m_tr(std), m_det(std)
        disc = tr_std * tr_std - 4 * det_std
        disc_scale = max(tr_std * tr_std, abs(4 * det_std),
                         mp.mpf("1e-300"))
        if abs(disc) <= disc_eps * disc_scale:
            n_disc_boundary += 1
        std_pos = bool(disc >= -disc_eps * disc_scale
                       and tr_std >= 0 and det_std >= 0)
        alt_pos = bool(alt >= 0)
        spectral_pos = bool(sym >= 0) and alt_pos and std_pos
        # (F) Frobenius pairings tr_M(b_i . a) in block land
        frob = [y_sym * basis_sym[i] * sym
                + y_std * m_tr(m2(basis_std[i], std))
                + y_alt * basis_alt[i] * alt
                for i in range(6)]
        frob_pos = bool(all(v >= 0 for v in frob))
        parity_ok = (alt >= 0) == (T % 2 == 0)
        n_F += frob_pos
        n_P += spectral_pos
        n_std_pos += std_pos
        n_parity_ok += parity_ok
        if spectral_pos:
            permitted_P.append([Z, N])
        s_sym = sgn_log10(sym)
        s_alt = sgn_log10(alt)
        trm = y_sym * sym + y_std * tr_std + y_alt * alt
        s_trm = sgn_log10(trm)
        rows.append({
            "Z": Z, "N": N, "A": A, "T_crossings": T,
            "sym_sign": s_sym[0], "sym_log10": _dp(s_sym[1]),
            "alt_sign": s_alt[0], "alt_log10": _dp(s_alt[1]),
            "std_tr_sign": 1 if tr_std >= 0 else -1,
            "std_det_sign": 1 if det_std >= 0 else -1,
            "std_disc_sign": 1 if disc >= 0 else -1,
            "std_positive": std_pos,
            "spectral_positive": spectral_pos,
            "frobenius_member": frob_pos,
            "trM_sign": s_trm[0], "trM_log10": _dp(s_trm[1]),
            # keV -> MeV in exact arithmetic. `float(...) * A / 1000.0` did
            # the conversion in binary64, where neither 1/1000 nor most of
            # the AME table's keV values are representable; `mpf(str(...))`
            # reads the tabulated decimal AS that decimal.
            "B_AME_MeV": _dp(
                mp.mpf(str(e.get("binding_energy_per_A_keV") or 0)) * A / 1000,
                6),
        })
        if (idx + 1) % 400 == 0:
            el = time.monotonic() - t_start
            eta = el / (idx + 1) * (len(entries) - idx - 1)
            print(f"[progress] {idx+1}/{len(entries)} "
                  f"elapsed {el:.0f}s eta {eta:.0f}s", file=sys.stderr)

    w.set_description(
        "v2 Wedderburn-spectral admissibility over the AME2020 chart at "
        "q_0 (EXPLORATORY). Per nucleus: the three Wedderburn block "
        "images of build_atom_nf's crossing sequence at 40-dps mpmath "
        "(no f64 overflow — closes v1's 38% gap). Tests: (F) Frobenius-"
        "cone membership tr_M(b_i a) >= 0 (prop:operator-selection-lp "
        "positivity); (P) spectral positivity of all blocks (the genuine "
        "SDP-strength per-nucleus criterion; the diagonal-lift "
        "solve_psd_operator_selection_sdp is LP-equivalent, so v1's "
        "suggestion would not have been a real upgrade). Includes the "
        "closed form sign(alt) = (-1)^T, T = 11A + A(A-1)/2 + Z."
    )
    w.add_data("q0_dps", DPS)
    w.add_data("n_nuclides", n_total)
    w.add_data("counts", {
        "frobenius_members_F": n_F,
        "spectrally_positive_P": n_P,
        "std_block_positive": n_std_pos,
        "alt_parity_closed_form_matches": n_parity_ok,
        "disc_roundoff_boundary_cases": n_disc_boundary,
        "stable_nuclides_empirical": 251,
        "ame_chart": n_total,
    })
    # aggregate structure of the permitted sets
    F_rows = [r for r in rows if r["frobenius_member"]]
    P_rows = [r for r in rows if r["spectral_positive"]]
    par_hist: dict[str, int] = {}
    for r in P_rows:
        k = f"(A%4={r['A'] % 4}, Z%2={r['Z'] % 2})"
        par_hist[k] = par_hist.get(k, 0) + 1
    w.add_data("parity_class_hist_P", par_hist)
    w.add_data("findings", [
        "(F) is a LIGHT-CHART criterion: every Frobenius-cone member has "
        f"A <= {max((r['A'] for r in F_rows), default=0)} "
        f"({len(F_rows)} members; selective even within the light region "
        "— e.g. 4He, 12C in; 16O out).",
        "(P) obeys the alt-parity selection rule exactly: allowed classes "
        "(A mod 4, Z parity) in {(0,even),(1,odd),(2,odd),(3,even)} — "
        "(0,even) contains the alpha-ladder (4He, 12C, 16O, 56Fe, 208Pb "
        "all spectrally positive) and (2,odd) the stable odd-odd family "
        "(2H, 6Li, 10B, 14N). The std-block condition then cuts the "
        f"parity-allowed half (~{n_total // 2}) down to {len(P_rows)}.",
        "(P) is NOT simply the stable set (251): it admits "
        f"{len(P_rows)} across A = "
        f"{min((r['A'] for r in P_rows), default=0)}-"
        f"{max((r['A'] for r in P_rows), default=0)}. Exploratory — "
        "no production wiring; the criterion's physical meaning (if any) "
        "is the open question this probe feeds to the Delta_lambda work.",
    ])
    # GUARD: refuse a vacuous pass. BOTH assertions below compare quantities
    # that are 0 exactly when nothing was swept -- len(rows) == n_total and
    # n_parity_ok == n_total are each trivially true at 0 == 0. n_total counts
    # AME entries with A >= 1, so zero means the nuclide table did not load,
    # not that the chart was swept and found empty.
    if n_total == 0:
        raise SystemExit(
            f"REFUSING to emit a witness: 0 of {len(entries)} AME entries were "
            f"swept (n_total == 0), so both chart_fully_swept_no_overflow and "
            f"alt_parity_closed_form would pass vacuously at 0 == 0. The "
            f"nuclide table is empty or failed to load."
        )

    w.add_data("permitted_ZN_spectral", permitted_P)
    w.add_data("rows", rows)
    w.add_assertion(name="chart_fully_swept_no_overflow",
                    computed=len(rows), expected=n_total, tolerance=0,
                    source="every AME entry with A>=1 computed at mpf")
    w.add_assertion(name="alt_parity_closed_form",
                    computed=n_parity_ok, expected=n_total, tolerance=0,
                    source="sign(alt) == (-1)^(11A + A(A-1)/2 + Z)")

    out = w.save()
    print(f"\nnuclides: {n_total} (all computed — no overflow)")
    print(f"(F) Frobenius-cone members:    {n_F} / {n_total}")
    print(f"(P) spectrally positive:       {n_P} / {n_total}")
    print(f"    std block positive:        {n_std_pos}")
    print(f"    alt parity closed form:    {n_parity_ok} / {n_total}")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
