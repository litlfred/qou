#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only LP across counterfactual q.
"""
S(4) — exact n=4 (and exact n=3) metallic LP active-set sweep.

Picks up the stalled §7.4 thread of
docs/audits/2026-06-09-metallic-q-csc-phase-synthesis.md: the n=4 LP
active set S(4) needed H₄(q) Markov-trace data that pyhecke (pure
Python, H₃-hardcoded) cannot provide.  `pyhecke_native` (built from
source in-sandbox per compute-author §0.1) provides exact Hoefsmit
characters χ_λ(β) for any strand count, so both the n=4 probe AND the
exact-Gram n=3 re-run (synthesis §8 open question 4 — the prior n=3
probe used a rank-1 outer-product Gram approximation) are done here
with NO Gram approximation:

    basis   = {T_w : w ∈ S_n}, positive reduced words (canonical
              Hecke basis; n=3: 6 words, n=4: 24 words)
    t_i     = tr_M(b_i)        = Σ_λ y_λ χ_λ(b_i)
    G_ij    = tr_M(b_i · b_j)  = Σ_λ y_λ χ_λ(b_i ∘ b_j)   (concatenation)

Two weight conventions are carried side by side:

  * "plancherel" — y_λ = H_q(λ)² / [n]_q!  (H_q = product of q-hook
    lengths).  This is the convention of the PROVED n=2 statement
    (silver_lp_coincidence: t_γ = 2(q+q⁻¹), t_σ = q²−q⁻²) and of the
    prior n=2 / n=3 probes; the S(n) ladder conjecture is anchored
    here.
  * "canonical" — y_λ from `pyhecke_native.trace_weights_n` (Markov-
    normalized: tr_M(1) = 1, tr_M(σ_i) = z, Markov-stable across n).
    Carried as a control: does the metallic transition survive the
    canonical normalization, or is it a convention artifact?

Outputs: active-set transitions per convention (with metallic-ratio
bracketing against δ₁..δ₄), pairwise cost-coincidence loci t_i = t_j
(the PROVED mechanism at n=2) with mpfr refinement, the S(4)
candidate set, witness JSON (full LP duals per the LP/SDP discipline)
and a PNG chart.

Note on basis convention: the prior n=3 probe used the pyhecke NF
basis {γ, σ₀, σ₁, L₊, L₋ = σ₀⁻¹σ₁⁻¹, e⁻} which contains one
inverse-generator word.  Here the canonical T_w basis replaces L₋ by
the positive word σ₂σ₁ (same permutation, positive lift).  Cost
functions differ on that one element; coincidence loci of the other
five and the active-set structure are directly comparable.
"""

from __future__ import annotations

import json
import math
import sys
import time
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import pyhecke_native as pn
from scipy.optimize import linprog

mp.mp.dps = 50
HERE = Path(__file__).parent

MPFR_DPS = 40  # refinement precision for coincidence roots


def delta_n(n: int) -> mp.mpf:
    return (mp.mpf(n) + mp.sqrt(n * n + 4)) / 2


METALLIC = {k: delta_n(k) for k in (1, 2, 3, 4, 5)}
METALLIC_NAMES = {1: "φ", 2: "δ_silver", 3: "δ_bronze", 4: "δ_4", 5: "δ_5"}
Q0 = mp.mpf("1.1099785955541805")


# ── S_n reduced words (canonical T_w basis) ────────────────────────────


def reduced_words(n: int) -> list[tuple[tuple[int, ...], list[int]]]:
    """BFS over S_n: returns [(one_line_perm, reduced_word)] with words
    as 1-based generator indices, sorted by (length, word)."""
    ident = tuple(range(1, n + 1))
    seen = {ident: []}
    frontier = [ident]
    while frontier:
        nxt = []
        for w in frontier:
            for i in range(n - 1):  # right-multiply by s_{i+1}
                if w[i] < w[i + 1]:  # length increases
                    v = list(w)
                    v[i], v[i + 1] = v[i + 1], v[i]
                    v = tuple(v)
                    if v not in seen:
                        seen[v] = seen[w] + [i + 1]
                        nxt.append(v)
        frontier = nxt
    out = sorted(seen.items(), key=lambda kv: (len(kv[1]), kv[1]))
    assert len(out) == math.factorial(n)
    return out


def cycle_type(perm: tuple[int, ...]) -> tuple[int, ...]:
    n = len(perm)
    seen = [False] * n
    parts = []
    for i in range(n):
        if not seen[i]:
            j, c = i, 0
            while not seen[j]:
                seen[j] = True
                j = perm[j] - 1
                c += 1
            parts.append(c)
    return tuple(sorted(parts, reverse=True))


def word_label(word: list[int]) -> str:
    return "γ" if not word else "·".join(f"σ{i}" for i in word)


# ── q-combinatorics (plancherel weights) ───────────────────────────────


def q_int(k: int, q):
    return (q**k - q**-k) / (q - 1 / q)


def q_factorial(n: int, q):
    out = q * 0 + 1
    for k in range(1, n + 1):
        out *= q_int(k, q)
    return out


def hook_lengths(shape: list[int]) -> list[int]:
    conj = [sum(1 for r in shape if r > j) for j in range(shape[0])]
    return [
        shape[i] - j + conj[j] - i - 1
        for i in range(len(shape))
        for j in range(shape[i])
    ]


def plancherel_weights(shapes: list[list[int]], q) -> list:
    n = sum(shapes[0])
    fact = q_factorial(n, q)
    out = []
    for sh in shapes:
        H = q * 0 + 1
        for h in hook_lengths(sh):
            H *= q_int(h, q)
        out.append(H * H / fact)
    return out


# ── trace assembly ─────────────────────────────────────────────────────


def braid(word: list[int]) -> list[tuple[int, int]]:
    return [(1, g) for g in word]


def _weights_f64(n: int, shapes: list[list[int]], q: float,
                 convention: str) -> list[float]:
    if convention == "plancherel":
        return [float(v) for v in plancherel_weights(shapes, mp.mpf(q))]
    return pn.trace_weights_n(n, q)


def t_vector_f64(n: int, shapes: list[list[int]], words: list[list[int]],
                 q: float, convention: str) -> np.ndarray:
    """Exact cost vector t_i = tr_M(b_i) only (no Gram) — used by the
    coincidence grid where the Gram would be O(d²) wasted work."""
    y = _weights_f64(n, shapes, q, convention)
    t = np.empty(len(words))
    for i, w in enumerate(words):
        chi = pn.chi_lambdas_braid(shapes, braid(w), q)
        t[i] = sum(yi * ci for yi, ci in zip(y, chi))
    return t


def t_and_gram(n: int, shapes: list[list[int]], words: list[list[int]],
               q: float, convention: str) -> tuple[np.ndarray, np.ndarray]:
    """Exact cost vector t_i = tr_M(b_i) and Gram G_ij = tr_M(b_i b_j)."""
    y = _weights_f64(n, shapes, q, convention)
    d = len(words)
    t = t_vector_f64(n, shapes, words, q, convention)
    G = np.empty((d, d))
    for i in range(d):
        for j in range(i, d):
            chi = pn.chi_lambdas_braid(shapes, braid(words[i] + words[j]), q)
            G[i, j] = G[j, i] = sum(yi * ci for yi, ci in zip(y, chi))
    return t, G


def t_vector_mpf(n: int, shapes: list[list[int]], words: list[list[int]],
                 q: mp.mpf) -> list[mp.mpf]:
    """Plancherel-convention cost vector at MPFR_DPS precision."""
    y = plancherel_weights(shapes, q)
    qs = mp.nstr(q, MPFR_DPS, strip_zeros=False)
    out = []
    for w in words:
        chi = pn.chi_lambdas_braid_mpfr(shapes, braid(w), qs, MPFR_DPS)
        out.append(sum(yi * mp.mpf(ci) for yi, ci in zip(y, chi)))
    return out


# ── LP (full dual emission per the LP/SDP discipline) ──────────────────


def solve_lp(t: np.ndarray, G: np.ndarray, n_target: float = 1.0,
             M: float = 1e6) -> dict:
    d = len(t)
    # conditioning: scale objective to unit max; row-scale the Frobenius
    # cone (each row is a half-space through the origin — the feasible
    # set and the active set are invariant under positive row scaling)
    t_s = t / max(1.0, np.max(np.abs(t)))
    row_norm = np.maximum(np.max(np.abs(G), axis=1), 1e-300)
    G_s = G / row_norm[:, None]
    res = linprog(
        t_s, A_ub=-G_s, b_ub=np.zeros(d), A_eq=np.ones((1, d)),
        b_eq=np.array([n_target]), bounds=[(-M, None)] * d, method="highs",
    )
    if not res.success:
        return {"status": f"failed: {res.message}", "active_set": None}
    t = t_s
    y0 = float(res.eqlin.marginals[0])
    y_star = (-np.array(res.ineqlin.marginals)).tolist()
    tol = 1e-7 * max(1.0, max(abs(v) for v in y_star))
    active = [i for i, v in enumerate(y_star) if abs(v) > tol]
    primal = float(t @ res.x)
    dual = float(n_target * y0)
    return {
        "x_star": res.x.tolist(),
        "y0_star": y0,
        "y_star": y_star,
        "active_set": active,
        "primal_obj": primal,
        "dual_obj": dual,
        "duality_gap": abs(primal - dual),
        "status": "ok",
    }


# ── sweeps ─────────────────────────────────────────────────────────────


def build_sweep(top_k: int) -> list[mp.mpf]:
    """Dense per-interval sweep hitting each metallic point exactly."""
    pts: list[mp.mpf] = []
    eps = mp.mpf("0.004")
    anchors = [Q0] + [METALLIC[k] for k in range(1, top_k + 1)]
    for a, b in zip(anchors, anchors[1:]):
        lo, hi, m = a + eps, b - eps, 16
        pts += [lo + (hi - lo) * i / (m - 1) for i in range(m)]
        pts.append(b)  # exact metallic point
    last = anchors[-1]
    pts += [last + eps + (mp.mpf("0.4") - eps) * i / 7 for i in range(8)]
    return pts


def run_sweep(n: int, top_k: int) -> dict:
    shapes = pn.partitions_of(n)
    basis = reduced_words(n)
    words = [w for _, w in basis]
    labels = [word_label(w) for w in words]
    ctypes = [cycle_type(p) for p, _ in basis]

    qs = build_sweep(top_k)
    rows = []
    for q in qs:
        row: dict = {"q": str(q)}
        for conv in ("plancherel", "canonical"):
            t, G = t_and_gram(n, shapes, words, float(q), conv)
            lp = solve_lp(t, G)
            row[conv] = {
                "active_set": lp.get("active_set"),
                "status": lp["status"],
                "t": t.tolist(),
            }
            # keep one full dual record per metallic point for the witness
            if any(abs(q - METALLIC[k]) < 1e-12 for k in range(1, top_k + 1)):
                row[conv]["lp_full"] = lp
        rows.append(row)

    transitions = {conv: [] for conv in ("plancherel", "canonical")}
    for conv in transitions:
        for a, b in zip(rows, rows[1:]):
            sa, sb = a[conv]["active_set"], b[conv]["active_set"]
            if sa is None or sb is None:
                continue  # LP failure rows recorded via status, not here
            if sa != sb:
                qa, qb = mp.mpf(a["q"]), mp.mpf(b["q"])
                brackets = [
                    METALLIC_NAMES[k]
                    for k in range(1, top_k + 1)
                    if qa <= METALLIC[k] <= qb
                ]
                transitions[conv].append({
                    "q_below": a["q"], "q_above": b["q"],
                    "set_below": sa, "set_above": sb,
                    "labels_below": [labels[i] for i in sa],
                    "labels_above": [labels[i] for i in sb],
                    "metallic_brackets": brackets,
                })
    return {
        "n": n, "words": words, "labels": labels,
        "cycle_types": [list(c) for c in ctypes],
        "rows": rows, "transitions": transitions,
    }


# ── cost-coincidence loci (the proved n=2 mechanism) ───────────────────


def trace_classes(n: int, shapes, words, conv: str) -> list[list[int]]:
    """Group basis indices whose cost functions are identical (probe at
    3 generic q's) — braid-conjugate words share tr_M for all q."""
    probes = [1.31, 2.07, 3.71]
    tt = [t_vector_f64(n, shapes, words, q, conv) for q in probes]
    classes: list[list[int]] = []
    for i in range(len(words)):
        for cl in classes:
            j = cl[0]
            if all(abs(t[i] - t[j]) < 1e-9 * max(1.0, abs(t[j])) for t in tt):
                cl.append(i)
                break
        else:
            classes.append([i])
    return classes


def coincidence_roots(n: int, shapes, words, labels, conv: str,
                      q_lo: float, q_hi: float, top_k: int) -> list[dict]:
    classes = trace_classes(n, shapes, words, conv)
    reps = [cl[0] for cl in classes]
    grid = np.linspace(q_lo, q_hi, 600)
    tgrid = np.array(
        [t_vector_f64(n, shapes, words, float(q), conv)[reps] for q in grid]
    )  # (600, n_reps)

    found: list[dict] = []
    for a, b in combinations(range(len(reps)), 2):
        diff = tgrid[:, a] - tgrid[:, b]
        for k in range(len(grid) - 1):
            if diff[k] == 0.0 or diff[k] * diff[k + 1] >= 0:
                continue
            lo, hi = grid[k], grid[k + 1]

            def d_f64(q: float) -> float:
                t = t_vector_f64(n, shapes, words, q, conv)
                return float(t[reps[a]] - t[reps[b]])

            for _ in range(60):  # f64 bisection
                mid = 0.5 * (lo + hi)
                if d_f64(lo) * d_f64(mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            root = 0.5 * (lo + hi)
            entry = {
                "pair": [labels[reps[a]], labels[reps[b]]],
                "class_sizes": [len(classes[a]), len(classes[b])],
                "q_root": root,
            }
            # metallic classification (refine in mpf for plancherel)
            metallic_hit = None
            for kk in range(1, top_k + 1):
                if abs(root - float(METALLIC[kk])) < 1e-6:
                    metallic_hit = METALLIC_NAMES[kk]
                    if conv == "plancherel":
                        ia, ib = reps[a], reps[b]

                        def d_mpf(q: mp.mpf) -> mp.mpf:
                            t = t_vector_mpf(n, shapes, words, q)
                            return t[ia] - t[ib]

                        resid = d_mpf(METALLIC[kk])
                        entry["residual_at_metallic"] = mp.nstr(resid, 8)
                        entry["metallic_exact"] = bool(
                            abs(resid) < mp.mpf(10) ** (-(MPFR_DPS - 10))
                        )
            entry["metallic"] = metallic_hit
            found.append(entry)
    return found


# ── validation battery ─────────────────────────────────────────────────


def validations() -> dict:
    out = {}
    q = 1.5
    # (V1) plancherel n=2 reproduces the PROVED closed forms
    shapes2 = pn.partitions_of(2)
    words2 = [w for _, w in reduced_words(2)]
    t2, _ = t_and_gram(2, shapes2, words2, q, "plancherel")
    exp = [2 * (q + 1 / q), q * q - 1 / q**2]
    out["v1_n2_proved_closed_forms"] = bool(
        abs(t2[0] - exp[0]) < 1e-12 and abs(t2[1] - exp[1]) < 1e-12
    )
    # (V2) silver regression: t_γ − t_σ root == δ_silver at mpf
    ds = METALLIC[2]
    tm = t_vector_mpf(2, shapes2, words2, ds)
    out["v2_silver_residual"] = mp.nstr(tm[0] - tm[1], 8)
    out["v2_silver_exact"] = bool(abs(tm[0] - tm[1]) < mp.mpf(10) ** -30)
    # (V3) canonical normalization + Markov stability across n
    ok3 = True
    z = pn.markov_z(q)
    for n in (2, 3, 4):
        shapes = pn.partitions_of(n)
        y = pn.trace_weights_n(n, q)
        chi_id = pn.chi_lambdas_braid(shapes, [], q)
        chi_s1 = pn.chi_lambdas_braid(shapes, [(1, 1)], q)
        ok3 &= abs(sum(a * b for a, b in zip(y, chi_id)) - 1.0) < 1e-10
        ok3 &= abs(sum(a * b for a, b in zip(y, chi_s1)) - z) < 1e-10
    out["v3_canonical_markov_stable"] = bool(ok3)
    # (V4) Hecke relation χ(σ²) = h χ(σ) + χ(1) per λ at n=4
    shapes4 = pn.partitions_of(4)
    h = pn.hecke_h(q)
    c0 = pn.chi_lambdas_braid(shapes4, [], q)
    c1 = pn.chi_lambdas_braid(shapes4, [(1, 2)], q)
    c2 = pn.chi_lambdas_braid(shapes4, [(1, 2), (1, 2)], q)
    out["v4_hecke_relation"] = bool(
        all(abs(c2[i] - h * c1[i] - c0[i]) < 1e-10 for i in range(len(shapes4)))
    )
    # (V5) Gram symmetry tr(ab) = tr(ba) on random word pairs at n=4
    rng = np.random.default_rng(0)
    words4 = [w for _, w in reduced_words(4)]
    ok5 = True
    for _ in range(10):
        i, j = rng.integers(0, len(words4), 2)
        for conv in ("plancherel", "canonical"):
            y = (
                [float(v) for v in plancherel_weights(shapes4, mp.mpf(q))]
                if conv == "plancherel" else pn.trace_weights_n(4, q)
            )
            ab = pn.chi_lambdas_braid(shapes4, braid(list(words4[i]) + list(words4[j])), q)
            ba = pn.chi_lambdas_braid(shapes4, braid(list(words4[j]) + list(words4[i])), q)
            tab = sum(a * b for a, b in zip(y, ab))
            tba = sum(a * b for a, b in zip(y, ba))
            ok5 &= abs(tab - tba) < 1e-9 * max(1.0, abs(tab))
    out["v5_trace_symmetry"] = bool(ok5)
    return out


# ── main ───────────────────────────────────────────────────────────────


def main() -> None:
    t_start = time.time()
    print("S(4) exact LP sweep — validations…", file=sys.stderr)
    checks = validations()
    print(json.dumps(checks, indent=2), file=sys.stderr)
    hard = ["v1_n2_proved_closed_forms", "v2_silver_exact",
            "v3_canonical_markov_stable", "v4_hecke_relation",
            "v5_trace_symmetry"]
    assert all(checks[k] for k in hard), f"validation failure: {checks}"

    results = {}
    coinc = {}
    for n, top_k in ((3, 3), (4, 4)):
        print(f"n={n} sweep…", file=sys.stderr)
        results[n] = run_sweep(n, top_k)
        shapes = pn.partitions_of(n)
        words = results[n]["words"]
        labels = results[n]["labels"]
        coinc[n] = {
            conv: coincidence_roots(
                n, shapes, words, labels, conv, 1.02,
                float(METALLIC[top_k]) + 0.45, top_k,
            )
            for conv in ("plancherel", "canonical")
        }
        for conv in ("plancherel", "canonical"):
            distinct = []
            n_fail = 0
            for r in results[n]["rows"]:
                a = r[conv]["active_set"]
                if a is None:
                    n_fail += 1
                elif a not in distinct:
                    distinct.append(a)
            print(
                f"  [{conv}] distinct active sets: {distinct} "
                f"(failed rows: {n_fail})",
                file=sys.stderr,
            )
            tr = results[n]["transitions"][conv]
            print(f"  [{conv}] transitions: {len(tr)}", file=sys.stderr)
            for t in tr:
                tag = ",".join(t["metallic_brackets"]) or "interior"
                print(
                    f"    q∈[{float(mp.mpf(t['q_below'])):.5f},"
                    f"{float(mp.mpf(t['q_above'])):.5f}] "
                    f"{t['set_below']}→{t['set_above']} [{tag}]",
                    file=sys.stderr,
                )

    # S(n) verdicts
    def s_set(n: int, conv: str) -> list[str]:
        out = {m for t in results[n]["transitions"][conv]
               for m in t["metallic_brackets"]}
        out |= {c["metallic"] for c in coinc[n][conv] if c["metallic"]}
        return sorted(out)

    verdict = {
        f"S({n})_{conv}": s_set(n, conv)
        for n in (3, 4) for conv in ("plancherel", "canonical")
    }
    print(json.dumps(verdict, indent=2), file=sys.stderr)

    # ── plot (n=4) ─────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(15, 8), sharex=True)
    for col, conv in enumerate(("plancherel", "canonical")):
        rows = results[4]["rows"]
        qsf = [float(mp.mpf(r["q"])) for r in rows]
        classes = trace_classes(4, pn.partitions_of(4),
                                results[4]["words"], conv)
        ax = axes[0][col]
        for cl in classes:
            i = cl[0]
            ax.plot(qsf, [r[conv]["t"][i] for r in rows], lw=1.2,
                    label=f"{results[4]['labels'][i]} (×{len(cl)})")
        ax.set_yscale("symlog")
        ax.set_title(f"n=4 cost classes — {conv}")
        ax.legend(fontsize=6, ncol=2)
        ax.grid(alpha=0.3)
        ax = axes[1][col]
        ax.step(qsf, [len(r[conv]["active_set"]) for r in rows],
                where="post", lw=1.5)
        ax.set_title(f"n=4 |active set| — {conv}")
        ax.set_xlabel("q")
        ax.grid(alpha=0.3)
        for a in (axes[0][col], axes[1][col]):
            for k in range(1, 5):
                a.axvline(float(METALLIC[k]), color="goldenrod",
                          lw=1.0, ls=":", alpha=0.8)
    plt.tight_layout()
    out_png = HERE / "metallic-q-s4-exact-lp-sweep.png"
    fig.savefig(out_png, dpi=140, bbox_inches="tight")
    print(f"Saved plot: {out_png}", file=sys.stderr)

    # slim the rows for the witness (full t vectors only at metallic pts)
    for n in (3, 4):
        for r in results[n]["rows"]:
            for conv in ("plancherel", "canonical"):
                if "lp_full" not in r[conv]:
                    r[conv].pop("t")

    witness = {
        "description": (
            "S(4) exact metallic LP active-set sweep on the canonical "
            "T_w basis of H_4(q) (24 positive reduced words), plus the "
            "exact-Gram n=3 re-run closing the prior probe's rank-1 Gram "
            "approximation.  Exact costs t_i = tr_M(b_i) and Gram "
            "G_ij = tr_M(b_i b_j) from native Hoefsmit characters "
            "(pyhecke_native), two weight conventions: plancherel "
            "(y_λ = H_q(λ)²/[n]_q!, the proved-S(2) convention) and "
            "canonical Markov (trace_weights_n).  LP duals emitted per "
            "the LP/SDP discipline; cost-coincidence loci located and "
            "classified against the metallic ladder δ_1..δ_4."
        ),
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "script": "metallic_q_s4_exact_lp_sweep.py",
        "engine": "pyhecke_native " + getattr(pn, "__version__", "0.9.0"),
        "validations": checks,
        "n3": {
            "labels": results[3]["labels"],
            "cycle_types": results[3]["cycle_types"],
            "transitions": results[3]["transitions"],
            "coincidences": coinc[3],
            "rows": results[3]["rows"],
        },
        "n4": {
            "labels": results[4]["labels"],
            "cycle_types": results[4]["cycle_types"],
            "transitions": results[4]["transitions"],
            "coincidences": coinc[4],
            "rows": results[4]["rows"],
        },
        "S_sets": verdict,
        "metallic_ladder": {METALLIC_NAMES[k]: mp.nstr(METALLIC[k], 30)
                            for k in range(1, 5)},
        "limitations": [
            "LP solved in f64 (scipy highs); coincidence roots refined "
            "by f64 bisection and—where a root lands within 1e-6 of a "
            "metallic ratio in the plancherel convention—re-verified at "
            f"{MPFR_DPS}-dps mpfr (residual_at_metallic field).",
            "Basis is the canonical positive T_w lift; the prior n=3 "
            "probe's NF basis used one inverse word (L_- = σ₀⁻¹σ₁⁻¹), "
            "replaced here by σ₂σ₁.  Active-set indices are therefore "
            "not 1:1 comparable to the 2026-06-09 approximate n=3 probe "
            "on that one element.",
            "n_target=1.0 and the Frobenius-cone constraint Gx ≥ 0 "
            "follow the prior probes; physical demand vectors (per-"
            "nucleus) are out of scope for this structural probe.",
        ],
        "runtime_seconds": round(time.time() - t_start, 1),
    }
    out_json = HERE / "metallic-q-s4-exact-lp-sweep.witness.json"
    out_json.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Saved witness: {out_json}", file=sys.stderr)
    print(f"TOTAL {witness['runtime_seconds']} s", file=sys.stderr)


if __name__ == "__main__":
    main()
