#!/usr/bin/env python3
"""Hyperbolic volumes of the braid closures of the γγ atom-word candidates.

Pre-registration: `preregistration.md` (this directory), pushed before any
volume was computed. Adopts nothing.

Word (generators 0-indexed): V = σ_a σ_{a+1}^{-1}.
  nucleon k : V^m on (3k, 3k+1), m ∈ {3, 6};
  free      : nucleon blocks only;
  atom L/R  : after nucleon k < A−1, bond (default V³) on (3k+1, 3k+2) [L]
              or (3k+2, 3k+3) [R].

The bond is a parameter (`bond_power`; the arm fixes the site) so bond words admitted by
the reading-3 derivation can be added later as a new pre-registered run.

Volumes are SnapPy floating point: `volume()` (double) and `ManifoldHP`
(quad-double). A verified interval volume needs SnapPy inside Sage; when that
is unavailable it is reported as unavailable, not substituted.

Usage:
    python3 -u computations/probes/gg_atom_word_volumes/gg_atom_word_volumes_probe.py \
        2>&1 | tee /tmp/gg_atom_word_volumes.log
"""
from __future__ import annotations

import sys
import time
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from substrate.knot_volumes import VOL_BORROMEAN_MPF, VOL_8_11_MPF  # noqa: E402

warnings.filterwarnings("ignore")
try:
    import snappy  # noqa: E402
except ImportError:
    print("SKIP: snappy not installed (pip install snappy)")
    sys.exit(0)
try:
    import regina  # noqa: E402
except ImportError:
    regina = None

GOOD = "all tetrahedra positively oriented"
TRIES = 12
RECOGNISE_TRIES = 40
mp.mp.dps = 50

# Production VOL_K of binding_a3plus_full_theta_assembly.py, by A.
PRODUCTION = {
    2: ("D: Vol(Borromean)", VOL_BORROMEAN_MPF),
    3: ("T: Vol(8_11); 3He: Vol(Borromean)", None),
    4: ("4He: 2*Vol(Borromean)", 2 * VOL_BORROMEAN_MPF),
}


def block(a: int, power: int) -> list[int]:
    """(σ_a σ_{a+1}^{-1})^power, 1-indexed signed generators."""
    return [a + 1, -(a + 2)] * power


def word(A: int, nucleon_power: int, arm: str | None,
         bond_power: int = 3) -> list[int]:
    w: list[int] = []
    for k in range(A):
        w += block(3 * k, nucleon_power)
        if arm is not None and k < A - 1:
            w += block(3 * k + 1 if arm == "L" else 3 * k + 2, bond_power)
    return w


def geometry(link) -> dict:
    """Hyperbolic structure of one non-split link, with retries."""
    M = link.exterior()
    sol, vol = M.solution_type(), None
    for _ in range(TRIES):
        sol = M.solution_type()
        if sol == GOOD:
            vol = M.volume()
            break
        M.randomize()
    out = {"solution_type": sol, "hyperbolic": sol == GOOD}
    if sol == GOOD:
        MH = snappy.ManifoldHP(M)
        hp_sol = MH.solution_type()
        out["volume_double"] = str(vol)
        out["volume_hp"] = str(MH.volume()) if hp_sol == GOOD else None
        out["hp_solution_type"] = hp_sol
        try:
            out["identify"] = [str(x) for x in M.identify()]
        except Exception as e:  # noqa: BLE001
            out["identify"] = f"failed: {type(e).__name__}"
    else:
        out["volume_double"] = None
        out["volume_hp"] = None
        out["identify"] = []
    return out


def _sol(N) -> tuple[str, object]:
    for _ in range(TRIES):
        if N.solution_type() == GOOD:
            return GOOD, N
        N.randomize()
    return N.solution_type(), N


def jsj(M, depth: int = 0) -> dict:
    """Cut a SnapPy manifold along essential tori found by Regina.

    Hyperbolic pieces are reported with SnapPy volumes (floating point).
    Non-hyperbolic pieces are searched for a closed, connected, orientable,
    non-vertex-linking normal torus (standard coordinates, vertex surfaces)
    that Regina's exact `isIncompressible()` accepts; the piece is cut along it
    and each half recursed on. A piece with no such torus is passed to
    Regina's `StandardTriangulation.recognise` (Seifert-fibred recognition).
    The decomposition is computational evidence: Regina's surface steps are
    exact, SnapPy's hyperbolicity is floating point and uncertified.
    """
    sol, N = _sol(M)
    if sol == GOOD:
        MH = snappy.ManifoldHP(N)
        return {"kind": "hyperbolic", "cusps": N.num_cusps(),
                "volume_hp": str(MH.volume()) if MH.solution_type() == GOOD else None,
                "volume_double": str(N.volume()),
                "identify": [str(x) for x in N.identify()]}
    if regina is None or depth > 4:
        return {"kind": "unresolved", "solution_type": sol,
                "reason": "regina unavailable" if regina is None else "depth"}
    T = regina.Triangulation3(N._to_string())
    ns = regina.NormalSurfaces(T, regina.NS_STANDARD)
    for s in ns:
        if not (s.isCompact() and s.isConnected() and s.isOrientable()
                and s.eulerChar() == 0 and not s.isVertexLinking()
                and not s.hasRealBoundary()):
            continue
        if not s.isIncompressible():
            continue
        parts = []
        for P in s.cutAlong().triangulateComponents():
            P = regina.Triangulation3(P)
            # T^2 x I guard: a boundary-parallel torus leaves a piece with two
            # torus boundaries and H1 = Z^2.
            if (P.countBoundaryComponents() == 2
                    and P.homology().str() == "2 Z"):
                parts = None
                break
            parts.append(P)
        if not parts:
            continue
        pieces = []
        for P in parts:
            Q = regina.Triangulation3(P)
            Q.finiteToIdeal()
            Q.intelligentSimplify()
            pieces.append(jsj(snappy.Manifold(Q.snapPea()), depth + 1))
        return {"kind": "cut_along_essential_torus", "pieces": pieces}
    name = None
    for _ in range(RECOGNISE_TRIES):
        F = regina.Triangulation3(N._to_string())
        F.idealToFinite()
        F.intelligentSimplify()
        st = regina.StandardTriangulation.recognise(F)
        if st is not None:
            m = st.manifold()
            name = m.name() if m is not None else st.name()
            if _is_sfs(name):
                break
        N.randomize()
    return {"kind": "seifert_fibred" if _is_sfs(name) else "unresolved",
            "solution_type": sol, "regina_recognised": name,
            "cusps": N.num_cusps()}


def _is_sfs(name: str | None) -> bool:
    """Regina names a Seifert-fibred space either `SFS [...]` or `<base> x S1`."""
    return bool(name) and (name.startswith("SFS") or name.endswith("x S1"))


def hyperbolic_sum(node: dict) -> tuple[object, bool]:
    """Sum of hyperbolic JSJ-piece volumes; False if any piece unresolved."""
    k = node["kind"]
    if k == "hyperbolic":
        return (mp.mpf(node["volume_hp"]), True) if node["volume_hp"] else (mp.mpf(0), False)
    if k == "seifert_fibred":
        return mp.mpf(0), True
    if k == "cut_along_essential_torus":
        tot, ok = mp.mpf(0), True
        for p in node["pieces"]:
            v, o = hyperbolic_sum(p)
            tot += v
            ok = ok and o
        return tot, ok
    return mp.mpf(0), False


def analyse(w: list[int]) -> dict:
    L = snappy.Link(braid_closure=w)
    rec: dict = {"word": w, "letters": len(w),
                 "components": len(L.link_components),
                 "crossings": len(L.crossings)}
    pieces = L.split_link_diagram()
    rec["split"] = len(pieces) > 1
    rec["n_split_pieces"] = len(pieces)
    if rec["split"]:
        rec["whole"] = {"hyperbolic": False,
                        "reason": "split link: complement contains an essential sphere"}
        rec["pieces"] = [dict(components=len(P.link_components), **geometry(P))
                         for P in pieces]
    else:
        rec["whole"] = geometry(L)
    # Simplicial-volume bookkeeping: split pieces -> prime summands -> JSJ.
    # v3·||M|| = sum of hyperbolic JSJ-piece volumes (Gromov–Thurston); it is
    # additive under split union and connected sum. It is NOT a hyperbolic
    # volume of the closure unless the closure is itself hyperbolic.
    primes = []
    for P in (pieces if rec["split"] else [L]):
        try:
            ds = P.deconnect_sum()
        except Exception:  # noqa: BLE001
            ds = [P]
        primes += ds
    rec["n_prime_pieces"] = len(primes)
    rec["prime_pieces"] = []
    tot, ok = mp.mpf(0), True
    for P in primes:
        node = jsj(P.exterior())
        node["components"] = len(P.link_components)
        v, o = hyperbolic_sum(node)
        node["hyperbolic_jsj_volume_sum_hp"] = str(v) if o else None
        rec["prime_pieces"].append(node)
        tot += v
        ok = ok and o
    rec["v3_simplicial_volume_hp"] = str(tot) if ok else None
    return rec


def main() -> int:
    t0 = time.time()
    try:
        snappy.Manifold("m004").volume(verified=True)
        verified = "available"
    except Exception as e:  # noqa: BLE001
        verified = f"unavailable ({type(e).__name__}: needs SnapPy inside Sage)"
    print(f"snappy {snappy.__version__}; verified volume {verified}", flush=True)

    words: dict[str, tuple[int, list[int]]] = {
        "N3": (1, word(1, 3, None)), "N6": (1, word(1, 6, None))}
    for m in (3, 6):
        for A in (2, 3, 4):
            words[f"F{m}-A{A}"] = (A, word(A, m, None))
    for m in (3, 6):
        for arm in ("L", "R"):
            for A in (2, 3, 4):
                words[f"{arm}{m}-A{A}"] = (A, word(A, m, arm))
    assert len(words) == 20, len(words)

    results = {}
    for wid, (A, w) in words.items():
        t = time.time()
        r = analyse(w)
        r["A"] = A
        if A in PRODUCTION:
            r["production_vol_k"] = PRODUCTION[A][0]
        results[wid] = r
        whole = r["whole"]
        print(f"{wid:7s} comp={r['components']:2d} split={r['split']!s:5s} "
              f"hyp={whole.get('hyperbolic')!s:5s} "
              f"vol={whole.get('volume_hp')} "
              f"primes={r['n_prime_pieces']} kinds={[q['kind'] for q in r['prime_pieces']]} "
              f"v3||M||={r['v3_simplicial_volume_hp']} "
              f"id={whole.get('identify')} ({time.time() - t:.1f}s)", flush=True)

    n3 = mp.mpf(results["N3"]["whole"]["volume_hp"])
    borro_gap = abs(n3 - VOL_BORROMEAN_MPF)
    print(f"N3 HP vs 8G: |diff| = {mp.nstr(borro_gap, 5)}", flush=True)

    wb = WitnessBuilder("gg-atom-word-volumes", engine=f"snappy {snappy.__version__}",
                        output_dir=HERE)
    wb.set_description(
        "Hyperbolic volumes (SnapPy floating point) of the braid closures of the "
        "gamma-gamma candidate atom words: nucleon V^3/V^6 with V = s_a s_{a+1}^-1, "
        "free blocks and bonded atoms (bond V^3, site arms L/R), A = 1..4. Adopts "
        "nothing; compares with the production VOL_K of the A>=3 chain.")
    wb.add_data("verified_volume", verified)
    wb.add_data("production_vol_k", {
        "D": str(VOL_BORROMEAN_MPF), "T": str(VOL_8_11_MPF),
        "3He": str(VOL_BORROMEAN_MPF), "4He": str(2 * VOL_BORROMEAN_MPF)})
    wb.add_data("results", results)
    wb.add_data("borromean_8G_50dps", str(VOL_BORROMEAN_MPF))
    wb.add_data("n3_hp_minus_8G_abs", mp.nstr(borro_gap, 5))
    wb.add_assertion("n3_is_borromean_to_hp_precision",
                     computed=mp.nstr(borro_gap, 5), expected="0", tolerance="1e-50",
                     source="SnapPy ManifoldHP vs 8*Catalan at 50 dps")
    # Double vs quad-double agreement on every hyperbolic piece (floating point
    # vs floating point: this bounds the double's error, it certifies nothing).
    def _walk(n):
        if n["kind"] == "hyperbolic" and n.get("volume_hp"):
            yield n
        for q in n.get("pieces", []):
            yield from _walk(q)
    worst = mp.mpf(0)
    for r in results.values():
        for pp in r["prime_pieces"]:
            for h in _walk(pp):
                hp, db = mp.mpf(h["volume_hp"]), mp.mpf(h["volume_double"])
                worst = max(worst, abs(hp - db) / hp)
    print(f"max rel |double - HP| over hyperbolic pieces: {mp.nstr(worst, 3)}", flush=True)
    wb.add_data("max_rel_double_vs_hp", mp.nstr(worst, 5))
    ratios = {wid: mp.nstr(mp.mpf(r["v3_simplicial_volume_hp"]) / VOL_BORROMEAN_MPF, 30)
              for wid, r in results.items() if r["v3_simplicial_volume_hp"]}
    wb.add_data("v3_simplicial_volume_over_8G", ratios)
    wb.add_assertion("all_twenty_words_computed", computed=len(results), expected=20,
                     tolerance=0, source="preregistration.md word list")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": (
                 "Topology only: braid-closure link complements, SnapPy "
                 "hyperbolic volumes and Regina JSJ cuts. No q_parameter / "
                 "q_at import and no q0 literal; the only corpus constant read "
                 "is Vol(Borromean) = 8G from substrate.knot_volumes.")})
    print(f"total {time.time() - t0:.0f}s; witness written", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
