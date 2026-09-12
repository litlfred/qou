#!/usr/bin/env python3
"""he4_magnus_mpfr_probe.py — the A=4 Magnus Ω₂ sign, computed on gmpy2.mpfr
(native MPFR) instead of mpmath.mpf. MEASURED 4.0× faster on the inner arithmetic
(0.24 vs 0.97 µs/op at 466-bit ≈ 140 dp), which is what makes the heavy H₁₂
partitions (dim 5632–7700) finish inside a container window.

Same object, same math, same precision as he4_magnus_omega2_sign_sparse_probe.py —
only the arithmetic backend changes. NO-FLOAT64: MPFR is arbitrary precision,
context pinned to 466 bits (= 140 dp), NOT float64. The structural helpers
(block_structure, partitions, _dim_estimate) are reused from the mpmath probe —
they are pure integer / tableau combinatorics with no floating arithmetic, so
they are backend-agnostic and need no re-validation.

GATE (--gate): reproduce the COMMITTED triton H₉ P_total to < 1e-30. Only then is
the H₁₂ run trusted. Per-partition JSONL checkpoint (own file) is resumable.
scope-(a); 0 free parameters.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hecke"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402

_PREC = 466  # bits ≈ 140 decimal digits
gmpy2.get_context().precision = _PREC

# structural helpers (integer/tableau only — backend-agnostic)
from he4_magnus_omega2_sign_sparse_probe import (  # noqa: E402
    block_structure,
    partitions,
    _dim_estimate,
    _Q0_RESOLVED,
)

Q0 = mpfr(_Q0_RESOLVED)
H = Q0 - 1 / Q0
EPS = mpfr(10) ** -50
_EXACT = mpfr(10) ** -30


def gsqrt(x):
    return gmpy2.sqrt(x if x >= 0 else -x)


def fmt(x, digits=50):
    """Serialize an mpfr to a decimal string (~50 sig digits), checkpoint-compatible."""
    return _fmt_decimal(x, digits)


def _fmt_decimal(x, digits):
    s = mpfr(x)
    # gmpy2.digits -> (mantissa_str, exp, prec); rebuild a plain decimal
    mant, exp, _ = gmpy2.digits(s, 10, digits)
    neg = mant.startswith("-")
    if neg:
        mant = mant[1:]
    # value = 0.mant * 10^exp
    if exp <= 0:
        out = "0." + "0" * (-exp) + mant
    elif exp >= len(mant):
        out = mant + "0" * (exp - len(mant))
    else:
        out = mant[:exp] + "." + mant[exp:]
    return ("-" if neg else "") + out


def q_int(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def wedderburn_weight(shape, q):
    from math import prod
    n = sum(shape)
    rows = list(shape)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    hooks = []
    for i, ri in enumerate(rows):
        for j in range(ri):
            hooks.append((ri - j - 1) + (cols[j] - i - 1) + 1)
    dq = mpfr(1)
    for hh in hooks:
        dq *= q_int(hh, q)
    nf = mpfr(1)
    for k in range(1, n + 1):
        nf *= q_int(k, q)
    return (dq * dq) / nf


def _a_scalars(rho, q):
    h = q - 1 / q
    return h / (1 - q ** (-2 * rho)), h / (1 - q ** (2 * rho))


def sigma_csr(per_gen, dim, q):
    sig = []
    for blocks in per_gen:
        rows = [[] for _ in range(dim)]
        for blk in blocks:
            if blk[0] == "diag":
                _, i, rho = blk
                a, _ = _a_scalars(rho, q)
                rows[i].append((i, a))
            else:
                _, i, j, rho = blk
                a, ap = _a_scalars(rho, q)
                b = gsqrt(a * ap + 1)
                rows[i].append((i, a)); rows[i].append((j, b))
                rows[j].append((j, ap)); rows[j].append((i, b))
        sig.append(rows)
    return sig


def germ_csr(per_gen, dim, q, eps):
    """A_g = q·(∂_q σ_g)·σ_g⁻¹ per block (central finite diff), explicit 2×2."""
    qp, qm = q + eps, q - eps
    hp = 1 + 1 / q ** 2
    hcheck = mpfr(0)
    germ = []
    for blocks in per_gen:
        rows = [[] for _ in range(dim)]
        for blk in blocks:
            if blk[0] == "diag":
                _, i, rho = blk
                a, _ = _a_scalars(rho, q)
                ap_p, _ = _a_scalars(rho, qp)
                ap_m, _ = _a_scalars(rho, qm)
                da = (ap_p - ap_m) / (2 * eps)
                rows[i].append((i, q * da / a))
                r = a * da + da * a - (hp * a + H * da)
                hcheck = max(hcheck, abs(r))
            else:
                _, i, j, rho = blk
                a, ap = _a_scalars(rho, q)
                b = gsqrt(a * ap + 1)
                a1, ap1 = _a_scalars(rho, qp); b1 = gsqrt(a1 * ap1 + 1)
                a2, ap2 = _a_scalars(rho, qm); b2 = gsqrt(a2 * ap2 + 1)
                # B, dB (2x2), Binv (2x2)
                B = (a, b, b, ap)
                dB = ((a1 - a2) / (2 * eps), (b1 - b2) / (2 * eps),
                      (b1 - b2) / (2 * eps), (ap1 - ap2) / (2 * eps))
                det = a * ap - b * b
                Bi = (ap / det, -b / det, -b / det, a / det)
                # A = q * dB @ Binv
                A00 = q * (dB[0] * Bi[0] + dB[1] * Bi[2])
                A01 = q * (dB[0] * Bi[1] + dB[1] * Bi[3])
                A10 = q * (dB[2] * Bi[0] + dB[3] * Bi[2])
                A11 = q * (dB[2] * Bi[1] + dB[3] * Bi[3])
                rows[i].append((i, A00)); rows[i].append((j, A01))
                rows[j].append((i, A10)); rows[j].append((j, A11))
                # Hecke check: B@dB + dB@B == hp*B + H*dB
                def mm(X, Y):
                    return (X[0] * Y[0] + X[1] * Y[2], X[0] * Y[1] + X[1] * Y[3],
                            X[2] * Y[0] + X[3] * Y[2], X[2] * Y[1] + X[3] * Y[3])
                l = mm(B, dB); r2 = mm(dB, B)
                for t in range(4):
                    hcheck = max(hcheck, abs(l[t] + r2[t] - (hp * B[t] + H * dB[t])))
        germ.append(rows)
    return germ, hcheck


def csr_to_dict(rows):
    d = {}
    for i, entries in enumerate(rows):
        if not entries:
            continue
        acc = {}
        for c, v in entries:
            acc[c] = acc.get(c, mpfr(0)) + v
        d[i] = acc
    return d


def spmatmul(Ad, Bd):
    out = {}
    for i, arow in Ad.items():
        orow = {}
        for k, av in arow.items():
            brow = Bd.get(k)
            if not brow:
                continue
            for l, bv in brow.items():
                orow[l] = orow.get(l, mpfr(0)) + av * bv
        if orow:
            out[i] = orow
    return out


def commutator(Ad, Bd):
    AB = spmatmul(Ad, Bd); BA = spmatmul(Bd, Ad)
    out = {}
    for i in set(AB) | set(BA):
        r = dict(AB.get(i, {}))
        for l, v in BA.get(i, {}).items():
            r[l] = r.get(l, mpfr(0)) - v
        r = {l: v for l, v in r.items() if v != 0}
        if r:
            out[i] = r
    return out


def spmatvec(sig_rows, v):
    n = len(v)
    out = [mpfr(0)] * n
    for i, entries in enumerate(sig_rows):
        s = mpfr(0)
        for c, val in entries:
            s += val * v[c]
        out[i] = s
    return out


def apply_word_to_e(gens, sig, k, dim):
    v = [mpfr(0)] * dim
    v[k] = mpfr(1)
    for g in reversed(gens):
        v = spmatvec(sig[g], v)
    return v


def partition_contribution(shape, gens):
    per_gen, dim = block_structure(shape)
    y = wedderburn_weight(shape, Q0)
    if dim == 1:
        row = {"lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
               "tr_rho_Omega2": fmt(mpfr(0)), "tr_Omega2_ctrl": fmt(mpfr(0))}
        return row, mpfr(0), mpfr(0), mpfr(0), mpfr(0), dim, 0
    sig = sigma_csr(per_gen, dim, Q0)
    germ_rows, hcheck = germ_csr(per_gen, dim, Q0, EPS)
    assert hcheck < mpfr(10) ** -55, f"germ Hecke check {shape}: {hcheck}"
    A = [csr_to_dict(germ_rows[g]) for g in range(len(germ_rows))]
    ccache = {}
    Om2 = {}
    L = len(gens)
    for i in range(L):
        a = gens[i]
        for j in range(i + 1, L):
            b = gens[j]
            if abs(a - b) != 1:
                continue
            C = ccache.get((a, b))
            if C is None:
                C = commutator(A[a], A[b]); ccache[(a, b)] = C
            for r, crow in C.items():
                orow = Om2.setdefault(r, {})
                for c, v in crow.items():
                    orow[c] = orow.get(c, mpfr(0)) + v
    for r in Om2:
        for c in Om2[r]:
            Om2[r][c] = Om2[r][c] / 2
    tr_O = mpfr(0)
    for r, orow in Om2.items():
        tr_O += orow.get(r, mpfr(0))
    tr_rO = mpfr(0)
    for k, orow in Om2.items():
        w = apply_word_to_e(gens, sig, k, dim)
        s = mpfr(0)
        for c, v in orow.items():
            s += v * w[c]
        tr_rO += s
    row = {"lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
           "tr_rho_Omega2": fmt(tr_rO), "tr_Omega2_ctrl": fmt(tr_O)}
    return row, y * tr_rO, y * tr_O, tr_rO, hcheck, dim, len(Om2)


def _agg(rows):
    P = mpfr(0); C = mpfr(0)
    for r in rows:
        yv = mpfr(r["y_lambda"])
        P += yv * mpfr(r["tr_rho_Omega2"]); C += yv * mpfr(r["tr_Omega2_ctrl"])
    return P, C


def _worker(args):
    return partition_contribution(*args)


def run_word(gens, n, log, workers=1, checkpoint=None):
    parts = list(partitions(n))
    order = sorted(parts, key=_dim_estimate)
    rows_by = {}
    if checkpoint and os.path.exists(checkpoint):
        for line in open(checkpoint):
            line = line.strip()
            if line:
                rec = json.loads(line)
                rows_by[tuple(rec["lambda"])] = rec
        print(f"{log} resumed {len(rows_by)}/{len(parts)}", flush=True)
    fh = open(checkpoint, "a") if checkpoint else None
    todo = [p for p in order if tuple(p) not in rows_by]
    t0 = time.time(); done = len(rows_by); worst = mpfr(0)

    def rec(res):
        nonlocal done, worst
        row, dP, dC, tr_rO, hc, dim, nnz = res
        rows_by[tuple(row["lambda"])] = row
        worst = max(worst, hc); done += 1
        if fh:
            fh.write(json.dumps(row) + "\n"); fh.flush(); os.fsync(fh.fileno())
        P, _ = _agg(rows_by.values())
        print(f"{log} [{done}/{len(parts)}] {tuple(row['lambda'])} dim={dim} "
              f"P={gmpy2.digits(P,10,8)[0]}e{gmpy2.digits(P,10,8)[1]} {time.time()-t0:.1f}s", flush=True)

    if todo:
        if workers > 1:
            import multiprocessing as mpc
            with mpc.Pool(workers) as pool:
                for res in pool.imap_unordered(_worker, [(p, gens) for p in todo]):
                    rec(res)
        else:
            for p in todo:
                rec(partition_contribution(p, gens))
    if fh:
        fh.close()
    rows = [rows_by[tuple(p)] for p in parts]
    P, C = _agg(rows)
    return rows, P, C, worst


def run_gate():
    from mass_at_3A_proper import atom_braid_word_3A
    print(f"[gate] mpfr backend, precision={gmpy2.get_context().precision} bits", flush=True)
    tri = [int(t[2]) for t in atom_braid_word_3A(1, 2)]
    _rows, P, C, worst = run_word(tri, 9, "[gate]", workers=1)
    committed = json.load(open(os.path.join(os.path.dirname(__file__),
                          "triton-magnus-omega2-sign.witness.json")))["results"]
    Pd = mpfr(committed["P_total"])
    rel = abs(P - Pd) / abs(Pd)
    print(f"[gate] mpfr P={_fmt_decimal(P,12)}  committed={_fmt_decimal(Pd,12)}  rel={_fmt_decimal(rel,3)}")
    assert (P > 0) == (Pd > 0), "sign disagree"
    assert rel < mpfr(10) ** -30, f"P disagrees: {rel}"
    assert abs(C) < _EXACT, "control nonzero"
    print("[gate] PASS — mpfr reproduces the committed triton P_total to <1e-30.")


_ALLOW_CLOBBER = False


def _smap(s):
    """Render a sibling sign for display without inventing one when it is absent."""
    return "?" if s is None else f"{s:+d}"


# The fields the SPARSE probe writes into this same witness path that THIS
# producer does not compute.  Overwriting the file would delete them silently.
_SPARSE_ONLY_FIELDS = (
    "weight_family", "weight_family_note", "headline_pairing",
    "P_total_wenzl", "P_total_wenzl_sign", "P_total_wenzl_note",
    "sign_indefinite_across_partitions", "sign_flip_vs_A3",
)


def _refuse_to_clobber(out):
    """Refuse to overwrite a committed witness carrying fields we cannot produce.

    THE HAZARD, measured 2026-09-12.  Two producers write
    `he4-magnus-omega2-sign.witness.json`: the sparse probe
    (`he4_magnus_omega2_sign_sparse_probe.py`, which the committed witness names
    in its own `scriptFile`) and this one.  The sparse probe emits BOTH weight
    families and declares `headline_pairing = "P_total_wenzl"`.  This producer
    does not mention Wenzl anywhere, so a plain re-run would drop the entire
    Wenzl column and the headline declaration -- the whole basis of the A=4
    weight-family result -- while looking like a routine refresh.

    Guard rather than redirect: which producer SHOULD own this path is a design
    question (this file is 4x faster and describes itself as the same math on a
    different backend, so it may be the intended successor), and that is not an
    agent's call to make by moving a filename.  Refusing loudly loses nothing and
    is reversible; a silent overwrite is neither.

    `--allow-clobber` is the deliberate override, for when the answer is "this
    producer owns the path now".
    """
    if not os.path.exists(out):
        return
    try:
        with open(out) as fh:
            cur = json.load(fh)
    except Exception:
        return
    res = cur.get("results", {})
    lost = [k for k in _SPARSE_ONLY_FIELDS if k in res]
    if not lost:
        return
    owner = cur.get("scriptFile", "(unstated)")
    raise SystemExit(
        f"\nREFUSING to overwrite {os.path.basename(out)}.\n"
        f"  Its own scriptFile names the owner: {owner}\n"
        f"  This producer would DELETE {len(lost)} field(s) it cannot compute:\n"
        + "".join(f"    - {k}\n" for k in lost)
        + "  Among them the Wenzl/Ocneanu column and the headline-pairing\n"
        "  declaration, which is the A=4 weight-family result itself.\n"
        "  Run the sparse probe to refresh this witness, or pass\n"
        "  --allow-clobber if this producer is meant to own the path now.\n"
    )


def _sibling_sign(path):
    """Plancherel `P_total_sign` from a committed sibling witness, or None.

    Mirrors `he4_magnus_omega2_sign_sparse_probe.py::_sign` deliberately: the
    cross-A signs are MEASURED data held in the A=2 and A=3 witnesses, never
    constants.  Hardcoding them is how this file came to assert
    `A3_P_total_sign = -1` while the triton witness it loads in `run_gate()`
    records `P_total_sign = 1`.
    """
    try:
        with open(os.path.join(os.path.dirname(__file__), path)) as fh:
            return int(json.load(fh)["results"]["P_total_sign"])
    except Exception:
        return None


def run_he4(workers, checkpoint):
    from mass_at_3A_proper import atom_braid_word_3A
    gens = [int(t[2]) for t in atom_braid_word_3A(2, 2)]
    a2_sign = _sibling_sign("deuteron-magnus-omega2-sign.witness.json")
    a3_sign = _sibling_sign("triton-magnus-omega2-sign.witness.json")
    if checkpoint is None:
        checkpoint = os.path.join(os.path.dirname(__file__), "he4-magnus-mpfr.checkpoint.jsonl")
    rows, P, C, worst = run_word(gens, 12, "[he4mpfr]", workers=workers, checkpoint=checkpoint)
    P_sign = 0 if abs(P) < _EXACT else (1 if P > 0 else -1)
    ctrl_ok = abs(C) < _EXACT
    npos = sum(1 for r in rows if mpfr(r["tr_rho_Omega2"]) > _EXACT)
    nneg = sum(1 for r in rows if mpfr(r["tr_rho_Omega2"]) < -_EXACT)
    witness = {
        "computation": "he4-magnus-omega2-sign",
        "scriptFile": "he4_magnus_mpfr_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": f"gmpy2.mpfr at {_PREC} bits (=140 dp); sparse H₁₂; 4x mpmath.mpf; 0 free params",
        "free_parameters": 0,
        "results": {
            "per_partition": rows, "P_total": fmt(P), "P_total_sign": P_sign,
            "P_control_rho_identity": fmt(C), "control_tr_M_Omega2_vanishes": bool(ctrl_ok),
            "n_partitions_positive": npos, "n_partitions_negative": nneg,
            "A2_P_total_sign": a2_sign, "A3_P_total_sign": a3_sign,
            "sign_vs_A": {"A2": a2_sign, "A3": a3_sign, "A4": P_sign},
            "germ_hecke_check_worst_residual": fmt(worst),
        },
        "verdict": (f"A=4 EXACT (mpfr): P(A=4)={_fmt_decimal(P,10)}, sign={P_sign:+d}. "
                    f"Map A2/A3/A4 = {_smap(a2_sign)}/{_smap(a3_sign)}/{P_sign:+d} "
                    f"(A2, A3 read from the committed sibling witnesses, not assumed). "
                    f"QUANTUM-PLANCHEREL arm only -- this producer does not compute the "
                    f"Wenzl/Ocneanu column, so it is NOT the headline pairing the sparse "
                    f"probe declares. Control tr(Ω₂)=0 holds "
                    f"({ctrl_ok}); per-partition {npos}+/{nneg}-. scope-(a)."),
        "scope": "scope-(a): A=4 sign of tr_M(ρ·Ω₂). No MeV; nothing wired.",
        "wired": False,
    }
    try:
        from qou_substrate.witness import WitnessBuilder as _WB
        _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=None)
    except Exception:
        pass
    out = os.path.join(os.path.dirname(__file__), "he4-magnus-omega2-sign.witness.json")
    if not _ALLOW_CLOBBER:
        _refuse_to_clobber(out)
    with open(out, "w") as f:
        json.dump(witness, f, indent=1); f.write("\n")
    print(f"\nP(A=4) = {_fmt_decimal(P,10)}   sign={P_sign:+d}   (per-partition {npos}+/{nneg}-)")
    print(f"control (must be 0) = {_fmt_decimal(C,6)} -> {ctrl_ok}")
    print(f"sign-vs-A: A2={_smap(a2_sign)} A3={_smap(a3_sign)} A4={P_sign:+d}  "
          f"(A2/A3 from the committed witnesses)")
    print(f"wrote {out}")
    assert ctrl_ok, "control must vanish"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--skip-gate", action="store_true")
    ap.add_argument("--checkpoint", default=None)
    ap.add_argument("--allow-clobber", action="store_true",
                    help="overwrite the committed witness even though this producer "
                         "cannot emit the Wenzl column the sparse probe writes there")
    args = ap.parse_args()
    global _ALLOW_CLOBBER
    _ALLOW_CLOBBER = args.allow_clobber
    if args.gate:
        run_gate(); return
    if not args.skip_gate:
        run_gate()
    run_he4(args.workers, args.checkpoint)


if __name__ == "__main__":
    main()
