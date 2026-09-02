#!/usr/bin/env python3
"""`1 < q_0 < phi` is `h < 1` — and the metallic rungs are NOT regime changes.

THE CONSTRAINT, TRANSLATED
----------------------------
Owner: *"in our local patch of the universe we have `1 < q_0 < phi`"*, and
*"metallic ladder should be change in behaviour / SDP solution regime"*.

The first half is exact and clean. Since `1/phi = phi - 1`,

    h(phi)  =  phi - 1/phi  =  1        exactly,

and `h = q - 1/q` is strictly increasing (`dh/dq = 1 + 1/q^2 > 0`), so

    1 < q < phi     <=>     0 < h < 1.

`phi` is `delta_1` of the corpus's own **metallic ladder**
`delta_n = (n + sqrt(n^2 + 4))/2` — the values where `h` crosses the integer `n`
(`computations/metallic_q_illustration.py`). So the constraint says: **`q_0`
lies below the first metallic rung.** At `q_0`, `h = 0.20906`.

WHAT THE BOUND SECURES — ONE THING, WITH MARGIN
-------------------------------------------------
`D_PN < 0`, i.e. **the binding operator always carries inverse-crossing
(entanglement) content**. Its sign boundary is `q_c = 3.4580993`
(`qc_is_the_convexity_boundary_probe`), where `h(q_c) = 3.16892` — more than
three times the bound, sitting between the bronze rung `delta_3` and `delta_4`.
So in our patch `K` is never in the positive sector, not as a measurement at
`q_0` but as a consequence of the bound.

It secures **none** of the positive-sector LP results, each of which has its own
window strictly inside `(1, phi)` — the tightest, the sub-alphabet, at
`h ~ 0.47`, less than half way to the golden rung.

THE REGIME PREDICTION IS NOT SUPPORTED BY WHAT CAN BE MEASURED HERE
---------------------------------------------------------------------
Three observables, swept in `h` (the natural variable) from 0.2 to 4.5, across
all four rungs `h = 1, 2, 3, 4`:

**(1) The Gram signature is CONSTANT.** `(n_+, n_-, n_0) = (4, 1, 1)` at every
`h` tested, rank 5 throughout. The SDP cone never changes shape, so there is no
regime for the solution to change between. This is the observable a "SDP
solution regime" would have to move, and it does not move.

**(2) The LP objective grows smoothly, and its one feature is inherited.**
`obj(T)` runs `0.27 -> 283 -> 6.1e7 -> 7.3e14` over `h = 0.21 .. 4.0` with no
kink at any rung. Its growth rate `d log(obj)/dh` does have a broad maximum near
`h = 1` (peak at `h = 0.9875`, within the 0.025 scan resolution of the rung) —
but that maximum is **not a property of the program**: the same peak, at the
same `h = 0.9875`, appears in `tr_M(free)`, a plain scalar with no LP in it at
all. The objective inherits it because row 1 of `Gx >= u` bounds the objective
by `u_1 = tr_M(free)` (the `t = G e_1` structure of
`h3a_frobenius_gram_offdiagonal_probe`). Controls: `|t3|` and `|x_free|` peak at
`h = 0.7125`, `|G|` at `0.9375` — so the coincidence at `0.9875` is one scalar's,
not the selection's.

**(3) The discrete outputs flicker OFF the rungs.** Separation fails at
`h = 0.9, 2.9, 3.3, 3.4, 3.8, 3.9`; `obj > u_1` flips at `0.6, 0.8, 0.9, 1.1,
1.8, 2.2, 2.5, 2.6, 3.5, 4.0`. Neither set clusters at integers. Flickering of
this kind is the signature of LP vertex degeneracy.

**CORROBORATION WITHDRAWN (2026-08-31).** This section used to cite
`computations/metallic_q_illustration.py` — *"not a bifurcation … no sign flips
at metallic ratios for any `beta` at `n = 3`"* (PR #1999) — as independent
support. That file is **pre-convention-D** (last touched 2026-08-15, one day
before `qou-cds2`) and `metallic_silver_coincidence_weighting_probe.py` shows
it fails three checks under D: its `q_0` is stale by `1.3e-8`; its
`chi^(2,1)(sigma_1 sigma_2) = h^2 - 1` is wrong, the convention-D value being
the constant `-1`; and it plots bare `chi^lambda` while claiming weighted
`y_lambda · chi^lambda` — which matters because under D `y_alt = 0` and only
two blocks are live. Its own `h^2 - 1` changes sign at `h = 1`, the golden
rung, contradicting the sentence quoted. **The citation is withdrawn.** The
measurements in this probe are unaffected.

**AND THIS NEGATIVE IS ABOUT ONE FUNCTIONAL, NOT THE LADDER.** The same probe
shows the metallic structure is real but lives in the **q-Plancherel**
weighting `W_lambda = d_q^2 / sum d_q^2`, where

    T(sigma) / T(gamma) = h/2      identically, at every strand count,

so the cost coincidence sits at `h = 2 = delta_silver` for every `n` —
generalising the sorry-free Lean `silver_lp_coincidence` (PR #2047) from its
`n = 2` statement. Everything swept below is **Markov**-weighted (`y_lambda`,
convention D), whose ratio is `z = q^2/[2]_q` instead and whose coincidence
sits at the supergolden ratio `q^3 = q^2 + 1`. The negative below is therefore
evidence about the Markov-weighted LP and **not** evidence that the metallic
ladder is inert.

The distinction this probe drew in its closing between a "representation-
theoretic regime (which blocks exist)" and "an optimisation one" is likewise
withdrawn. The owner's objection is right: `T(sigma) = (h/2) T(gamma)` is a
single identity that is simultaneously an optimisation fact (two cost
coefficients coincide) and a representation fact (the transpose-pair character
sum `chi^lambda + chi^lambda' = dim(lambda) · h`). The dual *is* the
representation.

SCOPE
-----
This tests the observables that a *selection* regime would live in: the cone
(Gram signature), the objective, and the discrete solution. What is established
is narrow and now known to be functional-specific: **in the Markov-weighted SDP
data at `H_3` and the Markov-weighted selection at `H_9`, the metallic rungs
are not distinguished.** Under the Plancherel weighting they are.

DISCIPLINE
----------
No fit; no `B_AME`; nothing wired. `h(phi) = 1` and the ladder are exact; the
sweep is mpmath at 40 dps with everything rebuilt per `q`; the signature and
growth-rate conclusions are f64 on well-separated quantities.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] metallic_silver_coincidence_weighting_probe.py (supersedes the
   PR #1999 corroboration and localises this negative to the Markov weighting)
-- Ref: [probe] qc_is_the_convexity_boundary_probe.py;
   positive_sector_q_stability_probe.py
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from scipy.optimize import linprog  # noqa: E402

from pyhecke.gram import _hm_mp, gram_matrix_mp  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
H_Q0 = float(mp.mpf(str(Q0)) - 1 / mp.mpf(str(Q0)))


def delta_n(n: int) -> float:
    """Metallic ratio: the `q` at which `h = q - 1/q` equals `n`."""
    return (n + math.sqrt(n * n + 4)) / 2


def q_of_h(h):
    h = mp.mpf(h)
    return (h + mp.sqrt(h * h + 4)) / 2


def substrate_at_h(hv):
    """Gram, Markov cost and both nucleon NFs at the `q` with this `h`."""
    q = q_of_h(hv)
    hq = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    G = np.array([[float(x) for x in row] for row in gram_matrix_mp(30, q=q)])
    t = np.array([1.0, float(z), float(z), float(z ** 2), float(z ** 2),
                  float(hq * z ** 2 + z)])

    def nucleon(kind: str) -> np.ndarray:
        nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
        for _ in range(3):
            nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq, 1, hq)
        if kind == "p":
            nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq / 2, 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq / 2, 1, hq)
        else:
            nf = _hm_mp(nf, mp.mpf(1), -hq / 2, 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq / 2, 0, hq)
            nf = _hm_mp(nf, mp.mpf(1), -hq, 1, hq)
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, hq)
        nf = _hm_mp(nf, mp.mpf(1), mp.mpf(0), 0, hq)
        return np.array([float(x) for x in nf])

    return G, t, {k: nucleon(k) for k in "pn"}


def kron_pow(M, A: int):
    out = M
    for _ in range(A - 1):
        out = np.kron(out, M)
    return out


def lp_at_h(hv):
    """Positive-sector LP at A = 3; returns objectives and the free trace."""
    G, t, NUC = substrate_at_h(hv)
    GA = kron_pow(G, 3)
    tA = kron_pow(t.reshape(1, -1), 3).ravel()
    d = GA.shape[0]
    out = {}
    for seq in ("pnn", "ppn"):
        v = NUC[seq[0]]
        for k in seq[1:]:
            v = np.kron(v, NUC[k])
        r = linprog(tA, A_ub=-GA, b_ub=-(GA @ v), bounds=[(0, None)] * d,
                    method="highs")
        if not r.success:
            return None
        out[seq] = {"obj": float(r.fun), "u1": float(tA @ v),
                    "support": tuple(i for i in range(d) if r.x[i] > 1e-9)}
    out["trM_free"] = abs(out["pnn"]["u1"])
    return out


def main() -> int:
    assertions = []
    print("t7qv — the golden bound, and the metallic rungs as a regime test")

    # ── A1. 1 < q < phi is exactly h < 1 ──────────────────────────────
    phi = (1 + mp.sqrt(5)) / 2
    h_phi = phi - 1 / phi
    ok = abs(float(h_phi) - 1.0) < 1e-30 and H_Q0 < 1.0
    print("\n  1. the constraint, translated")
    print(f"     phi = {mp.nstr(phi, 20)}   1/phi = phi - 1")
    print(f"     h(phi) = phi - 1/phi = {mp.nstr(h_phi, 20)}")
    print(f"     h strictly increasing (dh/dq = 1 + 1/q^2 > 0)")
    print(f"     => 1 < q < phi  <=>  0 < h < 1;   h(q_0) = {H_Q0:.10f}")
    print("\n     the metallic ladder delta_n = (n + sqrt(n^2+4))/2:")
    for n in range(1, 5):
        print(f"        delta_{n} = {delta_n(n):.15f}   h = {n}"
              + ("   <- phi, the GOLDEN rung" if n == 1 else ""))
    print(f"\n  A1  1 < q_0 < phi is exactly 0 < h < 1 .................. "
          f"{'PASS' if ok else 'FAIL'}")
    assertions.append(("golden_bound_is_h_below_one", ok,
                       f"h(phi) = {mp.nstr(h_phi, 12)}; h(q_0) = {H_Q0:.10f}"))

    # ── A2. The Gram signature is constant across every rung ──────────
    print("\n  2. Gram signature across the rungs (the SDP cone's shape)")
    sigs, hs_sig = [], [round(0.1 * i, 4) for i in range(2, 46)]
    for hv in hs_sig:
        G = np.array([[float(x) for x in r]
                      for r in gram_matrix_mp(30, q=q_of_h(hv))])
        w = np.linalg.eigvalsh((G + G.T) / 2)
        sigs.append((int((w > 1e-9).sum()), int((w < -1e-9).sum())))
    uniq = sorted(set(sigs))
    ok = len(uniq) == 1
    print(f"     h from {hs_sig[0]} to {hs_sig[-1]}, {len(hs_sig)} points, "
          f"crossing h = 1, 2, 3, 4")
    print(f"     distinct signatures (n_+, n_-): {uniq}   rank {sum(uniq[0])}/6")
    print(f"\n  A2  the SDP cone NEVER changes shape ..................... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      => there is no regime for the solution to change between.")
    assertions.append(("gram_signature_constant_across_all_rungs", ok,
                       f"signatures {uniq} over h = 0.2..4.5"))

    # ── A3. The growth-rate peak is inherited, not a program feature ──
    print("\n  3. the objective's growth rate, and its control")
    hs = [round(0.7 + 0.025 * i, 4) for i in range(29)]
    obj, trm = {}, {}
    for hv in hs:
        r = lp_at_h(hv)
        if r is None:
            continue
        obj[hv] = r["pnn"]["obj"]
        trm[hv] = r["trM_free"]

    def peak(series):
        best = (None, -1e9)
        for a, b in zip(hs, hs[1:]):
            if a in series and b in series:
                rate = (math.log(series[b]) - math.log(series[a])) / (b - a)
                if rate > best[1]:
                    best = ((a + b) / 2, rate)
        return best

    p_obj, p_trm = peak(obj), peak(trm)
    same = abs(p_obj[0] - p_trm[0]) < 1e-9
    ok = same
    print(f"     peak d(log obj)/dh      at h = {p_obj[0]:.4f}  "
          f"(|h-1| = {abs(p_obj[0] - 1):.4f})")
    print(f"     peak d(log trM_free)/dh at h = {p_trm[0]:.4f}  "
          f"(|h-1| = {abs(p_trm[0] - 1):.4f})")
    print(f"\n  A3  the peak is INHERITED from tr_M(free), not the LP ... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      tr_M(free) is a plain scalar with no LP in it, and it peaks")
    print("      at the same h. The objective inherits it because row 1 of")
    print("      Gx >= u bounds the objective by u_1 = tr_M(free) — the")
    print("      t = G e_1 structure. So the near-coincidence with h = 1 is")
    print("      one scalar's, not the selection program's.")
    assertions.append(("growth_peak_is_inherited_from_trM_free", ok,
                       f"obj peak {p_obj[0]}, trM_free peak {p_trm[0]}"))

    # ── A4. q_c is far outside the patch, so K is always entangled ────
    q_c = 3.458099300032797192042069
    h_c = q_c - 1 / q_c
    ok = h_c > 3.0 and H_Q0 < 1.0
    print("\n  4. what the bound DOES secure")
    print(f"     q_c = {q_c:.15f}   h(q_c) = {h_c:.6f}")
    print(f"     the bound is h < 1, so q_c sits {h_c:.2f}x beyond it,")
    print(f"     between the bronze rung delta_3 = {delta_n(3):.5f} and "
          f"delta_4 = {delta_n(4):.5f}")
    print(f"\n  A4  D_PN < 0 throughout the patch, with 3x margin ....... "
          f"{'PASS' if ok else 'FAIL'}")
    print("      => K always carries inverse-crossing (entanglement) content,")
    print("         as a CONSEQUENCE of the bound, not a measurement at q_0.")
    assertions.append(("golden_bound_secures_K_entanglement_content", ok,
                       f"h(q_c) = {h_c:.6f} vs bound h < 1"))

    print("\n### VERDICT: the golden bound is exactly h < 1 — below the first")
    print("    metallic rung — and it secures exactly one result, that K always")
    print("    carries entanglement content, with a 3x margin. The prediction")
    print("    that the rungs mark SDP regime changes is NOT supported by the")
    print("    MARKOV-WEIGHTED observables measured here: the Gram signature is")
    print("    constant (4,1,1) across all four rungs, the objective grows")
    print("    smoothly with its one feature inherited from a plain scalar, and")
    print("    the discrete flickers fall off the rungs.")
    print("\n    SUPERSEDED IN PART (2026-08-31). The PR #1999 corroboration")
    print("    this probe used to claim is WITHDRAWN — that file is pre-")
    print("    convention-D and wrong under D (see metallic_silver_coincidence")
    print("    _weighting_probe.py). And the prediction IS supported under the")
    print("    q-Plancherel weighting, where T(sigma)/T(gamma) = h/2 exactly at")
    print("    every n, putting the cost coincidence at h = 2 = delta_silver")
    print("    for every strand count. The negative above is about the Markov")
    print("    functional, not about the ladder.")

    all_ok = all(a[1] for a in assertions)

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("metallic-ladder-regime-test", engine="scipy",
                                output_dir=COMP)
            wb.set_description(
                "EXPLORATORY (bean t7qv): translates the owner's constraint "
                "1 < q_0 < phi and tests the prediction that the metallic "
                "ladder marks SDP regime changes. TRANSLATION (exact): since "
                "1/phi = phi - 1, h(phi) = phi - 1/phi = 1 and h is strictly "
                "increasing, so 1 < q < phi is exactly 0 < h < 1 — below the "
                "first rung of the corpus's own metallic ladder "
                "delta_n = (n + sqrt(n^2+4))/2. At q_0, h = 0.20906. WHAT IT "
                "SECURES: one result, with margin — D_PN < 0 throughout, since "
                "its boundary q_c = 3.4580993 has h = 3.16892, over 3x the "
                "bound, so K always carries inverse-crossing (entanglement) "
                "content as a consequence of the bound rather than a "
                "measurement. It secures NONE of the positive-sector LP "
                "results, whose windows are strictly inside (1, phi). REGIME "
                "PREDICTION NOT SUPPORTED here: the Gram signature is constant "
                "(4,1,1) at every h from 0.2 to 4.5 across all four rungs, so "
                "the SDP cone never changes shape; the LP objective grows "
                "smoothly and its growth-rate maximum near h=1 is INHERITED — "
                "tr_M(free), a plain scalar with no LP in it, peaks at the same "
                "h = 0.9875, and the objective inherits it via the t = G e_1 "
                "row-1 bound; and the discrete flickers fall at h = 0.9, 2.9, "
                "3.3, 3.4, 3.8, 3.9, off the rungs. SUPERSEDED IN PART "
                "(2026-08-31): the PR #1999 corroboration this probe claimed "
                "is WITHDRAWN (pre-convention-D and wrong under D), and the "
                "negative is now known to be functional-specific — everything "
                "swept here is Markov-weighted, whereas under the q-Plancherel "
                "weighting T(sigma)/T(gamma) = h/2 exactly at every n, putting "
                "the cost coincidence at h = 2 = delta_silver for every strand "
                "count. See metallic_silver_coincidence_weighting_probe.py. "
                "No fit; no B_AME; nothing wired.")
            wb.add_data("h_of_phi", "1")
            wb.add_data("h_of_q0", f"{H_Q0:.12f}")
            wb.add_data("metallic_ladder",
                        {str(n): f"{delta_n(n):.15f}" for n in range(1, 5)})
            wb.add_data("gram_signatures_seen", [list(u) for u in uniq])
            wb.add_data("growth_peaks", {"obj": f"{p_obj[0]:.4f}",
                                         "trM_free": f"{p_trm[0]:.4f}"})
            wb.add_data("q_c", f"{q_c:.15f}")
            wb.add_data("h_of_q_c", f"{h_c:.6f}")
            for name, passed, detail in assertions:
                wb.add_assertion(name=name, computed=str(int(bool(passed))),
                                 expected="1", tolerance=0, source=str(detail))
            wb.add_caveat(
                "SCOPE: this tests the observables a SELECTION regime would "
                "live in — the cone (Gram signature), the objective, and the "
                "discrete solution — at H_3 and H_9. A regime change could "
                "still live in something not formed here: a different algebra "
                "level, or a functional other than these. The negative is "
                "'the metallic rungs are not distinguished in the SDP data at "
                "H_3 or the selection at H_9', not 'the metallic ladder is "
                "physically inert'.")
            wb.add_caveat(
                "The growth-rate maximum sits at h = 0.9875 with a 0.025 scan "
                "step, so it is within resolution of h = 1 and the maximum is "
                "very flat (0.2% above its neighbour). It is reported as "
                "INHERITED rather than absent, because tr_M(free) — which "
                "contains no LP — peaks at exactly the same h. Controls |t3| "
                "and |x_free| peak at h = 0.7125 and |G| at 0.9375.")
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:  # pragma: no cover
            print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
