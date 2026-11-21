#!/usr/bin/env python3
"""Nuclear Regime-I shell rule: re-measure the operator selection.

Background
----------
``prop:nuclear-operator-regimes`` used to state a Regime-I rule: at a
shell-filling step the selected inter-nucleon operator is the torus knot
``T(2, n_s)``, with ``n_s`` the shell size. Its only datum was the operator
``(σ₀σ₁)²σ₀`` at the step ``p → pp``, labelled ``T(2,5)``. That word closes to
the ``T(2,4)`` link (PR #8739), so the rule was withdrawn. The witness the block
cited, ``nuclear-binding-lp.witness.json``, is not in the tree. Its producer,
``nuclear-binding-lp.py``, was moved to ``_deprecated/`` on 2026-06-15 and off
``main`` on 2026-10-10 (``6333715860``). Retrieved from git, it shows that:

* the witness never recorded the transition table. It held only an
  ``sdp_lift`` block for three pair channels. The per-step selection was
  printed to stdout and nowhere else;
* the arithmetic was float64, convention C (``z = 0.49932``, muon q₀), and the
  trace weight of ``e⁻ = σ₀σ₁σ₀`` was written ``z³``. The Markov trace gives
  ``h·z² + z`` (``pyhecke.gram.TR_M``);
* the candidate set was hand-picked and contained only three torus-labelled
  words (``T_{2,2}, T_{2,3}, T_{2,5}``). By
  ``QOU.Interactions.NuclearRegimeShellRule.not_shellRuleT2_of_bounded_index``,
  such a set cannot satisfy a ``T(2, n_s)`` rule at any shell with
  ``n_s > 5``, which includes the ``sd`` (6) and ``fp`` (12) shells.

This probe re-implements the selection in mpmath (no float64), under
convention D, at the proton q₀. The criteria were fixed before the run. They
are in ``docs/audits/2026-11-21-nuclear-regime-shell-rule.md`` §2 and are
restated here.

Pre-registered criteria (fixed before any output was looked at)
--------------------------------------------------------------
Model, unchanged from the 2026-04 producer and NOT canonical: the
nucleons are the legacy elements ``(σ₀σ₁⁻¹)³ · Π typed quark crossings`` in
``H₃(q)``. The owner's γγ selection rule now governs nucleon words, and this
element predates it. A step multiplies ``N_k · o · n_{k+1}`` in ``H₃(q)`` (GS
normal-form basis ``1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀``).

* **Cost K1 (primary, the original criterion).** The demand is the sum of the
  absolute values of the negative NF coefficients. The tie-break is the Markov
  trace ``tr_M`` under convention D, ``z = q³/(q²+1)``.
* **Cost K2 (reported, not adopted).** K1 divided by the sum of the absolute
  values of all coefficients. K1 is not scale-free: an operator with larger
  coefficients is penalised just for being larger. K2 exists to show how much
  of the K1 selection is that effect.
* **Candidate set C0.** The ten operators of the 2026-04 producer.
* **Candidate set C1.** C0 plus ``σ₀ⁿσ₁`` for ``n = 2..12``. By Markov
  stabilisation the closure of ``σ₀ⁿσ₁ ∈ B₃`` is exactly ``T(2,n)``, so C1
  contains a true ``T(2,n)`` at every ``n ≤ 12``.
* **Torus index.** ``σ₀ⁿσ₁ ↦ n``, ``L₊ = σ₀σ₁ ↦ 1`` (unknot = ``T(2,1)``),
  ``e⁻ = σ₀σ₁σ₀ ↦ 2`` (Hopf link, owner ruling 2026-11-21) and
  ``(σ₀σ₁)²σ₀ ↦ 4`` (PR #8739). Every other operator gets no index.
* **Shell size.** The size of the same-type shell entered by the added
  nucleon, with capacities ``2, 6, 12, 8, 22, 32, 44`` (cumulative magic numbers
  ``2, 8, 20, 28, 50, 82, 126``).
* **Rule test.** A step passes iff every selected operator has torus index
  equal to that shell size. The rule is tested on EVERY step: no step is
  excluded after the fact as "not Regime I".
* **Sequences.** S_He4 = ``p p n n`` and S_Li6 = ``p p n n p n`` (the
  original orders), plus ``p²⁰``, ``n²⁰`` and ``(pn)¹⁰``.
* **No rule is adopted from the output.** Any regularity seen is reported as a
  conjecture, with its evidence and a falsifier.

Precision: the work is done at ``mp.dps = 80`` and repeated at 120. A selection
counts only if both precisions agree and the cost gap to the runner-up exceeds
``10⁻⁴⁰``. The smallest gap is recorded. Selection is unchanged by positive
rescaling of the costs (``isSelected_smul_iff``), so the running nucleus is
rescaled to max-abs 1 after each step.

LP duals: each step's selection is the LP ``min Σ c_o w_o`` subject to
``Σ w_o = 1``, ``w ≥ 0``. Its dual is solved exactly: ``y0* = min c``, the
reduced costs are ``y*_o = c_o − y0*``, and the active set is
``{o : y*_o > 0}``, the constraints ``w_o ≥ 0`` that bind. The duality gap is
0. All of these are emitted per step.

Usage::

    python3 -u computations/nuclear_regime_shell_rule_probe.py 2>&1 | tee /tmp/nrsr.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from q_parameter import q_at  # noqa: E402  (proton pin: this stem is not ideal_muon)
from witness_base import WitnessBuilder  # noqa: E402

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["1", "σ₀", "σ₁", "σ₀σ₁", "σ₁σ₀", "σ₀σ₁σ₀"]
SHELL_CAPS = [2, 6, 12, 8, 22, 32, 44]


def shell_size(count: int) -> int:
    """Capacity of the same-type shell holding the `count`-th nucleon (1-based)."""
    cum = 0
    for cap in SHELL_CAPS:
        cum += cap
        if count <= cum:
            return cap
    raise ValueError(count)


class H3:
    """H₃(q) in the GS normal-form basis, mpmath coefficients at a fixed q."""

    def __init__(self, q):
        self.q = q
        self.h = q - 1 / q
        self.z = q ** 3 / (q ** 2 + 1)            # convention D
        self.z_C = mp.sqrt(q) / (q + 1)            # convention C, comparison only
        self.tr = [mp.mpf(1), self.z, self.z, self.z ** 2, self.z ** 2,
                   self.h * self.z ** 2 + self.z]
        self.tr_C = [mp.mpf(1), self.z_C, self.z_C, self.z_C ** 2, self.z_C ** 2,
                     self.h * self.z_C ** 2 + self.z_C]
        self.table = [[self._nf_word(NF_BASIS[i] + NF_BASIS[j]) for j in range(6)]
                      for i in range(6)]

    def _reduce(self, terms):
        """Same rewriting system as the 2026-04 producer: σᵢ² → hσᵢ + 1,
        aba → bab when bab is lexicographically smaller."""
        changed = True
        while changed:
            changed = False
            new = {}
            for w, c in terms.items():
                if c == 0:
                    continue
                hit = None
                for p in range(len(w) - 1):
                    if w[p] == w[p + 1]:
                        i = w[p]
                        a, b = w[:p] + (i,) + w[p + 2:], w[:p] + w[p + 2:]
                        hit = [(a, c * self.h), (b, c)]
                        break
                if hit is None:
                    for p in range(len(w) - 2):
                        x, y, u = w[p], w[p + 1], w[p + 2]
                        if x == u and abs(x - y) == 1 and (y, x, y) < (x, y, x):
                            hit = [(w[:p] + (y, x, y) + w[p + 3:], c)]
                            break
                if hit is None:
                    new[w] = new.get(w, 0) + c
                else:
                    changed = True
                    for ww, cc in hit:
                        new[ww] = new.get(ww, 0) + cc
            terms = new
        return terms

    def _nf_word(self, word):
        t = self._reduce({tuple(word): mp.mpf(1)})
        v = [mp.mpf(0)] * 6
        for w, c in t.items():
            v[NF_BASIS.index(w)] += c
        return v

    def mul(self, a, b):
        out = [mp.mpf(0)] * 6
        for i in range(6):
            if a[i] == 0:
                continue
            for j in range(6):
                if b[j] == 0:
                    continue
                c = a[i] * b[j]
                row = self.table[i][j]
                for k in range(6):
                    out[k] += c * row[k]
        return out

    def gen(self, i):
        v = [mp.mpf(0)] * 6
        v[1 + i] = mp.mpf(1)
        return v

    def one(self):
        return [mp.mpf(1)] + [mp.mpf(0)] * 5

    def inv_gen(self, i):          # σᵢ⁻¹ = σᵢ − h
        v = self.gen(i)
        v[0] = -self.h
        return v

    def word(self, letters):
        out = self.one()
        for g in letters:
            out = self.mul(out, self.gen(g) if g >= 0 else self.inv_gen(-g - 1))
        return out

    def add(self, a, b, s=1):
        return [x + s * y for x, y in zip(a, b)]

    def scal(self, a, s):
        return [s * x for x in a]

    def trace(self, v, conv="D"):
        t = self.tr if conv == "D" else self.tr_C
        return mp.fsum(x * y for x, y in zip(v, t))


def build(H):
    one = H.one()
    b3 = H.word((0, -2, 0, -2, 0, -2))            # (σ₀σ₁⁻¹)³

    def crossing(kind, gen):
        g = H.gen(gen)
        if kind == "uu":
            return g
        if kind == "dd":
            return H.add(g, H.scal(one, H.h), -1)
        return H.add(g, H.scal(one, H.h / 2), -1)

    def nucleon(types):
        e = list(b3)
        for i in range(3):
            for j in range(i + 1, 3):
                gen = min(min(i, j), 1)
                kind = ("uu" if types[i] == types[j] == "u" else
                        "dd" if types[i] == types[j] == "d" else "ud")
                e = H.mul(e, crossing(kind, gen))
        return e

    nuc = {"p": nucleon("uud"), "n": nucleon("udd")}

    # (name, element, torus index or None)
    C0 = [
        ("C_pp = σ₀", crossing("uu", 0), None),
        ("C_nn = σ₀ − h", crossing("dd", 0), None),
        ("C_pn = σ₀ − h/2", crossing("ud", 0), None),
        ("σ₀² (old 'T_{2,2}')", H.word((0, 0)), None),
        ("e⁻ = σ₀σ₁σ₀ (old 'T_{2,3}')", H.word((0, 1, 0)), 2),
        ("(σ₀σ₁)²σ₀ (old 'T_{2,5}')", H.word((0, 1, 0, 1, 0)), 4),
        ("B₃ = (σ₀σ₁⁻¹)³", list(b3), None),
        ("1", one, None),
        ("L₊ = σ₀σ₁", H.word((0, 1)), 1),
        ("L₋ = σ₁σ₀", H.word((1, 0)), None),
    ]
    C1 = C0 + [(f"σ₀^{n}σ₁ (T(2,{n}))", H.word((0,) * n + (1,)), n) for n in range(2, 13)]
    return nuc, C0, C1


def demand(v):
    return mp.fsum(-x for x in v if x < 0)


def l1(v):
    return mp.fsum(abs(x) for x in v)


def run_sequence(H, nuc, cands, seq, cost_kind):
    N = list(nuc[seq[0]])
    counts = {"p": 1 if seq[0] == "p" else 0, "n": 1 if seq[0] == "n" else 0}
    steps = []
    min_gap = None
    for k in range(1, len(seq)):
        t = seq[k]
        counts[t] += 1
        ns = shell_size(counts[t])
        rows = []
        for name, op, tidx in cands:
            r = H.mul(H.mul(N, op), nuc[t])
            d = demand(r)
            c = d if cost_kind == "K1" else (d / l1(r) if l1(r) != 0 else mp.mpf(0))
            rows.append((c, H.trace(r), name, tidx, r, H.trace(r, "C")))
        rows.sort(key=lambda x: (x[0], x[1]))
        y0 = rows[0][0]
        tol = mp.mpf(10) ** -40
        selected = [x for x in rows if x[0] - y0 <= tol]
        n_cost_tied = len(selected)
        tminC = min(x[5] for x in selected)
        sel_C = [x[2] for x in selected if x[5] - tminC <= tol]
        if len(selected) > 1:   # tie-break by tr_M
            tmin = min(x[1] for x in selected)
            selected = [x for x in selected if x[1] - tmin <= tol]
        others = [x for x in rows if x not in selected]
        gap = (others[0][0] - y0) if others else None
        if gap is not None and gap > tol:
            min_gap = gap if min_gap is None else min(min_gap, gap)
        sel = selected[0]
        passes = all(x[3] == ns for x in selected)
        steps.append({
            "step": k,
            "added": t,
            "same_type_count": counts[t],
            "shell_size": ns,
            "selected": [x[2] for x in selected],
            "selected_torus_index": [x[3] for x in selected],
            "rule_T2_ns_passes": passes,
            "cost_selected": mp.nstr(y0, 30),
            "runner_up": others[0][2] if others else None,
            "gap_to_runner_up": mp.nstr(gap, 12) if gap is not None else None,
            "tied": len(selected) > 1,
            "n_candidates_at_min_cost": n_cost_tied,
            "selected_if_conv_C_tiebreak": sel_C,
            "decided_by": "cost" if n_cost_tied == 1 else "tr_M tie-break",
            "lp_dual": {
                "y0_star": mp.nstr(y0, 30),
                "y_star": {x[2]: mp.nstr(x[0] - y0, 20) for x in rows},
                "active_set": [x[2] for x in rows if x[0] - y0 > tol],
                "primal_obj": mp.nstr(y0, 30),
                "dual_obj": mp.nstr(y0, 30),
                "duality_gap": "0",
            },
        })
        r = sel[4]
        m = max(abs(x) for x in r)
        N = [x / m for x in r] if m != 0 else r
    return steps, min_gap


SEQUENCES = {
    "S_He4": "ppnn",
    "S_Li6": "ppnnpn",
    "S_p20": "p" * 20,
    "S_n20": "n" * 20,
    "S_pn10": "pn" * 10,
}


def run_all(dps):
    mp.mp.dps = dps
    q = q_at(dps + 10)
    H = H3(q)
    nuc, C0, C1 = build(H)
    out = {}
    for cset_name, cset in (("C0", C0), ("C1", C1)):
        for cost in ("K1", "K2"):
            for sname, seq in SEQUENCES.items():
                steps, gap = run_sequence(H, nuc, cset, seq, cost)
                out[(cset_name, cost, sname)] = (steps, gap)
    return out, H, nuc


def main():
    t0 = time.time()
    res80, H, nuc = run_all(80)
    print(f"[{time.time()-t0:.1f}s] dps=80 done", flush=True)
    res120, _, _ = run_all(120)
    print(f"[{time.time()-t0:.1f}s] dps=120 done", flush=True)
    mp.mp.dps = 80

    agree = all([s["selected"] for s in res80[k][0]] == [s["selected"] for s in res120[k][0]]
                for k in res80)

    table = {}
    global_min_gap = None
    for key, (steps, gap) in res80.items():
        cset, cost, sname = key
        table.setdefault(cset, {}).setdefault(cost, {})[sname] = steps
        if gap is not None:
            global_min_gap = gap if global_min_gap is None else min(global_min_gap, gap)
        npass = sum(s["rule_T2_ns_passes"] for s in steps)
        print(f"\n== {cset} {cost} {sname}: rule passes {npass}/{len(steps)} steps")
        for s in steps:
            sel = " | ".join(s["selected"])
            print(f"  k={s['step']:2d} +{s['added']} (#{s['same_type_count']:2d}, n_s={s['shell_size']:2d})"
                  f"  → {sel}  idx={s['selected_torus_index']}"
                  f"  {'PASS' if s['rule_T2_ns_passes'] else 'fail'}"
                  f"  gap={s['gap_to_runner_up']}  min-cost-ties={s['n_candidates_at_min_cost']}")

    # Nucleon NFs, for the record
    nucl = {t: [mp.nstr(x, 30) for x in v] for t, v in nuc.items()}

    print(f"\n80 vs 120 dps selections agree: {agree}")
    print(f"smallest nonzero cost gap to runner-up: {mp.nstr(global_min_gap, 6)}")

    w = WitnessBuilder("nuclear-regime-shell-rule", engine="mpmath",
                       output_dir=Path(__file__).resolve().parent)
    w.set_description(
        "Re-measurement of the inductive inter-nucleon operator selection behind "
        "prop:nuclear-operator-regimes (Regime I shell rule, withdrawn). Legacy "
        "nucleon elements in H3(q), convention D, proton q0, mpmath 80/120 dps. "
        "Criteria pre-registered in docs/audits/2026-11-21-nuclear-regime-shell-rule.md §2.")
    w.set_content_block("prop:nuclear-operator-regimes")
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", mp.nstr(H.q, 60))
    w.add_parameter("convention", "D: z = q^3/(q^2+1)")
    w.add_parameter("z", mp.nstr(H.z, 60))
    w.add_parameter("dps", 80)
    w.add_parameter("crosscheck_dps", 120)
    w.add_parameter("shell_capacities", SHELL_CAPS)
    w.add_data("nucleon_nf", {"basis": NF_NAMES, **nucl})
    w.add_data("selection", table)
    w.add_data("dps_80_vs_120_selections_agree", agree)
    w.add_data("min_cost_gap_to_runner_up", mp.nstr(global_min_gap, 20))
    w.add_caveat("Nucleon elements are the legacy (σ₀σ₁⁻¹)³·typed-crossing construction of the "
                 "2026-04 producer, not γγ-selected; the model is the 2026-04 one, re-run honestly.")
    w.add_caveat("The selection LP per step is the vertex-selection LP over the simplex of candidates; "
                 "its duals are exact and recorded per step under lp_dual.")
    path = w.save()
    print(f"witness: {path}")


if __name__ == "__main__":
    main()
