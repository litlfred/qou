"""Term 4 two-arm report, carried to binding energy.

Information only. Writes no witness and changes no production value.

``term4_two_arm_dimq_probe`` gives Term 4 per A under three readings (production, hook arm,
sl₂ arm). This probe asks what a switch from production to another arm would do to a
binding energy B. The answer depends on how each consumer uses Term 4.

* **Canonical sweep** (``sweeps/paper_six_term_isotope_sweep.assemble_per_derivation_weights``):
  ``binding_T4 = m_e·(T4_atom − T4_free)``. Both calls go through ``paper_six_term_mass``,
  whose Term 4 is ``term4_frobenius_codim(Z + N)`` and does not read ``include_inter``. So
  ``T4_atom = T4_free`` and ``binding_T4 = 0`` under every arm. A switch moves the
  canonical B by exactly 0.
* **Additive consumers** (``mass_formula_6term`` per-3A row, ``unified_low_isotope_predictor``,
  ``d_from_scratch``): Term 4 is added to B once, undifferenced. A switch moves B by
  ``m_e·(arm − production)`` at that A.

No arm is chosen here, and the AME column is context only: selecting an arm by its
residual is fitting. The ruling is on issue #8109.
"""
import _path_bridge  # noqa: F401
from mpmath import mp

from term4_two_arm_dimq_probe import arms
from codata_constants import M_E_MEV  # noqa: E402  (sweep: M_E_MEV_DERIV = M_E_MEV)

mp.dps = 60
M_E = mp.mpf(str(M_E_MEV))

# AME2020 total binding energies (MeV), context only.
AME = {2: ("2H", "2.224566"), 3: ("3H", "8.481798"), 4: ("4He", "28.295673"),
       6: ("6Li", "31.993949"), 7: ("7Li", "39.244526"), 8: ("8Be", "56.499508")}


def main() -> None:
    print(f"m_e = {mp.nstr(M_E, 12)} MeV")
    print("Canonical sweep: binding_T4 = m_e*(T4(A) - T4(A)) = 0 under every arm.\n")
    print("Additive consumers: shift in B (MeV) if Term 4 switched from production")
    hdr = ("A", "T4 prod", "dB sl2", "dB hook", "isotope", "B_AME", "dB_sl2/B")
    print("{:<2} {:>12} {:>12} {:>12} {:>8} {:>10} {:>10}".format(*hdr))
    for A in range(1, 9):
        _, prod, hook, sl2, _ = arms(A)
        d_sl2 = M_E * (sl2 - prod)
        d_hook = M_E * (hook - prod)
        iso, b = AME.get(A, ("-", None))
        rel = f"{float(d_sl2 / mp.mpf(b)) * 100:+.2f}%" if b else "-"
        print(f"{A:<2} {mp.nstr(M_E * prod, 8):>12} {mp.nstr(d_sl2, 8):>12} "
              f"{mp.nstr(d_hook, 8):>12} {iso:>8} {b or '-':>10} {rel:>10}")


if __name__ == "__main__":
    main()
