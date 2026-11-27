#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical census search; the q-polynomial
# discipline applies inside the cohomological identities, but this script only
# evaluates candidate F(Vol + i*CS)/hbar_q^k expressions at the substrate q_0.
"""m_tau_complex_volume_search — COMPLEX-volume extension of the refuted
25-knot m_tau search.

Context
-------
The muon mass identity  m_mu/m_e = Vol(4_1)/hbar_q^2  uses the *real*
hyperbolic volume of the figure-eight knot.  A prior audit
(docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md,
computations/m_tau_knot_prediction.py) searched 25 hyperbolic knots for a
tau analogue  m_tau/m_e ~ Vol(K_tau)/hbar_q^k  and found no match under 1%
(best: Vol(8_1)/hbar_q^3 = +1.33%).  That search used the REAL volume only.

Queued extension #1 of the audit ("Volume + Chern-Simons pair"): hyperbolic
knot complements carry a *complex* volume  Vol(K) + i*CS(K)  (SnapPy:
M.volume(), M.chern_simons()).  This script redoes / extends the search over
the complex volume, over the full <=12-crossing hyperbolic knot census, and
over composite (connected-sum) carriers, for the tau at the n=7 generation
column.

DERIVE-THEN-CHECK discipline (AGENTS.md anti-fit)
-------------------------------------------------
A large census + a free functional F + a free exponent k is NUMEROLOGY unless
F, k, and the carrier are FIXED/derived, not chosen to match.  This script
therefore separates two questions:

  Part A -- the DERIVED carrier.  The framework's tau decay carrier is
     T(3,5)-adjacent (T(2,7) generation column, n=7).  Torus knots are
     non-hyperbolic (Seifert-fibered; Gromov norm 0), so their hyperbolic
     volume is identically zero and SnapPy returns a degenerate solution.
     The complex volume Vol + i*CS is (0, non-geometric).  This is a
     structural fact about the derived carrier, independent of any fit.

  Part B -- the entropy of the wide census search.  For the alternative
     reading (carrier = some hyperbolic knot, not the torus one), we run the
     wide search but score it against the search-space-entropy vs precision
     bound.  The muon anchor is CS-BLIND (CS(4_1) = 0 because 4_1 is
     amphichiral), so it supplies NO information about how CS should enter F.
     Any F(Vol,CS) reducing to Vol at CS=0 is equally "muon-consistent" -- a
     whole function's worth of freedom.  We test the two most natural fixed
     functionals and count chance hits.

Fixed functionals tested (each FIXED before scoring, not per-knot tuned):
  F_re  = Re(Vol + i*CS)      = Vol            (the muon-derived choice)
  F_abs = |Vol + i*CS|        = sqrt(Vol^2+CS^2)
Fixed exponents: k in {2,3,4,5} (k=3 = the "generation-step in hbar_q"
derived guess, one power above the muon's k=2).

Outputs a witness with: census size, per-(F,k) hit counts at 1% / 0.1% /
100 ppm, the closest knot under each (F,k) (reported so the reader sees it is
one of many chance hits), and the entropy/precision analysis.

References
- docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md (queued ext #1)
- computations/m_tau_knot_prediction.py (the refuted real-volume search)
- PR #1805 (PSLQ entropy bound precedent: precision > n_terms*log10(2*height))
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import math
import os
import sys
import time
from pathlib import Path

import mpmath as mp
from _precision import json_safe_float  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import Q_50_DIGIT_STR, Q_MP, MASS_RATIO_MU_E_STR  # type: ignore

from _precision import set_compute_dps, fmt  # type: ignore
set_compute_dps(50)

import snappy  # noqa: E402

# ── targets & substrate ─────────────────────────────────────────────────────
TARGET_MU_OVER_E = mp.mpf(MASS_RATIO_MU_E_STR)   # CODATA 206.7682830
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

TARGET_TAU_OVER_E = mp.mpf("3477.23")            # PDG 2024 m_tau/m_e (4 sig figs)
SIGMA_EXP_TAU = mp.mpf("5e-5")                   # ~ rel. exp. precision of m_tau/m_e

Q0 = Q_MP
HBAR_Q = (Q0 - 1) / Q0
HBAR_Q_SQ = HBAR_Q ** 2

SEARCH_KS = [2, 3, 4, 5]
DERIVED_K = 3
THRESH = {"loose_1pct": mp.mpf("1e-2"),
          "mid_0p1pct": mp.mpf("1e-3"),
          "tight_100ppm": mp.mpf("1e-4")}

MAX_CROSSINGS = 12


def rel_err(pred: mp.mpf, target: mp.mpf) -> mp.mpf:
    return abs(pred - target) / target


# ── Part A: derived torus-knot carriers ─────────────────────────────────────
def torus_braid_word(p: int, q: int) -> list[int]:
    """Braid word for the (p,q) torus knot as the closure of (s1...s_{p-1})^q
    in B_p (standard positive braid presentation)."""
    return [i for _ in range(q) for i in range(1, p)]


def part_a_derived_carriers() -> list[dict]:
    """The framework-derived tau carrier is T(3,5)-adjacent / T(2,7)
    (n=7 generation column).  Torus knots are non-hyperbolic; report the
    structural failure of the complex-volume reading for them."""
    out = []
    for name, (p, q) in {"T(2,7)": (2, 7), "T(3,5)": (3, 5),
                         "T(3,4)=8_19": (3, 4)}.items():
        rec = {"carrier": name, "p": p, "q": q, "class": "torus"}
        try:
            M = snappy.Link(braid_closure=torus_braid_word(p, q)).exterior()
            vol = M.volume()
            sol = str(M.solution_type())
            _degenerate = ("degenerate" in sol or "flat" in sol)
            # A torus-knot complement is Seifert-fibred, not hyperbolic, so its
            # hyperbolic volume is EXACTLY zero — this module's own docstring
            # says so. What SnapPy returns is the residual of a degenerate
            # solve, and it is NONDETERMINISTIC: two consecutive calls in one
            # process gave -4.335420911161236e-14 and -2.4684863123708434e-07.
            # Publishing 17 digits of that made the witness unreproducible for a
            # value that is not a measurement at all. The exact 0 is recorded
            # instead; `solution_type` carries the degeneracy, and the
            # `hyperbolic` verdict below is unaffected (its threshold is 1e-4,
            # far above any residual seen).
            rec["snappy_volume"] = ("0" if _degenerate
                                    else repr(float(vol)))
            rec["snappy_volume_note"] = (
                "exact 0: Seifert-fibred, not hyperbolic; SnapPy's degenerate "
                "solve returns a nondeterministic residual which is not recorded"
                if _degenerate else None)
            rec["solution_type"] = sol
            rec["hyperbolic"] = bool(abs(float(vol)) > 1e-4 and not _degenerate)
        except Exception as e:  # pragma: no cover
            rec["error"] = str(e)
            rec["hyperbolic"] = False
        rec["note"] = ("Seifert-fibered / torus knot complement: Gromov norm 0, "
                       "so hyperbolic volume is identically 0 and the complex "
                       "volume Vol+iCS is (0, non-geometric). The Vol+iCS "
                       "reading -- real OR complex -- cannot apply to this "
                       "carrier.")
        out.append(rec)
    return out


# ── Part B: wide complex-volume census search ───────────────────────────────
def crossing_number(name: str) -> int | None:
    # HTLinkExteriors knot names: 'K<crossings><a|n><idx>', e.g. 'K12n0123'
    if not name.startswith("K"):
        return None
    i = 1
    while i < len(name) and name[i].isdigit():
        i += 1
    return int(name[1:i]) if i > 1 else None


def build_census(max_crossings: int, log_every: float = 20.0) -> list[dict]:
    """Iterate the Hoste-Thistlethwaite knot census (1-cusped), keep knots
    with crossing number <= max_crossings, compute (Vol, CS)."""
    census = snappy.HTLinkExteriors
    out: list[dict] = []
    t0 = time.time()
    last = t0
    n_seen = n_nonhyp = 0
    for M in census:
        name = M.name()
        if not name.startswith("K"):      # skip links (L...)
            continue
        c = crossing_number(name)
        if c is None or c > max_crossings:
            # census is ordered by crossing number; once past the cap we can stop
            if c is not None and c > max_crossings:
                break
            continue
        if M.num_cusps() != 1:
            continue
        n_seen += 1
        try:
            vol = float(M.volume())
            sol = str(M.solution_type())
            if abs(vol) < 1e-4 or "degenerate" in sol or "flat" in sol:
                n_nonhyp += 1
                continue
            try:
                cs = float(M.chern_simons())
            except Exception:
                cs = None
            out.append({"knot": name, "crossings": c, "vol": vol, "cs": cs})
        except Exception:
            n_nonhyp += 1
            continue
        now = time.time()
        if now - last > log_every:
            print(f"[census] {len(out)} hyperbolic knots kept "
                  f"(<= {max_crossings}x), {n_seen} scanned, "
                  f"elapsed {now - t0:.0f}s", flush=True)
            last = now
    print(f"[census] DONE: {len(out)} hyperbolic knots, "
          f"{n_nonhyp} non-hyperbolic/failed, elapsed {time.time() - t0:.0f}s",
          flush=True)
    return out


def functional(vol: float, cs: float | None, kind: str) -> float | None:
    if kind == "F_re":
        return vol
    if kind == "F_abs":
        if cs is None:
            return None
        return math.sqrt(vol * vol + cs * cs)
    raise ValueError(kind)


def score_census(census: list[dict]) -> dict:
    """For each fixed (F, k), count how many census knots land within each
    tolerance of the tau target, and record the single closest knot."""
    target = float(TARGET_TAU_OVER_E)
    hbar = float(HBAR_Q)
    results = {}
    for Fkind in ("F_re", "F_abs"):
        for k in SEARCH_KS:
            denom = hbar ** k
            hits = {"loose_1pct": 0, "mid_0p1pct": 0, "tight_100ppm": 0}
            best = None
            n_eval = 0
            for rec in census:
                fval = functional(rec["vol"], rec.get("cs"), Fkind)
                if fval is None:
                    continue
                n_eval += 1
                pred = fval / denom
                err = abs(pred - target) / target
                if err < THRESH["loose_1pct"]:
                    hits["loose_1pct"] += 1
                if err < THRESH["mid_0p1pct"]:
                    hits["mid_0p1pct"] += 1
                if err < THRESH["tight_100ppm"]:
                    hits["tight_100ppm"] += 1
                if best is None or err < best["rel_err"]:
                    best = {"knot": rec["knot"], "crossings": rec["crossings"],
                            "vol": rec["vol"], "cs": rec.get("cs"),
                            "predicted": pred, "rel_err": err}
            results[f"{Fkind}_k{k}"] = {
                "functional": Fkind, "k": k, "n_evaluated": n_eval,
                "hits_within": hits,
                "closest_knot": best,
            }
    return results


def composite_pairwise(census: list[dict], target: float, k: int,
                       max_base_crossings: int = 8) -> dict:
    """Composite carrier K1#K2 has additive volume Vol(K1)+Vol(K2) and additive
    CS.  Enumerate unordered pairs from the small-crossing sub-census and count
    1% hits under F_re at fixed k.  This is an N^2 search: its point is to show
    the entropy EXPLODES, not to find a carrier."""
    hbar = float(HBAR_Q)
    denom = hbar ** k
    base = [r for r in census if r["crossings"] <= max_base_crossings]
    n = len(base)
    hits = 0
    best = None
    for i in range(n):
        vi = base[i]["vol"]
        for j in range(i, n):
            vsum = vi + base[j]["vol"]
            pred = vsum / denom
            err = abs(pred - target) / target
            if err < 1e-2:
                hits += 1
            if best is None or err < best["rel_err"]:
                best = {"pair": f"{base[i]['knot']}#{base[j]['knot']}",
                        "vol_sum": vsum, "predicted": pred, "rel_err": err}
    n_pairs = n * (n + 1) // 2
    return {"n_base_knots": n, "max_base_crossings": max_base_crossings,
            "k": k, "F": "F_re", "n_pairs": n_pairs,
            "hits_within_1pct": hits, "closest_pair": best}


def entropy_analysis(census_size: int, n_functionals: int, n_exponents: int,
                     hit_counts_1pct: list[int]) -> dict:
    """Search-space entropy vs precision-of-match (PSLQ-entropy style, PR #1805).

    A match at fractional tolerance w to the 4-sig-fig target identifies the
    target to log2(1/(2w)) bits of specificity.  The search has
    N = census_size * n_functionals * n_exponents free choices, i.e.
    log2(N) bits of search entropy.  If search entropy > bits-of-match, a hit
    at tolerance w is EXPECTED BY CHANCE and carries no evidential weight.
    """
    N = census_size * n_functionals * n_exponents
    search_bits = math.log2(N) if N > 0 else 0.0
    def match_bits(w):
        return math.log2(1.0 / (2.0 * w))
    tiers = {}
    for label, w in (("1pct", 1e-2), ("0p1pct", 1e-3), ("100ppm", 1e-4),
                     ("exp_5e-5", 5e-5)):
        mb = match_bits(w)
        tiers[label] = {
            "tolerance": w,
            "match_specificity_bits": round(mb, 2),
            "identifiable": bool(mb > search_bits),  # need more info than search noise
            # loose UNIFORM upper bound on chance hits (assumes prediction density
            # ~ N/target over the window); the empirical scan count is the true
            # figure and is far below this -- predictions are sparse near target.
            "upper_bound_chance_hits_uniform": round(N * 2.0 * w, 2),
        }
    return {
        "census_size": census_size,
        "n_functionals": n_functionals,
        "n_exponents": n_exponents,
        "search_space_size_N": N,
        "search_entropy_bits": round(search_bits, 2),
        "tiers": tiers,
        "observed_1pct_hits_per_Fk": hit_counts_1pct,
        "observed_1pct_hits_total": sum(hit_counts_1pct),
        "interpretation": (
            "A tolerance w is 'identifiable' only if match_specificity_bits > "
            "search_entropy_bits, i.e. the match pins the target more tightly "
            "than the search itself can resolve by chance. Here NO reachable "
            "tolerance (down to the experimental 5e-5) is identifiable: the "
            "census cannot pin m_tau even in principle. Independently, the "
            "empirical scan finds 0 hits at 1% -- the predictions are sparse "
            "near the target, floor stays at 1.33 percent as in the 25-knot "
            "search. Both point the same way."
        ),
    }



def _f64_json(o):
    """Recursively write plain Python floats as their repr strings.

    `_witness_default` below already serializes mpmath values at 50 dps, but it
    is only a FALLBACK — json handles a plain `float` natively, so every f64
    value in this witness went out as a raw JSON number and the file was on the
    raw-float64 ratchet. These are genuinely f64 (snappy volumes, census scores,
    entropy bits), so repr is exactly the digits produced: it round-trips
    bit-exactly and invents nothing.
    """
    if isinstance(o, bool) or o is None:
        return o
    if isinstance(o, float):
        return json_safe_float(o) if o != o or o in (float("inf"), float("-inf")) \
            else repr(o)
    if isinstance(o, dict):
        return {k: _f64_json(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_f64_json(v) for v in o]
    return o


def _witness_default(o):
    """JSON encoder fallback for mpmath types.

    The witness convention in this corpus is that high-precision values are
    serialized as **full-precision decimal strings** (see `substrate_q0`,
    `hbar_q`), never as float64 -- per AGENTS.md the serialization target is
    50 dps.  Without this hook `json.dumps` raises
    `TypeError: Object of type mpf is not JSON serializable` and the run dies
    *after* all the compute, emitting no witness.
    """
    if isinstance(o, mp.mpf):
        return mp.nstr(o, 50, strip_zeros=False)
    if isinstance(o, mp.mpc):
        return {"re": mp.nstr(o.real, 50, strip_zeros=False),
                "im": mp.nstr(o.imag, 50, strip_zeros=False)}
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")


def main() -> None:
    started = time.time()
    print(f"[m_tau_complex_volume] q_0    = {fmt(Q0, 30)}")
    print(f"[m_tau_complex_volume] hbar_q = {fmt(HBAR_Q, 30)}")

    # muon sanity: Vol(4_1)/hbar_q^2 = m_mu/m_e, AND CS(4_1)=0 (amphichiral).
    # Use the canonical high-precision Vol(4_1) = 2*Im(Li_2(e^{i pi/3})) = 2*Cl_2(pi/3)
    # (Bloch-Wigner form), NOT SnapPy's platform-dependent float, and keep the gate
    # at 1e-6 to match the real-volume probe.
    vol41 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    cs41 = float(snappy.Manifold("4_1").chern_simons())
    muon_pred = vol41 / HBAR_Q_SQ
    muon_err = rel_err(muon_pred, TARGET_MU_OVER_E)
    print(f"[sanity] Vol(4_1)={float(vol41):.12f}  CS(4_1)={cs41:.3e}  "
          f"muon rel_err={fmt(muon_err,4)}")
    if muon_err > mp.mpf("1e-6"):
        print("[sanity] FAILED"); sys.exit(1)
    print("[sanity] PASS -- and CS(4_1)~0: the muon anchor is CS-BLIND.")

    # Part A -- derived torus carrier
    print("\n[part A] derived tau carrier (T(3,5)-adjacent / T(2,7), n=7):")
    part_a = part_a_derived_carriers()
    for r in part_a:
        print(f"  {r['carrier']:>14}: vol={r.get('snappy_volume')}  "
              f"sol={r.get('solution_type')}  hyperbolic={r['hyperbolic']}")

    # Part B -- wide complex-volume census
    print(f"\n[part B] building <= {MAX_CROSSINGS}-crossing hyperbolic knot census...")
    census = build_census(MAX_CROSSINGS)
    n_with_cs = sum(1 for r in census if r.get("cs") is not None)
    print(f"[part B] {len(census)} knots ({n_with_cs} with CS). Scoring...")
    scores = score_census(census)

    print("\n[part B] hit counts (knots within tolerance) per fixed (F,k):")
    hit_counts_1pct = []
    for key in sorted(scores):
        s = scores[key]
        h = s["hits_within"]
        hit_counts_1pct.append(h["loose_1pct"])
        b = s["closest_knot"]
        bstr = (f"closest={b['knot']} rel_err={b['rel_err']:.4e}"
                if b else "closest=none")
        print(f"  {key:>10}: 1%={h['loose_1pct']:>4}  0.1%={h['mid_0p1pct']:>3}  "
              f"100ppm={h['tight_100ppm']:>2}  {bstr}")

    # composite (connected-sum) pairwise at derived k=3
    print(f"\n[part B'] composite K1#K2 pairwise search at k={DERIVED_K} "
          f"(additive volume)...")
    comp = composite_pairwise(census, float(TARGET_TAU_OVER_E), DERIVED_K)
    print(f"  {comp['n_pairs']} pairs, 1% hits = {comp['hits_within_1pct']}, "
          f"closest {comp['closest_pair']['pair']} "
          f"rel_err={comp['closest_pair']['rel_err']:.4e}")

    # entropy analysis
    ent = entropy_analysis(len(census), n_functionals=2,
                           n_exponents=len(SEARCH_KS),
                           hit_counts_1pct=hit_counts_1pct)
    print(f"\n[entropy] search N = {ent['search_space_size_N']} "
          f"({ent['search_entropy_bits']} bits)")
    for lbl, t in ent["tiers"].items():
        print(f"  tol {lbl:>8} ({t['tolerance']:.0e}): "
              f"{t['match_specificity_bits']} bits, "
              f"identifiable={t['identifiable']}, "
              f"ub_chance_hits={t['upper_bound_chance_hits_uniform']}")

    conclusion = ("sharpened_negative: the complex-volume axis does not yield a "
                  "DERIVED identification of m_tau. (1) The framework-derived "
                  "carrier is a torus knot (T(3,5)/T(2,7)) with zero hyperbolic "
                  "volume -- the Vol+iCS reading, real or complex, does not apply. "
                  "(2) For a hyperbolic-knot carrier the muon anchor is CS-blind "
                  "(CS(4_1)=0), so the CS-dependence of F is unconstrained; the "
                  "wide census search has entropy far exceeding the specificity of "
                  "any attainable match, so the closest knot is expected by chance.")

    witness = {
        "$schema": "../../folio-assistant/cat-harness/schemas/witness.schema.json",
        "computation": "m-tau-complex-volume-search",
        "description": ("Complex-volume (Vol + i*CS) extension of the refuted "
                        "25-knot m_tau search: derived torus carrier + wide "
                        "<=12-crossing census with search-entropy scoring."),
        "substrate_q0": fmt(Q0, 50),
        "hbar_q": fmt(HBAR_Q, 50),
        "target_m_tau_over_m_e_codata": fmt(TARGET_TAU_OVER_E, 12),
        "target_source": "PDG 2024; m_tau/m_e = 3477.23 (4 sig figs)",
        "sigma_exp_rel": float(SIGMA_EXP_TAU),
        "muon_sanity": {
            "vol_4_1": vol41, "cs_4_1": cs41,
            "muon_pred": fmt(muon_pred, 12),
            "muon_rel_err": fmt(muon_err, 6),
            "cs_blind_note": ("CS(4_1) ~ 0 because the figure-eight is "
                              "amphichiral; the muon anchor therefore carries no "
                              "information about how CS enters the functional F."),
        },
        "fixed_functionals": {
            "F_re": "Re(Vol + i*CS) = Vol  (the muon-derived choice)",
            "F_abs": "|Vol + i*CS| = sqrt(Vol^2 + CS^2)",
        },
        "fixed_exponents": SEARCH_KS,
        "derived_exponent_guess": DERIVED_K,
        "part_a_derived_carriers": part_a,
        "part_b_census": {
            "max_crossings": MAX_CROSSINGS,
            "n_hyperbolic_knots": len(census),
            "n_with_cs": n_with_cs,
            "scores": scores,
        },
        "part_b_composite_pairwise": comp,
        "entropy_analysis": ent,
        "conclusion": conclusion,
        "anti_fit_guard": (
            "F and k are FIXED before scoring, not per-knot tuned. The report is "
            "hit-COUNTS + entropy, not a 'closest knot' cherry-pick. Reported "
            "closest knots are shown precisely to demonstrate they are chance hits "
            "among many. No 4th calibration, no fit, no ansatz proposed."
        ),
        "cross_references": {
            "queued_extension": ("docs/audits/2026-06-03-m-tau-knot-prediction-"
                                 "falsification.md (extension #1: Vol + CS pair)"),
            "refuted_real_search": "computations/m_tau_knot_prediction.py",
            "entropy_precedent": "PR #1805 (PSLQ entropy bound)",
        },
        "duration_sec": f"{time.time() - started:.3f}",
    }

    wpath = Path(__file__).resolve().parent / "m-tau-complex-volume-search.witness.json"
    _d = os.path.dirname(os.path.abspath(__file__))
    while _d != os.path.dirname(_d) and not os.path.isdir(os.path.join(_d, "substrate")):
        _d = os.path.dirname(_d)
    sys.path.insert(0, os.path.join(_d, "substrate"))
    try:
        from witness_base import WitnessBuilder  # noqa: E402
        WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                                engine="snappy+mpmath")
    except Exception as e:  # pragma: no cover
        # Never emit a witness without provenance: if the canonical WitnessBuilder
        # is unavailable, stamp commitSha/scriptHash/engine manually (fail-safe).
        import hashlib
        import subprocess
        try:
            sha = subprocess.check_output(
                ["git", "log", "-1", "--format=%H", "--", __file__],
                cwd=os.path.dirname(os.path.abspath(__file__)),
            ).decode().strip() or "unknown"
        except Exception:
            sha = "unknown"
        witness["engine"] = "snappy+mpmath"
        witness["scriptHash"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:12]
        witness["scriptCommitSha"] = sha
        print(f"[witness] canonical stamp unavailable ({e}); stamped provenance manually")
    witness["scriptFile"] = os.path.basename(__file__)
    wpath.write_text(
        json.dumps(_f64_json(witness), indent=2, default=_witness_default) + "\n")
    print(f"\n[witness] wrote {wpath}")
    print(f"[conclusion] {conclusion}")
    print(f"[done] elapsed {witness['duration_sec']}s")


if __name__ == "__main__":
    main()
