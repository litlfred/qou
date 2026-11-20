#!/usr/bin/env python3
"""Bean qou-prjo -- principle (i): is a nucleon-symmetric readout FORCED, and does
the super-pairwise transverse residual R_3 survive it?

PR #4849 measured the multi-generator NA-Stokes transverse pairing, found it
super-pairwise, and disqualified it on the ground that it is nucleon-ORDERING
dependent (T: 1.13x over pnn/npn/nnp), citing the corpus identity
``tr_M(beta) = tr_M(rep)`` (``computations/atom_orbit_reduction.py``) as evidence
that the corpus's own scalar observable is ordering-invariant.

This probe tests that citation, and the symmetrization question behind it.

## What the corpus identity actually says (Phase 0, structural -- Part A here)

The identity is over ``S_Z x S_N`` (protons among protons, neutrons among
neutrons) and its proof (Lemma 1,
``docs/audits/2026-05-30-orbit-trace-identity-proof.md``) establishes it by
showing such a permutation leaves the braid WORD unchanged: it fixes the
ordering string ``p...pn...n`` and preserves every adjacency type.  So the
``S_Z x S_N`` orbit of words is a SINGLE POINT, and orbit-symmetrization over
that group is the IDENTITY MAP on every readout -- scalar or operator.  Part A
verifies this mechanically: |group| = Z!*N! but |orbit of ordering strings| = 1.

The permutations #4849 varied are CROSS-SPECIES (pnn <-> npn).  They are not in
``S_Z x S_N``; no corpus identity covers them; and a proton and a neutron are
distinguishable, so there is no exchange symmetry to invoke.

## The decisive measurement (Part B)

If the corpus's own ``tr_M`` is itself cross-species-ordering-dependent, then
#4849's disqualifier -- "a nuclear observable cannot be a function of the braid
word" -- applies verbatim to the canonical mass/binding trace, and therefore does
NOT single out the transverse pairing.

``tr_M`` is computed here from the canonical Frobenius pairing
``tr_M(beta) = sum_{lambda |- n} y_lambda(q) * chi^lambda(beta)``
with ``y_lambda`` from the live closed form
``schur_principal_mpmath.y_lambda_at_q0_mpmath`` at the EXPERIMENTAL PROTON
ANCHOR (owner directive 2026-08-07; never the muon-serving cache), and
``chi^lambda`` the trace of the corpus seminormal/Hoefsmit representation.  The
implementation is certified before use:

  * ``tr_M(1) = 1``                        (normalisation sum_lambda y_lambda f^lambda = 1)
  * ``tr_M(AB) = tr_M(BA)``                (Markov M1, on the real atom word)
  * ``tr_M(beta sigma_{n-1}) / tr_M(beta)`` constant over many ``beta`` in
    ``H_{n-1}``                            (Markov M2 -- this is what pins the
                                            weights as JONES-MARKOV weights,
                                            not merely as trace weights)
  * braid + Hecke + far-commutation on the seminormal matrices.

## The counterfactual (Part C)

The DERIVED symmetrization (``S_Z x S_N``) is the identity, so the derived answer
to "survive or cancel" is SURVIVE, fixed before any arithmetic and with no
freedom to shop among symmetrizations.  Part C additionally reports the
non-derived ``S_A`` operator average -- ``<R> = |orderings|^-1 sum_o R(word_o)``,
which is well defined because the top-level Moebius residual sums over ALL
subsets and is therefore independent of the nucleon labelling -- purely so the
counterfactual is on the record.  It selects nothing: the derived readout is
already committed above.  Reported for all three of #4849's germ readings, not
one.

## Discipline

* ``free_parameters = 0``.  No AME quantity and no ``g_2`` appears anywhere.
* ``q0`` = experimental proton anchor; recorded (the A >= 3 germ is q-DEPENDENT
  per #4849 section 5.2, so the pin is material).
* Nothing is wired.  Bean ``qou-prjo`` stays OPEN: this dissolves blocker (i);
  blocker (ii) (which germ observer pair + the representation gauge) is
  untouched and still binding.

Audit: docs/audits/2026-08-09-nastokes-orbit-symmetric-readout.md
"""
from __future__ import annotations

import itertools
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent            # computations/probes
_COMP = HERE.parent                               # computations
for p in (str(_COMP), str(HERE), str(_COMP / "hecke"), str(_COMP / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp                                # noqa: E402
import numpy as np                                 # noqa: E402

from witness_base import WitnessBuilder                        # noqa: E402
from schur_principal_mpmath import (                           # noqa: E402
    y_lambda_at_q0_mpmath, partitions_of)
from atom_orbit_reduction import interface_multiset            # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A               # noqa: E402

# Reuse #4849's certified machinery verbatim -- rep, germs, transports, the
# ordered pairing and the Moebius residual are NOT re-derived here.
from nastokes_multigen_cluster_additivity_probe import (       # noqa: E402
    rep_and_germs, certify_rep, word_for_ordering, moebius_residual,
    omega_for_subset, fro, _blocks)

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP             # noqa: E402

Q0 = Q_MP          # EXPERIMENTAL PROTON ANCHOR
TOL_ZERO = 1e-8

ISOTOPES = [("D", 1, 1), ("T", 1, 2), ("He3", 2, 1), ("He4", 2, 2)]
N_STRANDS = 12                       # H_12: A = 2,3,4 words all embed
SHAPE = (10, 1, 1)                   # #4849's representative lambda |- 12


# ---------------------------------------------------------------------------
# Part A.  The orbit identity is vacuous as an ordering symmetry
# ---------------------------------------------------------------------------


def orderings_of(Z: int, N: int):
    """All distinct cross-species orderings of the multiset (Z protons, N neutrons)."""
    return sorted({"".join(o) for o in
                   set(itertools.permutations("p" * Z + "n" * N))})


def same_species_orbit_of_strings(Z: int, N: int):
    """Orbit of the canonical ordering STRING under S_Z x S_N.

    A same-species permutation permutes proton labels among themselves and
    neutron labels among themselves; acting on the canonical string it is a
    permutation of positions 0..Z-1 and of positions Z..A-1.  Since every
    proton position carries 'p' and every neutron position carries 'n', the
    string is FIXED -- Lemma 1(a).  Enumerated rather than asserted.
    """
    canon = "p" * Z + "n" * N
    out = set()
    for sp in itertools.permutations(range(Z)):
        for sn in itertools.permutations(range(N)):
            perm = list(sp) + [Z + i for i in sn]
            out.add("".join(canon[perm[k]] for k in range(Z + N)))
    return out


# ---------------------------------------------------------------------------
# Part B.  tr_M from the canonical Frobenius pairing, certified
# ---------------------------------------------------------------------------


def seminormal_np(shape, q):
    """rho(sigma_i), i = 0..n-2, float64 (numpy).  Same closed form as #4849."""
    sig, _germs, dim, h = rep_and_germs(shape, q)
    return sig, dim, h


def _letters_to_mat(word, sig, dim):
    """rho(prod of letters (c, d, g) -> c*sigma_g + d*1)."""
    I = np.eye(dim)
    P = I
    for (c, d, g) in word:
        P = P @ (float(c) * sig[g] + float(d) * I)
    return P


class MarkovTrace:
    """tr_M(beta) = sum_{lambda |- n} y_lambda(q0) * chi^lambda(beta)."""

    def __init__(self, n: int, q):
        self.n = n
        self.shapes = partitions_of(n)
        yl = y_lambda_at_q0_mpmath(n, q)
        self.y = {s: float(yl[s]) for s in self.shapes}
        self.rep = {}
        self.worst_cert = 0.0
        for s in self.shapes:
            sig, dim, h = seminormal_np(s, q)
            self.worst_cert = max(self.worst_cert, certify_rep(sig, dim, h))
            self.rep[s] = (sig, dim)
        self.f = {s: self.rep[s][1] for s in self.shapes}

    def __call__(self, word) -> float:
        tot = 0.0
        for s in self.shapes:
            sig, dim = self.rep[s]
            tot += self.y[s] * float(np.trace(_letters_to_mat(word, sig, dim)))
        return tot

    def normalisation(self) -> float:
        """sum_lambda y_lambda * f^lambda -- must be tr_M(1) = 1."""
        return sum(self.y[s] * self.f[s] for s in self.shapes)


def certify_markov(tr: MarkovTrace, word, n: int):
    """M1 (cyclic) and M2 (stabilisation) certification.  Returns a dict."""
    out = {}
    out["tr_identity"] = tr([])
    out["normalisation"] = tr.normalisation()

    # M1: tr_M(AB) = tr_M(BA) for several splits of the real atom word.
    m1 = 0.0
    base = tr(word)
    for cut in (1, len(word) // 3, len(word) // 2, 2 * len(word) // 3, len(word) - 1):
        rot = word[cut:] + word[:cut]
        m1 = max(m1, abs(tr(rot) - base) / max(abs(base), 1e-300))
    out["M1_max_rel"] = m1

    # M2: tr_M(beta . sigma_{n-1}) = z . tr_M(beta) for beta in H_{n-1}.
    # Measure z over several beta; a CONSTANT ratio is what pins y_lambda as the
    # Jones-Markov weights (M1 alone holds for any character weights).
    zs = []
    for k in (3, 7, 11, 15):
        beta = [(c, d, g) for (c, d, g) in word[:k] if g < n - 2]
        b = tr(beta)
        if abs(b) < 1e-12:
            continue
        zs.append(tr(beta + [(1.0, 0.0, n - 2)]) / b)
    out["M2_z"] = zs[0] if zs else None
    out["M2_max_rel_spread"] = (
        (max(zs) - min(zs)) / max(abs(zs[0]), 1e-300) if len(zs) > 1 else None)
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def f64_json(o):
    """Serialize an f64 result tree for a witness: every float becomes its own
    repr string; ints/bools/None/strings pass through.

    Same rationale as nastokes_multigen_cluster_additivity_probe.f64_json: the
    numeric sweep here is float64 by design, so repr(float) is exactly the ~17
    digits the kernel produced. It round-trips bit-exactly and keeps raw
    float64 JSON out of the witness. Applied once at the sink so a field added
    later cannot miss it.
    """
    if isinstance(o, bool) or o is None:
        return o
    if isinstance(o, float):
        return repr(o)
    if isinstance(o, dict):
        return {k: f64_json(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [f64_json(v) for v in o]
    return o


def main() -> int:
    t0 = time.time()
    W = 96
    print("=" * W)
    print("  Bean qou-prjo, principle (i): is a nucleon-symmetric readout FORCED?")
    print("=" * W)
    print(f"  q0 (EXPERIMENTAL PROTON ANCHOR) = {mp.nstr(Q0, 20)}")
    print("  y_lambda: schur_principal_mpmath.y_lambda_at_q0_mpmath (live closed form,")
    print("            NOT the muon-built cache)")

    results, assertions, caveats = {}, {}, []

    # ---- Part A -------------------------------------------------------------
    print("\n" + "=" * W)
    print("  [PART A]  The S_Z x S_N orbit identity, anatomised")
    print("=" * W)
    print("    'group' = |S_Z x S_N| = Z!N!;  'string orbit' = its orbit on the")
    print("    ordering string;  'S_A words' = distinct cross-species orderings.")
    print()
    print(f"    {'atom':6s} {'Z,N':>6s} {'|group|':>8s} {'|string orbit|':>15s} "
          f"{'|S_A orderings|':>16s} {'distinct interface multisets':>30s}")
    print("    " + "-" * 88)
    partA = {}
    vacuous = True
    sa_nontrivial = True
    for name, Z, N in ISOTOPES:
        grp = math.factorial(Z) * math.factorial(N)
        orb = same_species_orbit_of_strings(Z, N)
        ords = orderings_of(Z, N)
        ifaces = sorted({tuple(sorted(interface_multiset(o).items())) for o in ords})
        partA[name] = dict(Z=Z, N=N, group_order=grp, string_orbit_size=len(orb),
                           n_SA_orderings=len(ords),
                           n_distinct_interface_multisets=len(ifaces),
                           SA_orderings=ords)
        print(f"    {name:6s} {f'{Z},{N}':>6s} {grp:>8d} {len(orb):>15d} "
              f"{len(ords):>16d} {len(ifaces):>30d}")
        vacuous = vacuous and (len(orb) == 1)
        if len(ords) > 1:
            sa_nontrivial = sa_nontrivial and (len(ifaces) > 1 or len(ords) > 1)
    print()
    print("    => the S_Z x S_N orbit of ORDERING STRINGS is a single point for every")
    print("       atom, while |S_Z x S_N| = Z!N! > 1.  Lemma 1 holds because the word")
    print("       NEVER CHANGES, so orbit-symmetrization over the forced group is the")
    print("       IDENTITY MAP on every readout.  It cannot cancel anything.")
    assertions["same_species_orbit_of_strings_is_a_point"] = 1 if vacuous else 0
    assertions["cross_species_orderings_are_distinct"] = 1 if sa_nontrivial else 0

    # the words themselves must genuinely differ across species orderings
    diff_words = {}
    for name, Z, N in ISOTOPES:
        ords = orderings_of(Z, N)
        ws = {o: tuple((float(c), float(d), g) for (c, d, g) in word_for_ordering(o))
              for o in ords}
        diff_words[name] = len(set(ws.values()))
    print(f"\n    distinct WORDS across cross-species orderings: "
          + ", ".join(f"{k}={v}" for k, v in diff_words.items()))
    results["part_A"] = partA
    results["distinct_words_across_SA_orderings"] = diff_words
    assertions["SA_orderings_give_distinct_words"] = \
        1 if all(diff_words[n] == partA[n]["n_SA_orderings"] for n in diff_words) else 0

    # ---- Part B -------------------------------------------------------------
    print("\n" + "=" * W)
    print("  [PART B]  Is the corpus's OWN tr_M cross-species ordering-dependent?")
    print("=" * W)
    partB = {}
    ordering_dep = True
    for name, Z, N in ISOTOPES[:3]:          # D (n=6), T (n=9), He3 (n=9)
        n = 3 * (Z + N)
        t1 = time.time()
        tr = MarkovTrace(n, Q0)
        canon_word = [(float(c), float(d), g) for (c, d, g) in atom_braid_word_3A(Z, N)]
        cert = certify_markov(tr, canon_word, n)
        print(f"\n    {name}  (Z={Z}, N={N}, n={n} strands, {len(tr.shapes)} partitions)")
        print(f"      certification:  rep worst residual {tr.worst_cert:.2e}")
        print(f"                      tr_M(1) = {cert['tr_identity']:.15f}  "
              f"(must be 1)")
        print(f"                      M1 cyclic max rel dev = {cert['M1_max_rel']:.2e}")
        z_txt = "n/a" if cert["M2_z"] is None else f"{cert['M2_z']:.12f}"
        sp_txt = ("n/a" if cert["M2_max_rel_spread"] is None
                  else f"{cert['M2_max_rel_spread']:.2e}")
        print(f"                      M2 stabilisation z = {z_txt}"
              f"   spread over beta = {sp_txt}")
        ok_cert = (tr.worst_cert < 1e-9 and abs(cert["tr_identity"] - 1.0) < 1e-9
                   and cert["M1_max_rel"] < 1e-9
                   and (cert["M2_max_rel_spread"] is None
                        or abs(cert["M2_max_rel_spread"]) < 1e-9))
        assertions[f"trM_certified_{name}"] = 1 if ok_cert else 0

        vals, ifm = {}, {}
        for o in orderings_of(Z, N):
            vals[o] = tr(word_for_ordering(o))
            ifm[o] = tuple(sorted(interface_multiset(o).items()))
        lo, hi = min(vals.values()), max(vals.values())
        spread = hi / lo if lo != 0 else float("inf")
        canon = "p" * Z + "n" * N
        for o, v in vals.items():
            mark = "  <- canonical (interface-minimal)" if o == canon else ""
            rel = (v - vals[canon]) / abs(vals[canon])
            im = ",".join(f"{k}:{c}" for k, c in ifm[o])
            print(f"      tr_M({o:<4s}) = {v: .12e}   rel to canonical {rel:+.3e}"
                  f"   ifaces {{{im}}}{mark}")
        # structural read: does the trace track the INTERFACE MULTISET exactly?
        by_if, tracks = {}, True
        for o, v in vals.items():
            by_if.setdefault(ifm[o], []).append(v)
        for grp in by_if.values():
            if max(grp) - min(grp) > 1e-12 * max(abs(x) for x in grp):
                tracks = False
        n_if = len(by_if)
        print(f"      spread max/min = {spread:.6f}   "
              f"({n_if} distinct interface multiset(s); trace constant within each: "
              f"{tracks})   [{time.time()-t1:.1f}s]")
        partB[name] = dict(n=n, values={o: v for o, v in vals.items()},
                           interface_multisets={o: dict(ifm[o]) for o in ifm},
                           n_distinct_interface_multisets=n_if,
                           trace_constant_within_interface_class=bool(tracks),
                           spread_max_over_min=spread,
                           canonical=canon,
                           max_rel_dev_from_canonical=max(
                               abs((v - vals[canon]) / vals[canon]) for v in vals.values()),
                           certification={k: (None if v is None else float(v))
                                          for k, v in cert.items()},
                           rep_worst_residual=float(tr.worst_cert))
        # An atom whose S_A orderings all share ONE interface multiset (D) is a
        # NULL control: the trace must be ordering-invariant there.  An atom with
        # several (T, He3) is the positive case.
        if n_if > 1:
            ordering_dep = ordering_dep and (
                partB[name]["max_rel_dev_from_canonical"] > 1e-9)
        else:
            assertions[f"trM_null_control_invariant_{name}"] = \
                1 if partB[name]["max_rel_dev_from_canonical"] < 1e-12 else 0
        assertions[f"trM_tracks_interface_multiset_{name}"] = 1 if tracks else 0
    results["part_B"] = partB
    assertions["corpus_trM_is_cross_species_ordering_dependent"] = 1 if ordering_dep else 0
    print()
    print("    => the corpus's OWN canonical scalar observable is cross-species")
    print("       ordering-DEPENDENT.  #4849's disqualifier ('a nuclear observable")
    print("       cannot be a function of the braid word') therefore applies verbatim")
    print("       to the canonical mass/binding trace and does NOT single out the")
    print("       transverse pairing.")

    # ---- Part C -------------------------------------------------------------
    print("\n" + "=" * W)
    print("  [PART C]  Survive or cancel")
    print("=" * W)
    print("    DERIVED symmetrization = S_Z x S_N = the identity map (Part A).")
    print("    Counterfactual = the NON-DERIVED S_A operator average, reported for all")
    print("    three of #4849's germ readings.  It selects nothing.")
    sig, germs, dim, h = rep_and_germs(SHAPE, Q0)
    worst = certify_rep(sig, dim, h)
    print(f"\n    lambda = {SHAPE}, dim = {dim}; rep worst residual {worst:.2e}")
    assertions["partC_rep_certified"] = 1 if worst < 1e-9 else 0
    Fp = {(i, i + 1): germs[i] @ germs[i + 1] - germs[i + 1] @ germs[i]
          for i in range(N_STRANDS - 2)}

    def band_local(g, _F=Fp):
        return _F[(g, g + 1)] if (g, g + 1) in _F else _F[(g - 1, g)]

    READINGS = [("(0,1)", Fp[(0, 1)], None), ("(3,4)", Fp[(3, 4)], None),
                ("band-local", None, band_local)]

    partC = {}
    survives = True
    for name, Z, N in (("T", 1, 2), ("He4", 2, 2)):
        A = Z + N
        ords = orderings_of(Z, N)
        canon = "p" * Z + "n" * N
        subset = tuple(range(A))
        print(f"\n    {name}  (A={A}, {len(ords)} cross-species orderings)")
        print(f"      {'germ reading':<13s} {'||R||(canon)':>14s} {'mean||R||':>12s} "
              f"{'||<R>||':>12s} {'||<R>||/mean':>13s} {'cancels?':>9s}")
        print("      " + "-" * 78)
        rows = {}
        # NOTE: `subset` is the FULL nucleon set, so this is the top-level
        # A-body Moebius residual -- R_3 for T, R_4 for He4.  The top-level
        # residual sums over ALL subsets, so it is independent of which nucleon
        # carries which label, which is what makes the S_A average well defined.
        for label, F, co in READINGS:
            Rs, Oms = [], []
            for o in ords:
                w = [(float(c), float(d), g) for (c, d, g) in word_for_ordering(o)]
                cache = {}
                Rs.append(moebius_residual(w, subset, sig, h, dim, F,
                                           curvature_of=co, cache=cache))
                Oms.append(fro(omega_for_subset(w, subset, sig, h, dim, F,
                                                curvature_of=co, cache=cache)))
            Rc = Rs[ords.index(canon)]
            mean_norm = float(np.mean([fro(R) for R in Rs]))
            avg = sum(Rs) / len(Rs)
            ratio = fro(avg) / mean_norm if mean_norm > TOL_ZERO else float("nan")
            cancels = ratio < 1e-3
            print(f"      {label:<13s} {fro(Rc):>14.4e} {mean_norm:>12.4e} "
                  f"{fro(avg):>12.4e} {ratio:>13.4f} {str(cancels):>9s}")
            rows[label] = dict(
                R_canonical=fro(Rc), R_mean_norm=mean_norm,
                R_SA_average_norm=fro(avg), SA_average_over_mean=ratio,
                SA_average_cancels=bool(cancels),
                Omega_canonical=Oms[ords.index(canon)],
                R_rel_canonical=(fro(Rc) / Oms[ords.index(canon)]
                                 if Oms[ords.index(canon)] > TOL_ZERO else None),
                per_ordering={o: fro(R) for o, R in zip(ords, Rs)})
            # He4 + band-local is the ONE reading where #4849 s4.2 already found
            # the 4-body cluster level empty (||R_4|| ~ 1e-11).  Reproducing that
            # zero is a cross-check, not a failure of survival; exclude it from
            # the survival assertion and assert the zero separately.
            if name == "He4" and label == "band-local":
                assertions["He4_bandlocal_4body_level_empty_reproduces_4849"] = \
                    1 if fro(Rc) < 1e-8 else 0
            else:
                survives = survives and fro(Rc) > TOL_ZERO
        partC[name] = rows
    results["part_C"] = partC
    assertions["residual_survives_the_derived_symmetrization"] = 1 if survives else 0
    # the counterfactual S_A average does not cancel either, on those same readings
    no_cancel = all(
        r["SA_average_over_mean"] > 0.5
        for nm, rows in partC.items() for lb, r in rows.items()
        if not (nm == "He4" and lb == "band-local"))
    assertions["SA_counterfactual_average_does_not_cancel"] = 1 if no_cancel else 0
    print()
    print("    DERIVED readout: symmetrization is the identity, so ||R|| is exactly")
    print("    ||R||(canon) above -- unchanged, nonzero.  R SURVIVES, by derivation.")
    print("    Counterfactual: the S_A average does NOT cancel either (ratios O(1)),")
    print("    so even the non-derived symmetrization would have left a signal.")

    # ---- mpmath precision control (Part B, n = 6) ---------------------------
    print("\n" + "=" * W)
    print("  [PRECISION CONTROL]  Part B at n = 6 re-run in mpmath 40 dps")
    print("=" * W)
    ctl = {}
    shapes6 = partitions_of(6)
    yl6 = y_lambda_at_q0_mpmath(6, Q0)
    for o in orderings_of(1, 1):
        tot = mp.mpf(0)
        for s in shapes6:
            per_gen, d = _blocks(s)
            one = mp.mpf(1)
            hq = Q0 - one / Q0
            sg = []
            for blocks in per_gen:
                M = mp.zeros(d, d)
                for (i, j, r) in blocks:
                    a = hq / (one - Q0 ** (-2 * r))
                    ap = hq / (one - Q0 ** (2 * r))
                    if j is None:
                        M[i, i] = a
                    else:
                        M[i, i], M[j, j] = a, ap
                        b = mp.sqrt(a * ap + one)
                        M[i, j], M[j, i] = b, b
                sg.append(M)
            P = mp.eye(d)
            for (c, dd, g) in word_for_ordering(o):
                P = P * (mp.mpf(c) * sg[g] + mp.mpf(dd) * mp.eye(d))
            tot += yl6[s] * sum(P[i, i] for i in range(d))
        ctl[o] = tot
        print(f"    mpmath tr_M({o}) = {mp.nstr(tot, 25)}")
    f64 = partB["D"]["values"]
    rel = max(abs(float(ctl[o]) - f64[o]) / abs(f64[o]) for o in ctl)
    dev_mp = abs(ctl["np"] - ctl["pn"]) / abs(ctl["pn"])
    T_dev = partB["T"]["max_rel_dev_from_canonical"]
    print(f"    float64 vs mpmath max rel diff = {rel:.3e}")
    print(f"    NULL CONTROL -- D's two orderings share one interface multiset {{pn:1}},")
    print(f"      so the trace must be EXACTLY equal:")
    print(f"      mpmath |tr_M(np) - tr_M(pn)| / |tr_M(pn)| = {mp.nstr(dev_mp, 10)}")
    print(f"      => the machinery does NOT manufacture spurious ordering differences.")
    print(f"    POSITIVE CASE -- T's measured spread is {T_dev:.3e}, i.e. "
          f"{T_dev/max(rel,1e-300):.1e}x the")
    print(f"      float64 noise floor: real, not arithmetic.")
    results["precision_control"] = dict(
        f64_vs_mpmath_max_rel=float(rel),
        mpmath_D_null_control_rel_dev=float(dev_mp),
        T_rel_dev_over_noise_floor=float(T_dev / max(rel, 1e-300)))
    assertions["null_control_D_exactly_invariant_at_40dps"] = \
        1 if float(dev_mp) < 1e-30 else 0
    assertions["ordering_dependence_exceeds_numeric_noise"] = \
        1 if T_dev > 1e3 * rel else 0

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * W)
    print("  [VERDICT]")
    print("=" * W)
    print("  1. Orbit-symmetry over S_Z x S_N is FORCED (identical particles) and")
    print("     VACUOUS (Lemma 1: the word never changes).  Symmetrizing over it is")
    print("     the identity map.")
    print("  2. R SURVIVES the derived symmetrization -- trivially, by derivation, not")
    print("     by a choice of symmetrization.")
    print("  3. Cross-species reordering is NOT a symmetry: the corpus's own tr_M is")
    print("     ordering-dependent, so #4849's disqualifier is VOID as a reason to")
    print("     reject the transverse pairing specifically.")
    print("  4. Blocker (i) is DISSOLVED, not solved.  Blocker (ii) -- which germ")
    print("     observer pair, plus the representation gauge (16.4x spread, #4849")
    print("     sections 4.4/2.3) -- is UNTOUCHED and still binding.")
    print("  5. Nothing wired.  free_parameters = 0.  Bean qou-prjo stays OPEN.")
    print(f"\n  wall {time.time()-t0:.1f}s")

    # ---- witness ------------------------------------------------------------
    w = WitnessBuilder("nastokes-orbit-symmetric-readout", engine="numpy+mpmath",
                       output_dir=HERE)
    w.set_description(
        "Bean qou-prjo, principle (i) from PR #4849: is a nucleon-symmetric readout "
        "FORCED by the corpus's treatment of an atom, and does the super-pairwise "
        "transverse residual survive it? Part A anatomises the corpus orbit identity "
        "tr_M(beta) = tr_M(rep): it is over S_Z x S_N only, and its Lemma 1 establishes "
        "it by showing such a permutation leaves the braid WORD unchanged -- the orbit of "
        "ordering strings is a SINGLE POINT for every atom while |S_Z x S_N| = Z!N! > 1. "
        "So symmetrization over the forced group is the IDENTITY MAP and R survives "
        "trivially, by derivation rather than by choosing a symmetrization. Part B is the "
        "decisive control: the corpus's OWN canonical scalar observable tr_M (Frobenius "
        "pairing sum_lambda y_lambda chi^lambda, certified by tr_M(1)=1, Markov M1 cyclic "
        "invariance and constant M2 stabilisation ratio) is itself CROSS-SPECIES "
        "ORDERING-DEPENDENT, so #4849's disqualifier -- a nuclear observable cannot be a "
        "function of the braid word -- applies verbatim to the canonical mass/binding "
        "trace and does not single out the transverse pairing. Part C reports the "
        "non-derived S_A operator average as a labelled counterfactual only; it selects "
        "nothing and does not cancel either. Blocker (i) is DISSOLVED, not solved; "
        "blocker (ii) (which germ observer pair + the representation gauge) is untouched "
        "and still binding. Nothing wired, no AME input, free_parameters = 0."
    )
    w.set_audit_only(True)
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("q0_pin", "experimental/proton (qou_substrate.constants); the A>=3 "
                              "germ is q-DEPENDENT (#4849 s5.2) so the pin is material")
    w.add_parameter("y_lambda_source",
                    "schur_principal_mpmath.y_lambda_at_q0_mpmath (live closed form; "
                    "NOT the muon-built y-lambda-at-q0 cache)")
    w.add_parameter("free_parameters", 0)
    w.add_parameter("derived_symmetrization_group", "S_Z x S_N (identical particles)")
    w.add_parameter("derived_symmetrization_action", "identity on the word (Lemma 1)")
    w.add_parameter("counterfactual_group", "S_A cross-species (NOT derived, NOT a symmetry)")
    w.add_parameter("algebra", "H_12(q) seminormal/Hoefsmit for Part C; H_{3A}(q) for Part B")
    w.add_parameter("shape_partC", str(SHAPE))
    for k, v in results.items():
        w.add_data(k, f64_json(v))
    for k, v in assertions.items():
        w.add_assertion(k, v, 1)
    w.add_caveat("SCOPE-(b) for the vacuity claim (a proved structural fact about the "
                 "corpus construction: the S_Z x S_N orbit of ordering strings is a "
                 "single point, so symmetrization over the forced group is the identity). "
                 "SCOPE-(a) for everything else: this DISSOLVES blocker (i); it does not "
                 "determine any value and does not close the binding magnitude. Bean "
                 "qou-prjo stays OPEN.")
    w.add_caveat("Blocker (ii) is UNTOUCHED: the transverse pairing still varies 16.4x "
                 "with the germ observer pair and carries #4849 s2.3's unpinned "
                 "connection gauge. This probe does NOT revive the transverse route.")
    w.add_caveat("SEPARATE FINDING (not a transverse-route matter): the corpus's "
                 "canonical cross-species ordering p...pn...n is a CHOICE. The orbit "
                 "identity does not license it (it covers only S_Z x S_N, under which "
                 "the word is fixed), 'interface-minimal' is stated as a cost property "
                 "rather than a physical selection rule, and Part B measures that the "
                 "canonical trace DEPENDS on the choice. Filed as its own bean.")
    w.add_caveat("Arithmetic: float64 for the sweep with an independent mpmath 40-dps "
                 "re-run of Part B at n = 6 as the control; the measured ordering "
                 "dependence exceeds the float64 noise floor by many orders. The "
                 "verdict is an equal-vs-unequal question, not a 1-ppQ question.")
    for c in caveats:
        w.add_caveat(c)
    w.save()
    print("witness -> nastokes-orbit-symmetric-readout.witness.json")

    ok = all(v == 1 for v in assertions.values())
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
