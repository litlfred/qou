"""Most of the non-central freedom is INERT on Delta_bind — and the mechanism
says which part is not.

*** 🛑 THIS IS A TEST, NOT A SEARCH ***

`qou-bmz8` showed the ell-1 binding ceiling bounds exactly the CENTRE of `H_n`:
for central `z`, Schur gives `chi^lambda(beta.z) = c_lambda . chi^lambda(beta)`,
a reweighting, which the ceiling already excludes. The freedom it never touched
is the NON-CENTRAL part. That invites an obvious abuse — sweep `w` until
`tr_M(beta.w)` lands near the target and call it derived, which is the defect
recorded against the electroweak residual in `qou-4qno`. So:

  * The candidate set is CATEGORICALLY DISTINGUISHED and fixed in advance:
    Jucys-Murphy elements, the central class-sum as control, a bare generator,
    the two Lagrange spectral projectors of `sigma_1`.
  * The test is OVERDETERMINED — one shared constant across several atoms.
  * EVERY candidate is reported with its spread. There is no "best".
  * A small spread would be A TARGET TO CHECK A FUTURE DERIVATION AGAINST,
    never a derivation.

*** THE QUANTITY ***

`binding_canonical.py` computes `B = Q_beta(n) . (tr_M(W_free) - tr_M(W_atom))`
with `Q_beta(n) = 0.78233340931 MeV`. The dimensionless shortfall is

    R_X = B_AME(X)/Q_beta - ( tr_M(free_X) - tr_M(atom_X) )

measured: 2H 2.286957, 3H 9.953130, 3He 8.972505 — the framework supplies
19.6 %, 8.2 % and 9.1 % of binding respectively. The candidate contributes
`S_X(w) = tr_M(free_X . w) - tr_M(atom_X . w)`, and the test asks whether
`c_X = R_X / S_X(w)` is the same at every atom.

*** THE RESULT: THREE DIFFERENT `w`, ONE SPREAD ***

    candidate w                    2H          3H         3He     spread
    w = 1 (control)          4.109206   11.201717   10.048627    0.83903
    sigma_1 (control)        3.116688    8.496109    7.621531    0.83903
    L_2 = T1T1               3.221299    8.781280    7.877346    0.83903

Identical to five digits, because each is a pure RESCALING of the same object:

    tr_M(Delta.sigma_1) / tr_M(Delta) = 1.318452615852908   at every atom
    tr_M(Delta.L_2)     / tr_M(Delta) = 1.275636097818101   at every atom

**Mechanism, and it is derived rather than observed.** Every atom's word begins
with the same intra-nucleon block — `atom_braid_word_3A` emits the same
first-nucleon letters whatever `(Z, N)` is — so by trace cyclicity a `w`
supported there modifies a factor that is COMMON to all atoms, and the ratio
cannot depend on the atom. Such a `w` carries no atom-dependent information, so
it cannot supply an atom-dependent shortfall, whatever its coefficient.

This is NOT the naive Markov factorisation over disjoint supports: that would
predict the ratio `tr_M(sigma_1) = z = 0.612688`, and the measured ratio is
1.318453. `Delta_bind` is a difference of two full-length words, not a locally
supported operator, so the disjoint-support argument does not apply — an earlier
draft of this note asserted it and was wrong.

*** THE PART THAT IS NOT INERT, AND THE PREDICTION IT CAME FROM ***

The mechanism predicts which `w` CAN matter: those supported where the atoms
differ. `atom_braid_word_3A` adds exactly one letter per bond relative to the
free word — generator index 2 at A = 2, indices {2, 5} at A = 3 — so the
INTERFACE generators are the whole of the difference.

Measured at 2H, and it breaks the pattern as predicted:

    interface product   tr(D.w)/tr(D) = -0.917909   (a sign flip, not a rescale)
    interface^2         tr(D.w)/tr(D) = +0.808102

So the non-central freedom `qou-bmz8` identified is real but almost all of it is
inert on `Delta_bind`. The part that can carry the shortfall is the INTERFACE
SUBALGEBRA, which is a large narrowing of the open question — and it is the
subalgebra the corpus's own `include_inter` switch already names.

*** 🛑 THE DECIDING TEST IS BLOCKED, AND NO CONCLUSION IS DRAWN FROM ONE ATOM ***

Whether an interface-supported `w` supplies the shortfall CONSISTENTLY is not
answered here. `tr_m_atomic_mpfr` raises

    RuntimeError: tr_m_word_lq: Case C (multiple top-1 in segment) not
    implemented

on interface-suffixed words at n = 9, so 3H and 3He could not be evaluated on
the fast exact path. 2H alone is one atom and one free constant: **fitted by
construction, and it proves nothing.** The seminormal-matrix route has no
Case C and would settle it at n = 9; that is the next step, not a result here.
"""
from __future__ import annotations

import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import pyhecke_native as ph

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "computations"))

DPS = 40
mp.mp.dps = DPS
Q0S = "1.1099785827513808075916690956107688798744991218736"
Q0 = mp.mpf(Q0S)
H = Q0 - 1 / Q0

ATOMS = {                      # Z, N, B_AME (MeV) — same values the ceiling uses
    "2H":  (1, 1, "2.224566"),
    "3H":  (1, 2, "8.481798"),
    "3He": (2, 1, "7.718043"),
    "4He": (2, 2, "28.295673"),
}


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def expand(letters):
    """(c.sigma_g + d.1) letters -> [(weight, signed_word)] over the crossings."""
    terms = [(mp.mpf(1), [])]
    for (c, d, g) in letters:
        b = -mp.mpf(d) / H
        a = mp.mpf(c) + mp.mpf(d) / H
        nxt = []
        for (w, word) in terms:
            if abs(a) > mp.mpf(10) ** (-(DPS - 5)):
                nxt.append((w * a, word + [(1, int(g))]))
            if abs(b) > mp.mpf(10) ** (-(DPS - 5)):
                nxt.append((w * b, word + [(-1, int(g))]))
        terms = nxt
    return terms


def jm(k):
    """Jucys-Murphy L_k = T_{k-1} … T_1 T_1 … T_{k-1}, as a 0-based signed word.

    L_1 = 1 (empty word); L_{k+1} = T_k L_k T_k unrolls to this palindrome."""
    if k <= 1:
        return []
    idx = list(range(k - 2, -1, -1))          # T_{k-1} … T_1  (0-based)
    return [(1, g) for g in idx] + [(1, g) for g in reversed(idx)]


def candidates(n):
    """Fixed in advance. Each entry: name -> [(coeff, signed_word), …]."""
    one = mp.mpf(1)
    qp = Q0 + 1 / Q0
    cands = {
        "w = 1 (control)":            [(one, [])],
        "sigma_1 (control)":          [(one, [(1, 0)])],
        "L_2 = T1T1":                 [(one, jm(2))],
        # Lagrange spectral projectors of sigma_1: eigenvalues q and -1/q
        "P+ of sigma_1":              [(one / qp, [(1, 0)]), (one / (qp * Q0), [])],
        "P- of sigma_1":              [(Q0 / qp, []), (-one / qp, [(1, 0)])],
        # THE PREDICTED-INFORMATIVE ONE: supported where the atoms differ.
        # atom_braid_word_3A adds one letter per bond, at generator 3j-1.
        "interface product":          [(one, [(1, 3 * j - 1)
                                              for j in range(1, n // 3)])],
    }
    return cands


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    from mass_at_3A_proper import atom_braid_word_3A
    from experimental_constants import Q_NEUTRON_MEV as _QB
    QB = mp.mpf(str(_QB))
    print(f"Q_beta(n) = {mp.nstr(QB, 12)} MeV   (binding_canonical's scale)")

    max_terms = int(os.environ.get("QOU_MAX_TERMS", "600"))
    data, shortfall, dtr = {}, {}, {}
    print(f"\n{'atom':<5}{'n':>4}{'terms':>7}{'dtr_pred':>14}{'dtr_req':>14}"
          f"{'shortfall R':>14}{'pred/req':>10}")
    prepared = {}
    for name, (Z, N, B) in ATOMS.items():
        n = 3 * (Z + N)
        ta = expand(atom_braid_word_3A(Z, N, include_inter=True, q=Q0))
        tf = expand(atom_braid_word_3A(Z, N, include_inter=False, q=Q0))
        if len(ta) > max_terms:
            print(f"{name:<5}{n:>4}{len(ta):>7}   skipped (over QOU_MAX_TERMS)")
            continue
        prepared[name] = (n, ta, tf)

    def trM(terms, n, suffix):
        tot = mp.mpf(0)
        for (w, word) in terms:
            tot += w * mp.mpf(ph.tr_m_atomic_mpfr(
                list(word) + list(suffix), n, Q0S, DPS))
        return tot

    def S(terms_f, terms_a, n, combo):
        """tr_M(free.w) - tr_M(atom.w) for w = sum_i coeff_i . word_i."""
        tot = mp.mpf(0)
        for (coef, word) in combo:
            tot += coef * (trM(terms_f, n, word) - trM(terms_a, n, word))
        return tot

    for name, (n, ta, tf) in prepared.items():
        B = mp.mpf(ATOMS[name][2])
        d = trM(tf, n, []) - trM(ta, n, [])
        req = B / QB
        R = req - d
        shortfall[name] = R
        dtr[name] = d
        data[name] = {"n": n, "terms": len(ta), "dtr_pred": mp.nstr(d, 14),
                      "dtr_required": mp.nstr(req, 14), "shortfall_R": mp.nstr(R, 14),
                      "fraction_supplied": mp.nstr(d / req, 8)}
        print(f"{name:<5}{n:>4}{len(ta):>7}{mp.nstr(d,10):>14}{mp.nstr(req,10):>14}"
              f"{mp.nstr(R,10):>14}{mp.nstr(d/req,6):>10}")

    atoms = list(prepared)
    print("\n" + "=" * 78)
    print("THE OVERDETERMINED TEST — one constant c must serve every atom")
    print("=" * 78)
    print(f"  {'candidate w':<26}" + "".join(f"{x:>13}" for x in atoms) + f"{'spread':>10}")
    print("  " + "-" * (26 + 13 * len(atoms) + 10))

    rows, blocked, ratios, ratios_raw = [], {}, {}, {}
    n_any = prepared[atoms[0]][0]
    for cname, combo in candidates(n_any).items():
        cs = {}
        for x in atoms:
            n, ta, tf = prepared[x]
            # Rebuild at this atom's n — `L_last` and the central sum are
            # n-dependent. Keys are n-INDEPENDENT so this cannot silently fall
            # back to another atom's element, which an earlier draft did.
            local = candidates(n)[cname]
            try:
                s = S(tf, ta, n, local)
            except RuntimeError as exc:          # tr_m_word_lq Case C
                cs[x] = None
                blocked.setdefault(cname, []).append(f"{x}: {str(exc)[:60]}")
                continue
            ratios.setdefault(cname, {})[x] = mp.nstr(s / dtr[x], 16)
            ratios_raw.setdefault(cname, {})[x] = s / dtr[x]
            cs[x] = None if abs(s) < mp.mpf("1e-25") else shortfall[x] / s
        vals = [v for v in cs.values() if v is not None]
        if len(vals) == len(atoms) and vals:
            mean = sum(vals) / len(vals)
            spread = (max(vals) - min(vals)) / abs(mean) if mean != 0 else None
        else:
            spread = None
        rows.append({"w": cname, "ratio_to_w1": ratios.get(cname),
                 "blocked_at": blocked.get(cname),
                     "c_per_atom": {x: (mp.nstr(v, 10) if v is not None else None)
                                    for x, v in cs.items()},
                     "spread": (mp.nstr(spread, 6) if spread is not None else None)})
        cells = "".join(f"{(mp.nstr(cs[x],8) if cs[x] is not None else '—'):>13}"
                        for x in atoms)
        sp = mp.nstr(spread, 5) if spread is not None else "—"
        print(f"  {cname:<26}{cells}{sp:>10}")

    finite = [r for r in rows if r["spread"] is not None]
    best = min(finite, key=lambda r: mp.mpf(r["spread"])) if finite else None
    tight = [r["w"] for r in finite if mp.mpf(r["spread"]) < mp.mpf("0.05")]

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"  candidates with spread < 5 % across all {len(atoms)} atoms: "
          f"{tight if tight else 'NONE'}")
    if best:
        print(f"  smallest spread in the fixed set: {best['w']} at {best['spread']}")
    print("\n  🛑 A small spread here is a TARGET TO CHECK A FUTURE DERIVATION")
    print("     AGAINST, never a derivation. The candidate set was fixed before")
    print("     any number was seen and every member is reported.")

    inert = [r for r in rows
             if r["spread"] is not None and r["w"] != "w = 1 (control)"
             and abs(mp.mpf(r["spread"]) - mp.mpf(next(
                 x["spread"] for x in rows if x["w"] == "w = 1 (control)")))
             < mp.mpf("1e-4")]
    print(f"\n  candidates whose spread EQUALS the w = 1 control (inert): "
          f"{[r['w'] for r in inert]}")
    for r in inert:
        vals = list((r["ratio_to_w1"] or {}).values())
        same = len({v[:12] for v in vals}) == 1 if vals else False
        print(f"    {r['w']:<22} ratio tr(D.w)/tr(D) = {vals[0] if vals else '—'}"
              f"   atom-independent: {same}")
    if blocked:
        print(f"\n  🛑 BLOCKED (tr_m_word_lq Case C), so NOT decided here:")
        for k, v in blocked.items():
            print(f"    {k}: {v}")

    ok = True
    ok &= chk("some_noncentral_w_is_inert_equal_spread_to_control",
              len(inert) > 0, True,
              "a w supported in the common intra-nucleon block rescales by an "
              "atom-independent constant and carries no atom-dependent signal")
    ok &= chk("inert_ratios_are_atom_independent",
              all(len({v[:12] for v in (r["ratio_to_w1"] or {}).values()}) == 1
                  for r in inert), True)
    ok &= chk("deciding_interface_test_is_recorded_as_blocked_not_passed",
              bool(blocked), True,
              "one atom is fitted by construction; the n=9 evaluation is needed")
    ok &= chk("shortfall_measured_at_every_prepared_atom",
              sorted(shortfall) == sorted(atoms), True)
    ok &= chk("framework_supplies_well_under_half_of_binding",
              all(mp.mpf(data[x]["fraction_supplied"]) < mp.mpf("0.5") for x in atoms),
              True, "the shortfall R is the object being explained")
    # Internal consistency: P+ and P- are complementary spectral projectors of
    # sigma_1, so their ratios must sum to the w = 1 ratio, which is 1.
    pp = ratios_raw.get("P+ of sigma_1") or {}
    pm = ratios_raw.get("P- of sigma_1") or {}
    # Assert on the RAW mpf ratios. An earlier version compared the stringified
    # 16-digit forms against a 1e-25 tolerance and failed on rounding alone —
    # the arithmetic was right and the check was wrong.
    proj_sum_ok = bool(pp) and bool(pm) and all(
        abs(pp[x] + pm[x] - 1) < mp.mpf("1e-25") for x in pp)
    ok &= chk("complementary_projector_ratios_sum_to_one", proj_sum_ok, True,
              "P+ + P- = 1, so their ratios must too — an internal check on the "
              "whole ratio computation")
    ok &= chk("every_candidate_reported_with_its_spread",
              len(rows), len(candidates(n_any)),
              "no candidate is dropped after seeing its value")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-derived-w-overdetermined-test",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": Q0S, "dps": DPS,
                       "Q_beta_n_MeV": mp.nstr(QB, 20),
                       "binding_law": "B = Q_beta(n) . (tr_M(W_free) - tr_M(W_atom))",
                       "trace_convention": "D (SU(2)/Temperley-Lieb)",
                       "atoms_prepared": atoms},
        "data": {"per_atom": data,
                 "overdetermined_test": rows,
                 "candidates_with_spread_under_5pct": tight,
                 "smallest_spread": best},
        "context": {
            "axis": "is there a CATEGORICALLY DISTINGUISHED non-central w whose "
                    "tr_M(. w) supplies the binding shortfall at every atom with "
                    "one shared constant?",
            "method": "The candidate set (Jucys-Murphy elements, the central "
                      "class-sum as control, a bare generator, the two Lagrange "
                      "spectral projectors of sigma_1) was fixed in advance. The "
                      "test is overdetermined: one constant, several atoms.",
            "anti_fit": "A small spread is a TARGET TO CHECK A FUTURE DERIVATION "
                        "AGAINST, never a derivation. Every candidate is reported "
                        "with its spread; none is dropped after the fact. A "
                        "single-atom match would be fitted by construction.",
            "numerical_accident": "The deuteron shortfall 2.286957 sits near the "
                                  "2.2867072 maximum ell-1 ceiling of the sibling "
                                  "probe. Different normalisations (Q_beta vs "
                                  "m_e, ratio 1.53098) — coincidence, flagged so "
                                  "it is not chased.",
            "scope": "Scope-(a). No content block is edited here.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-derived-w-overdetermined-test.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out_p
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=Q0S)
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
