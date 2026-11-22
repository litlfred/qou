#!/usr/bin/env python3
"""Symbolic chi^lambda_q(beta_atom) by the SYT path sum: fast exact rebuild of the
`chi-<atom>-h<n>.witness.json` caches.

WHY. `per_irrep_pole_atom` builds the caches by multiplying full symbolic
Hoefsmit matrices (`hecke_character_symbolic`), whose cost grows with dim V_lambda.
Measured 2026-11-20: at H_9 the shape (7,2) (dim 27) took 1070 s on 2 cores and
the largest H_9 irreps have dim 216, so a full tritium / helium-3 rebuild would
take days. `chi_path_sum_seminormal.py` already proves (and cross-checks at 50
dps) that for the level-local atom word chi^lambda is a path sum over standard
tableaux that never builds V_lambda; it is numeric (mpmath). This file is the
same contraction over Q(q) with sympy, so it returns the exact rational function
the caches store.

ONE CHANGE OF BASIS. The numeric path sum uses the orthogonal (symmetric)
seminormal form, whose off-diagonal entries are b = sqrt(a*a' + 1). Over Q(q) a
square root would have to be simplified away. Young's natural seminormal form
puts 1 and b^2 = a*a' + 1 on the two off-diagonal slots instead; it is the
orthogonal form conjugated by a diagonal matrix, so every trace, and therefore
every chi, is unchanged. The orientation rule is fixed by `--selftest`, which
compares against an independent build.

CONVENTION, identical to `hecke_character_symbolic._q_character_compute`:
a crossing of type c contributes rho(sigma_g) + d_for_ctype(c, h, delta=
flavor_split_leading(q)) * I, with crossings (gen_idx, ctype), gen_idx 0-based.

Usage:
    python3 chi_path_sum_symbolic.py --selftest
    python3 chi_path_sum_symbolic.py tritium helium-3 [--write]
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
for _p in (HERE, HERE / "substrate", HERE / "hecke"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from canonical_braid_crossings import d_for_ctype  # noqa: E402
from chi_path_sum_seminormal import (  # noqa: E402
    _addable, _content, _fillings, _swap_standard, segments_of,
)

Q = sp.Symbol("q")


class SymSegment:
    """<T | F_seg | T> over Q(q) in Young's natural seminormal form."""

    def __init__(self, gens, letters, shifts, orient):
        self.gens, self.letters, self.shifts = gens, letters, shifts
        self.a, self.b = gens[0], gens[-1]
        self.orient = orient
        self.h = Q - 1 / Q
        self._cache = {}

    def _orbit(self, boxes):
        idx, nodes, k = {boxes: 0}, [boxes], 0
        while k < len(nodes):
            t = nodes[k]
            k += 1
            for g in self.gens:
                i = g - self.a
                if _swap_standard(t[i], t[i + 1]):
                    u = list(t)
                    u[i], u[i + 1] = u[i + 1], u[i]
                    u = tuple(u)
                    if u not in idx:
                        idx[u] = len(nodes)
                        nodes.append(u)
        return nodes, idx

    def _gen_rows(self, g, nodes, idx):
        i = g - self.a
        h = self.h
        rows = []
        for t in nodes:
            rho = _content(t[i + 1]) - _content(t[i])
            a = sp.cancel(h / (1 - Q ** (-2 * rho)))
            if _swap_standard(t[i], t[i + 1]):
                u = list(t)
                u[i], u[i + 1] = u[i + 1], u[i]
                j = idx[tuple(u)]
                ap = sp.cancel(h / (1 - Q ** (2 * rho)))
                bsq = sp.cancel(a * ap + 1)
                # Natural form: one off-diagonal slot 1, the other b^2. Which
                # slot gets which is the orientation, fixed per pair by the
                # rows of the two entries in t.
                lower = t[i + 1][0] > t[i][0]
                off = bsq if (lower == self.orient) else sp.Integer(1)
                rows.append((a, j, off))
            else:
                rows.append((a, None, None))
        return rows

    def weight(self, boxes):
        w = self._cache.get(boxes)
        if w is not None:
            return w
        nodes, idx = self._orbit(boxes)
        mats = {g: self._gen_rows(g, nodes, idx) for g in self.gens}
        v = [sp.Integer(0)] * len(nodes)
        v[0] = sp.Integer(1)
        # v <- F_seg e_T, letters applied right to left; diagonal = v[0].
        for pos in range(len(self.letters) - 1, -1, -1):
            g = self.letters[pos][1]
            d = self.shifts[pos]
            new = []
            for (a, j, off) in mats[g]:
                x = (a + d) * v[len(new)]
                if j is not None:
                    x += off * v[j]
                new.append(sp.cancel(x))
            v = new
        self._cache[boxes] = v[0]
        return v[0]


def build(crossings, orient=True):
    from _li_2_q_util import flavor_split_leading
    h = Q - 1 / Q
    delta = flavor_split_leading(Q)
    word = [(0, g + 1) for g, _ct in crossings]  # sign unused; shifts carry it
    shifts_all = [sp.cancel(d_for_ctype(ct, h, delta=delta)) for _g, ct in crossings]
    segs = []
    for sg in segments_of(word):
        sh = [shifts_all[p] for p in range(sg["start"], sg["end"] + 1)]
        segs.append(SymSegment(sg["gens"], sg["letters"], sh, orient))
    return segs


def chi_lambda(shape, n, segs):
    lam = tuple(shape)
    states = {((), None): sp.Integer(1)}
    k = 0

    def advance(states):
        nxt = {}
        for (sh, _bx), wgt in states.items():
            for new, box in _addable(sh, lam):
                key = (new, box)
                nxt[key] = nxt.get(key, sp.Integer(0)) + wgt
        return nxt

    for sw in segs:
        while k < sw.a:
            states = advance(states)
            k += 1
        nxt = {}
        for (sh, bx), wgt in states.items():
            for fin, boxes in _fillings(sh, lam, sw.b + 1 - sw.a):
                w = sw.weight((bx,) + boxes)
                if w == 0:
                    continue
                key = (fin, boxes[-1])
                nxt[key] = nxt.get(key, sp.Integer(0)) + wgt * w
        states = {kk: sp.cancel(vv) for kk, vv in nxt.items()}
        k = sw.b + 1
    while k < n:
        states = advance(states)
        k += 1
    return sp.cancel(sum((w for (sh, _b), w in states.items() if sh == lam),
                         sp.Integer(0)))


def _reference(Z, N, atom, cr):
    """Hoefsmit-matrix chi for every lambda: the committed cache when it was
    built from this ordered word, else a direct `chi_lambda_symbolic` build."""
    from canonical_braid_crossings import word_fingerprint
    from hoefsmit_symbolic import chi_lambda_symbolic
    from per_irrep_pole_atom import parts_of
    n = 3 * (Z + N)
    path = HERE / f"chi-{atom}-h{n}.witness.json"
    if path.exists():
        d = json.loads(path.read_text())
        if d.get("word_fingerprint") == word_fingerprint(cr):
            return {tuple(e["partition"]): sp.sympify(e["chi_q_symbolic"], locals={"q": Q})
                    for e in d["chi_lambda_symbolic"]}
    out = {}
    for lam in parts_of(n):
        ref = chi_lambda_symbolic(lam, cr)
        out[tuple(lam)] = ref.subs({s_: Q for s_ in ref.free_symbols})
    return out


def _selftest() -> int:
    """Against the Hoefsmit-matrix build on every partition of the proton,
    neutron (n=3) and deuteron (n=6), plus every cached tritium partition."""
    from canonical_braid_crossings import atom_canonical_crossings
    results = {}
    cases = (("proton", 1, 0), ("neutron", 0, 1), ("deuteron", 1, 1), ("tritium", 1, 2))
    refs = {}
    for atom, Z, N in cases:
        cr = atom_canonical_crossings(Z, N)
        if atom == "tritium":
            from canonical_braid_crossings import word_fingerprint
            d = json.loads((HERE / "chi-tritium-h9.witness.json").read_text())
            if d.get("word_fingerprint") != word_fingerprint(cr):
                continue
            refs[atom] = (cr, 9, {tuple(e["partition"]): sp.sympify(e["chi_q_symbolic"], locals={"q": Q})
                                  for e in d["chi_lambda_symbolic"]})
        else:
            refs[atom] = (cr, 3 * (Z + N), _reference(Z, N, atom, cr))
    for orient in (True, False):
        ok, checked = True, 0
        for atom, (cr, n, ref) in refs.items():
            segs = build(cr, orient)
            for lam, r in ref.items():
                got = chi_lambda(lam, n, segs)
                checked += 1
                if sp.cancel(r - got) != 0:
                    ok = False
                    print(f"  orient={orient} MISMATCH {atom} {lam}", flush=True)
                    break
            if not ok:
                break
        results[orient] = ok
        print(f"orient={orient}: {'PASS' if ok else 'FAIL'} ({checked} partitions)", flush=True)
    return 0 if any(results.values()) else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("atoms", nargs="*")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--orient", choices=["true", "false"], default="true")
    ap.add_argument("--write", action="store_true",
                    help="write chi-<atom>-h<n>.witness.json")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(_selftest())
    from canonical_braid_crossings import atom_canonical_crossings
    from per_irrep_pole_atom import ATOMS, ATOM_ALIASES, parts_of
    for raw in args.atoms:
        atom = ATOM_ALIASES.get(raw, raw)
        Z, N = ATOMS[atom]
        cr = atom_canonical_crossings(Z, N)
        n = 3 * (Z + N)
        segs = build(cr, args.orient == "true")
        t0 = time.time()
        out = {}
        for lam in parts_of(n):
            t1 = time.time()
            out[lam] = chi_lambda(lam, n, segs)
            print(f"  {atom} {lam}: {time.time()-t1:.1f}s", flush=True)
        print(f"{atom}: {len(out)} partitions in {time.time()-t0:.1f}s", flush=True)
        dump = Path(f"/tmp/chi_path_sum_{atom}.json")
        dump.write_text(json.dumps({str(list(k)): str(v) for k, v in out.items()}))
        print(f"  -> {dump}")
        if args.write:
            write_cache(atom, Z, N, n, out, time.time() - t0)


def write_cache(atom, Z, N, n, out, elapsed):
    """Write `chi-<atom>-h<n>.witness.json` in per_irrep_pole_atom's format
    (same writer, so the ordered-word guard and q0Anchor stamp are identical),
    then record which backend produced it."""
    from per_irrep_pole_atom import _write_chi_cache
    path = HERE / f"chi-{atom}-h{n}.witness.json"
    _write_chi_cache(path, atom, Z, N, n, {k: str(v) for k, v in out.items()},
                     elapsed, 1, partial=False)
    d = json.loads(path.read_text())
    d["backend"] = ("chi_path_sum_symbolic.py: SYT path sum over Q(q), Young natural "
                    "seminormal form; equal to the Hoefsmit-matrix build on every "
                    "partition checked by --selftest")
    path.write_text(json.dumps(d, indent=2, ensure_ascii=False))
    print(f"  wrote {path.name}")
