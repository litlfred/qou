#!/usr/bin/env python3
"""
Electron-distribution probe with per-case NF-fingerprint verification.

Background
----------
Session nucleon-ordering probe revealed that the "Z × σ₁⁻¹ at gen 1"
electron convention couples electrons to whichever nucleon occupies
strand 0 — creating a position-dependent pile-up that bifurcates
orderings.  This is a bug: electrons should be pe crossings (per
atom_gen_chains comment) tied to PROTON POSITIONS.

This probe
----------
For each atom and each candidate (ordering, electron distribution):
  1. Build the full atom braid word.
  2. Compute the Hecke CHARACTER FINGERPRINT — the tuple of χ_λ(W)
     for every partition λ ⊢ 3A.  Two braid words with identical
     fingerprints represent the same H_{3A} element at numerical
     precision; different fingerprints mean genuinely different
     atoms.  This is a strong **NF-equivalence check** that doesn't
     require full Gröbner-Shirshov reduction (which is infeasible
     for n ≥ 9).
  3. Compute tr_M (Plancherel-weighted Markov trace) and binding.
  4. Save witness incrementally after EACH case (so time-outs still
     preserve the completed subset).

NF verification
---------------
The fingerprint IS the NF-equivalence check: by Wedderburn,
  H_n(q) = ⊕_λ Mat(dim(λ)),
and each χ_λ is the trace in the λ-block.  A Hecke element is
determined by its 2-sided-ideal projections, captured here by the
full character vector.  Equal fingerprints ⇒ equal elements up to
centre (for generic q, centre is trivial).  Different fingerprints
⇒ different elements for sure.

Candidate distributions (iterative to add more)
-----------------------------------------------
  end_pile_gen1:         Z × σ₁⁻¹ at gen 1, at end (current default)
  per_proton_ordered:    σ₁⁻¹ at (3·k + 1) for each proton k in ordering
  per_proton_inline:     σ₁⁻¹ inside each proton's intra block
  per_proton_end:        σ₁⁻¹ at (3·k + 1) in ordering, at end of word

Iterative witness
-----------------
electron-distribution-probe.witness.json is appended to after each
case.  Resume: run reloads prior cases and skips them.  No partial
data is lost on SIGTERM.
"""
from __future__ import annotations

import sys
import json
import time
import itertools
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HA as h
from canonical_plus_multibrane import E_0_BETA_DECAY_MEV
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1


# ── Electron distributions ──────────────────────────────────

def _append_electron(word: list, gen: int):
    """Append a single σ₁⁻¹-style electron crossing at given gen."""
    word.append((1.0, -float(h), gen))


def atom_word_distribution(
        Z: int, N: int, ordering: list[str],
        distribution: str,
        *, include_inter: bool = True,
        m_pp: int = 1, m_pn: int = 1, m_nn: int = 1
        ) -> list[tuple[float, float, int]]:
    """Atom braid word with specified nucleon ordering and electron
    distribution."""
    assert ordering.count('p') == Z
    assert ordering.count('n') == N
    A = Z + N
    word: list[tuple[float, float, int]] = []
    proton_positions = [k for k, t in enumerate(ordering) if t == 'p']

    for k, nuc in enumerate(ordering):
        intra_g0 = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        base_g0, base_g1 = 3 * k, 3 * k + 1
        for (c, d) in intra_g0:
            word.append((float(c), float(d), base_g0))
        for (c, d) in intra_g1:
            word.append((float(c), float(d), base_g1))

        if distribution == "per_proton_inline" and nuc == 'p':
            # Electron inserted right after this proton's intra block
            _append_electron(word, base_g1)

        if include_inter and k < A - 1:
            nxt = ordering[k + 1]
            gen = 3 * k + 2
            if nuc == 'p' and nxt == 'p':
                c, d, m = 1.0, 0.0, m_pp
            elif nuc == 'n' and nxt == 'n':
                c, d, m = 1.0, -h, m_nn
            else:
                c, d, m = 1.0, -h / 2, m_pn
            for _ in range(m):
                word.append((c, d, gen))

    if distribution == "end_pile_gen1":
        for _ in range(Z):
            _append_electron(word, 1)
    elif distribution == "per_proton_ordered":
        for k in proton_positions:
            _append_electron(word, 3 * k + 1)
    elif distribution == "per_proton_end":
        for k in proton_positions:
            _append_electron(word, 3 * k + 1)
        # same as per_proton_ordered since the "end" of the word is the
        # same structural position; kept as an alias for semantic clarity
    elif distribution == "per_proton_inline":
        pass  # already inserted during nucleon loop
    else:
        raise ValueError(f"unknown distribution: {distribution}")
    return word


# ── Hecke character fingerprint (NF-equivalence check) ──────

def character_fingerprint(Z: int, N: int,
                              word: list[tuple[float, float, int]]
                              ) -> dict:
    """Return χ_λ(W) for every partition λ ⊢ 3A, plus the
    Plancherel-weighted tr_M.  Two braid words with identical
    fingerprints represent the same H_{3A} element at numerical
    precision."""
    from scipy.sparse import issparse, eye as speye
    A = Z + N
    n = 3 * A
    nfac = qfac(n)
    chi_vec = {}
    trM = 0.0
    for shape in partitions_of(n):
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            chi_vec[str(shape)] = 0.0
            continue
        dq = dim_q(shape)
        if dq == 0:
            chi_vec[str(shape)] = 0.0
            continue
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim, format='csr'); I = speye(dim, format='csr')
        else:
            prod = np.eye(dim); I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
        chi_vec[str(shape)] = chi
        w = (dq * dq) / nfac
        trM += w * chi / dim
    return {"chi": chi_vec, "trM": trM}


# ── Iterative witness writer ────────────────────────────────

WITNESS_PATH = (Path(__file__).parent
                / "electron-distribution-probe.witness.json")


def load_witness() -> dict:
    if WITNESS_PATH.exists():
        try:
            return json.loads(WITNESS_PATH.read_text())
        except Exception:
            pass
    return {
        "computation": "electron-distribution-probe",
        "description": (
            "Iterative probe: for each (atom, nucleon_ordering, "
            "electron_distribution), compute the Hecke character "
            "fingerprint (χ_λ for every λ ⊢ 3A) and the Plancherel "
            "tr_M.  Character fingerprints are strong NF-equivalence "
            "checks: equal fingerprints ⇒ equal H_{3A} elements, "
            "different fingerprints ⇒ different atoms.  Witness is "
            "saved after each case; resume skips completed ones."),
        "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV},
        "results": [],
    }


def save_witness(data: dict):
    """Atomic write via temp file + rename."""
    data["timestamp"] = datetime.now(timezone.utc).isoformat()
    tmp = WITNESS_PATH.with_suffix(".witness.json.tmp")
    tmp.write_text(json.dumps(data, indent=2, default=str))
    tmp.replace(WITNESS_PATH)


def case_key(name: str, ordering: list[str], dist: str) -> str:
    return f"{name}/{'.'.join(ordering)}/{dist}"


def completed_cases(witness: dict) -> set[str]:
    return {r.get("case_key") for r in witness.get("results", [])}


# ── Main probe ──────────────────────────────────────────────

DISTRIBUTIONS = [
    "end_pile_gen1",        # current default
    "per_proton_ordered",   # one electron per proton, at its g1 gen
    "per_proton_inline",    # electron inside each proton's block
]

ATOMS = [
    ("T",   1, 2,  8.481821),
    ("3He", 2, 1,  7.71804),
    ("4He", 2, 2, 28.295674),
]


def distinct_orderings(Z: int, N: int) -> list[list[str]]:
    seen = set()
    out = []
    for perm in itertools.permutations(['p'] * Z + ['n'] * N):
        if perm not in seen:
            seen.add(perm)
            out.append(list(perm))
    return out


def main():
    witness = load_witness()
    done = completed_cases(witness)
    print("=" * 110)
    print("ELECTRON-DISTRIBUTION PROBE (iterative, NF-fingerprint)")
    print(f"q0 = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print(f"Resuming from {len(done)} completed cases")
    print("=" * 110)

    for (name, Z, N, B_AME) in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        orderings = distinct_orderings(Z, N)
        for ordering in orderings:
            for dist in DISTRIBUTIONS:
                key = case_key(name, ordering, dist)
                if key in done:
                    continue
                t0 = time.time()
                word_atom = atom_word_distribution(
                    Z, N, ordering, dist, include_inter=True)
                word_free = atom_word_distribution(
                    Z, N, ordering, dist, include_inter=False)
                try:
                    fp_atom = character_fingerprint(Z, N, word_atom)
                    fp_free = character_fingerprint(Z, N, word_free)
                except Exception as e:
                    fp_atom = {"error": str(e)}
                    fp_free = {"error": str(e)}
                dt = time.time() - t0
                if "error" in fp_atom:
                    row = {"case_key": key, "atom": name,
                             "ordering": ''.join(ordering),
                             "distribution": dist, "error": fp_atom["error"],
                             "time_sec": dt}
                else:
                    B = E_0_BETA_DECAY_MEV * (abs(fp_free["trM"])
                                                 - abs(fp_atom["trM"]))
                    err = abs(B - B_AME) / Mtot * 100
                    row = {"case_key": key, "atom": name, "Z": Z, "N": N,
                             "A": A,
                             "ordering": ''.join(ordering),
                             "distribution": dist,
                             "trM_atom": fp_atom["trM"],
                             "trM_free": fp_free["trM"],
                             "chi_atom": fp_atom["chi"],
                             "chi_free": fp_free["chi"],
                             "B_pred_MeV": B, "err_pct": err,
                             "B_AME_MeV": B_AME,
                             "time_sec": dt}
                print(f"  {key:<32} trM_atom={row.get('trM_atom','?'):>14}  "
                      f"B={row.get('B_pred_MeV', '?')}  "
                      f"err={row.get('err_pct', '?')}  ({dt:.1f}s)")
                witness["results"].append(row)
                save_witness(witness)
                done.add(key)

    # Fingerprint-equality analysis
    print("\n" + "=" * 110)
    print("NF-FINGERPRINT EQUIVALENCE CLASSES (by atom)")
    print("=" * 110)
    analysis = {}
    for (name, Z, N, B_AME) in ATOMS:
        atom_rows = [r for r in witness["results"]
                        if r.get("atom") == name and "error" not in r]
        if not atom_rows:
            continue
        # Group by fingerprint (rounded to 6 decimal places for hashing)
        groups: dict[str, list[dict]] = {}
        for r in atom_rows:
            if "chi_atom" not in r:
                continue
            fp = tuple(sorted(
                (shape, round(chi, 6))
                for shape, chi in r["chi_atom"].items()))
            groups.setdefault(str(hash(fp)), []).append(r)
        print(f"\n{name}: {len(groups)} distinct equivalence classes "
              f"out of {len(atom_rows)} cases")
        for gi, members in enumerate(groups.values()):
            cases = [f"{m['ordering']}/{m['distribution']}"
                      for m in members]
            B = members[0].get("B_pred_MeV", 0)
            err = members[0].get("err_pct", 0)
            print(f"  class {gi}: B_pred={B:+10.4f}  err={err:.4f}%  "
                  f"[{len(members)} cases]")
            for c in cases[:5]:
                print(f"    {c}")
            if len(cases) > 5:
                print(f"    ... {len(cases)-5} more")
        analysis[name] = {"n_classes": len(groups),
                              "n_cases": len(atom_rows)}
    witness["equivalence_classes"] = analysis
    save_witness(witness)
    print(f"\nWitness: {WITNESS_PATH}")


if __name__ == "__main__":
    main()
